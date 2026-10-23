"""Shared shell for every Layer One page. Direction: .claude/skills/layer-one-site/SKILL.md"""
import os

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CAL = "https://cal.com/layerone"
EMAIL = "layerone@proton.me"
LINKEDIN = "https://www.linkedin.com/company/layerone.co.in/"
X = "https://x.com/LayeroneStudios"
MEDIUM = "https://medium.com/@layerone_11803"

ARROW = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LONG_ARROW = '<svg viewBox="0 0 34 14" fill="none" aria-hidden="true"><path d="M1 7h31M26 1l6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR = ('M50 0a50 50 0 1 1 0 100A50 50 0 0 1 50 0Z'
        'M16.3 50A34 34 0 0 0 50 16.3V49.2a.8.8 0 0 1-.8.8Z'
        'M83.7 50A34 34 0 0 0 50 83.7V50.8a.8.8 0 0 1 .8-.8Z')
LOGO = f'<svg viewBox="0 0 100 100" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="{STAR}"/></svg>'

# Big layered wordmark for the sidebar: the front copy is filled, two outline copies sit behind it like layers.
def _layered(lines, size, lh, x=4, w=300, extra=""):
    h = lh * len(lines) + 14
    out = f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Layer One">'
    for dx, op, fill in ((10, 0.35, False), (5, 0.6, False), (0, 1, True)):
        out += f'<g transform="translate({dx} {dx})" opacity="{op}" font-family="Schibsted Grotesk, sans-serif" font-weight="800" font-size="{size}" letter-spacing="-4">'
        for i, t in enumerate(lines):
            y = lh * (i + 1) - 4
            if fill:
                out += f'<text x="{x}" y="{y}" fill="currentColor">{t}</text>'
            else:
                out += f'<text x="{x}" y="{y}" fill="none" stroke="currentColor" stroke-width="1.4">{t}</text>'
        out += "</g>"
    return out + extra + "</svg>"


WORDMARK = _layered(["LAYER", "ONE"], 92, 84, w=300,
                    extra=f'<g transform="translate(222 100) scale(.62)"><path fill="currentColor" fill-rule="evenodd" d="{STAR}"/></g>')

# Cropped top-of-page banner, in the spirit of Hex's cut-off wordmark artwork.
BANNER = ('<svg viewBox="0 0 1000 150" role="img" aria-label="Layer One">'
          + "".join(f'<g transform="translate({d} {d})" opacity="{o}" font-family="Schibsted Grotesk, sans-serif" font-weight="800" font-size="250" letter-spacing="-12">'
                    f'<text x="-6" y="172" {"fill=" + chr(34) + "currentColor" + chr(34) if f else "fill=" + chr(34) + "none" + chr(34) + " stroke=" + chr(34) + "currentColor" + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34)}>LAYER ONE</text></g>'
                    for d, o, f in ((18, 0.3, False), (9, 0.55, False), (0, 1, True)))
          + "</svg>")

NAV = [("home", "Home", "index.html"), ("work", "Work", "work.html"), ("clients", "Clients", "clients.html"),
       ("studio", "Studio", "studio.html"), ("services", "Services", "services.html"), ("lab", "Lab", "lab.html"),
       ("writing", "Writing", "blog.html"), ("contact", "Contact", "contact.html")]


def head(title, desc, depth=0, theme="dark", og="assets/work/tokens/cover.jpg"):
    p = "../" * depth
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.layerone.co.in/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{"#0b0d12" if theme == "dark" else "#f6f6f3"}">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{p}assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css">
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body class="theme-{theme}">
<a class="skip" href="#main">Skip to content</a>
'''


def topbar(active=None, depth=0):
    p = "../" * depth
    links = "".join(f'<a href="{p}{h}"{" aria-current=" + chr(34) + "page" + chr(34) if k == active else ""}>{t}</a>' for k, t, h in NAV)
    return f'''<header class="topbar">
  <a class="logo" href="{p}index.html" aria-label="Layer One, home">{LOGO}<span>LAYER ONE</span></a>
  <nav class="topnav" aria-label="Main">{links}</nav>
  <button class="pill menu-btn" type="button" aria-expanded="false">Menu</button>
  <a class="pill book" href="{CAL}" target="_blank" rel="noopener">Book a call</a>
