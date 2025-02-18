import re

def analyze_assembly(file_path):
    metrics = {
        'total_functions': 0,
        'total_instructions': 0,
        'control_flow_ops': 0,
        'library_calls': 0,
        'stack_operations': 0,
        'heap_operations': {'malloc': 0, 'free': 0, 'realloc': 0},
        'stack_heap_ratio': 0,
        'memory_access_ops': 0,
        'data_movement_ops': 0,
        'computational_ops': 0,
        'max_stack_frame': 0,
        'functions': {}
    }

    current_function = None
    current_stack_frame = 0

    # Patterns
    func_pattern = re.compile(r'^[0-9a-f]+\s<([^>]+)>:')
    stack_alloc_pattern = re.compile(r'sub\s+\$0x([0-9a-f]+),%rsp')
    stack_dealloc_pattern = re.compile(r'add\s+\$0x([0-9a-f]+),%rsp')
    heap_pattern = re.compile(r'<(\w+?)(@\w+)?>')
    
    # Instruction categories
    control_flow_ops = {'jmp', 'je', 'jne', 'jz', 'jnz', 'call', 'ret'}
    stack_ops = {'push', 'pop', 'leave'}
    heap_ops = {'malloc', 'free', 'realloc'}
    data_movement = {'mov', 'lea', 'movzx', 'movsx', 'xchg'}
    computational_ops = {'add', 'sub', 'mul', 'div', 'inc', 'dec', 
                        'and', 'or', 'xor', 'shl', 'shr', 'cmp', 'test'}

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Detect function start
            if func_match := func_pattern.match(line):
                current_function = func_match.group(1)
                metrics['total_functions'] += 1
                metrics['functions'][current_function] = {
                    'instructions': 0,
                    'control_flow': 0,
                    'calls': [],
                    'max_stack_frame': 0
                }
                current_stack_frame = 0
                continue
            
            # Skip non-instruction lines
            if not line or line.startswith(('Disassembly', '...')):
                continue
            
            # Count instructions and analyze
            if current_function:
                metrics['functions'][current_function]['instructions'] += 1
                metrics['total_instructions'] += 1
                
                # Split into operation and arguments
                parts = line.split('\t')
                if len(parts) >= 2:
                    op_part = parts[-1].split()
                    op = op_part[0]
                    args = ' '.join(op_part[1:]) if len(op_part) > 1 else ''

                    # Stack operations analysis
                    if op in stack_ops:
                        metrics['stack_operations'] += 1
                        if op == 'push':
                            current_stack_frame += 8
                        elif op == 'pop':
                            current_stack_frame -= 8
                        elif op == 'leave':
                            current_stack_frame = 0  # Approximation
                        # Update function's max stack frame
                        if current_stack_frame > metrics['functions'][current_function]['max_stack_frame']:
                            metrics['functions'][current_function]['max_stack_frame'] = current_stack_frame
                        # Update global max stack frame
                        if metrics['functions'][current_function]['max_stack_frame'] > metrics['max_stack_frame']:
                            metrics['max_stack_frame'] = metrics['functions'][current_function]['max_stack_frame']
                    
                    # Stack frame analysis (sub/add to %rsp)
                    if stack_alloc := stack_alloc_pattern.search(line):
                        alloc_size = int(stack_alloc.group(1), 16)
                        current_stack_frame += alloc_size
                        if current_stack_frame > metrics['functions'][current_function]['max_stack_frame']:
                            metrics['functions'][current_function]['max_stack_frame'] = current_stack_frame
                        if metrics['functions'][current_function]['max_stack_frame'] > metrics['max_stack_frame']:
                            metrics['max_stack_frame'] = metrics['functions'][current_function]['max_stack_frame']
                    elif stack_dealloc := stack_dealloc_pattern.search(line):
                        dealloc_size = int(stack_dealloc.group(1), 16)
                        current_stack_frame -= dealloc_size
                    
                    # Memory access detection
                    if '[' in args:
                        metrics['memory_access_ops'] += 1

                    # Instruction type categorization
                    if op in data_movement:
                        metrics['data_movement_ops'] += 1
                    elif op in computational_ops:
                        metrics['computational_ops'] += 1
                    
                    # Control flow operations
                    if op in control_flow_ops:
                        metrics['functions'][current_function]['control_flow'] += 1
                        metrics['control_flow_ops'] += 1
                    
                    # Library calls and heap management
                    if op == 'call':
                        call_target = op_part[-1]
                        
                        # Check for PLT calls (library functions)
                        if '@plt' in call_target:
                            lib_func = call_target.split('@')[0]
                            metrics['library_calls'] += 1
                            metrics['functions'][current_function]['calls'].append(lib_func)
                        
                        # Check for heap operations
                        if match := heap_pattern.search(call_target):
                            func_name = match.group(1)
                            if func_name in heap_ops:
                                metrics['heap_operations'][func_name] += 1

    # Calculate additional statistics
    total_heap_ops = sum(metrics['heap_operations'].values())
    total_mem_ops = metrics['stack_operations'] + total_heap_ops + metrics['memory_access_ops']
    instruction_mix = {
        'control_flow_pct': metrics['control_flow_ops'] / metrics['total_instructions'] * 100 if metrics['total_instructions'] else 0,
        'data_movement_pct': metrics['data_movement_ops'] / metrics['total_instructions'] * 100 if metrics['total_instructions'] else 0,
        'computational_pct': metrics['computational_ops'] / metrics['total_instructions'] * 100 if metrics['total_instructions'] else 0,
        'memory_ops_pct': total_mem_ops / metrics['total_instructions'] * 100 if metrics['total_instructions'] else 0
    }
    
    # Calculate stack metrics
    function_max_stacks = [f['max_stack_frame'] for f in metrics['functions'].values()]
    avg_stack = sum(function_max_stacks) / len(function_max_stacks) if function_max_stacks else 0
    
    metrics.update({
        'instruction_mix': instruction_mix,
        'stack_metrics': {
            'avg_stack_per_function': avg_stack,
            'max_stack_frame': metrics['max_stack_frame']
        },
        'memory_metrics': {
            'total_memory_ops': total_mem_ops,
            'stack_heap_ratio': metrics['stack_operations'] / (total_heap_ops + 0.001)  # avoid division by zero
        }
    })
    
    return metrics

