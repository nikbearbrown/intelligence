"""
Pass 3 — Wayback Machine validation:
  - Replace 3 subjects that fail the no-post-2000-alive rule
    (Toshiyuki Nakagaki → Howard Berg, May-Britt Moser → Rüdiger Wehner,
     Diana Reiss → William James)
  - Insert AI-generated-portrait stubs after the opening paragraph of every
    Wayback Machine section in chapters 1-18.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
CHAPTERS = ROOT / "chapters"

# ----------------------------------------------------------------------
# Replacement Wayback section content (full section bodies for ch 2, 7, 13)
# ----------------------------------------------------------------------

REPLACEMENT_SECTIONS = {
    "02-before-brains.md": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Howard Berg** was tracking individual *E. coli* under a custom-built tracking microscope in the 1970s — and proving that a bacterium navigates by *running and tumbling*, biasing its direction by the temporal derivative of attractant concentration — when most biology textbooks still treated single cells as inert. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Howard Berg, and how does his work tracking individual E. coli with a custom-built microscope connect to the question of whether brainless organisms can be intelligent? Keep it to three paragraphs. End with the single most surprising thing about his experiments or his career.
```

→ Search **"Howard Berg (biophysicist)"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *run-and-tumble* chemotaxis using a step-by-step worked example with concentration values
- Ask it to compare Berg's E. coli tracking to *Physarum*'s maze-solving — what computational ingredients do both have in common?
- Add a constraint: "Answer as if you're describing the experiment to a physicist who has never thought about bacteria"

What changes? What gets better? What gets worse?""",

    "07-navigation-and-spatial-intelligence.md": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Rüdiger Wehner** spent decades watching the desert ant *Cataglyphis* march across the Sahara — and proved that this insect navigates home by integrating the path it has just walked, second by second, with no map and no landmarks. The home vector is real, computed, and updated in flight. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who is Rüdiger Wehner, and how does his work on the desert ant Cataglyphis fortis connect to the broader question of how animals navigate without internal maps? Keep it to three paragraphs. End with the single most surprising thing about Cataglyphis navigation or about Wehner's career.
```

→ Search **"Rüdiger Wehner"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *path integration* in plain language, using a worked example of a foraging trip with three turns
- Ask it to compare Wehner's *Cataglyphis* findings to grid-cell discoveries in the mammalian entorhinal cortex
- Add a constraint: "Answer as if you're field-narrating a Wehner experiment for a documentary"

What changes? What gets better? What gets worse?""",

    "13-self-awareness.md": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **William James** drew the line carefully in *The Principles of Psychology* (1890), distinguishing the *material self* (the body), the *social self* (recognition by others), and the *spiritual self* (the introspecting "I") — the three-part division that this chapter's three subsystems trace directly to. The mirror test had not yet been invented. The distinctions had. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was William James, and how does his treatment of the self in The Principles of Psychology (1890) connect to modern empirical work on body-self, social-self, and narrative-self in animals and humans? Keep it to three paragraphs. End with the single most surprising thing about his account.
```

→ Search **"William James"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain James's distinction between the *I* (knower) and the *me* (known) in plain language
- Ask it to compare James's three-part self to what the mirror test, mark test, and theory-of-mind tasks each measure
- Add a constraint: "Answer as if you're writing the introduction to a 21st-century neuroscientific reading of James"