</header>
'''


CHIP_COLORS = ["#4736fe", "#ff6b3d", "#9de7c8", "#220e54", "#e5343f", "#512aac", "#0b0d12", "#174527"]


def sidebar(subnav, depth=0, card="founding"):
    p = "../" * depth
    sub = "".join(f'<a href="{h}">{t}</a>' for t, h in subnav)
    if card == "bar":
        c = f'<a class="side-card side-card--bar" href="{p}contact.html"><span>Start a project</span>{LONG_ARROW}</a>'
    else:
        chips = "".join(f'<span style="--c:{col};--i:{i}"></span>' for i, col in enumerate(CHIP_COLORS))
        c = f'''<a class="side-card" href="{p}services.html#founding">
      <div class="chips" aria-hidden="true">{chips}</div>
      <div><strong>Founding partners, 2027</strong><p>Three teams get 20% off any engagement. We publish the case study together.</p></div>
      <span class="go">Book a call {LONG_ARROW}</span>
    </a>'''
    return f'''<aside class="side" aria-label="Studio">
    <nav class="side-nav" aria-label="On this page">{sub}</nav>
    {c}
    <p class="side-blurb">Layer One is a design systems studio in Bangalore, India.<br>Led by Aniket Pandey.</p>
    <div class="wordmark">{WORDMARK}</div>
    <div class="side-foot">
      <ul><li><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin</a></li><li><a href="{X}" target="_blank" rel="noopener">x</a></li><li><a href="{MEDIUM}" target="_blank" rel="noopener">medium</a></li></ul>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </aside>'''


def shell(active, subnav, content, card="founding", depth=0):
    """Dark listing page: top bar + sticky sidebar + content column."""
    return (topbar(active, depth)
            + f'<div class="shell">{sidebar(subnav, depth, card)}<main id="main" class="content">{content}</main></div>'
            + close(depth))


def close(depth=0):
    p = "../" * depth
    return f'<script src="{p}assets/site.js" defer></script>\n</body>\n</html>\n'


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path, len(html) // 1024, "KB")


# ---------------------------------------------------------------------------
# Projects. "case" = full case study page; otherwise a short project page.
# Frame colours come from each project's own work.
# ---------------------------------------------------------------------------
PROJECTS = [
    dict(slug="cars24-tokens", case=True, client="CARS24", year="2024–25",
         title="CARS24: one colour system for 10+ products in three countries",
         kind="Colour, Tokens, Architecture", f="#4736fe", ft="#ffffff", cover="assets/work/tokens/cover.jpg",
         blurb="A new palette in OKLCH and a four-layer token system that carried the CARS24 rebrand across India, the UAE and Australia.",
         stat=("65%", "faster design-to-development handoff")),
    dict(slug="cars24-governance", case=True, client="CARS24", year="2025",
         title="CARS24: how the design system team stopped being the bottleneck",
         kind="Governance, Operations", f="#f1efff", ft="#0b0d12", cover="assets/work/governance/cover.jpg",
         blurb="One front door for requests, a 70-point scorecard any team can apply, three ownership tiers and a contribution playbook.",
         stat=("70 pts", "scorecard any team can apply")),
    dict(slug="cars24-pattern-library", case=True, client="CARS24", year="2025",
         title="CARS24: a pattern library that builds pages from tested blocks",
         kind="Patterns, CMS, Adoption", f="#9de7c8", ft="#0b0d12", cover="assets/work/patterns/cover.jpg",
         blurb="Six families of page blocks wired to the CMS and the tokens, so a super app with new services every month ships pages in days.",
         stat=("~43%", "less time to design and build a page")),
    dict(slug="riyadh-air", case=False, client="Riyadh Air", year="",
         title="Riyadh Air: a bilingual design system and pattern library",
         kind="Design system, Patterns, Arabic and English", f="#220e54", ft="#ffffff", cover="assets/work/riyadh-air/cover.jpg",
         blurb="Base elements, components and patterns for a new airline's digital products, built to work in English and in Arabic, right to left.",
         scope=[("Design system", "Foundations, base elements, components"), ("Pattern library", "Lists, titles, navigation"), ("Localisation", "Arabic and English, right-to-left layouts")]),
    dict(slug="cars24-consumer", case=False, client="CARS24", year="2024–25",
         title="CARS24: a token-driven component library for consumer products",
         kind="Components, Tokens", f="#cfcbff", ft="#0b0d12", cover="assets/work/cars24-consumer/cover.jpg",
         blurb="The consumer design system and component library behind the CARS24 apps, with every component built on tokens rather than hard-coded values.",
         scope=[("Component library", "Buttons, chips, toasts, inline alerts and more"), ("Token architecture", "100% token-driven components"), ("Platforms", "App and mobile web")]),
    dict(slug="cars24-internal-tools", case=False, client="CARS24", year="2024–25",
         title="CARS24: a design system for internal tools at enterprise scale",
         kind="Design system, Documentation", f="#174527", ft="#ffffff", cover="assets/work/cars24-internal-tools/cover.jpg",
         blurb="A separate system for the dashboards and operations tools CARS24 teams use every day: enterprise-ready, localised, with spec-first documentation.",
         scope=[("Foundations", "Type weights, spacing and radius tokens"), ("Components", "Forms, tables, navigation, account flows"), ("Documentation", "Spec-first docs for engineering")]),
    dict(slug="pharma-b2b", case=False, client="Global pharmaceutical company (USA)", year="",
         title="A US pharmaceutical company: web components for a B2B platform",
         kind="Web components, Tokens", f="#e5343f", ft="#ffffff", cover="assets/work/pharma-b2b/cover.jpg",
         blurb="A design system for a next-generation B2B ordering platform, delivered as framework-agnostic web components on a semantic token layer.",
         scope=[("Token architecture", "Semantic background, surface, action and status tokens"), ("Components", "Web components for search, navigation and account flows"), ("Platform", "B2B web")]),
    dict(slug="district", case=False, client="District by Zomato", year="",
         title="District by Zomato: a visual design system for going out",
         kind="Visual design system", f="#512aac", ft="#ffffff", cover="assets/work/district/cover.jpg",
         blurb="A visual design system for District, Zomato's app for movies, events and dining in one place.",
         scope=[("Visual language", "Colour, illustration and iconography"), ("Product UI", "Category navigation and discovery"), ("Platforms", "Mobile app")]),
]


def href(proj, depth=0):
    return ("../" * depth) + f"work/{proj['slug']}.html"


def frame(proj, depth=0, show_year=False, small=False):
    p = "../" * depth
    year = f'<span>{proj["year"]}</span>' if show_year and proj["year"] else ""
    return f'''<a class="frame" href="{href(proj, depth)}" style="--f:{proj["f"]};--ft:{proj["ft"]}">
      <div class="frame-media"><img src="{p}{proj["cover"]}" alt="" loading="lazy" width="1800" height="1238"></div>
      <h3>{proj["title"]}</h3>
      <div class="frame-meta"><span class="kind">{proj["kind"]}</span>{year}</div>
    </a>'''


STAGE_BRANDS = [("CARS24", "#4736fe"), ("Riyadh Air", "#5b2d90"), ("Pharma B2B", "#e5343f"), ("District", "#7b3fe4"), ("Internal tools", "#1f7a4a")]


def stage(depth=0):
    dots = "".join(f'<button type="button" style="--c:{h}" data-hex="{h}" data-name="{n}" aria-label="Show the {n} theme" aria-pressed="false"></button>' for n, h in STAGE_BRANDS)
    return f'''<figure class="stage" data-stage aria-label="One design system, many brands: the same four token layers re-themed for each client">
      <div class="stage-grid"></div>
      <p class="stage-legend">value → primitive → semantic → component</p>
      <div class="iso-wrap" aria-hidden="true"><div class="iso">
        <div class="plate plate--value"><span class="tag">value</span><div class="swatch"></div></div>
        <div class="plate plate--primitive"><span class="tag">primitive · color-brand-50…900</span><div class="ramp">{"<span></span>" * 10}</div></div>
        <div class="plate plate--semantic"><span class="tag">semantic</span><div class="sem"><div><i></i>color-action-primary</div><div><i></i>color-surface-accent</div><div><i></i>color-text-strong</div></div></div>
        <div class="plate plate--component"><span class="tag">component</span><div class="ui"><div class="bar"></div><div class="bar s"></div><div class="card"></div><div class="btn">Get started</div></div></div>
      </div></div>
      <figcaption class="stage-caption"><span>One system, re-themed: <span class="mono" data-brand-name>CARS24</span> <span class="mono" data-brand-hex>#4736FE</span></span><span class="brand-dots">{dots}</span></figcaption>
    </figure>'''
ARROW_SHIFT = ARROW
