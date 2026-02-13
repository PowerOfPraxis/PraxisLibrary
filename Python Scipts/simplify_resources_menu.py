"""
Simplify Resources mega-menu across all HTML files.
Removes column headers (Guides, Principles, AI & ND, About) and
consolidates all 9 links into a flat quick-links dropdown.

Usage:
  python "Python Scipts/simplify_resources_menu.py"           # dry-run
  python "Python Scipts/simplify_resources_menu.py" --execute  # apply
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXECUTE = "--execute" in sys.argv

# Match the entire mega-menu--multi-column div for Resources
# This regex captures the path prefix from any link inside
PATTERN = re.compile(
    r'<div class="mega-menu mega-menu--multi-column">\s*'
    r'<div class="mega-menu-section">\s*'
    r'<h4>Guides</h4>\s*'
    r'<a href="([^"]*?)pages/glossary\.html">Glossary</a>\s*'
    r'<a href="[^"]*?pages/faq\.html">FAQ</a>\s*'
    r'<a href="[^"]*?benchmarks/index\.html">AI Benchmarks</a>\s*'
    r'</div>\s*'
    r'<div class="mega-menu-section">\s*'
    r'<h4>Principles</h4>\s*'
    r'<a href="[^"]*?pages/responsible-ai\.html">Responsible AI</a>\s*'
    r'<a href="[^"]*?pages/security\.html">Security</a>\s*'
    r'<a href="[^"]*?pages/performance\.html">Performance</a>\s*'
    r'</div>\s*'
    r'<div class="mega-menu-section mega-menu-section--featured">\s*'
    r'<h4>AI (?:&amp;|&) ND</h4>\s*'
    r'<a href="[^"]*?neurodivergence/resources\.html">ND Resources</a>\s*'
    r'</div>\s*'
    r'<div class="mega-menu-section">\s*'
    r'<h4>About</h4>\s*'
    r'<a href="[^"]*?pages/about\.html">About Praxis</a>\s*'
    r'<a href="[^"]*?pages/audit-report\.html">Audit Report</a>\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)


def build_replacement(prefix):
    """Build flat quick-links dropdown with correct path prefix."""
    return (
        f'<div class="mega-menu mega-menu--categories">\n'
        f'                        <div class="mega-menu-quick-links">\n'
        f'                            <a href="{prefix}pages/glossary.html">Glossary</a>\n'
        f'                            <a href="{prefix}pages/faq.html">FAQ</a>\n'
        f'                            <a href="{prefix}benchmarks/index.html">AI Benchmarks</a>\n'
        f'                            <a href="{prefix}pages/responsible-ai.html">Responsible AI</a>\n'
        f'                            <a href="{prefix}pages/security.html">Security</a>\n'
        f'                            <a href="{prefix}neurodivergence/resources.html">ND Resources</a>\n'
        f'                            <a href="{prefix}pages/about.html">About Praxis</a>\n'
        f'                            <a href="{prefix}pages/audit-report.html">Audit Report</a>\n'
        f'                        </div>\n'
        f'                    </div>'
    )


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = PATTERN.search(content)
    if not match:
        return 0

    prefix = match.group(1)  # e.g. "", "../", "../../", "../../../"
    replacement = build_replacement(prefix)
    new_content = PATTERN.sub(replacement, content)

    if new_content != content:
        if EXECUTE:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
        return 1
    return 0


def main():
    mode = "EXECUTE" if EXECUTE else "DRY-RUN"
    print(f"=== Resources Menu Simplification ({mode}) ===\n")

    changed = 0
    total = 0

    for dirpath, _, filenames in os.walk(ROOT):
        # Skip hidden dirs, node_modules, etc.
        if any(skip in dirpath for skip in [".claude", ".git", "node_modules", "Python Scipts"]):
            continue
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            filepath = os.path.join(dirpath, fn)
            total += 1
            result = process_file(filepath)
            if result:
                rel = os.path.relpath(filepath, ROOT)
                print(f"  {'Updated' if EXECUTE else 'Would update'}: {rel}")
                changed += result

    print(f"\n{changed}/{total} files {'updated' if EXECUTE else 'would be updated'}")
    if not EXECUTE and changed > 0:
        print("Run with --execute to apply changes.")


if __name__ == "__main__":
    main()
