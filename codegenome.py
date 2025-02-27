#!/usr/bin/env python3
"""
Binary Analysis Tool - Analyzes and compares binary executables using static and dynamic analysis

This tool uses Radare2 and strace to extract metrics from binary files and compares
multiple variants using radar charts and distance matrices. It provides insights into
instruction mix, syscall usage patterns, and structural similarity between binaries.
"""

import r2pipe
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess
import re
import signal
import os
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

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
    'swapon', 'swapoff', 'reboot', 'sethostname', 'gethostname'
}

# Instruction categories for analysis
INSTRUCTION_CATEGORIES = {
    'control_flow_ops': {'jmp', 'je', 'jne', 'jz', 'jnz', 'call', 'ret'},
    'data_movement_ops': {'mov', 'lea', 'push', 'pop'},
    'computational_ops': {'add', 'sub', 'mul', 'div', 'inc', 'dec',
                          'and', 'or', 'xor', 'shl', 'shr', 'cmp', 'test'},
    'memory_access_ops': {'mov', 'lea', 'push', 'pop', '['} # Instructions involving memory access
}

# Analysis axis labels for radar charts and metrics display
ANALYSIS_AXES = [
    'Code Size', 'Control Flow', 'Data Movement',
    'Computational', 'Memory Access',
    'Function Diversity', 'Complexity', 'Total Syscalls'
]


def safe_cmdj(r2, cmd):
    """Execute r2 command safely and return JSON result, returning empty list on failure."""
    try:
        result = r2.cmdj(cmd)
        return result if result is not None else []
    except Exception as e:
        print(f"[!] Command failed: {cmd} - {str(e)}")
        return []


def analyze_syscalls_with_strace(file_path, timeout=20):
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
        
        print(f"[*] Processed {len(lines)} strace output lines")
        
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
            print(f"[*] Captured {total_syscalls} syscalls")
        
        return {
            'total_syscalls': total_syscalls, 
            'syscalls': syscall_counts,
            'syscall_sequence': syscall_sequence
        }
    except Exception as e:
        print(f"[!] Strace analysis failed for {file_path}: {e}")
        return {'total_syscalls': 0, 'syscalls': {}, 'syscall_sequence': []}


