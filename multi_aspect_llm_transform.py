#!/usr/bin/env python3
"""
Multi-Aspect LLM Metamorphism Module
Pure LLM-driven binary transformation with 6 strategies.
"""

import subprocess
import re
import time
import requests
import os
from typing import List, Dict, Tuple, Optional

# Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "gemma3:27b"
LLM_TIMEOUT = 300  # Increased for thinking models
MAX_RETRIES = 3
DEBUG = True

# Current model being used (set by run_all_strategies)
CURRENT_MODEL = None

# Models that use <think>...</think> reasoning blocks
THINKING_MODELS = ["deepseek-r1", "qwq", "r1"]

def is_thinking_model(model_name: str) -> bool:
    """Check if model uses thinking/reasoning blocks."""
    return any(tm in model_name.lower() for tm in THINKING_MODELS)

def extract_thinking_output(response: str) -> str:
    """
    Extract final output from thinking model response.
    Thinking models wrap reasoning in <think>...</think> tags.
    We want only the content AFTER the closing </think> tag.
    Also handles variations and cleans up any remaining reasoning text.
    """
    import re
    
    result = response
    
    # Handle various tag formats (case insensitive)
    # Try: </think>, </thinking>, </reasoning>
    for close_tag in ['</think>', '</thinking>', '</reasoning>']:
        if close_tag.lower() in result.lower():
            # Find the tag case-insensitively
            idx = result.lower().rfind(close_tag.lower())
            if idx != -1:
                result = result[idx + len(close_tag):].strip()
                debug_log(f"Extracted {len(result)} chars after {close_tag} tag", "INFO")
                break
    
    # Also clean up any remaining reasoning prefixes
    # Common patterns: "Let me...", "I'll analyze...", "Looking at...", "Okay, let's..."
    reasoning_prefixes = [
        r"^(ok(?:ay)?[,.]?\s*)?let['']?s?\s+(?:analyze|look|delve|examine|see|think|consider)",
        r"^i['']?ll?\s+(?:analyze|look|examine|consider)",
        r"^looking\s+at",
        r"^here['']?s?\s+(?:the|my|what)",
        r"^the\s+instruction\s+.*?can\s+be\s+expanded",
        r"^the\s+instruction\s+.*?can\s+be\s+transformed",
        r"^first[,.]?\s+(?:let|i)",
    ]
    
    for pattern in reasoning_prefixes:
        # Match roughly start of string
        if re.search(pattern, result.lower()[:300], re.MULTILINE): 
             # found a conversational prefix.
             # Now look for the first line that matches the output format: address: ... -> ...
             lines = result.split('\n')
             start_idx = -1
             for i, line in enumerate(lines):
                 # Strong check for "ADDR: OLD -> NEW" format
                 if re.search(r'(?:0x)?[0-9a-fA-F]+:\s*.*\s*->', line):
                     start_idx = i
                     break
             
             if start_idx != -1:
                 result = '\n'.join(lines[start_idx:])
                 debug_log(f"Cleaned conversational preamble, starting from line {start_idx+1}", "INFO")
             break
    
    return result

def debug_log(msg: str, level: str = "INFO"):
    """Verbose debug output."""
    if DEBUG:
        timestamp = time.strftime("%H:%M:%S")
        colors = {"INFO": "\033[94m", "OK": "\033[92m", "WARN": "\033[93m", "ERR": "\033[91m", "END": "\033[0m"}
        print(f"{colors.get(level, '')}{timestamp} [{level}] {msg}{colors['END']}")

