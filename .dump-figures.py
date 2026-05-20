import re
from pathlib import Path
ch = Path('chapters')
n = 0
for f in sorted(ch.glob('*.md')):
    t = f.read_text()
    matches = list(re.finditer(r'<!--\s*→\s*\[(IMAGE|FIGURE|DIAGRAM|INFOGRAPHIC|CHART):(.+?)-->', t, re.DOTALL))
    for m in matches:
        n += 1
        line = t[:m.start()].count('\n') + 1
        kind = m.group(1)
        body = m.group(2).strip()
        print(f"\n=== #{n}  {f.name} L{line}  {kind} ===")
        print(body[:400])
print(f"\n\nTOTAL: {n}")
