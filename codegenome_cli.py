#!/usr/bin/env python3
"""
CodeGenome Modern CLI - Claude Code Style
Features: Natural scrolling, all original functions, intuitive navigation
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import readline
import glob

# Core libraries
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box
import pyfiglet

# Import simple configuration
import config

# Import existing systems
def check_system_availability():
    """Check if all required components are available"""
    try:
        from codegenome_core import CodeGenomeSuite, SuiteConfig
        from advanced_binary_analyzer import AdvancedBinaryAnalyzer
        return True, (CodeGenomeSuite, SuiteConfig, AdvancedBinaryAnalyzer)
    except ImportError as e:
        print(f"⚠️ Warning: Some components not available: {e}")
        return False, None

# Initial check
FULL_SYSTEM_AVAILABLE, SYSTEM_COMPONENTS = check_system_availability()

class EnhancedPathCompleter:
    """Enhanced path completer with better user experience"""
    
    def __init__(self, console):
        self.matches = []
        self.console = console
        self.last_directory = None
        self.preview_cache = {}
    
    def complete(self, text, state):
        """Complete paths with intelligent preview"""
        if state == 0:
            self.matches = []
            
            # Handle tilde expansion
            if text.startswith('~'):
                text = os.path.expanduser(text)
            
            # Get directory and partial filename
            if '/' in text:
                directory = os.path.dirname(text) or '/'
                partial = os.path.basename(text)
            else:
                directory = '.'
                partial = text
            
            try:
                # Always show current directory first
                if not text or text == '.':
                    self.matches = ['./', '../']
                
                # Get matching entries
                if directory and os.path.exists(directory):
                    try:
                        entries = []
                        for item in os.listdir(directory):
                            if partial and not item.startswith(partial):
                                continue
                            
                            full_path = os.path.join(directory, item)
                            if os.path.isdir(full_path):
                                entries.append(full_path + '/')
                            else:
                                entries.append(full_path)
                        
                        # Sort: directories first, then files
                        directories = [e for e in entries if e.endswith('/')]
                        files = [e for e in entries if not e.endswith('/')]
                        
                        self.matches.extend(sorted(directories))
                        self.matches.extend(sorted(files))
                        
                    except PermissionError:
                        pass
                
                # Remove duplicates while preserving order
                seen = set()
                unique_matches = []
                for match in self.matches:
                    if match not in seen:
                        seen.add(match)
                        unique_matches.append(match)
                self.matches = unique_matches
                
            except Exception:
                pass
        
        try:
            return self.matches[state]
        except IndexError:
            return None
    
    def show_directory_preview(self, directory):
        """Show preview of directory contents"""
        try:
            if not os.path.exists(directory) or not os.path.isdir(directory):
                return
            
            # Cache preview to avoid repeated filesystem calls
            if directory in self.preview_cache:
                preview = self.preview_cache[directory]
            else:
                items = list(os.listdir(directory))
                dirs = [d for d in items if os.path.isdir(os.path.join(directory, d))]
                files = [f for f in items if os.path.isfile(os.path.join(directory, f))]
                
                preview = {
                    'dirs': sorted(dirs)[:5],  # Show first 5 directories
                    'files': sorted(files)[:5],  # Show first 5 files
                    'total_dirs': len(dirs),
                    'total_files': len(files)
                }
                self.preview_cache[directory] = preview
            
            # Show compact preview
            preview_text = []
            if preview['dirs']:
                preview_text.append(f"📁 {len(preview['dirs'])}/{preview['total_dirs']} dirs")
            if preview['files']:
                preview_text.append(f"📄 {len(preview['files'])}/{preview['total_files']} files")
            
            if preview_text:
                self.console.print(f"[dim]  {' | '.join(preview_text)}[/dim]")
                
        except Exception:
            pass

class ModernCodeGenomeCLI:
    """Modern CLI that preserves terminal scrolling and includes all features"""
    
    def __init__(self):
        self.console = Console()
        self.completer = EnhancedPathCompleter(self.console)
        
        # Setup readline for better input handling
        try:
            if config.ENABLE_TAB_COMPLETION:
                readline.set_completer(self.completer.complete)
                readline.parse_and_bind('tab: complete')
                readline.set_completer_delims(' \t\n`!@#$%^&*()=+[{]}\\|;:\'",<>?')
        except:
            pass  # Fallback for systems without readline
        
        # Initialize system
        self.workspace = Path(config.WORKSPACE_DIR)
        self.workspace.mkdir(exist_ok=True)
        
        # Re-check system availability at runtime
        self.system_available, components = check_system_availability()
        
        if self.system_available and components:
            CodeGenomeSuite, SuiteConfig, AdvancedBinaryAnalyzer = components
            try:
                self.suite_config = SuiteConfig(workspace_dir=str(self.workspace))
                self.core_suite = CodeGenomeSuite()
                # Show performance monitoring status
                if hasattr(self.core_suite.agent, 'enhanced_system') and self.core_suite.agent.enhanced_system:
                    if config.ENABLE_PERFORMANCE_MONITORING:
                        self.console.print(f"[dim]✅ Performance monitoring enabled | Max time: {config.MAX_GENERATION_TIME}s[/dim]")
                    else:
                        self.console.print("[dim]⚠️ Performance monitoring disabled in config[/dim]")
                else:
                    self.console.print("[dim]⚠️ Enhanced AI system not available[/dim]")
                self.advanced_analyzer = AdvancedBinaryAnalyzer(self.console, self.workspace)
            except Exception as e:
                self.console.print(f"[red]❌ Error initializing system: {e}[/red]")
                self.system_available = False
                self.suite_config = None
                self.core_suite = None
                self.advanced_analyzer = None
        else:
            self.suite_config = None
            self.core_suite = None
            self.advanced_analyzer = None
        
        # State
        self.loaded_binaries = []
        self.source_files = []
        self.generated_variants = []
        
        # Commands with descriptions
        self.commands = {
            'help': 'Show this help message',
            'menu': 'Show interactive menu (like original)',
            'load': 'Load files (auto-detects sources vs binaries)',
            'metame': 'Generate MetaME variants from binaries',
            'ai': 'Generate AI variants from source code',
            'variants': 'View generated variants',
            'analyze': 'Compare binary differences (MetaME variants or compiled AI sources)',
            'config': 'Show configuration settings',
            'status': 'Show current status',
            'ls': 'List directory contents',
            'cd': 'Change directory',
            'pwd': 'Show current directory',
            'clear': 'Clear screen (optional)',
            'exit': 'Exit CodeGenome',
            'quit': 'Exit CodeGenome'
        }
    
    def start(self):
        """Start the modern CLI"""
        # Clear screen once at start (optional) - only in interactive mode
        import sys
        if sys.stdin.isatty():  # Only ask if running interactively
            if config.CLEAR_SCREEN_ON_START:
                os.system('clear' if os.name == 'posix' else 'cls')
            elif not config.CLEAR_SCREEN_ON_START and Confirm.ask("🧹 Clear screen at startup?", default=False):
                os.system('clear' if os.name == 'posix' else 'cls')
        
        self.show_banner()
        self.show_welcome()
        
        # Main command loop - preserves terminal scrolling
        while True:
            try:
                # Show status in prompt
                status = self.get_status_indicator()
                prompt_text = f"\n[bold blue]CodeGenome[/bold blue] {status} [cyan]❯[/cyan] "
                
                # Get input with auto-completion
                user_input = self.get_input(prompt_text)
                
                if not user_input.strip():
                    continue
                
                # Process command
                if not self.process_command(user_input.strip()):
                    break
                    
            except KeyboardInterrupt:
                self.console.print("\n[yellow]💡 Use 'exit' or Ctrl+D to quit[/yellow]")
                continue
            except EOFError:
                break
        
        self.console.print("\n[blue]👋 Thanks for using CodeGenome Suite![/blue]")
    
    def get_input(self, prompt_text: str) -> str:
        """Get user input with readline support"""
        # Print prompt using rich
        self.console.print(prompt_text, end='')
        
        try:
            # Use input() which works with readline
            return input()
        except (EOFError, KeyboardInterrupt):
            raise
    
    def show_banner(self):
        """Show the beautiful CodeGenome banner"""
        # Get terminal width for responsive design
        terminal_width = shutil.get_terminal_size().columns
        
        if terminal_width >= 120:
            # Full banner for wide terminals
            banner = pyfiglet.figlet_format("CodeGenome", font="slant")
            subtitle = "Advanced Binary Analysis & AI-Powered Variant Generation Suite"
        elif terminal_width >= 80:
            # Medium banner
            banner = pyfiglet.figlet_format("CodeGenome", font="small")
            subtitle = "Binary Analysis & AI Variants"
        else:
            # Compact banner
            banner = "🧬 CodeGenome"
            subtitle = "Binary Analysis Suite"
        
        # Create styled banner
        banner_panel = Panel(
            f"[bold green]{banner}[/bold green]\n[dim cyan]{subtitle}[/dim cyan]",
            box=box.DOUBLE,
            style="blue",
            padding=(1, 2)
        )
        
        self.console.print(banner_panel)
    
    def show_welcome(self):
        """Show welcome message with quick start guide"""
        terminal_width = shutil.get_terminal_size().columns
        
        if terminal_width >= 100:
            # Full welcome for wide terminals
            welcome_table = Table(show_header=False, box=None, padding=(0, 2))
            welcome_table.add_column("Command", style="cyan", width=15)
            welcome_table.add_column("Description", style="dim", width=40)
            welcome_table.add_column("Example", style="yellow")
            
            quick_commands = [
                ("help", "Show all commands", "help"),
                ("menu", "Interactive menu (original style)", "menu"),
                ("load", "Load binary files", "load workspace/"),
                ("analyze", "Analyze binaries", "analyze static"),
                ("status", "Show current status", "status")
            ]
            
            for cmd, desc, example in quick_commands:
                welcome_table.add_row(cmd, desc, example)
            
            self.console.print("\n[bold]🚀 Quick Start Commands[/bold]")
            self.console.print(welcome_table)
        else:
            # Compact welcome
            self.console.print("\n[bold]🚀 Quick Start:[/bold] [cyan]help[/cyan] | [cyan]menu[/cyan] | [cyan]load[/cyan] | [cyan]analyze[/cyan]")
        
        if config.ENABLE_TAB_COMPLETION:
            self.console.print("\n[green]💡 TAB completion enabled[/green]")
        self.console.print(f"[dim]💡 Using model: {config.LLM_MODEL} | Workspace: {config.WORKSPACE_DIR}[/dim]")
    
    def get_status_indicator(self) -> str:
        """Get compact status indicator for prompt"""
        indicators = []
        
        if self.loaded_binaries:
            indicators.append(f"📁{len(self.loaded_binaries)}")
        if self.source_files:
            indicators.append(f"📄{len(self.source_files)}")
        if self.generated_variants:
            indicators.append(f"🤖{len(self.generated_variants)}")
        
        if indicators:
            return f"[{' '.join(indicators)}]"
        else:
            return "[ready]"
    
    def process_command(self, command: str) -> bool:
        """Process user command"""
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd in ['exit', 'quit']:
            return False
        elif cmd == 'help':
            self.show_help()
        elif cmd == 'menu':
            self.show_interactive_menu()
        elif cmd == 'load':
            self.load_files_unified(args)
        elif cmd == 'metame':
            self.generate_metame_variants()
        elif cmd == 'ai':
            self.generate_ai_variants()
        elif cmd == 'variants':
            self.show_variants()
        elif cmd == 'analyze':
            self.analyze_binaries_modern(args)
        elif cmd == 'config':
            self.configure_settings(args)
        elif cmd == 'status':
            self.show_detailed_status()
        elif cmd == 'ls':
            self.list_directory(args)
        elif cmd == 'cd':
            self.change_directory(args)
        elif cmd == 'pwd':
            self.console.print(f"[cyan]{Path.cwd()}[/cyan]")
        elif cmd == 'clear':
            if Confirm.ask("🧹 Clear screen?", default=False):
                os.system('clear' if os.name == 'posix' else 'cls')
                self.show_banner()
        else:
            self.console.print(f"[red]❌ Unknown command: {cmd}[/red]")
            self.console.print("[dim]Type 'help' for available commands[/dim]")
        
        return True
    
    def show_help(self):
        """Show comprehensive help"""
        self.console.print("\n[bold]📚 CodeGenome Commands[/bold]")
        
        # Group commands by category
        categories = {
            "🗂️ File Management": ['load', 'ls', 'cd', 'pwd'],
            "🤖 Variant Generation": ['ai', 'metame', 'variants'],
            "📊 Analysis": ['analyze', 'status'],
            "⚙️ System": ['menu', 'config', 'clear', 'help', 'exit', 'quit']
        }
        
        workflow_info = """
