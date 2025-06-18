#!/usr/bin/env python3
"""
Advanced Binary Analysis Tool - Comprehensive analysis and comparison of binary executables

This tool uses Radare2 and strace to extract detailed metrics from binary files and compares
multiple variants using radar charts and distance matrices. It provides insights into
instruction mix, syscall usage patterns, and structural similarity between binaries.

Adapted for CodeGenome Suite integration with interactive binary selection.
"""

import r2pipe
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess
import re
import signal
import os
import time
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from rich.console import Console
from rich.table import Table
from rich import box
import json

try:
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

# N-gram analysis support
try:
    from collections import Counter, defaultdict
except ImportError:
    pass

# Common syscall wrappers to detect during analysis
SYSCALL_WRAPPERS = {
    'open', 'read', 'write', 'close', 'execve', 'fork', 'socket',
    'connect', 'bind', 'listen', 'accept', 'kill', 'exit', 'wait',
    'waitpid', 'stat', 'fstat', 'lstat', 'poll', 'lseek', 'brk',
    'ioctl', 'access', 'pipe', 'dup', 'dup2', 'chdir', 'fchdir',
    'chmod', 'fchmod', 'chown', 'fchown', 'lchown', 'umask',
    'getpid', 'getuid', 'getgid', 'geteuid', 'getegid', 'setuid',
    'setgid', 'getppid', 'getpgrp', 'setsid', 'setreuid', 'setregid',
    'getgroups', 'setgroups', 'getpgid', 'getsid', 'prctl', 'getpriority',
    'setpriority', 'sched_yield', 'mlock', 'munlock', 'mlockall',
    'munlockall', 'sysinfo', 'times', 'ptrace', 'getrusage', 'getrlimit',
    'setrlimit', 'mmap', 'munmap', 'mprotect', 'nanosleep', 'getitimer',
    'alarm', 'setitimer', 'gettimeofday', 'unlink', 'symlink', 'readlink',
    'truncate', 'ftruncate', 'fsync', 'fdatasync', 'sync', 'pause',
    'mkdir', 'rmdir', 'creat', 'link', 'unlink', 'chroot', 'acct',
    'swapon', 'swapoff', 'reboot', 'sethostname', 'gethostname',
    # Add common libc functions that are syscall wrappers
    'puts', 'printf', 'scanf', 'malloc', 'free', 'fopen', 'fclose', 
    'fread', 'fwrite', 'gets', 'getchar', 'putchar'
}

# Instruction categories for analysis
INSTRUCTION_CATEGORIES = {
    'control_flow_ops': {'jmp', 'je', 'jne', 'jz', 'jnz', 'call', 'ret'},
    'data_movement_ops': {'mov', 'lea', 'push', 'pop'},
    'computational_ops': {'add', 'sub', 'mul', 'div', 'inc', 'dec',
                          'and', 'or', 'xor', 'shl', 'shr', 'cmp', 'test'},
    'memory_access_ops': {'mov', 'lea', 'push', 'pop', '['}  # Instructions involving memory access
}

# Analysis axis labels for radar charts and metrics display
ANALYSIS_AXES = [
    'Code Size', 'Control Flow', 'Data Movement',
    'Computational', 'Memory Access',
    'Function Diversity', 'Complexity', 'Total Syscalls'
]

@dataclass
class AdvancedBinaryMetrics:
    """Comprehensive binary analysis metrics"""
    # Basic properties
    file_path: str = ""
    file_size: int = 0
    
    # Function and instruction metrics
    total_functions: int = 0
    total_instructions: int = 0
    complexity: int = 0
    
    # Instruction categories
    control_flow_ops: int = 0
    data_movement_ops: int = 0
    computational_ops: int = 0
    memory_access_ops: int = 0
    stack_operations: int = 0
    
    # Heap operations
    heap_operations: Dict[str, int] = None
    
    # Syscalls
    syscalls: Dict[str, int] = None
    total_syscalls: int = 0
    syscall_sequence: List[str] = None
    syscall_ngrams: Dict[str, Dict[str, int]] = None
    
    # Instruction mix
    instruction_mix: Dict[str, int] = None
    
    # Function details
    function_details: Dict[str, Dict] = None
    
    def __post_init__(self):
        if self.heap_operations is None:
            self.heap_operations = {'malloc': 0, 'free': 0, 'realloc': 0}
        if self.syscalls is None:
            self.syscalls = {}
        if self.syscall_sequence is None:
            self.syscall_sequence = []
        if self.syscall_ngrams is None:
            self.syscall_ngrams = {'bigrams': {}, 'trigrams': {}}
        if self.instruction_mix is None:
            self.instruction_mix = {cat: 0 for cat in INSTRUCTION_CATEGORIES}
        if self.function_details is None:
            self.function_details = {}

