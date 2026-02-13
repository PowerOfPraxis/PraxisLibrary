#!/usr/bin/env python3
"""Simplify the Discover mega-menu across all 168 HTML files.

Changes:
1. Remove the Prompt Engineering mega-menu-group (7 category links)
2. Remove the Modality mega-menu-group (5 modality links)
3. Rename quick-link "Discover" to "Prompt Engineering"

Usage:
    python "Python Scipts/simplify_discover_menu.py"           # dry-run
    python "Python Scipts/simplify_discover_menu.py" --execute  # apply
"""
import os
import re
import sys
import glob

DRY_RUN = '--execute' not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def find_html_files():
    patterns = [
        os.path.join(ROOT, '*.html'),
        os.path.join(ROOT, '**', '*.html'),
    ]
    files = set()
    for p in patterns:
        files.update(glob.glob(p, recursive=True))
    # Exclude .claude directory
    files = [f for f in files if '.claude' not in f]
    return sorted(files)

def remove_mega_menu_group(lines, label):
    """Remove a <div class="mega-menu-group"> block identified by its label text."""
    removed = 0
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for the label inside a mega-menu-group
        if f'mega-menu-group__label">{label}</span>' in line:
            # Walk backwards to find the parent <div class="mega-menu-group">
            start = i - 1
            while start >= 0 and 'class="mega-menu-group"' not in lines[start]:
                start -= 1
            if start < 0:
                result.append(line)
                i += 1
                continue
            # Remove lines already added from start to current position
            result = result[:start]
            # Now find the closing </div> by counting div nesting
            depth = 0
            j = start
            while j < len(lines):
                depth += lines[j].count('<div')
                depth -= lines[j].count('</div>')
                if depth <= 0:
                    break
                j += 1
            # Skip from start to j (inclusive)
            removed = j - start + 1
            i = j + 1
            continue
        result.append(line)
        i += 1
    return result, removed

def rename_quick_link(lines):
    """Rename >Discover</a> to >Prompt Engineering</a> inside mega-menu-quick-links."""
    renamed = 0
    in_quick_links = False
    result = []
    for line in lines:
        if 'mega-menu-quick-links' in line:
            in_quick_links = True
        if in_quick_links and '>Discover</a>' in line:
            line = line.replace('>Discover</a>', '>Prompt Engineering</a>')
            renamed += 1
            in_quick_links = False  # Only rename the first occurrence
        # Reset if we exit the quick-links div
        if in_quick_links and '</div>' in line and 'mega-menu-quick-links' not in line:
            in_quick_links = False
        result.append(line)
    return result, renamed

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip files without the Discover mega-menu
    if 'mega-menu--categories' not in content:
        return 0

    lines = content.split('\n')

    # Step 1: Remove Prompt Engineering group
    lines, pe_removed = remove_mega_menu_group(lines, 'Prompt Engineering')

    # Step 2: Remove Modality group
    lines, mod_removed = remove_mega_menu_group(lines, 'Modality')

    # Step 3: Rename Discover quick-link to Prompt Engineering
    lines, renamed = rename_quick_link(lines)

    changes = pe_removed + mod_removed + renamed
    if changes > 0 and not DRY_RUN:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

    return changes

def main():
    files = find_html_files()
    print(f"{'DRY RUN' if DRY_RUN else 'EXECUTING'} — scanning {len(files)} HTML files\n")

    total_changed = 0
    changed_files = 0

    for filepath in files:
        rel = os.path.relpath(filepath, ROOT)
        changes = process_file(filepath)
        if changes > 0:
            print(f"  {'[would change]' if DRY_RUN else '[changed]'} {rel} ({changes} modifications)")
            changed_files += 1
            total_changed += changes

    print(f"\n{'Would modify' if DRY_RUN else 'Modified'} {changed_files} files ({total_changed} total changes)")
    if DRY_RUN:
        print("\nRe-run with --execute to apply changes.")

if __name__ == '__main__':
    main()
