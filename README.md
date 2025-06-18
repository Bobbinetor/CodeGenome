# CodeGenome Suite

![CodeGenome Suite](./assets/codegenome-banner.png)

**AI-Powered Code Variant Generation with Advanced Binary Analysis**

CodeGenome is a sophisticated system that generates functionally equivalent C code variants with different binary signatures. Using advanced AI transformation strategies and metamorphic techniques, it creates diverse program variants while maintaining identical functionality, making it invaluable for binary analysis research, reverse engineering studies, and software testing scenarios.

## ✨ Features

### 🤖 AI-Powered Variant Generation
- **6 Advanced Transformation Strategies** targeting maximum binary differentiation
- **LLM-based code transformations** using Ollama with models like gemma3:12b/27b
- **Intelligent prompt engineering** for consistent, high-quality variants
- **Comprehensive test suite generation** with automatic validation
- **Performance monitoring** with detailed metrics and CSV logging

### 📊 Advanced Binary Analysis
- **Multi-tool analysis** using radare2, strace, and static analysis
- **Radar chart visualizations** for multi-binary comparison
- **Syscall pattern analysis** with n-gram detection
- **Distance matrices** (Euclidean and Cosine similarity)
- **Interactive binary selection** with smart categorization

### 🔬 MetaME Integration
- **Metamorphic binary transformations** for compiled executables
- **Semantic-preserving transformations** with configurable passes
- **Binary-level variant generation** complementing AI source transformations

### 🖥️ Modern CLI Interface
- **Tab completion** with intelligent path suggestions
- **Auto-detection** of source files vs. binary files
- **Status indicators** and real-time feedback
- **Natural terminal scrolling** with rich formatting
- **Unified workflow** supporting mixed file types

### ✅ Validation & Testing
- **Automated test case generation** from source analysis
- **Functional equivalence verification** with detailed reporting
- **Standalone test runners** for each generated variant
- **Cross-platform compatibility** handling

## 🏗️ Architecture

```
CodeGenome Suite Architecture:

┌─────────────────────────────────────────────────────────────┐
│                    CLI Interface Layer                      │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ codegenome_cli  │  │ Terminal UI     │                  │
│  │ (Modern CLI)    │  │ (Interactive)   │                  │
│  └─────────────────┘  └─────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Core Application Layer                   │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ codegenome_core │  │ AgenticLLM      │                  │
│  │ (Main Logic)    │  │ (AI Agent)      │                  │
│  └─────────────────┘  └─────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Generation Engines                       │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ ai_engine       │  │ MetaME          │                  │
│  │ (AI Variants)   │  │ (Binary Morphs) │                  │
│  └─────────────────┘  └─────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Analysis & Validation                    │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ advanced_binary │  │ Test Suites     │                  │
│  │ _analyzer       │  │ (Validation)    │                  │
│  └─────────────────┘  └─────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

## 🔑 Key Files

### Core Components
- **`codegenome_cli.py`** - Modern CLI interface with tab completion and unified file handling
- **`ai_engine.py`** - Enhanced AI transformation engine with 6 strategic approaches
- **`advanced_binary_analyzer.py`** - Comprehensive binary analysis with radar charts and metrics
- **`codegenome_core.py`** - Core application logic and terminal interface management
- **`config.py`** - Unified configuration system with well-documented settings

### Configuration & Data
- **`config.toml`** - Single configuration file for all system settings
- **`requirements.txt`** - Python dependencies and package versions
- **`workspace/`** - Generated variants, test suites, and analysis results
- **`source_code/`** - Sample C programs for testing and demonstration

## 🚀 Getting Started

### Prerequisites

#### System Requirements
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install build-essential gcc git python3 python3-pip
```

#### Python Dependencies
```bash
pip install -r requirements.txt
```

#### Ollama Setup (Required for AI generation)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the recommended model
ollama pull gemma3:12b

# Or for faster generation (smaller model)
ollama pull gemma3:1b

# Start Ollama service (if not auto-started)
ollama serve
```

### For Making MetaME Work

MetaME requires a specific version of radare2 for optimal compatibility. Here's how to install the exact version:

#### Prerequisites for radare2
```bash
# Add 32-bit architecture support
sudo dpkg --add-architecture i386
sudo apt update

# Install development tools and multilib support
sudo apt install build-essential git
sudo apt install libc6-dev-i386 gcc-multilib g++-multilib
```

#### Install Specific radare2 Version
```bash
# Clone radare2 repository
rm -rf radare2  # Remove existing if present
git clone https://github.com/radareorg/radare2.git
cd radare2

