#!/usr/bin/env python3
"""
Enhanced Agentic System for Code Variant Generation
Focuses on maximum binary differentiation while preserving functionality
"""

import ast
import os
import re
import subprocess
import tempfile
import uuid
import json
import time
from typing import List, Dict, Tuple, Optional, Any
from pathlib import Path
from dataclasses import dataclass
import requests
from rich.console import Console

@dataclass
class TestCase:
    """Represents a test case for functional equivalence"""
    name: str
    input_args: List[str]
    input_stdin: str
    expected_output: str
    expected_exit_code: int
    timeout: int = 10

@dataclass
class TransformationStrategy:
    """Defines code transformation strategies for maximum binary differentiation"""
    name: str
    description: str
    prompt_section: str
    priority: int

class EnhancedAgenticSystem:
    """Enhanced AI-powered code variant generation with comprehensive testing"""
    
    def __init__(self, config, console: Console, workspace: Path):
        self.config = config
        self.console = console
        self.workspace = workspace
        
        # Create test suites directory
        self.test_suites_dir = workspace / "test_suites"
        self.test_suites_dir.mkdir(exist_ok=True)
        
        # Transformation strategies for maximum binary differentiation
        self.transformation_strategies = [
            TransformationStrategy(
                name="control_flow_restructuring",
                description="Replace loops (for/while/do-while), conditionals (if/switch), and control structures",
                prompt_section="""
- Convert for loops to while loops or vice versa
- Replace if-else chains with switch statements or vice versa
- Use different loop patterns (recursive vs iterative)
- Change loop direction (forward vs backward iteration)
- Use different break/continue patterns""",
                priority=1
            ),
            TransformationStrategy(
                name="data_structure_transformation",
                description="Change variable types, names, and data organization",
                prompt_section="""
- Use different variable names with semantic meaning
- Change data types where possible (int vs long, array vs pointer arithmetic)
- Reorganize variable declarations (separate vs combined)
- Use different initialization patterns
- Change variable scope and lifetime""",
                priority=2
            ),
            TransformationStrategy(
                name="algorithmic_equivalence",
                description="Use mathematically equivalent but different algorithms",
                prompt_section="""
- Use different mathematical formulas that produce same results
- Change computation order (left-to-right vs right-to-left)
- Use lookup tables vs direct computation
- Apply different optimization techniques
- Use different accumulation patterns""",
                priority=3
            ),
            TransformationStrategy(
                name="memory_access_patterns",
                description="Change how memory is accessed and managed",
                prompt_section="""
- Use different array indexing patterns
- Change memory allocation strategies
- Use different pointer arithmetic approaches
- Modify buffer handling techniques
- Change string processing methods""",
                priority=4
            ),
            TransformationStrategy(
                name="function_organization",
                description="Restructure functions and code organization",
                prompt_section="""
- Break monolithic functions into smaller ones or vice versa
- Change function parameter passing (by value vs by reference)
- Use different return value strategies
- Modify error handling approaches
- Change code organization and structure""",
                priority=5
            ),
            TransformationStrategy(
                name="system_calls_variation",
                description="Use different system calls and library functions",
                prompt_section="""
- Use alternative library functions with same functionality
- Change I/O methods (printf vs puts, scanf vs fgets)
- Use different file handling approaches
- Modify process/thread management calls
- Change error checking and handling patterns""",
                priority=6
            )
        ]
    
    def analyze_source_complexity(self, source_code: str) -> Dict[str, Any]:
        """Analyze source code to determine appropriate transformation strategies"""
        analysis = {
            'has_loops': bool(re.search(r'\b(for|while|do)\b', source_code)),
            'has_conditionals': bool(re.search(r'\bif\b', source_code)),
            'has_functions': bool(re.search(r'\w+\s*\([^)]*\)\s*{', source_code)),
            'has_arrays': bool(re.search(r'\w+\[\w*\]', source_code)),
            'has_pointers': bool(re.search(r'\*\w+|\w+\s*\*', source_code)),
            'has_structs': bool(re.search(r'\bstruct\b', source_code)),
            'has_syscalls': bool(re.search(r'\b(printf|scanf|malloc|free|getpid|open|close|read|write)\b', source_code)),
            'complexity_score': len(source_code.split('\n')),
            'include_count': len(re.findall(r'#include', source_code)),
            'variable_count': len(set(re.findall(r'\b[a-zA-Z_]\w*\b', source_code)))
        }
        
        # Determine applicable transformation strategies
        analysis['applicable_strategies'] = []
        
        if analysis['has_loops'] or analysis['has_conditionals']:
            analysis['applicable_strategies'].append('control_flow_restructuring')
        
        if analysis['variable_count'] > 5:
            analysis['applicable_strategies'].append('data_structure_transformation')
            
        if analysis['complexity_score'] > 20:
            analysis['applicable_strategies'].append('algorithmic_equivalence')
            
        if analysis['has_arrays'] or analysis['has_pointers']:
            analysis['applicable_strategies'].append('memory_access_patterns')
            
        if analysis['has_functions']:
            analysis['applicable_strategies'].append('function_organization')
            
        if analysis['has_syscalls']:
            analysis['applicable_strategies'].append('system_calls_variation')
        
        return analysis
    
    def generate_comprehensive_prompt(self, source_code: str, variant_number: int) -> str:
        """Generate comprehensive prompt for maximum binary differentiation"""
        
        analysis = self.analyze_source_complexity(source_code)
        
        # Ultra-concise prompt optimized for gemma3:12b
        if variant_number == 1:
            transformation_focus = "Change for→while loops, int→long variables, rename all variables"
        elif variant_number == 2:
            transformation_focus = "Use backward iteration, arrays instead of scalars, different math"
        else:
            transformation_focus = "Recursive approach, helper functions, reorganize computation"

        prompt = f"""Transform this C code with {transformation_focus} while keeping EXACT same output:

{source_code}

Requirements:
- Identical output and behavior
- Different variable names  
- Different loop types
- Compilable C code

Transformed code:"""

        return prompt
    
    def generate_test_cases_from_source(self, source_code: str, binary_path: str) -> List[TestCase]:
        """Automatically generate test cases from source analysis"""
        test_cases = []
        
        # Basic execution test
        try:
            result = subprocess.run([binary_path], capture_output=True, text=True, timeout=10)
            test_cases.append(TestCase(
                name="basic_execution",
                input_args=[],
                input_stdin="",
                expected_output=result.stdout,
                expected_exit_code=result.returncode
            ))
        except Exception as e:
            self.console.print(f"[red]❌ Failed to generate basic test case: {e}[/red]")
        
        # If program accepts arguments, test with different args
        if re.search(r'argc|argv', source_code):
            for args in [["test"], ["1", "2", "3"], ["--help"]]:
                try:
                    result = subprocess.run([binary_path] + args, capture_output=True, text=True, timeout=10)
                    test_cases.append(TestCase(
                        name=f"args_{'_'.join(args)}",
                        input_args=args,
                        input_stdin="",
                        expected_output=result.stdout,
                        expected_exit_code=result.returncode
                    ))
                except:
                    continue
        
        # If program uses stdin, test with input
        if re.search(r'scanf|gets|fgets|getchar', source_code):
            test_inputs = ["test input\n", "123\n", "multiple\nlines\nof\ninput\n"]
            for stdin_input in test_inputs:
                try:
                    result = subprocess.run([binary_path], input=stdin_input, capture_output=True, text=True, timeout=10)
                    test_cases.append(TestCase(
                        name=f"stdin_{len(stdin_input)}chars",
                        input_args=[],
                        input_stdin=stdin_input,
                        expected_output=result.stdout,
                        expected_exit_code=result.returncode
                    ))
                except:
                    continue
        
        # Multiple runs to check consistency
        for i in range(3):
            try:
                result = subprocess.run([binary_path], capture_output=True, text=True, timeout=10)
                test_cases.append(TestCase(
                    name=f"consistency_run_{i+1}",
                    input_args=[],
                    input_stdin="",
                    expected_output=result.stdout,
                    expected_exit_code=result.returncode
                ))
            except:
                continue
        
        return test_cases
    
    def save_test_suite(self, variant_id: str, test_cases: List[TestCase], original_source: str) -> str:
        """Save test suite to dedicated folder for visibility"""
        test_suite_dir = self.test_suites_dir / variant_id
        test_suite_dir.mkdir(exist_ok=True)
        
        # Save test cases as JSON
        test_cases_data = []
        for tc in test_cases:
            test_cases_data.append({
                'name': tc.name,
                'input_args': tc.input_args,
                'input_stdin': tc.input_stdin,
                'expected_output': tc.expected_output,
                'expected_exit_code': tc.expected_exit_code,
                'timeout': tc.timeout
            })
        
        test_cases_file = test_suite_dir / "test_cases.json"
        with open(test_cases_file, 'w') as f:
            json.dump(test_cases_data, f, indent=2)
        
        # Create test runner script
        test_runner_script = f"""#!/usr/bin/env python3
'''
Automated test runner for variant {variant_id}
Generated by Enhanced Agentic System
'''

import subprocess
import sys
import json
from pathlib import Path

def run_test(binary_path, test_case):
    try:
        result = subprocess.run(
            [binary_path] + test_case['input_args'],
            input=test_case['input_stdin'],
            capture_output=True,
            text=True,
            timeout=test_case['timeout']
        )
        
        # Check exit code
        if result.returncode != test_case['expected_exit_code']:
            return False, f"Exit code mismatch: expected {{test_case['expected_exit_code']}}, got {{result.returncode}}"
        
        # Check output (normalize whitespace and handle PID differences)
        expected = test_case['expected_output'].strip().replace('\\r\\n', '\\n')
        actual = result.stdout.strip().replace('\\r\\n', '\\n')
        
        # Handle Process ID differences (PIDs change between runs)
        import re
        expected_normalized = re.sub(r'Process ID: \\d+', 'Process ID: [PID]', expected)
        actual_normalized = re.sub(r'Process ID: \\d+', 'Process ID: [PID]', actual)
        
        if expected_normalized != actual_normalized:
            return False, f"Output mismatch:\\nExpected: {{repr(expected_normalized)}}\\nActual: {{repr(actual_normalized)}}"
        
        return True, "PASS"
        
    except subprocess.TimeoutExpired:
        return False, f"Test timed out after {{test_case['timeout']}} seconds"
    except Exception as e:
        return False, f"Test execution failed: {{str(e)}}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_runner.py <binary_path>")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    
    # Load test cases
    with open('test_cases.json', 'r') as f:
        test_cases = json.load(f)
    
    print(f"Running {{len(test_cases)}} test cases for {{binary_path}}")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {{i}}: {{test_case['name']}}", end=" ... ")
        
        success, details = run_test(binary_path, test_case)
        
        if success:
            print("✅ PASS")
            passed += 1
        else:
            print("❌ FAIL")
            print(f"  {{details}}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {{passed}} passed, {{failed}} failed")
    print(f"Success rate: {{passed/(passed+failed)*100:.1f}}%")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
"""
        
        test_runner_file = test_suite_dir / "test_runner.py"
        with open(test_runner_file, 'w') as f:
            f.write(test_runner_script)
        
        # Make test runner executable
        test_runner_file.chmod(0o755)
        
        # Save original source for reference
        original_source_file = test_suite_dir / "original_source.c"
        with open(original_source_file, 'w') as f:
            f.write(original_source)
        
        # Create README for the test suite
        readme_content = f"""# Test Suite for Variant {variant_id}

## Overview
This directory contains the comprehensive test suite for validating functional equivalence between the original source code and the generated variant.

## Files
- `test_cases.json`: All test cases in JSON format
- `test_runner.py`: Python script to run tests against any binary
- `original_source.c`: Original source code for reference

## Usage
```bash
# Test a binary
python3 test_runner.py /path/to/binary

# View test cases
cat test_cases.json
```

## Test Cases
Total test cases: {len(test_cases)}

Test types:
- Basic execution tests
- Multiple run consistency tests  
- Input/output validation tests
- Edge case tests

## Generated by
Enhanced Agentic System - CodeGenome Suite v3.0
"""
        
        readme_file = test_suite_dir / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        self.console.print(f"[green]📁 Test suite saved to: {test_suite_dir}[/green]")
        return str(test_suite_dir)
    
    def execute_test_case(self, binary_path: str, test_case: TestCase) -> Tuple[bool, str]:
        """Execute a test case and return success status and details"""
        try:
            result = subprocess.run(
                [binary_path] + test_case.input_args,
                input=test_case.input_stdin,
                capture_output=True,
                text=True,
                timeout=test_case.timeout
            )
            
            # Check exit code
            if result.returncode != test_case.expected_exit_code:
                return False, f"Exit code mismatch: expected {test_case.expected_exit_code}, got {result.returncode}"
            
            # Check output (normalize whitespace and line endings, ignore PID differences)
            expected_clean = test_case.expected_output.strip().replace('\r\n', '\n')
            actual_clean = result.stdout.strip().replace('\r\n', '\n')
            
            # Handle Process ID differences (PIDs change between runs)
            import re
            expected_normalized = re.sub(r'Process ID: \d+', 'Process ID: [PID]', expected_clean)
            actual_normalized = re.sub(r'Process ID: \d+', 'Process ID: [PID]', actual_clean)
            
            if expected_normalized != actual_normalized:
                return False, f"Output mismatch:\nExpected: {repr(expected_normalized)}\nActual: {repr(actual_normalized)}"
            
            return True, "Test passed"
            
        except subprocess.TimeoutExpired:
            return False, f"Test timed out after {test_case.timeout} seconds"
        except Exception as e:
            return False, f"Test execution failed: {str(e)}"
    
    def validate_variant_with_tests(self, original_binary: str, variant_binary: str, test_cases: List[TestCase]) -> Tuple[bool, Dict[str, Any]]:
        """Validate variant against original using comprehensive test cases"""
        
        results = {
            'total_tests': len(test_cases),
            'passed_tests': 0,
            'failed_tests': [],
            'success_rate': 0.0,
            'validation_time': time.time()
        }
        
        for test_case in test_cases:
            # Test original (should always pass since we generated tests from it)
            orig_success, orig_details = self.execute_test_case(original_binary, test_case)
            
            # Test variant
            var_success, var_details = self.execute_test_case(variant_binary, test_case)
            
            if orig_success and var_success:
                results['passed_tests'] += 1
            else:
                results['failed_tests'].append({
                    'test_name': test_case.name,
                    'original_result': orig_details,
                    'variant_result': var_details
                })
        
        results['success_rate'] = results['passed_tests'] / results['total_tests'] if results['total_tests'] > 0 else 0.0
        results['validation_time'] = time.time() - results['validation_time']
        
        return results['success_rate'] == 1.0, results
    
    def call_llm(self, prompt: str, use_fast_model: bool = False) -> str:
        """Call LLM with enhanced prompt"""
        # Use faster model for fallback
        model = "gemma3:1b" if use_fast_model else self.config.ollama_model
        timeout = 30 if use_fast_model else 45
        
        try:
            response = requests.post(
                f"{self.config.ollama_base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.4,  # Slightly higher for creative transformations
                        "num_predict": 2048 if use_fast_model else 4096,  # Faster for light model
                        "top_p": 0.85,       # Slightly more focused
                        "top_k": 30          # More focused selection
                    }
                },
                timeout=timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "").strip()
                
        except Exception as e:
            self.console.print(f"[red]❌ LLM call failed: {e}[/red]")
            
        return ""
    
    def extract_c_code(self, llm_response: str) -> str:
        """Extract C code from LLM response, handling various formats"""
        # Remove markdown code blocks
        code_block_pattern = r'```(?:c|cpp)?\s*(.*?)\s*```'
        matches = re.findall(code_block_pattern, llm_response, re.DOTALL)
        
        if matches:
            code = matches[0].strip()
            # Basic validation: ensure it has main function and includes
            if 'int main(' in code and '#include' in code:
                return code
        
        # If no code blocks, look for #include statements as start
        lines = llm_response.split('\n')
        start_idx = -1
        end_idx = len(lines)
        
        for i, line in enumerate(lines):
            if line.strip().startswith('#include') and start_idx == -1:
                start_idx = i
            elif line.strip().startswith('//') and ('explanation' in line.lower() or 'note' in line.lower()):
                end_idx = i
                break
        
        if start_idx != -1:
            code = '\n'.join(lines[start_idx:end_idx]).strip()
            # Basic validation
            if 'int main(' in code and '#include' in code:
                return code
        
        # Fallback: try to find any C-like code structure
        if 'int main(' in llm_response and '#include' in llm_response:
            return llm_response.strip()
        
        return ""
    
    def compile_code(self, source_file: str, output_file: str) -> Tuple[bool, str]:
        """Compile C code and return success status and details"""
        try:
            result = subprocess.run(
                ['gcc', '-o', output_file, source_file, '-w'],  # -w suppresses warnings
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return True, "Compilation successful"
            else:
                return False, f"Compilation failed:\n{result.stderr}"
                
        except Exception as e:
            return False, f"Compilation error: {str(e)}"
    
    def generate_enhanced_variant(self, source_path: str, variant_number: int = 1) -> Optional[Dict[str, Any]]:
        """Generate a single enhanced variant with comprehensive validation"""
        
        # Read source code
        with open(source_path, 'r') as f:
            source_code = f.read()
        
        # Generate variant ID
        variant_id = f"enhanced_ai_variant_{variant_number}_{uuid.uuid4().hex[:8]}"
        
        self.console.print(f"[cyan]🔄 Generating enhanced variant: {variant_id}[/cyan]")
        
        # Generate comprehensive prompt
        prompt = self.generate_comprehensive_prompt(source_code, variant_number)
        
        # Call LLM with retry logic
        self.console.print("[yellow]🤖 Calling AI model for variant generation (this may take time with 12b model)...[/yellow]")
        llm_response = self.call_llm(prompt)
        
        # If no response, try with faster model and intermediate prompt
        if not llm_response:
            self.console.print("[yellow]⚠️ 12b model timeout, switching to gemma3:1b with intermediate prompt...[/yellow]")
            intermediate_prompt = f"""Transform this C code while keeping identical functionality:

{source_code}

Apply these changes:
- Rename all variables (sum→total, i→counter)
- Change for loops to while loops
- Use long instead of int where possible
- Keep exact same output

C code:"""
            
            llm_response = self.call_llm(intermediate_prompt, use_fast_model=True)
        
        # Final fallback to focused simple prompt with fast model
        if not llm_response:
            self.console.print("[yellow]⚠️ Trying focused simple prompt with fast model...[/yellow]")
            simple_prompt = f"""Rewrite this C code with different variable names and while loop instead of for loop:

{source_code}

Requirements:
- Change "sum" to "total" 
- Change "int i" to "int counter"
- Change for loop to while loop
- Keep same functionality

Modified C code:"""
            
            llm_response = self.call_llm(simple_prompt, use_fast_model=True)
        
        if not llm_response:
            self.console.print("[red]❌ No response from AI model even with simplified prompt[/red]")
            return None
        
        # Extract C code
        variant_code = self.extract_c_code(llm_response)
        
        if not variant_code:
            self.console.print("[red]❌ No valid C code extracted from response[/red]")
            return None
        
        # Save variant source
        variant_source_path = self.workspace / f"{variant_id}.c"
        with open(variant_source_path, 'w') as f:
            f.write(variant_code)
        
        self.console.print(f"[green]📝 Saved variant source: {variant_source_path}[/green]")
        
        # Compile variant
        variant_binary_path = self.workspace / variant_id
        compile_success, compile_details = self.compile_code(str(variant_source_path), str(variant_binary_path))
        
        if not compile_success:
            self.console.print(f"[red]❌ Compilation failed: {compile_details}[/red]")
            return None
        
        self.console.print(f"[green]⚙️ Compiled variant binary: {variant_binary_path}[/green]")
        
        # Compile original for comparison
        original_binary_path = self.workspace / f"original_{uuid.uuid4().hex[:6]}"
        compile_success, compile_details = self.compile_code(source_path, str(original_binary_path))
        
        if not compile_success:
            self.console.print(f"[red]❌ Original compilation failed: {compile_details}[/red]")
            return None
        
        # Generate test cases from original
        self.console.print("[blue]🧪 Generating test cases...[/blue]")
        test_cases = self.generate_test_cases_from_source(source_code, str(original_binary_path))
        
        if not test_cases:
            self.console.print("[yellow]⚠️ No test cases generated, creating basic test[/yellow]")
            # Create a basic test case
            try:
                result = subprocess.run([str(original_binary_path)], capture_output=True, text=True, timeout=10)
                test_cases = [TestCase(
                    name="basic_test",
                    input_args=[],
                    input_stdin="",
                    expected_output=result.stdout,
                    expected_exit_code=result.returncode
                )]
            except Exception as e:
                self.console.print(f"[red]❌ Failed to create basic test: {e}[/red]")
                return None
        
        self.console.print(f"[blue]🧪 Generated {len(test_cases)} test cases[/blue]")
        
        # Save test suite to dedicated folder
        with open(source_path, 'r') as f:
            original_source = f.read()
        
        test_suite_path = self.save_test_suite(variant_id, test_cases, original_source)
        
        # Validate variant
        self.console.print("[blue]🔍 Validating functional equivalence...[/blue]")
        validation_success, validation_results = self.validate_variant_with_tests(
            str(original_binary_path), str(variant_binary_path), test_cases
        )
        
        if validation_success:
            self.console.print(f"[green]✅ Variant validated successfully! Success rate: {validation_results['success_rate']*100:.1f}%[/green]")
            
            # Clean up original binary
            original_binary_path.unlink()
            
            return {
                'variant_id': variant_id,
                'source_path': str(variant_source_path),
                'binary_path': str(variant_binary_path),
                'validation_results': validation_results,
                'test_cases': len(test_cases),
                'test_suite_path': test_suite_path,
                'source_code': variant_code
            }
        else:
            self.console.print(f"[red]❌ Variant validation failed! Success rate: {validation_results['success_rate']*100:.1f}%[/red]")
            self.console.print(f"[red]Failed tests: {len(validation_results['failed_tests'])}[/red]")
            
            # Show details of first few failed tests
            for i, failed_test in enumerate(validation_results['failed_tests'][:3]):
                self.console.print(f"[yellow]Test {i+1} '{failed_test['test_name']}': {failed_test['variant_result']}[/yellow]")
            
            # Keep files for debugging, clean up original binary only
            original_binary_path.unlink() if original_binary_path.exists() else None
            
            self.console.print(f"[yellow]Debug: Variant files kept at {variant_source_path} for analysis[/yellow]")
            
            return None