[bold yellow]📋 Unified Workflow:[/bold yellow]
[cyan]1. Load Files (auto-detection):[/cyan]
  load directory/                 # Auto-detects sources & binaries
  load file1.c binary1 file2.c    # Mix sources and binaries

[cyan]2. Generate Variants:[/cyan]
  ai                              # Generate AI variants from sources
  metame                          # Generate MetaME variants from binaries

[cyan]3. Analysis (compare binaries):[/cyan]
  analyze                         # Compare binary differences (MetaME variants OR compiled AI sources)
  variants                        # View all generated variants"""
        
        for category, cmds in categories.items():
            self.console.print(f"\n[bold cyan]{category}[/bold cyan]")
            
            help_table = Table(show_header=False, box=None, padding=(0, 1))
            help_table.add_column("Command", style="green", width=12)
            help_table.add_column("Description", style="dim")
            
            for cmd in cmds:
                if cmd in self.commands:
                    help_table.add_row(cmd, self.commands[cmd])
            
            self.console.print(help_table)
        
        self.console.print(f"\n[green]💡 Current Configuration:[/green]")
        self.console.print(f"  🤖 Model: {config.LLM_MODEL} (temp: {config.LLM_TEMPERATURE})")
        self.console.print(f"  🧪 Max test cases: {config.MAX_TEST_CASES}")
        self.console.print(f"  📊 Analysis tools: {'radare2' if config.USE_RADARE2 else 'basic'}")
        self.console.print(f"  📁 Workspace: {config.WORKSPACE_DIR}")
        
        # Show workflow guide
        self.console.print(workflow_info)
    
    def show_interactive_menu(self):
        """Show original-style interactive menu"""
        if not self.system_available:
            self.console.print("[red]❌ Full system not available[/red]")
            return
        
        self.console.print("\n[bold]📋 Interactive Menu (Original Style)[/bold]")
        self.console.print("[dim]This preserves the exact original menu functionality[/dim]")
        
        # Use the original menu system
        try:
            self.core_suite.main_menu()
        except Exception as e:
            self.console.print(f"[red]❌ Menu error: {e}[/red]")
    
    def load_files_unified(self, args: List[str]):
        """Unified file loading that auto-detects sources vs binaries"""
        if not args:
            # Interactive mode
            paths = self.get_paths_interactive("Files (sources & binaries)")
        else:
            # Command line arguments
            paths = []
            for arg in args:
                arg = os.path.expanduser(arg.strip())
                if os.path.isdir(arg):
                    # Directory: get all files and categorize
                    categorized = self.get_all_files_from_directory(arg)
                    paths.extend(categorized['sources'])
                    paths.extend(categorized['binaries'])
                    if categorized['sources']:
                        self.console.print(f"[blue]📁 Found {len(categorized['sources'])} source files in {arg}[/blue]")
                    if categorized['binaries']:
                        self.console.print(f"[blue]📁 Found {len(categorized['binaries'])} binaries in {arg}[/blue]")
                    if categorized['other']:
                        self.console.print(f"[dim]📄 Skipped {len(categorized['other'])} other files in {arg}[/dim]")
                elif os.path.isfile(arg):
                    paths.append(arg)
                else:
                    self.console.print(f"[red]❌ Path not found: {arg}[/red]")
        
        if not paths:
            return
        
        # Categorize loaded files
        sources_loaded = 0
        binaries_loaded = 0
        
        for path in paths:
            file_type = self.detect_file_type(path)
            
            if file_type == "source":
                if path not in self.source_files:
                    if self.validate_source_file(path):
                        self.source_files.append(path)
                        sources_loaded += 1
                        self.console.print(f"[green]✅ Loaded source: {os.path.basename(path)}[/green]")
                    else:
                        self.console.print(f"[yellow]⚠️ Skipped invalid source: {path}[/yellow]")
                else:
                    self.console.print(f"[dim]📝 Already loaded: {os.path.basename(path)}[/dim]")
                    
            elif file_type == "binary":
                if path not in self.loaded_binaries:
                    self.loaded_binaries.append(path)
                    binaries_loaded += 1
                    self.console.print(f"[green]✅ Loaded binary: {os.path.basename(path)}[/green]")
                else:
                    self.console.print(f"[dim]🎯 Already loaded: {os.path.basename(path)}[/dim]")
            else:
                self.console.print(f"[yellow]⚠️ Unsupported file type: {path}[/yellow]")
        
        # Sync loaded files with core suite for AI/MetaME generation
        if self.core_suite:
            if not hasattr(self.core_suite, 'loaded_sources'):
                self.core_suite.loaded_sources = []
            if not hasattr(self.core_suite, 'loaded_binaries'):
                self.core_suite.loaded_binaries = []
            
            # Sync the loaded files with core suite
            self.core_suite.loaded_sources = self.source_files.copy()
            self.core_suite.loaded_binaries = self.loaded_binaries.copy()
        
        # Summary
        if sources_loaded > 0 or binaries_loaded > 0:
            summary_parts = []
            if sources_loaded > 0:
                summary_parts.append(f"{sources_loaded} source file(s)")
            if binaries_loaded > 0:
                summary_parts.append(f"{binaries_loaded} binary file(s)")
            
            self.console.print(f"\n[green]🎉 Successfully loaded {' and '.join(summary_parts)}[/green]")
            
            # Show next steps
            if sources_loaded > 0:
                self.console.print("[blue]💡 Use 'ai' command to generate variants from source files[/blue]")
            if binaries_loaded > 0:
                self.console.print("[blue]💡 Use 'metame' to generate variants from binaries[/blue]")
                self.console.print("[blue]💡 Use 'analyze' to compare binary differences[/blue]")
        else:
            self.console.print("[yellow]⚠️ No new files were loaded[/yellow]")
    
    def load_binaries_interactive(self, args: List[str]):
        """Load compiled binaries into the suite"""
        if not self.system_available:
            self.console.print("[red]❌ Core suite not available[/red]")
            return
        
        if args:
            # Handle command line arguments
            final_paths = []
            for p in args:
                p = os.path.expanduser(p.strip())
                if os.path.isdir(p):
                    dir_files = self.get_files_from_directory(p, ['.bin', '.exe', '.out', ''])
                    # Also include files without extensions that are executable
                    executable_files = []
                    for f in os.listdir(p):
                        full_path = os.path.join(p, f)
                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                            if not os.path.splitext(f)[1]:  # No extension
                                executable_files.append(full_path)
                    dir_files.extend(executable_files)
                    final_paths.extend(dir_files)
                elif os.path.isfile(p):
                    final_paths.append(p)
                else:
                    self.console.print(f"[red]❌ Path not found: {p}[/red]")
        else:
            # Interactive mode
            final_paths = self.get_paths_interactive("Binary Files", ['.bin', '.exe', '.out'])
        
        if not final_paths:
            return
        
        loaded_count = 0
        for p in final_paths:
            if p not in self.loaded_binaries:  # Avoid duplicates
                self.loaded_binaries.append(p)
                loaded_count += 1
                self.console.print(f"[green]✅ Loaded binary: {p}[/green]")
        
        # Update core suite
        if hasattr(self.core_suite, 'loaded_binaries'):
            self.core_suite.loaded_binaries = self.loaded_binaries
        
        if loaded_count > 0:
            self.console.print(f"\n[green]🎉 Successfully loaded {loaded_count} binary file(s)[/green]")

    def get_paths_interactive(self, file_type: str, extensions: List[str] = None) -> List[str]:
        """Enhanced path input with directory support and better UX"""
        self.console.print(f"\n[cyan]📄 Load {file_type}:[/cyan]")
        self.console.print("[dim]  • Use TAB for auto-completion and directory preview[/dim]")
        self.console.print("[dim]  • Separate multiple paths with spaces or commas[/dim]")
        self.console.print("[dim]  • Specify a directory to load all matching files[/dim]")
        self.console.print(f"[dim]  • Current directory: {Path.cwd()}[/dim]")
        
        # Show current directory preview
        self.completer.show_directory_preview('.')
        
        while True:
            try:
                # Use input() with readline support instead of Prompt.ask
                self.console.print(f"Enter {file_type.lower()} paths: ", end='')
                path_input = input().strip()
                
                if not path_input:
                    self.console.print("[yellow]⚠️ No paths provided. Try again or press Ctrl+C to cancel[/yellow]")
                    continue
                
                break
            except KeyboardInterrupt:
                self.console.print("\n[yellow]❌ Cancelled[/yellow]")
                return []
            except EOFError:
                self.console.print("\n[yellow]❌ Cancelled[/yellow]")
                return []
        
        # Parse input paths
        if ',' in path_input:
            raw_paths = [p.strip() for p in path_input.split(',') if p.strip()]
        else:
            raw_paths = path_input.split()
        
        final_paths = []
        for p in raw_paths:
            p = os.path.expanduser(p.strip())
            
            if os.path.isdir(p):
                # Load all matching files from directory
                dir_files = self.get_files_from_directory(p, extensions)
                final_paths.extend(dir_files)
                self.console.print(f"[blue]📁 Found {len(dir_files)} files in directory: {p}[/blue]")
            elif os.path.isfile(p):
                final_paths.append(p)
            else:
                self.console.print(f"[red]❌ Path not found: {p}[/red]")
        
        return final_paths
    
    def get_files_from_directory(self, directory: str, extensions: List[str] = None) -> List[str]:
        """Get all files matching extensions from a directory"""
        files = []
        try:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    if not extensions:
                        files.append(item_path)
                    else:
                        # Check if file has matching extension
                        _, ext = os.path.splitext(item.lower())
                        if ext in extensions:
                            files.append(item_path)
        except PermissionError:
            self.console.print(f"[red]❌ Permission denied accessing: {directory}[/red]")
        
        return sorted(files)

    def validate_source_file(self, file_path: str) -> bool:
        """Validate that a source file is not empty and has basic structure"""
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
                
            if not content:
                self.console.print(f"[yellow]⚠️ Skipping empty file: {file_path}[/yellow]")
                return False
            
            # Basic validation for C/C++ files
            if file_path.endswith(('.c', '.cpp', '.cc', '.cxx')):
                # Check for some basic C/C++ indicators
                has_function = 'main(' in content or '{' in content or 'int ' in content or 'void ' in content
                if not has_function:
                    self.console.print(f"[yellow]⚠️ File may not be valid C/C++ code: {file_path}[/yellow]")
                    self.console.print(f"[dim]  Content preview: {content[:100]}...[/dim]")
                    return False
            
            return True
            
        except Exception as e:
            self.console.print(f"[red]❌ Error reading file {file_path}: {e}[/red]")
            return False

    def load_source_interactive(self, args: List[str]):
        """Load source files into the suite"""
        if not self.system_available:
            self.console.print("[red]❌ Core suite not available[/red]")
            return
        
        if args:
            # Handle command line arguments
            final_paths = []
            for p in args:
                p = os.path.expanduser(p.strip())
                if os.path.isdir(p):
                    dir_files = self.get_files_from_directory(p, ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp'])
                    final_paths.extend(dir_files)
                elif os.path.isfile(p):
                    final_paths.append(p)
                else:
                    self.console.print(f"[red]❌ Path not found: {p}[/red]")
        else:
            # Interactive mode
            final_paths = self.get_paths_interactive("Source Files", ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp'])
        
        if not final_paths:
            return
        
        loaded_count = 0
        for p in final_paths:
            if p not in self.source_files:  # Avoid duplicates
                # Validate source file before loading
                if self.validate_source_file(p):
                    self.source_files.append(p)
                    loaded_count += 1
                    self.console.print(f"[green]✅ Loaded source: {p}[/green]")
        
        # Update core suite with loaded files
        if self.core_suite:
            if not hasattr(self.core_suite, 'loaded_sources'):
                self.core_suite.loaded_sources = []
            if not hasattr(self.core_suite, 'loaded_binaries'):
                self.core_suite.loaded_binaries = []
            
            # Sync the loaded files with core suite
            self.core_suite.loaded_sources = self.source_files.copy()
            self.core_suite.loaded_binaries = self.loaded_binaries.copy()
        
        if loaded_count > 0:
            self.console.print(f"\n[green]🎉 Successfully loaded {loaded_count} valid source file(s)[/green]")
        elif final_paths:
            self.console.print(f"\n[yellow]⚠️ No valid source files found to load[/yellow]")

    def generate_metame_variants(self):
        """Generate MetaME variants via core suite"""
        if not self.system_available:
            self.console.print("[red]❌ Core suite not available[/red]")
            self.console.print("[dim]Please ensure all dependencies are installed and try restarting the CLI[/dim]")
            return
        
        if not self.loaded_binaries:
            self.console.print("[yellow]⚠️ No binary files loaded. Use 'load' command first[/yellow]")
            self.console.print("[dim]💡 MetaME works on compiled binaries, not source files[/dim]")
            return
        
        enabled_status = "✅ Enabled" if config.METAME_ENABLED else "❌ Disabled"
        self.console.print(f"\n[cyan]🔄 MetaME Variant Generation ({enabled_status})[/cyan]")
        self.console.print(f"[dim]Binary files: {', '.join(self.loaded_binaries)}[/dim]")
        if not config.METAME_ENABLED:
            self.console.print("[yellow]⚠️ MetaME is disabled in config.py[/yellow]")
        
        count = Prompt.ask("Number of MetaME variants to generate", default="1")
        try:
            num = int(count)
            if num <= 0:
                self.console.print("[red]❌ Number must be positive[/red]")
                return
            
            # Show simple progress message instead of spinner to avoid conflicts
            self.console.print(f"\n[cyan]⚙️ Starting MetaME variant generation ({num} variant(s))...[/cyan]")
            
            # Store count before generation to check if new variants were added
            initial_count = len(self.generated_variants) if self.generated_variants else 0
            
            # MetaME generation needs binary selection - let's handle it properly
            selected_binary = None
            
            if len(self.loaded_binaries) == 1:
                # Single binary - use it directly
                selected_binary = self.loaded_binaries[0]
                self.console.print(f"[cyan]📄 Using binary: {selected_binary}[/cyan]")
            else:
                # Multiple binaries - ask user to select
                self.console.print("\n[cyan]📁 Available binaries:[/cyan]")
                for i, binary in enumerate(self.loaded_binaries, 1):
                    self.console.print(f"  {i}. {binary}")
                
                choice = Prompt.ask("Select binary (number)", default="1")
                try:
                    binary_index = int(choice) - 1
                    if 0 <= binary_index < len(self.loaded_binaries):
                        selected_binary = self.loaded_binaries[binary_index]
                        self.console.print(f"[cyan]📄 Selected binary: {selected_binary}[/cyan]")
                    else:
                        self.console.print("[red]❌ Invalid selection[/red]")
                        return
                except ValueError:
                    self.console.print("[red]❌ Invalid number[/red]")
                    return
            
            # Check if we have a valid binary selected
            if not selected_binary:
                self.console.print("[red]❌ No binary selected[/red]")
                return
            
            # Generate MetaME variants using the correct method
            variants = self.core_suite.metame.generate_variants(selected_binary, num)
            
            # Process the results - MetaME returns a list of VariantInfo objects
            if variants:
                # Add to core suite's generated variants list
                if not hasattr(self.core_suite, 'generated_variants'):
                    self.core_suite.generated_variants = []
                self.core_suite.generated_variants.extend(variants)
                
                # Update our local list
                self.generated_variants = self.core_suite.generated_variants
                
                self.console.print(f"\n[green]🎉 Generated {len(variants)} MetaME variant(s) successfully![/green]")
                
                # Show generated variants
                for i, variant in enumerate(variants, 1):
                    self.console.print(f"  {i}. {variant.name} - {variant.path}")
                    
                self.console.print(f"\n[blue]📁 MetaME variants saved in workspace/[/blue]")
            else:
                self.console.print(f"[red]❌ Failed to generate MetaME variants[/red]")
                self.console.print("[dim]Make sure MetaME is installed: pip install metame[/dim]")
                    
        except ValueError:
            self.console.print("[red]❌ Invalid number format[/red]")
        except Exception as e:
            self.console.print(f"[red]❌ Generation error: {e}[/red]")

    def test_compilation(self, source_file: str) -> bool:
        """Test if a source file can be compiled successfully"""
        try:
            import tempfile
            import subprocess
            
            with tempfile.NamedTemporaryFile(suffix='.out', delete=True) as temp_binary:
                result = subprocess.run(
                    ['gcc', '-o', temp_binary.name, source_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    return True
                else:
                    self.console.print(f"[yellow]⚠️ Compilation test failed for {source_file}:[/yellow]")
                    self.console.print(f"[dim]{result.stderr}[/dim]")
                    return False
                    
        except Exception as e:
            self.console.print(f"[yellow]⚠️ Could not test compilation: {e}[/yellow]")
            return True  # Allow generation to proceed if test fails

    def generate_ai_variants(self):
        """Generate AI variants via core suite"""
        if not self.system_available:
            self.console.print("[red]❌ Core suite not available[/red]")
            self.console.print("[dim]Please ensure all dependencies are installed and try restarting the CLI[/dim]")
            return
        
        if not self.source_files:
            self.console.print("[yellow]⚠️ No source files loaded. Use 'load' command first[/yellow]")
            return
        
        self.console.print(f"\n[cyan]🤖 AI Variant Generation (Model: {config.LLM_MODEL})[/cyan]")
        self.console.print(f"[dim]Source files: {', '.join(self.source_files)}[/dim]")
        self.console.print(f"[dim]Temperature: {config.LLM_TEMPERATURE} | Timeout: {config.LLM_TIMEOUT}s[/dim]")
        
        # Test compilation of source files
        self.console.print(f"\n[blue]🔍 Testing compilation ({config.COMPILER} {' '.join(config.COMPILER_FLAGS)})...[/blue]")
        valid_sources = []
        for source_file in self.source_files:
            if self.test_compilation(source_file):
                valid_sources.append(source_file)
                self.console.print(f"[green]✅ {source_file} compiles successfully[/green]")
            else:
                self.console.print(f"[red]❌ {source_file} failed compilation test[/red]")
        
        if not valid_sources:
            self.console.print("[red]❌ No valid source files can be compiled[/red]")
            return
        
        count = Prompt.ask(f"Number of AI variants to generate (max: {config.MAX_TOTAL_VARIANTS})", default="1")
        try:
            num = int(count)
            if num <= 0:
                self.console.print("[red]❌ Number must be positive[/red]")
                return
            
            # Show simple progress message instead of spinner to avoid conflicts
            self.console.print(f"\n[cyan]⚙️ Starting AI variant generation ({num} variant(s))...[/cyan]")
            
            # Store count before generation to check if new variants were added
            initial_count = len(self.generated_variants) if self.generated_variants else 0
            
            # Sync source files with core suite before generation
            if not hasattr(self.core_suite, 'loaded_sources'):
                self.core_suite.loaded_sources = []
            self.core_suite.loaded_sources = valid_sources.copy()
            
            # Use the core suite's generation method (doesn't return success value)
            self.core_suite.generate_ai_variants(source_index=0, num_variants=num)
            
            # Update our list and check if new variants were generated
            if hasattr(self.core_suite, 'generated_variants') and self.core_suite.generated_variants:
                self.generated_variants = self.core_suite.generated_variants
                new_count = len(self.generated_variants)
                
                if new_count > initial_count:
                    variants_generated = new_count - initial_count
                    self.console.print(f"\n[green]🎉 Generated {variants_generated} AI variant(s) successfully![/green]")
                    
                    # Show generated variants (only the new ones)
                    for i, variant in enumerate(self.generated_variants[-variants_generated:], 1):
                        self.console.print(f"  {i}. {variant.name} - {variant.path}")
                        
                    # Show test suite info
                    self.console.print(f"\n[blue]📋 Test suites generated in workspace/test_suites/[/blue]")
                else:
                    self.console.print(f"[yellow]⚠️ No new variants were generated[/yellow]")
            else:
                self.console.print(f"[red]❌ Failed to generate AI variants[/red]")
                self.console.print("[dim]Make sure Ollama is running with gemma3:12b model[/dim]")
                    
        except ValueError:
            self.console.print("[red]❌ Invalid number format[/red]")
        except Exception as e:
            self.console.print(f"[red]❌ Generation error: {e}[/red]")

    def show_variants(self):
        """Display generated variants"""
        if not self.generated_variants:
            self.console.print("[yellow]⚠️ No variants generated yet[/yellow]")
            return
        table = Table(title="Generated Variants", box=box.ROUNDED)
        table.add_column("#", style="cyan", width=4)
        table.add_column("Name", style="green")
        table.add_column("Type", style="magenta")
        table.add_column("Binary Path", style="yellow")
        for i, v in enumerate(self.generated_variants, 1):
            table.add_row(str(i), v.name, v.variant_type.value, v.path)
        self.console.print(table)

    def analyze_binaries_modern(self, args: List[str]):
        """Full-featured binary analysis with user control (equivalent to codegenome.py)"""
        if not self.advanced_analyzer:
            self.console.print("[red]❌ Advanced analyzer not available[/red]")
            return
        
        # Step 1: Show available binaries and let user select
        available_binaries = []
        
        # Add loaded binaries
        if self.loaded_binaries:
            available_binaries.extend(self.loaded_binaries)
        
        # Add command line args if provided
        if args:
            for arg in args:
                arg = os.path.expanduser(arg.strip())
                if os.path.isfile(arg) and self.detect_file_type(arg) == "binary":
                    if arg not in available_binaries:
                        available_binaries.append(arg)
                elif os.path.isdir(arg):
                    # Get binaries from directory
                    categorized = self.get_all_files_from_directory(arg)
                    for binary in categorized['binaries']:
                        if binary not in available_binaries:
                            available_binaries.append(binary)
        
        if not available_binaries:
            self.console.print("[yellow]⚠️ No binaries available. Use 'load' to load binaries first[/yellow]")
            return
        
        tools_status = []
        if config.USE_RADARE2:
            tools_status.append("radare2")
        if config.USE_STRACE and config.ENABLE_DYNAMIC_ANALYSIS:
            tools_status.append("strace")
        tools_str = " + ".join(tools_status) if tools_status else "basic"
        
        self.console.print(f"\n[bold cyan]🔍 Binary Analysis ({tools_str})[/bold cyan]")
        self.console.print(f"[blue]Found {len(available_binaries)} available binaries:[/blue]")
        
        # Show available binaries
        table = Table(title="Available Binaries", box=box.ROUNDED)
        table.add_column("#", style="cyan", width=4)
        table.add_column("Binary Name", style="green")
        table.add_column("Path", style="yellow")
        table.add_column("Size", style="magenta")
        
        for i, binary_path in enumerate(available_binaries, 1):
            size = "Unknown"
            if os.path.exists(binary_path):
                try:
                    size = self.format_size(os.path.getsize(binary_path))
                except:
                    pass
            table.add_row(str(i), os.path.basename(binary_path), binary_path, size)
        
        self.console.print(table)
        
        # Step 2: Let user select binaries to analyze
        self.console.print("\n[cyan]Select binaries to analyze:[/cyan]")
        self.console.print("[dim]• Enter numbers (e.g., '1,3,5' or '1-3' or 'all')[/dim]")
        self.console.print("[dim]• Press Enter to analyze all binaries[/dim]")
        
        selection = Prompt.ask("Selection", default="all").strip().lower()
        
        selected_binaries = []
        
        if selection == "all" or selection == "":
            selected_binaries = available_binaries.copy()
        else:
            try:
                # Parse selection
                indices = []
                for part in selection.split(','):
                    part = part.strip()
                    if '-' in part:
                        # Range like "1-3"
                        start, end = map(int, part.split('-'))
                        indices.extend(range(start, end + 1))
                    else:
                        # Single number
                        indices.append(int(part))
                
                # Convert to binary paths
                for idx in indices:
                    if 1 <= idx <= len(available_binaries):
                        selected_binaries.append(available_binaries[idx - 1])
                    else:
                        self.console.print(f"[yellow]⚠️ Invalid selection: {idx}[/yellow]")
                        
            except ValueError:
                self.console.print("[red]❌ Invalid selection format[/red]")
                return
        
        if not selected_binaries:
            self.console.print("[yellow]⚠️ No binaries selected[/yellow]")
            return
        
        # Step 3: Analysis options
        self.console.print(f"\n[green]Selected {len(selected_binaries)} binaries for analysis[/green]")
        
        default_strace = config.ENABLE_DYNAMIC_ANALYSIS and config.USE_STRACE
        use_strace = Confirm.ask(f"🔬 Enable dynamic analysis (strace) [config: {default_strace}]", default=default_strace)
        
        # Step 4: Perform analysis
        if len(selected_binaries) == 1:
            # Single binary analysis
            binary_path = selected_binaries[0]
            self.console.print(f"[cyan]🔍 Analyzing: {os.path.basename(binary_path)}[/cyan]")
            metrics = self.advanced_analyzer.analyze_with_radare2(binary_path, use_strace=use_strace)
            self.advanced_analyzer.print_detailed_metrics(metrics)
        else:
            # Multiple binary analysis with comparison
            self.console.print(f"[cyan]🔍 Analyzing {len(selected_binaries)} binaries with comparison[/cyan]")
            metrics_list, chart_path = self.advanced_analyzer.analyze_multiple_binaries_advanced(selected_binaries, use_strace=use_strace)
            
            if chart_path:
                self.console.print(f"[green]📊 Analysis complete![/green]")
                self.console.print(f"[blue]📈 Radar chart: {chart_path}[/blue]")
                self.console.print(f"[blue]📄 Analysis report: {chart_path.replace('.png', '.json')}[/blue]")
            else:
                self.console.print("[yellow]⚠️ Analysis complete but visualization failed[/yellow]")
        
        # Analysis results info with actual config
        self.console.print(f"\n[blue]📁 Results saved to: {config.ANALYSIS_OUTPUT_DIR}[/blue]")
        if config.GENERATE_RADAR_CHARTS:
            self.console.print("[blue]📊 Radar charts enabled in configuration[/blue]")

    def configure_settings(self, args: List[str]):
        """Show configuration information"""
        self.console.print("\n[bold cyan]🔧 Configuration[/bold cyan]")
        
        self.console.print(f"\n[green]🤖 LLM Settings:[/green]")
        self.console.print(f"  Model: {config.LLM_MODEL}")
        self.console.print(f"  Fallback: {config.LLM_FALLBACK_MODEL}")
        self.console.print(f"  Temperature: {config.LLM_TEMPERATURE}")
        self.console.print(f"  Timeout: {config.LLM_TIMEOUT}s")
        
        self.console.print(f"\n[green]🧪 Testing Settings:[/green]")
        self.console.print(f"  Enabled: {config.TESTING_ENABLED}")
        self.console.print(f"  Max Test Cases: {config.MAX_TEST_CASES}")
        self.console.print(f"  Test Timeout: {config.TEST_TIMEOUT}s")
        
        self.console.print(f"\n[green]📁 Workspace Settings:[/green]")
        self.console.print(f"  Workspace: {config.WORKSPACE_DIR}")
        self.console.print(f"  Metrics Logging: {config.ENABLE_METRICS_LOGGING}")
        self.console.print(f"  Performance Monitoring: {config.ENABLE_PERFORMANCE_MONITORING}")
        
        self.console.print(f"\n[green]📊 Analysis Settings:[/green]")
        self.console.print(f"  Use Radare2: {config.USE_RADARE2}")
        self.console.print(f"  Dynamic Analysis: {config.ENABLE_DYNAMIC_ANALYSIS}")
        self.console.print(f"  Generate Charts: {config.GENERATE_RADAR_CHARTS}")
        
        self.console.print(f"\n[blue]💡 To modify settings:[/blue]")
        self.console.print(f"  1. Edit [cyan]config.py[/cyan] file")
        self.console.print(f"  2. Change the values at the top")
        self.console.print(f"  3. Save and restart CLI")

    def show_detailed_status(self):
        """Show detailed suite and analyzer status"""
        self.console.print(f"\n[bold cyan]📊 CodeGenome Status[/bold cyan]")
        
        # System availability with config
        if self.system_available:
            self.console.print(f"[green]✅ Core system: Available (Model: {config.LLM_MODEL})[/green]")
        else:
            self.console.print("[red]❌ Core system: Not available[/red]")
            self.console.print("[dim]Some features may not work. Try restarting the CLI.[/dim]")
        
        # Show key configuration
        self.console.print(f"[green]⚙️ Configuration:[/green]")
        self.console.print(f"  Model: {config.LLM_MODEL} | Temperature: {config.LLM_TEMPERATURE}")
        self.console.print(f"  Max test cases: {config.MAX_TEST_CASES} | Timeout: {config.TEST_TIMEOUT}s")
        self.console.print(f"  Performance monitoring: {'✅' if config.ENABLE_PERFORMANCE_MONITORING else '❌'}")
        
        # Files loaded
        if self.source_files:
            self.console.print(f"[green]📝 Source files: {len(self.source_files)}[/green]")
            for i, src in enumerate(self.source_files[:3], 1):
                self.console.print(f"  {i}. {os.path.basename(src)}")
            if len(self.source_files) > 3:
                self.console.print(f"  ... and {len(self.source_files) - 3} more")
        else:
            self.console.print("[dim]📝 No source files loaded[/dim]")
        
        if self.loaded_binaries:
            self.console.print(f"[green]🎯 Binaries: {len(self.loaded_binaries)}[/green]")
            for i, bin_path in enumerate(self.loaded_binaries[:3], 1):
                self.console.print(f"  {i}. {os.path.basename(bin_path)}")
            if len(self.loaded_binaries) > 3:
                self.console.print(f"  ... and {len(self.loaded_binaries) - 3} more")
        else:
            self.console.print("[dim]🎯 No binaries loaded[/dim]")
        
        if self.generated_variants:
            self.console.print(f"[green]🤖 Generated variants: {len(self.generated_variants)}[/green]")
        else:
            self.console.print("[dim]🤖 No variants generated[/dim]")
        
        # Quick actions based on loaded files
        if not self.source_files and not self.loaded_binaries:
            self.console.print(f"\n[blue]💡 Start with: 'load <files>' to load source files or binaries[/blue]")
        elif self.source_files and not self.generated_variants:
            self.console.print(f"\n[blue]💡 Ready for: 'ai' to generate variants[/blue]")
        elif self.generated_variants:
            self.console.print(f"\n[blue]💡 Ready for: 'analyze' to compare binaries[/blue]")
    
    def list_directory(self, args: List[str]):
        """List directory contents"""
        path = Path(args[0]) if args else Path.cwd()
        
        if not path.exists() or not path.is_dir():
            self.console.print(f"[red]❌ Directory not found: {path}[/red]")
            return
        
        self.console.print(f"\n[bold]📂 {path}[/bold]")
        
        try:
            items = list(path.iterdir())
            dirs = [item for item in items if item.is_dir()]
            files = [item for item in items if item.is_file()]
            
            # Show directories
            if dirs:
                self.console.print("\n[cyan]📁 Directories:[/cyan]")
                for d in sorted(dirs):
                    item_count = len(list(d.iterdir())) if d.is_dir() else 0
                    self.console.print(f"  📁 {d.name}/ ({item_count} items)")
            
            # Show files
            if files:
                self.console.print("\n[cyan]📄 Files:[/cyan]")
                for f in sorted(files):
                    size = self.format_size(f.stat().st_size)
                    file_type = "🎯 Binary" if self.is_binary_file(f) else "📄 File"
                    if self.is_source_file(f):
                        file_type = "📝 Source"
                    self.console.print(f"  {file_type} {f.name} ({size})")
            
            if not items:
                self.console.print("[dim]📁 Empty directory[/dim]")
                
        except PermissionError:
            self.console.print("[red]❌ Permission denied[/red]")
    
    def change_directory(self, args: List[str]):
        """Change directory"""
        if not args:
            path = Path.home()
        else:
            path = Path(args[0])
        
        try:
            if path.exists() and path.is_dir():
                os.chdir(path)
                self.console.print(f"[green]📂 Changed to: {path.resolve()}[/green]")
            else:
                self.console.print(f"[red]❌ Directory not found: {path}[/red]")
        except PermissionError:
            self.console.print("[red]❌ Permission denied[/red]")
    
    def format_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f}{size_names[i]}"
    
    def is_binary_file(self, path: Path) -> bool:
        """Check if file is a binary executable"""
        try:
            with open(path, 'rb') as f:
                chunk = f.read(1024)
                return b'\x00' in chunk or path.suffix in ['.bin', '.exe', '.out', '']
        except:
            return False
    
    def is_executable_binary(self, file_path: Path) -> bool:
        """Check if file is an executable binary"""
        if not file_path.is_file() or not os.access(file_path, os.X_OK):
            return False
        
        try:
            # Check ELF magic number (Linux) or Mach-O (macOS)
            with open(file_path, 'rb') as f:
                magic = f.read(4)
                return (magic[:4] == b'\x7fELF' or  # ELF
                       magic[:4] == b'\xfe\xed\xfa\xce' or  # Mach-O 32-bit big endian
                       magic[:4] == b'\xce\xfa\xed\xfe' or  # Mach-O 32-bit little endian
                       magic[:4] == b'\xfe\xed\xfa\xcf' or  # Mach-O 64-bit big endian
                       magic[:4] == b'\xcf\xfa\xed\xfe')    # Mach-O 64-bit little endian
        except:
            return False
    
    def detect_file_type(self, file_path: str) -> str:
        """Detect if file is source, binary, or other"""
        path = Path(file_path)
        
        if not path.exists():
            return "missing"
        
        if path.is_dir():
            return "directory"
        
        if self.is_source_file(path):
            return "source"
        
        if self.is_executable_binary(path):
            return "binary"
        
        return "other"
    
    def get_all_files_from_directory(self, directory: str) -> dict:
        """Get all files from directory, categorized by type"""
        files = {
            'sources': [],
            'binaries': [],
            'other': []
        }
        
        try:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    file_type = self.detect_file_type(item_path)
                    if file_type == "source":
                        files['sources'].append(item_path)
                    elif file_type == "binary":
                        files['binaries'].append(item_path)
                    else:
                        files['other'].append(item_path)
        except PermissionError:
            self.console.print(f"[red]❌ Permission denied accessing: {directory}[/red]")
        
        return files
    
    def is_source_file(self, path: Path) -> bool:
        """Check if file is a source code file"""
        source_extensions = {'.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx'}
        return path.suffix.lower() in source_extensions

def main():
    """Main entry point"""
    import sys
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--help', '-h', 'help']:
            print("🧬 CodeGenome Modern CLI")
            print("\nUsage:")
            print("  python3 codegenome_cli.py          # Start interactive CLI")
            print("  python3 codegenome_cli.py --help   # Show this help")
            print("\nInteractive Commands:")
            print("  load <files/dirs>  # Load files (auto-detects sources vs binaries)")
            print("  ai                 # Generate AI variants from sources")
            print("  metame             # Generate MetaME variants from binaries")
            print("  analyze            # Compare binary differences (MetaME or compiled AI sources)")
            print("  menu               # Original interactive menu")
            print("  help               # Show all commands")
            print("  exit               # Exit CLI")
            return
        elif arg in ['--version', '-v']:
            print("CodeGenome CLI v1.0.0")
            return
    
    try:
        cli = ModernCodeGenomeCLI()
        cli.start()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()