# Checkout the exact commit needed for MetaME compatibility
git checkout 41dc7e6db6932ebca90a9bc66ee58ee845880fee

# Install radare2
sudo sys/install.sh
```

This specific commit (`41dc7e6db6932ebca90a9bc66ee58ee845880fee`) corresponds to radare2 version 5.9.9 build 33338, which is required for MetaME to function correctly.

### Basic Usage

#### 1. Start the CLI
```bash
python3 codegenome_cli.py
```

#### 2. Load Source Files
```bash
CodeGenome ❯ load source_code/hello_world.c
```

#### 3. Generate AI Variants
```bash
CodeGenome [📄1] ❯ ai
# Follow prompts to generate variants
```

#### 4. Analyze Generated Binaries
```bash
CodeGenome [📄1 🤖2] ❯ analyze
# Select binaries for comparison and analysis
```

#### 5. View Results
```bash
CodeGenome ❯ variants
# Lists all generated variants with details
```

### Configuration

Configuration is managed in the `config.py` file, which is designed to be simple and easy to modify. Below is a breakdown of the key sections and settings you can customize.

#### LLM Configuration
This section controls the behavior of the AI model.

```python
# Which LLM model to use for code generation
LLM_MODEL = "gemma3:27b"          # Main model (gemma3:12b recommended)
LLM_FALLBACK_MODEL = "gemma3:1b"  # Faster fallback model
LLM_BASE_URL = "http://localhost:11434"  # Ollama server URL

# LLM generation parameters - adjust for creativity vs consistency
LLM_TEMPERATURE = 0.4      # Lower = more consistent, Higher = more creative (0.0-1.0)
LLM_TIMEOUT = 45           # Seconds to wait for LLM response
LLM_MAX_RETRIES = 3        # How many times to retry on failure
```

- `LLM_MODEL`: The primary Ollama model for generating code variants.
- `LLM_FALLBACK_MODEL`: A smaller, faster model to use if the primary one fails.
- `LLM_BASE_URL`: The URL of your running Ollama instance.
- `LLM_TEMPERATURE`: Controls the creativity of the AI. Lower values produce more predictable code, while higher values result in more diverse and creative outputs.
- `LLM_TIMEOUT`: The maximum time to wait for a response from the model.
- `LLM_MAX_RETRIES`: The number of times to retry if the model fails to generate a valid response.

#### AI Prompts
This section allows you to customize the instructions given to the AI for transforming code.

```python
# Main prompt template
AI_PROMPT_TEMPLATE = """Transform this C code with {focus} while keeping EXACT same output:

{source_code}

Requirements:
- Identical output and behavior
- Different variable names
- Different loop types  
- Compilable C code

Transformed code:"""

# Different transformation focuses for variants
AI_VARIANT_1_FOCUS = "Change for→while loops, int→long variables, rename all variables"
AI_VARIANT_2_FOCUS = "Use backward iteration, arrays instead of scalars, different math"
AI_VARIANT_3_FOCUS = "Recursive approach, helper functions, reorganize computation"
```

- `AI_PROMPT_TEMPLATE`: The main template used to instruct the AI. You can modify the requirements to guide the transformation process.
- `AI_VARIANT_FOCUS`: These variables define different transformation strategies. The text provided here will be inserted into the `{focus}` placeholder in the main prompt.

#### Testing Configuration
These settings control the automated test generation and validation process.

```python
# Test generation settings
TESTING_ENABLED = True           # Enable test generation and validation
MAX_TEST_CASES = 20              # Maximum test cases per variant
MIN_TEST_CASES = 4               # Minimum test cases per variant
TEST_TIMEOUT = 10                # Seconds per test execution
```

- `TESTING_ENABLED`: A master switch to turn test generation on or off.
- `MAX_TEST_CASES` / `MIN_TEST_CASES`: The range for how many test cases the AI should generate for each variant.
- `TEST_TIMEOUT`: The maximum time allowed for a single test case to run.

#### Workspace and Files
This section defines the directory structure for inputs and outputs.

```python
# Directory structure
WORKSPACE_DIR = "workspace"                    # Main workspace directory
SOURCE_CODE_DIR = "source_code"              # Where to find source files
TEST_SUITES_DIR = "workspace/test_suites"    # Generated test suites
METRICS_DIR = "workspace/llm_metrics"        # Performance metrics
```

#### Binary Analysis
Configure the tools and settings for analyzing the generated binaries.

```python
# Analysis tools (set to False if not installed)
USE_RADARE2 = True              # Use radare2 for binary analysis
USE_STRACE = True               # Use strace for syscall tracing
ENABLE_DYNAMIC_ANALYSIS = False # Enable dynamic analysis (requires strace)

