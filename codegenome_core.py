#!/usr/bin/env python3
"""
CodeGenome Suite - Advanced Binary Analysis and AI-Powered Variant Generation

A comprehensive suite for binary analysis and intelligent code variant generation.
"""

import asyncio
import json
import os
import subprocess
import sys
import tempfile
import time
import uuid
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime

# Core libraries
import questionary
import requests
import toml
import pyfiglet
from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.layout import Layout
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich import box

# Configuration and data models
from pydantic import BaseModel, Field
from enum import Enum

# Import enhanced AI system
try:
    from ai_engine import EnhancedAgenticSystem
    ENHANCED_AI_AVAILABLE = True
except ImportError:
    ENHANCED_AI_AVAILABLE = False

# Import binary analyzer
try:
    from binary_analyzer import BinaryAnalyzer
    BINARY_ANALYZER_AVAILABLE = True
except ImportError:
    BINARY_ANALYZER_AVAILABLE = False

# Import advanced binary analyzer
try:
    from advanced_binary_analyzer import AdvancedBinaryAnalyzer
    ADVANCED_ANALYZER_AVAILABLE = True
except ImportError:
    ADVANCED_ANALYZER_AVAILABLE = False


class VariantType(Enum):
    """Types of variants that can be generated"""
    METAME = "metame"
    AI_GENERATED = "ai_generated"
    SOURCE_ORIGINAL = "source_original"


class SuiteConfig(BaseModel):
    """Main configuration for the entire suite"""
    workspace_dir: str = "workspace"
    metame_path: str = ""
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "gemma3:12b"
    log_level: str = "INFO"


@dataclass
class VariantInfo:
    """Information about a generated variant"""
    id: str
    name: str
    path: str
    variant_type: VariantType
    generation_time: datetime
    metadata: Dict[str, Any]