def analyze_with_radare2(file_path, use_strace=False):
    """
    Analyze binary using Radare2 and optionally strace.
    
    Args:
        file_path: Path to the binary to analyze
        use_strace: Whether to use strace for dynamic analysis
        
    Returns:
        Dictionary with comprehensive analysis metrics
    """
    r2 = r2pipe.open(file_path)
    r2.cmd('e bin.relocs.apply=true')
    r2.cmd('e bin.cache=true')
    r2.cmd('aaaa')  # Perform deep analysis

    metrics = {
        'total_functions': 0,
        'total_instructions': 0,
        'control_flow_ops': 0,
        'data_movement_ops': 0,
        'computational_ops': 0,
        'memory_access_ops': 0,
        'stack_operations': 0,
        'heap_operations': {'malloc': 0, 'free': 0, 'realloc': 0},
        'syscalls': {},
        'total_syscalls': 0,
        'complexity': 0,
        'instruction_mix': {cat: 0 for cat in INSTRUCTION_CATEGORIES},
        'function_details': {}
    }

    try:
        # Static syscall analysis
        if not use_strace:
            imports = safe_cmdj(r2, 'ii')
            syscall_imports = {}
            for imp in imports:
                name = imp.get('name', '')
                clean_name = name.split('@')[0].lstrip('_').split('.')[0]
                if clean_name in SYSCALL_WRAPPERS:
                    syscall_imports[imp['name']] = clean_name

            for imp_name, clean_name in syscall_imports.items():
                xrefs = safe_cmdj(r2, f'axtj @ `is~{imp_name}$[0]`')
                count = len([x for x in xrefs if x.get('type') == 'CALL'])
                if count > 0:
                    metrics['syscalls'][clean_name] = metrics['syscalls'].get(clean_name, 0) + count
                    metrics['total_syscalls'] += count

        # Function and instruction analysis
        functions = [f for f in safe_cmdj(r2, 'aflj') if not f['name'].startswith('sym.imp.')]
        metrics['total_functions'] = len(functions)

        for func in functions:
            fname = func['name']
            metrics['function_details'][fname] = {
                'instructions': 0,
                'calls': []
            }
            try:
                # Calculate cyclomatic complexity for each function
                bblocks = safe_cmdj(r2, f'afbj @ {func["offset"]}')
                if bblocks:
                    edges = sum(1 for b in bblocks if b.get('jump', -1) != -1)
                    nodes = len(bblocks)
                    complexity = edges - nodes + 2
                    metrics['complexity'] += max(complexity, 0)

                # Analyze instructions in the function
                insts = safe_cmdj(r2, f'pdj @ {func["offset"]}')
                if not insts:
                    continue

                valid_insts = [i for i in insts if 'opcode' in i]
                count = len(valid_insts)
                metrics['function_details'][fname]['instructions'] = count
                metrics['total_instructions'] += count

                # Categorize instructions
                for inst in valid_insts:
                    op = inst['opcode'].split()[0].lower()
                    ops = inst['opcode'].lower()

                    for cat_name, ops_list in INSTRUCTION_CATEGORIES.items():
                        for instr_op in ops_list:
                            if instr_op in ops:
                                metrics['instruction_mix'][cat_name] += 1
                                break  # Avoid double counting

                    # Check for heap operations
                    if op == 'call':
                        target = ' '.join(inst['opcode'].split()[1:]).lower()
                        for heap_op in ['malloc', 'free', 'realloc']:
                            if heap_op in target:
                                metrics['heap_operations'][heap_op] += 1

            except Exception as e:
                print(f"[!] Error processing function {fname}: {str(e)}")

        # Dynamic analysis with strace if requested
        if use_strace:
            print(f"[*] Performing dynamic analysis with strace on {file_path}")
            syscall_metrics = analyze_syscalls_with_strace(file_path)
            metrics['total_syscalls'] = syscall_metrics.get('total_syscalls', 0)
            metrics['syscalls'] = syscall_metrics.get('syscalls', {})
            metrics['syscall_sequence'] = syscall_metrics.get('syscall_sequence', [])

    finally:
        r2.quit()

    return metrics


def get_radar_metrics(metrics):
    """
    Extract normalized metrics for radar chart visualization.
    
    Args:
        metrics: Full metrics dictionary from analyze_with_radare2
        
    Returns:
        List of metrics for radar chart
    """
    total_inst = metrics['total_instructions']
    
    return [
        total_inst,  # Code Size
        (metrics['instruction_mix']['control_flow_ops'] / total_inst * 100) if total_inst > 0 else 0,
        (metrics['instruction_mix']['data_movement_ops'] / total_inst * 100) if total_inst > 0 else 0,
        (metrics['instruction_mix']['computational_ops'] / total_inst * 100) if total_inst > 0 else 0,
        (metrics['instruction_mix']['memory_access_ops'] / total_inst * 100) if total_inst > 0 else 0,
        metrics['total_functions'],
        metrics['complexity'],
        metrics['total_syscalls']
    ]


def normalize_multiple_metrics(metrics_list):
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


def plot_radar_comparison(metrics_list, axis_labels, legend_labels, output_file="radar_comparison.png"):
    """
    Generate radar chart comparing multiple binaries.
    
    Args:
        metrics_list: List of normalized metrics vectors
        axis_labels: Labels for each axis
        legend_labels: Labels for each binary
        output_file: Path to save the generated chart
    """
    num_vars = len(axis_labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the loop

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'polar': True})
    
    for data, legend in zip(metrics_list, legend_labels):
        data = np.concatenate((data, data[:1]))  # Close the loop
        ax.plot(angles, data, label=legend, linewidth=2)
        ax.fill(angles, data, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(axis_labels)
    ax.set_yticklabels([])
    plt.title('Binary Comparison Analysis', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1.1))
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    
    return output_file