def call_llm_with_retry(prompt: str, max_retries: int = MAX_RETRIES, model_override: str = None) -> Optional[str]:
    """Call LLM with automatic retry on failure.
    
    Args:
        prompt: The prompt to send to the LLM
        max_retries: Number of retry attempts
        model_override: Optional model name to use instead of default OLLAMA_MODEL
    """
    model_to_use = model_override or CURRENT_MODEL or OLLAMA_MODEL
    
    for attempt in range(max_retries):
        try:
            debug_log(f"LLM call attempt {attempt + 1}/{max_retries} (model: {model_to_use})", "INFO")
            debug_log(f"Prompt preview: {prompt[:100]}...", "INFO")
            
            response = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model_to_use,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.3,
                        "num_predict": 4096 if is_thinking_model(model_to_use) else 1500
                    }
                },
                timeout=LLM_TIMEOUT
            )
            
            if response.status_code == 200:
                result = response.json().get("response", "")
                # Handle thinking models - extract output after </think>
                if is_thinking_model(model_to_use):
                    result = extract_thinking_output(result)
                debug_log(f"LLM response ({len(result)} chars): {result[:80]}...", "OK")
                return result
            else:
                debug_log(f"LLM HTTP error: {response.status_code}", "WARN")
                
        except Exception as e:
            debug_log(f"LLM call failed: {e}", "ERR")
            time.sleep(2)  # Wait before retry
    
    debug_log(f"All {max_retries} attempts failed", "ERR")
    return None


# =============================================================================
# SECTION FILTERING AND VALIDATION HELPERS
# =============================================================================

def get_text_section_range(asm_text: str) -> Tuple[int, int]:
    """
    Extract .text section address range from objdump output.
    Returns (start_addr, end_addr) or (0, 0) if not found.
    """
    in_text = False
    text_start = 0
    text_end = 0
    
    for line in asm_text.split('\n'):
        if 'Disassembly of section .text:' in line:
            in_text = True
            continue
        if in_text and line.startswith('Disassembly of section'):
            # Reached next section, stop
            break
        if in_text:
            # Match instruction line: "  10e0:  f3 0f 1e fa    endbr64"
            match = re.match(r'^\s*([0-9a-fA-F]+):', line)
            if match:
                addr = int(match.group(1), 16)
                if text_start == 0:
                    text_start = addr
                text_end = addr + 16  # Approximate end
    
    return (text_start, text_end)


def filter_to_text_section(asm_text: str) -> str:
    """
    Filter objdump output to only include .text section.
    Removes .plt, .init, .fini, .plt.got, .plt.sec which are not safe to patch.
    """
    lines = []
    in_text = False
    
    for line in asm_text.split('\n'):
        if 'Disassembly of section .text:' in line:
            in_text = True
            lines.append(line)
            continue
        if in_text and line.startswith('Disassembly of section'):
            # Reached next section, stop collecting
            break
        if in_text:
            lines.append(line)
    
    if not lines:
        debug_log("WARNING: No .text section found, using full ASM", "WARN")
        return asm_text
    
    return '\n'.join(lines)


def validate_with_keystone(instr: str, addr: int = 0) -> Tuple[bool, int]:
    """
    Validate instruction is assemblable by Keystone.
    Returns (success, assembled_size_in_bytes).
    """
    try:
        from keystone import Ks, KS_ARCH_X86, KS_MODE_64, KsError
        ks = Ks(KS_ARCH_X86, KS_MODE_64)
        encoding, count = ks.asm(instr, addr)
        return (True, len(encoding))
    except Exception as e:
        debug_log(f"Keystone validation failed for '{instr}': {e}", "WARN")
        return (False, 0)


def parse_instruction_with_size(line: str) -> Optional[Dict]:
    """
    Parse an objdump instruction line to extract address, byte size, and instruction.
    Input: "  10e0:  f3 0f 1e fa    endbr64"
    Output: {"addr": "10e0", "size": 4, "instr": "endbr64"}
    """
    # Pattern with hex bytes
    match = re.match(r'^\s*([0-9a-fA-F]+):\s+([0-9a-fA-F]{2}(?:\s+[0-9a-fA-F]{2})*)\s+(.+)$', line)
    if match:
        hex_bytes = match.group(2)
        return {
            "addr": match.group(1),
            "size": len(hex_bytes.split()),
            "instr": match.group(3).strip()
        }
    return None


