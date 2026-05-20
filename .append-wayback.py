"""
Append AI Wayback Machine sections to chapters 01..18 of intelligence/.
Pulls the blocks from wayback-machine-blocks.md by parsing its
'## N. `chapters/...md`' headings and the four-backtick code blocks beneath.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "wayback-machine-blocks.md"
text = SRC.read_text()

# Match each numbered step: "## N. `chapters/<file>.md`" followed by ```` ... ````
pattern = re.compile(
    r"##\s*\d+\.\s*`(chapters/[^`]+\.md)`\s*\n+"  # heading w/ filename
    r"````markdown\n"                              # opening 4-backtick fence
    r"(.*?)\n````",                                # content + closing fence
    re.DOTALL,
)

count = 0
for m in pattern.finditer(text):
    rel_path = m.group(1)
    block = m.group(2)
    target = ROOT / rel_path
    if not target.exists():
        print(f"  MISSING: {rel_path}")
        continue
    chapter_text = target.read_text()
    # Skip if a Wayback block already exists
    if "AI Wayback Machine" in chapter_text:
        print(f"  SKIPPED (already has Wayback): {rel_path}")
        continue
    # Ensure single trailing newline before append
    if not chapter_text.endswith("\n"):
        chapter_text += "\n"
    chapter_text += "\n" + block + "\n"
    target.write_text(chapter_text)
    print(f"  appended: {rel_path}")
    count += 1

print(f"\nappended Wayback blocks to {count} chapters")
