"""
Pass 2 — generate 53 editorial-monochrome figures (SVG + PNG) for the
intelligence book. Replaces IMAGE/FIGURE/DIAGRAM/INFOGRAPHIC/CHART tokens.

Style: warm-grayscale, Georgia serif, 1px borders, no rounded corners.
"""

import math
import re
import random
from pathlib import Path

INK = "#1a1714"
GRAY_DARK = "#4a4540"
GRAY_MID = "#8a8480"
GRAY_LIGHT = "#c8c4c0"
CREAM = "#f5f2ee"
WHITE = "#fdfcfb"

ROOT = Path(__file__).parent
CHAPTERS = ROOT / "chapters"
IMAGES = ROOT / "images"
IMAGES.mkdir(exist_ok=True)


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------

def svg_open(w=700, h=420):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'font-family="Georgia, \'Times New Roman\', serif" font-size="11" fill="{INK}">'
        f'<defs>'
        f'  <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
        f'    <polygon points="0 0, 8 3, 0 6" fill="{INK}"/>'
        f'  </marker>'
        f'  <marker id="arrowL" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
        f'    <polygon points="0 0, 10 4, 0 8" fill="{INK}"/>'
        f'  </marker>'
        f'</defs>'
        f'<rect width="{w}" height="{h}" fill="{WHITE}"/>'
    )


def svg_close():
    return '</svg>'


def text(x, y, s, *, size=11, anchor="start", weight="normal", italic=False, fill=INK):
    style = f'font-size="{size}"'
    if anchor != "start":
        style += f' text-anchor="{anchor}"'
    if weight != "normal":
        style += f' font-weight="{weight}"'
    if italic:
        style += ' font-style="italic"'
    style += f' fill="{fill}"'
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<text x="{x}" y="{y}" {style}>{s}</text>'


