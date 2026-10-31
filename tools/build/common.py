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

NAV = [("home", "Home", "index.html"), ("work", "Work", "work.html"), ("experience", "Experience", "clients.html"),
       ("studio", "Studio", "studio.html"), ("pricing", "Pricing", "pricing.html"), ("lab", "Lab", "lab.html"),
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
    return f'''<header class="topbar"><div class="topbar-in">
  <a class="logo" href="{p}index.html" aria-label="Layer One, home">{LOGO}<span>LAYER ONE</span></a>
  <nav class="topnav" aria-label="Main">{links}</nav>
  <button class="pill menu-btn" type="button" aria-expanded="false">Menu</button>
  <a class="pill book" href="{CAL}" target="_blank" rel="noopener">Book a call</a>
</div></header>
'''


CHIP_COLORS = ["#4736fe", "#ff6b3d", "#9de7c8", "#0f62fe", "#8a5434", "#cfcbff", "#0b0d12", "#174527"]


def sidebar(subnav, depth=0, card="founding"):
    p = "../" * depth
    sub = "".join(f'<a href="{h}">{t}</a>' for t, h in subnav)
    if card == "bar":
        c = f'<a class="side-card side-card--bar" href="{p}contact.html"><span>Start a project</span>{LONG_ARROW}</a>'
    else:
        chips = "".join(f'<span style="--c:{col};--i:{i}"></span>' for i, col in enumerate(CHIP_COLORS))
        c = f'''<a class="side-card" href="{p}pricing.html#founding">
      <div class="chips" aria-hidden="true">{chips}</div>
      <div><strong>Founding partners, 2027</strong><p>Three teams get 20% off any engagement. We publish the case study together.</p></div>
      <span class="go">See pricing {LONG_ARROW}</span>
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
# Companies and projects. Only CARS24, IBM and JPMorgan Chase appear on the site.
# ---------------------------------------------------------------------------
COMPANIES = {
    "cars24": dict(name="CARS24", logo="assets/logos/cars24.png", years="2024–25", role="Design Systems Lead",
                   line="One of India's largest platforms for buying and selling used cars, with loans, insurance and servicing, in India, the UAE and Australia."),
    "ibm": dict(name="IBM", logo="assets/logos/ibm.png", years="2021–24", role="UX Designer, design systems",
                line="Enterprise software and infrastructure used by businesses around the world."),
    "jpmc": dict(name="JPMorgan Chase", logo="assets/logos/jpmorgan-chase.jpg", years="2025–now", role="Senior Designer, Design Systems",
                 line="One of the world's largest financial services companies."),
}


def logo_tile(key, depth=0, size=None, label=True):
    c = COMPANIES[key]
    st = f' style="--s:{size}px"' if size else ""
    cap = f'<span>{c["name"]}</span>' if label else ""
    return f'<span class="ltile"{st}><img src="{"../" * depth}{c["logo"]}" alt="{c["name"]}" width="200" height="200" loading="lazy">{cap}</span>'


PROJECTS = [
    dict(slug="cars24-tokens", case=True, co="cars24", client="CARS24", year="2024–25",
         title="CARS24: one colour system for 10+ products in three countries",
         kind="Colour, Tokens, Architecture", f="#4736fe", ft="#ffffff", cover="assets/work/tokens/cover.jpg",
         blurb="A new palette in OKLCH and a four-layer token system that carried the CARS24 rebrand across India, the UAE and Australia.",
         stat=("65%", "faster design-to-development handoff")),
    dict(slug="cars24-governance", case=True, co="cars24", client="CARS24", year="2025",
         title="CARS24: how the design system team stopped being the bottleneck",
         kind="Governance, Operations", f="#f1efff", ft="#0b0d12", cover="assets/work/governance/cover.jpg",
         blurb="One front door for requests, a 70-point scorecard any team can apply, three ownership tiers and a contribution playbook.",
         stat=("70 pts", "scorecard any team can apply")),
    dict(slug="cars24-pattern-library", case=True, co="cars24", client="CARS24", year="2025",
         title="CARS24: a pattern library that builds pages from tested blocks",
         kind="Patterns, CMS, Adoption", f="#9de7c8", ft="#0b0d12", cover="assets/work/patterns/cover.jpg",
         blurb="Six families of page blocks wired to the CMS and the tokens, so a super app with new services every month ships pages in days.",
         stat=("~43%", "less time to design and build a page")),
    dict(slug="jpmc-system-checks", case=False, co="jpmc", client="JPMorgan Chase", year="2026",
         title="JPMorgan Chase: design system checks for 500+ designers and 1,000+ engineers",
         kind="Tooling, Governance", f="#8a5434", ft="#ffffff", cover="assets/work/jpmc-checks/cover.jpg", illus=True,
         blurb="Two tools that point out where a design file or a piece of code doesn't match the design system, so problems are fixed before review.",
         points=["A checker for designers that compares a Figma file against the design system and suggests the right token or pattern.",
                 "A matching checker for engineers that flags hard-coded values and detached patterns in code.",
                 "Used by a community of 500+ designers and 1,000+ engineers."],
         scope=[("Designer tool", "Checks Figma files against tokens and patterns"), ("Engineer tool", "Checks code against the same rules"), ("Reach", "500+ designers, 1,000+ engineers")]),
    dict(slug="jpmc-patterns", case=False, co="jpmc", client="JPMorgan Chase", year="2025–26",
         title="JPMorgan Chase: company-wide design patterns, drafted with an AI workflow",
         kind="Patterns, AI workflow", f="#c99a74", ft="#1a120c", cover="assets/work/jpmc-patterns/cover.jpg", illus=True,
         blurb="Shared design patterns that product teams across the company use, and a workflow where an AI agent does the early research and drafts each pattern for designers to review.",
         points=["Leads the creation of design patterns used by product teams across the company.",
                 "An AI agent does the early research, talks through needs with product teams and drafts a first version of each pattern.",
                 "Designers review, refine and publish. Regular office hours help teams use what's there."],
         scope=[("Pattern library", "Patterns used across the company"), ("AI workflow", "Research and first drafts by an agent, reviewed by designers"), ("Support", "Office hours for product teams")]),
    dict(slug="ibm-design-systems", case=False, co="ibm", client="IBM", year="2021–24",
         title="IBM: design systems for products used around the world",
         kind="Design systems, Contribution", f="#0f62fe", ft="#ffffff", cover="assets/work/ibm-design-systems/cover.jpg", illus=True,
         blurb="Several product design systems built and launched in Bangalore, with a contribution process other teams could follow, regular releases and training.",
         points=["Built and launched several design systems for products used around the world.",
                 "Set up a clear process for other teams to contribute and keep the systems consistent.",
                 "Ran research and usability tests, managed regular releases and ran training to help teams adopt the systems."],
         scope=[("Design systems", "Several product systems, built and launched"), ("Contribution", "A process other teams could follow"), ("Releases", "Regular releases with training")]),
    dict(slug="cars24-consumer", case=False, co="cars24", client="CARS24", year="2024–25",
         title="CARS24: a token-driven component library for consumer products",
         kind="Components, Tokens", f="#cfcbff", ft="#0b0d12", cover="assets/work/cars24-consumer/cover.jpg",
         blurb="The consumer design system and component library behind the CARS24 apps, with every component built on tokens rather than hard-coded values.",
         points=["Buttons, chips, toasts, inline alerts, inputs and more, each built on the token architecture.",
                 "100% token-driven, so the rebrand and every theme flowed through without redesigning components.",
                 "Shared by app and mobile web teams across the CARS24 businesses."],
         scope=[("Component library", "Buttons, chips, toasts, inline alerts and more"), ("Token architecture", "100% token-driven components"), ("Platforms", "App and mobile web")]),
    dict(slug="cars24-internal-tools", case=False, co="cars24", client="CARS24", year="2024–25",
         title="CARS24: a design system for internal tools at enterprise scale",
         kind="Design system, Documentation", f="#174527", ft="#ffffff", cover="assets/work/cars24-internal-tools/cover.jpg",
         blurb="A separate system for the dashboards and operations tools CARS24 teams use every day: enterprise-ready, localised, with spec-first documentation.",
         points=["Foundations tuned for dense, data-heavy screens: type weights, spacing and radius tokens.",
                 "Components for forms, tables, navigation and account flows.",
                 "Spec-first documentation so engineering could build without waiting on design."],
         scope=[("Foundations", "Type weights, spacing and radius tokens"), ("Components", "Forms, tables, navigation, account flows"), ("Documentation", "Spec-first docs for engineering")]),
]


def href(proj, depth=0):
    return ("../" * depth) + f"work/{proj['slug']}.html"


def frame(proj, depth=0, show_year=False):
    p = "../" * depth
    year = f'<span>{proj["year"]}</span>' if show_year and proj["year"] else ""
    illus = '<span class="illus">Illustration</span>' if proj.get("illus") else ""
    return f'''<a class="frame" href="{href(proj, depth)}" style="--f:{proj["f"]};--ft:{proj["ft"]}">
      <div class="frame-media"><img src="{p}{proj["cover"]}" alt="" loading="lazy" width="1800" height="1238">{illus}</div>
      <h3>{proj["title"]}</h3>
      <div class="frame-meta"><span class="kind">{proj["kind"]}</span>{year}</div>
    </a>'''


def reel(depth=0):
    p = "../" * depth
    return f'''<figure class="reel" data-reel>
      <video autoplay muted loop playsinline preload="auto" poster="{p}assets/video/hero-poster.jpg" aria-label="A 24-second recap of our design system work at CARS24, IBM and JPMorgan Chase">
        <source src="{p}assets/video/hero-reel.webm" type="video/webm">
        <source src="{p}assets/video/hero-reel.mp4" type="video/mp4">
      </video>
      <button class="reel-btn" type="button" aria-label="Pause the video" data-reel-toggle><svg viewBox="0 0 16 16" aria-hidden="true"><rect class="i-pause" x="3.5" y="3" width="3" height="10" rx="1"/><rect class="i-pause" x="9.5" y="3" width="3" height="10" rx="1"/><path class="i-play" d="M4.5 2.8v10.4L13 8z"/></svg></button>
      <div class="reel-progress" aria-hidden="true"><span></span></div>
    </figure>'''

def trust(label, keys=("jpmc", "ibm", "cars24"), depth=0):
    """Logo strip: a label row, then one wide brand panel per company (JPMorgan Chase first). Logos only, no dates."""
    cells = "".join(f'<li><img src="{"../" * depth}{COMPANIES[k]["logo"]}" alt="{COMPANIES[k]["name"]}" width="400" height="400" loading="lazy"></li>' for k in keys)
    return f'<div class="trust"><p>{label}</p><ul>{cells}</ul></div>'


ARROW_SHIFT = ARROW


def short(p):
    """Project title without the client prefix, sentence case."""
    t = p["title"].split(": ", 1)[1]
    return t[0].upper() + t[1:]
