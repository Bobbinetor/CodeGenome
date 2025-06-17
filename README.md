# CodeGenome Suite v3.0 - Enhanced Agentic AI Edition

Professional terminal application for AI-powered code variant generation using **gemma3:12b**.

## Quick Start

```bash
# 1. Install Ollama and model
ollama pull gemma3:12b

# 2. Install dependencies
pip install -r requirements.txt

# 3. Interactive mode (full featured)
python3 codegenome.py

# 4. Direct generation mode
python3 codegenome.py generate source_code/simple_test.c
```

## Features

### 🖥️ Professional Terminal Interface
- **Interactive CLI** with rich UI and menus
- **Direct mode** for automation and scripting
- **Status dashboard** with real-time information
- **Progress tracking** with visual feedback

### 🧬 Advanced AI Transformations
- **6 transformation strategies** for maximum binary differentiation
- **Enhanced validation** with comprehensive testing
- **Automatic test suite generation** for each variant
- **100% functional equivalence** guarantee

### 📊 Example Transformation

**Original:**
```c
int sum = 0;
for (int i = 0; i < 100; i++) {
    sum += i;
}
printf("Sum: %d\n", sum);
```

**AI-Generated:**
```c
long total = 0;
int counter = 0;
while (counter < 100) {
    total += counter;
    counter++;
}
printf("Sum: %ld\n", total);
```

## Usage Modes

### Interactive Mode (Recommended)
```bash
python3 codegenome.py
# or
python3 codegenome.py interactive
```

**Features:**
- 📁 Load and analyze binaries
- 📄 Load source files for processing  
- 🤖 Generate AI variants with advanced strategies
- 🔄 Generate MetaME variants (if available)
- 📊 View and analyze generated variants
- ⚙️ Configure settings and parameters

### Direct Mode (Automation)
```bash
python3 codegenome.py generate <source_file.c>
# or  
python3 codegenome.py <source_file.c>
```

**Features:**
- Single command execution
- Perfect for scripts and automation
- Generates 1 variant with comprehensive testing
- Outputs results and paths

## File Structure

```
CodeGenome/
├── codegenome.py         # Main entry point  
├── codegenome_core.py    # Core application logic
├── ai_engine.py          # AI transformation engine
├── config.toml           # Configuration file
├── requirements.txt      # Python dependencies
├── source_code/          # Sample C programs
├── workspace/            # Generated variants and tests
│   ├── [variant_id].c    # Generated source
│   ├── [variant_id]      # Compiled binary
│   └── test_suites/      # Automated test suites
└── old/                  # Previous versions
```

## Commands

```bash
python3 codegenome.py [command] [options]

Commands:
  (no args)           Interactive mode (default)
  interactive, i      Launch interactive interface  
  generate <file>     Generate variant for file
  help, h             Show help information
  version, v          Show version info

Examples:
  python3 codegenome.py                           # Interactive
  python3 codegenome.py source_code/simple_test.c # Direct  
  python3 codegenome.py generate myfile.c         # Direct
  python3 codegenome.py --help                    # Help
```

## Output

Each variant generates:
- **Source code** (`[variant_id].c`) - Transformed source
- **Compiled binary** (`[variant_id]`) - Executable variant  
- **Test suite** (`test_suites/[variant_id]/`) - Comprehensive tests
  - `test_cases.json` - All test case definitions
  - `test_runner.py` - Standalone test executor
  - `original_source.c` - Reference source
  - `README.md` - Test documentation

## Transformation Strategies

1. **Control Flow Restructuring** - Loop and conditional transformations
2. **Data Structure Transformation** - Variable types and organization  
3. **Algorithmic Equivalence** - Alternative mathematical approaches
4. **Memory Access Patterns** - Different indexing and pointer usage
5. **Function Organization** - Structure and parameter modifications
6. **System Calls Variation** - Alternative library functions

## Requirements

- **Ollama** with gemma3:12b model running
- **Python 3.8+** with Rich, questionary, pydantic
- **GCC** compiler for code compilation
- **Optional:** strace for dynamic analysis

## Configuration

Edit `config.toml`:
```toml
[ollama]
model_name = "gemma3:12b"
base_url = "http://localhost:11434" 
enabled = true

[testing]
enabled = true
verify_outputs = true
```

## Applications

- **Malware Research** - Evasion-resistant variant generation
- **Compiler Testing** - Optimization analysis and benchmarking  
- **Code Analysis** - Similarity detection algorithm testing
- **AI Evaluation** - Code generation quality assessment