def box(x, y, w, h, *, fill=CREAM, stroke=INK, sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, *, stroke=INK, sw=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def circle(cx, cy, r, *, fill="none", stroke=INK, sw=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def ellipse(cx, cy, rx, ry, *, fill="none", stroke=INK, sw=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def path(d, *, fill="none", stroke=INK, sw=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def arrow(x1, y1, x2, y2, *, stroke=INK, sw=1.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" marker-end="url(#arrow)"/>'


def title(t, x=350, y=20):
    return text(x, y, t, size=13, anchor="middle", weight="bold")


# ======================================================================
# Builders: one per figure
# ======================================================================

def f01_definition_timeline():
    s = svg_open(700, 360)
    s += title("Major intelligence definitions, 1905–2019", 350, 22)
    # Horizontal axis from 1900 to 2020
    ax = 60
    aw = 580
    ay = 230
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID, sw=1)
    # Tick marks per decade
    for yr in range(1900, 2030, 10):
        x = ax + (yr - 1900) / 120 * aw
        s += line(x, ay - 4, x, ay + 4, stroke=GRAY_MID, sw=0.7)
        if yr % 20 == 0:
            s += text(x, ay + 18, str(yr), anchor="middle", size=9, fill=GRAY_DARK)
    # Entries
    entries = [
        (1905, "Binet", "judgment, auto-critique", "clinical triage", "above"),
        (1944, "Wechsler", "aggregate adaptive capacity", "psychometric measurement", "below"),
        (1983, "Gardner", "multiple intelligences", "educational profiling", "above"),
        (1985, "Sternberg", "analytic + creative + practical", "cognitive theory", "below"),
        (2007, "Legg–Hutter", "goals across environments", "computational AI", "above"),
        (2019, "Chollet", "skill-acquisition efficiency", "AI evaluation", "below"),
    ]
    for yr, name, defn, app, side in entries:
        x = ax + (yr - 1900) / 120 * aw
        if side == "above":
            ty = ay - 20
            s += line(x, ay, x, ty + 4, stroke=INK, sw=0.8)
            s += text(x, ty - 50, name, anchor="middle", weight="bold", size=11)
            s += text(x, ty - 36, f"({yr})", anchor="middle", size=9, fill=GRAY_DARK)
            s += text(x, ty - 22, defn, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
            s += text(x, ty - 6, f"→ {app}", anchor="middle", size=9, fill=GRAY_DARK)
        else:
            ty = ay + 30
            s += line(x, ay, x, ty - 4, stroke=INK, sw=0.8)
            s += text(x, ty + 12, name, anchor="middle", weight="bold", size=11)
            s += text(x, ty + 26, f"({yr})", anchor="middle", size=9, fill=GRAY_DARK)
            s += text(x, ty + 40, defn, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
            s += text(x, ty + 56, f"→ {app}", anchor="middle", size=9, fill=GRAY_DARK)
    s += text(350, 340, "Each definition was built for a real purpose. The history is one of accumulation, not convergence.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f02_shalizi_pca():
    s = svg_open(700, 360)
    s += title("The same algebra produces a 'general factor' from any positively correlated set", 350, 22)
    # Two panels
    for i, (cx, head, vars_, factor) in enumerate([
        (180, "Cognitive tests", ["verbal", "spatial", "math"], "g  (\"general intelligence\")"),
        (520, "Cars", ["horsepower", "top speed", "sticker price"], "general car-quality factor"),
    ]):
        s += text(cx, 50, head, anchor="middle", weight="bold", size=12)
        # Variable boxes on the left
        for j, v in enumerate(vars_):
            y = 90 + j * 50
            s += box(cx - 100, y, 90, 30)
            s += text(cx - 55, y + 19, v, anchor="middle", size=10)
            # Arrow to PCA box
            s += arrow(cx - 10, y + 15, cx + 30, 165)
        # PCA box
        s += box(cx + 30, 145, 90, 40, fill=GRAY_LIGHT)
        s += text(cx + 75, 161, "PCA", anchor="middle", weight="bold", size=11)
        s += text(cx + 75, 177, "(first PC)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
        # Output factor
        s += arrow(cx + 75, 185, cx + 75, 230)
        s += box(cx - 50, 230, 250, 40, fill=CREAM)
        s += text(cx + 75, 252, factor, anchor="middle", weight="bold", size=11)
    # Punch line
    s += text(350, 310, "Mathematical structure identical. The first algorithm yields biology;", anchor="middle", italic=True, size=10)
    s += text(350, 326, "the second yields a number Consumer Reports already knew. Neither shows that g is a thing.",
              anchor="middle", italic=True, size=10)
    return s + svg_close()


def f03_physarum_maze():
    s = svg_open(700, 360)
    s += title("Physarum polycephalum solving a maze in four frames", 350, 22)
    # 4 frames
    captions = [
        "1. Inoculation",
        "2. Full coverage",
        "3. Pruning dead ends",
        "4. Single shortest path",
    ]
    for i, cap in enumerate(captions):
        x0 = 30 + i * 165
        s += box(x0, 50, 150, 200)
        # Maze walls (same in all panels)
        # Outer border
        s += box(x0 + 12, 60, 126, 180, fill=WHITE, stroke=INK, sw=1)
        # Internal walls (some sample maze walls)
        walls = [
            (x0 + 12, 100, 60, 0), (x0 + 90, 100, 48, 0),
            (x0 + 60, 60, 0, 60), (x0 + 60, 140, 0, 50),
            (x0 + 90, 140, 0, 60), (x0 + 12, 180, 50, 0),
        ]
        for wx, wy, ww, wh in walls:
            s += line(wx, wy, wx + ww, wy + wh, sw=1.5)
        # Start (top-left) and end (bottom-right) markers
        s += circle(x0 + 25, 75, 4, fill=INK)
        s += circle(x0 + 125, 225, 4, fill=INK)
        # Physarum at varying coverage
        if i == 0:
            # Just blob at start
            s += circle(x0 + 25, 75, 8, fill=GRAY_MID, stroke=INK, sw=0.5)
        elif i == 1:
            # Fills entire maze
            for k in range(40):
                cx_ = x0 + 12 + (k % 8) * 16 + 4
                cy_ = 60 + (k // 8) * 36 + 8
                if x0 + 12 < cx_ < x0 + 138 and 60 < cy_ < 240:
                    s += circle(cx_, cy_, 7, fill=GRAY_LIGHT, stroke=GRAY_MID, sw=0.4)
        elif i == 2:
            # Partly retracted — main path + some branches
            s += path(f"M {x0 + 25} 75 L {x0 + 50} 75 L {x0 + 50} 130 L {x0 + 80} 130 L {x0 + 80} 200 L {x0 + 125} 200 L {x0 + 125} 225",
                      stroke=INK, sw=4)
            # Some thinning dead ends
            for (sx, sy, ex, ey) in [(x0 + 50, 75, x0 + 50, 90), (x0 + 80, 130, x0 + 100, 130)]:
                s += line(sx, sy, ex, ey, stroke=GRAY_LIGHT, sw=2)
        else:
            # Final clean path
            s += path(f"M {x0 + 25} 75 L {x0 + 50} 75 L {x0 + 50} 130 L {x0 + 80} 130 L {x0 + 80} 200 L {x0 + 125} 200 L {x0 + 125} 225",
                      stroke=INK, sw=4)
        s += text(x0 + 75, 270, cap, anchor="middle", weight="bold", size=11)
    s += text(350, 320, "No nervous system. Network self-pruning toward the optimal path between food sources.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f04_physarum_tokyo():
    s = svg_open(700, 360)
    s += title("Physarum's network and the actual Tokyo rail map", 350, 22)
    # Two panels
    centers = [(180, "Physarum on agar with oat flakes"), (520, "Tokyo Kanto rail network")]
    # Approximate "city" positions matching across panels
    cities = [(0, 0), (-50, -30), (40, -40), (-30, 30), (50, 20), (-15, -55), (60, -10), (10, 40), (-45, 5), (25, -65)]
    labels = ["Tokyo", "Yokohama", "Chiba", "Hachioji", "Saitama", "Kawagoe", "Funabashi", "Kawasaki", "Tachikawa", "Tsukuba"]
    for cx_panel, head in centers:
        s += text(cx_panel, 50, head, anchor="middle", weight="bold", size=12)
        # Frame
        s += box(cx_panel - 130, 65, 260, 230)
        cx0, cy0 = cx_panel, 180
        # Draw nodes
        positions = [(cx0 + dx * 1.6, cy0 + dy * 1.6) for dx, dy in cities]
        # Edges (similar in both panels — that's the point)
        edges = [(0,1), (0,2), (0,3), (0,4), (0,6), (0,7), (1,3), (1,8), (2,5), (2,9), (4,6), (4,9), (3,8), (5,9), (1,7)]
        for a, b in edges:
            x1, y1 = positions[a]
            x2, y2 = positions[b]
            s += line(x1, y1, x2, y2, stroke=INK, sw=1.5)
        # Nodes
        for i, (x, y) in enumerate(positions):
            s += circle(x, y, 5, fill=INK, stroke=INK)
        # Label only Tokyo (center) and one outlier
        s += text(positions[0][0] + 8, positions[0][1] - 4, "Tokyo", size=9, fill=GRAY_DARK)
    s += text(350, 320, "Tero et al. 2010 — the slime mold reproduces the topology of an engineered transportation network.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f05_ecoli_signal_cascade():
    s = svg_open(700, 360)
    s += title("E. coli chemotaxis — fast signaling and slow methylation memory", 350, 22)
    # Two columns
    # Left: fast cascade
    s += text(180, 60, "Fast signaling arm  (~100 ms)", anchor="middle", weight="bold", size=12)
    fast_steps = [
        (90, "MCP receptor", "binds attractant"),
        (200, "CheA kinase", "autophosphorylates"),
        (290, "CheY-P", "diffuses to motor"),
        (380, "Flagellar motor", "switches CW ↔ CCW"),
    ]
    for y, name, sub in fast_steps:
        s += box(60, y, 240, 40)
        s += text(180, y + 17, name, anchor="middle", weight="bold", size=11)
        s += text(180, y + 32, sub, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    for y in [130, 240, 330]:
        s += arrow(180, y, 180, y + 10)
    # Right: slow methylation arm
    s += text(520, 60, "Slow memory arm  (~4 s)", anchor="middle", weight="bold", size=12)
    slow_steps = [
        (90, "CheR methylase", "adds methyl groups"),
        (200, "MCP receptor", "(activity ↑)"),
        (290, "CheB demethylase", "removes methyls"),
        (380, "MCP receptor", "(activity ↓ to baseline)"),
    ]
    for y, name, sub in slow_steps:
        s += box(400, y, 240, 40)
        s += text(520, y + 17, name, anchor="middle", weight="bold", size=11)
        s += text(520, y + 32, sub, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    for y in [130, 240, 330]:
        s += arrow(520, y, 520, y + 10)
    # Bridge note
    return s + svg_close()


def f06_temporal_weighting():
    s = svg_open(700, 360)
    s += title("E. coli temporal weighting — the cell computes a difference, not a level", 350, 22)
    # Bar chart
    ax = 90
    ay = 250
    aw = 520
    # axes
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID, sw=1)
    s += line(ax, 70, ax, ay + 20, stroke=GRAY_MID, sw=1)
    # x ticks for time -4..0
    for i, t in enumerate([-4, -3, -2, -1, 0]):
        x = ax + i * (aw / 4)
        s += line(x, ay, x, ay + 4, stroke=GRAY_MID)
        s += text(x, ay + 18, f"{t} s", anchor="middle", size=10, fill=GRAY_DARK)
    s += text(350, ay + 38, "time before measurement (s)", anchor="middle", size=11, weight="bold")
    s += text(40, 165, "weighting", anchor="middle", italic=True, size=11, weight="bold")
    s += text(40, 180, "coefficient", anchor="middle", italic=True, size=11, weight="bold")
    # y axis
    for v, lbl in [(80, "+1"), (165, "0"), (240, "−1")]:
        s += line(ax - 4, v, ax, v, stroke=GRAY_MID)
        s += text(ax - 8, v + 4, lbl, anchor="end", size=10, fill=GRAY_DARK)
    s += line(ax, 165, ax + aw, 165, stroke=GRAY_LIGHT, sw=0.6, dash="2,3")
    # Bars: heights for -4..-1 negative, 0 positive
    bar_w = 80
    # most recent second (t=0) positive
    s += box(ax + 4 * (aw / 4) - bar_w / 2, 80, bar_w, 85, fill=INK, stroke=INK)
    # prior 3 seconds negative
    for i in range(1, 4):
        x = ax + (4 - i) * (aw / 4) - bar_w / 2
        h = [40, 50, 30][i - 1]
        s += box(x, 165, bar_w, h, fill=GRAY_DARK, stroke=INK)
    s += text(ax + 4 * (aw / 4), 70, "+1.0", anchor="middle", size=10, weight="bold")
    s += text(350, 320, "The flagellar motor is gated by  (recent concentration) − (concentration ~3 s ago).",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f07_flytrap_integrator():
    s = svg_open(700, 360)
    s += title("Venus flytrap — leaky calcium integrator counts trigger touches", 350, 22)
    ax = 90
    ay = 290
    aw = 520
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID, sw=1)
    s += line(ax, 70, ax, ay + 10, stroke=GRAY_MID, sw=1)
    s += text(40, 180, "[Ca²⁺]ᵢ", anchor="middle", italic=True, size=11, weight="bold")
    s += text(350, 320, "First touch triggers a Ca²⁺ spike that decays. Second touch within ~20 s adds to the residual — and crosses threshold.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, ay + 30, "time (s)", anchor="middle", weight="bold", size=11)
    # Threshold line
    th_y = 110
    s += line(ax, th_y, ax + aw, th_y, stroke=INK, sw=0.8, dash="4,3")
    s += text(ax + aw + 4, th_y + 4, "threshold", size=9, italic=True, fill=INK)
    # Trace
    # First spike at t=2s
    s += path(f"M {ax} {ay} L {ax+50} {ay} L {ax+60} 200 Q {ax+90} 280, {ax+150} {ay-30}", stroke=INK, sw=2)
    # Decay continues but second spike at ~t=15s
    s += path(f"M {ax+150} {ay-30} Q {ax+200} {ay-15}, {ax+260} {ay-22}", stroke=INK, sw=2)
    # Second spike adds — crosses threshold
    s += path(f"M {ax+260} {ay-22} L {ax+270} 100 Q {ax+310} 250, {ax+360} {ay-10}", stroke=INK, sw=2)
    s += path(f"M {ax+360} {ay-10} Q {ax+450} {ay-3}, {ax+520} {ay-1}", stroke=INK, sw=2)
    # Trigger marks on x axis
    for tx, lbl in [(ax + 55, "touch 1"), (ax + 265, "touch 2")]:
        s += line(tx, ay - 4, tx, ay + 8, stroke=INK, sw=1.5)
        s += text(tx, ay + 22, lbl, anchor="middle", size=9, weight="bold")
    return s + svg_close()


def f08_radial_vs_bilateral():
    s = svg_open(700, 360)
    s += title("Radial vs. bilateral symmetry — geometry constrains the decision", 350, 22)
    # Hydra (radial)
    s += text(180, 60, "Radial symmetry  (hydra)", anchor="middle", weight="bold", size=12)
    s += circle(180, 175, 50, fill=CREAM)
    # Tentacles
    for k in range(8):
        a = 2 * math.pi * k / 8
        x2 = 180 + 90 * math.cos(a)
        y2 = 175 + 90 * math.sin(a)
        s += line(180 + 50 * math.cos(a), 175 + 50 * math.sin(a), x2, y2, stroke=INK, sw=1.2)
        # Sensors
        s += circle(x2, y2, 4, fill=INK)
    s += text(180, 280, "sensors distributed around perimeter", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(180, 296, "decision: any direction (360°)", anchor="middle", size=10, fill=GRAY_DARK)
    # C. elegans (bilateral)
    s += text(520, 60, "Bilateral symmetry  (C. elegans)", anchor="middle", weight="bold", size=12)
    # Worm body
    s += path(f"M {520-100} 175 Q {520-50} 155, 520 175 Q {520+50} 195, {520+100} 175",
              fill=CREAM, stroke=INK, sw=1)
    s += path(f"M {520-100} 175 Q {520-50} 195, 520 175 Q {520+50} 155, {520+100} 175",
              fill=CREAM, stroke=INK, sw=1)
    # Head sensors clustered at left (anterior)
    head_x = 420
    for cy_, label in [(165, "AWA"), (175, "ASH"), (185, "AFD"), (180, "ASE")]:
        s += circle(head_x + 5, cy_, 3, fill=INK)
    s += text(head_x - 15, 145, "Sensors clustered", italic=True, size=10, weight="bold")
    s += text(head_x - 15, 158, "at head end →", italic=True, size=10)
    # Direction of motion arrow
    s += arrow(530, 220, 600, 220, sw=2)
    s += text(565, 240, "forward", anchor="middle", italic=True, size=10)
    s += text(520, 280, "decision: continue forward, or turn?", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(520, 296, "binary choice (with random pirouette)", anchor="middle", size=10, fill=GRAY_DARK)
    return s + svg_close()


def f09_run_pirouette():
    s = svg_open(700, 360)
    s += title("C. elegans run-and-pirouette navigation up a chemical gradient", 350, 22)
    # Chemical gradient (faded background — but we're monochrome)
    # Show source
    src_x, src_y = 600, 150
    s += circle(src_x, src_y, 12, fill=INK, stroke=INK)
    s += text(src_x, src_y - 20, "attractant source", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Gradient rings
    for r in (60, 100, 140, 180):
        s += circle(src_x, src_y, r, fill="none", stroke=GRAY_LIGHT, sw=0.6, dash="3,3")
    # Worm trajectory: runs interrupted by pirouettes
    pts = [(80, 220), (130, 195), (180, 200), (190, 200),
           (235, 175), (280, 185), (290, 185),
           (340, 160), (390, 175), (400, 175),
           (445, 150), (490, 165), (500, 165),
           (545, 145), (590, 150)]
    pirouette_idx = [3, 6, 9, 12]
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        if i in pirouette_idx:
            # tight coil
            s += path(f"M {x1} {y1} q 6 -8 12 0 q 6 8 0 12 q -10 4 -8 -8 q 4 -4 8 0 L {x2} {y2}",
                      stroke=INK, sw=1.5)
        else:
            s += arrow(x1, y1, x2, y2, sw=1)
    # dC/dt labels
    label_segs = [(80, 220, 130, 195, "+ dC/dt"), (180, 200, 235, 175, "+ dC/dt"), (235, 175, 280, 185, "− dC/dt → pirouette")]
    for x1, y1, x2, y2, lbl in label_segs:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 10
        s += text(mx, my, lbl, anchor="middle", size=9, fill=GRAY_DARK, italic=True)
    s += text(350, 320, "Each pirouette resets heading. Positive dC/dt suppresses pirouettes; negative dC/dt triggers them.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f10_synaptic_vs_neuromodulatory():
    s = svg_open(700, 360)
    s += title("Fast synaptic transmission vs. neuromodulatory broadcast", 350, 22)
    # Left: synaptic
    s += text(180, 60, "Fast synaptic", anchor="middle", weight="bold", size=12)
    # Source neuron
    s += circle(80, 180, 18, fill=GRAY_LIGHT, stroke=INK)
    s += text(80, 184, "src", anchor="middle", size=10, weight="bold")
    # Wire to target
    s += line(98, 180, 280, 180, stroke=INK, sw=2)
    s += text(190, 170, "labeled wire", anchor="middle", italic=True, size=10)
    # Target neuron
    s += circle(298, 180, 18, fill=GRAY_LIGHT, stroke=INK)
    s += text(298, 184, "tgt", anchor="middle", size=10, weight="bold")
    s += text(180, 250, "one signal → one specific target", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(180, 268, "the specificity is the message", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Right: neuromodulatory
    s += text(520, 60, "Neuromodulatory broadcast", anchor="middle", weight="bold", size=12)
    # Source
    s += circle(420, 180, 18, fill=GRAY_LIGHT, stroke=INK)
    s += text(420, 184, "src", anchor="middle", size=10, weight="bold")
    # Diffusion field
    for r in (40, 70, 100, 130):
        s += circle(420, 180, r, stroke=GRAY_MID, sw=0.6, dash="3,3")
    # Multiple target neurons in field
    target_positions = [(540, 130), (590, 200), (560, 260), (470, 250), (510, 110)]
    for tx, ty in target_positions:
        s += circle(tx, ty, 12, fill=CREAM, stroke=INK)
        # gain change icon (small ↑ next to)
        s += text(tx + 17, ty + 4, "g↕", size=9, weight="bold", fill=GRAY_DARK)
    s += text(520, 320, "one molecule → many neurons, each receptor-specific gain change", anchor="middle",
              italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f11_six_component_stack():
    s = svg_open(700, 480)
    s += title("Steering — six-component architecture as a causal stack", 350, 22)
    layers = [
        (60, "1. Bilateral body plan", "constrains decision to forward / turn"),
        (115, "2. Labeled-line sensors", "each input carries its valence structurally"),
        (170, "3. Integration  (AIY)", "weights inputs, computes decision"),
        (225, "4. Temporal comparison", "drives the pirouette rule (dC/dt)"),
        (280, "5. Mutual inhibition", "enforces coherent motor output"),
        (335, "6. Associative plasticity", "weights update with experience"),
    ]
    for y, name, sub in layers:
        s += box(140, y, 420, 38, fill=CREAM)
        s += text(150, y + 17, name, weight="bold", size=11)
        s += text(150, y + 32, sub, italic=True, size=10, fill=GRAY_DARK)
    # Arrows down between layers
    for y in [100, 155, 210, 265, 320]:
        s += arrow(350, y, 350, y + 14)
    # Wraparound: neuromodulatory state
    s += path("M 50 70 Q 50 220, 50 380 Q 50 410, 580 410 Q 620 410, 620 240 Q 620 60, 350 60", stroke=INK, sw=1.2, dash="6,4")
    s += text(610, 240, "Neuromodulatory state", anchor="end", italic=True, size=11, weight="bold")
    s += text(610, 256, "(fed/starved, etc.) wraps", anchor="end", italic=True, size=10, fill=GRAY_DARK)
    s += text(610, 270, "the entire stack as context", anchor="end", italic=True, size=10, fill=GRAY_DARK)
    # Plasticity feedback
    s += path("M 350 380 Q 90 380, 90 130", stroke=INK, sw=1.2, dash="6,4")
    s += arrow(91, 132, 91, 119, sw=1.2)
    s += text(110, 420, "associative plasticity feeds back to update the labeled-line weights",
              italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f12_learning_ladder():
    s = svg_open(700, 420)
    s += title("Three forms of learning, in evolutionary order", 350, 22)
    rungs = [
        (340, "Habituation", "decreased response to repeated stimulus", "neurons not required (slime mold)", "Physarum, C. elegans, Mimosa"),
        (240, "Sensitization", "increased response after a single salient event", "single modulatory neuron sufficient", "Aplysia (Kandel)"),
        (140, "Associative learning", "form predictive link between stimuli", "minimum: pre/post co-activation + a teaching signal", "Aplysia, Drosophila, Nematostella (2023)"),
    ]
    for y, name, defn, substrate, exemplar in rungs:
        s += box(80, y, 540, 70, fill=CREAM)
        s += text(110, y + 18, name, weight="bold", size=12)
        s += text(110, y + 34, defn, italic=True, size=10, fill=GRAY_DARK)
        s += text(110, y + 50, "substrate: " + substrate, size=10)
        s += text(110, y + 65, "exemplar: " + exemplar, size=10, fill=GRAY_DARK)
    # Up arrow on the side
    s += arrow(50, 360, 50, 160, sw=2)
    s += text(40, 240, "increasing evolutionary complexity", anchor="middle", italic=True, size=10,
              weight="bold")
    s += text(35, 250, "(rotated)", anchor="middle", size=8, fill=GRAY_LIGHT)
    s += text(350, 395, "Boundary moved in 2023 — Nematostella (sea anemone, no central brain) shows associative conditioning.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f13_aplysia_circuit():
    s = svg_open(700, 360)
    s += title("Aplysia gill-withdrawal — sensitization circuit", 350, 22)
    # Sensory neurons + interneuron + motor neuron + gill
    # Layout:
    # Siphon SN (left) -> motor neuron -> gill
    # Tail SN -> serotonergic interneuron -> synapses onto siphon SN terminal
    s += circle(120, 200, 22, fill=CREAM, stroke=INK)
    s += text(120, 196, "Siphon", anchor="middle", weight="bold", size=10)
    s += text(120, 210, "SN", anchor="middle", size=10)
    s += arrow(142, 200, 290, 200)
    s += text(216, 188, "glutamate", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Motor neuron
    s += circle(310, 200, 22, fill=CREAM, stroke=INK)
    s += text(310, 196, "Motor", anchor="middle", weight="bold", size=10)
    s += text(310, 210, "neuron", anchor="middle", size=10)
    s += arrow(332, 200, 480, 200)
    # Gill
    s += box(490, 175, 90, 50, fill=GRAY_LIGHT)
    s += text(535, 195, "Gill", anchor="middle", weight="bold", size=11)
    s += text(535, 210, "(withdraw)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Tail SN
    s += circle(120, 90, 22, fill=CREAM, stroke=INK)
    s += text(120, 86, "Tail", anchor="middle", weight="bold", size=10)
    s += text(120, 100, "SN", anchor="middle", size=10)
    s += arrow(142, 90, 240, 90)
    # Serotonergic interneuron
    s += circle(265, 90, 22, fill=GRAY_LIGHT, stroke=INK)
    s += text(265, 86, "5-HT", anchor="middle", weight="bold", size=10)
    s += text(265, 100, "IN", anchor="middle", size=10)
    # Synapse onto siphon SN terminal (presynaptic facilitation)
    s += path(f"M 265 112 Q 220 150, 175 195", stroke=INK, sw=1.5)
    s += arrow(178, 196, 165, 196, sw=1.2)
    s += text(195, 145, "serotonin", italic=True, size=10, fill=GRAY_DARK, weight="bold")
    s += text(195, 158, "(modulates SN→motor synapse)", italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 320, "Tail shock recruits 5-HT IN, which strengthens the existing siphon→motor pathway from the side.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f14_short_vs_long_term():
    s = svg_open(700, 360)
    s += title("Short-term vs. long-term sensitization in Aplysia", 350, 22)
    # Two panels
    for px, head, scope in [(180, "Short-term  (minutes–hours)", "no new protein synthesis"),
                            (520, "Long-term  (days–weeks)", "CREB-1 → new synaptic growth")]:
        s += text(px, 60, head, anchor="middle", weight="bold", size=12)
        s += text(px, 76, scope, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Left panel: cAMP-PKA-K+ at membrane, no nucleus
    # Cell membrane (curve at top)
    s += path("M 80 130 Q 180 110, 280 130", stroke=INK, sw=1.5)
    s += text(180, 145, "membrane", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Components
    for cy_, lbl in [(160, "5-HT receptor"), (190, "cAMP ↑"), (220, "PKA active"), (250, "K⁺ channel closed")]:
        s += text(180, cy_, lbl, anchor="middle", size=10)
    s += arrow(180, 165, 180, 175); s += arrow(180, 195, 180, 205); s += arrow(180, 225, 180, 235)
    s += text(180, 285, "transient: synaptic terminal", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(180, 298, "stays sensitized while PKA active", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Right panel: cascade extends into nucleus
    s += path("M 420 130 Q 520 110, 620 130", stroke=INK, sw=1.5)
    s += text(520, 145, "membrane", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    for cy_, lbl in [(160, "5-HT receptor"), (180, "cAMP ↑"), (200, "PKA → nucleus")]:
        s += text(520, cy_, lbl, anchor="middle", size=10)
    s += arrow(520, 165, 520, 175); s += arrow(520, 185, 520, 195)
    # Nucleus
    s += ellipse(520, 245, 90, 35, fill=CREAM, stroke=INK)
    s += text(520, 230, "nucleus", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(520, 248, "CREB-2 displaced", anchor="middle", size=10)
    s += text(520, 263, "CREB-1 binds DNA", anchor="middle", weight="bold", size=10)
    s += arrow(520, 280, 520, 295)
    s += text(520, 308, "new synaptic terminals grow", anchor="middle", italic=True, size=10, fill=INK, weight="bold")
    s += text(520, 322, "(persistent, structural change)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f15_rescorla_wagner():
    s = svg_open(700, 360)
    s += title("Rescorla–Wagner — learning tracks the residual prediction error", 350, 22)
    # Three panels stacked horizontally, each a small line plot
    titles = [
        "Phase 1: A → reward",
        "Phase 2: A+B → reward (B blocked)",
        "Phase 3: B alone → reward",
    ]
    for i, ttl in enumerate(titles):
        x0 = 30 + i * 220
        s += text(x0 + 100, 60, ttl, anchor="middle", weight="bold", size=11)
        # Axes
        ax = x0 + 30
        ay = 250
        aw = 160
        ah = 150
        s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
        s += line(ax, 90, ax, ay, stroke=GRAY_MID)
        s += text(ax + aw / 2, ay + 18, "trials →", anchor="middle", size=9, fill=GRAY_DARK)
        s += text(ax - 8, 92, "V", anchor="end", size=10, italic=True)
        s += text(ax - 8, ay + 4, "0", anchor="end", size=10)
        # asymptote line
        s += line(ax, 100, ax + aw, 100, stroke=GRAY_LIGHT, sw=0.6, dash="3,3")
        s += text(ax + aw + 4, 102, "λ", italic=True, size=9, fill=GRAY_DARK)
        if i == 0:
            # V_A rises
            s += path(f"M {ax} {ay} Q {ax+50} {ay-90}, {ax+aw} 105", stroke=INK, sw=1.8)
            s += text(ax + aw / 2, 130, "V_A → λ", anchor="middle", weight="bold", size=10)
        elif i == 1:
            # V_A flat at lambda; V_B flat at 0 (blocked)
            s += line(ax, 100, ax + aw, 100, stroke=INK, sw=1.8)
            s += text(ax + aw / 2, 95, "V_A", anchor="middle", weight="bold", size=10)
            s += line(ax, ay, ax + aw, ay - 5, stroke=INK, sw=1.8, dash="4,3")
            s += text(ax + aw / 2, ay - 16, "V_B (blocked)", anchor="middle", italic=True, size=10)
        else:
            # V_B rises
            s += path(f"M {ax} {ay} Q {ax+50} {ay-90}, {ax+aw} 105", stroke=INK, sw=1.8)
            s += text(ax + aw / 2, 130, "V_B → λ", anchor="middle", weight="bold", size=10)
    s += text(350, 330, "When λ − ΣV ≈ 0 (phase 2), there is no error to drive new learning. B's failure to gain value is the diagnostic.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f16_per_rate():
    s = svg_open(700, 360)
    s += title("Bateson 2011 — proboscis-extension rate across CS+/CS− continuum", 350, 22)
    ax = 90
    ay = 280
    aw = 540
    ah = 200
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
    s += line(ax, 80, ax, ay, stroke=GRAY_MID)
    # x-axis: 5 positions
    pos_labels = ["CS−", "ambig.−", "midpoint", "ambig.+", "CS+"]
    for i, lbl in enumerate(pos_labels):
        x = ax + (i / 4) * aw
        s += line(x, ay, x, ay + 4, stroke=GRAY_MID)
        s += text(x, ay + 18, lbl, anchor="middle", size=9, fill=GRAY_DARK)
    s += text(350, ay + 38, "Test odor position", anchor="middle", size=11, weight="bold")
    # y axis
    for v, lbl in [(80, "100"), (160, "50"), (ay, "0")]:
        s += line(ax - 4, v, ax, v, stroke=GRAY_MID)
        s += text(ax - 8, v + 4, lbl, anchor="end", size=10, fill=GRAY_DARK)
    s += text(35, 180, "PER (%)", anchor="middle", italic=True, weight="bold")
    # Lines
    # Unshaken (control): rises sharply
    pts_un = [(0, 8), (0.25, 22), (0.5, 50), (0.75, 80), (1.0, 92)]
    pts_sh = [(0, 5), (0.25, 12), (0.5, 28), (0.75, 56), (1.0, 88)]
    def to_xy(pp, hpct):
        x = ax + pp * aw
        y = ay - (hpct / 100) * (ay - 80)
        return x, y
    for i, pts in enumerate([pts_un, pts_sh]):
        d = "M "
        for j, (pp, h) in enumerate(pts):
            x, y = to_xy(pp, h)
            if j == 0:
                d += f"{x} {y} "
            else:
                d += f"L {x} {y} "
            s += circle(x, y, 4, fill=(WHITE if i == 0 else INK), stroke=INK, sw=1)
        s += path(d, stroke=INK, sw=(2 if i == 1 else 1.5), dash=("4,3" if i == 0 else None))
    # Legend
    s += text(ax + aw - 20, 100, "○ Unshaken (control)", anchor="end", size=10)
    s += text(ax + aw - 20, 116, "● Shaken (60 s)", anchor="end", size=10)
    s += text(350, 330, "Pessimistic shift biggest at the ambiguous midpoint and ambiguous-negative — not a uniform suppression.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f17_cognitive_bias_paradigm():
    s = svg_open(700, 360)
    s += title("The cognitive-bias paradigm — training and test", 350, 22)
    # Training panel
    s += text(180, 60, "Training", anchor="middle", weight="bold", size=12)
    s += box(60, 80, 240, 80)
    s += text(180, 100, "CS+ (e.g. lemon odor)", anchor="middle", size=10)
    s += arrow(245, 100, 270, 100)
    s += text(280, 104, "→ reward", size=10)
    s += text(180, 130, "CS− (e.g. pineapple odor)", anchor="middle", size=10)
    s += arrow(245, 130, 270, 130)
    s += text(280, 134, "→ aversive", size=10)
    s += text(180, 175, "Animal learns the contingency.", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Test panel
    s += text(520, 60, "Test", anchor="middle", weight="bold", size=12)
    s += box(400, 80, 240, 80)
    s += text(520, 110, "Ambiguous stimulus", anchor="middle", weight="bold", size=11)
    s += text(520, 128, "(midpoint between CS+ and CS−)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Two outcome arrows
    s += arrow(520, 165, 460, 220, sw=1.5)
    s += box(390, 220, 150, 50, fill=CREAM)
    s += text(465, 240, "Negatively biased", anchor="middle", weight="bold", size=10)
    s += text(465, 255, "interprets as CS−", anchor="middle", italic=True, size=10)
    s += text(465, 268, "(slow approach, withdrawal)", anchor="middle", size=9, fill=GRAY_DARK)
    s += arrow(520, 165, 580, 220, sw=1.5)
    s += box(510, 220, 150, 50, fill=CREAM)
    s += text(585, 240, "Positively biased", anchor="middle", weight="bold", size=10)
    s += text(585, 255, "interprets as CS+", anchor="middle", italic=True, size=10)
    s += text(585, 268, "(fast approach)", anchor="middle", size=9, fill=GRAY_DARK)
    s += text(350, 310, "The paradigm requires a trained discrimination plus a deliberately ambiguous probe stimulus.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f18_approach_latency():
    s = svg_open(700, 360)
    s += title("Perry 2016 — approach latency to ambiguous cylinder, three groups", 350, 22)
    ax = 100
    ay = 290
    aw = 480
    ah = 200
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
    s += line(ax, 80, ax, ay, stroke=GRAY_MID)
    # y axis labels
    for v, lbl in [(80, "60"), (165, "30"), (ay, "0")]:
        s += line(ax - 4, v, ax, v, stroke=GRAY_MID)
        s += text(ax - 10, v + 4, lbl, anchor="end", size=10, fill=GRAY_DARK)
    s += text(45, 180, "Latency", anchor="middle", italic=True, weight="bold", size=11)
    s += text(45, 195, "(s)", anchor="middle", italic=True, size=10)
    # 3 bars
    bars = [
        (140, 120, "Control\n(water)"),
        (300, 200, "Sucrose\nsurprise"),
        (460, 110, "Sucrose +\nfluphenazine"),
    ]
    bw = 80
    for cx, h, lbl in bars:
        bar_h = (h / 60) * (ay - 80)
        bar_y = ay - bar_h
        if "Sucrose\nsurprise" in lbl:
            fill = INK
        else:
            fill = GRAY_LIGHT
        s += box(cx - bw / 2, bar_y, bw, bar_h, fill=fill, stroke=INK)
        s += text(cx, bar_y - 6, str(int(60 - (h/60)*30)) + " s", anchor="middle", size=10, weight="bold")
        # Multi-line label
        for i, ln in enumerate(lbl.split("\n")):
            s += text(cx, ay + 18 + i * 14, ln, anchor="middle", size=10, fill=GRAY_DARK)
    s += text(350, 330, "Dopamine antagonist abolishes the sucrose-surprise effect — the bias is dopamine-mediated, not water-deprivation.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f19_discrim_general_2d():
    s = svg_open(700, 360)
    s += title("Discrimination–generalization tension in representational space", 350, 22)
    # Two clusters of points
    random.seed(7)
    cx_a, cy_a = 240, 180
    cx_b, cy_b = 460, 180
    for _ in range(35):
        rx = cx_a + random.gauss(0, 35)
        ry = cy_a + random.gauss(0, 35)
        s += circle(rx, ry, 3, fill=INK, stroke=INK)
    for _ in range(35):
        rx = cx_b + random.gauss(0, 35)
        ry = cy_b + random.gauss(0, 35)
        s += circle(rx, ry, 3, fill=GRAY_DARK, stroke=GRAY_DARK)
    # Cluster boundaries
    s += circle(cx_a, cy_a, 70, stroke=INK, sw=1.2, dash="5,3")
    s += circle(cx_b, cy_b, 70, stroke=INK, sw=1.2, dash="5,3")
    # Arrows: intra-spread (generalization) and inter-gap (discrimination)
    s += text(cx_a, cy_a - 95, "Category A", anchor="middle", weight="bold", size=12)
    s += text(cx_b, cy_b - 95, "Category B", anchor="middle", weight="bold", size=12)
    # Intra arrows (collapse — generalization)
    s += arrow(cx_a - 50, cy_a + 50, cx_a - 10, cy_a + 10, sw=1)
    s += arrow(cx_a + 50, cy_a + 50, cx_a + 10, cy_a + 10, sw=1)
    s += text(cx_a, cy_a + 75, "generalization →", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(cx_a, cy_a + 90, "collapse intra-spread", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Inter arrow (preserve gap — discrimination)
    s += arrow(cx_a + 75, cy_a, cx_b - 75, cy_b, sw=2)
    s += arrow(cx_b - 75, cy_b, cx_a + 75, cy_a, sw=2)
    s += text((cx_a + cx_b) / 2, cy_a - 6, "← discrimination →", anchor="middle", italic=True, size=10, weight="bold")
    s += text((cx_a + cx_b) / 2, cy_a + 12, "preserve inter-gap", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 320, "Solving both at once requires different operations: dimensionality expansion + sparse coding (gap),",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 336, "and recurrent completion (collapse) — the three operations of Chapter 6.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f20_phylo_pallium():
    s = svg_open(700, 360)
    s += title("Three-layer pallial blueprint across vertebrate phylogeny", 350, 22)
    # Tree from common ancestor branching out
    # nodes at different x
    nodes = [
        (90, 200, "common\nancestor", True),
        (210, 110, "lamprey", True),
        (320, 90,  "fish", True),
        (430, 80,  "reptile", True),
        (540, 70,  "mammal", True),
        (640, 80,  "bird", True),
    ]
    for x, y, name, _ in nodes:
        # Highlight: three-layer pallium (marker)
        s += box(x - 28, y - 14, 56, 28, fill=GRAY_LIGHT, stroke=INK)
        for ln, off in zip(name.split("\n"), [-2, 12]):
            s += text(x, y + off, ln, anchor="middle", weight="bold", size=10)
        s += text(x, y - 22, "[3-layer ✓]", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Edges
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5)]
    for a, b in edges:
        x1, y1, _, _ = nodes[a]
        x2, y2, _, _ = nodes[b]
        s += line(x1 + 28, y1, x2 - 28, y2, stroke=INK, sw=1)
    # Pallium components box
    s += box(70, 250, 560, 70, fill=CREAM)
    s += text(350, 268, "Three-layer pallial blueprint (preserved at every node):",
              anchor="middle", weight="bold", size=11)
    s += text(350, 284, "1. Excitatory projection layer    2. Inhibitory interneurons    3. Recurrent collaterals",
              anchor="middle", size=10)
    s += text(350, 304, "Cortex is not a mammalian invention. The blueprint is older than vertebrates' diversification.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f21_odor_completion():
    s = svg_open(700, 360)
    s += title("Pattern completion in piriform cortex — Odor A", 350, 22)
    # Two panels
    for px, head, sub, n_active in [(180, "Full odor A", "40 / 1000 neurons active", 40),
                                     (520, "Dilute odor A", "25 directly + 15 by completion", 40)]:
        s += text(px, 60, head, anchor="middle", weight="bold", size=12)
        s += text(px, 76, sub, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
        # 10x10 grid of neurons
        gx0 = px - 80
        gy0 = 95
        random.seed(11)
        cells = [(gx0 + i * 18, gy0 + j * 18) for i in range(10) for j in range(10)]
        # Pattern: active set is the same in both panels (40 cells)
        active_idx = sorted(random.sample(range(100), 40))
        if px == 180:
            # Full pattern — all 40 active, recurrent connections shown
            for i, (cx_, cy_) in enumerate(cells):
                if i in active_idx:
                    s += circle(cx_, cy_, 4, fill=INK, stroke=INK)
                else:
                    s += circle(cx_, cy_, 3, fill="none", stroke=GRAY_LIGHT, sw=0.5)
            # Some recurrent connections among active cells
            for k in range(0, 30, 5):
                if k + 1 < 40:
                    a = cells[active_idx[k]]
                    b = cells[active_idx[k + 1]]
                    s += line(a[0], a[1], b[0], b[1], stroke=INK, sw=0.5, dash="2,2")
        else:
            # Dilute: 25 directly active + 15 completed
            direct_active = active_idx[:25]
            completed = active_idx[25:40]
            for i, (cx_, cy_) in enumerate(cells):
                if i in direct_active:
                    s += circle(cx_, cy_, 4, fill=INK, stroke=INK)
                elif i in completed:
                    s += circle(cx_, cy_, 4, fill=GRAY_LIGHT, stroke=INK, sw=0.8)
                else:
                    s += circle(cx_, cy_, 3, fill="none", stroke=GRAY_LIGHT, sw=0.5)
            # Arrow from a few direct to completed
            for k in range(3):
                a = cells[direct_active[k * 5]]
                b = cells[completed[k * 5]]
                s += arrow(a[0], a[1], b[0], b[1], sw=0.6, stroke=GRAY_DARK)
        # Legend
    s += text(350, 320, "Recurrent collaterals fill in the missing cells. Downstream regions can't tell the dilute pattern from the full one.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f22_goldfish_rotation():
    s = svg_open(700, 360)
    s += title("Goldfish recognition across rotations — DeLong et al.", 350, 22)
    ax = 90
    ay = 260
    aw = 540
    ah = 180
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
    s += line(ax, 80, ax, ay, stroke=GRAY_MID)
    rotations = [(0, 92), (90, 75), (180, 60), (270, 78)]
    bw = 100
    for i, (deg, acc) in enumerate(rotations):
        cx = ax + 50 + i * 130
        h = (acc / 100) * (ay - 80)
        y_ = ay - h
        s += box(cx - bw / 2, y_, bw, h, fill=(INK if deg == 0 else GRAY_LIGHT), stroke=INK)
        s += text(cx, y_ - 6, f"{acc}%", anchor="middle", weight="bold", size=10)
        s += text(cx, ay + 18, f"{deg}°", anchor="middle", weight="bold", size=11)
    s += text(35, 180, "Accuracy", anchor="middle", italic=True, weight="bold")
    s += text(35, 195, "(%)", anchor="middle", italic=True, size=10)
    s += text(350, ay + 40, "rotation from training orientation", anchor="middle", weight="bold", size=11)
    s += text(350, 320, "Drop is asymmetric — not a smooth function of angle. The goldfish has invariance, but limited.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 336, "Compare archerfish: 81% on a 44-face recognition task (Newport et al.).",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f23_saltpan_path():
    s = svg_open(700, 360)
    s += title("Cataglyphis path integration — outward zigzag, homeward straight", 350, 22)
    # Saltpan is a flat plane
    s += box(50, 60, 600, 240, fill=CREAM)
    # Nest at upper-left, food at lower-right
    nest = (110, 130)
    food = (550, 240)
    s += circle(nest[0], nest[1], 6, fill=INK, stroke=INK)
    s += text(nest[0] + 12, nest[1] - 6, "nest", italic=True, size=10, weight="bold")
    s += circle(food[0], food[1], 6, fill=INK, stroke=INK)
    s += text(food[0] - 24, food[1] + 18, "food", italic=True, size=10, weight="bold")
    # Outward zigzag
    out_pts = [nest, (160, 100), (220, 150), (280, 110), (330, 175), (380, 130), (440, 200), (480, 170), (520, 220), food]
    d = f"M {out_pts[0][0]} {out_pts[0][1]}"
    for x, y in out_pts[1:]:
        d += f" L {x} {y}"
    s += path(d, stroke=GRAY_DARK, sw=1.5)
    s += text(330, 80, "outward (foraging zigzag)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Homeward straight
    s += line(food[0], food[1], nest[0], nest[1], stroke=INK, sw=2.5)
    s += text(330, 200, "homeward (vector)", anchor="middle", italic=True, size=10, weight="bold")
    # Displacement experiment dotted continuation
    disp_start = (380, 160)
    disp_end = (350, 100)  # where the displaced ant would end up
    s += line(380, 130, 350, 100, stroke=GRAY_LIGHT, sw=0.8, dash="3,3")
    s += circle(350, 100, 5, fill="none", stroke=INK, sw=1)
    s += text(330, 95, "termination after displacement", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 330, "Displaced ants walk the home vector from the displacement point — they do not correct.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f24_place_grid_hd_cells():
    s = svg_open(700, 360)
    s += title("Hippocampal–entorhinal coordinate system", 350, 22)
    panels = [
        (130, "Place cells", "place"),
        (380, "Grid cells", "grid"),
        (610, "Head-direction", "hd"),
    ]
    for cx, head, kind in panels:
        s += text(cx, 60, head, anchor="middle", weight="bold", size=12)
        # Arena box
        if kind != "hd":
            s += box(cx - 80, 80, 160, 160)
        if kind == "place":
            # 4 distinct place fields
            fields = [(cx - 40, 110, 18, INK), (cx + 30, 130, 22, GRAY_DARK), (cx - 20, 200, 24, GRAY_MID), (cx + 50, 210, 18, INK)]
            for fx, fy, fr, c in fields:
                s += circle(fx, fy, fr, fill=c, stroke=c, dash=None)
            s += text(cx, 260, "each cell fires in one place", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
        elif kind == "grid":
            # Hexagonal lattice — three colors offset
            for fxx in range(0, 5):
                for fyy in range(0, 5):
                    base_x = cx - 70 + fxx * 35 + (fyy % 2) * 17
                    base_y = 95 + fyy * 30
                    if cx - 78 < base_x < cx + 78 and 82 < base_y < 240:
                        s += circle(base_x, base_y, 4, fill=INK, stroke=INK)
                        # Phase-offset 2nd cell
                        s += circle(base_x + 7, base_y + 4, 3, fill=GRAY_MID, stroke=GRAY_MID)
            s += text(cx, 260, "hexagonal lattice across space", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
        else:
            # Polar plot for head direction
            s += circle(cx, 160, 70, fill=CREAM, stroke=INK)
            # Ticks for cardinal directions
            for ang_deg, lbl in [(0, "0°"), (90, "90°"), (180, "180°"), (270, "270°")]:
                a = math.radians(ang_deg - 90)
                tx = cx + 78 * math.cos(a)
                ty = 160 + 78 * math.sin(a)
                s += text(tx, ty + 4, lbl, anchor="middle", size=9, fill=GRAY_DARK)
            # Firing rate as function of heading — peak at 45° let's say
            d = "M "
            for k in range(101):
                ang = math.radians(k / 100 * 360 - 90)
                preferred = math.radians(45 - 90)
                rate = 25 + 35 * max(0, math.cos(ang - preferred)) ** 2
                px_ = cx + rate * math.cos(ang)
                py_ = 160 + rate * math.sin(ang)
                d += f"{px_:.1f} {py_:.1f} "
                if k < 100:
                    d += "L "
            s += path(d, stroke=INK, sw=1.5, fill=GRAY_LIGHT)
            s += text(cx, 260, "fires when heading = preferred", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 320, "Together: where you are, the lattice you're in, and which way you face — three independent codes.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f25_fmri_routing():
    s = svg_open(700, 360)
    s += title("Hippocampal + PFC activity during self-routing vs. GPS following", 350, 22)
    # Two grouped bar charts
    for px, head, profile in [(180, "Self-planned routing", "scaling"), (520, "GPS instruction-following", "flat")]:
        s += text(px, 60, head, anchor="middle", weight="bold", size=12)
        ax = px - 100
        ay = 270
        aw = 200
        s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
        s += line(ax, 90, ax, ay, stroke=GRAY_MID)
        # X axis: junction complexity
        for i, lvl in enumerate(["2 routes", "4 routes", "6 routes"]):
            x = ax + 30 + i * 60
            s += text(x, ay + 18, lvl, anchor="middle", size=9, fill=GRAY_DARK)
        # bars: hippocampal (light) and PFC (ink) at each level
        if profile == "scaling":
            heights = [60, 100, 140]
        else:
            heights = [25, 28, 30]
        for i, h in enumerate(heights):
            x = ax + 30 + i * 60
            # hippocampal
            s += box(x - 16, ay - h, 14, h, fill=GRAY_LIGHT, stroke=INK, sw=0.7)
            # PFC
            s += box(x + 2, ay - (h * 0.8), 14, h * 0.8, fill=INK, stroke=INK)
        s += text(ax, 70, "BOLD activity", italic=True, size=10, fill=GRAY_DARK)
    # Legend
    s += box(280, 305, 14, 12, fill=GRAY_LIGHT, stroke=INK)
    s += text(298, 315, "hippocampus", size=9, fill=GRAY_DARK)
    s += box(370, 305, 14, 12, fill=INK)
    s += text(388, 315, "prefrontal cortex", size=9, fill=GRAY_DARK)
    s += text(350, 340, "GPS use suppresses route-complexity scaling — the system stops doing the work the route demanded.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f26_dopamine_three_panels():
    s = svg_open(700, 360)
    s += title("Schultz dopamine — the reward-prediction-error signature", 350, 22)
    panels = [
        (135, "Early training", "no cue burst, big reward burst", "early"),
        (350, "After learning", "cue burst, no reward burst", "after"),
        (565, "Reward omission", "cue burst, dip below baseline", "omission"),
    ]
    for cx, head, sub, kind in panels:
        s += text(cx, 60, head, anchor="middle", weight="bold", size=11)
        s += text(cx, 76, sub, anchor="middle", italic=True, size=9, fill=GRAY_DARK)
        ax = cx - 90
        ay = 280
        aw = 180
        ah = 160
        s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
        s += line(ax, 110, ax, ay, stroke=GRAY_MID)
        # Cue and reward marks
        cue_x = ax + 50
        rew_x = ax + 130
        s += line(cue_x, ay - 4, cue_x, ay + 8, stroke=INK)
        s += text(cue_x, ay + 22, "cue", anchor="middle", size=9, fill=GRAY_DARK)
        s += line(rew_x, ay - 4, rew_x, ay + 8, stroke=INK)
        s += text(rew_x, ay + 22, "reward", anchor="middle", size=9, fill=GRAY_DARK)
        # Trace
        if kind == "early":
            d = f"M {ax} {ay-30} L {cue_x} {ay-30} L {rew_x-2} {ay-30} L {rew_x-1} 130 L {rew_x+5} 130 L {rew_x+10} {ay-30} L {ax+aw} {ay-30}"
        elif kind == "after":
            d = f"M {ax} {ay-30} L {cue_x-2} {ay-30} L {cue_x-1} 130 L {cue_x+5} 130 L {cue_x+10} {ay-30} L {ax+aw} {ay-30}"
        else:  # omission
            d = f"M {ax} {ay-30} L {cue_x-2} {ay-30} L {cue_x-1} 130 L {cue_x+5} 130 L {cue_x+10} {ay-30} L {rew_x-2} {ay-30} L {rew_x-1} {ay+15} L {rew_x+5} {ay+15} L {rew_x+10} {ay-30} L {ax+aw} {ay-30}"
        s += path(d, stroke=INK, sw=1.5)
    s += text(350, 320, "δ_t = r_{t+1} + γV(s_{t+1}) − V(s_t).  The dopamine spike IS prediction error.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(50, 200, "DA rate", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f27_td_equation():
    s = svg_open(700, 360)
    s += title("Temporal-difference error — local computation across two time steps", 350, 22)
    # Equation centered
    s += text(350, 90, "δ_t  =  r_{t+1}  +  γV(s_{t+1})  −  V(s_t)",
              anchor="middle", weight="bold", size=18)
    # Annotations beneath each term
    annotations = [
        (215, "δ_t", "the prediction error\n(broadcast as dopamine)"),
        (290, "r_{t+1}", "actual reward\nreceived"),
        (370, "γV(s_{t+1})", "discounted estimate\nof what comes next"),
        (480, "V(s_t)", "current estimate\nbeing updated"),
    ]
    for cx, term, ann in annotations:
        s += line(cx, 100, cx, 130, stroke=INK, sw=0.8)
        for i, ln in enumerate(ann.split("\n")):
            s += text(cx, 145 + i * 14, ln, anchor="middle", size=10, fill=GRAY_DARK)
    # Timeline
    s += line(120, 240, 580, 240, stroke=INK, sw=1.5)
    for x, t in [(140, "t"), (350, "t+1"), (560, "t+2")]:
        s += line(x, 235, x, 245, stroke=INK)
        s += text(x, 260, t, anchor="middle", size=11, weight="bold")
    s += text(350, 290, "Update at time t uses information from t+1. Local — no need to remember long histories.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 308, "Computed in dopamine neurons; broadcast as a global plasticity gate to striatum.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f28_actor_critic():
    s = svg_open(700, 360)
    s += title("Actor–critic in the basal ganglia", 350, 22)
    # Cortex
    s += box(50, 80, 600, 40, fill=GRAY_LIGHT)
    s += text(350, 105, "Cortex  (state representation)", anchor="middle", weight="bold", size=11)
    # Two arrows down: to actor and critic
    s += arrow(220, 120, 220, 165)
    s += arrow(480, 120, 480, 165)
    # Actor
    s += box(120, 165, 200, 50, fill=CREAM)
    s += text(220, 185, "Actor", anchor="middle", weight="bold", size=12)
    s += text(220, 202, "dorsolateral striatum", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(220, 215, "(selects actions)", anchor="middle", size=9, fill=GRAY_DARK)
    # Critic
    s += box(380, 165, 200, 50, fill=CREAM)
    s += text(480, 185, "Critic", anchor="middle", weight="bold", size=12)
    s += text(480, 202, "striosomes / VTA inputs", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(480, 215, "(supplies V(s_t))", anchor="middle", size=9, fill=GRAY_DARK)
    # Critic to dopamine neurons
    s += arrow(480, 215, 480, 250)
    s += box(380, 250, 200, 40, fill=INK)
    s += text(480, 268, "Dopamine neurons", anchor="middle", weight="bold", size=11, fill=CREAM)
    s += text(480, 282, "compute δ_t", anchor="middle", italic=True, size=10, fill=CREAM)
    # Dopamine feedback to striatum
    s += path(f"M 380 270 Q 280 320, 220 215", stroke=INK, sw=2)
    s += arrow(222, 217, 220, 215, sw=2)
    s += text(280, 320, "δ_t  (plasticity gate)", anchor="middle", weight="bold", size=11, fill=INK)
    s += text(350, 350, "δ_t  trains both critic's V estimate AND actor's action selection — same signal, different uses.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f29_reward_spec_gap():
    s = svg_open(700, 420)
    s += title("The reward specification gap — proxy vs. underlying goal", 350, 22)
    # Two columns
    s += text(220, 60, "What was measured", anchor="middle", weight="bold", size=12)
    s += text(500, 60, "What was wanted", anchor="middle", weight="bold", size=12)
    rows = [
        (100, "Recommendation engine", "engagement time", "user well-being\n+ epistemic health"),
        (200, "HFT trading", "revenue per ms", "market stability"),
        (300, "Chip floorplan optimizer", "area + wire length", "full manufacturing\n+ maintenance cost"),
    ]
    for y, agent, proxy, goal in rows:
        s += text(60, y - 5, agent, weight="bold", size=11)
        s += box(160, y, 140, 60, fill=GRAY_LIGHT)
        for i, ln in enumerate(proxy.split("\n")):
            s += text(230, y + 24 + i * 14, ln, anchor="middle", size=10)
        # Gap arrow with growing divergence
        s += arrow(305, y + 30, 425, y + 30, sw=1.5)
        s += text(365, y + 22, "diverges", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
        s += box(430, y, 180, 60, fill=CREAM)
        for i, ln in enumerate(goal.split("\n")):
            s += text(520, y + 22 + i * 14, ln, anchor="middle", size=10)
    s += text(350, 390, "Goodhart's Law in action — when a measure becomes a target, the target stops being measured by it.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f30_replay():
    s = svg_open(700, 360)
    s += title("Hippocampal replay — forward (planning) and reverse (credit)", 350, 22)
    # Two panels
    for px, head, direction in [(180, "Forward replay  (at choice point)", "forward"),
                                 (520, "Reverse replay  (at reward)", "reverse")]:
        s += text(px, 60, head, anchor="middle", weight="bold", size=12)
        # Maze T-shape
        s += box(px - 110, 80, 220, 140, fill=CREAM)
        # Maze arms (T)
        s += line(px - 70, 200, px + 70, 200, stroke=INK, sw=2)  # bottom
        s += line(px, 100, px, 200, stroke=INK, sw=2)  # stem
        # Rat position
        if direction == "forward":
            rx, ry = px, 200
            s += circle(rx, ry, 6, fill=INK)
            s += text(rx, ry + 14, "rat (junction)", anchor="middle", size=9, fill=GRAY_DARK)
            # Forward sweep — left arm
            seq = [(px - 10, 200), (px - 30, 200), (px - 50, 200), (px - 70, 200)]
            for i, (cx_, cy_) in enumerate(seq):
                s += circle(cx_, cy_, 3, fill=INK if i == 0 else GRAY_LIGHT, stroke=INK, sw=0.5)
            s += arrow(px - 8, 195, px - 65, 195, sw=1, stroke=GRAY_DARK)
            s += text(px - 35, 185, "place-cell sequence", anchor="middle", size=9, italic=True, fill=GRAY_DARK)
        else:
            rx, ry = px - 70, 200
            s += circle(rx, ry, 6, fill=INK)
            s += text(rx, ry + 14, "rat (reward)", anchor="middle", size=9, fill=GRAY_DARK)
            # Reverse sweep
            seq = [(px - 50, 200), (px - 30, 200), (px - 10, 200), (px, 200), (px, 180), (px, 150), (px, 120)]
            for cx_, cy_ in seq:
                s += circle(cx_, cy_, 3, fill=GRAY_LIGHT, stroke=INK, sw=0.5)
            s += arrow(px - 65, 195, px + 5, 195, sw=1, stroke=GRAY_DARK)
            s += arrow(px + 5, 195, px + 5, 125, sw=1, stroke=GRAY_DARK)
            s += text(px - 30, 185, "reverse sequence", anchor="middle", size=9, italic=True, fill=GRAY_DARK)
            # Goal at top
            s += text(px, 95, "(start)", anchor="middle", size=9, fill=GRAY_DARK)
        s += text(px, 250, "during sharp-wave ripple", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 310, "Forward replay simulates a future trajectory. Reverse replay credits a recent path.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 326, "Same hippocampal hardware — opposite arrows of time.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f31_convergent_simulation():
    s = svg_open(700, 360)
    s += title("Convergent evolution of mental simulation", 350, 22)
    # Common ancestor at left
    s += circle(80, 200, 12, fill=INK)
    s += text(80, 230, "common\nancestor", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(80, 244, "~300 Mya", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Two branches
    s += line(80, 200, 350, 110, stroke=INK, sw=1.5)
    s += line(80, 200, 350, 290, stroke=INK, sw=1.5)
    # Mammals
    s += box(350, 80, 280, 80, fill=CREAM)
    s += text(490, 100, "Mammals", anchor="middle", weight="bold", size=12)
    s += text(490, 120, "hippocampus + PFC system", anchor="middle", size=10)
    s += text(490, 138, "forward + reverse replay; VTE", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Corvids
    s += box(350, 240, 280, 80, fill=CREAM)
    s += text(490, 260, "Corvids", anchor="middle", weight="bold", size=12)
    s += text(490, 278, "dorsal pallium + nidopallium", anchor="middle", size=10)
    s += text(490, 296, "caching + future planning", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Convergence label
    s += text(350, 200, "→  same abstract function:", weight="bold", size=11)
    s += text(350, 215, "evaluate options before acting", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f32_three_layers_phylo():
    s = svg_open(700, 420)
    s += title("Phylogenetic distribution of social-cognitive layers", 350, 22)
    # 3 layer rows
    layers = [
        (80, "1. Emotional contagion", ["all vertebrates ✓"]),
        (180, "2. Consolation / empathy", ["great apes ✓", "canids ✓", "elephants ✓", "corvids ✓", "prairie voles ✓", "macaques ✗"]),
        (280, "3. Perceptual perspective-taking", ["great apes ✓", "corvids ✓"]),
        (340, "4. False-belief attribution", ["great apes (implicit only)", "human children @ 4 yrs"]),
    ]
    for y, name, taxa in layers:
        s += text(60, y, name, weight="bold", size=11)
        for i, t in enumerate(taxa):
            s += box(310 + (i % 4) * 90, y - 14, 86, 22, fill=CREAM)
            s += text(310 + (i % 4) * 90 + 43, y, t, anchor="middle", size=9)
            if (i % 4 == 3) and i < len(taxa) - 1:
                # wrap to next row — but our layout has one row only; truncate after 4
                break
    s += text(350, 390, "Each higher layer is a strict subset of the lower. Macaques are the conspicuous gap at layer 2.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f33_hare_vs_sallyanne():
    s = svg_open(700, 360)
    s += title("Hare paradigm vs. Sally-Anne — what each test isolates", 350, 22)
    # Two panels
    # Left: Hare — perceptual perspective-taking
    s += text(180, 60, "Hare paradigm", anchor="middle", weight="bold", size=12)
    s += text(180, 76, "perceptual perspective-taking", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Setup: dominant on one side, food piles, barrier blocking dominant's view of one pile
    # Cage box
    s += box(60, 95, 240, 130)
    # Dominant
    s += circle(95, 130, 14, fill=GRAY_DARK, stroke=INK)
    s += text(95, 134, "D", anchor="middle", weight="bold", size=10, fill=CREAM)
    # Subordinate
    s += circle(265, 130, 14, fill=GRAY_LIGHT, stroke=INK)
    s += text(265, 134, "S", anchor="middle", weight="bold", size=10)
    # Food piles
    s += circle(160, 175, 5, fill=INK)
    s += text(165, 165, "food (visible)", size=9, fill=GRAY_DARK)
    s += circle(220, 175, 5, fill=INK)
    s += text(195, 200, "food (hidden)", size=9, fill=GRAY_DARK)
    # Barrier blocking D's view of right pile
    s += line(195, 145, 195, 215, stroke=INK, sw=2)
    s += text(180, 240, "barrier", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(180, 270, "Q: which pile does S take?", anchor="middle", weight="bold", size=10)
    s += text(180, 285, "A: the one D cannot see.", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Right: Sally-Anne — false-belief
    s += text(520, 60, "Sally-Anne", anchor="middle", weight="bold", size=12)
    s += text(520, 76, "false-belief attribution", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += box(400, 95, 240, 130)
    # Sally and Anne
    s += circle(440, 130, 14, fill=GRAY_DARK, stroke=INK)
    s += text(440, 134, "Sa", anchor="middle", weight="bold", size=9, fill=CREAM)
    # Sally went away
    s += text(395, 110, "(absent)", italic=True, size=9, fill=GRAY_DARK)
    s += circle(600, 130, 14, fill=GRAY_LIGHT, stroke=INK)
    s += text(600, 134, "An", anchor="middle", weight="bold", size=9)
    # Basket and box
    s += box(450, 175, 30, 30, fill=CREAM, stroke=INK)
    s += text(465, 215, "basket", anchor="middle", size=9, fill=GRAY_DARK)
    s += box(560, 175, 30, 30, fill=CREAM, stroke=INK)
    s += text(575, 215, "box", anchor="middle", size=9, fill=GRAY_DARK)
    # Marble (now in box) and original location (basket)
    s += circle(575, 195, 4, fill=INK)
    s += text(465, 195, "—", anchor="middle", size=9)
    s += text(520, 270, "Q: where will Sally LOOK?", anchor="middle", weight="bold", size=10)
    s += text(520, 285, "A: basket — Sally's false belief.", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 320, "Hare tests what the OTHER can see right now. Sally-Anne tests what the OTHER believes despite reality.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f34_von_economo():
    s = svg_open(700, 360)
    s += title("Von Economo neurons — independent appearance in three lineages", 350, 22)
    # Common ancestor
    s += circle(80, 200, 10, fill=INK)
    s += text(80, 230, "common\nmammalian\nancestor", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Three branches
    s += line(80, 200, 340, 100, stroke=INK)
    s += line(80, 200, 340, 200, stroke=INK)
    s += line(80, 200, 340, 300, stroke=INK)
    # Three lineages
    for y, lineage, where, when in [
        (100, "Primates", "ACC + frontoinsular", "~5 Mya (great apes)"),
        (200, "Cetaceans", "ACC + frontoinsular", "~30 Mya"),
        (300, "Elephants", "ACC + frontoinsular", "~50 Mya"),
    ]:
        s += box(340, y - 25, 280, 50, fill=CREAM)
        s += text(360, y - 7, lineage, weight="bold", size=12)
        s += text(360, y + 9, "Von Economo neurons in: " + where, italic=True, size=10)
        s += text(360, y + 23, "appeared independently " + when, italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 340, "Same cell type. Same cortical region. Three independent evolutionary origins. The substrate convergent.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f35_sally_anne():
    s = svg_open(700, 360)
    s += title("The Sally-Anne false-belief task", 350, 22)
    # Three panels
    panels_x = [130, 350, 570]
    for i, (cx, label) in enumerate(zip(panels_x, ["1. Sally hides marble", "2. Sally leaves; Anne moves", "3. Sally returns"])):
        s += text(cx, 60, label, anchor="middle", weight="bold", size=11)
        s += box(cx - 90, 75, 180, 180)
        # Basket on left
        s += box(cx - 60, 200, 30, 30, fill=CREAM, stroke=INK)
        s += text(cx - 45, 245, "basket", anchor="middle", size=9, fill=GRAY_DARK)
        # Box on right
        s += box(cx + 30, 200, 30, 30, fill=CREAM, stroke=INK)
        s += text(cx + 45, 245, "box", anchor="middle", size=9, fill=GRAY_DARK)
        # Sally and Anne
        if i == 0:
            # Sally + Anne both present, marble in basket
            s += circle(cx - 50, 110, 14, fill=GRAY_DARK)
            s += text(cx - 50, 114, "Sa", anchor="middle", weight="bold", size=9, fill=CREAM)
            s += circle(cx + 40, 110, 14, fill=GRAY_LIGHT, stroke=INK)
            s += text(cx + 40, 114, "An", anchor="middle", weight="bold", size=9)
            s += circle(cx - 45, 215, 4, fill=INK)
            s += arrow(cx - 50, 124, cx - 50, 195, sw=0.7)
        elif i == 1:
            # Sally absent; Anne moves marble
            s += text(cx - 50, 114, "(Sally", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
            s += text(cx - 50, 126, " away)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
            s += circle(cx + 40, 110, 14, fill=GRAY_LIGHT, stroke=INK)
            s += text(cx + 40, 114, "An", anchor="middle", weight="bold", size=9)
            s += circle(cx + 45, 215, 4, fill=INK)
            s += arrow(cx - 35, 215, cx + 30, 215, sw=1.2, stroke=GRAY_DARK)
        else:
            # Sally returns
            s += circle(cx - 50, 110, 14, fill=GRAY_DARK)
            s += text(cx - 50, 114, "Sa", anchor="middle", weight="bold", size=9, fill=CREAM)
            s += text(cx - 50, 130, "(returning)", anchor="middle", italic=True, size=8, fill=GRAY_DARK)
            s += circle(cx + 45, 215, 4, fill=INK)
            # Question mark over Sally
            s += text(cx - 50, 95, "?", anchor="middle", weight="bold", size=18)
            # Two arrows
            s += arrow(cx - 50, 130, cx - 45, 195, sw=1.2)
            s += text(cx - 75, 175, "false-belief", italic=True, size=9, weight="bold", fill=INK)
            s += text(cx - 75, 187, "answer (basket)", italic=True, size=9, fill=GRAY_DARK)
            s += arrow(cx - 36, 130, cx + 40, 195, sw=0.8, stroke=GRAY_LIGHT)
            s += text(cx + 30, 165, "wrong", italic=True, size=9, fill=GRAY_LIGHT)
    s += text(350, 305, "Correct answer = where Sally BELIEVES it is, not where it is. Tests representation of belief-as-belief.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f36_irl_tom():
    s = svg_open(700, 360)
    s += title("Inverse reinforcement learning as theory of mind", 350, 22)
    # Left: observed behavior
    s += text(180, 60, "Observed behavior", anchor="middle", weight="bold", size=12)
    behaviors = [
        (90, "walks toward kitchen"),
        (130, "opens refrigerator"),
        (170, "scans interior"),
    ]
    for y, b in behaviors:
        s += box(60, y, 240, 30)
        s += text(180, y + 18, b, anchor="middle", size=10)
    # IRL arrow
    s += arrow(305, 130, 395, 130, sw=2)
    s += text(350, 122, "IRL inference", anchor="middle", italic=True, weight="bold", size=11)
    # Right: latent variables
    s += text(520, 60, "Inferred latent variables", anchor="middle", weight="bold", size=12)
    latents = [
        (90, "desire", "food"),
        (130, "belief", "food is here"),
        (170, "intention", "eat"),
    ]
    for y, k, v in latents:
        s += box(400, y, 240, 30)
        s += text(440, y + 18, k + ":", weight="bold", size=10)
        s += text(620, y + 18, v, anchor="end", italic=True, size=10)
    # Generalization arrow
    s += arrow(520, 215, 520, 250, sw=2)
    s += text(540, 235, "generalizes to novel situations", italic=True, size=10, weight="bold")
    s += text(520, 280, "predicts behavior in cases never observed", anchor="middle", size=10, fill=GRAY_DARK)
    s += text(350, 320, "The compact mental-state representation is the compression that makes social prediction tractable.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f37_crow_tools():
    s = svg_open(700, 360)
    s += title("New Caledonian crow tools — sequential modification of raw materials", 350, 22)
    # Two panels
    # Hooked twig
    s += text(180, 60, "Hooked twig (from forked branch)", anchor="middle", weight="bold", size=11)
    s += box(60, 80, 240, 200)
    # Original branch
    s += text(180, 105, "raw material:", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += path("M 100 130 L 200 130 L 215 145 L 240 165", stroke=INK, sw=2)
    s += line(200, 130, 240, 100, stroke=INK, sw=2)
    s += text(180, 195, "modifications:", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(70, 215, "1. break at fork  2. shorten side  3. retain hook", size=10)
    s += text(180, 250, "final tool: ↪ hook", anchor="middle", weight="bold", size=11)
    # Stepped pandanus
    s += text(520, 60, "Stepped pandanus strip", anchor="middle", weight="bold", size=11)
    s += box(400, 80, 240, 200)
    s += text(520, 105, "raw material: pandanus leaf with barbs", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Strip with steps
    d = "M 430 140 "
    for k in range(8):
        d += f"L {430 + k * 24} {140 - (k * 4)} L {430 + (k+1) * 24} {140 - (k * 4)} "
    s += path(d, stroke=INK, sw=1.5)
    # Barbs on the strip
    for x in (430, 460, 490, 520, 550, 580):
        s += line(x, 140 - (((x - 430) // 24) * 4), x + 4, 140 - (((x - 430) // 24) * 4) - 8, stroke=INK, sw=1)
    s += text(520, 200, "modifications:", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(410, 220, "1. cut along grain  2. step the cut  3. preserve barbs", size=10)
    s += text(520, 250, "final tool: standardized barbed strip", anchor="middle", weight="bold", size=11)
    s += text(350, 320, "Both tools require sequential form imposition — not selection from available objects.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f38_bowerbird():
    s = svg_open(700, 360)
    s += title("Great bowerbird — forced perspective court layout", 350, 22)
    # Two panels: top view and female perspective
    s += text(180, 60, "Top view", anchor="middle", weight="bold", size=12)
    s += box(60, 80, 240, 200)
    # Avenue (two parallel rows of sticks)
    for k in range(8):
        s += line(120 + k * 5, 110, 120 + k * 5, 200, stroke=INK, sw=0.6)
        s += line(220 + k * 5, 110, 220 + k * 5, 200, stroke=INK, sw=0.6)
    s += text(180, 100, "stick avenue (female enters here)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    # Court with size-graded objects
    sizes = [3, 5, 8, 12, 18, 24]
    for i, sz in enumerate(sizes):
        s += circle(110 + i * 30, 240, sz / 2, fill=INK)
    s += text(180, 270, "graded objects: small near, large far", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Female sightlines
    for i in range(len(sizes)):
        s += line(180, 200, 110 + i * 30, 240, stroke=GRAY_LIGHT, sw=0.6, dash="2,2")
    # Right: female's perspective
    s += text(520, 60, "From female's perspective", anchor="middle", weight="bold", size=12)
    s += box(400, 80, 240, 200)
    # Show all objects appearing the SAME size
    for i, sz in enumerate(sizes):
        s += circle(440 + i * 30, 180, 7, fill=INK)
    s += text(520, 220, "all objects appear uniform size", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(520, 240, "(forced perspective inflates the male)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 320, "Males re-arrange the gradient after viewing from inside the avenue. Sensitive to viewer.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f39_individual_vs_cumulative():
    s = svg_open(700, 360)
    s += title("Individual creativity vs. cumulative culture — two distinct loops", 350, 22)
    # Left loop
    s += text(180, 60, "Individual creativity", anchor="middle", weight="bold", size=12)
    # 4 nodes around a loop
    nodes_a = [
        (180, 100, "novel behavior"),
        (260, 175, "evaluate"),
        (180, 250, "may spread"),
        (100, 175, "loop ends"),
    ]
    for x, y, lbl in nodes_a:
        s += box(x - 50, y - 14, 100, 28, fill=CREAM)
        s += text(x, y + 4, lbl, anchor="middle", size=10)
    # Arrows
    s += arrow(180, 114, 180, 114 + 40)
    # Hmm actually let's simplify with a circular path
    s += path(f"M 230 100 Q 270 175, 230 250", stroke=INK, sw=1, dash="3,2")
    s += path(f"M 130 100 Q 90 175, 130 250", stroke=INK, sw=1, dash="3,2")
    s += text(180, 285, "(no ratchet)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Right loop
    s += text(520, 60, "Cumulative culture (the ratchet)", anchor="middle", weight="bold", size=12)
    nodes_b = [
        (430, 110, "innovation"),
        (610, 110, "transmission"),
        (610, 220, "next gen inherits"),
        (430, 220, "extends + refines"),
    ]
    for x, y, lbl in nodes_b:
        s += box(x - 60, y - 14, 120, 28, fill=CREAM)
        s += text(x, y + 4, lbl, anchor="middle", size=10)
    s += arrow(490, 110, 549, 110)
    s += arrow(610, 124, 610, 206)
    s += arrow(550, 220, 491, 220)
    s += arrow(430, 206, 430, 124)
    # Indicate accumulation: a small "+1" arrow
    s += arrow(430, 234, 430, 290, sw=1.5)
    s += text(440, 270, "+1 every cycle", italic=True, size=10, weight="bold")
    s += text(520, 305, "knowledge accumulates", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 340, "Left: ends with the individual. Right: each generation begins where the last left off.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f40_three_rings():
    s = svg_open(700, 360)
    s += title("Three concentric subsystems of the self", 350, 22)
    cx, cy = 350, 195
    # Outer ring: narrative
    s += circle(cx, cy, 130, fill=CREAM, stroke=INK)
    # Middle ring: social
    s += circle(cx, cy, 90, fill=GRAY_LIGHT, stroke=INK)
    # Inner: body
    s += circle(cx, cy, 50, fill=INK, stroke=INK)
    s += text(cx, cy - 4, "Body self", anchor="middle", weight="bold", size=12, fill=CREAM)
    s += text(cx, cy + 12, "(mirror test)", anchor="middle", italic=True, size=10, fill=CREAM)
    s += text(cx, cy - 70, "Social self", anchor="middle", weight="bold", size=12)
    s += text(cx, cy - 56, "(recognition by others)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(cx, cy - 110, "Narrative self", anchor="middle", weight="bold", size=12)
    s += text(cx, cy - 96, "(continuity over time)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Species annotations
    species = [
        (560, 110, "Chimpanzee", "✓ ✓ ✓"),
        (560, 175, "Magpie", "✓ partial ✗"),
        (560, 240, "Cleaner wrasse", "✓ ? ✗"),
    ]
    for x, y, name, marks in species:
        s += text(x, y, name, weight="bold", size=10)
        s += text(x, y + 14, marks, italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 340, "The mirror test probes one ring — the innermost.", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f41_mirror_decision_tree():
    s = svg_open(700, 420)
    s += title("Decision tree — interpreting a mirror-test failure", 350, 22)
    # Root
    s += box(260, 60, 180, 36, fill=CREAM)
    s += text(350, 82, "Species fails mark test", anchor="middle", weight="bold", size=11)
    # Branch 1: visual-only?
    s += arrow(350, 96, 350, 130)
    s += box(260, 130, 180, 36, fill=GRAY_LIGHT)
    s += text(350, 152, "Was the test visual-only?", anchor="middle", weight="bold", size=10)
    # Yes branch
    s += arrow(350, 166, 200, 200)
    s += box(80, 200, 240, 36, fill=CREAM)
    s += text(200, 220, "Sensory mismatch possible —", anchor="middle", size=10)
    s += text(200, 234, "test olfactory/tactile analog", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(180, 192, "yes", anchor="end", italic=True, size=9, fill=GRAY_DARK)
    # No branch — continues to Branch 2
    s += arrow(350, 166, 500, 200)
    s += box(380, 200, 240, 36, fill=GRAY_LIGHT)
    s += text(500, 222, "Did animal show social response", anchor="middle", weight="bold", size=10)
    s += text(500, 236, "to reflection?", anchor="middle", italic=True, size=10)
    s += text(370, 192, "no", anchor="start", italic=True, size=9, fill=GRAY_DARK)
    # Yes — social inhibition
    s += arrow(500, 236, 200, 290)
    s += box(80, 290, 240, 36, fill=CREAM)
    s += text(200, 310, "Social inhibition possible —", anchor="middle", size=10)
    s += text(200, 324, "check gaze-aversion norms", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(220, 285, "yes", anchor="end", italic=True, size=9, fill=GRAY_DARK)
    # No — continues to Branch 3
    s += arrow(500, 236, 500, 290)
    s += box(380, 290, 240, 36, fill=GRAY_LIGHT)
    s += text(500, 312, "Did animal attend to mark?", anchor="middle", weight="bold", size=10)
    s += text(490, 285, "no", anchor="start", italic=True, size=9, fill=GRAY_DARK)
    # Outcomes
    s += arrow(500, 326, 350, 360)
    s += box(220, 360, 260, 36, fill=CREAM)
    s += text(350, 380, "Genuine absence of body-self?", anchor="middle", weight="bold", size=10, fill=INK)
    s += text(350, 394, "(the strongest negative interpretation)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    return s + svg_close()


def f42_clinical_dissociation():
    s = svg_open(700, 360)
    s += title("Clinical dissociations — body-self decomposes into independent components", 350, 22)
    # Two panels showing self-model with one component damaged
    panels = [
        (180, "Mirrored self-misidentification",
         [("visual–kinesthetic match", True), ("social self", False), ("agency", False)]),
        (520, "Alien hand syndrome",
         [("visual–kinesthetic match", False), ("ownership", False), ("agency", True)]),
    ]
    for cx, head, components in panels:
        s += text(cx, 60, head, anchor="middle", weight="bold", size=12)
        # Self-model diagram: 3 stacked components
        for i, (name, damaged) in enumerate(components):
            y = 90 + i * 50
            fill = INK if damaged else GRAY_LIGHT
            stroke = INK
            s += box(cx - 110, y, 220, 40, fill=fill, stroke=stroke)
            s += text(cx, y + 22, name, anchor="middle", weight="bold", size=11,
                      fill=(CREAM if damaged else INK))
            if damaged:
                s += text(cx + 90, y + 22, "✗", anchor="middle", weight="bold", size=14, fill=CREAM)
            else:
                s += text(cx + 90, y + 22, "✓", anchor="middle", weight="bold", size=14, fill=INK)
        # Caption
        if "Mirrored" in head:
            cap = "patient sees own reflection as a stranger;\n recognizes the body, but not as theirs"
        else:
            cap = "hand acts on its own;\n patient owns the hand, denies agency"
        for i, ln in enumerate(cap.split("\n")):
            s += text(cx, 260 + i * 14, ln, anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 330, "Different lesions damage different sub-components — body-self is not a single faculty.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f43_hampton_accuracy():
    s = svg_open(700, 360)
    s += title("Hampton 2001 — chosen vs. forced trials across delays", 350, 22)
    ax = 100
    ay = 280
    aw = 480
    ah = 200
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
    s += line(ax, 80, ax, ay, stroke=GRAY_MID)
    # x: short / medium / long
    for i, d in enumerate(["short", "medium", "long"]):
        x = ax + 80 + i * 160
        s += text(x, ay + 18, d, anchor="middle", size=11, fill=GRAY_DARK)
    s += text(350, ay + 38, "delay length", anchor="middle", weight="bold", size=11)
    # y axis
    for v, lbl in [(80, "100"), (180, "70"), (ay, "40")]:
        s += line(ax - 4, v, ax, v, stroke=GRAY_MID)
        s += text(ax - 8, v + 4, lbl, anchor="end", size=10, fill=GRAY_DARK)
    s += text(45, 180, "accuracy (%)", anchor="middle", italic=True, weight="bold", size=11)
    # Two lines
    short, mid, long_ = 80 + 90 + 160, 80 + 80 + 160, 80 + 60 + 160
    pts_forced = [(ax + 80, 92), (ax + 240, 130), (ax + 400, 200)]
    pts_chosen = [(ax + 80, 88), (ax + 240, 98), (ax + 400, 130)]
    for pts, label, dash, fill in [(pts_forced, "Forced trials", "4,3", WHITE),
                                    (pts_chosen, "Chosen trials", None, INK)]:
        d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
        s += path(d, stroke=INK, sw=2, dash=dash)
        for x, y in pts:
            s += circle(x, y, 4, fill=fill, stroke=INK, sw=1)
    # Labels on the lines
    s += text(ax + 410, 200, "forced", italic=True, size=10, fill=GRAY_DARK)
    s += text(ax + 410, 132, "chosen (opt-in)", italic=True, size=10, weight="bold")
    s += text(350, 320, "The gap WIDENS with delay — the diagnostic that rules out simple stimulus avoidance.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f44_metacog_timeline():
    s = svg_open(700, 360)
    s += title("Metacognition across 600 million years of evolution", 350, 22)
    ax = 80
    ay = 200
    aw = 580
    s += line(ax, ay, ax + aw, ay, stroke=INK, sw=1.2)
    # Tick markers (rough)
    branch_points = [(0, "common ancestor"), (0.45, "vertebrate split"), (0.65, "amniote split"), (0.85, "primates"), (1.0, "today")]
    for f, lbl in branch_points:
        x = ax + f * aw
        s += line(x, ay - 4, x, ay + 4, sw=0.7)
        s += text(x, ay + 18, lbl, anchor="middle", size=9, fill=GRAY_DARK)
    # Species icons / labels
    species = [
        (0.78, 110, "Dolphin (Smith 1995)\nuncertainty monitoring", "low"),
        (0.86, 80, "Macaque (Hampton 2001)\nuncertainty monitoring", "low"),
        (0.78, 270, "Rat (Foote-Crystal 2007)\nuncertainty monitoring", "low"),
        (0.55, 90, "Honeybee (Perry-Barron 2013)\nuncertainty monitoring", "low"),
        (0.94, 270, "Scrub-jay (Watanabe-Clayton 2016)\ninformation seeking", "high"),
    ]
    for f, y, lbl, level in species:
        x = ax + f * aw
        # vertical line from species to timeline
        s += line(x, y, x, ay, stroke=GRAY_LIGHT, sw=0.6, dash="2,2")
        # Marker
        s += circle(x, y, 5, fill=(INK if level == "high" else GRAY_DARK), stroke=INK)
        for i, ln in enumerate(lbl.split("\n")):
            s += text(x, y + 18 + i * 12, ln, anchor="middle", size=9)
    # Y-axis label
    s += text(45, 90, "info-seeking", italic=True, size=10, weight="bold", fill=INK)
    s += text(45, 110, "(higher demand)", italic=True, size=9, fill=GRAY_DARK)
    s += text(45, 270, "uncertainty monitoring", italic=True, size=10)
    s += text(45, 285, "(lower demand)", italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 330, "Information seeking is the higher rung. Most demonstrations remain at uncertainty monitoring.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f45_language_curriculum():
    s = svg_open(700, 360)
    s += title("Language acquisition — proto-conversation to recursive grammar", 350, 22)
    ax = 80
    ay = 220
    aw = 580
    s += line(ax, ay, ax + aw, ay, stroke=INK, sw=1.2)
    # X axis: months
    for m in (0, 6, 12, 18, 24, 30, 36):
        x = ax + (m / 36) * aw
        s += line(x, ay, x, ay + 4, stroke=GRAY_MID)
        s += text(x, ay + 18, f"{m} mo", anchor="middle", size=9, fill=GRAY_DARK)
    # Stages
    stages = [
        (3, 100, "Proto-conversations", "dyad: face-to-face turn-taking"),
        (8, 80, "Gaze following", "infant tracks adult attention"),
        (12, 110, "Joint attention →\ndeclarative pointing", "triad: I, you, that thing"),
        (12, 180, "First words", "labeled categories"),
        (18, 100, "Vocabulary explosion", "30+ new words per week"),
        (21, 180, "Question forms", "asking for information"),
        (33, 110, "Recursive grammar", "embedded clauses"),
    ]
    for m, y, name, sub in stages:
        x = ax + (m / 36) * aw
        s += line(x, y, x, ay, stroke=GRAY_LIGHT, sw=0.6, dash="2,2")
        s += circle(x, y, 5, fill=INK, stroke=INK)
        s += text(x, y - 8, name, anchor="middle", weight="bold", size=10)
        s += text(x, y + 14, sub, anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 290, "First two stages are dyadic. The shift to triadic joint attention (~9 mo) is the precursor of language.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f46_collective_timeline():
    s = svg_open(700, 360)
    s += title("Three mechanisms of collective intelligence", 350, 22)
    ax = 80
    ay = 280
    aw = 580
    ah = 200
    s += line(ax, ay, ax + aw, ay, stroke=GRAY_MID)
    s += line(ax, 80, ax, ay, stroke=GRAY_MID)
    s += text(35, 180, "generational", anchor="middle", italic=True, weight="bold")
    s += text(35, 195, "improvement", anchor="middle", italic=True, size=10)
    # 3 stages with increasing height
    rows = [
        (140, 270, "Aggregation", "(Galton's ox; any independent estimators)", "flat — no improvement"),
        (350, 240, "Coordination", "(murmurations, fish schools, bee foraging)", "flat — same task each generation"),
        (560, 110, "Cumulative culture", "(humans only — documented ratcheting)", "logarithmic — knowledge accumulates"),
    ]
    for cx, top_y, name, ex, growth in rows:
        s += box(cx - 90, top_y, 180, ay - top_y, fill=GRAY_LIGHT)
        s += text(cx, top_y - 6, name, anchor="middle", weight="bold", size=11)
        s += text(cx, top_y + 18, ex, anchor="middle", italic=True, size=9, fill=GRAY_DARK)
        s += text(cx, ay + 18, growth, anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += text(350, 330, "The third mechanism is the ratchet. The first two are real but bounded — they don't accumulate.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f47_swarm_decision():
    s = svg_open(700, 360)
    s += title("Honeybee swarm — quality-weighted positive feedback with stop signals", 350, 22)
    panels = [
        (130, "1. Scouts depart", "scouts"),
        (300, "2. Two dancer pops.\nwith stop signals", "dancers"),
        (470, "3. One pop. wins\nat quorum threshold", "quorum"),
        (640, "4. Swarm lifts off", "liftoff"),
    ]
    for cx, label, kind in panels:
        s += box(cx - 70, 60, 140, 200)
        # Cluster (a circle representing the swarm cluster)
        s += circle(cx, 130, 30, fill=GRAY_LIGHT, stroke=INK)
        s += text(cx, 134, "swarm", anchor="middle", italic=True, size=9)
        if kind == "scouts":
            # Two arrows departing
            s += arrow(cx + 22, 115, cx + 65, 90)
            s += arrow(cx - 22, 115, cx - 65, 90)
            s += text(cx, 250, "site A and site B", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
        elif kind == "dancers":
            # Two populations of dancers as small dots on the swarm with stop arrows between them
            for k in range(8):
                ang = math.radians(180 - 40 + k * 7)
                px_ = cx + 30 * math.cos(ang)
                py_ = 130 + 30 * math.sin(ang)
                s += circle(px_, py_, 3, fill=INK)
            for k in range(5):
                ang = math.radians(360 - 40 + k * 7)
                px_ = cx + 30 * math.cos(ang)
                py_ = 130 + 30 * math.sin(ang)
                s += circle(px_, py_, 3, fill=GRAY_DARK)
            # Stop signal arrows crossing
            s += line(cx - 25, 120, cx + 25, 140, stroke=INK, sw=1, dash="3,2")
            s += line(cx + 25, 120, cx - 25, 140, stroke=INK, sw=1, dash="3,2")
            s += text(cx, 220, "vibrational stop", anchor="middle", italic=True, size=9)
            s += text(cx, 234, "signals between", anchor="middle", italic=True, size=9)
        elif kind == "quorum":
            # One population grew, line marks threshold
            for k in range(15):
                ang = math.radians(180 + k * 13)
                px_ = cx + 30 * math.cos(ang)
                py_ = 130 + 30 * math.sin(ang)
                s += circle(px_, py_, 3, fill=INK)
            s += line(cx - 60, 200, cx + 60, 200, stroke=INK, sw=1.5, dash="4,3")
            s += text(cx, 215, "quorum", anchor="middle", italic=True, weight="bold", size=10)
        else:
            # Liftoff — arrows up
            s += arrow(cx, 130, cx, 90, sw=2)
            s += arrow(cx + 12, 130, cx + 12, 90, sw=2)
            s += arrow(cx - 12, 130, cx - 12, 90, sw=2)
            s += text(cx, 250, "to winning site", anchor="middle", italic=True, size=10, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            s += text(cx, 290 + i * 14, ln, anchor="middle", size=11, weight="bold")
    s += text(350, 350, "No central planner. Local interactions; global decision. Cross-inhibition speeds convergence.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f48_geirhos_cue_conflict():
    s = svg_open(700, 360)
    s += title("Geirhos cue-conflict — texture beats shape in ImageNet-trained CNNs", 350, 22)
    # Two panels
    # Left: cat-shape with elephant-skin texture
    s += text(180, 60, "Cat shape  +  elephant skin", anchor="middle", weight="bold", size=11)
    s += box(60, 80, 240, 200)
    # Cat silhouette (simplified)
    s += path("M 120 250 L 120 180 L 110 160 L 130 150 L 130 130 L 150 130 L 160 110 L 180 110 L 190 130 L 220 130 L 240 150 L 250 170 L 250 230 L 240 250 Z",
              fill=GRAY_LIGHT, stroke=INK, sw=1.2)
    # Add wrinkly texture marks (suggesting elephant skin)
    for k in range(15):
        rx = 130 + (k % 5) * 22
        ry = 150 + (k // 5) * 30
        s += line(rx, ry, rx + 12, ry + 4, stroke=GRAY_DARK, sw=0.6)
    s += text(180, 305, "human: 'cat'  /  CNN: 'elephant'", anchor="middle", italic=True, size=10, weight="bold")
    # Right: elephant-shape with cat-fur texture
    s += text(520, 60, "Elephant shape  +  cat fur", anchor="middle", weight="bold", size=11)
    s += box(400, 80, 240, 200)
    # Elephant silhouette
    s += path("M 440 250 L 440 200 L 430 180 L 440 160 L 460 150 L 480 150 L 510 130 L 540 130 L 570 150 L 600 160 L 620 180 L 620 240 L 610 250 Z",
              fill=GRAY_LIGHT, stroke=INK, sw=1.2)
    # Fur-like short hatches
    for k in range(35):
        rx = 440 + (k % 7) * 25 + (k // 7) * 4
        ry = 180 + (k // 7) * 12
        s += line(rx, ry, rx + 1, ry - 5, stroke=GRAY_DARK, sw=0.5)
    s += text(520, 305, "human: 'elephant'  /  CNN: 'cat'", anchor="middle", italic=True, size=10, weight="bold")
    s += text(350, 340, "Network gets benchmark performance via texture cues. Right answers, wrong computation.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f49_radar_profile():
    s = svg_open(700, 480)
    s += title("AI cognitive profile — extreme highs and extreme lows", 350, 22)
    cx, cy = 350, 250
    # Axes
    axes = [
        "in-distribution\npattern recognition",
        "ToM (standard\nbenchmarks)",
        "ToM (perturbation\nrobustness)",
        "metacognition\n(language)",
        "metacognition\n(operation)",
        "embodied\nnavigation",
        "cumulative\nculture",
    ]
    n = len(axes)
    R = 160
    for i, ax_label in enumerate(axes):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        x_ = cx + R * math.cos(ang)
        y_ = cy + R * math.sin(ang)
        s += line(cx, cy, x_, y_, stroke=GRAY_LIGHT, sw=0.6)
        # Label outside
        lx = cx + (R + 30) * math.cos(ang)
        ly = cy + (R + 30) * math.sin(ang)
        for j, ln in enumerate(ax_label.split("\n")):
            s += text(lx, ly + j * 12, ln, anchor="middle", size=9)
    # Concentric reference rings
    for r in (40, 80, 120, 160):
        s += circle(cx, cy, r, stroke=GRAY_LIGHT, sw=0.5, dash="2,2")
    # AI profile (extreme high on 0,3 ; extreme low on 2,5,6 ; medium on 1,4)
    ai_radii = [150, 120, 30, 130, 25, 10, 15]
    biological_radii = [80, 70, 70, 60, 55, 90, 60]
    # Plot AI profile
    pts = []
    for i, r in enumerate(ai_radii):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
    s += path(d, stroke=INK, sw=2, fill=GRAY_LIGHT)
    # Biological profile (smoother)
    pts2 = []
    for i, r in enumerate(biological_radii):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        pts2.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d2 = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts2) + " Z"
    s += path(d2, stroke=INK, sw=1.5, dash="4,3")
    # Legend
    s += line(60, 440, 80, 440, stroke=INK, sw=2)
    s += text(86, 444, "AI profile", size=10)
    s += line(180, 440, 200, 440, stroke=INK, sw=1.5, dash="4,3")
    s += text(206, 444, "biological generalist", size=10)
    s += text(350, 460, "The shape — not the height — is the data point.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f50_extension_asymmetry():
    s = svg_open(700, 420)
    s += title("Extension asymmetry — capacity extended, direction retained", 350, 22)
    # Two columns + horizontal layered structure
    s += text(180, 60, "Pearl Rung 1 — capacities tools have extended", anchor="middle", weight="bold", size=12)
    s += text(520, 60, "Pearl Rungs 2–3 — direction the human keeps", anchor="middle", weight="bold", size=12)
    # Rows: capacities and the corresponding directing capacity
    rows = [
        (100, "gradient sensing", "choosing what to measure"),
        (140, "steering / navigation", "deciding the destination"),
        (180, "pattern recognition", "framing the question"),
        (220, "memory / retrieval", "judging what is worth remembering"),
        (260, "prediction", "selecting the counterfactual"),
        (300, "language production", "auditing for plausibility + accountability"),
    ]
    for y, cap, direction in rows:
        s += box(50, y, 260, 30, fill=GRAY_LIGHT)
        s += text(180, y + 19, cap, anchor="middle", size=10)
        s += arrow(310, y + 15, 390, y + 15, sw=1)
        s += box(390, y, 260, 30, fill=CREAM)
        s += text(520, y + 19, direction, anchor="middle", size=10)
    s += text(350, 360, "Right column does not shrink as tools improve — it grows.", anchor="middle",
              weight="bold", size=11)
    s += text(350, 378, "Every tool in the catalog extends a Rung-1 capacity and leaves Rungs 2–3 to the human.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 394, "AI is the next entry in this catalog — not a replacement for the directing layer.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f51_celegans_micrograph():
    s = svg_open(700, 360)
    s += title("Caenorhabditis elegans — anatomical landmarks", 350, 22)
    # Worm body
    cx_, cy_ = 350, 200
    # Long thin worm
    s += path(f"M 80 200 Q 200 170, 350 200 Q 500 230, 620 200 Q 500 180, 350 200 Q 200 220, 80 200 Z",
              fill=CREAM, stroke=INK, sw=1.2)
    # Pharynx (anterior bulb)
    s += ellipse(110, 200, 22, 8, fill=GRAY_LIGHT, stroke=INK)
    s += text(110, 175, "pharynx", anchor="middle", size=10, weight="bold")
    s += text(110, 188, "(anterior)", anchor="middle", italic=True, size=9, fill=GRAY_DARK)
    s += line(110, 192, 110, 195, stroke=INK)
    # Intestine (long stripe)
    s += line(140, 200, 560, 200, stroke=GRAY_DARK, sw=0.8, dash="4,2")
    s += text(350, 232, "intestine (runs along midline)", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Gonads (two loops near posterior)
    s += path("M 400 200 Q 430 180, 460 200 Q 430 220, 400 200 Z", fill=GRAY_LIGHT, stroke=INK, sw=0.7)
    s += path("M 470 200 Q 500 180, 530 200 Q 500 220, 470 200 Z", fill=GRAY_LIGHT, stroke=INK, sw=0.7)
    s += text(490, 175, "gonads", anchor="middle", size=10, weight="bold")
    # Posterior tail
    s += text(610, 192, "tail", anchor="middle", size=10, weight="bold")
    # Scale bar
    s += line(540, 290, 620, 290, sw=2.5)
    s += text(580, 305, "1 mm", anchor="middle", size=10)
    # Side annotations
    s += text(350, 270, "Transparent under stereo microscope; entire anatomy visible without sectioning.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 330, "302 neurons, complete connectome (White et al. 1986). The book's central organism.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f52_celegans_radar():
    s = svg_open(700, 480)
    s += title("C. elegans across the book's 14 cognitive axes", 350, 22)
    cx, cy = 350, 270
    R = 165
    axes = [
        "steering", "learning", "affect", "pattern\nrecognition",
        "navigation", "RL", "simulation", "social",
        "ToM", "creativity", "self-awareness",
        "metacognition", "language", "cumulative\nculture",
    ]
    # The worm scores: present (low value) on first ~7 axes; absent on the last 7
    radii = [70, 50, 10, 30, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0]
    n = len(axes)
    for i, lbl in enumerate(axes):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        x_ = cx + R * math.cos(ang)
        y_ = cy + R * math.sin(ang)
        s += line(cx, cy, x_, y_, stroke=GRAY_LIGHT, sw=0.5)
        lx = cx + (R + 32) * math.cos(ang)
        ly = cy + (R + 32) * math.sin(ang)
        for j, ln in enumerate(lbl.split("\n")):
            s += text(lx, ly + j * 12, ln, anchor="middle", size=9)
    for r in (50, 100, 150):
        s += circle(cx, cy, r, stroke=GRAY_LIGHT, sw=0.5, dash="2,2")
    pts = []
    for i, r in enumerate(radii):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        if r == 0:
            r = 1
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
    s += path(d, stroke=INK, sw=2, fill=GRAY_LIGHT)
    # Mark zero-axis cluster
    for i in range(7, 14):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        x_ = cx + 1 * math.cos(ang)
        y_ = cy + 1 * math.sin(ang)
        s += circle(x_, y_, 3, fill=INK)
    s += text(350, 460, "Present on 6 axes. Absent on 8. The worm's shape is small, asymmetric, and exactly fitted to its niche.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    return s + svg_close()


def f53_map_vs_ladder():
    s = svg_open(700, 480)
    s += title("Scala naturae vs. the actual map", 350, 22)
    # Two panels
    # Left: the ladder (vertical hierarchy)
    s += text(180, 60, "Scala naturae  (the ladder)", anchor="middle", weight="bold", size=12)
    rungs = [
        (90,  "Human", INK),
        (130, "Chimpanzee", GRAY_DARK),
        (170, "Dolphin", GRAY_DARK),
        (210, "Crow", GRAY_MID),
        (250, "Bee", GRAY_MID),
        (290, "Fish", GRAY_LIGHT),
        (330, "Worm", GRAY_LIGHT),
        (370, "Bacterium", GRAY_LIGHT),
    ]
    s += line(180, 80, 180, 380, stroke=INK, sw=2)
    for y, name, c in rungs:
        s += line(160, y, 200, y, stroke=INK, sw=2)
        s += text(220, y + 4, name, weight="bold", size=11)
        s += circle(180, y, 5, fill=c)
    s += text(180, 410, "single axis, ranked", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    # Right: the map (2D scatter)
    s += text(520, 60, "The actual map  (multi-axis)", anchor="middle", weight="bold", size=12)
    s += box(390, 80, 260, 320, fill=CREAM)
    # X axis: social cognition; Y axis: pattern recognition (illustrative)
    s += line(390, 380, 650, 380, stroke=GRAY_MID)
    s += line(390, 80, 390, 380, stroke=GRAY_MID)
    s += text(520, 395, "social cognition →", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(380, 240, "pattern recog. →", anchor="end", italic=True, size=10, fill=GRAY_DARK)
    # Species at non-rank positions
    points = [
        (425, 110, "human", "h"),
        (590, 130, "chimp", "c"),
        (470, 160, "dolphin", "d"),
        (610, 270, "crow", "cr"),
        (510, 290, "bee", "b"),
        (560, 350, "archerfish", "f"),
        (430, 360, "worm", "w"),
        (440, 200, "octopus", "o"),
    ]
    for x, y, name, _ in points:
        s += circle(x, y, 6, fill=INK)
        s += text(x + 9, y + 3, name, size=10)
    s += text(520, 425, "each species occupies a region defined by its profile",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(520, 442, "no axis ranks them all", anchor="middle", italic=True, size=10, fill=GRAY_DARK)
    s += text(350, 470, "The ladder is the picture from a single axis.  The map is the data.",
              anchor="middle", italic=True, size=10, fill=GRAY_DARK, weight="bold")
    return s + svg_close()


# ======================================================================
# Map: token substring → (chapter file, fig num, slug, title, builder)
# ======================================================================

FIGURES = [
    ("01-the-definition-problem.md",              "01", "definitions-timeline",       "Major intelligence definitions, 1905–2019.",                                       f01_definition_timeline,              "timeline of major intelligence definitions"),
    ("01-the-definition-problem.md",              "02", "shalizi-pca",                "Shalizi's PCA argument — a 'general factor' falls out of any positively correlated set.", f02_shalizi_pca,             "two-panel illustration of Shalizi's PCA argument"),
    ("02-before-brains.md",                       "01", "physarum-maze",              "Physarum solves a maze in four frames — coverage, then pruning to the shortest path.",  f03_physarum_maze,                    "Time-lapse sequence of Physarum polycephalum filling a plastic maze"),
    ("02-before-brains.md",                       "02", "physarum-tokyo",             "Physarum's network and the actual Tokyo Kanto rail map.",                            f04_physarum_tokyo,                   "Side-by-side comparison of the Physarum oat-flake network"),
    ("02-before-brains.md",                       "03", "ecoli-cascade",              "E. coli chemotaxis — fast signaling and slow methylation memory.",                  f05_ecoli_signal_cascade,             "E. coli chemotaxis signal cascade"),
    ("02-before-brains.md",                       "04", "ecoli-temporal-weights",     "E. coli temporal weighting — the cell computes a difference, not a level.",          f06_temporal_weighting,               "Temporal weighting function for E. coli chemotaxis"),
    ("02-before-brains.md",                       "05", "flytrap-integrator",         "Venus flytrap — leaky calcium integrator counts trigger touches.",                  f07_flytrap_integrator,               "Venus flytrap leaky integrator"),
    ("03-steering.md",                            "01", "radial-vs-bilateral",        "Radial vs. bilateral symmetry — geometry constrains the decision.",                 f08_radial_vs_bilateral,              "side-by-side illustration of radial symmetry"),
    ("03-steering.md",                            "02", "run-pirouette",              "C. elegans run-and-pirouette navigation up a chemical gradient.",                   f09_run_pirouette,                    "time-lapse diagram of C. elegans run-and-pirouette navigation"),
    ("03-steering.md",                            "03", "synaptic-vs-modulatory",     "Fast synaptic transmission vs. neuromodulatory broadcast.",                          f10_synaptic_vs_neuromodulatory,      "contrast of fast synaptic transmission vs. neuromodulatory broadcast"),
    ("03-steering.md",                            "04", "six-component-stack",        "Steering — six-component architecture as a causal stack.",                          f11_six_component_stack,              "the six-component architecture as a causal stack"),
    ("04-learning-and-memory.md",                 "01", "learning-ladder",            "Three forms of learning, in evolutionary order.",                                    f12_learning_ladder,                  "vertical ladder showing the three forms of learning"),
    ("04-learning-and-memory.md",                 "02", "aplysia-circuit",            "Aplysia gill-withdrawal — sensitization circuit.",                                  f13_aplysia_circuit,                  "schematic of the Aplysia gill-withdrawal circuit"),
    ("04-learning-and-memory.md",                 "03", "short-vs-long-term",         "Short-term vs. long-term sensitization in Aplysia.",                                f14_short_vs_long_term,               "two-panel comparison of short-term vs. long-term sensitization"),
    ("04-learning-and-memory.md",                 "04", "rescorla-wagner",            "Rescorla–Wagner — learning tracks the residual prediction error.",                  f15_rescorla_wagner,                  "three-panel illustration of the Rescorla-Wagner prediction error"),
    ("05-emotion.md",                             "01", "per-rate",                   "Bateson 2011 — proboscis-extension rate across the CS+/CS− continuum.",             f16_per_rate,                         "Proboscis extension rate"),
    ("05-emotion.md",                             "02", "cognitive-bias-paradigm",    "The cognitive-bias paradigm — training and test.",                                  f17_cognitive_bias_paradigm,          "The cognitive-bias paradigm"),
    ("05-emotion.md",                             "03", "approach-latency",           "Perry 2016 — approach latency to ambiguous cylinder, three groups.",                f18_approach_latency,                 "Approach latency to the ambiguous cylinder"),
    ("06-pattern-recognition-and-perception.md",  "01", "discrim-general",            "Discrimination–generalization tension in representational space.",                  f19_discrim_general_2d,               "the discrimination-generalization tension illustrated"),
    ("06-pattern-recognition-and-perception.md",  "02", "phylo-pallium",              "Three-layer pallial blueprint across vertebrate phylogeny.",                         f20_phylo_pallium,                    "simplified phylogenetic tree from lamprey to fish"),
    ("06-pattern-recognition-and-perception.md",  "03", "odor-completion",            "Pattern completion in piriform cortex — Odor A.",                                   f21_odor_completion,                  "two-panel diagram of the Odor A completion example"),
    ("06-pattern-recognition-and-perception.md",  "04", "goldfish-rotation",          "Goldfish recognition across rotations.",                                            f22_goldfish_rotation,                "bar chart of goldfish response times"),
    ("07-navigation-and-spatial-intelligence.md", "01", "saltpan-path",               "Cataglyphis path integration — outward zigzag, homeward straight.",                 f23_saltpan_path,                     "overhead view of a Tunisian saltpan"),
    ("07-navigation-and-spatial-intelligence.md", "02", "place-grid-hd",              "Hippocampal–entorhinal coordinate system — place, grid, head-direction cells.",     f24_place_grid_hd_cells,              "three-panel figure — panel 1 shows a rat arena"),
    ("07-navigation-and-spatial-intelligence.md", "03", "fmri-routing",               "fMRI activity — self-routing scales with route complexity; GPS following does not.", f25_fmri_routing,                    "side-by-side fMRI activation bar charts"),
    ("08-reinforcement-and-prediction.md",        "01", "dopamine-three-panels",      "Schultz dopamine — the reward-prediction-error signature.",                          f26_dopamine_three_panels,            "Dopamine neuron firing rate"),
    ("08-reinforcement-and-prediction.md",        "02", "td-equation",                "Temporal-difference error — local computation across two time steps.",              f27_td_equation,                      "Visual decomposition of the TD error equation"),
    ("08-reinforcement-and-prediction.md",        "03", "actor-critic",               "Actor–critic in the basal ganglia.",                                                f28_actor_critic,                     "Actor-critic architecture in the basal ganglia"),
    ("08-reinforcement-and-prediction.md",        "04", "reward-spec-gap",            "The reward specification gap — proxy vs. underlying goal.",                          f29_reward_spec_gap,                  "The reward specification gap"),
    ("09-simulation-and-planning.md",             "01", "replay",                     "Hippocampal replay — forward (planning) and reverse (credit).",                     f30_replay,                            "two-panel schematic of forward and reverse hippocampal replay"),
    ("09-simulation-and-planning.md",             "02", "convergent-simulation",      "Convergent evolution of mental simulation in mammals and corvids.",                  f31_convergent_simulation,             "convergent evolution of simulation"),
    ("10-social-and-emotional-intelligence.md",   "01", "three-layers-phylo",         "Phylogenetic distribution of social-cognitive layers.",                              f32_three_layers_phylo,                "phylogenetic distribution of the three layers"),
    ("10-social-and-emotional-intelligence.md",   "02", "hare-vs-sallyanne",          "Hare paradigm vs. Sally-Anne — what each test isolates.",                           f33_hare_vs_sallyanne,                 "two-panel comparison of what the Hare paradigm tests"),
    ("10-social-and-emotional-intelligence.md",   "03", "von-economo",                "Von Economo neurons — independent appearance in three lineages.",                   f34_von_economo,                       "three-branch evolutionary tree showing the primate, cetacean, and elephant"),
    ("11-theory-of-mind.md",                      "01", "sally-anne",                 "The Sally-Anne false-belief task.",                                                  f35_sally_anne,                        "The Sally-Anne false-belief task"),
    ("11-theory-of-mind.md",                      "02", "irl-tom",                    "Inverse reinforcement learning as theory of mind.",                                  f36_irl_tom,                           "Inverse reinforcement learning as theory of mind"),
    ("12-creativity.md",                          "01", "crow-tools",                 "New Caledonian crow tools — sequential modification of raw materials.",             f37_crow_tools,                       "side-by-side photographs or illustrations of New Caledonian crow tool"),
    ("12-creativity.md",                          "02", "bowerbird-court",            "Great bowerbird — forced perspective court layout.",                                f38_bowerbird,                        "diagram of great bowerbird bower court layout"),
    ("12-creativity.md",                          "03", "individual-vs-cumulative",   "Individual creativity vs. cumulative culture — two distinct loops.",                f39_individual_vs_cumulative,         "individual creativity vs. cumulative creativity"),
    ("13-self-awareness.md",                      "01", "three-rings",                "Three concentric subsystems of the self — body, social, narrative.",                f40_three_rings,                       "three concentric rings labeled body self"),
    ("13-self-awareness.md",                      "02", "mirror-decision-tree",       "Decision tree — interpreting a mirror-test failure.",                               f41_mirror_decision_tree,              "decision tree for interpreting a mirror test failure"),
    ("13-self-awareness.md",                      "03", "clinical-dissociation",      "Clinical dissociations — body-self decomposes into independent components.",        f42_clinical_dissociation,             "two-panel clinical dissociation figure"),
    ("14-metacognition.md",                       "01", "hampton-accuracy",           "Hampton 2001 — chosen vs. forced trials across delays.",                            f43_hampton_accuracy,                  "Hampton 2001 accuracy cross-check"),
    ("14-metacognition.md",                       "02", "metacog-timeline",           "Metacognition across 600 million years of evolution.",                              f44_metacog_timeline,                  "Metacognition across 600 million years of evolution"),
    ("15-language.md",                            "01", "language-curriculum",        "Language acquisition — proto-conversation to recursive grammar.",                   f45_language_curriculum,               "timeline of the language acquisition curriculum"),
    ("16-collective-intelligence.md",             "01", "collective-timeline",        "Three mechanisms of collective intelligence.",                                       f46_collective_timeline,               "timeline showing the three mechanisms"),
    ("16-collective-intelligence.md",             "02", "swarm-decision",             "Honeybee swarm decision — quality-weighted positive feedback with stop signals.",   f47_swarm_decision,                    "four-panel schematic of the swarm decision mechanism"),
    ("17-ai-as-data-point.md",                    "01", "geirhos-cue-conflict",       "Geirhos cue-conflict — texture beats shape in ImageNet-trained CNNs.",              f48_geirhos_cue_conflict,              "Side-by-side pair from the Geirhos cue-conflict stimuli"),
    ("17-ai-as-data-point.md",                    "02", "ai-radar-profile",           "AI cognitive profile — extreme highs and extreme lows.",                            f49_radar_profile,                     "AI cognitive profile across five axes"),
    ("18-extended-mind.md",                       "01", "extension-asymmetry",        "Extension asymmetry — capacity extended, direction retained.",                       f50_extension_asymmetry,               "the asymmetry between capacity-extended and direction-retained"),
    ("19-epilogue-what-the-nematode-knows.md",    "01", "celegans-anatomy",           "Caenorhabditis elegans — anatomical landmarks.",                                    f51_celegans_micrograph,               "photomicrograph or high-quality illustration of C. elegans"),
    ("19-epilogue-what-the-nematode-knows.md",    "02", "celegans-radar",             "C. elegans across the book's 14 cognitive axes.",                                   f52_celegans_radar,                    "radar/spider chart of C. elegans on the book"),
    ("19-epilogue-what-the-nematode-knows.md",    "03", "map-vs-ladder",              "Scala naturae vs. the actual map.",                                                  f53_map_vs_ladder,                     "the map vs. the ladder"),
]


def chapter_slug(filename):
    return filename.replace(".md", "")


def render_all():
    rendered = 0
    replaced = 0
    skipped = []
    for entry in FIGURES:
        filename, fnum, slug, title_text, builder, target_substr = entry
        cs = chapter_slug(filename)
        full_slug = f"{cs}-fig-{fnum}"
        svg = builder()
        svg_path = IMAGES / f"{full_slug}.svg"
        png_path = IMAGES / f"{full_slug}.png"
        svg_path.write_text(svg)
        try:
            import cairosvg
            m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
            if m:
                vw = int(m.group(1))
                vh = int(m.group(2))
                cairosvg.svg2png(
                    bytestring=svg.encode('utf-8'),
                    write_to=str(png_path),
                    output_width=vw * 2,
                    output_height=vh * 2,
                )
            else:
                cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=str(png_path))
        except Exception as e:
            print(f"  PNG fail {full_slug}: {e}")
        rendered += 1
        # Replace the comment in chapter
        chapter_path = CHAPTERS / filename
        text_ = chapter_path.read_text()
        replacement = (
            f'![{title_text}](../images/{full_slug}.png)\n\n'
            f'*Figure {int(fnum)} — {title_text}*\n'
        )
        pat = re.compile(
            r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM|INFOGRAPHIC|CHART):.*?'
            + re.escape(target_substr)
            + r'.*?-->',
            re.DOTALL,
        )
        m2 = pat.search(text_)
        if m2:
            text_ = text_[:m2.start()] + replacement + text_[m2.end():]
            chapter_path.write_text(text_)
            replaced += 1
        else:
            skipped.append(f"{filename}#{fnum} — substring not found: {target_substr[:60]}")
    print(f"rendered: {rendered} figures (SVG+PNG)")
    print(f"replaced: {replaced} tokens in chapters")
    if skipped:
        print(f"skipped (token not found): {len(skipped)}")
        for sk in skipped:
            print(f"  - {sk}")


if __name__ == "__main__":
    render_all()
