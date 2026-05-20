"""
Append LLM Exercise blocks to chapters 01..19 of intelligence/.
Pulls blocks from llm-exercise-blocks.md by parsing its
'## N. `chapters/...md`' headings and the four-backtick code blocks beneath.

For chapters that already have an AI Wayback Machine section (1-18),
insert the LLM Exercise BEFORE the Wayback section header.
For chapter 19 (no Wayback), append at the end.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "llm-exercise-blocks.md"
text = SRC.read_text()

# Match each numbered step
pattern = re.compile(
    r"##\s*\d+\.\s*`(chapters/[^`]+\.md)`\s*\n+"
    r"````markdown\n"
    r"(.*?)\n````",
    re.DOTALL,
)

WAYBACK_HEADER = "## AI Wayback Machine"

count = 0
for m in pattern.finditer(text):
    rel_path = m.group(1)
    block = m.group(2).rstrip()
    target = ROOT / rel_path
    if not target.exists():
        print(f"  MISSING: {rel_path}")
        continue
    chapter_text = target.read_text()
    # Skip if an LLM Exercise block already exists
    if "LLM Exercise — Chapter" in chapter_text:
        print(f"  SKIPPED (already has LLM Exercise): {rel_path}")
        continue

    # Find the Wayback Machine section, if any
    wayback_idx = chapter_text.find(WAYBACK_HEADER)

    if wayback_idx >= 0:
        # The block we want to insert ends with --- separator already
        # We need to insert the block immediately before the --- that precedes
        # the Wayback header. Walk back from wayback_idx to find that ---.
        before_wayback = chapter_text[:wayback_idx].rstrip()
        # Look for trailing --- separator above wayback_idx
        # Pattern: ...content...\n\n---\n\n## AI Wayback Machine
        # We want to insert: \n\n{block}\n right before the --- separator
        m2 = re.search(r'\n\n---\n*$', before_wayback)
        if m2:
            insert_pos = before_wayback[:m2.start()].rstrip()
            # block already starts with --- separator; preserve double newline
            new_text = (
                insert_pos + "\n\n" + block + "\n\n---\n\n" +
                chapter_text[wayback_idx:]
            )
        else:
            # Fallback: insert block right before wayback header
            new_text = (
                before_wayback + "\n\n" + block + "\n\n---\n\n" +
                chapter_text[wayback_idx:]
            )
        target.write_text(new_text)
        print(f"  inserted (before Wayback): {rel_path}")
    else:
        # No Wayback section — append at end (chapter 19)
        if not chapter_text.endswith("\n"):
            chapter_text += "\n"
        chapter_text += "\n" + block + "\n"
        target.write_text(chapter_text)
        print(f"  appended (no Wayback): {rel_path}")
    count += 1

print(f"\ninserted LLM Exercise blocks into {count} chapters")
