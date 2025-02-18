import re
import csv
from collections import Counter
from prettytable import PrettyTable

def analyze_disassembly(filepath):
    """Analyzes a disassembled file and counts instruction occurrences."""

    instruction_counts = Counter()

    try:
        with open(filepath, 'r') as f:
            for line in f:
                # Improved regex to capture instructions more reliably.
                # This regex assumes instructions start at the beginning of a line,
                # possibly preceded by a label (like "100002f18:").
                # Adjust this regex if your disassembler's output has a different format.
                match = re.match(r"^\s*(?:[0-9a-fA-F]+:\s*)?([a-zA-Z]+)\s+", line)
                if match:
                    instruction = match.group(1)
                    instruction_counts[instruction] += 1
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None

    return instruction_counts

def write_to_csv(instruction_counts, output_file):
    """Writes instruction counts to a CSV file."""
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Instruction', 'Count'])  # Header row
        for instr, count in instruction_counts.items():
            writer.writerow([instr, count])

def print_table(instruction_counts):
    """Prints instruction counts in a pretty table."""
    table = PrettyTable()
    table.field_names = ["Instruction", "Count"]
    for instr, count in instruction_counts.items():
        table.add_row([instr, count])
    print(table)

if __name__ == "__main__":
    disassembly_file = "diss.asm"  # Replace with your .asm file
    output_csv = "instruction_counts.csv"

    counts = analyze_disassembly(disassembly_file)

    if counts:
        write_to_csv(counts, output_csv)
        print(f"Instruction counts saved to {output_csv}")

        print("\nInstruction Counts:")
        print_table(counts)