# =============================================================================
# STRATEGY 1: FUNCTION-LEVEL TRANSFORMATION
# =============================================================================
def extract_functions(asm_text: str) -> List[Dict]:
    """Extract functions from disassembly."""
    functions = []
    current_func = None
    current_lines = []
    
    for line in asm_text.split('\n'):
        # Function header: "0000000000001400 <function_name>:"
        match = re.match(r'^([0-9a-fA-F]+)\s+<([^>]+)>:', line)
        if match:
            if current_func:
                functions.append({
                    'name': current_func,
                    'addr': current_addr,
                    'body': '\n'.join(current_lines)
                })
            current_func = match.group(2)
            current_addr = match.group(1)
            current_lines = [line]
        elif current_func and line.strip():
            current_lines.append(line)
    
    if current_func:
        functions.append({
            'name': current_func,
            'addr': current_addr,
            'body': '\n'.join(current_lines)
        })
    
    return functions

def transform_function(func: Dict) -> List[Tuple[str, str, str]]:
    """Transform a single function using LLM with size constraints."""
    prompt = f"""You are a binary analyst doing metamorphic transformation on x86-64.

TASK: Generate instruction substitutions that are functionally equivalent and SAME SIZE OR SMALLER.

CRITICAL RULES:
1. Output ONLY: address: old_instruction -> new_instruction
2. New instruction MUST be SAME BYTE SIZE or SMALLER than original
3. NEVER use: endbr64, endbr32, QWORD PTR/DWORD PTR in jump/call operands
4. NEVER change: calls, jumps, or ret instructions  
5. Use PURE Intel syntax - NO annotations like <func@plt> or comments
6. Use register names directly: rax, rbx, etc. - not [label] or <symbol>

SAFE TRANSFORMATIONS (with byte sizes):
- [2B] xor eax, eax -> sub eax, eax (2B, equal)
- [3B] xor rax, rax -> sub rax, rax (3B, equal)
- [3B] test rax, rax -> or rax, rax (3B, equal)
- [5B] mov eax, 0 -> xor eax, eax (5B->2B, smaller OK)

FORBIDDEN (will be rejected):
- endbr64, endbr32
- Any instruction with <symbol> or @plt
- jz QWORD PTR ... (invalid syntax)
- Comments (#) or semicolons (;)

FUNCTION ({func['name']}) - .text section:
{func['body'][:2000]}

OUTPUT (substitutions only, one per line, or EMPTY if no safe transforms):"""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'(?:0x)?([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            new = match.group(3).strip()
            # Filter known bad patterns
            if any(bad in new.lower() for bad in ['endbr', '<', '@plt', '#', ';', 'qword ptr']):
                debug_log(f"  SKIP (forbidden pattern): {new}", "WARN")
                continue
            
            # PRE-VALIDATE with Keystone before accepting
            addr = int(match.group(1), 16)
            is_valid, asm_size = validate_with_keystone(new, addr)
            if not is_valid:
                debug_log(f"  SKIP (keystone failed): {new}", "WARN")
                continue
            
            addr_str = "0x" + match.group(1)
            old = match.group(2).strip()
            patches.append((addr_str, old, new))
            debug_log(f"  PATCH: {addr_str}: {old} -> {new} ({asm_size}B)", "OK")
    
    return patches



# =============================================================================
# STRATEGY 2: BASIC BLOCK TRANSFORMATION
# =============================================================================
def extract_basic_blocks(asm_text: str) -> List[Dict]:
    """Extract basic blocks with instruction byte sizes from raw objdump.
    
    Parses lines like: "  1064:  48 83 ec 08    sub    rsp,0x8"
    Extracts: addr=1064, size=4, instr="sub rsp,0x8"
    """
    blocks = []
    current_block = []
    block_start = None
    
    # Pattern to capture: address, hex bytes, instruction
    # "  1064:  48 83 ec 08    sub    rsp,0x8"
    instr_pattern = re.compile(
        r'^\s*([0-9a-fA-F]+):\s+([0-9a-fA-F]{2}(?:\s+[0-9a-fA-F]{2})*)\s+(.+)$'
    )
    # Fallback pattern for --no-show-raw-insn format
    instr_pattern_no_bytes = re.compile(
        r'^\s*([0-9a-fA-F]+):\s+(\S.*)$'
    )
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            hex_bytes = match.group(2)
            instr = match.group(3).strip()
            byte_count = len(hex_bytes.split())
        else:
            match = instr_pattern_no_bytes.match(line)
            if match:
                addr = match.group(1)
                instr = match.group(2).strip()
                byte_count = 0  # Unknown size
            else:
                continue
        
        if block_start is None:
            block_start = addr
        
        current_block.append({
            'addr': addr,
            'instr': instr,
            'size': byte_count
        })
        
        # Block terminators
        first_word = instr.split()[0].lower() if instr else ''
        if first_word in ['jmp', 'je', 'jne', 'jz', 'jnz', 'ja', 'jb', 'jg', 'jl', 
                          'jge', 'jle', 'jae', 'jbe', 'call', 'ret', 'hlt']:
            if len(current_block) >= 2:
                blocks.append({
                    'start': block_start,
                    'instructions': current_block.copy()
                })
            current_block = []
            block_start = None
    
    return blocks[:50]