What changes? What gets better? What gets worse?""",
}

# ----------------------------------------------------------------------
# Portrait stubs — one per chapter (filename, full name, era, source)
# ----------------------------------------------------------------------

PORTRAITS = {
    "01-the-definition-problem.md":              ("lotfi-zadeh.jpg",          "Lotfi A. Zadeh",        "c. 1965",  "photograph", "portrait"),
    "02-before-brains.md":                        ("howard-berg.jpg",          "Howard Berg",           "c. 1980s", "photograph", "portrait"),
    "03-steering.md":                             ("valentino-braitenberg.jpg","Valentino Braitenberg", "c. 1980s", "photograph", "portrait"),
    "04-learning-and-memory.md":                  ("brenda-milner.jpg",        "Brenda Milner",         "c. 1960s", "photograph", "portrait"),
    "05-emotion.md":                              ("jaak-panksepp.jpg",        "Jaak Panksepp",         "c. 1990s", "photograph", "portrait"),
    "06-pattern-recognition-and-perception.md":   ("kunihiko-fukushima.jpg",   "Kunihiko Fukushima",    "c. 1980s", "photograph", "portrait"),
    "07-navigation-and-spatial-intelligence.md":  ("rudiger-wehner.jpg",       "Rüdiger Wehner",        "c. 1980s", "photograph", "portrait"),
    "08-reinforcement-and-prediction.md":         ("wolfram-schultz.jpg",      "Wolfram Schultz",       "c. 1990s", "photograph", "portrait"),
    "09-simulation-and-planning.md":              ("eleanor-maguire.jpg",      "Eleanor Maguire",       "c. 2000",  "photograph", "portrait"),
    "10-social-and-emotional-intelligence.md":    ("sarah-blaffer-hrdy.jpg",   "Sarah Blaffer Hrdy",    "c. 1990s", "photograph", "portrait"),
    "11-theory-of-mind.md":                       ("alison-gopnik.jpg",        "Alison Gopnik",         "c. 1990s", "photograph", "portrait"),
    "12-creativity.md":                           ("margaret-boden.jpg",       "Margaret Boden",        "c. 1990s", "photograph", "portrait"),
    "13-self-awareness.md":                       ("william-james.jpg",        "William James",         "c. 1890",  "photograph", "portrait"),
    "14-metacognition.md":                        ("asher-koriat.jpg",         "Asher Koriat",          "c. 1990s", "photograph", "portrait"),
    "15-language.md":                             ("ursula-bellugi.jpg",       "Ursula Bellugi",        "c. 1980s", "photograph", "portrait"),
    "16-collective-intelligence.md":              ("deborah-m-gordon.jpg",     "Deborah M. Gordon",     "c. 1990s", "photograph", "portrait"),
    "17-ai-as-data-point.md":                     ("seppo-linnainmaa.jpg",     "Seppo Linnainmaa",      "c. 1970",  "photograph", "portrait"),
    "18-extended-mind.md":                        ("edwin-hutchins.jpg",       "Edwin Hutchins",        "c. 1990s", "photograph", "portrait"),
}


def build_portrait_stub(filename, full_name, era, source_type, type_label):
    return (
        f"\n![{full_name}, {era}. AI-generated {type_label} based on a public domain {source_type}.](../images/{filename})\n"
        f"*{full_name}, {era}. AI-generated {type_label} based on a public domain {source_type} (Wikimedia Commons).*\n"
    )


def replace_section(chapter_text, new_section_body):
    """Find and replace the entire ## AI Wayback Machine section."""
    header = "## AI Wayback Machine"
    start = chapter_text.find(header)
    if start < 0:
        return chapter_text, False
    # Find the end: next top-level horizontal rule (---), or end of file
    # In our chapters, the Wayback section is the final section (no further --- after)
    # so we end at end-of-file.
    return chapter_text[:start] + new_section_body, True


def insert_portrait_stub(chapter_text, stub):
    """Insert stub after opening paragraph (which contains 'didn't appear from nowhere')."""
    header = "## AI Wayback Machine"
    idx = chapter_text.find(header)
    if idx < 0:
        return chapter_text, False
    # Skip a portrait stub already inserted
    after_header = chapter_text[idx:]
    if "AI-generated portrait" in after_header or "AI-generated illustration" in after_header:
        return chapter_text, False
    # Find the opening paragraph by locating the line that starts with
    # "The ideas in this chapter didn't appear from nowhere."
    open_line_re = re.compile(r"(The ideas in this chapter didn't appear from nowhere\..+?Here's a prompt to find out more — and then make it better\.)", re.DOTALL)
    m = open_line_re.search(chapter_text, idx)
    if not m:
        return chapter_text, False
    insert_at = m.end()
    new_text = chapter_text[:insert_at] + stub + chapter_text[insert_at:]
    return new_text, True


def apply():
    n_replaced = 0
    n_stubs = 0
    for f in sorted(CHAPTERS.glob('*.md')):
        bn = f.name
        if bn not in PORTRAITS:
            continue
        text = f.read_text()
        # Step 1: replace section content if this is one of the 3 subject swaps
        if bn in REPLACEMENT_SECTIONS:
            text, replaced = replace_section(text, REPLACEMENT_SECTIONS[bn])
            if replaced:
                n_replaced += 1
                print(f"  {bn}: subject replaced")
        # Step 2: insert portrait stub
        filename, full_name, era, source_type, type_label = PORTRAITS[bn]
        stub = build_portrait_stub(filename, full_name, era, source_type, type_label)
        text, inserted = insert_portrait_stub(text, stub)
        if inserted:
            n_stubs += 1
            print(f"  {bn}: portrait stub inserted ({full_name})")
        f.write_text(text)
    print(f"\nsubjects replaced: {n_replaced}")
    print(f"portrait stubs inserted: {n_stubs}")


if __name__ == "__main__":
    apply()