class AdvancedBinaryAnalyzer:
    """Advanced binary analyzer with comprehensive metrics and visualization"""
    
    def __init__(self, console: Console, workspace: Path):
        self.console = console
        self.workspace = workspace
        
        # Create analysis output directory
        self.analysis_dir = workspace / "analysis_results"
        self.analysis_dir.mkdir(exist_ok=True)
        
        # Check if r2pipe is available
        try:
            import r2pipe
            self.r2pipe_available = True
        except ImportError:
            self.r2pipe_available = False
            self.console.print("[yellow]⚠️ r2pipe not available. Install with: pip install r2pipe[/yellow]")
    
    def safe_cmdj(self, r2, cmd):
        """Execute r2 command safely and return JSON result, returning empty list on failure."""
        try:
            result = r2.cmdj(cmd)
            return result if result is not None else []
        except Exception as e:
            # Try alternative approach for failed JSON commands
            try:
                # For disassembly commands, try without JSON first
                if 'pdj' in cmd:
                    plain_result = r2.cmd(cmd.replace('pdj', 'pd'))
                    if plain_result:
                        # Parse plain disassembly manually
                        return self._parse_plain_disassembly(plain_result)
                elif 'afbj' in cmd:
                    plain_result = r2.cmd(cmd.replace('afbj', 'afb'))
                    if plain_result:
                        return self._parse_plain_blocks(plain_result)
                # For other failed commands, return empty
                return []
            except:
                return []
    
    def _parse_plain_disassembly(self, plain_output: str) -> List[Dict]:
        """Parse plain disassembly output into instruction list"""
        instructions = []
        lines = plain_output.split('\n')
        
        # Common x86/x64 instructions
        common_instructions = {
            'mov', 'add', 'sub', 'mul', 'div', 'inc', 'dec', 'and', 'or', 'xor',
            'call', 'ret', 'jmp', 'je', 'jne', 'jz', 'jnz', 'jl', 'jg', 'jle', 'jge',
            'push', 'pop', 'lea', 'cmp', 'test', 'shl', 'shr', 'sal', 'sar',
            'nop', 'int', 'syscall', 'leave', 'enter'
        }
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';') or line.startswith('/'):
                continue
                
            # Remove radare2 formatting characters
            clean_line = line.replace('│', '').replace('└', '').replace('┌', '').strip()
            
            # Look for instruction lines (radare2 format: address spaces bytes spaces instruction)
            # Example: "0x000012ad      55             push rbp"
            if '0x' in clean_line:
                parts = clean_line.split()
                if len(parts) >= 3:
                    # Find instruction part after address and hex bytes
                    instruction_found = False
                    
                    # Skip address (0x...) and hex bytes, look for instruction
                    for i, part in enumerate(parts):
                        if i == 0:  # Skip address
                            continue
                        
                        part_lower = part.lower().rstrip(',')
                        if part_lower in common_instructions:
                            # Found instruction, take rest as full opcode
                            opcode = ' '.join(parts[i:])
                            instructions.append({'opcode': opcode})
                            instruction_found = True
                            break
                    
                    # If no standard instruction found, look for any alphabetic instruction after hex bytes
                    if not instruction_found:
                        for i, part in enumerate(parts[2:], 2):  # Skip address and first hex byte
                            if part.isalpha() and len(part) >= 2:
                                opcode = ' '.join(parts[i:])
                                instructions.append({'opcode': opcode})
                                break
        
        return instructions
    
    def _parse_plain_blocks(self, plain_output: str) -> List[Dict]:
        """Parse plain basic blocks output"""
        blocks = []
        lines = plain_output.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and '0x' in line:
                # Basic block entry
                blocks.append({'jump': -1})  # Simple placeholder
        
        return blocks
    
    def analyze_syscalls_with_strace(self, file_path: str, timeout: int = 20) -> Dict[str, Any]:
        """
        Run strace to collect syscall metrics and sequence.
        
        Args:
            file_path: Path to the binary to analyze
            timeout: Seconds to run the binary before interrupting
            
        Returns:
            Dictionary with syscall metrics including count and sequence
        """
        if not os.path.isabs(file_path) and not file_path.startswith("./"):
            file_path = "./" + file_path

        cmd = ["strace", "-f", "-s", "256", file_path]  # -f to follow forks, -s for string length
        syscall_sequence = []
        
        try:
            self.console.print(f"[blue]🔍 Running strace analysis on {os.path.basename(file_path)}...[/blue]")
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True)
            try:
                stdout, stderr = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.send_signal(signal.SIGINT)
                stdout, stderr = proc.communicate(timeout=10)
            
            output = stderr
            total_syscalls = 0
            syscall_counts = {}
            lines = output.splitlines()
            
            self.console.print(f"[green]✅ Processed {len(lines)} strace output lines[/green]")
            
            # Pattern to recognize syscalls
            syscall_pattern = re.compile(r'^(\d+\s+)?([a-zA-Z0-9_]+)\(')
            
            for line in lines:
                if not line.strip() or line.startswith("strace:") or line.startswith("%") or "------" in line:
                    continue
                
                match = syscall_pattern.match(line)
                if match:
                    syscall_name = match.group(2).strip()
                    if syscall_name in SYSCALL_WRAPPERS:
                        syscall_sequence.append(syscall_name)
                        syscall_counts[syscall_name] = syscall_counts.get(syscall_name, 0) + 1
                        total_syscalls += 1
            
            if syscall_sequence:
                self.console.print(f"[green]📊 Captured {total_syscalls} syscalls[/green]")
            
            return {
                'total_syscalls': total_syscalls, 
                'syscalls': syscall_counts,
                'syscall_sequence': syscall_sequence
            }
        except Exception as e:
            self.console.print(f"[red]❌ Strace analysis failed for {file_path}: {e}[/red]")
            return {'total_syscalls': 0, 'syscalls': {}, 'syscall_sequence': []}
    
    def generate_syscall_ngrams(self, syscall_sequence: List[str]) -> Dict[str, Dict[str, int]]:
        """
        Generate n-grams from syscall sequence for pattern analysis.
        
        Args:
            syscall_sequence: Ordered list of syscalls
            
        Returns:
            Dictionary with bigrams and trigrams counts
        """
        ngrams = {'bigrams': {}, 'trigrams': {}}
        
        if len(syscall_sequence) < 2:
            return ngrams
        
        # Generate bigrams
        for i in range(len(syscall_sequence) - 1):
            bigram = f"{syscall_sequence[i]}->{syscall_sequence[i+1]}"
            ngrams['bigrams'][bigram] = ngrams['bigrams'].get(bigram, 0) + 1
        
        # Generate trigrams
        if len(syscall_sequence) >= 3:
            for i in range(len(syscall_sequence) - 2):
                trigram = f"{syscall_sequence[i]}->{syscall_sequence[i+1]}->{syscall_sequence[i+2]}"
                ngrams['trigrams'][trigram] = ngrams['trigrams'].get(trigram, 0) + 1
        
        # Log top patterns
        if ngrams['bigrams']:
            top_bigrams = sorted(ngrams['bigrams'].items(), key=lambda x: x[1], reverse=True)[:5]
            self.console.print(f"[cyan]🔗 Top syscall bigrams: {', '.join([f'{bg}({c})' for bg, c in top_bigrams])}[/cyan]")
        
        if ngrams['trigrams']:
            top_trigrams = sorted(ngrams['trigrams'].items(), key=lambda x: x[1], reverse=True)[:3]
            self.console.print(f"[cyan]🔗 Top syscall trigrams: {', '.join([f'{tg}({c})' for tg, c in top_trigrams])}[/cyan]")
        
        return ngrams
    
    def analyze_with_radare2(self, file_path: str, use_strace: bool = False) -> AdvancedBinaryMetrics:
        """
        Analyze binary using Radare2 and optionally strace.
        
        Args:
            file_path: Path to the binary to analyze
            use_strace: Whether to use strace for dynamic analysis
            
        Returns:
            AdvancedBinaryMetrics with comprehensive analysis results
        """
        if not self.r2pipe_available:
            self.console.print("[red]❌ r2pipe not available for advanced analysis[/red]")
            return AdvancedBinaryMetrics(file_path=file_path)
        
        # Get file size
        try:
            file_size = os.path.getsize(file_path)
        except:
            file_size = 0
        
        metrics = AdvancedBinaryMetrics(
            file_path=file_path,
            file_size=file_size,
            heap_operations={'malloc': 0, 'free': 0, 'realloc': 0},
            syscalls={},
            syscall_sequence=[],
            syscall_ngrams={'bigrams': {}, 'trigrams': {}},
            instruction_mix={cat: 0 for cat in INSTRUCTION_CATEGORIES},
            function_details={}
        )
        
        try:
            r2 = r2pipe.open(file_path)
            r2.cmd('e bin.relocs.apply=true')
            r2.cmd('e bin.cache=true')
            r2.cmd('aaaa')  # Perform deep analysis
            
            # Enhanced static syscall analysis
            if not use_strace:
                self.console.print(f"[blue]🔍 Analyzing static syscall references...[/blue]")
                
                # Get imports and symbols
                imports = self.safe_cmdj(r2, 'ii')
                symbols = self.safe_cmdj(r2, 'isj')
                
                # Combine imports and symbols for comprehensive analysis
                all_refs = []
                if imports:
                    all_refs.extend(imports)
                if symbols:
                    # Filter for imported symbols when imports command fails
                    imported_symbols = [s for s in symbols if s.get('is_imported', False) or 'imp.' in s.get('name', '')]
                    all_refs.extend(imported_symbols)
                
                self.console.print(f"[blue]🔍 Found {len(all_refs)} import/symbol references to analyze[/blue]")
                
                # Enhanced syscall detection
                syscall_refs = {}
                for ref in all_refs:
                    original_name = ref.get('name', '')
                    name = original_name.lower()
                    
                    # Clean up symbol names (remove prefixes and suffixes)
                    clean_names = [
                        name.split('@')[0].lstrip('_').split('.')[0],
                        name.replace('plt', '').replace('got', '').strip('._'),
                        name.split('@@')[0],  # Handle versioned symbols
                        name.replace('sym.imp.', '').replace('sym.', ''),  # Handle radare2 prefixes
                        name.replace('fcn.', '').replace('entry.', ''),
                        name.replace('imp.', '')  # Handle imp. prefix directly
                    ]
                    
                    for clean_name in clean_names:
                        if clean_name in SYSCALL_WRAPPERS:
                            syscall_refs[original_name] = clean_name
                            self.console.print(f"[green]✓ Found syscall: {original_name} -> {clean_name}[/green]")
                            break
                
                # Additional detection: check for common libc functions that are syscall wrappers
                libc_wrappers = {'printf', 'scanf', 'malloc', 'free', 'exit', 'puts', 'gets', 'fopen', 'fclose', 'fread', 'fwrite'}
                for ref in all_refs:
                    name = ref.get('name', '').lower()
                    clean_name = name.split('@')[0].lstrip('_').split('.')[0].replace('sym.imp.', '').replace('sym.', '')
                    if clean_name in libc_wrappers:
                        syscall_refs[ref.get('name', '')] = clean_name
                        self.console.print(f"[green]✓ Found libc wrapper: {ref.get('name', '')} -> {clean_name}[/green]")
                
                # Count references for each detected syscall
                for ref_name, clean_name in syscall_refs.items():
                    try:
                        # Try multiple reference counting approaches
                        count = 0
                        
                        # Method 1: Direct cross-references using symbol address
                        try:
                            addr_result = r2.cmd(f'f~{ref_name}$')
                            if addr_result.strip():
                                addr = addr_result.split()[0]
                                xrefs = self.safe_cmdj(r2, f'axtj @ {addr}')
                                if xrefs:
                                    count += len([x for x in xrefs if x.get('type') in ['CALL', 'call']])
                        except:
                            pass
                        
                        # Method 2: Simple presence check - if we detected it, assume at least 1 usage
                        if count == 0:
                            count = 1  # Conservative estimate
                        
                        # Method 3: Look for the symbol name in all disassembly
                        if count <= 1:
                            try:
                                # Count occurrences in all function disassembly
                                all_disasm = r2.cmd('pdf @@f')
                                symbol_mentions = all_disasm.lower().count(clean_name.lower())
                                if symbol_mentions > count:
                                    count = symbol_mentions
                            except:
                                pass
                        
                        if count > 0:
                            metrics.syscalls[clean_name] = metrics.syscalls.get(clean_name, 0) + count
                            metrics.total_syscalls += count
                            self.console.print(f"[cyan]📊 {clean_name}: {count} references[/cyan]")
                            
                    except Exception as e:
                        self.console.print(f"[yellow]⚠️ Error analyzing {ref_name}: {str(e)[:50]}[/yellow]")
                        continue
                
                if metrics.total_syscalls > 0:
                    self.console.print(f"[green]📊 Static analysis found {metrics.total_syscalls} syscall references[/green]")
                else:
                    self.console.print(f"[yellow]⚠️ No syscalls detected in static analysis[/yellow]")

            # Function and instruction analysis - try multiple approaches
            functions = self.safe_cmdj(r2, 'aflj')
            
            # If JSON fails, try plain text approach
            if not functions:
                try:
                    func_output = r2.cmd('afl')
                    func_lines = [line.strip() for line in func_output.split('\n') if line.strip()]
                    functions = []
                    for line in func_lines:
                        if 'sym.' in line and not line.startswith('sym.imp.'):
                            parts = line.split()
                            if len(parts) >= 3:
                                try:
                                    offset = int(parts[0], 16)
                                    name = parts[-1]
                                    functions.append({'name': name, 'offset': offset})
                                except:
                                    continue
                except:
                    functions = []
            else:
                # Filter out import functions and include main and other non-sym functions
                functions = [f for f in functions if not f.get('name', '').startswith('sym.imp.')]
            
            # Debug: print function count
            self.console.print(f"[green]🔍 Found {len(functions)} functions to analyze[/green]")
            
            metrics.total_functions = len(functions)

            for func in functions:
                fname = func.get('name', 'unknown')
                func_offset = func.get('offset', 0) or func.get('addr', 0)
                
                if not func_offset:
                    self.console.print(f"[yellow]⚠️ Skipping {fname}: no offset[/yellow]")
                    continue
                    
                metrics.function_details[fname] = {
                    'instructions': 0,
                    'calls': []
                }
                
                self.console.print(f"[blue]  Analyzing function: {fname} @ 0x{func_offset:x}[/blue]")
                
                try:
                    # Calculate cyclomatic complexity for each function
                    bblocks = self.safe_cmdj(r2, f'afbj @ {func_offset}')
                    if bblocks:
                        edges = sum(1 for b in bblocks if b.get('jump', -1) != -1)
                        nodes = len(bblocks)
                        complexity = edges - nodes + 2
                        metrics.complexity += max(complexity, 0)

                    # Use plain text disassembly directly (more reliable than JSON)
                    insts = []
                    try:
                        plain_disasm = r2.cmd(f'pdf @ {func_offset}')
                        if plain_disasm:
                            insts = self._parse_plain_disassembly(plain_disasm)
                    except Exception as e:
                        # Fallback to JSON if plain fails
                        insts = self.safe_cmdj(r2, f'pdfj @ {func_offset}')
                        if not insts:
                            insts = self.safe_cmdj(r2, f'pdj @ {func_offset}')
                    
                    if not insts:
                        continue

                    valid_insts = [i for i in insts if 'opcode' in i]
                    count = len(valid_insts)
                    metrics.function_details[fname]['instructions'] = count
                    metrics.total_instructions += count

                    # Categorize instructions
                    for inst in valid_insts:
                        opcode = inst.get('opcode', '')
                        if not opcode:
                            continue
                            
                        op = opcode.split()[0].lower()
                        ops = opcode.lower()

                        for cat_name, ops_list in INSTRUCTION_CATEGORIES.items():
                            for instr_op in ops_list:
                                if instr_op in ops:
                                    metrics.instruction_mix[cat_name] += 1
                                    break  # Avoid double counting

                        # Check for heap operations
                        if op == 'call':
                            target = ' '.join(opcode.split()[1:]).lower()
                            for heap_op in ['malloc', 'free', 'realloc']:
                                if heap_op in target:
                                    metrics.heap_operations[heap_op] += 1

                except Exception as e:
                    self.console.print(f"[yellow]⚠️ Error processing function {fname}: {str(e)}[/yellow]")

            # Dynamic analysis with strace if requested
            if use_strace:
                self.console.print(f"[cyan]🔍 Performing dynamic analysis with strace...[/cyan]")
                syscall_metrics = self.analyze_syscalls_with_strace(file_path)
                metrics.total_syscalls = syscall_metrics.get('total_syscalls', 0)
                metrics.syscalls = syscall_metrics.get('syscalls', {})
                metrics.syscall_sequence = syscall_metrics.get('syscall_sequence', [])
                
                # Generate n-grams from syscall sequence
                if metrics.syscall_sequence:
                    self.console.print(f"[cyan]🔗 Generating syscall n-gram patterns...[/cyan]")
                    metrics.syscall_ngrams = self.generate_syscall_ngrams(metrics.syscall_sequence)

        except Exception as e:
            self.console.print(f"[red]❌ R2 analysis failed: {e}[/red]")
        finally:
            try:
                r2.quit()
            except:
                pass

        return metrics
    
    def get_radar_metrics(self, metrics: AdvancedBinaryMetrics) -> List[float]:
        """
        Extract normalized metrics for radar chart visualization.
        
        Args:
            metrics: AdvancedBinaryMetrics object
            
        Returns:
            List of metrics for radar chart
        """
        total_inst = metrics.total_instructions
        
        return [
            total_inst,  # Code Size
            (metrics.instruction_mix['control_flow_ops'] / total_inst * 100) if total_inst > 0 else 0,
            (metrics.instruction_mix['data_movement_ops'] / total_inst * 100) if total_inst > 0 else 0,
            (metrics.instruction_mix['computational_ops'] / total_inst * 100) if total_inst > 0 else 0,
            (metrics.instruction_mix['memory_access_ops'] / total_inst * 100) if total_inst > 0 else 0,
            metrics.total_functions,
            metrics.complexity,
            metrics.total_syscalls
        ]
    
    def normalize_multiple_metrics(self, metrics_list: List[List[float]]) -> List[List[float]]:
        """
        Normalize metrics for fair comparison.
        
        Args:
            metrics_list: List of metrics vectors
            
        Returns:
            List of normalized metrics vectors
        """
        num_metrics = len(metrics_list[0])
        max_vals = [max(metrics[i] for metrics in metrics_list) or 1 for i in range(num_metrics)]
        
        return [
            [m / max_val for m, max_val in zip(metrics, max_vals)]
            for metrics in metrics_list
        ]
    
    def plot_radar_comparison(self, metrics_list: List[List[float]], axis_labels: List[str], 
                             legend_labels: List[str], output_file: str = "radar_comparison.png") -> str:
        """
        Generate radar chart comparing multiple binaries.
        
        Args:
            metrics_list: List of normalized metrics vectors
            axis_labels: Labels for each axis
            legend_labels: Labels for each binary
            output_file: Path to save the generated chart
            
        Returns:
            Path to the generated chart file
        """
        try:
            num_vars = len(axis_labels)
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            angles += angles[:1]  # Close the loop

            fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'polar': True})
            
            colors = plt.cm.Set3(np.linspace(0, 1, len(legend_labels)))
            
            for i, (data, legend) in enumerate(zip(metrics_list, legend_labels)):
                data = np.concatenate((data, data[:1]))  # Close the loop
                ax.plot(angles, data, label=legend, linewidth=2, color=colors[i])
                ax.fill(angles, data, alpha=0.25, color=colors[i])

            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(axis_labels)
            ax.set_yticklabels([])
            plt.title('Advanced Binary Comparison Analysis', pad=20, fontsize=16)
            plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1.1))
            plt.tight_layout()
            
            full_output_path = self.analysis_dir / output_file
            plt.savefig(full_output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            return str(full_output_path)
        except Exception as e:
            self.console.print(f"[red]❌ Radar chart generation failed: {e}[/red]")
            return ""
    
    def print_detailed_metrics(self, metrics: AdvancedBinaryMetrics):
        """Display formatted detailed metrics for a binary."""
        self.console.print(f"\n[bold cyan]📊 Detailed Analysis: {os.path.basename(metrics.file_path)}[/bold cyan]")
        
        # General metrics table
        general_table = Table(title="General Metrics", box=box.ROUNDED)
        general_table.add_column("Metric", style="cyan")
        general_table.add_column("Value", style="green")
        
        general_table.add_row("File Size", f"{metrics.file_size:,} bytes")
        general_table.add_row("Total Functions", f"{metrics.total_functions:,}")
        general_table.add_row("Total Instructions", f"{metrics.total_instructions:,}")
        general_table.add_row("Cyclomatic Complexity", f"{metrics.complexity:,}")
        
        self.console.print(general_table)
        
        # Instruction distribution table
        if metrics.total_instructions > 0:
            inst_table = Table(title="Instruction Distribution", box=box.ROUNDED)
            inst_table.add_column("Category", style="yellow")
            inst_table.add_column("Count", style="green")
            inst_table.add_column("Percentage", style="cyan")
            
            total = metrics.total_instructions
            for category, count in metrics.instruction_mix.items():
                readable_cat = category.replace('_ops', '').replace('_', ' ').title()
                percentage = (count/total*100)
                inst_table.add_row(readable_cat, f"{count:,}", f"{percentage:.2f}%")
            
            self.console.print(inst_table)
        
        # Syscalls table
        if metrics.syscalls:
            syscall_table = Table(title="Top System Calls", box=box.ROUNDED)
            syscall_table.add_column("Syscall", style="magenta")
            syscall_table.add_column("Count", style="green")
            
            top_syscalls = sorted(metrics.syscalls.items(), key=lambda x: x[1], reverse=True)[:10]
            for syscall, count in top_syscalls:
                syscall_table.add_row(syscall, f"{count:,}")
            
            self.console.print(syscall_table)
        
        # Syscall n-grams analysis
        if metrics.syscall_ngrams and (metrics.syscall_ngrams.get('bigrams') or metrics.syscall_ngrams.get('trigrams')):
            if metrics.syscall_ngrams.get('bigrams'):
                bigram_table = Table(title="Top Syscall Bigrams", box=box.ROUNDED)
                bigram_table.add_column("Bigram Pattern", style="magenta")
                bigram_table.add_column("Count", style="green")
                
                top_bigrams = sorted(metrics.syscall_ngrams['bigrams'].items(), key=lambda x: x[1], reverse=True)[:8]
                for bigram, count in top_bigrams:
                    bigram_table.add_row(bigram, f"{count:,}")
                
                self.console.print(bigram_table)
            
            if metrics.syscall_ngrams.get('trigrams'):
                trigram_table = Table(title="Top Syscall Trigrams", box=box.ROUNDED)
                trigram_table.add_column("Trigram Pattern", style="magenta")
                trigram_table.add_column("Count", style="green")
                
                top_trigrams = sorted(metrics.syscall_ngrams['trigrams'].items(), key=lambda x: x[1], reverse=True)[:5]
                for trigram, count in top_trigrams:
                    trigram_table.add_row(trigram, f"{count:,}")
                
                self.console.print(trigram_table)
        
        # Heap operations
        heap_total = sum(metrics.heap_operations.values())
        if heap_total > 0:
            heap_table = Table(title="Heap Operations", box=box.ROUNDED)
            heap_table.add_column("Operation", style="red")
            heap_table.add_column("Count", style="green")
            
            for op, count in metrics.heap_operations.items():
                if count > 0:
                    heap_table.add_row(op, f"{count:,}")
            
            self.console.print(heap_table)
    
    def calculate_distance_matrix_euclidean(self, metrics_list: List[List[float]]) -> List[List[float]]:
        """Calculate pairwise Euclidean distance matrix."""
        n = len(metrics_list)
        distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                diff = np.array(metrics_list[i]) - np.array(metrics_list[j])
                dist = np.sqrt(np.sum(diff ** 2))
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist
                
        return distance_matrix
    
    def calculate_distance_matrix_cosine(self, normalized_metrics_list: List[List[float]]) -> List[List[float]]:
        """Calculate pairwise Cosine distance matrix."""
        if not SKLEARN_AVAILABLE:
            self.console.print("[yellow]⚠️ sklearn not available for cosine similarity[/yellow]")
            return self.calculate_distance_matrix_euclidean(normalized_metrics_list)
        
        n = len(normalized_metrics_list)
        distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                vec1 = np.array(normalized_metrics_list[i]).reshape(1, -1)
                vec2 = np.array(normalized_metrics_list[j]).reshape(1, -1)
                # Cosine distance is 1 - cosine similarity
                dist = 1 - cosine_similarity(vec1, vec2)[0][0]
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist
                
        return distance_matrix
    
    def print_distance_matrix(self, distance_matrix: List[List[float]], legend_labels: List[str], matrix_type: str):
        """Print distance matrix in a formatted table."""
        self.console.print(f"\n[bold yellow]{matrix_type} Distance Matrix[/bold yellow]")
        
        table = Table(box=box.ROUNDED)
        table.add_column("Binary", style="cyan")
        
        for label in legend_labels:
            table.add_column(label[:12], style="green")
        
        for i, row in enumerate(distance_matrix):
            row_data = [legend_labels[i][:20]] + [f"{d:.6f}" for d in row]
            table.add_row(*row_data)
        
        self.console.print(table)
    
    def save_analysis_report(self, all_metrics: List[AdvancedBinaryMetrics], 
                            all_radar_metrics: List[List[float]], 
                            legend_labels: List[str], 
                            output_path: str) -> bool:
        """Save comprehensive analysis report as JSON"""
        try:
            report_data = {
                'analysis_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'total_binaries_analyzed': len(all_metrics),
                'binaries': {},
                'comparison_matrices': {},
                'radar_metrics': {}
            }
            
            # Add detailed metrics for each binary
            for i, (metrics, label) in enumerate(zip(all_metrics, legend_labels)):
                report_data['binaries'][label] = {
                    'file_path': metrics.file_path,
                    'file_size': metrics.file_size,
                    'total_functions': metrics.total_functions,
                    'total_instructions': metrics.total_instructions,
                    'complexity': metrics.complexity,
                    'instruction_mix': metrics.instruction_mix,
                    'syscalls': metrics.syscalls,
                    'total_syscalls': metrics.total_syscalls,
                    'syscall_sequence': metrics.syscall_sequence,
                    'syscall_ngrams': metrics.syscall_ngrams,
                    'heap_operations': metrics.heap_operations,
                    'radar_metrics': all_radar_metrics[i]
                }
            
            # Save to JSON
            with open(output_path, 'w') as f:
                json.dump(report_data, f, indent=2, default=str)
            
            self.console.print(f"[green]📄 Comprehensive analysis report saved to: {output_path}[/green]")
            return True
            
        except Exception as e:
            self.console.print(f"[red]❌ Failed to save analysis report: {e}[/red]")
            return False
    
    def analyze_multiple_binaries_advanced(self, binary_paths: List[str], use_strace: bool = False) -> Tuple[List[AdvancedBinaryMetrics], str]:
        """
        Perform comprehensive analysis of multiple binaries with visualization
        
        Args:
            binary_paths: List of binary file paths to analyze
            use_strace: Whether to use dynamic analysis with strace
            
        Returns:
            Tuple of (metrics_list, radar_chart_path)
        """
        self.console.print(f"\n[bold cyan]🔍 Advanced Binary Analysis[/bold cyan]")
        self.console.print(f"[blue]📊 Analyzing {len(binary_paths)} binaries...[/blue]")
        self.console.print(f"[blue]🔬 Dynamic analysis: {'Enabled' if use_strace else 'Disabled'}[/blue]")
        
        all_metrics = []
        all_radar_metrics = []
        legend_labels = []
        
        # Analyze each binary
        for i, binary_path in enumerate(binary_paths, 1):
            binary_name = os.path.basename(binary_path)
            self.console.print(f"\n[yellow]  [{i}/{len(binary_paths)}] Analyzing {binary_name}...[/yellow]")
            
            try:
                metrics = self.analyze_with_radare2(binary_path, use_strace=use_strace)
                radar_metrics = self.get_radar_metrics(metrics)
                
                all_metrics.append(metrics)
                all_radar_metrics.append(radar_metrics)
                legend_labels.append(binary_name)
                
                self.print_detailed_metrics(metrics)
                
            except Exception as e:
                self.console.print(f"[red]❌ Failed to analyze {binary_name}: {e}[/red]")
                continue
        
        if len(all_metrics) < 2:
            self.console.print("[yellow]⚠️ Need at least 2 successfully analyzed binaries for comparison[/yellow]")
            return all_metrics, ""
        
        # Generate comparison visualization
        try:
            self.console.print(f"\n[cyan]📊 Generating comparison visualization...[/cyan]")
            
            # Normalize metrics for radar chart
            norm_metrics = self.normalize_multiple_metrics(all_radar_metrics)
            
            # Generate radar chart
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            radar_file = f"advanced_radar_comparison_{timestamp}.png"
            radar_path = self.plot_radar_comparison(norm_metrics, ANALYSIS_AXES, legend_labels, radar_file)
            
            if radar_path:
                self.console.print(f"[green]🎯 Radar chart saved: {radar_path}[/green]")
            
            # Calculate and display distance matrices
            self.console.print(f"\n[cyan]📏 Calculating similarity matrices...[/cyan]")
            
            euclidean_matrix = self.calculate_distance_matrix_euclidean(norm_metrics)
            cosine_matrix = self.calculate_distance_matrix_cosine(norm_metrics)
            
            self.print_distance_matrix(euclidean_matrix, legend_labels, "EUCLIDEAN")
            self.print_distance_matrix(cosine_matrix, legend_labels, "COSINE")
            
            # Save comprehensive report
            report_path = self.analysis_dir / f"advanced_analysis_report_{timestamp}.json"
            self.save_analysis_report(all_metrics, all_radar_metrics, legend_labels, str(report_path))
            
            return all_metrics, radar_path
            
        except Exception as e:
            self.console.print(f"[red]❌ Comparison analysis failed: {e}[/red]")
            return all_metrics, ""