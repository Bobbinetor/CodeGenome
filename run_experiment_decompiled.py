#!/usr/bin/env python3
"""
CodeGenome Decompiled Experiment Runner
Uses decompilation (C pseudocode) instead of disassembly for LLM transformation.

Workflow:
1. Decompile binary functions to C using RetDec
2. LLM transforms C code (objective: evade detection)
3. Recompile transformed C back to binary

Configure the variables below and run:
    python3 run_experiment_decompiled.py
"""

import os
import sys
import time
import subprocess
import shutil
import re
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from typing import Dict, Tuple, Optional

# =============================================================================
# EXPERIMENT CONFIGURATION
# =============================================================================

# 1. INPUT & EXPERIMENT SETTINGS
SOURCE_FILE = "source_code/crypto_aes.c"
EXPERIMENT_NAME = f"exp_decomp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
WORKSPACE_DIR = "workspace/experiments"

# 2. LLM CONFIGURATION
LLM_TIMEOUT = 300
LLM_TEMPERATURE = 0.4
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "deepseek-r1:32b"

# Multi-model configuration
LLM_MODELS = [
    {"model": "deepseek-r1:32b", "variants": 2}, #qwen3-coder:480b-cloud
]

# 3. DECOMPILER
GHIDRA_INSTALL_DIR = os.path.expanduser("~/ghidra")

# 4. COMPILATION
COMPILER = "gcc"
COMPILER_FLAGS = ["-O2", "-std=c99", "-w", "-lssl", "-lcrypto", "-lm"]

# 5. BASELINE
USE_METAME = True
METAME_PATH = "/home/fitnesslab/miniconda3/bin/metame"
METAME_NUM_VARIANTS = 2

# 6. ANALYSIS
RUN_ANALYSIS = True

# =============================================================================
# END CONFIGURATION
# =============================================================================

console = Console()
LOG_FILE = f"experiment_decomp_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
log_file_handle = open(LOG_FILE, 'w', encoding='utf-8')

def log(msg, style="white"):
    """Print styled message to console AND save to log file"""
    console.print(f"[{style}]{msg}[/{style}]")
    clean_msg = re.sub(r'\[/?[^\]]+\]', '', msg)
    log_file_handle.write(f"{datetime.now().strftime('%H:%M:%S')} {clean_msg}\n")
    log_file_handle.flush()


# Models that use <think>...</think> reasoning blocks
THINKING_MODELS = ["deepseek-r1", "qwq", "r1"]

def is_thinking_model(model_name: str) -> bool:
    return any(tm in model_name.lower() for tm in THINKING_MODELS)

def extract_thinking_output(response: str) -> str:
    """Extract output after </think> tag for thinking models."""
    result = response
    for close_tag in ['</think>', '</thinking>', '</reasoning>']:
        if close_tag.lower() in result.lower():
            idx = result.lower().rfind(close_tag.lower())
            if idx != -1:
                result = result[idx + len(close_tag):].strip()
                break
    return result

def check_ollama():
    """Verify Ollama is running and model is available"""
    import requests
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = [m['name'] for m in response.json().get('models', [])]
            if any(OLLAMA_MODEL in m for m in models):
                log(f"✅ Ollama running, model {OLLAMA_MODEL} available", "green")
                return True
            else:
                log(f"❌ Model {OLLAMA_MODEL} not found. Available: {models}", "red")
                return False
    except Exception as e:
        log(f"❌ Ollama connection failed: {e}", "red")
        return False


# =============================================================================
# DECOMPILATION FUNCTIONS (PyGhidra)
# =============================================================================

# Global flag to track if Ghidra is initialized
_ghidra_initialized = False

def init_ghidra():
    """Initialize PyGhidra with Ghidra installation."""
    global _ghidra_initialized
    if _ghidra_initialized:
        return True
    
    try:
        os.environ['GHIDRA_INSTALL_DIR'] = GHIDRA_INSTALL_DIR
        import pyghidra
        pyghidra.start()
        _ghidra_initialized = True
        log(f"✅ PyGhidra initialized with Ghidra at {GHIDRA_INSTALL_DIR}", "green")
        return True
    except Exception as e:
        log(f"❌ PyGhidra initialization failed: {e}", "red")
        return False


