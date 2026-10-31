"""Writing covers in the Layer One style: graphite, signal orange, the star mark, mono token labels.
Renders assets/images/blog/*.jpg (1600 x 900). Run: python3 tools/covers/blog_art.py (needs playwright)."""
import base64, os
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "assets", "images", "blog")
INK, RAISED, SUNK, RULE, MUTED, PAPER, SIG = "#0b0d12", "#13161d", "#1b1f28", "#2a2f3a", "#9aa0aa", "#ecece8", "#ff6b3d"
STAR = ('M50 0a50 50 0 1 1 0 100A50 50 0 0 1 50 0Z'
        'M16.3 50A34 34 0 0 0 50 16.3V49.2a.8.8 0 0 1-.8.8Z'
        'M83.7 50A34 34 0 0 0 50 83.7V50.8a.8.8 0 0 1 .8-.8Z')
SANS = 'font-family="Schibsted Grotesk"'
MONO = 'font-family="JetBrains Mono"'


def star(x, y, s, fill):
    return f'<g transform="translate({x} {y}) scale({s / 100})"><path fill="{fill}" fill-rule="evenodd" d="{STAR}"/></g>'


def frame(bg, body, ink=PAPER, label=""):
    dots = f'<pattern id="d" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="{ink}" opacity=".12"/></pattern>'
    head = (f'<text x="72" y="96" {MONO} font-size="22" fill="{ink}" opacity=".7">{label}</text>'
            + star(1488, 66, 40, ink))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900"><defs>{dots}</defs>'
            f'<rect width="1600" height="900" fill="{bg}"/><rect width="1600" height="900" fill="url(#d)"/>{head}{body}</svg>')


def librarian():
    b = f'<path d="M800 150V800" stroke="{RULE}" stroke-width="2" stroke-dasharray="6 10"/>'
    # Left: a tidy catalogue, every component shelved and labelled
    for r in range(4):
        for c in range(5):
            x, y = 104 + c * 128, 220 + r * 112
            b += (f'<rect x="{x}" y="{y}" width="108" height="88" rx="8" fill="{SUNK}" stroke="{RULE}" stroke-width="2"/>'
                  f'<rect x="{x + 16}" y="{y + 22}" width="{40 + (r * 5 + c) % 4 * 10}" height="12" rx="6" fill="{MUTED}" opacity=".5"/>'
                  f'<rect x="{x + 16}" y="{y + 50}" width="56" height="8" rx="4" fill="{RULE}"/>')
    b += f'<text x="104" y="760" {MONO} font-size="30" fill="{MUTED}">librarian/</text>'
    # Right: the same parts, pulled into a direction
    pts = [(872, 600), (992, 520), (1112, 440), (1232, 360), (1352, 280)]
    d = "M" + " L".join(f"{x + 54} {y + 44}" for x, y in pts)
    b += f'<path d="{d}" fill="none" stroke="{SIG}" stroke-width="4" stroke-linejoin="round"/>'
    for i, (x, y) in enumerate(pts[:-1]):
        b += f'<rect x="{x}" y="{y}" width="108" height="88" rx="8" fill="{SUNK}" stroke="{SIG if i > 1 else RULE}" stroke-width="2"/>'
    x, y = pts[-1]
    b += f'<rect x="{x}" y="{y}" width="108" height="88" rx="8" fill="{SIG}"/>' + star(x + 30, y + 20, 48, INK)
    b += f'<text x="880" y="760" {MONO} font-size="30" fill="{SIG}">leader/</text>'
    return frame(INK, b, label="writing / leadership")


def backbone():
    b = f'<rect x="104" y="436" width="1392" height="28" rx="14" fill="{INK}"/>'
    names = ["checkout", "search", "loans", "insurance", "ops", "partners", "admin", "docs"]
    for i, n in enumerate(names):
        cx = 180 + i * 177
        up = i % 2 == 0
        y = 210 if up else 560
        b += (f'<path d="M{cx} {450} V{y + (130 if up else 0)}" stroke="{INK}" stroke-width="4"/>'
              f'<circle cx="{cx}" cy="450" r="22" fill="{SIG}" stroke="{INK}" stroke-width="4"/>'
              f'<rect x="{cx - 76}" y="{y}" width="152" height="130" rx="8" fill="none" stroke="{INK}" stroke-width="4"/>'
              f'<rect x="{cx - 56}" y="{y + 22}" width="64" height="12" rx="6" fill="{INK}"/>'
              f'<rect x="{cx - 56}" y="{y + 46}" width="100" height="8" rx="4" fill="{INK}" opacity=".35"/>'
              f'<text x="{cx - 56}" y="{y + 106}" {MONO} font-size="20" fill="{INK}">{n}</text>')
    b += f'<text x="104" y="820" {MONO} font-size="30" fill="{INK}">one spine, many products</text>'
    return frame(SIG, b, ink=INK, label="writing / operations")


