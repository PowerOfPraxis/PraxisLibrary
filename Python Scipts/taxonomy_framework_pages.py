"""
taxonomy_framework_pages.py — Update hero badges, highlight boxes, and Related
section headings on the 12 framework pages.

Usage:
    python "Python Scipts/taxonomy_framework_pages.py"          # Dry run
    python "Python Scipts/taxonomy_framework_pages.py" --execute # Apply changes
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEARN_DIR = os.path.join(ROOT_DIR, 'learn')

# === HERO BADGE REPLACEMENTS ===
# (filename, old_badge_text, new_badge_text)
BADGE_UPDATES = [
    ('costar.html', 'Structured Framework', 'Structured Framework'),  # already changed by Phase 1
    ('crisp.html', 'Structured Framework', 'Structured Framework'),
    ('crispe.html', 'Structured Framework', 'Structured Framework'),
    ('react.html', 'Agentic Framework', 'Agentic Framework'),  # already changed
    ('tree-of-thought.html', 'Advanced Reasoning', 'Reasoning Framework'),
    ('graph-of-thought.html', 'Advanced Reasoning', 'Reasoning Framework'),
    ('skeleton-of-thought.html', 'Decomposition Framework', 'Decomposition Framework'),  # already changed
    ('reflexion.html', 'Self-Correction', 'Self-Correction Framework'),
    ('dspy.html', 'Optimization Framework', 'Optimization Framework'),  # already changed
    ('mipro.html', 'Optimization Framework', 'Optimization Framework'),  # already changed
    ('agentflow.html', 'Agentic Optimization Framework', 'Agentic Framework'),
    ('rag.html', 'Prompting Strategy', 'Retrieval Framework'),
]

# ALL badge updates needed (Phase 1 did NOT touch hero badge text)
BADGE_CHANGES_NEEDED = [
    ('costar.html', 'Structured Technique', 'Structured Framework'),
    ('crisp.html', 'Structured Technique', 'Structured Framework'),
    ('crispe.html', 'Structured Technique', 'Structured Framework'),
    ('react.html', 'Agentic Technique', 'Agentic Framework'),
    ('tree-of-thought.html', 'Advanced Reasoning', 'Reasoning Framework'),
    ('graph-of-thought.html', 'Advanced Reasoning', 'Reasoning Framework'),
    ('skeleton-of-thought.html', 'Decomposition Technique', 'Decomposition Framework'),
    ('reflexion.html', 'Self-Correction', 'Self-Correction Framework'),
    ('dspy.html', 'Optimization Technique', 'Optimization Framework'),
    ('mipro.html', 'Optimization Technique', 'Optimization Framework'),
    ('agentflow.html', 'Agentic Optimization Technique', 'Agentic Framework'),
    ('rag.html', 'Prompting Strategy', 'Retrieval Framework'),
]

# All 12 framework pages
ALL_FRAMEWORK_PAGES = [
    'costar.html', 'crisp.html', 'crispe.html', 'react.html',
    'tree-of-thought.html', 'graph-of-thought.html', 'skeleton-of-thought.html',
    'reflexion.html', 'dspy.html', 'mipro.html', 'agentflow.html', 'rag.html'
]


def process_file(filepath, dry_run=True):
    """Apply framework-specific updates to a single file."""
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Hero badge updates (only for pages that need it)
    for fname, old_badge, new_badge in BADGE_CHANGES_NEEDED:
        if basename == fname:
            old_str = f'<span class="hero-badge__text">{old_badge}</span>'
            new_str = f'<span class="hero-badge__text">{new_badge}</span>'
            count = content.count(old_str)
            if count > 0:
                content = content.replace(old_str, new_str)
                changes.append(('badge', old_badge, new_badge, count))

    # 2. Highlight box: "Technique Context" -> "Framework Context"
    old_hl = 'Technique Context:'
    new_hl = 'Framework Context:'
    count = content.count(old_hl)
    if count > 0:
        content = content.replace(old_hl, new_hl)
        changes.append(('highlight', old_hl, new_hl, count))

    # 3. Related Techniques -> Related Techniques & Frameworks
    old_related = '>Related Techniques</h2>'
    new_related = '>Related Techniques &amp; Frameworks</h2>'
    count = content.count(old_related)
    if count > 0:
        content = content.replace(old_related, new_related)
        changes.append(('related', old_related, new_related, count))

    if content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []


def main():
    dry_run = '--execute' not in sys.argv
    mode = 'DRY RUN' if dry_run else 'EXECUTING'

    print(f'{"=" * 60}')
    print(f'  FRAMEWORK PAGE UPDATES — {mode}')
    print(f'{"=" * 60}\n')

    total_changes = 0
    for fname in ALL_FRAMEWORK_PAGES:
        filepath = os.path.join(LEARN_DIR, fname)
        if not os.path.exists(filepath):
            print(f'  [MISSING] {fname}')
            continue

        changes = process_file(filepath, dry_run)
        if changes:
            print(f'  {fname}:')
            for change_type, old, new, count in changes:
                total_changes += count
                print(f'    [{change_type}] "{old}" -> "{new}" ({count}x)')
        else:
            print(f'  {fname}: no changes needed')

    print(f'\n{"=" * 60}')
    print(f'  Total changes: {total_changes}')
    if dry_run:
        print(f'  ** DRY RUN — no files modified **')
    else:
        print(f'  ** CHANGES APPLIED **')

    return 0


if __name__ == '__main__':
    sys.exit(main())