def transform_basic_block(block: Dict) -> List[Tuple[str, str, str]]:
    """Transform a single basic block with size-aware constraints."""
    
    # Format block with sizes: "1064: [4B] sub rsp,0x8"
    block_lines = []
    for i in block['instructions']:
        size_str = f"[{i['size']}B]" if i['size'] > 0 else "[?B]"
        block_lines.append(f"{i['addr']}: {size_str} {i['instr']}")
    block_text = '\n'.join(block_lines)
    
    prompt = f"""You are transforming x86-64 assembly for metamorphism.

FUNCTION BLOCK (with instruction byte sizes):
{block_text}

CRITICAL CONSTRAINTS:
1. New instruction MUST be SAME SIZE or SMALLER than original (shown as [NB])
2. Use PURE Intel syntax - NO annotations like <func@plt> or comments
3. NEVER use: endbr64, endbr32 (not supported by assembler)
4. NEVER change calls or jumps - they have position-dependent encoding
5. ONLY transform arithmetic/logic instructions

SAFE SAME-SIZE TRANSFORMATIONS:
- [2B] xor eax, eax -> sub eax, eax  (both 2 bytes)
- [3B] xor rax, rax -> sub rax, rax  (both 3 bytes)
- [3B] test rax, rax -> or rax, rax  (both 3 bytes)
- [2B] je X -> jz X  (same opcode, 2 bytes)
- [2B] jne X -> jnz X  (same opcode, 2 bytes)

OUTPUT FORMAT (one per line, ONLY lines you want to change):
address: old_instruction -> new_instruction

SKIP: calls, jumps to externals, nops, endbr64, and any instruction you cannot make same-size.
DO NOT OUTPUT anything else. Just the substitution lines or nothing."""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'(?:0x)?([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            new_instr = match.group(3).strip()
            # Filter out known bad patterns
            if any(bad in new_instr.lower() for bad in ['endbr', '<', '@plt', '#', ';', 'qword ptr']):
                debug_log(f"  SKIP (forbidden pattern): {new_instr}", "WARN")
                continue
            
            # PRE-VALIDATE with Keystone
            addr = int(match.group(1), 16)
            is_valid, asm_size = validate_with_keystone(new_instr, addr)
            if not is_valid:
                debug_log(f"  SKIP (keystone failed): {new_instr}", "WARN")
                continue
            
            patches.append(("0x" + match.group(1), match.group(2).strip(), new_instr))
            debug_log(f"  PATCH: 0x{match.group(1)}: {match.group(2)} -> {new_instr} ({asm_size}B)", "OK")
    
    return patches



# =============================================================================
# STRATEGY 3: CFG TRANSFORMATION (Control Flow)
# =============================================================================
def extract_cfg_edges(asm_text: str) -> List[Dict]:
    """Extract control flow edges (jumps and their targets)."""
    edges = []
    
    # Pattern supports BOTH formats (with and without hex bytes)
    instr_pattern = re.compile(r'^\s*([0-9a-fA-F]+):\s+(?:[0-9a-fA-F]{2}[0-9a-fA-F ]*\s+)?(\S.*)$')
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            instr = match.group(2).strip()
            
            # Parse jump instruction: "je     1016 <_init+0x16>"
            jump_match = re.match(r'^(j[a-z]+)\s+([0-9a-fA-F]+)', instr, re.IGNORECASE)
            if jump_match:
                edges.append({
                    'addr': addr,
                    'type': jump_match.group(1),
                    'target': jump_match.group(2)
                })
    
    return edges[:30]  # Limit