def print_metrics(metrics):
    """Display formatted metrics for a binary."""
    print("\n" + "="*80)
    print(" BINARY ANALYSIS RESULTS ".center(80, "="))
    print("="*80)
    
    print("\n📊 GENERAL METRICS:")
    print(f"  Functions:    {metrics['total_functions']:,}")
    print(f"  Instructions: {metrics['total_instructions']:,}")
    print(f"  Complexity:   {metrics['complexity']:,}")
    
    print("\n📈 INSTRUCTION DISTRIBUTION:")
    total = metrics['total_instructions']
    if total > 0:
        for category, count in metrics['instruction_mix'].items():
            readable_cat = category.replace('_ops', '').replace('_', ' ').title()
            percentage = (count/total*100)
            print(f"  {readable_cat:16} {percentage:6.2f}% ({count:,})")
    else:
        print("  No instructions analyzed")
    
    print("\n🔄 MEMORY OPERATIONS:")
    print(f"  Heap: malloc({metrics['heap_operations']['malloc']:,}), " + 
          f"free({metrics['heap_operations']['free']:,}), " + 
          f"realloc({metrics['heap_operations']['realloc']:,})")
    
    print("\n⚙️ SYSCALLS USAGE:")
    print(f"  Total syscalls: {metrics['total_syscalls']:,}")
    
    if metrics['syscalls']:
        top_syscalls = sorted(metrics['syscalls'].items(), key=lambda x: x[1], reverse=True)[:10]
        print("  Top syscalls:")
        for syscall, count in top_syscalls:
            print(f"    {syscall:<10} {count:,}")
    else:
        print("  No syscalls detected")
    
    print("\n" + "-"*80)


def print_metrics_vector(metrics_vector, binary_name, normalized=False):
    """Print metrics vector in a formatted table."""
    print(f"\n{'NORMALIZED ' if normalized else ''}METRICS VECTOR: {binary_name}")
    print("-" * 60)
    
    format_str = "{:20} {:>12.6f}" if normalized else "{:20} {:>12,}"
    
    for label, value in zip(ANALYSIS_AXES, metrics_vector):
        print(format_str.format(label, value))


def calculate_distance_matrix_euclidean(metrics_list):
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


def calculate_distance_matrix_cosine(normalized_metrics_list):
    """Calculate pairwise Cosine distance matrix."""
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


def print_distance_matrix(distance_matrix, legend_labels, matrix_type):
    """Print distance matrix in a formatted table."""
    print(f"\n{matrix_type} DISTANCE MATRIX")
    print("=" * 80)
    
    # Print header row
    header = f"{'':20}" + "".join(f"{label:>12}" for label in legend_labels)
    print(header)
    print("-" * len(header))
    
    # Print data rows
    for i, row in enumerate(distance_matrix):
        row_str = f"{legend_labels[i]:20}" + "".join(f"{d:12.6f}" for d in row)
        print(row_str)


def save_distance_matrix_csv(distance_matrices, legend_labels, filename_base="distance_matrix"):
    """
    Save multiple distance matrices to CSV.
    
    Args:
        distance_matrices: Dictionary mapping matrix type to distance matrix
        legend_labels: Labels for binaries
        filename_base: Base filename for output CSV
    """
    csv_output = ""
    
    for matrix_type, matrix in distance_matrices.items():
        csv_output += f"# Distance Matrix: {matrix_type}\n"
        header_row = "," + ",".join(legend_labels) + "\n"
        csv_output += header_row
        
        for i, row in enumerate(matrix):
            row_str = ",".join(f"{d:.6f}" for d in row)
            csv_output += legend_labels[i] + "," + row_str + "\n"
        
        csv_output += "\n"

    filepath = f"{filename_base}.csv"
    with open(filepath, 'w') as f:
        f.write(csv_output)
        
    print(f"[*] Distance matrices saved to '{filepath}'")