def decompile_binary(binary_path: str, output_dir: str) -> Dict[str, str]:
    """
    Decompile binary using PyGhidra (Ghidra's decompiler).
    Returns dict mapping function names to their C code.
    """
    log(f"🔍 Decompiling {binary_path} with Ghidra...", "cyan")
    
    if not init_ghidra():
        return {}
    
    start_time = time.time()
    
    try:
        import pyghidra
        from ghidra.app.decompiler import DecompInterface
        from ghidra.util.task import ConsoleTaskMonitor
        
        functions = {}
        full_code_parts = []
        
        with pyghidra.open_program(binary_path) as flat_api:
            program = flat_api.getCurrentProgram()
            decompiler = DecompInterface()
            decompiler.openProgram(program)
            
            monitor = ConsoleTaskMonitor()
            func_manager = program.getFunctionManager()
            
            # Get all functions
            all_funcs = list(func_manager.getFunctions(True))
            log(f"📝 Found {len(all_funcs)} functions to decompile", "cyan")
            
            for func in all_funcs:
                func_name = func.getName()
                
                # Skip PLT and external functions
                if '@' in func_name or func_name.startswith('_'):
                    continue
                
                try:
                    result = decompiler.decompileFunction(func, 60, monitor)
                    if result and result.decompileCompleted():
                        decomp_func = result.getDecompiledFunction()
                        if decomp_func:
                            c_code = decomp_func.getC()
                            if c_code and len(c_code) > 20:
                                functions[func_name] = c_code
                                full_code_parts.append(c_code)
                                log(f"   ✓ {func_name}: {len(c_code)} chars", "dim")
                except Exception as e:
                    log(f"   ⚠️ Failed to decompile {func_name}: {e}", "yellow")
            
            decompiler.dispose()
        
        decompile_time = time.time() - start_time
        log(f"✅ Decompiled {len(functions)} functions in {decompile_time:.1f}s", "green")
        
        # Save full decompiled output
        full_code = "\n\n".join(full_code_parts)
        output_c = Path(output_dir) / f"{Path(binary_path).stem}_ghidra.c"
        with open(output_c, 'w') as f:
            f.write(full_code)
        log(f"📝 Saved decompiled code: {output_c} ({len(full_code)} chars)", "green")
        
        return {"_full_code": full_code, **functions}
        
    except Exception as e:
        log(f"❌ Decompilation error: {e}", "red")
        import traceback
        traceback.print_exc()
        return {}


def parse_decompiled_functions(code: str) -> Dict[str, str]:
    """
    Parse decompiled C code to extract individual functions.
    Returns dict: function_name -> function_code
    """
    functions = {}
    
    # Pattern for function definitions
    # Matches: type name(args) { ... }
    func_pattern = re.compile(
        r'^(\w[\w\s\*]+?)\s+(\w+)\s*\([^)]*\)\s*\{',
        re.MULTILINE
    )
    
    matches = list(func_pattern.finditer(code))
    
    for i, match in enumerate(matches):
        func_name = match.group(2)
        start = match.start()
        
        # Find the matching closing brace
        brace_count = 0
        end = match.end() - 1  # Start from the opening brace
        
        for j in range(match.end() - 1, len(code)):
            if code[j] == '{':
                brace_count += 1
            elif code[j] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = j + 1
                    break
        
        func_code = code[start:end]
        
        # Skip trivial/wrapper functions
        if len(func_code) > 50 and func_name not in ['main', '_start', '__libc_csu_init']:
            functions[func_name] = func_code
    
    return functions


# =============================================================================
# LLM TRANSFORMATION
# =============================================================================

