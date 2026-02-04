# How to Run CodeGenome Experiments

This guide explains how to configure and run the obfuscation experiments using the CodeGenome suite.

## 🚀 Quick Start
To run the default comprehensive experiment (LLM vs MetaME vs Tigress):

```bash
cd ~/KNOSYS_work/CodeGenome
python3 run_experiment.py
```

## ⚙️ Configuration
Open `run_experiment.py` and modify the "CONFIGURATION" section at the top.

### 1. Enable/Disable Generators
```python
USE_LLM = True          # Enable AI (Gemma/DeepSeek) generation
USE_METAME = True       # Enable Assembly Metamorphism
USE_TIGRESS = True      # Enable Source-to-Source Obfuscation
```

### 2. Tigress Presets (Advanced)
We have implemented 4 obfuscation strategies that rotate automatically for each variant. Set `TIGRESS_NUM_VARIANTS` to 4 or more to see them all.

| Preset | Description | Strategy |
|:---|:---|:---|
| **Virtualize** | **High Evasion**. Converts code to a custom bytecode interpreter. | `Virtualize + Dispatch=switch` |
| **Data Hiding** | **Math Obfuscation**. Encodes numbers and strings. | `EncodeLiterals + EncodeArithmetic` |
| **Hardening** | **Anti-Analysis**. Flattens flow + adds fake branches. | `Flatten + AddOpaque` |
| **JIT** | **Complexity**. Compiles code to binary at runtime. | `Jit` |

To change the number of Tigress variants:
```python
TIGRESS_NUM_VARIANTS = 4 
```

### 4. Experiment Mode (Source vs Binary)
You can now choose between two comparison modes:

```python
EXPERIMENT_MODE = "source"   # LLM (C) vs Tigress  -> Works on source code
EXPERIMENT_MODE = "binary"   # LLM (ASM) vs MetaME -> Works on compiled binary only
```

**Binary Mode** is useful for:
- Fair comparison with MetaME (both start from binary)
- Testing LLM's ability to understand and rewrite assembly
- Scenarios where source code is unavailable

Binary mode settings:
```python
DISASSEMBLER = "objdump"       # or "radare2"
ASM_SYNTAX = "intel"           # or "att"
REASSEMBLY_METHOD = "r2patch"  # or "keystone", "nasm"
LLM_ASM_NUM_VARIANTS = 2       # How many LLM ASM variants
```

### 3. Source File
To target a different C file:
```python
SOURCE_FILE = "source_code/my_program.c"
```
The script will **automatically discover function names** to target for obfuscation.

## 📊 Results
Outputs are saved in `workspace/exp_YYYYMMDD_HHMMSS/`.

*   **HTML/CSV Reports**: `results_complete.csv`
*   **Distance Matrices**: `distance_matrix_euclidean.csv` (Structural diversity)
*   **Radar Charts**: Check the `analysis_results` subfolder for visualizations.

## 🛠️ Troubleshooting
*   **Tigress Error**: If you see errors, check `workspace/tigress_install`.
*   **Missing CSVs**: Ensure `advanced_binary_analyzer.py` is up to date (we patched it to save matrices).
