"""
taxonomy_nav_update.py — Update nav link "Techniques" → "Discover" site-wide,
plus quick-links and breadcrumbs that point to learn/index.html.

Does NOT touch:
  - <span class="mega-menu-group__label">Techniques</span>  (mega-menu group label)
  - <h4>Techniques</h4>  (footer heading)
  - Any other "Techniques" text inside page content

Usage:
    python "Python Scipts/taxonomy_nav_update.py"          # Dry run
    python "Python Scipts/taxonomy_nav_update.py" --execute # Apply changes
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# === REPLACEMENT RULES ===

# All replacements are exact string → exact string
HTML_REPLACEMENTS = [
    # 1. Nav link (every page — the top-level nav link text)
    (
        'aria-expanded="false">Techniques</a>',
        'aria-expanded="false">Discover</a>'
    ),
    # 2. Quick-link + breadcrumb variants (different path depths)
    # Root level (index.html)
    (
        '<a href="learn/index.html">Techniques</a>',
        '<a href="learn/index.html">Discover</a>'
    ),
    # 1-deep non-learn pages (benchmarks/, pages/, tools/, etc.)
    (
        '<a href="../learn/index.html">Techniques</a>',
        '<a href="../learn/index.html">Discover</a>'
    ),
    # learn/ pages (1-deep from root)
    (
        '<a href="index.html">Techniques</a>',
        '<a href="index.html">Discover</a>'
    ),
    # learn/modality/ hub pages (2-deep from root)
    (
        '<a href="../index.html">Techniques</a>',
        '<a href="../index.html">Discover</a>'
    ),
    # learn/modality/audio/ etc. pages (3-deep from root)
    (
        '<a href="../../index.html">Techniques</a>',
        '<a href="../../index.html">Discover</a>'
    ),
]

# CSS replacement in styles.css
CSS_FILE = os.path.join(ROOT_DIR, 'styles.css')
CSS_REPLACEMENTS = [
    (
        'content: "TECHNIQUES";',
        'content: "DISCOVER";'
    ),
]


def find_html_files(root):
    """Find all HTML files recursively, excluding .git and similar."""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {'.git', 'node_modules', '__pycache__', '.claude'}]
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))
    return sorted(html_files)


def process_html_file(filepath, dry_run=True):
    """Apply nav/quick-link/breadcrumb replacements to a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original
    changes = []

    for old, new in HTML_REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes.append((old[:70], new[:70], count))

    if content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []


def process_css(dry_run=True):
    """Apply CSS replacement in styles.css."""
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original
    changes = []

    for old, new in CSS_REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes.append((old, new, count))

    if content != original:
        if not dry_run:
            with open(CSS_FILE, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []


def main():
    dry_run = '--execute' not in sys.argv
    mode = 'DRY RUN' if dry_run else 'EXECUTING'

    print(f'{"=" * 70}')
    print(f'  NAV LINK UPDATE — {mode}')
    print(f'{"=" * 70}\n')

    # HTML files
    html_files = find_html_files(ROOT_DIR)
    print(f'Found {len(html_files)} HTML files\n')

    total_files = 0
    total_replacements = 0
    summary = {}

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, ROOT_DIR)
        changes = process_html_file(filepath, dry_run)
        if changes:
            total_files += 1
            print(f'  {rel_path}')
            for old, new, count in changes:
                total_replacements += count
                key = f'{old} -> {new}'
                summary[key] = summary.get(key, 0) + count
                print(f'    [{count}x] "{old}" -> "{new}"')

    # CSS file
    print(f'\n  --- CSS ---')
    css_changes = process_css(dry_run)
    if css_changes:
        print(f'  styles.css')
        for old, new, count in css_changes:
            total_replacements += count
            print(f'    [{count}x] "{old}" -> "{new}"')
    else:
        print(f'  styles.css: no changes needed')

    print(f'\n{"=" * 70}')
    print(f'  SUMMARY')
    print(f'{"=" * 70}')
    print(f'  HTML files changed: {total_files}/{len(html_files)}')
    print(f'  Total replacements: {total_replacements}')
    print(f'\n  Breakdown:')
    for key, count in sorted(summary.items()):
        print(f'    [{count:3d}x] {key}')
    if css_changes:
        for old, new, count in css_changes:
            print(f'    [{count:3d}x] {old} -> {new}')

    if dry_run:
        print(f'\n  ** DRY RUN — no files modified **')
        print(f'  Run with --execute to apply changes')
    else:
        print(f'\n  ** CHANGES APPLIED SUCCESSFULLY **')

    return 0


if __name__ == '__main__':
    sys.exit(main())
