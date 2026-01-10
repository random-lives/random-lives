#!/usr/bin/env python3
"""
Apply lifestyle classifications from JSON output to markdown files.

Handles both array format (multiple files) and single object format.
Supports double-check mode output.

Usage:
    python apply_lifestyle_classifications.py classifications.json
    python apply_lifestyle_classifications.py single_file.json
"""

import json
import re
import sys
from pathlib import Path

def apply_classification(filepath, old_lifestyle, new_lifestyle):
    """Apply lifestyle classification to a markdown file."""

    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if old_lifestyle field already exists
    if 'old_lifestyle:' in content:
        # Already processed, just update lifestyle
        pattern = r'^lifestyle: ".*"$'
        replacement = f'lifestyle: "{new_lifestyle}"'
    else:
        # First time processing - add old_lifestyle and update lifestyle
        # Find the lifestyle line
        pattern = r'^lifestyle: ".*"\nera: "Holocene"$'
        replacement = f'old_lifestyle: "{old_lifestyle}"\nlifestyle: "{new_lifestyle}"\nera: "Holocene"'

    # Apply the replacement
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)

    if new_content == content:
        print(f"  WARNING: No changes made to {filepath.name}")
        return False

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def process_entry(entry, base_dir):
    """Process a single classification entry."""
    filename = entry['filename']
    old_lifestyle = entry['old_lifestyle']
    new_lifestyle = entry['new_lifestyle']

    # Check for double-check mode
    double_check = entry.get('double_check')
    is_double_check = double_check is not None

    # Check if flagged
    is_flagged = new_lifestyle.startswith('FLAG:')

    # Try both directories
    filepath = base_dir / '_lives_pending' / filename
    if not filepath.exists():
        filepath = base_dir / '_lives' / filename

    if not filepath.exists():
        print(f"ERROR: File not found: {filename}")
        return None, is_flagged

    # In double-check mode, only apply if disagrees or flagged
    if is_double_check:
        if double_check == "agrees":
            print(f"  [✓ OK] {filename}: Double-check agrees with {new_lifestyle}")
            return "agree", False
        else:
            print(f"  [REVIEW] {filename}: {double_check}")

    # Apply classification
    try:
        if apply_classification(filepath, old_lifestyle, new_lifestyle):
            status = "FLAGGED" if is_flagged else "OK"
            print(f"  [{status}] {filename}: {old_lifestyle} -> {new_lifestyle}")
            return "applied", is_flagged
        else:
            return None, is_flagged
    except Exception as e:
        print(f"ERROR processing {filename}: {e}")
        raise

def main():
    if len(sys.argv) != 2:
        print("Usage: python apply_lifestyle_classifications.py classifications.json")
        sys.exit(1)

    json_file = Path(sys.argv[1])
    if not json_file.exists():
        print(f"Error: {json_file} not found")
        sys.exit(1)

    # Load classifications
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Handle both single object and array formats
    if isinstance(data, dict):
        classifications = [data]
        print("Processing single file")
    else:
        classifications = data
        print(f"Loaded {len(classifications)} classifications")

    # Determine base directory (check both _lives and _lives_pending)
    base_dir = Path(__file__).parent

    applied = 0
    agreed = 0
    flagged = 0
    errors = 0

    for entry in classifications:
        try:
            result, is_flagged = process_entry(entry, base_dir)
            if result == "applied":
                applied += 1
                if is_flagged:
                    flagged += 1
            elif result == "agree":
                agreed += 1
            elif result is None:
                errors += 1
        except Exception as e:
            errors += 1

    print(f"\nSummary:")
    print(f"  Applied: {applied}")
    if agreed > 0:
        print(f"  Agreed (double-check): {agreed}")
    print(f"  Flagged: {flagged}")
    print(f"  Errors: {errors}")

    if flagged > 0:
        print(f"\n⚠️  {flagged} files were flagged for manual review")
        print("   Search for 'FLAG:' in lifestyle field to find them")

if __name__ == '__main__':
    main()
