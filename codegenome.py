#!/usr/bin/env python3
"""
CodeGenome Suite v3.0 - Enhanced Agentic AI Edition
Advanced Binary Analysis & AI-Powered Variant Generation

Professional command-line interface with interactive modes
"""

import sys
import os
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Main entry point with command routing"""
    
    # No arguments = interactive mode
    if len(sys.argv) == 1:
        run_interactive()
        return
    
    command = sys.argv[1].lower()
    
    if command in ['interactive', 'gui', 'run', 'i']:
        run_interactive()
    elif command in ['generate', 'gen', 'g'] and len(sys.argv) > 2:
        run_direct_generation(sys.argv[2])
    elif command in ['help', '-h', '--help', 'h']:
        print_help()
    elif command in ['version', '--version', '-v']:
        print_version()
    elif os.path.exists(command):  # File path provided directly
        run_direct_generation(command)
    else:
        print(f"Unknown command: {command}")
        print_usage()

def run_interactive():
    """Run full interactive terminal interface"""
    try:
        from codegenome_core import CodeGenomeSuite
        suite = CodeGenomeSuite()
        suite.main_menu()
    except ImportError as e:
        print(f"Error importing core modules: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")

def run_direct_generation(source_file):
    """Run direct generation mode for quick usage"""
    if not os.path.exists(source_file):
        print(f"Error: File not found: {source_file}")
        return
    
    try:
        from codegenome_core import CodeGenomeSuite
        from rich.console import Console
        
        console = Console()
        console.print(f"[bold]CodeGenome v3.0 - Direct Generation Mode[/bold]")
        console.print(f"[blue]📄 Source: {source_file}[/blue]")
        
        # Initialize suite
        suite = CodeGenomeSuite()
        
        # Load source file
        suite.loaded_sources = [source_file]
        console.print(f"[green]✅ Loaded source file[/green]")
        
        # Generate AI variants (non-interactive mode)
        console.print(f"[cyan]🤖 Generating AI variants...[/cyan]")
        suite.generate_ai_variants(source_index=0, num_variants=1)
        
        if suite.generated_variants:
            console.print(f"\n[green]🎉 Generated {len(suite.generated_variants)} variant(s)[/green]")
            for i, variant in enumerate(suite.generated_variants, 1):
                console.print(f"  {i}. {variant.name}")
                console.print(f"     Binary: {variant.path}")
        else:
            console.print(f"[red]❌ No variants generated[/red]")
            
    except ImportError as e:
        print(f"Error importing core modules: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error during generation: {e}")

def print_usage():
    """Print basic usage information"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CodeGenome Suite v3.0 - Enhanced Agentic AI Edition                        ║
║  Advanced Binary Analysis & AI-Powered Variant Generation                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

Usage:
  python3 codegenome.py [command] [file]

Commands:
  (no args)           Launch interactive mode (default)
  interactive, i      Launch full interactive interface
  generate <file>     Generate variants for specific file
  help, h             Show detailed help
  version, v          Show version information

Examples:
  python3 codegenome.py                           # Interactive mode
  python3 codegenome.py source_code/simple_test.c # Direct generation
  python3 codegenome.py generate myfile.c         # Direct generation
  python3 codegenome.py interactive               # Interactive mode

Requirements:
  - Ollama with gemma3:12b model running
  - Python dependencies: pip install -r requirements.txt
  - GCC compiler for code compilation
""")

def print_help():
    """Print detailed help information"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CodeGenome Suite v3.0 - Enhanced Agentic AI Edition                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

OVERVIEW:
  Professional terminal application for AI-powered code variant generation.
  Uses advanced AI (gemma3:12b) to create dramatically different code variants
  while maintaining identical functionality.

KEY FEATURES:
  ✓ Interactive terminal interface with rich UI
  ✓ AI-powered code transformations (6 transformation strategies)
  ✓ Comprehensive automated testing and validation
  ✓ Maximum binary differentiation techniques
  ✓ Test suite generation and management
  ✓ Support for C/C++ code analysis
  ✓ Direct generation mode for automation

MODES:
  Interactive Mode    Full-featured terminal interface with menus
  Direct Mode         Command-line generation for automation/scripts

INTERACTIVE FEATURES:
  📁 Load Binaries       Load and analyze compiled binaries
  📄 Load Source Files   Load C/C++ source code for analysis
  🔄 Generate MetaME     Generate variants using MetaME engine
  🤖 Generate AI         Generate variants using AI (gemma3:12b)
  📊 View Variants       Browse and analyze generated variants
  ⚙️ Configuration       Customize settings and parameters

TRANSFORMATION STRATEGIES:
  1. Control Flow Restructuring (for↔while↔do-while loops)
  2. Data Structure Transformation (types, variables, organization)
  3. Algorithmic Equivalence (different math approaches)
  4. Memory Access Patterns (indexing, pointer arithmetic)
  5. Function Organization (structure, parameters, scope)
  6. System Calls Variation (alternative library functions)

SETUP:
  1. Install Ollama: https://ollama.ai
  2. Pull model: ollama pull gemma3:12b
  3. Install Python deps: pip install -r requirements.txt
  4. Run: python3 codegenome.py

OUTPUT STRUCTURE:
  workspace/
  ├── [variant_id].c              # Generated source code
  ├── [variant_id]                # Compiled binary
  ├── test_suites/[variant_id]/   # Comprehensive test suite
  │   ├── test_cases.json         # All test cases
  │   ├── test_runner.py          # Automated test runner
  │   ├── original_source.c       # Original code reference
  │   └── README.md               # Test documentation
  └── config.toml                 # Configuration file

VALIDATION:
  Each variant undergoes rigorous testing:
  - Compilation verification
  - Functional equivalence testing
  - Output consistency validation
  - Performance comparison
  - Only validated variants are confirmed

For more information, see: README.md and CLAUDE.md
""")

def print_version():
    """Print version information"""
    print("""
CodeGenome Suite v3.0 - Enhanced Agentic AI Edition
Advanced Binary Analysis & AI-Powered Variant Generation

Features:
- Enhanced AI engine with gemma3:12b
- 6 transformation strategies
- Comprehensive automated testing
- Interactive terminal interface
- Direct generation mode

Build: Enhanced Agentic Release
""")

if __name__ == "__main__":
    main()