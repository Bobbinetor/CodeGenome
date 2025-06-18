#!/usr/bin/env python3
"""
CodeGenome Simple Configuration
Single configuration file for all settings - easy to understand and modify
"""

# =============================================================================
# LLM CONFIGURATION
# =============================================================================

# Which LLM model to use for code generation
LLM_MODEL = "gemma3:27b"          # Main model (gemma3:12b recommended)
LLM_FALLBACK_MODEL = "gemma3:1b"  # Faster fallback model
LLM_BASE_URL = "http://localhost:11434"  # Ollama server URL

# LLM generation parameters - adjust for creativity vs consistency
LLM_TEMPERATURE = 0.4      # Lower = more consistent, Higher = more creative (0.0-1.0)
LLM_TIMEOUT = 45           # Seconds to wait for LLM response
LLM_MAX_RETRIES = 3        # How many times to retry on failure

# =============================================================================
# AI PROMPTS - MODIFY THESE TO CHANGE HOW CODE IS TRANSFORMED
# =============================================================================

# Main prompt template - this is what tells the AI how to transform code
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

# Simple fallback prompt if main prompt fails
AI_SIMPLE_PROMPT = """Rewrite this C code with different variable names and while loop instead of for loop:

{source_code}

Requirements:
- Change variable names (sum→total, i→counter)
- Change for loop to while loop
- Keep same functionality

Modified C code:"""

# =============================================================================
# TESTING CONFIGURATION
# =============================================================================

# Test generation settings
TESTING_ENABLED = True           # Enable test generation and validation
MAX_TEST_CASES = 20              # Maximum test cases per variant
MIN_TEST_CASES = 4               # Minimum test cases per variant
TEST_TIMEOUT = 10                # Seconds per test execution

# Test types to generate
GENERATE_EDGE_CASES = True       # Generate boundary condition tests
GENERATE_RANDOM_TESTS = True     # Generate random input tests
VERIFY_OUTPUT_CORRECTNESS = True # Verify outputs match exactly

# =============================================================================
# WORKSPACE AND FILES
# =============================================================================

# Directory structure
WORKSPACE_DIR = "workspace"                    # Main workspace directory
SOURCE_CODE_DIR = "source_code"              # Where to find source files
TEST_SUITES_DIR = "workspace/test_suites"    # Generated test suites
METRICS_DIR = "workspace/llm_metrics"        # Performance metrics

# File management
ENABLE_METRICS_LOGGING = True    # Log performance metrics to CSV
LOG_LEVEL = "INFO"               # Logging level: DEBUG, INFO, WARNING, ERROR

# =============================================================================
# BINARY ANALYSIS
# =============================================================================

# Analysis tools (set to False if not installed)
USE_RADARE2 = True              # Use radare2 for binary analysis
USE_STRACE = True               # Use strace for syscall tracing
ENABLE_DYNAMIC_ANALYSIS = False # Enable dynamic analysis (requires strace)

# Analysis settings
STRACE_TIMEOUT = 30             # Seconds for strace execution
GENERATE_RADAR_CHARTS = True    # Create visual comparison charts
ANALYSIS_OUTPUT_DIR = "workspace/analysis_results"

# =============================================================================
# COMPILATION SETTINGS
# =============================================================================

# Compiler configuration
COMPILER = "gcc"                           # Compiler to use
COMPILER_FLAGS = ["-O2", "-std=c99"]      # Default compilation flags
COMPILE_TIMEOUT = 30                      # Seconds for compilation

# =============================================================================
# PERFORMANCE AND LIMITS
# =============================================================================

# Performance monitoring
ENABLE_PERFORMANCE_MONITORING = True   # Track generation times and success rates
MAX_GENERATION_TIME = 300              # Maximum seconds for variant generation
MAX_TOTAL_VARIANTS = 50                 # Maximum total variants to keep

# UI settings
ENABLE_TAB_COMPLETION = True           # Enable file path tab completion
CLEAR_SCREEN_ON_START = False          # Clear screen when starting CLI
USE_COLORS = True                      # Use colored terminal output

# =============================================================================
# METAME INTEGRATION (Optional)
# =============================================================================

METAME_ENABLED = False                    # Enable MetaME transformations
METAME_PATH = "/usr/local/bin/metame"     # Path to MetaME binary
METAME_PASSES = 1                         # Number of transformation passes

# =============================================================================
# HELPER FUNCTIONS - DO NOT MODIFY UNLESS YOU KNOW WHAT YOU'RE DOING
# =============================================================================

def get_ai_prompt(source_code: str, variant_number: int = 1) -> str:
    """Generate AI prompt for given source code and variant number"""
    if variant_number == 1:
        focus = AI_VARIANT_1_FOCUS
    elif variant_number == 2:
        focus = AI_VARIANT_2_FOCUS
    else:
        focus = AI_VARIANT_3_FOCUS
    
    return AI_PROMPT_TEMPLATE.format(focus=focus, source_code=source_code)

def get_simple_prompt(source_code: str) -> str:
    """Get simple fallback prompt"""
    return AI_SIMPLE_PROMPT.format(source_code=source_code)

def get_workspace_path(subdir: str = "") -> str:
    """Get path within workspace"""
    import os
    if subdir:
        return os.path.join(WORKSPACE_DIR, subdir)
    return WORKSPACE_DIR

# Configuration validation
def validate_config():
    """Validate configuration settings"""
    issues = []
    
    if LLM_TEMPERATURE < 0 or LLM_TEMPERATURE > 1:
        issues.append("LLM_TEMPERATURE must be between 0.0 and 1.0")
    
    if MAX_TEST_CASES < MIN_TEST_CASES:
        issues.append("MAX_TEST_CASES must be >= MIN_TEST_CASES")
    
    if TEST_TIMEOUT <= 0:
        issues.append("TEST_TIMEOUT must be positive")
    
    if issues:
        print("⚠️ Configuration Issues:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    
    return True

# Auto-validate when imported
if __name__ != "__main__":
    validate_config()

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("🔧 CodeGenome Configuration")
    print("=" * 50)
    print(f"LLM Model: {LLM_MODEL}")
    print(f"Temperature: {LLM_TEMPERATURE}")
    print(f"Max Test Cases: {MAX_TEST_CASES}")
    print(f"Workspace: {WORKSPACE_DIR}")
    print(f"Performance Monitoring: {ENABLE_PERFORMANCE_MONITORING}")
    print("=" * 50)
    print("✅ Configuration loaded successfully!")
    print()
    print("To modify settings:")
    print("1. Edit this file (config.py)")
    print("2. Change the values above")
    print("3. Save the file")
    print("4. Restart CodeGenome CLI")