def calculate_ngram_syscall_similarity(seq1, seq2, n=3):
    """
    Calculate syscall sequence similarity using n-grams.
    
    Args:
        seq1, seq2: Syscall sequences to compare
        n: Size of n-grams
        
    Returns:
        Cosine similarity score (0-1)
    """
    def get_ngrams(sequence, n):
        if len(sequence) < n:
            return []
        return [tuple(sequence[i:i+n]) for i in range(len(sequence) - n + 1)]

    def get_ngram_counts(sequence, n):
        ngrams = get_ngrams(sequence, n)
        return Counter(ngrams)
    
    # Handle short sequences
    if len(seq1) < n or len(seq2) < n:
        print(f"[!] Sequences too short for {n}-gram analysis")
        return 0.0
    
    # Generate n-gram counts
    counts1 = get_ngram_counts(seq1, n)
    counts2 = get_ngram_counts(seq2, n)
    
    # Print top n-grams if available
    if counts1 and counts2:
        print(f"\n[*] Top {n}-grams in sequence 1:")
        for ngram, count in counts1.most_common(3):
            print(f"    {ngram}: {count}")
        
        print(f"[*] Top {n}-grams in sequence 2:")
        for ngram, count in counts2.most_common(3):
            print(f"    {ngram}: {count}")
    
    # Convert counts to vectors for cosine similarity
    all_ngrams = set(counts1.keys()) | set(counts2.keys())
    
    vec1 = np.array([counts1.get(ngram, 0) for ngram in all_ngrams]).reshape(1, -1)
    vec2 = np.array([counts2.get(ngram, 0) for ngram in all_ngrams]).reshape(1, -1)
    
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0  # Avoid division by zero
    
    similarity = cosine_similarity(vec1, vec2)[0][0]
    return similarity


def analyze_syscall_patterns(all_syscall_sequences):
    """Analyze and display syscall sequence patterns."""
    print("\n" + "="*80)
    print(" SYSCALL SEQUENCE ANALYSIS ".center(80, "="))
    print("="*80)
    
    for name, sequence in all_syscall_sequences.items():
        print(f"\n▶️ {name} syscall sequence:")
        if len(sequence) > 0:
            # Show basic stats
            print(f"  Length: {len(sequence):,} syscalls")
            
            # Show most frequent syscalls
            counter = Counter(sequence)
            print(f"  Most frequent syscalls:")
            for syscall, count in counter.most_common(5):
                percentage = (count / len(sequence)) * 100
                print(f"    {syscall:<12} {count:6,} ({percentage:5.1f}%)")
            
            # Show a sample
            if len(sequence) > 10:
                print(f"  Sample sequence:")
                print(f"    {' → '.join(sequence[:10])} ...")
        else:
            print("  No syscalls captured")


