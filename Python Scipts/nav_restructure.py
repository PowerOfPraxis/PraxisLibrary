"""
nav_restructure.py — Restructure main navigation site-wide.

Changes:
  1. "AI Foundations" → "History" (nav link text)
  2. Remove AI Benchmarks dropdown block entirely
  3. "AI Readiness" → "Readiness" (nav link text)
  4. Add "AI Benchmarks" link to Resources → Guides section
  5. Add "active" class to Resources link on benchmarks/ pages

Usage:
    python "Python Scipts/nav_restructure.py"          # Dry run
    python "Python Scipts/nav_restructure.py" --execute # Apply changes
"""

import os
import re
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_html_files(root):
    """Find all HTML files recursively, excluding .git and similar."""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in {'.git', 'node_modules', '__pycache__', '.claude'}]
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))
    return sorted(html_files)


def detect_prefix(content):
    """Detect path prefix by reading the Resources nav link href."""
    # Match: href="(prefix)pages/resources.html" — skip absolute URLs
    matches = re.findall(r'href="([^"]*?)pages/resources\.html"', content)
    for m in matches:
        if not m.startswith('http'):
            return m  # e.g. '', '../', '../../', '../../../'
    return '../'  # fallback


def is_benchmarks_page(filepath):
    """Check if file is in benchmarks/ directory."""
    rel = os.path.relpath(filepath, ROOT_DIR).replace('\\', '/')
    return rel.startswith('benchmarks/')


def remove_benchmarks_block(lines):
    """Remove the AI Benchmarks dropdown from the nav.
    Returns (new_lines, removed_count)."""
    # Find the line with >AI Benchmarks</a>
    benchmark_line = None
    for i, line in enumerate(lines):
        if '>AI Benchmarks</a>' in line:
            benchmark_line = i
            break

    if benchmark_line is None:
        return lines, 0

    # Walk backwards to find <div class="nav-item has-dropdown">
    start = benchmark_line
    for i in range(benchmark_line, -1, -1):
        if 'class="nav-item has-dropdown"' in lines[i]:
            start = i
            break

    # Count <div / </div> to find the matching close
    depth = 0
    end = start
    for i in range(start, len(lines)):
        depth += lines[i].count('<div')
        depth -= lines[i].count('</div>')
        if depth == 0:
            end = i
            break

    removed = end - start + 1
    return lines[:start] + lines[end + 1:], removed


def add_benchmarks_to_guides(lines, prefix):
    """Add AI Benchmarks link after FAQ in the Resources Guides section.
    Returns (new_lines, added)."""
    # Find the FAQ link in the Resources mega-menu
    # We need to be careful: FAQ link appears in the Resources mega-menu only
    # Look for the pattern: >FAQ</a> followed by </div> (end of Guides section)
    for i, line in enumerate(lines):
        if '>FAQ</a>' in line:
            # Verify this is in the Resources mega-menu (not elsewhere)
            # Check nearby lines for <h4>Guides</h4>
            context_start = max(0, i - 5)
            context = ''.join(lines[context_start:i + 1])
            if '<h4>Guides</h4>' in context:
                # Determine indentation from the FAQ line
                indent = ''
                m = re.match(r'^(\s*)', line)
                if m:
                    indent = m.group(1)
                # Insert after this line
                new_line = f'{indent}<a href="{prefix}benchmarks/index.html">AI Benchmarks</a>\n'
                new_lines = lines[:i + 1] + [new_line] + lines[i + 1:]
                return new_lines, 1

    return lines, 0


def fix_benchmarks_active(lines):
    """On benchmarks/ pages, add 'active' to the Resources nav link.
    Returns (new_lines, changed)."""
    for i, line in enumerate(lines):
        if 'aria-expanded="false">Resources</a>' in line:
            if 'class="nav-link"' in line and 'active' not in line:
                new_line = line.replace('class="nav-link"', 'class="nav-link active"')
                lines[i] = new_line
                return lines, 1
    return lines, 0


def process_file(filepath, dry_run=True):
    """Apply all nav restructuring to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # Step 1: Rename nav link text
    old1 = '>AI Foundations</a>'
    new1 = '>History</a>'
    count = content.count(old1)
    if count > 0:
        content = content.replace(old1, new1)
        changes.append(('rename', 'AI Foundations -> History', count))

    old2 = '>AI Readiness</a>'
    new2 = '>Readiness</a>'
    count = content.count(old2)
    if count > 0:
        content = content.replace(old2, new2)
        changes.append(('rename', 'AI Readiness -> Readiness', count))

    # Step 2: Remove AI Benchmarks dropdown block (line-based)
    lines = content.split('\n')
    # Preserve trailing newline state
    had_trailing = content.endswith('\n')
    lines_with_newlines = [line + '\n' for line in lines]
    if not had_trailing and lines_with_newlines:
        lines_with_newlines[-1] = lines_with_newlines[-1].rstrip('\n')

    lines_with_newlines, removed = remove_benchmarks_block(lines_with_newlines)
    if removed > 0:
        changes.append(('remove', f'AI Benchmarks block ({removed} lines)', 1))

    # Step 3: Detect prefix and add benchmarks to Guides section
    content_temp = ''.join(lines_with_newlines)
    prefix = detect_prefix(content_temp)

    lines_with_newlines, added = add_benchmarks_to_guides(lines_with_newlines, prefix)
    if added > 0:
        changes.append(('add', f'AI Benchmarks link in Guides (prefix: {prefix})', 1))

    # Step 4: Fix active class on benchmarks/ pages
    if is_benchmarks_page(filepath):
        lines_with_newlines, fixed = fix_benchmarks_active(lines_with_newlines)
        if fixed > 0:
            changes.append(('active', 'Resources nav-link active on benchmarks page', 1))

    content = ''.join(lines_with_newlines)

    if content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []


def main():
    dry_run = '--execute' not in sys.argv
    mode = 'DRY RUN' if dry_run else 'EXECUTING'

    print(f'{"=" * 70}')
    print(f'  NAV RESTRUCTURE — {mode}')
    print(f'{"=" * 70}\n')

    html_files = find_html_files(ROOT_DIR)
    print(f'Found {len(html_files)} HTML files\n')

    total_files = 0
    total_changes = 0
    summary = {}

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, ROOT_DIR)
        changes = process_file(filepath, dry_run)
        if changes:
            total_files += 1
            print(f'  {rel_path}')
            for change_type, desc, count in changes:
                total_changes += count
                key = f'[{change_type}] {desc}'
                summary[key] = summary.get(key, 0) + count
                print(f'    [{change_type}] {desc}')

    print(f'\n{"=" * 70}')
    print(f'  SUMMARY')
    print(f'{"=" * 70}')
    print(f'  Files changed: {total_files}/{len(html_files)}')
    print(f'  Total operations: {total_changes}')
    print(f'\n  Breakdown:')
    for key, count in sorted(summary.items()):
        print(f'    [{count:3d}x] {key}')

    if dry_run:
        print(f'\n  ** DRY RUN — no files modified **')
        print(f'  Run with --execute to apply changes')
    else:
        print(f'\n  ** CHANGES APPLIED SUCCESSFULLY **')

    return 0


if __name__ == '__main__':
    sys.exit(main())