def libraries():
    b = ""
    # A full component sheet...
    for i, (w, fill, txt, tc) in enumerate([(176, PAPER, "Primary", INK), (176, SUNK, "Secondary", PAPER), (150, "none", "Ghost", PAPER), (130, SIG, "Buy", INK)]):
        x = 104 + sum(v[0] + 24 for v in [(176,), (176,), (150,), (130,)][:i])
        b += (f'<rect x="{x}" y="180" width="{w}" height="64" rx="8" fill="{fill}" stroke="{RULE}" stroke-width="2"/>'
              f'<text x="{x + w / 2}" y="221" text-anchor="middle" {SANS} font-weight="500" font-size="24" fill="{tc}">{txt}</text>')
    for i in range(2):
        x = 104 + i * 420
        b += (f'<text x="{x}" y="300" {SANS} font-size="20" fill="{MUTED}">{["Email", "Company"][i]}</text>'
              f'<rect x="{x}" y="314" width="396" height="64" rx="8" fill="{SUNK}" stroke="{RULE}" stroke-width="2"/>'
              f'<rect x="{x + 20}" y="340" width="150" height="12" rx="6" fill="{MUTED}" opacity=".4"/>')
    for i in range(3):
        x = 104 + i * 120
        on = i == 1
        b += (f'<rect x="{x}" y="420" width="88" height="48" rx="24" fill="{SIG if on else SUNK}" stroke="{RULE}" stroke-width="2"/>'
              f'<circle cx="{x + (64 if on else 24)}" cy="444" r="16" fill="{INK if on else MUTED}"/>')
    for i, t in enumerate(["New", "Popular", "Sale", "Beta"]):
        x = 480 + i * 128
        b += (f'<rect x="{x}" y="424" width="112" height="40" rx="20" fill="none" stroke="{MUTED}" stroke-width="2"/>'
              f'<text x="{x + 56}" y="451" text-anchor="middle" {SANS} font-size="20" fill="{PAPER}">{t}</text>')
    # A price tag on the kit
    b += (f'<g transform="translate(1180 180) rotate(8)"><path d="M0 0H200L240 60L200 120H0Z" fill="{SIG}"/>'
          f'<circle cx="200" cy="60" r="10" fill="{RAISED}"/>'
          f'<text x="28" y="78" {SANS} font-weight="700" font-size="48" fill="{INK}">$$$</text></g>')
    # ...sitting on a missing layer
    b += (f'<rect x="104" y="560" width="1392" height="200" rx="8" fill="none" stroke="{SIG}" stroke-width="2" stroke-dasharray="10 10"/>'
          f'<text x="144" y="640" {MONO} font-size="30" fill="{PAPER}">tokens  ·  governance  ·  adoption</text>'
          f'<text x="144" y="700" {MONO} font-size="24" fill="{SIG}">// missing</text>')
    return frame(RAISED, b, label="writing / strategy")


def foundations():
    rows = [("color", 190), ("type", 370), ("space", 540), ("radius", 690)]
    b = "".join(f'<text x="104" y="{y + 56}" {MONO} font-size="26" fill="{MUTED}">{n}/</text>'
                f'<path d="M104 {y + 110}H1496" stroke="{RULE}" stroke-width="2"/>' for n, y in rows[:-1]) + \
        f'<text x="104" y="{690 + 56}" {MONO} font-size="26" fill="{MUTED}">radius/</text>'
    ramp = ["#fff1eb", "#ffd9c9", "#ffbfa6", "#ffa07f", "#ff8a63", "#ff6b3d", "#e5532a", "#b83f1f", "#8a2f17", "#5c1f0f"]
    b += "".join(f'<rect x="{320 + i * 118}" y="190" width="104" height="88" rx="8" fill="{c}"/>' for i, c in enumerate(ramp))
    x = 320
    for s in (28, 40, 56, 76, 100):
        b += f'<text x="{x}" y="456" {SANS} font-weight="600" font-size="{s}" fill="{PAPER}" letter-spacing="-1">Aa</text>'
        x += s * 1.25 + 40
    b += f'<text x="{x + 20}" y="456" {MONO} font-size="22" fill="{MUTED}">14 / 16 / 20 / 24 / 32 / 44</text>'
    x = 320
    for s in (8, 16, 24, 32, 48, 64, 96, 128):
        b += f'<rect x="{x}" y="560" width="{s}" height="48" rx="2" fill="{SIG}" opacity=".9"/>'
        x += s + 48
    for i, r in enumerate((0, 4, 8, 16, 24, 44)):
        b += f'<rect x="{320 + i * 140}" y="682" width="88" height="88" rx="{r}" fill="none" stroke="{PAPER}" stroke-width="3"/>'
    b += f'<rect x="{320 + 2 * 140}" y="682" width="88" height="88" rx="8" fill="{SIG}"/>'
    return frame(INK, b, label="writing / architecture")


ART = {"librarian-vs-leader": librarian, "operational-backbone": backbone, "ui-libraries": libraries, "foundations": foundations}


def main():
    def font(f):
        with open(os.path.join(ROOT, "assets", "fonts", f), "rb") as fh:
            return "data:font/woff2;base64," + base64.b64encode(fh.read()).decode()
    css = (f'@font-face{{font-family:"Schibsted Grotesk";src:url({font("schibsted-grotesk-latin-wght-normal.woff2")});font-weight:400 900}}'
           f'@font-face{{font-family:"JetBrains Mono";src:url({font("jetbrains-mono-latin-400-normal.woff2")})}}'
           'body{margin:0}svg{display:block}')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM") or None)
        pg = b.new_page(viewport={"width": 1600, "height": 900})
        for name, fn in ART.items():
            pg.set_content(f"<style>{css}</style>{fn()}")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            path = os.path.join(OUT, name + ".jpg")
            pg.screenshot(path=path, type="jpeg", quality=88)
            print("wrote", os.path.relpath(path, ROOT), os.path.getsize(path) // 1024, "KB")
        b.close()


if __name__ == "__main__":
    main()
