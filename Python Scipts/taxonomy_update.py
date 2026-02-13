"""
taxonomy_update.py — Bulk taxonomy replacement for Technique → Framework split

Performs safe, exact string replacements across all HTML files to update
the site taxonomy from "techniques" to "techniques & frameworks".

Usage:
    python "Python Scipts/taxonomy_update.py"              # Dry run (default)
    python "Python Scipts/taxonomy_update.py" --execute     # Actually write changes

Author: Praxis Library Automation
"""

import os
import sys
import glob

# === CONFIGURATION ===

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The 12 framework page filenames (for framework-only replacements)
FRAMEWORK_PAGES = {
    'costar.html', 'crisp.html', 'crispe.html', 'react.html',
    'tree-of-thought.html', 'graph-of-thought.html', 'skeleton-of-thought.html',
    'reflexion.html', 'dspy.html', 'mipro.html', 'agentflow.html', 'rag.html'
}

# === REPLACEMENT RULES ===

# Group 1: Apply to ALL HTML files
GLOBAL_REPLACEMENTS = [
    # Site-wide JSON-LD description
    (
        '110 prompting techniques, and interactive tools',
        '110 techniques & frameworks, and interactive tools'
    ),
    # Footer link text — CRISP
    (
        '>CRISP Technique</a>',
        '>CRISP Framework</a>'
    ),
    # Footer link text — CRISPE
    (
        '>CRISPE Technique</a>',
        '>CRISPE Framework</a>'
    ),
    # Footer link text — COSTAR
    (
        '>COSTAR Technique</a>',
        '>CO-STAR Framework</a>'
    ),
    # Footer link text — ReAct
    (
        '>ReAct Technique</a>',
        '>ReAct Framework</a>'
    ),
    # Name changes — CO-STAR (various contexts: title, meta, H1, OG, JSON-LD)
    (
        'CO-STAR Technique',
        'CO-STAR Framework'
    ),
    # Name changes — CRISP
    (
        'CRISP Technique',
        'CRISP Framework'
    ),
    # Name changes — CRISPE
    (
        'CRISPE Technique',
        'CRISPE Framework'
    ),
    # Name changes — ReAct
    (
        'ReAct Technique',
        'ReAct Framework'
    ),
]

# Group 2: Apply ONLY to the 12 framework pages
FRAMEWORK_ONLY_REPLACEMENTS = [
    (
        '"AI Prompting Techniques"',
        '"AI Prompting Frameworks"'
    ),
]


def find_html_files(root):
    """Find all HTML files recursively, excluding node_modules and .git."""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs and common excludes
        dirnames[:] = [d for d in dirnames if d not in {'.git', 'node_modules', '__pycache__', '.claude'}]
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))
    return sorted(html_files)


def is_framework_page(filepath):
    """Check if a file is one of the 12 framework pages."""
    basename = os.path.basename(filepath)
    return basename in FRAMEWORK_PAGES


def process_file(filepath, dry_run=True):
    """Process a single HTML file with all applicable replacements."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original
    changes = []

    # Apply global replacements
    for old, new in GLOBAL_REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes.append((old[:60], new[:60], count))

    # Apply framework-only replacements
    if is_framework_page(filepath):
        for old, new in FRAMEWORK_ONLY_REPLACEMENTS:
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                changes.append((old[:60], new[:60], count))

    if content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []


def main():
    dry_run = '--execute' not in sys.argv

    if dry_run:
        print('=' * 70)
        print('  TAXONOMY UPDATE — DRY RUN (no files will be modified)')
        print('  Run with --execute to apply changes')
        print('=' * 70)
    else:
        print('=' * 70)
        print('  TAXONOMY UPDATE — EXECUTING (files will be modified)')
        print('=' * 70)

    html_files = find_html_files(ROOT_DIR)
    print(f'\nFound {len(html_files)} HTML files\n')

    total_files_changed = 0
    total_replacements = 0
    replacement_summary = {}

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, ROOT_DIR)
        changes = process_file(filepath, dry_run)

        if changes:
            total_files_changed += 1
            print(f'  {rel_path}')
            for old, new, count in changes:
                total_replacements += count
                key = f'{old} -> {new}'
                replacement_summary[key] = replacement_summary.get(key, 0) + count
                print(f'    [{count}x] "{old}" -> "{new}"')

    print(f'\n{"=" * 70}')
    print(f'  SUMMARY')
    print(f'{"=" * 70}')
    print(f'  Files changed: {total_files_changed}/{len(html_files)}')
    print(f'  Total replacements: {total_replacements}')
    print(f'\n  Replacement breakdown:')
    for key, count in sorted(replacement_summary.items()):
        print(f'    [{count:3d}x] {key}')

    if dry_run:
        print(f'\n  ** DRY RUN — no files were modified **')
        print(f'  Run with --execute to apply these changes')
    else:
        print(f'\n  ** CHANGES APPLIED SUCCESSFULLY **')

    return 0


if __name__ == '__main__':
    sys.exit(main())