def transform_cfg_edge(edge: Dict) -> List[Tuple[str, str, str]]:
    """Transform a control flow edge (invert condition, etc.)."""
    prompt = f"""Transform this x86-64 jump. Output ONLY ONE substitution line.

INSTRUCTION: {edge['type']} 0x{edge['target']} at address 0x{edge['addr']}

VALID TRANSFORMS:
- je -> jz (same opcode)
- jne -> jnz (same opcode)  
- jz -> jnz (invert with target swap)

OUTPUT FORMAT: address: old -> new
EXAMPLE: 1234: je 5678 -> jz 5678

OUTPUT (single line only, NO explanation):"""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            patches.append(("0x" + match.group(1), match.group(2).strip(), match.group(3).strip()))
            break  # Only first match for CFG
    
    return patches


# =============================================================================
# STRATEGY 4: DATA SECTION TRANSFORMATION
# =============================================================================
def extract_data_references(asm_text: str) -> List[Dict]:
    """Extract references to data (strings, constants)."""
    refs = []
    
    # Pattern supports BOTH formats (with and without hex bytes)
    instr_pattern = re.compile(r'^\s*([0-9a-fA-F]+):\s+(?:[0-9a-fA-F]{2}[0-9a-fA-F ]*\s+)?(\S.*)$')
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            instr = match.group(2).strip()
            
            # Look for lea with rip-relative: "lea    rax,[rip+0x3fc9]"
            lea_match = re.match(r'^lea\s+(\w+),.*\[rip\+0x([0-9a-fA-F]+)\]', instr, re.IGNORECASE)
            if lea_match:
                refs.append({
                    'addr': addr,
                    'reg': lea_match.group(1),
                    'offset': lea_match.group(2),
                    'line': line.strip()
                })
                continue
            
            # Look for mov with rip-relative: "mov    rax,QWORD PTR [rip+0x3fc9]"
            mov_match = re.match(r'^mov\s+(\w+),.*\[rip\+0x([0-9a-fA-F]+)\]', instr, re.IGNORECASE)
            if mov_match:
                refs.append({
                    'addr': addr,
                    'reg': mov_match.group(1),
                    'offset': mov_match.group(2),
                    'line': line.strip()
                })
    
    return refs[:20]

def transform_data_ref(ref: Dict) -> List[Tuple[str, str, str]]:
    """Suggest data reference transformation."""
    prompt = f"""Transform this LEA instruction. Output ONLY ONE substitution.

INSTRUCTION at 0x{ref['addr']}: lea with [rip+offset]

VALID TRANSFORMS:
- Use different dest register: lea rdi -> lea rax
- Keep same (if no transform possible): lea rdi,[rip+X] -> lea rdi,[rip+X]

OUTPUT FORMAT: address: old -> new
EXAMPLE: 1400: lea rdi,[rip+0x1d01] -> lea rax,[rip+0x1d01]

OUTPUT (single line, NO explanation):"""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            patches.append(("0x" + match.group(1), match.group(2).strip(), match.group(3).strip()))
            break
    
    return patches


# =============================================================================
# STRATEGY 5: CALL GRAPH TRANSFORMATION
# =============================================================================
def extract_calls(asm_text: str) -> List[Dict]:
    """Extract function calls."""
    calls = []
    
    # Pattern supports BOTH formats (with and without hex bytes)
    instr_pattern = re.compile(r'^\s*([0-9a-fA-F]+):\s+(?:[0-9a-fA-F]{2}[0-9a-fA-F ]*\s+)?(\S.*)$')
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            instr = match.group(2).strip()
            
            # Parse call instruction: "call   1360 <function>" or "call   rax"
            call_match = re.match(r'^call\s+([0-9a-fA-F]+)(?:\s+<([^>]+)>)?', instr, re.IGNORECASE)
            if call_match:
                calls.append({
                    'addr': addr,
                    'target': call_match.group(1),
                    'name': call_match.group(2) or 'unknown'
                })
    
    return calls[:20]

