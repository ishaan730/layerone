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
