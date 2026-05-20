import re
from pathlib import Path
ch = Path('chapters')
n = 0
for f in sorted(ch.glob('*.md')):
    t = f.read_text()
    matches = list(re.finditer(r'<!--\s*→\s*\[TABLE:(.+?)-->', t, re.DOTALL))
    for m in matches:
        n += 1
        line = t[:m.start()].count('\n') + 1
        body = m.group(1).strip()
        print(f"\n=== #{n}  {f.name} L{line} ===")
        print(body[:600])
print(f"\n\nTOTAL: {n}")