def call_llm(prompt: str, model: str = None) -> str:
    """Call LLM and return response"""
    import requests
    model_to_use = model or OLLAMA_MODEL
    
    try:
        num_predict = 8192 if is_thinking_model(model_to_use) else 4096
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model_to_use,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": LLM_TEMPERATURE,
                    "num_predict": num_predict,
                }
            },
            timeout=LLM_TIMEOUT
        )
        
        if response.status_code == 200:
            result = response.json().get("response", "").strip()
            if is_thinking_model(model_to_use):
                result = extract_thinking_output(result)
            return result
            
    except Exception as e:
        log(f"❌ LLM error: {e}", "red")
    return ""


def transform_decompiled_code(decompiled_funcs: Dict[str, str], variant_num: int, model: str = None) -> Dict:
    """
    Transform decompiled C code using LLM.
    
    Returns:
        Dict with keys: 'success', 'code', 'gen_time'
    """
    start_time = time.time()
    model_display = model or OLLAMA_MODEL
    
    log(f"🧠 LLM transforming decompiled code (model: {model_display})...", "cyan")
    
    # Get full code or concatenate functions
    if "_full_code" in decompiled_funcs:
        original_code = decompiled_funcs["_full_code"]
    else:
        original_code = "\n\n".join(decompiled_funcs.values())
    
    # Truncate if too long for context
    if len(original_code) > 8000:
        original_code = original_code[:8000] + "\n// ... (truncated)"
    
    prompt = f"""You are a metamorphic code transformation engine.

OBJECTIVE: Transform this C code to evade detection while preserving EXACT functionality.
The original and transformed versions MUST produce identical output for all inputs.

INPUT CODE:
```c
{original_code}
```

TRANSFORMATION GOAL:
- Maximize code divergence from original
- Apply any techniques you deem effective:
  * Control flow restructuring (for→while, if→switch, etc.)
  * Variable renaming and type changes
  * Expression rewrites (algebraic equivalents)
  * Code reordering
  * Dead code injection (that doesn't affect output)
  * Loop transformations
  * Function inlining or extraction
  * Pointer/array conversions
  
CRITICAL: The code MUST compile with gcc and produce IDENTICAL behavior.

OUTPUT: Provide ONLY the complete transformed C code, no explanations.
The code must include all necessary headers and be self-contained.

```c
"""
    
    response = call_llm(prompt, model)
    gen_time = time.time() - start_time
    
    if not response:
        return {"success": False, "error": "No LLM response", "gen_time": gen_time}
    
    # Extract C code from response
    code = extract_c_code(response)
    
    if not code:
        return {"success": False, "error": "No valid C code extracted", "gen_time": gen_time}
    
    log(f"✅ LLM generated {len(code)} chars in {gen_time:.1f}s", "green")
    
    return {"success": True, "code": code, "gen_time": gen_time}


def extract_c_code(response: str) -> str:
    """Extract C code from LLM response"""
    # Try markdown code blocks first
    match = re.search(r'```(?:c|cpp)?\s*(.*?)```', response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        if '#include' in code or 'int ' in code or 'void ' in code:
            return code
    
    # Fallback: find code starting with #include or function
    lines = response.split('\n')
    start_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith('#include') or re.match(r'^\s*(int|void|char|double|float|long)\s+\w+', line):
            start_idx = i
            break
    
    if start_idx != -1:
        return '\n'.join(lines[start_idx:]).strip()
    
    return ""


# =============================================================================
# RECOMPILATION
# =============================================================================

def compile_code(source_path: str, binary_path: str) -> Tuple[bool, str]:
    """Compile C code, returns (success, error_message)"""
    cmd = [COMPILER, "-o", binary_path, source_path] + COMPILER_FLAGS
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return True, ""
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)


# =============================================================================
# MAIN EXPERIMENT
# =============================================================================

