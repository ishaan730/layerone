"""Covers for the writing library, in the same style as blog_art.py: graphite or signal orange, the star mark,
mono labels, and one diagram per article that says what the article is about.
Renders assets/images/writing/<slug>.jpg (1600 × 900). Run: python3 tools/covers/writing_art.py (needs playwright)."""
import base64, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_art import INK, RAISED, SUNK, RULE, MUTED, PAPER, SIG, SANS, MONO, star, frame, ROOT  # noqa: E402

OUT = os.path.join(ROOT, "assets", "images", "writing")
DATA = os.path.join(ROOT, "tools", "build", "content", "writing", "data")
MINT, LAV = "#9de7c8", "#cfcbff"


def box(x, y, w, h, fill=SUNK, stroke=RULE, rx=8, sw=2, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def text(x, y, t, size=26, fill=PAPER, font=MONO, anchor="start", weight=400):
    return f'<text x="{x}" y="{y}" {font} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{t}</text>'


def bar(x, y, w, h=12, fill=MUTED, op=.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{fill}" opacity="{op}"/>'


def what_is():
    # Three layers: decisions, parts, agreements
    b = ""
    labels = [("decisions/", "tokens · colour · type · space", SIG), ("parts/", "components · patterns", PAPER), ("agreements/", "owners · requests · releases", MUTED)]
    for i, (k, v, c) in enumerate(labels):
        y = 190 + i * 190
        b += box(104 + i * 40, y, 1100, 150, SUNK if i else RAISED, c if i == 0 else RULE, sw=3 if i == 0 else 2)
        b += text(150 + i * 40, y + 66, k, 34, c) + text(150 + i * 40, y + 112, v, 24, MUTED)
    b += box(1290, 230, 210, 430, "none", SIG, sw=3) + star(1345, 395, 100, SIG)
    return frame(INK, b, label="writing / fundamentals")


def versus():
    # Nested rounded rectangles
    b = ""
    names = [("design system", SIG, 3), ("component library", PAPER, 2), ("ui kit", MUTED, 2), ("style guide", MUTED, 2)]
    for i, (n, c, w) in enumerate(names):
        x, y = 104 + i * 110, 150 + i * 90
        b += f'<rect x="{x}" y="{y}" width="{1392 - i * 220}" height="{660 - i * 180}" rx="18" fill="none" stroke="{c}" stroke-width="{w}" stroke-dasharray="{"" if i == 0 else "10 10"}"/>'
        b += text(x + 28, y + 48, n, 28, c)
    return frame(INK, b, label="writing / fundamentals")


def need():
    # A decision tree: question → yes / not yet
    b = box(600, 160, 400, 110, RAISED, SIG, sw=3) + text(800, 228, "need a system?", 30, PAPER, anchor="middle")
    b += f'<path d="M800 270V340H400V420M800 340H1200V420" fill="none" stroke="{RULE}" stroke-width="3"/>'
    b += box(250, 420, 300, 100, SIG, SIG) + text(400, 482, "yes: start", 28, INK, anchor="middle")
    b += box(1050, 420, 300, 100, SUNK, RULE) + text(1200, 482, "not yet", 28, MUTED, anchor="middle")
    for i, t in enumerate(["teams > 3", "products > 1", "rebuilds"]):
        b += box(160 + i * 160, 600, 140, 56, "none", RULE, rx=28) + text(230 + i * 160, 636, t, 18, MUTED, anchor="middle")
    for i, t in enumerate(["one team", "pivoting", "no owner"]):
        b += box(960 + i * 160, 600, 140, 56, "none", RULE, rx=28) + text(1030 + i * 160, 636, t, 18, MUTED, anchor="middle")
    return frame(INK, b, label="writing / fundamentals")


def build():
    # Stages on a 12-month track, with gates
    b = f'<path d="M120 640H1480" stroke="{RULE}" stroke-width="4"/>'
    steps = ["audit", "tokens", "components", "docs", "govern", "scale"]
    for i, s in enumerate(steps):
        x = 150 + i * 225
        h = 120 + i * 60
        b += box(x, 620 - h, 180, h, SIG if i == 2 else SUNK, SIG if i == 2 else RULE) + text(x + 20, 620 - h + 46, s, 24, INK if i == 2 else PAPER)
        b += f'<circle cx="{x + 90}" cy="640" r="12" fill="{SIG if i < 3 else RAISED}" stroke="{SIG}" stroke-width="3"/>'
    for m in range(12):
        b += text(150 + m * 112, 700, f"m{m + 1}", 16, MUTED)
    return frame(INK, b, label="writing / building")


def audit():
    # A wall of inconsistent buttons, counted
    b = ""
    blues = ["#4c6ef5", "#3b5bdb", "#5c7cfa", "#364fc7", "#4263eb"]
    for r in range(4):
        for c in range(6):
            x, y = 104 + c * 176, 180 + r * 120
            col = blues[(r * 6 + c) % 5] if (r + c) % 3 else SIG
            b += box(x, y, 140 + (c % 3) * 6, 56 + (r % 2) * 8, col, "none", rx=4 + (c % 4) * 6) + bar(x + 24, y + 22, 70, 12, PAPER, .9)
    b += box(1200, 180, 296, 470, RAISED, SIG, sw=3)
    for i, (k, v) in enumerate([("buttons", "24"), ("blues", "5"), ("radii", "4"), ("heights", "2")]):
        b += text(1230, 250 + i * 104, k, 22, MUTED) + text(1466, 250 + i * 104, v, 40, SIG, anchor="end")
    return frame(INK, b, label="writing / building")


def tokens():
    # primitive → semantic → component
    cols = [("primitive", ["brand.600", "neutral.50", "space.4"]), ("semantic", ["action.primary", "action.text", "inset.md"]), ("component", ["button.bg", "button.label", "button.padding"])]
    b = ""
    for i, (k, rows) in enumerate(cols):
        x = 104 + i * 480
        b += text(x, 200, k + "/", 28, SIG if i == 1 else MUTED)
        for j, r in enumerate(rows):
            y = 240 + j * 150
            b += box(x, y, 420, 110, RAISED if i == 1 else SUNK, SIG if i == 1 else RULE, sw=2)
            b += f'<rect x="{x + 24}" y="{y + 31}" width="48" height="48" rx="8" fill="{[SIG, PAPER, MUTED][j]}"/>' + text(x + 96, y + 66, r, 24, PAPER)
            if i < 2:
                b += f'<path d="M{x + 420} {y + 55}H{x + 480}" stroke="{SIG}" stroke-width="3"/>'
    return frame(INK, b, label="writing / tokens")


def dark_mode():
    # The same card, light and dark, split down the middle
    b = f'<rect x="104" y="160" width="696" height="620" rx="12" fill="#f3f7fe"/><rect x="800" y="160" width="696" height="620" rx="12" fill="#1e232c"/>'
    for x, bg, tx, sub, act, acttx in ((104, "#f3f7fe", "#1e232c", "#595f69", "#ab2800", "#f3f7fe"), (800, "#1e232c", "#f3f7fe", "#bcc3ce", "#ff7951", "#1e232c")):
        b += text(x + 60, 280, "Invoice #2041", 44, tx, SANS, weight=600) + text(x + 60, 330, "Due 12 March · 3 items", 26, sub, SANS)
        b += box(x + 60, 390, 560, 70, "#ffe1dc" if x == 104 else "#67080f", "none") + text(x + 90, 434, "Payment overdue", 24, "#b3081d" if x == 104 else "#ffa198", SANS, weight=500)
        b += box(x + 60, 520, 220, 76, act, "none") + text(x + 170, 568, "Pay now", 26, acttx, SANS, "middle", 600)
        b += text(x + 60, 700, "bg.canvas · text.primary · action.primary", 18, sub)
    b += f'<path d="M800 130V810" stroke="{SIG}" stroke-width="4" stroke-dasharray="10 10"/>'
    return frame(INK, b, label="writing / tokens")


def oklch():
    p = json.load(open(os.path.join(DATA, "palette.json")))
    b = ""
    for i, r in enumerate(p["ramps"]):
        for j, s in enumerate(r["steps"]):
            b += f'<rect x="{104 + j * 127}" y="{170 + i * 100}" width="117" height="84" rx="8" fill="{s["hex"]}"/>'
    b += text(104, 820, "oklch(L C H) · one lightness curve · six hues", 24, MUTED)
    return frame(INK, b, label="writing / colour")


def governance():
    # Decision-rights grid
    rows = ["principles", "tokens", "components", "patterns", "breaking change"]
    cols = ["decides", "approves", "consulted"]
    b = ""
    for j, c in enumerate(cols):
        b += text(560 + j * 300, 210, c, 24, MUTED)
    for i, r in enumerate(rows):
        y = 250 + i * 104
        b += text(104, y + 50, r, 26, PAPER) + f'<path d="M104 {y + 84}H1496" stroke="{RULE}" stroke-width="2"/>'
        for j in range(3):
            on = (i + j) % 3 == 0
            if j == 0 or on:
                b += f'<circle cx="{600 + j * 300}" cy="{y + 40}" r="{22 if j == 0 else 14}" fill="{SIG if j == 0 else "none"}" stroke="{SIG if j == 0 else MUTED}" stroke-width="3"/>'
    return frame(INK, b, label="writing / governance")


def team():
    # Org chart
    b = box(650, 160, 300, 100, SIG, "none") + text(800, 220, "system lead", 26, INK, anchor="middle")
    b += f'<path d="M800 260V330M260 330H1340M260 330V380M620 330V380M980 330V380M1340 330V380" fill="none" stroke="{RULE}" stroke-width="3"/>'
    for i, t in enumerate(["designers", "web eng", "native eng", "a11y + docs"]):
        x = 140 + i * 360
        b += box(x, 380, 240, 90, SUNK, RULE) + text(x + 120, 434, t, 22, PAPER, anchor="middle")
    b += f'<path d="M140 560H1460" stroke="{SIG}" stroke-width="2" stroke-dasharray="8 10"/>' + text(140, 610, "champions in every product team", 22, SIG)
    for i in range(10):
        b += f'<circle cx="{180 + i * 132}" cy="700" r="30" fill="none" stroke="{MUTED}" stroke-width="2"/>'
    return frame(INK, b, label="writing / operations")


def operating():
    # A loop: intake → triage → build → release → support
    import math
    names = ["intake", "triage", "build", "release", "support", "measure"]
    cx, cy, R = 800, 480, 270
    b = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 12"/>'
    for i, n in enumerate(names):
        a = -math.pi / 2 + i * 2 * math.pi / len(names)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        b += box(x - 95, y - 40, 190, 80, INK, "none") + text(x, y + 9, n, 24, SIG if i == 0 else PAPER, anchor="middle")
    b += star(cx - 60, cy - 60, 120, INK)
    return frame(SIG, b, ink=INK, label="writing / operations")


def contribution():
    # A funnel of requests into a scored queue
    b = ""
    for i in range(9):
        b += box(104 + (i % 3) * 150, 170 + (i // 3) * 110, 120, 72, SUNK, RULE) + bar(124 + (i % 3) * 150, 198 + (i // 3) * 110, 70)
    b += f'<path d="M600 300H700M690 290L700 300L690 310" stroke="{SIG}" stroke-width="3" fill="none"/>' + box(720, 200, 200, 200, "none", SIG, rx=100, sw=3) + text(820, 312, "score", 28, SIG, anchor="middle")
    b += f'<path d="M940 300H1040" stroke="{SIG}" stroke-width="3"/>'
    for i, (n, s) in enumerate([("dialog focus bug", "12.0"), ("filter pattern", "5.0"), ("date range", "3.5"), ("editable grid", "2.3")]):
        y = 170 + i * 120
        b += box(1060, y, 436, 90, SIG if i == 0 else SUNK, "none") + text(1084, y + 54, n, 22, INK if i == 0 else PAPER) + text(1472, y + 54, s, 26, INK if i == 0 else SIG, anchor="end")
    b += text(104, 760, "(reach + impact + reuse + value) ÷ effort", 26, MUTED)
    return frame(INK, b, label="writing / governance")


def docs():
    # A docs page wireframe
    b = box(104, 160, 300, 640, SUNK, RULE)
    for i in range(9):
        b += bar(134, 200 + i * 56, 140 + (i % 3) * 40, 14, MUTED if i != 3 else SIG, .5 if i != 3 else 1)
    b += box(440, 160, 1056, 640, RAISED, RULE)
    b += text(480, 240, "Button", 48, PAPER, SANS, weight=600) + bar(480, 270, 520, 14)
    b += box(480, 320, 976, 200, SUNK, "none") + box(560, 390, 200, 64, SIG, "none") + box(800, 390, 200, 64, "none", PAPER)
    for i, t in enumerate(["usage", "do / don't", "accessibility", "props", "changelog"]):
        b += box(480 + i * 196, 560, 180, 52, "none", SIG if i == 1 else RULE, rx=26) + text(570 + i * 196, 594, t, 18, SIG if i == 1 else MUTED, anchor="middle")
    for i in range(3):
        b += bar(480, 660 + i * 36, 820 - i * 140)
    return frame(INK, b, label="writing / documentation")


def metrics():
    # A dashboard: four tiles
    b = ""
    tiles = [("adoption", "68%", "+4"), ("first response", "2 days", ""), ("hard-coded colours", "−38%", ""), ("“makes me faster”", "71%", "+9")]
    for i, (k, v, d) in enumerate(tiles):
        x, y = 104 + (i % 2) * 706, 170 + (i // 2) * 320
        b += box(x, y, 686, 290, RAISED if i else SIG, RULE if i else "none")
        c = INK if not i else PAPER
        b += text(x + 36, y + 64, k, 24, INK if not i else MUTED) + text(x + 36, y + 190, v, 96, c, SANS, weight=500)
        if i == 0:
            for j, h in enumerate([40, 52, 60, 68]):
                b += f'<rect x="{x + 470 + j * 44}" y="{y + 240 - h * 2}" width="30" height="{h * 2}" rx="4" fill="{INK}" opacity="{.4 + j * .2}"/>'
    return frame(INK, b, label="writing / measurement")


def roi():
    e = json.load(open(os.path.join(DATA, "economics.json")))
    b = f'<path d="M104 760H1496" stroke="{RULE}" stroke-width="3"/>'
    mx = 340000
    for i, y in enumerate(e["years"]):
        x = 200 + i * 430
        hv, hc = y["usd"] / mx * 520, y["cost"] / mx * 520
        b += f'<rect x="{x}" y="{760 - hc}" width="140" height="{hc}" rx="6" fill="{RAISED}" stroke="{MUTED}" stroke-width="2"/>'
        b += f'<rect x="{x + 160}" y="{760 - hv}" width="140" height="{hv}" rx="6" fill="{SIG}"/>'
        b += text(x + 150, 812, f"year {y['year']}", 24, MUTED, anchor="middle")
    yy = 760 - 288000 / mx * 520
    b += f'<path d="M104 {yy}H1496" stroke="{PAPER}" stroke-width="2" stroke-dasharray="8 10"/>' + text(120, yy - 16, "cost line: 2 FTE a year", 22, PAPER)
    return frame(INK, b, label="writing / business case")


ART = {"what-is-a-design-system": what_is, "design-system-vs-style-guide-vs-component-library": versus, "do-you-need-a-design-system": need,
       "how-to-build-a-design-system": build, "design-system-audit": audit, "design-tokens": tokens, "dark-mode-design-tokens": dark_mode,
       "oklch-color-palette": oklch, "design-system-governance": governance, "design-system-team-structure": team,
       "design-system-operating-model": operating, "design-system-contribution-model": contribution, "design-system-documentation": docs,
       "design-system-metrics": metrics, "design-system-roi": roi}


def maturity():
    b = ""
    names = ["unwritten", "shared styles", "basics in code", "looked after", "platform"]
    for i, n in enumerate(names):
        x, h = 130 + i * 270, 120 + i * 110
        on = i == 2
        b += box(x, 740 - h, 230, h, SIG if on else SUNK, "none" if on else RULE) + text(x + 22, 740 - h + 50, f"{i}", 34, INK if on else SIG) + text(x + 22, 740 - h + 92, n, 20, INK if on else PAPER)
    b += f'<path d="M110 760H1490" stroke="{RULE}" stroke-width="3"/>'
    return frame(INK, b, label="writing / fundamentals")


def versioning():
    b = ""
    for i, (v, t, c) in enumerate([("4.2.1", "fix", MUTED), ("4.3.0", "new", PAPER), ("4.6.0", "deprecate", PAPER), ("5.0.0", "breaking", SIG)]):
        x = 130 + i * 350
        b += f'<circle cx="{x + 60}" cy="450" r="{22 if i < 3 else 32}" fill="{SIG if i == 3 else RAISED}" stroke="{c}" stroke-width="3"/>'
        b += text(x + 60, 380, v, 34, c, anchor="middle") + text(x + 60, 540, t, 22, MUTED if i < 3 else SIG, anchor="middle")
    b = f'<path d="M190 450H1240" stroke="{RULE}" stroke-width="4" stroke-dasharray="12 10"/>' + b
    b += text(104, 760, "major . minor . patch", 26, MUTED)
    return frame(INK, b, label="writing / governance")


def naming():
    parts = [("color", SIG), ("action", PAPER), ("primary", PAPER), ("bg", PAPER), ("hover", MUTED)]
    b, x = "", 130
    for i, (p, c) in enumerate(parts):
        w = len(p) * 26 + 70
        b += box(x, 340, w, 110, RAISED if i else "none", c, sw=3 if i == 0 else 2) + text(x + w / 2, 408, p, 34, c, anchor="middle")
        if i < len(parts) - 1:
            b += text(x + w + 20, 410, ".", 50, MUTED, anchor="middle")
        x += w + 40
    for i, t in enumerate(["category", "concept", "variant", "property", "state"]):
        b += text(130 + i * 260, 540, t, 20, MUTED)
    return frame(INK, b, label="writing / tokens")


def spacing():
    vals = [4, 8, 12, 16, 24, 32, 48, 64, 96]
    b, x = "", 130
    for v in vals:
        w = v * 4
        b += f'<rect x="{x}" y="{620 - v * 4}" width="{w * 0.55}" height="{v * 4}" rx="4" fill="{SIG if v in (8, 16, 24, 32) else SUNK}" stroke="{RULE}"/>' + text(x, 660, f"{v}", 20, MUTED)
        x += w * 0.55 + 36
    b += text(104, 780, "4px base · 8px rhythm", 26, MUTED)
    return frame(INK, b, label="writing / foundations")


def typescale():
    b, x = "", 120
    for s in [14, 16, 20, 25, 31, 39, 49]:
        b += f'<text x="{x}" y="560" font-family="Schibsted Grotesk" font-weight="600" font-size="{s * 2.4:.0f}" fill="{SIG if s == 16 else PAPER}" letter-spacing="-2">Aa</text>'
        b += text(x, 640, f"{s}", 20, MUTED)
        x += s * 2.4 * 1.15 + 34
    b += f'<path d="M110 580H1490" stroke="{RULE}" stroke-width="2"/>' + text(104, 780, "base 16 · ratio 1.25", 26, MUTED)
    return frame(INK, b, label="writing / foundations")


def contrast():
    import json as _json
    c = _json.load(open(os.path.join(DATA, "contrast-matrix.json")))
    b = ""
    for i, row in enumerate(c["neutral"]):
        for j, v in enumerate(row):
            fill = "#12352a" if v >= 4.5 else ("#10283f" if v >= 3 else SUNK)
            b += f'<rect x="{400 + j * 74}" y="{150 + i * 56}" width="68" height="50" rx="6" fill="{fill}"/>'
            if i != j:
                b += text(434 + j * 74, 182 + i * 56, f"{v:.1f}", 15, "#9de7c8" if v >= 4.5 else ("#8ec6ff" if v >= 3 else MUTED), anchor="middle")
    b += text(104, 220, "4.5 : 1", 54, SIG, SANS, weight=600) + text(104, 270, "text", 22, MUTED) + text(104, 380, "3 : 1", 54, PAPER, SANS, weight=600) + text(104, 430, "borders · icons", 22, MUTED)
    return frame(INK, b, label="writing / accessibility")


def multibrand():
    b = box(560, 600, 480, 120, SIG, "none") + text(800, 672, "shared core", 30, INK, anchor="middle")
    for i, (n, col) in enumerate([("bank", "#ab2800"), ("insure", "#065db4"), ("lend", "#007628")]):
        x = 180 + i * 440
        b += box(x, 230, 360, 220, RAISED, RULE) + f'<rect x="{x + 30}" y="270" width="120" height="44" rx="8" fill="{col}"/>' + text(x + 30, 370, n, 26, PAPER) + text(x + 30, 410, "action.primary.bg", 18, MUTED)
        b += f'<path d="M{x + 180} 450L800 600" stroke="{RULE}" stroke-width="3"/>'
    return frame(INK, b, label="writing / scaling")


def buildfirst():
    b = f'<path d="M800 160V760M200 460H1400" stroke="{RULE}" stroke-width="3"/>'
    for x, y, t, hi in [(1030, 230, "button", True), (1180, 310, "field", True), (960, 360, "alert", True), (1250, 200, "dialog", True), (420, 240, "date picker", False), (500, 600, "one-off", False), (1100, 620, "badge", False)]:
        b += f'<circle cx="{x}" cy="{y}" r="16" fill="{SIG if hi else MUTED}"/>' + text(x + 28, y + 8, t, 22, PAPER if hi else MUTED)
    b += box(860, 170, 520, 270, "none", SIG, sw=3, extra='stroke-dasharray="10 10"') + text(880, 160, "build first", 22, SIG)
    b += text(1400, 800, "used more →", 20, MUTED, anchor="end") + text(210, 180, "↑ more trouble", 20, MUTED)
    return frame(INK, b, label="writing / building")


def headless():
    b = box(160, 230, 560, 440, "none", RULE, extra='stroke-dasharray="10 10"') + text(190, 280, "behaviour (borrowed)", 24, MUTED)
    for i, t in enumerate(["keyboard", "focus", "aria", "state"]):
        b += box(200, 320 + i * 82, 300, 60, SUNK, RULE) + text(225, 358 + i * 82, t, 22, PAPER)
    b += text(800, 460, "+", 70, SIG, anchor="middle")
    b += box(880, 230, 560, 440, RAISED, SIG, sw=3) + text(910, 280, "your tokens + API", 24, SIG)
    b += box(930, 340, 220, 64, SIG, "none") + text(1040, 381, "Button", 22, INK, anchor="middle") + box(930, 440, 420, 60, SUNK, RULE) + box(930, 530, 300, 60, "none", PAPER)
    return frame(INK, b, label="writing / building")


def complexity():
    b = ""
    for i, (n, sc) in enumerate([("badge", 2), ("button", 9), ("date picker", 17), ("data table", 22)]):
        y = 220 + i * 140
        b += text(130, y + 40, n, 26, PAPER) + box(420, y, 960, 60, SUNK, "none") + f'<rect x="420" y="{y}" width="{sc / 24 * 960:.0f}" height="60" rx="8" fill="{SIG if i == 2 else PAPER if i == 3 else MUTED}"/>' + text(1420, y + 42, f"{sc}", 30, SIG if i == 2 else PAPER, anchor="end")
    return frame(INK, b, label="writing / building")


def props():
    b = text(130, 300, '&lt;Button', 46, PAPER) + text(170, 380, 'variant=&quot;danger&quot;', 40, SIG) + text(170, 450, 'size=&quot;md&quot;', 40, PAPER) + text(170, 520, 'loading', 40, PAPER) + text(130, 600, '&gt;Delete&lt;/Button&gt;', 46, PAPER)
    b += box(960, 260, 440, 360, RAISED, RULE)
    for i, (k, v) in enumerate([("Variant", "Danger"), ("Size", "md"), ("Loading", "on")]):
        b += text(990, 330 + i * 90, k, 22, MUTED) + box(1180, 300 + i * 90, 190, 50, SUNK, SIG if i == 0 else RULE) + text(1200, 333 + i * 90, v, 22, PAPER)
    b += text(800, 460, "=", 70, MUTED, anchor="middle")
    return frame(INK, b, label="writing / components")


def officehours():
    b = ""
    days = ["mon", "tue", "wed", "thu", "fri"]
    for i, d in enumerate(days):
        x = 140 + i * 270
        b += text(x, 230, d, 24, MUTED) + box(x, 260, 230, 420, SUNK, RULE)
    b += box(410, 300, 230, 120, SIG, "none") + text(430, 350, "office hours", 22, INK) + text(430, 390, "60 min · open", 18, INK)
    b += box(950, 480, 230, 120, "none", SIG, sw=3) + text(970, 530, "second slot", 22, SIG) + text(970, 570, "other time zone", 18, MUTED)
    return frame(INK, b, label="writing / operations")


def releasenotes():
    b = box(280, 170, 1040, 600, RAISED, RULE) + text(320, 240, "4.6.0 is out", 40, PAPER, SANS, weight=600)
    for i, (k, c, w) in enumerate([("BREAKING", SIG, 600), ("NEW", "#9de7c8", 760), ("IMPROVED", PAPER, 520), ("FIXED", MUTED, 680)]):
        y = 320 + i * 100
        b += box(320, y, 170, 44, "none", c, rx=22) + text(405, y + 30, k, 18, c, anchor="middle") + bar(520, y + 16, w, 14, PAPER, .35)
    return frame(INK, b, label="writing / operations")


def champions():
    import math
    b = box(670, 370, 260, 120, SIG, "none") + text(800, 440, "system team", 24, INK, anchor="middle")
    for i in range(8):
        a = i * 2 * math.pi / 8
        x, y = 800 + 470 * math.cos(a), 430 + 260 * math.sin(a)
        b += f'<path d="M800 430L{x:.0f} {y:.0f}" stroke="{RULE}" stroke-width="2"/>'
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="{RAISED}" stroke="{SIG}" stroke-width="3"/>' + star(x - 14, y - 14, 28, SIG)
    b = b.replace(box(670, 370, 260, 120, SIG, "none") + text(800, 440, "system team", 24, INK, anchor="middle"), "") + box(670, 370, 260, 120, SIG, "none") + text(800, 440, "system team", 24, INK, anchor="middle")
    return frame(INK, b, label="writing / community")


def ai():
    b = ""
    steps = [("context", SUNK, PAPER), ("draft", SUNK, PAPER), ("review", SIG, INK), ("publish", SUNK, PAPER), ("check", SUNK, PAPER)]
    for i, (t, f, c) in enumerate(steps):
        x = 130 + i * 280
        b += box(x, 380, 220, 110, f, RULE if f == SUNK else "none") + text(x + 110, 445, t, 26, c, anchor="middle")
        if i < 4:
            b += f'<path d="M{x + 225} 435H{x + 275}" stroke="{SIG}" stroke-width="3"/>'
    b += text(130, 300, "ai drafts", 22, MUTED) + text(690, 300, "people decide", 22, SIG)
    return frame(INK, b, label="writing / tooling")


ART.update({"design-system-maturity-model": maturity, "design-system-versioning": versioning, "design-token-naming-conventions": naming,
            "spacing-system-4px-vs-8px": spacing, "type-scale-design-system": typescale, "color-contrast-design-system": contrast,
            "multi-brand-design-system": multibrand, "which-components-to-build-first": buildfirst,
            "headless-component-library-build-vs-buy": headless, "component-complexity": complexity, "component-props-best-practices": props,
            "design-system-office-hours": officehours, "design-system-release-notes": releasenotes, "design-system-champions": champions,
            "ai-in-design-systems": ai})


def patterns():
    # words (components) combine into a sentence (pattern)
    b = ""
    for i, t in enumerate(["field", "select", "chip", "button"]):
        x = 150 + i * 330
        b += box(x, 210, 270, 90, SUNK, RULE) + text(x + 135, 266, t, 26, PAPER, anchor="middle")
        b += f'<path d="M{x + 135} 310V420" stroke="{RULE}" stroke-width="2" stroke-dasharray="6 8"/>'
    b += box(150, 440, 1260, 200, RAISED, SIG, sw=3) + text(190, 500, "pattern / filter bar", 24, SIG)
    for i, w in enumerate([300, 240, 150, 150, 200]):
        x = 190 + sum([300, 240, 150, 150, 200][:i]) + i * 24
        b += box(x, 540, w, 60, SIG if i == 4 else SUNK, "none" if i == 4 else RULE, rx=30 if i in (2, 3) else 8)
    return frame(INK, b, label="writing / patterns")


def forms():
    b = box(440, 140, 720, 640, RAISED, RULE)
    b += box(480, 180, 640, 110, "none", SIG, sw=3) + text(510, 225, "2 problems", 24, PAPER, SANS, weight=600) + bar(510, 252, 360, 12, SIG, .7)
    for i, (lab, err) in enumerate([("customer email", True), ("due date", True), ("po number (optional)", False)]):
        y = 330 + i * 140
        b += text(480, y, lab, 22, PAPER if err else MUTED)
        if err:
            b += f'<rect x="466" y="{y - 30}" width="4" height="120" fill="{SIG}"/>' + bar(480, y + 18, 340, 12, SIG, .8)
        b += box(480, y + (44 if err else 20), 640, 50, SUNK, SIG if err else RULE)
    b += box(480, 720, 220, 40, SIG, "none", rx=6) + text(590, 747, "Send invoice", 20, INK, anchor="middle")
    return frame(INK, b, label="writing / patterns")


def uxwriting():
    b = ""
    words = [("Delete", "permanent · confirmed", SIG), ("Archive", "hidden · can be restored", PAPER), ("Remove", "out of a list · not deleted", PAPER)]
    for i, (w, m, c) in enumerate(words):
        y = 200 + i * 180
        b += box(140, y, 1320, 140, RAISED if i == 0 else SUNK, SIG if i == 0 else RULE, sw=3 if i == 0 else 2)
        b += text(190, y + 88, w, 52, c, SANS, weight=700) + text(640, y + 84, m, 28, MUTED)
    b += text(1420, 255, "not: discard, erase", 20, MUTED, anchor="end")
    return frame(INK, b, label="writing / content")


def grid():
    b = ""
    cols, x0, w, g = 12, 150, 1300, 16
    cw = (w - g * (cols - 1)) / cols
    for i in range(cols):
        b += f'<rect x="{x0 + i * (cw + g):.1f}" y="160" width="{cw:.1f}" height="600" fill="{SUNK}" opacity=".9"/>'
    def span(c0, n, y, h, fill, op=1):
        return f'<rect x="{x0 + c0 * (cw + g):.1f}" y="{y}" width="{n * cw + (n - 1) * g:.1f}" height="{h}" rx="8" fill="{fill}" opacity="{op}"/>'
    for i in range(4):
        b += span(i * 3, 3, 200, 130, SIG if i == 0 else PAPER, 1 if i == 0 else .85)
    b += span(0, 9, 360, 240, MUTED, .55) + span(9, 3, 360, 240, PAPER, .5) + span(0, 12, 630, 100, MUTED, .35)
    b += text(150, 140, "12 columns · 16px gutters", 22, MUTED)
    return frame(INK, b, label="writing / foundations")


def rtl():
    b = ""
    for side, x, lab in [(0, 130, "ltr"), (1, 830, "rtl")]:
        b += box(x, 200, 640, 520, RAISED, SIG if side else RULE, sw=3 if side else 2) + text(x + 30, 180, lab, 22, SIG if side else MUTED)
        ic = x + 40 if not side else x + 560
        bt = x + 430 if not side else x + 40
        b += box(ic, 240, 40, 40, SUNK, RULE, rx=8) + box(bt, 236, 170, 48, SIG, "none") + bar(x + (110 if not side else 300), 254, 220, 14, PAPER, .8)
        for i in range(4):
            y = 340 + i * 90
            ex = x + 40 if not side else x + 596
            b += f'<rect x="{ex}" y="{y}" width="4" height="56" fill="{SIG if i == 0 else RULE}"/>'
            b += bar(x + (64 if not side else 336), y + 20, 240, 14, PAPER, .55) + bar(x + (480 if not side else 64), y + 20, 100, 14, MUTED, .7)
    return frame(INK, b, label="writing / foundations")


def twins():
    b = box(150, 220, 560, 460, RAISED, RULE) + text(180, 270, "figma", 24, MUTED)
    b += box(890, 220, 560, 460, RAISED, RULE) + text(920, 270, "code", 24, MUTED)
    for i, (k, v, c) in enumerate([("Variant", "Primary", "primary"), ("Size", "Medium", "md"), ("Type", "Tertiary", "ghost")]):
        y = 330 + i * 110
        bad = i == 2
        b += text(190, y + 32, k, 22, MUTED) + box(400, y, 270, 50, SUNK, SIG if bad else RULE) + text(420, y + 33, v, 22, PAPER)
        b += text(930, y + 33, f'{k.lower()}=&quot;{c}&quot;', 26, SIG if bad else PAPER)
        b += f'<path d="M720 {y + 25}H880" stroke="{SIG if bad else RULE}" stroke-width="3" {"stroke-dasharray=&quot;8 8&quot;" if bad else ""}/>'
    b += text(800, 760, "≠ drift", 28, SIG, anchor="middle")
    return frame(INK, b, label="writing / tooling")


def tooling():
    b = ""
    areas = ["design", "tokens", "code", "docs", "quality", "insight"]
    for i, t in enumerate(areas):
        x = 120 + i * 230
        hi = t == "tokens"
        b += box(x, 360, 190, 140, SIG if hi else SUNK, "none" if hi else RULE) + text(x + 95, 440, t, 26, INK if hi else PAPER, anchor="middle")
        if i < 5:
            b += f'<path d="M{x + 196} 430H{x + 226}" stroke="{SIG}" stroke-width="3"/>'
    for i, (t, w) in enumerate([("1 token pipeline", 380), ("2 lint rules", 300)]):
        b += box(120, 580 + i * 80, w, 54, "none", SIG, sw=3, rx=27) + text(150, 616 + i * 80, t, 22, SIG)
    b += text(120, 300, "automate first ↓", 22, MUTED)
    return frame(INK, b, label="writing / tooling")


def migration():
    b = ""
    labs = ["tokens", "visible parts", "screen by screen", "remove the old"]
    for i, t in enumerate(labs):
        x, y = 150 + i * 330, 640 - i * 120
        b += box(x, y, 300, 780 - y, SIG if i == 0 else SUNK, "none" if i == 0 else RULE)
        b += text(x + 24, y + 48, f"{i + 1}", 30, INK if i == 0 else SIG) + text(x + 24, y + 92, t, 24, INK if i == 0 else PAPER)
    b += text(150, 200, "legacy → system, in layers", 26, MUTED)
    return frame(INK, b, label="writing / governance")


def onboarding():
    b = ""
    steps = [("day 1", "welcome"), ("week 1", "45 min"), ("week 2", "starter task"), ("week 4", "office hours"), ("month 2", "check-in")]
    b += f'<path d="M180 450H1420" stroke="{RULE}" stroke-width="3"/>'
    for i, (k, v) in enumerate(steps):
        x = 180 + i * 310
        hi = i == 2
        b += f'<circle cx="{x}" cy="450" r="{26 if hi else 16}" fill="{SIG if hi else PAPER}"/>'
        b += text(x, 380, k, 22, MUTED, anchor="middle") + text(x, 530, v, 26 if hi else 22, SIG if hi else PAPER, anchor="middle")
    b += box(560, 590, 480, 120, "none", SIG, sw=3) + text(800, 662, "learn by doing", 26, SIG, anchor="middle")
    return frame(INK, b, label="writing / operations")


def research():
    b = text(140, 210, "pain-point log", 24, MUTED)
    rows = [("filtering is inconsistent", 12, True), ("can't find warning banner", 7, False), ("which alert do I use?", 6, False), ("too many toast styles", 4, False)]
    for i, (t, n, hi) in enumerate(rows):
        y = 250 + i * 120
        b += box(140, y, 860, 90, RAISED if hi else SUNK, SIG if hi else RULE, sw=3 if hi else 2) + text(180, y + 56, t, 26, PAPER if hi else MUTED)
        b += text(960, y + 58, f"{n} teams", 22, SIG if hi else MUTED, anchor="end")
    b += f'<path d="M1020 {370 + 0}C1120 370 1120 560 1200 560" stroke="{SIG}" stroke-width="3" fill="none"/>'
    b += box(1200, 500, 260, 120, SIG, "none") + text(1330, 570, "roadmap", 28, INK, anchor="middle")
    return frame(INK, b, label="writing / research")


ART.update({"design-system-patterns": patterns, "form-design-patterns": forms, "ux-writing-design-system": uxwriting,
            "layout-grid-breakpoints": grid, "design-system-localization-rtl": rtl, "figma-code-sync": twins,
            "design-system-tooling": tooling, "design-system-migration": migration, "design-system-onboarding": onboarding,
            "design-system-research": research})


def states():
    b = ""
    labs = [("default", RULE, PAPER), ("hover", MUTED, PAPER), ("focus", SIG, PAPER), ("disabled", RULE, MUTED), ("read-only", RULE, PAPER), ("error", "#ff8a7a", PAPER), ("empty", RULE, MUTED), ("loading", RULE, MUTED)]
    for i, (t, st, tx) in enumerate(labs):
        x, y = 130 + (i % 4) * 340, 230 + (i // 4) * 250
        b += text(x, y, t, 20, SIG if t == "focus" else MUTED)
        if t == "focus":
            b += box(x - 6, y + 18, 312, 92, "none", SIG, rx=14, sw=2, extra='opacity=".45"')
        b += box(x, y + 24, 300, 80, SUNK if t in ("disabled", "read-only") else INK, st, sw=3 if t in ("focus", "error") else 2, extra='stroke-dasharray="8 6"' if t == "read-only" else "")
        if t == "loading":
            b += bar(x + 24, y + 58, 150, 12, MUTED, .5) + bar(x + 190, y + 58, 70, 12, MUTED, .35)
        else:
            b += text(x + 24, y + 74, "Customer name" if t == "empty" else "Acme Ltd", 24, tx)
    return frame(INK, b, label="writing / components")


def composition():
    b = box(150, 200, 560, 520, SUNK, RULE)
    for i in range(9):
        b += bar(190, 250 + i * 50, 300 + (i % 3) * 60, 14, MUTED, .5) + f'<circle cx="640" cy="{257 + i * 50}" r="10" fill="{SIG if i % 4 == 0 else MUTED}" opacity=".7"/>'
    b += text(170, 185, "40 settings", 22, MUTED)
    b += text(800, 470, "→", 60, SIG, anchor="middle")
    b += box(890, 200, 560, 520, RAISED, SIG, sw=3) + text(910, 185, "slots", 22, SIG)
    for i, (t, h) in enumerate([("header", 70), ("media", 170), ("body", 110), ("footer", 70)]):
        y = 230 + sum([70, 170, 110, 70][:i]) + i * 20
        b += box(920, y, 500, h, SUNK, RULE, extra='stroke-dasharray="10 8"') + text(945, y + 40, t, 22, PAPER)
    return frame(INK, b, label="writing / components")


def comptokens():
    b = ""
    tiers = [("primitive", "color.brand.700", SUNK, MUTED), ("semantic", "color.action.primary.bg", SUNK, PAPER), ("component", "button.primary.container.background", RAISED, SIG)]
    for i, (k, v, f, c) in enumerate(tiers):
        y = 210 + i * 190
        b += box(150, y, 1300, 140, f, SIG if i == 2 else RULE, sw=3 if i == 2 else 2) + text(190, y + 56, k, 22, MUTED) + text(190, y + 104, v, 34, c)
        if i < 2:
            b += f'<path d="M800 {y + 146}V{y + 184}" stroke="{SIG}" stroke-width="3"/>'
    return frame(INK, b, label="writing / tokens")


def testing():
    b = ""
    steps = [("lint", SUNK, PAPER), ("behaviour", SUNK, PAPER), ("visual", SIG, INK), ("a11y auto", SUNK, PAPER), ("manual", SUNK, PAPER)]
    for i, (t, f, c) in enumerate(steps):
        x = 120 + i * 280
        b += box(x, 300, 230, 110, f, RULE if f == SUNK else "none") + text(x + 115, 365, t, 24, c, anchor="middle")
        if i < 4:
            b += f'<path d="M{x + 236} 355H{x + 274}" stroke="{SIG}" stroke-width="3"/>'
    for i in range(6):
        x = 260 + i * 190
        b += box(x, 520, 150, 150, RAISED, RULE) + box(x + 25, 580, 100, 34, SIG if i == 3 else PAPER, "none", rx=6, extra=f'opacity="{1 if i == 3 else .8}"')
    b += box(822, 506, 178, 178, "none", SIG, sw=3, extra='stroke-dasharray="8 6"') + text(911, 720, "diff", 20, SIG, anchor="middle")
    return frame(INK, b, label="writing / quality")


def a11y():
    b = box(150, 200, 620, 520, RAISED, RULE)
    b += box(210, 290, 500, 100, INK, SIG, sw=3) + box(200, 280, 520, 120, "none", SIG, rx=14, sw=2, extra='opacity=".45"') + text(240, 352, "Send invoice", 32, PAPER, SANS, weight=600)
    b += text(210, 470, "role: button", 24, MUTED) + text(210, 520, "name: “Send invoice”", 24, MUTED) + text(210, 570, "focus: visible · 3:1", 24, SIG)
    b += text(210, 620, "target: 48 × 48", 24, MUTED)
    for i, (k, v) in enumerate([("text", "4.5:1"), ("ui", "3:1"), ("tab", "↹"), ("esc", "✕")]):
        y = 220 + i * 128
        b += box(860, y, 590, 104, SUNK, RULE) + text(900, y + 64, k, 26, MUTED) + text(1410, y + 66, v, 32, SIG if i < 2 else PAPER, anchor="end")
    return frame(INK, b, label="writing / accessibility")


def figlib():
    b = ""
    files = [("Foundations", True), ("Components", True), ("Extensions", True), ("Sandbox", False), ("Archive", False)]
    for i, (t, pub) in enumerate(files):
        y = 200 + i * 110
        b += box(140, y, 420, 84, RAISED if pub else "none", SIG if i == 1 else RULE, sw=3 if i == 1 else 2, extra="" if pub else 'stroke-dasharray="10 8"') + text(176, y + 52, t, 26, PAPER if pub else MUTED)
    pages = ["Start here", "Actions", "Forms", "Feedback", "Navigation", "Data display", "Overlays"]
    b += f'<path d="M560 352H650" stroke="{SIG}" stroke-width="3"/>' + box(650, 200, 800, 520, SUNK, RULE)
    for i, t in enumerate(pages):
        y = 240 + i * 66
        b += text(700, y + 30, ("★ " if i == 0 else "▸ ") + t, 26, SIG if i == 0 else PAPER) + bar(1100, y + 16, 280 - i * 18, 12, MUTED, .4)
    return frame(INK, b, label="writing / figma")


def platforms():
    b = box(640, 180, 320, 120, SIG, "none") + text(800, 252, "tokens.json", 28, INK, anchor="middle")
    for i, (t, sub) in enumerate([("web", "CSS variables"), ("iOS", "Swift"), ("Android", "Kotlin")]):
        x = 170 + i * 450
        b += f'<path d="M800 300C800 380 {x + 130} 360 {x + 130} 430" stroke="{SIG}" stroke-width="3" fill="none"/>'
        b += box(x, 430, 260, 300, RAISED, RULE) + text(x + 130, 490, t, 30, PAPER, anchor="middle") + text(x + 130, 530, sub, 20, MUTED, anchor="middle")
        b += box(x + 40, 580, 180, 52, SIG, "none", rx=26 if i == 1 else 8) + bar(x + 40, 660, 180, 12, MUTED, .5)
    return frame(INK, b, label="writing / platforms")


def roadmap():
    b = ""
    qs = ["Q1 start", "Q2 prove", "Q3 spread", "Q4 settle"]
    for i, q in enumerate(qs):
        b += text(330 + i * 300, 210, q, 22, MUTED)
    rows = [("foundations", [1, 1, .5, .5]), ("components", [.6, 1, 1, 1]), ("operations", [1, .5, .5, 1]), ("adoption", [.4, .6, 1, 1])]
    for r, (t, v) in enumerate(rows):
        y = 250 + r * 100
        b += text(120, y + 44, t, 22, PAPER)
        for i, a in enumerate(v):
            b += f'<rect x="{320 + i * 300}" y="{y + 12}" width="{int(280 * a)}" height="50" rx="8" fill="{SIG if a == 1 else MUTED}" opacity="{1 if a == 1 else .45}"/>'
    for i in range(4):
        b += f'<path d="M{600 + i * 300} 240V660" stroke="{PAPER}" stroke-width="2" stroke-dasharray="6 8" opacity=".5"/>' + star(588 + i * 300, 676, 24, SIG)
    return frame(INK, b, label="writing / planning")


def failures():
    b = ""
    for i in range(10):
        x, y = 140 + (i % 5) * 270, 230 + (i // 5) * 250
        bad = i in (0, 1)
        b += box(x, y, 230, 200, RAISED if bad else SUNK, SIG if bad else RULE, sw=3 if bad else 2) + text(x + 24, y + 60, f"{i + 1:02d}", 40, SIG if bad else MUTED)
        b += bar(x + 24, y + 110, 160, 12, PAPER if bad else MUTED, .55) + bar(x + 24, y + 140, 110, 12, MUTED, .35)
    return frame(INK, b, label="writing / fundamentals")


def startups():
    b = ""
    steps = [("tokens", 1), ("themed library", .8), ("small figma", .65), ("two owners", .5)]
    for i, (t, a) in enumerate(steps):
        x, h = 170 + i * 320, 140 + (3 - i) * 0 + i * 110
        y = 700 - h
        b += box(x, y, 280, h, SIG if i == 0 else SUNK, "none" if i == 0 else RULE) + text(x + 24, y + 50, t, 26, INK if i == 0 else PAPER)
    b += text(170, 220, "minimum viable system", 26, MUTED) + text(1430, 220, "add more only when it hurts", 22, SIG, anchor="end")
    return frame(INK, b, label="writing / fundamentals")


ART.update({"component-states": states, "component-composition-slots": composition, "component-tokens": comptokens, "design-system-testing": testing,
            "accessible-design-system": a11y, "figma-library-structure": figlib, "cross-platform-design-system": platforms,
            "design-system-roadmap": roadmap, "why-design-systems-fail": failures, "design-system-for-startups": startups})


def main():
    os.makedirs(OUT, exist_ok=True)
    from playwright.sync_api import sync_playwright

    def font(f):
        with open(os.path.join(ROOT, "assets", "fonts", f), "rb") as fh:
            return "data:font/woff2;base64," + base64.b64encode(fh.read()).decode()
    css = (f'@font-face{{font-family:"Schibsted Grotesk";src:url({font("schibsted-grotesk-latin-wght-normal.woff2")});font-weight:400 900}}'
           f'@font-face{{font-family:"JetBrains Mono";src:url({font("jetbrains-mono-latin-400-normal.woff2")})}}'
           'body{margin:0}svg{display:block}')
    only = sys.argv[1:]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM") or None)
        pg = b.new_page(viewport={"width": 1600, "height": 900})
        for name, fn in ART.items():
            if only and name not in only:
                continue
            pg.set_content(f"<style>{css}</style>{fn()}")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            path = os.path.join(OUT, name + ".jpg")
            pg.screenshot(path=path, type="jpeg", quality=88)
            print("wrote", os.path.relpath(path, ROOT), os.path.getsize(path) // 1024, "KB")
        b.close()


if __name__ == "__main__":
    main()