# Analysis settings
STRACE_TIMEOUT = 30             # Seconds for strace execution
GENERATE_RADAR_CHARTS = True    # Create visual comparison charts
```

- `USE_RADARE2` / `USE_STRACE`: Enable or disable specific analysis tools.
- `ENABLE_DYNAMIC_ANALYSIS`: A master switch for dynamic analysis, which relies on `strace`.
- `GENERATE_RADAR_CHARTS`: If enabled, the suite will generate radar charts to visualize the differences between binaries.

## 📖 Workflow Examples

### AI Variant Generation
```bash
# Load a C source file
CodeGenome ❯ load myprogram.c

# Generate multiple variants with different strategies
CodeGenome [📄1] ❯ ai
Number of AI variants to generate: 3

# Results: 3 functionally equivalent variants with different binary signatures
```

### Binary Analysis
```bash
# Load existing binaries or use generated variants
CodeGenome ❯ load workspace/

# Analyze all loaded binaries
CodeGenome [🎯5] ❯ analyze
# Select binaries for comparison
# Results: Radar charts, similarity matrices, detailed reports
```

### MetaME Transformations
```bash
# Load compiled binaries
CodeGenome ❯ load binaries/

# Generate metamorphic variants
CodeGenome [🎯3] ❯ metame
# Results: Binary-level transformed variants
```

## 📁 Output Structure

```
workspace/
├── variants/                     # Generated code variants
│   ├── program_ai_v01.c
│   ├── program_ai_v02.c
│   └── program_ai_v03.c
├── test_suites/                  # Validation test suites
│   ├── program_ai_v01/
│   │   ├── test_cases.json
│   │   ├── test_runner.py
│   │   └── README.md
├── analysis_results/             # Binary analysis reports
│   ├── radar_comparison.png
│   ├── analysis_report.json
│   └── distance_matrix.csv
└── llm_metrics/                  # Performance metrics
    ├── ai_generation_metrics.csv
    └── ai_generation_metrics.json
```

## 🔧 Advanced Configuration

### LLM Prompt Customization
Modify the AI transformation prompts in `ai_engine.py`:

```python
# Example from ai_engine.py
def _get_transformation_prompt(self, source_code: str, strategy: str) -> str:
    # ...
    prompts = {
        "obfuscate": "Obfuscate this C code...",
        # ...
    }
```

### Analysis Tool Configuration
```toml
# From config.toml
[analysis]
enable_dynamic = true
enable_static = true
generate_reports = true
```

## 🎯 Use Cases

### Research Applications
- **Binary Analysis Studies** - Compare how different code patterns affect binary characteristics
- **Reverse Engineering** - Generate diverse samples for analysis technique development
- **Malware Research** - Create polymorphic variants for detection algorithm testing

### Software Testing
- **Compiler Testing** - Validate compiler optimizations across functionally equivalent code
- **Performance Analysis** - Compare execution characteristics of equivalent implementations
- **Cross-platform Validation** - Test software behavior across different binary forms

### Educational Purposes
- **Teaching Binary Analysis** - Demonstrate how code changes affect binary structure
- **Algorithm Comparison** - Show different approaches to solving the same problem
- **Security Education** - Illustrate code obfuscation and variant generation techniques

## 🤝 Contributing

We welcome contributions to improve CodeGenome! Areas where you can help:

- **New Transformation Strategies** - Implement additional AI transformation approaches
- **Analysis Tools Integration** - Add support for more binary analysis tools
- **Performance Optimizations** - Improve generation speed and efficiency
- **Documentation** - Enhance guides, examples, and API documentation
- **Platform Support** - Extend compatibility to additional operating systems
- **UI/UX Improvements** - Enhance the CLI interface and user experience

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 Citation

If you use CodeGenome in your research or projects, please cite:

```bibtex
@software{codegenome_suite,
  title={CodeGenome: AI-Powered Code Variant Generation with Advanced Binary Analysis},
  author={Your Name},
  year={2024},
  url={https://github.com/yourusername/CodeGenome},
  note={AI-powered system for generating functionally equivalent code variants}
}
```

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 🙏 Acknowledgments

- **Ollama Team** for providing the LLM infrastructure
- **radare2 Project** for comprehensive binary analysis capabilities
- **MetaME Developers** for metamorphic transformation engine
- **Rich Library** for beautiful terminal interfaces
- **Open Source Community** for the foundational tools and libraries

---

**CodeGenome Suite** - Pushing the boundaries of automated code variant generation and binary analysis research.
