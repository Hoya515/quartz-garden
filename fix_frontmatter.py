#!/usr/bin/env python3
"""Fix duplicate 'publish: true' keys and double '---' in markdown frontmatter."""

import re
from pathlib import Path

def fix_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        content = f.read()

    original = content

    # Fix double --- at start (with optional BOM between)
    # Pattern: ---\n[optional BOM]---
    content = re.sub(r'^---\s*\n\s*\ufeff?---', '---\n', content, flags=re.MULTILINE)

    # Also handle case where BOM is at very start of file
    content = content.lstrip('\ufeff')

    # Check if file has frontmatter
    if not content.startswith('---'):
        return False

    # Find the end of frontmatter
    end_match = re.search(r'\n---\n', content[4:])
    if not end_match:
        return False

    frontmatter_end = end_match.start() + 4 + 4  # +4 for initial ---\n, +4 for \n---\n
    frontmatter = content[4:frontmatter_end-4]  # Content between --- and ---
    body = content[frontmatter_end:]

    # Check for duplicate publish: true
    lines = frontmatter.split('\n')
    publish_count = sum(1 for line in lines if line.strip() == 'publish: true')

    if publish_count > 1:
        # Remove all publish: true lines
        lines = [line for line in lines if line.strip() != 'publish: true']
        # Add publish: true at the beginning (after ---)
        lines.insert(0, 'publish: true')
        frontmatter = '\n'.join(lines)
        content = f'---\n{frontmatter}\n---{body}'

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    content_dir = Path("E:/Claude Brain/quartz-garden/content")
    fixed = 0
    for md_file in content_dir.rglob("*.md"):
        if fix_frontmatter(md_file):
            print(f"Fixed: {md_file.relative_to(content_dir)}")
            fixed += 1

    print(f"\nTotal fixed: {fixed}")

if __name__ == "__main__":
    main()