class AgenticLLM:
    """Agentic LLM that can write files, read files, and execute Python scripts"""
    
    def __init__(self, config: SuiteConfig, console: Console, workspace: Path):
        self.config = config
        self.console = console
        self.workspace = workspace
        self.conversation_history = []
        
        # Initialize enhanced AI system if available
        if ENHANCED_AI_AVAILABLE:
            self.enhanced_system = EnhancedAgenticSystem(config, console, workspace)
        else:
            self.enhanced_system = None
        
    def check_ollama_connection(self) -> bool:
        """Check if Ollama is running and model is available"""
        try:
            response = requests.get(f"{self.config.ollama_base_url}/api/version", timeout=5)
            if response.status_code != 200:
                return False
                
            # Check if model is available
            response = requests.get(f"{self.config.ollama_base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get("models", [])
                return any(model["name"].startswith(self.config.ollama_model) for model in models)
        except:
            pass
        return False
    
    def pull_model_if_needed(self) -> bool:
        """Pull model if not available"""
        try:
            self.console.print(f"[yellow]📥 Pulling model {self.config.ollama_model}...[/yellow]")
            response = requests.post(
                f"{self.config.ollama_base_url}/api/pull",
                json={"name": self.config.ollama_model},
                timeout=300
            )
            return response.status_code == 200
        except Exception as e:
            self.console.print(f"[red]❌ Failed to pull model: {e}[/red]")
            return False
    
    def _call_llm(self, prompt: str, system_prompt: str = "") -> str:
        """Call LLM with given prompt"""
        
        full_prompt = prompt
        
        try:
            response = requests.post(
                f"{self.config.ollama_base_url}/api/generate",
                json={
                    "model": self.config.ollama_model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 4096
                    }
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "").strip()
                
        except Exception as e:
            self.console.print(f"[red]❌ LLM call failed: {e}[/red]")
            
        return ""
    
    def write_file(self, path: str, content: str) -> bool:
        """Write content to file"""
        try:
            file_path = self.workspace / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            self.console.print(f"[green]📝 Wrote file: {path}[/green]")
            return True
        except Exception as e:
            self.console.print(f"[red]❌ Failed to write {path}: {e}[/red]")
            return False
    
    def read_file(self, path: str) -> str:
        """Read content from file"""
        try:
            file_path = self.workspace / path
            content = file_path.read_text()
            self.console.print(f"[blue]📖 Read file: {path}[/blue]")
            return content
        except Exception as e:
            self.console.print(f"[red]❌ Failed to read {path}: {e}[/red]")
            return ""
    
    def execute_python(self, code: str) -> Tuple[bool, str]:
        """Execute Python code and return result"""
        try:
            # Create temporary Python file
            temp_file = self.workspace / f"temp_script_{uuid.uuid4().hex[:8]}.py"
            temp_file.write_text(code)
            
            # Execute in workspace directory
            result = subprocess.run(
                [sys.executable, str(temp_file)],
                cwd=str(self.workspace),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Clean up
            temp_file.unlink(missing_ok=True)
            
            output = result.stdout + result.stderr
            success = result.returncode == 0
            
            if success:
                self.console.print(f"[green]🐍 Python execution successful[/green]")
            else:
                self.console.print(f"[red]❌ Python execution failed: {output}[/red]")
            
            return success, output
            
        except Exception as e:
            self.console.print(f"[red]❌ Python execution error: {e}[/red]")
            return False, str(e)
    
    def compile_c(self, source_path: str, binary_path: str) -> bool:
        """Compile C source to binary"""
        try:
            src_path = self.workspace / source_path
            bin_path = self.workspace / binary_path
            
            # Ensure source file exists
            if not src_path.exists():
                self.console.print(f"[red]❌ Source file not found: {src_path}[/red]")
                return False
            
            result = subprocess.run(
                ["gcc", "-o", binary_path, source_path, "-std=c99", "-Wall"],
                cwd=str(self.workspace),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.console.print(f"[green]⚙️ Compiled: {source_path} → {binary_path}[/green]")
                return True
            else:
                self.console.print(f"[red]❌ Compilation failed: {result.stderr}[/red]")
                return False
                
        except Exception as e:
            self.console.print(f"[red]❌ Compilation error: {e}[/red]")
            return False
    
    def run_executable(self, path: str, args: List[str] = None) -> Tuple[bool, str]:
        """Run executable and return result"""
        try:
            exe_path = self.workspace / path
            if args is None:
                args = []
                
            result = subprocess.run(
                [f"./{path}"] + args,
                cwd=str(self.workspace),
                capture_output=True,
                text=True,
                timeout=10
            )
            
            output = result.stdout + result.stderr
            success = result.returncode == 0
            
            if success:
                self.console.print(f"[green]🚀 Executed: {path}[/green]")
            else:
                self.console.print(f"[yellow]⚠️ Execution returned {result.returncode}: {path}[/yellow]")
            
            return success, output
            
        except Exception as e:
            self.console.print(f"[red]❌ Execution error: {e}[/red]")
            return False, str(e)
    
    def parse_llm_response(self, response: str) -> Tuple[str, str, str]:
        """Parse LLM response into thought, action, and action_input"""
        thought = ""
        action = ""
        action_input = ""
        
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith("THOUGHT:"):
                current_section = "thought"
                thought = line_stripped[8:].strip()
            elif line_stripped.startswith("ACTION:"):
                current_section = "action"
                action = line_stripped[7:].strip()
            elif line_stripped.startswith("ACTION_INPUT:"):
                current_section = "action_input"
                action_input = line_stripped[13:].strip()
            elif current_section == "thought" and line_stripped:
                thought += " " + line_stripped
            elif current_section == "action_input":
                # For action_input, preserve the original line formatting
                if action_input:
                    action_input += "\n" + line
                else:
                    action_input = line
        
        # Clean up and validate
        action = action.lower().strip()
        if action not in ["write_file", "read_file", "compile_c", "run_executable", "execute_python"]:
            # Try to find a valid action in the response
            for valid_action in ["write_file", "compile_c", "run_executable"]:
                if valid_action in response.lower():
                    action = valid_action
                    break
        
        return thought, action, action_input
    
    def execute_action(self, action: str, action_input: str) -> Tuple[bool, str]:
        """Execute the action specified by LLM"""
        
        if action == "write_file":
            # Parse path and content from action_input
            lines = action_input.split('\n', 1)
            if len(lines) >= 1:
                path = lines[0].strip()
                content = lines[1] if len(lines) > 1 else ""
                
                # Clean up content - remove code block markers
                if content.startswith('```c'):
                    content = content[4:]
                if content.startswith('```'):
                    content = content[3:]
                if content.endswith('```'):
                    content = content[:-3]
                content = content.strip()
                
                # Ensure path is valid
                if not path or path.lower() in ['none', 'null', ''] or len(path) > 100 or '/' in path:
                    return False, f"Invalid file path: {path}"
                return self.write_file(path, content), ""
            else:
                return False, "Invalid write_file format"
                
        elif action == "read_file":
            path = action_input.strip()
            # Ensure path is valid
            if not path or path.lower() in ['none', 'null', ''] or len(path) > 100 or '/' in path:
                return False, f"Invalid file path: {path}"
            content = self.read_file(path)
            return bool(content), content
            
        elif action == "execute_python":
            return self.execute_python(action_input)
            
        elif action == "compile_c":
            parts = action_input.split()
            if len(parts) >= 2:
                return self.compile_c(parts[0], parts[1]), ""
            else:
                return False, "Invalid compile_c format"
                
        elif action == "run_executable":
            parts = action_input.split()
            if parts:
                exe_path = parts[0]
                args = parts[1:] if len(parts) > 1 else []
                return self.run_executable(exe_path, args)
            else:
                return False, "Invalid run_executable format"
        
        return False, f"Unknown action: {action}"
    
    def generate_variants_from_source(self, source_path: str, num_variants: int = 3) -> List[VariantInfo]:
        """Generate code variants from source file using enhanced AI system"""
        
        variants = []
        
        # Use enhanced system if available
        if self.enhanced_system and ENHANCED_AI_AVAILABLE:
            # Start performance monitoring
            self.enhanced_system.performance_monitor.start_generation_session(num_variants)
            
            self.console.print(f"[blue]🤖 Generating {num_variants} enhanced AI variants from {source_path}...[/blue]")
            self.console.print("[cyan]🔧 Using advanced transformation strategies for maximum binary differentiation[/cyan]")
            
            for i in range(num_variants):
                self.console.print(f"\n[bold]--- Generating Enhanced Variant {i+1}/{num_variants} ---[/bold]")
                
                # Use enhanced system to generate and validate variant with metrics
                variant_result, metrics = self.enhanced_system.generate_enhanced_variant_with_metrics(source_path, i+1)
                
                # Add metrics to performance monitor
                if metrics:
                    self.enhanced_system.performance_monitor.add_variant_metrics(metrics)
                
                if variant_result:
                    # Create VariantInfo object compatible with existing system
                    variant_info = VariantInfo(
                        id=variant_result['variant_id'],
                        name=f"Enhanced AI Variant {i+1}",
                        path=variant_result['binary_path'],
                        variant_type=VariantType.AI_GENERATED,
                        generation_time=datetime.now(),
                        metadata={
                            "source_file": variant_result['source_path'],
                            "model": self.config.ollama_model,
                            "validation_results": variant_result['validation_results'],
                            "test_cases_count": variant_result['test_cases'],
                            "test_suite_path": variant_result['test_suite_path'],
                            "enhanced_generation": True,
                            "transformation_strategies": "advanced_multi_strategy"
                        }
                    )
                    
                    variants.append(variant_info)
                    self.console.print(f"[green]✅ Successfully generated and validated variant {i+1}[/green]")
                    
                    # Show validation summary
                    validation = variant_result['validation_results']
                    self.console.print(f"[blue]📊 Validation: {validation['passed_tests']}/{validation['total_tests']} tests passed[/blue]")
                else:
                    self.console.print(f"[red]❌ Failed to generate enhanced variant {i+1}[/red]")
            
            # End performance monitoring and display summary
            self.enhanced_system.performance_monitor.end_generation_session()
            
            return variants
        
        # Fallback to original method if enhanced system not available
        if not self.check_ollama_connection():
            if not self.pull_model_if_needed():
                self.console.print("[red]❌ Cannot connect to Ollama or pull model[/red]")
                return variants
        
        self.console.print(f"[blue]🤖 Generating {num_variants} AI variants from {source_path}...[/blue]")
        self.console.print("[yellow]⚠️ Enhanced system not available, using basic generation[/yellow]")
        
        # Read source code
        source_content = self.read_file(source_path)
        if not source_content:
            return variants
        
        for i in range(num_variants):
            # Generate meaningful variant name based on source file
            source_name = Path(source_path).stem
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            variant_id = f"{source_name}_ai_v{i+1:02d}_{timestamp}"
            
            self.console.print(f"[cyan]🔄 Creating variant {i+1}: {variant_id}[/cyan]")
            
            # Create different prompt variations to encourage diversity
            prompts = [
                f"""Rewrite this code using a while loop instead of for loop and different variable names:

{source_content}

Output only C code:""",
                f"""Create a C variant using different variable names (total, counter, etc.) and different control flow:

{source_content}

Just the C code:""",
                f"""Transform this C program to use different variable names and replace the for loop with a while loop:

{source_content}

Only respond with C code:"""
            ]
            
            prompt = prompts[i % len(prompts)]
            
            try:
                # Get LLM response for the variant
                response = self._call_llm(prompt)
                if not response:
                    continue
                
                # Extract C code from response
                c_code = response.strip()
                
                # Clean up the response - extract code block if present
                if "```c" in c_code:
                    start = c_code.find("```c") + 4
                    end = c_code.find("```", start)
                    if end != -1:
                        c_code = c_code[start:end].strip()
                elif "```" in c_code:
                    start = c_code.find("```") + 3
                    end = c_code.find("```", start)
                    if end != -1:
                        c_code = c_code[start:end].strip()
                
                # Write the variant source
                variant_source_name = f"{variant_id}.c"
                variant_binary_name = f"{variant_id}"
                
                success = self.write_file(variant_source_name, c_code)
                if not success:
                    self.console.print(f"[red]❌ Failed to write variant {i+1} source[/red]")
                    continue
                
                # Compile the variant
                success = self.compile_c(variant_source_name, variant_binary_name)
                if not success:
                    self.console.print(f"[red]❌ Failed to compile variant {i+1}[/red]")
                    continue
                
                # Test the variant
                success, output = self.run_executable(variant_binary_name)
                if not success:
                    self.console.print(f"[red]❌ Failed to run variant {i+1}[/red]")
                    continue
                
                # Verify functionality by comparing output with original
                variant_source = self.workspace / variant_source_name
                variant_binary = self.workspace / variant_binary_name
                
                if variant_source.exists() and variant_binary.exists():
                    variant = VariantInfo(
                        id=variant_id,
                        name=f"AI Variant {i+1}",
                        path=str(variant_binary),
                        variant_type=VariantType.AI_GENERATED,
                        generation_time=datetime.now(),
                        metadata={
                            "source_file": str(variant_source),
                            "model": self.config.ollama_model,
                            "output": output.strip()
                        }
                    )
                    variants.append(variant)
                    self.console.print(f"[green]✅ Generated AI variant {i+1}: {variant_id}[/green]")
                else:
                    self.console.print(f"[red]❌ Variant {i+1} files missing[/red]")
                    
            except Exception as e:
                self.console.print(f"[red]❌ Error generating variant {i+1}: {e}[/red]")
        
        return variants


class MetaMEIntegration:
    """Integration with MetaME metamorphic engine"""
    
    def __init__(self, config: SuiteConfig, console: Console):
        self.config = config
        self.console = console
        
    def check_installation(self) -> bool:
        """Check if MetaME is available"""
        try:
            import metame
            return True
        except ImportError:
            return False
    
    def generate_variant_name(self, binary_path: str, variant_number: int) -> str:
        """Generate a meaningful variant name based on binary file, number and timestamp"""
        # Extract binary file name without extension
        binary_name = Path(binary_path).stem
        
        # Generate timestamp (YYYYMMDD_HHMMSS format)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create variant name: binaryname_metame_vN_timestamp
        variant_name = f"{binary_name}_metame_v{variant_number:02d}_{timestamp}"
        
        return variant_name
    
    def check_binary_compatibility(self, binary_path: str) -> Tuple[bool, str]:
        """Check if binary is compatible with MetaME"""
        try:
            # Check binary format and architecture
            result = subprocess.run(['file', binary_path], capture_output=True, text=True)
            file_info = result.stdout.lower()
            
            # MetaME works best with ELF x86/x64 binaries
            if 'elf' not in file_info:
                return False, "MetaME requires ELF format binaries (Linux/Unix). Try compiling with: gcc -o program source.c"
            
            if 'mach-o' in file_info:
                return False, "Mach-O format (macOS) not supported. Please use ELF binaries."
                
            if 'pe32' in file_info or 'pe32+' in file_info:
                return False, "PE format (Windows) not supported. Please use ELF binaries."
            
            if 'arm' in file_info and '64' in file_info:
                return False, "ARM64 architecture may have limited support. x86/x64 recommended."
            
            # Check for PIE (Position Independent Executable) which can cause issues
            warnings = []
            if 'pie' in file_info:
                warnings.append("PIE binary detected - may cause MetaME issues")
            
            if 'dynamically linked' in file_info:
                warnings.append("Dynamic linking detected - static binaries work better")
            
            if warnings:
                warning_msg = ", ".join(warnings)
                return True, f"Binary compatible but with warnings: {warning_msg}"
            else:
                return True, "Binary appears fully compatible with MetaME"
                
        except Exception as e:
            return False, f"Cannot analyze binary: {e}"
    
    def generate_variants(self, binary_path: str, num_variants: int = 3) -> List[VariantInfo]:
        """Generate metamorphic variants using MetaME"""
        variants = []
        
        if not self.check_installation():
            self.console.print("[red]❌ MetaME not found. Install with: pip install metame[/red]")
            return variants
        
        # Check binary compatibility before attempting generation
        compatible, msg = self.check_binary_compatibility(binary_path)
        if not compatible:
            self.console.print(f"[red]❌ Binary compatibility issue: {msg}[/red]")
            self.console.print("[dim]💡 MetaME works best with ELF x86/x64 binaries compiled with GCC[/dim]")
            return variants
        else:
            self.console.print(f"[green]✅ {msg}[/green]")
        
        self.console.print(f"[blue]🔄 Generating {num_variants} MetaME variants from {binary_path}...[/blue]")
        
        for i in range(num_variants):
            variant_id = self.generate_variant_name(binary_path, i+1)
            output_path = f"{binary_path}.{variant_id}"
            
            try:
                # Use MetaME via subprocess since the Python API is limited
                cmd = [
                    sys.executable, "-c",
                    f"import sys, metame; sys.argv = ['metame', '-i', '{binary_path}', '-o', '{output_path}']; metame.main()"
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0 and Path(output_path).exists():
                    variant = VariantInfo(
                        id=variant_id,
                        name=f"MetaME Variant {i+1}",
                        path=output_path,
                        variant_type=VariantType.METAME,
                        generation_time=datetime.now(),
                        metadata={
                            "original_binary": binary_path,
                            "file_size": os.path.getsize(output_path),
                            "metame_output": result.stdout,
                            "transformations": "metamorphic"
                        }
                    )
                    variants.append(variant)
                    self.console.print(f"[green]✅ Generated MetaME variant {i+1}: {variant_id}[/green]")
                else:
                    # Enhanced error reporting
                    if result.stderr:
                        error_lines = result.stderr.strip().split('\n')
                        # Show only the most relevant error line
                        relevant_error = "Unknown error"
                        for line in error_lines:
                            if 'keyerror' in line.lower() and 'offset' in line.lower():
                                relevant_error = "MetaME bug: 'offset' key missing (known issue with some binaries)"
                                break
                            elif 'exception' in line.lower() or 'error' in line.lower():
                                relevant_error = line.split(':', 1)[-1].strip() if ':' in line else line
                                break
                        self.console.print(f"[red]❌ MetaME failed for variant {i+1}: {relevant_error}[/red]")
                    else:
                        self.console.print(f"[red]❌ MetaME failed for variant {i+1}: Process failed[/red]")
                    
            except subprocess.TimeoutExpired:
                self.console.print(f"[red]❌ MetaME timeout for variant {i+1}[/red]")
            except Exception as e:
                self.console.print(f"[red]❌ MetaME error for variant {i+1}: {e}[/red]")
        
        # Summary
        successful_variants = len(variants)
        if successful_variants > 0:
            self.console.print(f"\n[green]🎉 Successfully generated {successful_variants}/{num_variants} MetaME variants[/green]")
        else:
            self.console.print(f"\n[red]❌ No MetaME variants generated.[/red]")
            self.console.print("[yellow]⚠️ Note: MetaME has known compatibility issues with modern binaries[/yellow]")
            self.console.print("[dim]💡 MetaME works best with older, simpler ELF binaries[/dim]")
            self.console.print("[dim]💡 Alternative: Use AI variants instead - they work reliably with source code[/dim]")
            self.console.print("[dim]   1. source your_file.c[/dim]")
            self.console.print("[dim]   2. ai[/dim]")
        
        return variants


class CodeGenomeSuite:
    """Main CodeGenome Suite application"""
    
    def __init__(self):
        self.console = Console()
        self.config = SuiteConfig()
        self.workspace = Path(self.config.workspace_dir)
        self.workspace.mkdir(exist_ok=True)
        
        # Initialize components
        self.metame = MetaMEIntegration(self.config, self.console)
        self.agent = AgenticLLM(self.config, self.console, self.workspace)
        
        # Session data
        self.loaded_binaries = []
        self.loaded_sources = []
        self.generated_variants = []
    
    def show_banner(self):
        """Display CodeGenome banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Create ASCII art banner
        banner_text = pyfiglet.figlet_format("CodeGenome", font="big")
        colored_banner = colored(banner_text, "cyan", attrs=["bold"])
        
        print(colored_banner)
        print(colored("═" * 80, "blue"))
        print(colored("  Advanced Binary Analysis & AI-Powered Variant Generation Suite", "white", attrs=["bold"]))
        print(colored("  Version 3.0 - Agentic AI Edition", "yellow"))
        print(colored("═" * 80, "blue"))
        print()
    
    def show_status(self):
        """Show current status"""
        table = Table(title="Current Session Status", box=box.ROUNDED)
        table.add_column("Component", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Count/Info", style="yellow")
        
        # Binaries
        table.add_row(
            "Loaded Binaries",
            "✅ Ready" if self.loaded_binaries else "⚠️ None",
            str(len(self.loaded_binaries))
        )
        
        # Sources
        table.add_row(
            "Source Files", 
            "✅ Ready" if self.loaded_sources else "⚠️ None",
            str(len(self.loaded_sources))
        )
        
        # MetaME
        metame_status = "✅ Available" if self.metame.check_installation() else "❌ Not found"
        table.add_row("MetaME Engine", metame_status, self.config.metame_path or "Not configured")
        
        # Ollama
        ollama_status = "✅ Connected" if self.agent.check_ollama_connection() else "❌ Disconnected"
        table.add_row("Ollama AI", ollama_status, self.config.ollama_model)
        
        # Variants
        table.add_row(
            "Generated Variants",
            "✅ Available" if self.generated_variants else "⚠️ None",
            str(len(self.generated_variants))
        )
        
        # Workspace
        table.add_row("Workspace", "✅ Ready", str(self.workspace))
        
        self.console.print(table)
        print()
    
    def main_menu(self):
        """Main interactive menu"""
        
        while True:
            self.show_banner()
            self.show_status()
            
            choices = [
                "📁 Load Binaries",
                "📄 Load Source Files", 
                "🔄 Generate MetaME Variants",
                "🤖 Generate AI Variants",
                "📊 View Generated Variants",
                "🔍 Analyze Binaries & Generate Radar Chart",
                "⚙️ Configuration",
                "🚪 Exit"
            ]
            
            try:
                choice = questionary.select(
                    "What would you like to do?",
                    choices=choices,
                    style=questionary.Style([
                        ('selected', 'fg:#00aa00 bold'),
                        ('pointer', 'fg:#673ab7 bold'),
                        ('highlighted', 'fg:#673ab7'),
                        ('answer', 'fg:#f44336 bold'),
                    ])
                ).ask()
            except Exception:
                # Fallback for non-interactive environments
                self.console.print("\n[yellow]Non-interactive mode detected. Available options:[/yellow]")
                for i, option in enumerate(choices):
                    self.console.print(f"{i+1}. {option}")
                choice_num = input("\nEnter choice number (or 'q' to quit): ").strip()
                if choice_num.lower() == 'q':
                    choice = None
                else:
                    try:
                        choice = choices[int(choice_num) - 1]
                    except (ValueError, IndexError):
                        choice = None
            
            if choice is None or "Exit" in choice:
                break
            elif "Load Binaries" in choice:
                self.load_binaries()
            elif "Load Source Files" in choice:
                self.load_sources()
            elif "Generate MetaME Variants" in choice:
                self.generate_metame_variants()
            elif "Generate AI Variants" in choice:
                self.generate_ai_variants()
            elif "View Generated Variants" in choice:
                self.view_variants()
            elif "Analyze Binaries" in choice:
                self.analyze_binaries_with_radar()
            elif "Configuration" in choice:
                self.configure_settings()
        
        self.console.print("\n[blue]👋 Thanks for using CodeGenome Suite![/blue]")
    
    def load_binaries(self):
        """Load binary files"""
        self.console.print("\n[bold]📁 Load Binary Files[/bold]")
        
        while True:
            choices = [
                "➕ Add Binary File",
                "📂 Browse Directory",
                "📋 List Loaded Binaries",
                "🗑️ Remove Binary",
                "⬅️ Back to Main Menu"
            ]
            
            choice = questionary.select("Binary Management:", choices=choices).ask()
            
            if choice is None or "Back" in choice:
                break
            elif "Add Binary File" in choice:
                path = questionary.path("Binary file path:").ask()
                if path and os.path.isfile(path) and os.access(path, os.X_OK):
                    if path not in self.loaded_binaries:
                        self.loaded_binaries.append(path)
                        self.console.print(f"[green]✅ Added binary: {os.path.basename(path)}[/green]")
                    else:
                        self.console.print(f"[yellow]⚠️ Already loaded: {os.path.basename(path)}[/yellow]")
                else:
                    self.console.print("[red]❌ Invalid binary file[/red]")
            
            elif "List Loaded Binaries" in choice:
                if self.loaded_binaries:
                    table = Table(title="Loaded Binaries")
                    table.add_column("Index", style="cyan")
                    table.add_column("Path", style="green")
                    table.add_column("Size", style="yellow")
                    
                    for i, binary in enumerate(self.loaded_binaries):
                        size = os.path.getsize(binary) if os.path.exists(binary) else 0
                        table.add_row(str(i+1), binary, f"{size:,} bytes")
                    
                    self.console.print(table)
                else:
                    self.console.print("[yellow]⚠️ No binaries loaded[/yellow]")
            
            elif "Remove Binary" in choice:
                if self.loaded_binaries:
                    choices = [f"{i+1}: {os.path.basename(b)}" for i, b in enumerate(self.loaded_binaries)]
                    remove_choice = questionary.select("Select binary to remove:", choices=choices).ask()
                    if remove_choice:
                        index = int(remove_choice.split(":")[0]) - 1
                        removed = self.loaded_binaries.pop(index)
                        self.console.print(f"[green]✅ Removed: {os.path.basename(removed)}[/green]")
    
    def load_sources(self):
        """Load source files"""
        self.console.print("\n[bold]📄 Load Source Files[/bold]")
        
        while True:
            choices = [
                "➕ Add Source File",
                "📋 List Loaded Sources",
                "🗑️ Remove Source",
                "⬅️ Back to Main Menu"
            ]
            
            choice = questionary.select("Source Management:", choices=choices).ask()
            
            if choice is None or "Back" in choice:
                break
            elif "Add Source File" in choice:
                path = questionary.path("Source file path (*.c, *.cpp):").ask()
                if path and os.path.isfile(path) and path.endswith(('.c', '.cpp', '.cc')):
                    if path not in self.loaded_sources:
                        self.loaded_sources.append(path)
                        self.console.print(f"[green]✅ Added source: {os.path.basename(path)}[/green]")
                    else:
                        self.console.print(f"[yellow]⚠️ Already loaded: {os.path.basename(path)}[/yellow]")
                else:
                    self.console.print("[red]❌ Invalid source file[/red]")
            
            elif "List Loaded Sources" in choice:
                if self.loaded_sources:
                    table = Table(title="Loaded Source Files")
                    table.add_column("Index", style="cyan")
                    table.add_column("Path", style="green")
                    table.add_column("Size", style="yellow")
                    
                    for i, source in enumerate(self.loaded_sources):
                        size = os.path.getsize(source) if os.path.exists(source) else 0
                        table.add_row(str(i+1), source, f"{size:,} bytes")
                    
                    self.console.print(table)
                else:
                    self.console.print("[yellow]⚠️ No source files loaded[/yellow]")
    
    def generate_metame_variants(self):
        """Generate MetaME variants from binaries"""
        if not self.loaded_binaries:
            self.console.print("[red]❌ No binaries loaded. Please load binaries first.[/red]")
            return
        
        self.console.print("\n[bold]🔄 Generate MetaME Variants[/bold]")
        
        # Select binary
        binary_choices = [f"{i+1}: {os.path.basename(b)}" for i, b in enumerate(self.loaded_binaries)]
        binary_choice = questionary.select("Select binary:", choices=binary_choices).ask()
        
        if not binary_choice:
            return
        
        binary_index = int(binary_choice.split(":")[0]) - 1
        selected_binary = self.loaded_binaries[binary_index]
        
        num_variants = int(questionary.text("Number of variants to generate:", default="3").ask() or "3")
        
        # Generate variants
        variants = self.metame.generate_variants(selected_binary, num_variants)
        self.generated_variants.extend(variants)
        
        if variants:
            self.console.print(f"[green]✅ Successfully generated {len(variants)} MetaME variants[/green]")
        else:
            self.console.print("[red]❌ No variants were generated[/red]")
    
    def generate_ai_variants(self, source_index=None, num_variants=None):
        """Generate AI variants from source files"""
        if not self.loaded_sources:
            self.console.print("[red]❌ No source files loaded. Please load source files first.[/red]")
            return
        
        self.console.print("\n[bold]🤖 Generate AI Variants[/bold]")
        
        # Auto-select source or ask interactively
        if source_index is None:
            # Interactive mode
            source_choices = [f"{i+1}: {os.path.basename(s)}" for i, s in enumerate(self.loaded_sources)]
            source_choice = questionary.select("Select source file:", choices=source_choices).ask()
            
            if not source_choice:
                return
            
            source_index = int(source_choice.split(":")[0]) - 1
        else:
            # Non-interactive mode
            if source_index >= len(self.loaded_sources):
                source_index = 0
        
        selected_source = self.loaded_sources[source_index]
        
        # Auto-set variants or ask interactively  
        if num_variants is None:
            # Interactive mode
            num_variants = int(questionary.text("Number of AI variants to generate:", default="3").ask() or "3")
        
        self.console.print(f"[blue]📁 Selected source: {os.path.basename(selected_source)}[/blue]")
        self.console.print(f"[blue]🔢 Generating {num_variants} variant(s)[/blue]")
        
        # Copy source to workspace for AI processing
        source_name = os.path.basename(selected_source)
        workspace_source = self.workspace / source_name
        shutil.copy2(selected_source, workspace_source)
        
        # Generate variants using agentic AI
        variants = self.agent.generate_variants_from_source(str(workspace_source), num_variants)
        self.generated_variants.extend(variants)
        
        if variants:
            self.console.print(f"[green]✅ Successfully generated {len(variants)} AI variants[/green]")
            
            # Auto-suggest binary analysis
            if BINARY_ANALYZER_AVAILABLE and len(variants) > 0:
                self.console.print("\n[blue]💡 Tip: You can now analyze these variants with radar chart visualization![/blue]")
                if questionary.confirm("🔍 Run binary analysis now?").ask():
                    self.analyze_binaries_with_radar()
        else:
            self.console.print("[red]❌ No AI variants were generated[/red]")
    
    def view_variants(self):
        """View generated variants"""
        if not self.generated_variants:
            self.console.print("[yellow]⚠️ No variants generated yet[/yellow]")
            return
        
        self.console.print("\n[bold]📊 Generated Variants[/bold]")
        
        table = Table(title="Variant Summary", box=box.ROUNDED)
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Type", style="yellow")
        table.add_column("Generated", style="magenta")
        table.add_column("Status", style="bold")
        
        for variant in self.generated_variants:
            status = "✅ Ready" if os.path.exists(variant.path) else "❌ Missing"
            table.add_row(
                variant.id,
                variant.name,
                variant.variant_type.value,
                variant.generation_time.strftime("%H:%M:%S"),
                status
            )
        
        self.console.print(table)
        
        # Show workspace contents
        workspace_files = list(self.workspace.glob("*"))
        if workspace_files:
            self.console.print(f"\n[bold]📁 Workspace Contents ({len(workspace_files)} files):[/bold]")
            for file_path in sorted(workspace_files):
                if file_path.is_file():
                    size = file_path.stat().st_size
                    self.console.print(f"  📄 {file_path.name} ({size:,} bytes)")
    
    def configure_settings(self):
        """Configure suite settings"""
        self.console.print("\n[bold]⚙️ Configuration[/bold]")
        
        while True:
            choices = [
                "🔄 MetaME Path",
                "🤖 Ollama Settings",
                "📁 Workspace Directory",
                "💾 Save Configuration",
                "⬅️ Back to Main Menu"
            ]
            
            choice = questionary.select("Configuration:", choices=choices).ask()
            
            if choice is None or "Back" in choice:
                break
            elif "MetaME Path" in choice:
                current_path = self.config.metame_path or "Not set"
                new_path = questionary.text(f"MetaME path (current: {current_path}):").ask()
                if new_path:
                    self.config.metame_path = new_path
                    self.metame = MetaMEIntegration(self.config, self.console)
                    if self.metame.check_installation():
                        self.console.print("[green]✅ MetaME path updated and verified[/green]")
                    else:
                        self.console.print("[red]❌ MetaME not found at specified path[/red]")
            
            elif "Ollama Settings" in choice:
                self.config.ollama_base_url = questionary.text(
                    "Ollama base URL:", 
                    default=self.config.ollama_base_url
                ).ask()
                
                self.config.ollama_model = questionary.select(
                    "Ollama model:",
                    choices=["gemma3:12b", "gemma3:1b", "gemma2:2b", "llama3.2:1b", "llama3.2:3b"],
                    default=self.config.ollama_model
                ).ask()
                
                self.agent = AgenticLLM(self.config, self.console, self.workspace)
                
                if self.agent.check_ollama_connection():
                    self.console.print("[green]✅ Ollama connection verified[/green]")
                else:
                    self.console.print("[red]❌ Cannot connect to Ollama[/red]")
            
            elif "Workspace Directory" in choice:
                new_workspace = questionary.text(
                    "Workspace directory:",
                    default=self.config.workspace_dir
                ).ask()
                if new_workspace:
                    self.config.workspace_dir = new_workspace
                    self.workspace = Path(new_workspace)
                    self.workspace.mkdir(exist_ok=True)
                    self.agent = AgenticLLM(self.config, self.console, self.workspace)
                    self.console.print(f"[green]✅ Workspace updated: {self.workspace}[/green]")
            
            elif "Save Configuration" in choice:
                config_file = self.workspace / "config.toml"
                try:
                    config_dict = self.config.model_dump()
                    config_file.write_text(toml.dumps(config_dict))
                    self.console.print(f"[green]✅ Configuration saved: {config_file}[/green]")
                except Exception as e:
                    self.console.print(f"[red]❌ Failed to save config: {e}[/red]")


    def analyze_binaries_with_radar(self):
        """Advanced binary analysis with interactive selection and radar chart generation"""
        self.console.print("\n[bold]🔍 Advanced Binary Analysis & Radar Chart Generation[/bold]")
        
        if not ADVANCED_ANALYZER_AVAILABLE:
            self.console.print("[red]❌ Advanced binary analyzer not available. Please install required dependencies:[/red]")
            self.console.print("[yellow]  pip install matplotlib numpy r2pipe scikit-learn[/yellow]")
            
            # Fallback to basic analyzer
            if BINARY_ANALYZER_AVAILABLE:
                self.console.print("[blue]💡 Using basic analyzer as fallback...[/blue]")
                self._analyze_binaries_basic()
            return
        
        # Collect all available binaries with better categorization
        available_binaries = []
        
        # Add loaded binaries
        for binary in self.loaded_binaries:
            if os.path.exists(binary):
                available_binaries.append({
                    'name': f"📁 Loaded: {os.path.basename(binary)}",
                    'path': binary,
                    'category': 'loaded'
                })
        
        # Add generated variants
        for variant in self.generated_variants:
            if os.path.exists(variant.path):
                available_binaries.append({
                    'name': f"🤖 Variant: {variant.name}",
                    'path': variant.path,
                    'category': 'variant'
                })
        
        # Add workspace binaries (including compiled sources)
        for file_path in self.workspace.glob("*"):
            if file_path.is_file() and os.access(file_path, os.X_OK):
                # Check if it's a binary (simple heuristic)
                try:
                    with open(file_path, 'rb') as f:
                        header = f.read(4)
                        if header.startswith(b'\x7fELF') or header.startswith(b'MZ'):
                            # Check if not already added
                            already_added = any(b['path'] == str(file_path) for b in available_binaries)
                            if not already_added:
                                available_binaries.append({
                                    'name': f"⚙️ Workspace: {file_path.name}",
                                    'path': str(file_path),
                                    'category': 'workspace'
                                })
                except:
                    continue
        
        if not available_binaries:
            self.console.print("[yellow]⚠️ No binaries available for analysis.[/yellow]")
            self.console.print("[blue]💡 Load binaries or generate variants first.[/blue]")
            return
        
        # Show available binaries with categories
        self.console.print(f"\n[green]📊 Found {len(available_binaries)} binaries for analysis:[/green]")
        
        # Group by category for better display
        categories = {'loaded': [], 'variant': [], 'workspace': []}
        for binary in available_binaries:
            categories[binary['category']].append(binary)
        
        for category_name, binaries in categories.items():
            if binaries:
                self.console.print(f"[cyan]{category_name.title()} ({len(binaries)}):[/cyan]")
                for binary in binaries:
                    size = os.path.getsize(binary['path']) if os.path.exists(binary['path']) else 0
                    self.console.print(f"  {binary['name']} ({size:,} bytes)")
        
        # Selection menu
        self.console.print(f"\n[yellow]🎯 Analysis Options:[/yellow]")
        choices = [
            "🔍 Analyze All Binaries (Comprehensive)",
            "📊 Select Multiple Binaries",
            "🎯 Select Single Binary",
            "⬅️ Back to Main Menu"
        ]
        
        choice = questionary.select("Choose analysis mode:", choices=choices).ask()
        
        if choice is None or "Back" in choice:
            return
        
        binaries_to_analyze = []
        
        if "Analyze All" in choice:
            binaries_to_analyze = [b['path'] for b in available_binaries]
            
        elif "Select Multiple" in choice:
            # Multi-select binaries
            binary_choices = [f"{b['name']} ({os.path.getsize(b['path']):,} bytes)" for b in available_binaries]
            selected = questionary.checkbox(
                "Select binaries to analyze (use space to select, enter to confirm):",
                choices=binary_choices
            ).ask()
            
            if not selected:
                return
            
            # Map back to paths
            for selection in selected:
                for binary in available_binaries:
                    binary_display = f"{binary['name']} ({os.path.getsize(binary['path']):,} bytes)"
                    if binary_display == selection:
                        binaries_to_analyze.append(binary['path'])
                        break
        
        elif "Select Single" in choice:
            # Single select
            binary_choices = [b['name'] for b in available_binaries]
            selected = questionary.select("Select binary to analyze:", choices=binary_choices).ask()
            
            if not selected:
                return
            
            for binary in available_binaries:
                if binary['name'] == selected:
                    binaries_to_analyze = [binary['path']]
                    break
        
        if not binaries_to_analyze:
            self.console.print("[red]❌ No binaries selected[/red]")
            return
        
        # Advanced analysis mode selection
        self.console.print(f"\n[bold yellow]🔬 Analysis Mode Selection[/bold yellow]")
        self.console.print(f"[cyan]Choose how to analyze syscalls in the selected binaries:[/cyan]")
        
        analysis_choices = [
            "📊 Static Analysis Only (Fast - recommended for large sets)",
            "🔍 Dynamic Analysis with Strace (Slower but more accurate)",
            "🔬 Dynamic Analysis + N-gram Patterns (Most comprehensive)"
        ]
        
        # Show detailed comparison
        comparison_table = Table(title="Analysis Mode Comparison", box=box.ROUNDED)
        comparison_table.add_column("Mode", style="cyan")
        comparison_table.add_column("Speed", style="green")
        comparison_table.add_column("Accuracy", style="yellow")
        comparison_table.add_column("Features", style="blue")
        
        comparison_table.add_row(
            "Static Only", 
            "⚡ Very Fast", 
            "📊 Good", 
            "Import/symbol analysis"
        )
        comparison_table.add_row(
            "Dynamic Strace", 
            "🐌 Slower", 
            "🎯 High", 
            "Real syscall execution"
        )
        comparison_table.add_row(
            "Dynamic + N-grams", 
            "🐌 Slowest", 
            "🎯 Highest", 
            "Execution + pattern analysis"
        )
        
        self.console.print(comparison_table)
        
        # Warn about performance for large sets
        if len(binaries_to_analyze) > 5:
            self.console.print(f"\n[yellow]⚠️ Warning: You selected {len(binaries_to_analyze)} binaries[/yellow]")
            self.console.print(f"[yellow]   Dynamic analysis may take a long time![/yellow]")
        
        self.console.print(f"\n[green]💡 Tip: You can always start with static analysis and re-run with dynamic if needed[/green]")
        
        analysis_choice = questionary.select(
            "🔍 Select analysis mode:",
            choices=analysis_choices
        ).ask()
        
        if analysis_choice is None:
            self.console.print("[red]❌ No analysis mode selected[/red]")
            return
        
        # Parse the choice
        use_strace = False
        enable_ngrams = False
        
        if "Dynamic Analysis with Strace" in analysis_choice:
            use_strace = True
            enable_ngrams = False
            self.console.print(f"[blue]🔍 Selected: Dynamic strace analysis[/blue]")
        elif "Dynamic Analysis + N-gram" in analysis_choice:
            use_strace = True
            enable_ngrams = True
            self.console.print(f"[blue]🔬 Selected: Dynamic analysis with n-gram patterns[/blue]")
        else:
            use_strace = False
            enable_ngrams = False
            self.console.print(f"[blue]📊 Selected: Static analysis only[/blue]")
        
        # Final confirmation for dynamic analysis
        if use_strace and len(binaries_to_analyze) > 3:
            confirm = questionary.confirm(
                f"⚠️ Are you sure you want to run dynamic analysis on {len(binaries_to_analyze)} binaries? This may take several minutes."
            ).ask()
            if not confirm:
                self.console.print(f"[yellow]📊 Falling back to static analysis[/yellow]")
                use_strace = False
                enable_ngrams = False
        
        # Initialize advanced analyzer
        analyzer = AdvancedBinaryAnalyzer(self.console, self.workspace)
        
        # Perform comprehensive analysis
        try:
            all_metrics, radar_path = analyzer.analyze_multiple_binaries_advanced(
                binaries_to_analyze, use_strace=use_strace
            )
            
            if all_metrics:
                self.console.print(f"\n[green]✅ Analysis completed successfully![/green]")
                if radar_path:
                    self.console.print(f"[blue]📊 Radar chart: {radar_path}[/blue]")
                    
                # Ask to open results directory
                if questionary.confirm("📁 Open analysis results directory?").ask():
                    try:
                        import subprocess
                        subprocess.run(['xdg-open', str(analyzer.analysis_dir)], check=False)
                    except:
                        self.console.print(f"[blue]📁 Results directory: {analyzer.analysis_dir}[/blue]")
            else:
                self.console.print("[red]❌ Analysis failed - no binaries could be processed[/red]")
                
        except Exception as e:
            self.console.print(f"[red]❌ Analysis error: {e}[/red]")
    
    def _analyze_binaries_basic(self):
        """Fallback basic analysis method"""
        # This is the original basic analyzer method as fallback
        analyzer = BinaryAnalyzer(self.console, self.workspace)
        # Basic implementation here...

def main():
    """Main entry point"""
    try:
        suite = CodeGenomeSuite()
        suite.main_menu()
    except KeyboardInterrupt:
        print(colored("\n\n👋 Goodbye!", "yellow"))
    except Exception as e:
        print(colored(f"\n❌ Error: {e}", "red"))


if __name__ == "__main__":
    main()