def transform_call(call: Dict) -> List[Tuple[str, str, str]]:
    """Suggest call transformation."""
    prompt = f"""Transform this CALL instruction. Output ONLY ONE substitution.

CALL at 0x{call['addr']}: call {call['target']}

VALID TRANSFORMS:
- Direct to indirect: call 1234 -> mov rax, 0x1234; call rax
- If PLT call, keep same: call X@plt -> call X@plt

OUTPUT FORMAT: address: old -> new
EXAMPLE: 1420: call 1360 -> call 1360

OUTPUT (single line, NO explanation, or NONE if no transform):"""

    response = call_llm_with_retry(prompt)
    if not response or 'NONE' in response.upper():
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            patches.append(("0x" + match.group(1), match.group(2).strip(), match.group(3).strip()))
            break
    
    return patches


# =============================================================================
# STRATEGY 6: STACK LAYOUT TRANSFORMATION
# =============================================================================
def extract_stack_ops(asm_text: str) -> List[Dict]:
    """Extract stack operations (push/pop/sub rsp/add rsp)."""
    ops = []
    
    # Pattern supports BOTH formats (with and without hex bytes)
    instr_pattern = re.compile(r'^\s*([0-9a-fA-F]+):\s+(?:[0-9a-fA-F]{2}[0-9a-fA-F ]*\s+)?(\S.*)$')
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            instr = match.group(2).strip()
            first_word = instr.split()[0].lower() if instr else ''
            
            # Push/pop with register: "push   rbp" (not "push QWORD PTR")
            if first_word in ['push', 'pop']:
                # Match push/pop with simple register operand (r??, e??, ?x, etc)
                operand_match = re.match(r'^(push|pop)\s+([re]?[abcds][xpil]|r[0-9]+[dwb]?|[re]?bp|[re]?sp|[re]?si|[re]?di)', instr, re.IGNORECASE)
                if operand_match:
                    ops.append({
                        'addr': addr,
                        'op': first_word,
                        'operand': operand_match.group(2),
                        'line': line.strip()
                    })
            
            # Sub/add rsp: "sub    rsp,0x8" or "add    rsp,0x8"
            elif first_word in ['sub', 'add']:
                rsp_match = re.match(r'^(sub|add)\s+rsp\s*,\s*(\S+)', instr, re.IGNORECASE)
                if rsp_match:
                    ops.append({
                        'addr': addr,
                        'op': first_word + ' rsp',
                        'operand': rsp_match.group(2),
                        'line': line.strip()
                    })
    
    return ops[:30]

def transform_stack_op(op: Dict) -> List[Tuple[str, str, str]]:
    """Transform stack operation."""
    prompt = f"""Transform this stack op. Output ONLY ONE substitution.

INSTRUCTION at 0x{op['addr']}: {op['op']} {op['operand']}

VALID TRANSFORMS:
- sub rsp, 8 -> lea rsp, [rsp-8]
- add rsp, 8 -> lea rsp, [rsp+8]
- push X -> sub rsp, 8; mov [rsp], X

OUTPUT FORMAT: address: old -> new
EXAMPLE: 1004: sub rsp, 8 -> lea rsp, [rsp-8]

OUTPUT (single line, NO explanation):"""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            patches.append(("0x" + match.group(1), match.group(2).strip(), match.group(3).strip()))
            break
    
    return patches