def generate_metame_variant(original_binary: str, output_path: str) -> dict:
    """Generate a MetaME variant"""
    if not os.path.exists(METAME_PATH):
        return {"success": False, "error": f"MetaME not found at {METAME_PATH}"}
    
    cmd = [METAME_PATH, "-i", str(original_binary), "-o", str(output_path), "--debug"]
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        gen_time = time.time() - start_time
        
        if result.returncode == 0 and os.path.exists(output_path):
            return {"success": True, "gen_time": gen_time}
        else:
            return {"success": False, "error": f"MetaME failed: {result.stderr[:200]}", "gen_time": gen_time}
    except Exception as e:
        return {"success": False, "error": str(e), "gen_time": time.time() - start_time}


def run_decompiled_experiment():
    """Main experiment runner for decompiled approach."""
    
    log("=" * 60, "blue")
    log(f"🧬 CodeGenome DECOMPILED Experiment: {EXPERIMENT_NAME}", "bold blue")
    log("=" * 60, "blue")
    
    # Print configuration
    table = Table(title="Decompiled Experiment Configuration")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Mode", "DECOMPILED (C-level)", style="bold magenta")
    table.add_row("Source File", SOURCE_FILE)
    table.add_row("Decompiler", "Ghidra (PyGhidra)")
    table.add_row("LLM Model", OLLAMA_MODEL)
    total_variants = sum(m.get("variants", 1) for m in LLM_MODELS)
    table.add_row("LLM Variants", str(total_variants))
    table.add_row("Workspace", WORKSPACE_DIR)
    
    console.print(table)
    print()
    
    # Check prerequisites
    if not check_ollama():
        return
    
    # Load and compile original source
    if not os.path.exists(SOURCE_FILE):
        log(f"❌ Source file not found: {SOURCE_FILE}", "red")
        return
    
    # Create workspace
    workspace = Path(WORKSPACE_DIR)
    workspace.mkdir(exist_ok=True)
    
    exp_dir = workspace / EXPERIMENT_NAME
    exp_dir.mkdir(exist_ok=True)
    log(f"📁 Experiment directory: {exp_dir}", "green")
    
    # Compile original
    source_name = Path(SOURCE_FILE).stem
    original_binary = exp_dir / f"{source_name}_original"
    
    success, error = compile_code(SOURCE_FILE, str(original_binary))
    if not success:
        log(f"❌ Original compilation failed: {error}", "red")
        return
    
    log(f"✅ Original compiled: {original_binary}", "green")
    
    # Step 1: Decompile
    decompiled = decompile_binary(str(original_binary), str(exp_dir))
    
    if not decompiled:
        log("❌ Decompilation failed, cannot continue", "red")
        return
    
    # Save decompiled code
    decomp_path = exp_dir / f"{source_name}_decompiled.c"
    with open(decomp_path, 'w') as f:
        f.write(decompiled.get("_full_code", ""))
    log(f"📝 Saved decompiled: {decomp_path}", "green")
    
    results = []
    successful_variants = []
    
    # Step 2: Generate LLM variants
    models_to_use = LLM_MODELS if LLM_MODELS else [{"model": OLLAMA_MODEL, "variants": 1}]
    
    variant_counter = 0
    for model_config in models_to_use:
        model_name = model_config["model"]
        num_variants = model_config.get("variants", 1)
        model_short = model_name.split(":")[0].replace("-", "_")
        
        log(f"\n{'='*60}", "white")
        log(f"🤖 Model: {model_name} ({num_variants} variants)", "bold magenta")
        log(f"{'='*60}", "white")
        
        for i in range(1, num_variants + 1):
            variant_counter += 1
            log(f"\n{'='*40}", "white")
            log(f"🔄 Generating Decompiled Variant {i}/{num_variants}", "bold cyan")
            log(f"{'='*40}", "white")
            
            result = transform_decompiled_code(decompiled, variant_counter, model=model_name)
            
            if result["success"]:
                # Save transformed C
                variant_c_path = exp_dir / f"{source_name}_decomp_{model_short}_v{i:02d}.c"
                with open(variant_c_path, 'w') as f:
                    f.write(result["code"])
                
                # Compile
                variant_binary = exp_dir / f"{source_name}_decomp_{model_short}_v{i:02d}"
                success, error = compile_code(str(variant_c_path), str(variant_binary))
                
                if success:
                    log(f"✅ {model_short} V{i}: Compiled successfully ({result['gen_time']:.1f}s)", "green")
                    successful_variants.append(str(variant_binary))
                    results.append({
                        "variant": f"{model_short}_decomp_V{i}",
                        "model": model_name,
                        "success": True,
                        "gen_time": result["gen_time"],
                        "description": "LLM decompiled transformation"
                    })
                else:
                    log(f"❌ {model_short} V{i}: Compilation failed: {error[:100]}", "red")
                    results.append({
                        "variant": f"{model_short}_decomp_V{i}",
                        "model": model_name,
                        "success": False,
                        "gen_time": result["gen_time"],
                        "description": f"Compilation failed: {error[:50]}"
                    })
            else:
                log(f"❌ {model_short} V{i}: {result.get('error', 'Unknown error')}", "red")
                results.append({
                    "variant": f"{model_short}_decomp_V{i}",
                    "model": model_name,
                    "success": False,
                    "gen_time": result.get("gen_time", 0),
                    "description": result.get("error", "Unknown error")
                })
    
    # Step 3: MetaME variants for comparison
    if USE_METAME and os.path.exists(METAME_PATH):
        log(f"\n{'='*40}", "dim")
        log(f"🧬 Generating MetaME Variants ({METAME_NUM_VARIANTS})", "bold magenta")
        log(f"{'='*40}", "dim")
        
        for i in range(1, METAME_NUM_VARIANTS + 1):
            variant_path = exp_dir / f"{source_name}_metame_v{i:02d}"
            meta_result = generate_metame_variant(str(original_binary), str(variant_path))
            
            if meta_result["success"]:
                log(f"✅ MetaME V{i}: Generated ({meta_result['gen_time']:.1f}s)", "green")
                successful_variants.append(str(variant_path))
                results.append({
                    "variant": f"MetaME_V{i}",
                    "success": True,
                    "gen_time": meta_result["gen_time"],
                    "description": "MetaME binary transformation"
                })
            else:
                log(f"❌ MetaME V{i}: {meta_result.get('error', 'Failed')}", "red")
    
    # Step 4: Run analysis
    if RUN_ANALYSIS and successful_variants:
        log("\n" + "="*60, "blue")
        log("📊 Running Advanced Binary Analysis...", "bold blue")
        log("="*60, "blue")
        
        try:
            from advanced_binary_analyzer import AdvancedBinaryAnalyzer
            analyzer = AdvancedBinaryAnalyzer(console, exp_dir)
            all_binaries = [str(original_binary)] + successful_variants
            analyzer.analyze_multiple_binaries_advanced(all_binaries, str(exp_dir / "analysis_results"))
        except Exception as e:
            log(f"❌ Analysis error: {e}", "red")
    
    # Summary
    log(f"\n{'='*60}", "blue")
    log("📊 DECOMPILED EXPERIMENT SUMMARY", "bold blue")
    log(f"{'='*60}", "blue")
    
    summary_table = Table()
    summary_table.add_column("Variant", style="cyan")
    summary_table.add_column("Status", style="green")
    summary_table.add_column("Time", style="yellow")
    summary_table.add_column("Description", style="dim")
    
    for r in results:
        status = "✅ Success" if r["success"] else "❌ Failed"
        gen_time = f"{r.get('gen_time', 0):.1f}s"
        desc = r.get("description", "N/A")[:40]
        summary_table.add_row(r["variant"], status, gen_time, desc)
    
    console.print(summary_table)
    
    log(f"\n✅ Generated {len(successful_variants)} successful variants", "green" if successful_variants else "red")
    log(f"🎉 Decompiled Experiment complete! Results in: {exp_dir}", "bold green")
    log(f"📝 Log saved to: {LOG_FILE}", "dim")
    
    log_file_handle.close()
    
    return results


if __name__ == "__main__":
    run_decompiled_experiment()