def print_metrics(metrics):
    print("Basic Metrics:")
    print(f"Total Functions: {metrics['total_functions']}")
    print(f"Total Instructions: {metrics['total_instructions']}")
    print(f"Control Flow Operations: {metrics['control_flow_ops']}")
    print(f"Library Calls: {metrics['library_calls']}")
    
    print("\nMemory Analysis:")
    print(f"Stack Operations: {metrics['stack_operations']}")
    print(f"Heap Operations: {metrics['heap_operations']}")
    print(f"Memory Access Operations: {metrics['memory_access_ops']}")
    print(f"Max Stack Frame Size: {metrics['stack_metrics']['max_stack_frame']} bytes")
    print(f"Avg Stack Usage per Function: {metrics['stack_metrics']['avg_stack_per_function']:.2f} bytes")
    print(f"Stack/Heap Ratio: {metrics['memory_metrics']['stack_heap_ratio']:.2f}")
    
    print("\nInstruction Mix (% of total):")
    print(f"Control Flow: {metrics['instruction_mix']['control_flow_pct']:.1f}%")
    print(f"Data Movement: {metrics['instruction_mix']['data_movement_pct']:.1f}%")
    print(f"Computational: {metrics['instruction_mix']['computational_pct']:.1f}%")
    print(f"Memory Operations: {metrics['instruction_mix']['memory_ops_pct']:.1f}%")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python asm_analyzer.py <assembly_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    metrics = analyze_assembly(file_path)
    print_metrics(metrics)