# =============================================================================
# STRATEGY 7: INSTRUCTION INFLATION (LLM-BASED TRAMPOLINES)
# =============================================================================
def extract_inflatable_instructions(asm_text: str) -> List[Dict]:
    """Extract short instructions that can be inflated to longer equivalents."""
    inflatables = []
    
    # Pattern for instruction lines
    instr_pattern = re.compile(r'^\s*([0-9a-fA-F]+):\s+(?:[0-9a-fA-F]{2}[0-9a-fA-F ]*\s+)?(\S.*)$')
    
    # Instructions that can be inflated
    inflatable_patterns = [
        r'^xor\s+(\w+),\s*\1',      # xor reg, reg (zero)
        r'^sub\s+(\w+),\s*\1',      # sub reg, reg (zero)
        r'^test\s+(\w+),\s*\1',     # test reg, reg
        r'^mov\s+\w+,\s*0x?0$',     # mov reg, 0
        r'^inc\s+\w+',               # inc reg
        r'^dec\s+\w+',               # dec reg
        r'^push\s+r[a-z0-9]+$',      # push reg
        r'^pop\s+r[a-z0-9]+$',       # pop reg
        r'^nop$',                    # nop
    ]
    
    for line in asm_text.split('\n'):
        match = instr_pattern.match(line)
        if match:
            addr = match.group(1)
            instr = match.group(2).strip()
            
            for pattern in inflatable_patterns:
                if re.match(pattern, instr, re.IGNORECASE):
                    inflatables.append({
                        'addr': addr,
                        'instr': instr,
                        'line': line.strip()
                    })
                    break
    
    return inflatables[:30]  # Limit


def transform_inflate_instruction(instr: Dict) -> List[Tuple[str, str, str]]:
    """Ask LLM to inflate a short instruction into a longer equivalent sequence."""
    prompt = f"""You are an expert at instruction inflation for metamorphic transformation.

TASK: Expand this short instruction into a functionally equivalent LONGER sequence.
The goal is to increase code size while preserving semantics.

INSTRUCTION at 0x{instr['addr']}: {instr['instr']}

VALID INFLATIONS (examples):
- xor eax, eax -> push rbx; xor ebx, ebx; mov eax, ebx; pop rbx
- mov eax, 0 -> push rbx; xor ebx, ebx; mov eax, ebx; pop rbx
- inc eax -> add eax, 1
- push rax -> sub rsp, 8; mov [rsp], rax
- nop -> xchg eax, eax

OUTPUT FORMAT: address: old_instruction -> new_instruction(s)
EXAMPLE: 1234: xor eax, eax -> sub eax, eax

OUTPUT (single line, NO explanation):"""

    response = call_llm_with_retry(prompt)
    if not response:
        return []
    
    patches = []
    for line in response.split('\n'):
        match = re.match(r'(?:0x)?([0-9a-fA-F]+):\s*(.+?)\s*->\s*(.+)', line)
        if match:
            patches.append(("0x" + match.group(1), match.group(2).strip(), match.group(3).strip()))
            break
    
    return patches