def main():
    """Main program entry point."""
    # Parse command line arguments
    args = sys.argv[1:]
    use_strace = False
    
    if args and args[0] in ["-strace", "-insecure"]:
        use_strace = True
        args = args[1:]
        
    if len(args) < 2:
        print("\nBinary Analysis Tool - Compare binaries with static and dynamic analysis")
        print("\nUsage: ./binary_analyzer.py [-strace|-insecure] base_bin variant1 variant2 ...")
        print("  -strace, -insecure: Use strace for dynamic analysis (slower but more accurate)")
        print("  base_bin: Path to the reference binary")
        print("  variantN: Path to variant binaries for comparison")
        sys.exit(1)
    
    base_bin = args[0]
    variants = args[1:]
    
    print("\n" + "="*80)
    print(" BINARY ANALYSIS TOOL ".center(80, "="))
    print("="*80)
    print(f"\n[*] Analyzing base binary: {base_bin}")
    print(f"[*] Variant binaries: {', '.join(variants)}")
    print(f"[*] Dynamic analysis: {'Enabled' if use_strace else 'Disabled'}")
    
    # Analyze base binary
    try:
        base_metrics = analyze_with_radare2(base_bin, use_strace=use_strace)
        base_radar = get_radar_metrics(base_metrics)
        print_metrics(base_metrics)
        print_metrics_vector(base_radar, "Base Binary")
    except Exception as e:
        print(f"[!] Error analyzing base binary: {str(e)}")
        sys.exit(1)
    
    # Analyze variant binaries
    all_metrics = [base_radar]
    legend_labels = ["Base"]
    all_syscall_sequences = {"Base": base_metrics.get('syscall_sequence', [])}
    
    for i, variant in enumerate(variants, 1):
        try:
            print(f"\n[*] Analyzing variant {i}: {variant}")
            var_metrics = analyze_with_radare2(variant, use_strace=use_strace)
            var_radar = get_radar_metrics(var_metrics)
            
            all_metrics.append(var_radar)
            legend_labels.append(f"Variant {i}")
            
            print_metrics(var_metrics)
            print_metrics_vector(var_radar, f"Variant {i}")
            
            all_syscall_sequences[f"Variant {i}"] = var_metrics.get('syscall_sequence', [])
        except Exception as e:
            print(f"[!] Error analyzing variant {variant}: {str(e)}")
            continue
    
    # Generate normalized metrics and visualization
    try:
        norm_metrics = normalize_multiple_metrics(all_metrics)
        
        print("\n" + "="*80)
        print(" NORMALIZED METRICS COMPARISON ".center(80, "="))
        print("="*80)
        
        for i, label in enumerate(legend_labels):
            print_metrics_vector(norm_metrics[i], label, normalized=True)
        
        output_file = plot_radar_comparison(norm_metrics, ANALYSIS_AXES, legend_labels)
        print(f"\n[*] Radar chart saved as '{output_file}'")
    except Exception as e:
        print(f"[!] Error generating visualization: {str(e)}")
    
    # Calculate and display distance matrices
    try:
        print("\n" + "="*80)
        print(" BINARY SIMILARITY ANALYSIS ".center(80, "="))
        print("="*80)
        
        distance_matrix_raw = calculate_distance_matrix_euclidean(all_metrics)
        distance_matrix_norm = calculate_distance_matrix_euclidean(norm_metrics)
        distance_matrix_cosine = calculate_distance_matrix_cosine(norm_metrics)
        
        print_distance_matrix(distance_matrix_raw, legend_labels, "RAW EUCLIDEAN")
        print_distance_matrix(distance_matrix_norm, legend_labels, "NORMALIZED EUCLIDEAN")
        print_distance_matrix(distance_matrix_cosine, legend_labels, "COSINE")
        
        # Save matrices to CSV
        matrices = {
            "euclidean_raw": distance_matrix_raw,
            "euclidean_normalized": distance_matrix_norm,
            "cosine_normalized": distance_matrix_cosine
        }
        save_distance_matrix_csv(matrices, legend_labels)
    except Exception as e:
        print(f"[!] Error calculating distance matrices: {str(e)}")
    
    # Analyze syscall patterns if dynamic analysis was used
    if use_strace:
        analyze_syscall_patterns(all_syscall_sequences)
        
        print("\n" + "="*80)
        print(" SYSCALL SEQUENCE SIMILARITY ".center(80, "="))
        print("="*80)
        
        # Analyze n-gram similarity for different n values
        for n_value in [2, 3, 4]:
            print(f"\n[*] {n_value}-gram similarity analysis:")
            base_syscall_seq = all_syscall_sequences["Base"]
            
            for i, variant in enumerate(variants, 1):
                variant_name = f"Variant {i}"
                variant_syscall_seq = all_syscall_sequences[variant_name]
                
                if base_syscall_seq and variant_syscall_seq:
                    similarity = calculate_ngram_syscall_similarity(
                        base_syscall_seq, variant_syscall_seq, n=n_value
                    )
                    print(f"  Base vs {variant_name}: {similarity:.6f}")
                else:
                    print(f"  Base vs {variant_name}: N/A (insufficient syscall data)")
    
    print("\n" + "="*80)
    print(" ANALYSIS COMPLETE ".center(80, "="))
    print("="*80)


if __name__ == "__main__":
    main()