# =============================================================================
# MAIN TRANSFORMATION PIPELINE
# =============================================================================
def run_all_strategies(asm_text: str, model: str = None) -> Dict[str, List[Tuple[str, str, str]]]:
    """Run all 6 transformation strategies and collect patches.
    
    Args:
        asm_text: Disassembled code text (should include hex bytes for size info)
        model: Optional model name to use (defaults to OLLAMA_MODEL)
    """
    global CURRENT_MODEL
    CURRENT_MODEL = model or OLLAMA_MODEL
    debug_log(f"Using model: {CURRENT_MODEL}", "INFO")
    
    # CRITICAL: Filter to .text section only - no PLT/GOT/init patching
    text_only_asm = filter_to_text_section(asm_text)
    text_start, text_end = get_text_section_range(asm_text)
    debug_log(f"Filtered to .text section: 0x{text_start:x} - 0x{text_end:x}", "INFO")
    
    all_patches = {}
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 1: FUNCTION TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    functions = extract_functions(text_only_asm)  # Use filtered ASM
    # Filter boring functions
    functions = [f for f in functions if not any(x in f['name'] for x in ['@plt', '_start', '_init', '_fini', 'deregister'])]
    debug_log(f"Found {len(functions)} user functions", "INFO")
    
    func_patches = []
    for func in functions[:5]:  # Limit to 5 functions
        debug_log(f"Transforming: {func['name']}", "INFO")
        patches = transform_function(func)
        func_patches.extend(patches)
    all_patches['functions'] = func_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 2: BASIC BLOCK TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    blocks = extract_basic_blocks(text_only_asm)
    debug_log(f"Found {len(blocks)} basic blocks", "INFO")
    
    block_patches = []
    for block in blocks[:10]:  # Limit
        patches = transform_basic_block(block)
        block_patches.extend(patches)
    all_patches['blocks'] = block_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 3: CFG TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    edges = extract_cfg_edges(text_only_asm)
    debug_log(f"Found {len(edges)} CFG edges", "INFO")
    
    cfg_patches = []
    for edge in edges[:10]:
        patches = transform_cfg_edge(edge)
        cfg_patches.extend(patches)
    all_patches['cfg'] = cfg_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 4: DATA REFERENCE TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    refs = extract_data_references(text_only_asm)
    debug_log(f"Found {len(refs)} data references", "INFO")
    
    data_patches = []
    for ref in refs[:10]:
        patches = transform_data_ref(ref)
        data_patches.extend(patches)
    all_patches['data'] = data_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 5: CALL GRAPH TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    calls = extract_calls(text_only_asm)
    debug_log(f"Found {len(calls)} function calls", "INFO")
    
    call_patches = []
    for call in calls[:10]:
        patches = transform_call(call)
        call_patches.extend(patches)
    all_patches['calls'] = call_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 6: STACK LAYOUT TRANSFORMATION", "INFO")
    debug_log("=" * 60, "INFO")
    stack_ops = extract_stack_ops(text_only_asm)
    debug_log(f"Found {len(stack_ops)} stack operations", "INFO")
    
    stack_patches = []
    for op in stack_ops[:10]:
        patches = transform_stack_op(op)
        stack_patches.extend(patches)
    all_patches['stack'] = stack_patches
    
    debug_log("=" * 60, "INFO")
    debug_log("STRATEGY 7: INSTRUCTION INFLATION (TRAMPOLINES)", "INFO")
    debug_log("=" * 60, "INFO")
    
    # Find short instructions that can be inflated
    inflatables = extract_inflatable_instructions(text_only_asm)
    debug_log(f"Found {len(inflatables)} inflatable instructions", "INFO")
    
    inflate_patches = []
    for instr in inflatables[:15]:  # Limit to 15
        patches = transform_inflate_instruction(instr)
        inflate_patches.extend(patches)
    all_patches['inflate'] = inflate_patches
    
    # Summary
    debug_log("=" * 60, "INFO")
    debug_log("SUMMARY", "OK")
    debug_log("=" * 60, "INFO")
    total = 0
    for strategy, patches in all_patches.items():
        debug_log(f"  {strategy}: {len(patches)} patches", "OK")
        total += len(patches)
    debug_log(f"  TOTAL: {total} patches", "OK")
    
    return all_patches


def apply_patches_r2(binary_path: str, patches: Dict[str, List[Tuple[str, str, str]]]) -> int:
    """Apply all patches using r2."""
    applied = 0
    
    for strategy, patch_list in patches.items():
        for addr, old, new in patch_list:
            cmd = f"r2 -q -w -c 'wa {new} @ {addr}' {binary_path} 2>/dev/null"
            result = subprocess.run(cmd, shell=True, capture_output=True, timeout=10)
            if result.returncode == 0:
                applied += 1
                debug_log(f"Applied: {addr}: {new}", "OK")
            else:
                debug_log(f"Failed: {addr}: {new}", "WARN")
    
    return applied


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python multi_aspect_llm_transform.py <binary_path>")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    
    # Disassemble
    debug_log(f"Disassembling {binary_path}...", "INFO")
    cmd = f"objdump -d -M intel {binary_path}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    asm_text = result.stdout
    debug_log(f"Disassembly: {len(asm_text)} chars", "OK")
    
    # Run all strategies
    patches = run_all_strategies(asm_text)
    
    # Apply patches
    import shutil
    output_path = binary_path + "_llm_multi"
    shutil.copy2(binary_path, output_path)
    
    applied = apply_patches_r2(output_path, patches)
    debug_log(f"Applied {applied} total patches to {output_path}", "OK")
