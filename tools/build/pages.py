from common import *

# ======================= Work =======================
cases = [p for p in PROJECTS if p["case"]]
others = [p for p in PROJECTS if not p["case"]]
work_c = f'''
<h1 class="statement" id="case-studies">featured work</h1>
<p class="sub muted">Full, interactive case studies: the problem, the decisions and the numbers.</p>
<div class="frames" style="margin-top:20px">{"".join(frame(p, show_year=True) for p in cases)}</div>
<h2 class="label" id="projects">more projects</h2>
<p class="sub muted" style="margin:-8px 0 20px">Systems the team has shipped at CARS24, IBM and JPMorgan Chase. Walkthroughs on request.</p>
<div class="frames frames--2">{"".join(frame(p, show_year=True) for p in others)}</div>
<p class="small muted" style="margin-top:28px;max-width:72ch">This work was led by Aniket Pandey while employed at CARS24, IBM and JPMorgan Chase. Images marked "Illustration" are drawn by us to describe the work, because the real screens can't be shared.</p>
'''
write("work.html", head("Work — Layer One", "Design system case studies and projects from CARS24, IBM and JPMorgan Chase.")
      + shell("work", [("Featured", "#case-studies"), ("More projects", "#projects")], work_c, card="bar"))

# ======================= Experience =======================
xp = ""
for key, facts in [
    ("cars24", [("70+ / 200+", "designers and engineers on one system"), ("10+", "product lines, 3 countries"), ("65%", "faster handoff after the token rebuild")]),
    ("ibm", [("3.5 yrs", "building and running design systems"), ("Several", "product systems built and launched"), ("Worldwide", "products used around the world")]),
    ("jpmc", [("500+", "designers using the design checks"), ("1,000+", "engineers using the code checks"), ("AI", "workflow that drafts new patterns")]),
]:
    c = COMPANIES[key]
    projs = [p for p in PROJECTS if p["co"] == key]
    f_html = "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in facts)
    p_html = "".join(f'<a href="{href(p)}"><img src="{p["cover"]}" alt="" loading="lazy"><span>{short(p)}</span></a>' for p in projs)
    xp += f'''<article class="xrow" id="{key}">
      <header>{logo_tile(key, size=88, label=False)}<div><h2>{c["name"]}</h2><p>{c["role"]} · {c["years"]}</p><p class="muted">{c["line"]}</p></div></header>
      <div class="xfacts">{f_html}</div>
      <div class="xprojs">{p_html}</div>
    </article>'''
ex_c = f'''
<h1 class="statement">Where we've built systems</h1>
<p class="sub muted">Three companies, from a fast-growing marketplace to global enterprise. This is where the methods we bring to every engagement were learned.</p>
<div class="xrows">{xp}</div>
<p class="small muted" style="margin-top:32px;max-width:72ch">This experience was gained by our founder while employed at these companies. Layer One opened for studio engagements in 2026; our first studio clients will be listed here as their case studies are published.</p>
'''
write("clients.html", head("Experience — Layer One", "Design systems built by the Layer One team at CARS24, IBM and JPMorgan Chase.")
      + shell("experience", [("CARS24", "#cars24"), ("IBM", "#ibm"), ("JPMorgan Chase", "#jpmc")], ex_c))

# ======================= Studio (about) =======================
# Studio banner: a 10 x 3 tile grid built from the mark, the L1 monogram and the layered wordmark.
INK, PAPER, SIG, RAISED, RULE, MUTED = "#0b0d12", "#ecece8", "#ff6b3d", "#1b1f28", "#2a2f3a", "#9aa0aa"


def _star(x, y, size, fill, spin=None):
    s = size / 100
    cls = f' class="sb-turn" style="animation-delay:{spin}s"' if spin is not None else ""
    return f'<g transform="translate({x} {y}) scale({s})"><path{cls} fill="{fill}" fill-rule="evenodd" d="{STAR}"/></g>'


def _tile(kind, x, y, n):
    t = f'<rect x="{x + 4}" y="{y + 4}" width="92" height="92" rx="8"'
    if kind == "acc":
        return t + f' fill="{SIG}"/>' + _star(x + 22, y + 22, 56, INK, spin=n * 0.7)
    if kind == "paper":
        return t + f' fill="{PAPER}"/><text x="{x + 50}" y="{y + 67}" text-anchor="middle" font-family="Schibsted Grotesk, sans-serif" font-weight="800" font-size="46" letter-spacing="-3" fill="{INK}">L1</text>'
    if kind == "pstar":
        return t + f' fill="{PAPER}"/>' + _star(x + 22, y + 22, 56, SIG, spin=n * 0.7)
    if kind == "ink":
        return (t + f' fill="{RAISED}"/>'
                + "".join(f'<g transform="translate({x + 20 + d} {y + 20 + d}) scale(.52)" opacity="{o}"><path fill="none" stroke="{SIG}" stroke-width="3" fill-rule="evenodd" d="{STAR}"/></g>' for d, o in ((8, .3), (4, .6)))
                + _star(x + 20, y + 20, 52, SIG))
    # "line": an outlined tile with the mark drawn as a construction drawing
    return (t + f' fill="none" stroke="{RULE}" stroke-width="1.5"/>'
            f'<circle cx="{x + 50}" cy="{y + 50}" r="28" fill="none" stroke="{MUTED}" stroke-dasharray="2 4"/>'
            f'<path d="M{x + 22} {y + 50}h56M{x + 50} {y + 22}v56" stroke="{RULE}"/>'
            f'<g transform="translate({x + 22} {y + 22}) scale(.56)"><path fill="none" stroke="{MUTED}" stroke-width="2.4" fill-rule="evenodd" d="{STAR}"/></g>')


_GRID = [["ink", "paper", "acc", "F", "F", "line", "pstar", "acc", "ink", "paper"],
         ["acc", "line", "pstar", "F", "F", "paper", "ink", "line", "acc", "pstar"],
         ["paper", "acc", "ink", "line", "paper", "acc", "W", "W", "W", "ink"]]
_art = f'<rect width="1000" height="300" fill="{INK}"/>'
_n = 0
for r, row in enumerate(_GRID):
    for c, kind in enumerate(row):
        if kind in ("F", "W"):
            continue
        _art += _tile(kind, c * 100, r * 100, _n)
        _n += 1
# 2 x 2 feature: the mark with layered offset copies behind it
_art += f'<rect x="304" y="4" width="192" height="192" rx="8" fill="{SIG}"/>'
_art += "".join(f'<g transform="translate({340 + d} {40 + d}) scale(1.2)" opacity="{o}"><path fill="none" stroke="{INK}" stroke-width="1.6" fill-rule="evenodd" d="{STAR}"/></g>' for d, o in ((16, .25), (8, .5)))
_art += _star(340, 40, 120, INK)
# 3 x 1 wordmark plate
_art += (f'<rect x="604" y="204" width="292" height="92" rx="8" fill="{PAPER}"/>'
         + "".join(f'<text x="{750 + d}" y="{264 + d}" text-anchor="middle" font-family="Schibsted Grotesk, sans-serif" font-weight="800" font-size="42" letter-spacing="-1.5" word-spacing="10" '
                   + (f'fill="{INK}"' if d == 0 else f'fill="none" stroke="{SIG}" stroke-width="1.4" opacity="{o}"') + '>LAYER ONE</text>'
                   for d, o in ((6, .45), (3, .8), (0, 1))))
STUDIO_ART = f'<svg viewBox="0 0 1000 300" role="img" aria-label="Layer One mark, monogram and wordmark tiles">{_art}</svg>'

services_list = ["Design system audits", "Token architecture", "Colour systems and accessibility", "Core component libraries",
                 "Multi-brand and multi-market theming", "Pattern libraries", "Documentation", "Governance and contribution models",
                 "Design and engineering workflows", "Design system checks and tooling", "Team workshops and training", "Adoption measurement"]
svc_rows = "".join(f"<li>{s}<span>{i + 1:02d}</span></li>" for i, s in enumerate(services_list))

st_c = f'''
<h1 class="statement" id="overview">A design systems studio in Bangalore, building the shared foundations product teams ship on.</h1>
<div class="studio-banner">{STUDIO_ART}</div>
<p class="about-p">Layer One was started by Aniket Pandey after six years inside design systems teams: first at IBM in Bangalore, then leading the CARS24 design system through a rebrand across three countries, and now on the design systems team at JPMorgan Chase.</p>
<p class="about-p muted">The same problems came up everywhere. Teams didn't need another component kit. They needed decisions that hold across products, a way to run the system without becoming a bottleneck, and a reason for people to use it. That's the work Layer One exists to do, and it's the only work we do.</p>
{trust("Experience from")}
<div class="facts3">
  <div><strong>6 years</strong><span>building and running design systems</span></div>
  <div><strong>70+ / 200+</strong><span>designers and engineers on one system at CARS24</span></div>
  <div><strong>1,500+</strong><span>designers and engineers using tools at JPMorgan Chase</span></div>
</div>

<h2 class="label" id="founder">founder</h2>
<div class="founder">
  <img src="assets/studio/aniket.jpg" alt="Aniket Pandey" width="240" height="240">
  <div>
    <h3>Aniket Pandey</h3>
    <p class="role">Founder, Layer One. Bangalore, India.</p>
    <p>A designer who has spent most of his career on design systems, and who is comfortable close to code. He runs office hours, workshops and mentoring for designers new to systems, and writes about governance and tokens.</p>
    <ol class="timeline">
      <li><b>{logo_tile("jpmc", size=28)}</b><span>Senior Designer, Design Systems, 2025–now. Patterns used across the company, an AI workflow that drafts new patterns, and tools that check design files and code against the system.</span></li>
      <li><b>{logo_tile("cars24", size=28)}</b><span>Design Systems Lead, 2024–25. A system for 60+ designers and 100+ engineers across 10+ products; new palette and tokens for the rebrand; governance; pattern library. System Architect Award.</span></li>
      <li><b>{logo_tile("ibm", size=28)}</b><span>UX Designer, 2021–24, Bangalore. Built and launched design systems for products used worldwide; contribution process, releases and training.</span></li>
    </ol>
  </div>
</div>

<h2 class="label" id="services">what we do</h2>
<ol class="rows">{svc_rows}</ol>

<h2 class="label" id="how">how we work</h2>
<ol class="rules">
  <li>Small and senior. The person on the first call does the work.<span>01</span></li>
  <li>We work in your Figma files and your repository, not in a separate deck.<span>02</span></li>
  <li>Every engagement starts with an audit, so we fix what matters first.<span>03</span></li>
  <li>Weekly demos and written decisions, so nothing is a surprise.<span>04</span></li>
  <li>Fixed prices and fixed timelines. No hourly billing.<span>05</span></li>
  <li>We leave documentation and a governance model your team can run alone.<span>06</span></li>
</ol>

<h2 class="label" id="invitation">invitation</h2>
<div class="invite">
  <div><h3>Founding partners, 2027.</h3></div>
  <div>
    <p>We're choosing three teams to be Layer One's first studio partners. You get 20% off any engagement and a senior team that treats your system as its flagship. We get to publish what we build together.</p>
    <div class="slots" aria-label="Three slots open"><span></span><span></span><span></span></div>
    <a class="pill" href="contact.html?offer=founding">Apply for a slot</a>
  </div>
</div>

<h2 class="label" id="our-work">our work.</h2>
<div class="link-bars">
  <a href="work.html">Case studies: colour, tokens, governance and patterns at CARS24</a>
  <a href="work.html#projects">Projects: JPMorgan Chase, IBM and more from CARS24</a>
  <a href="pricing.html">Pricing: fixed prices for every engagement</a>
  <a href="lab.html">Lab: tools we built to think with</a>
</div>
'''
write("studio.html", head("Studio — Layer One", "Layer One is a design systems studio in Bangalore, India, founded by Aniket Pandey.")
      + shell("studio", [("Overview", "#overview"), ("Founder", "#founder"), ("What we do", "#services"), ("How we work", "#how"), ("Invitation", "#invitation"), ("Our work", "#our-work")], st_c, card="bar"))

# ======================= Lab =======================
questions = [
    ("where", "Where is it needed?", "Work in main products helps the most people.", [("20", "Main products"), ("15", "Smaller products"), ("5", "One small team"), ("x", "Nowhere")]),
    ("reuse", "How many can reuse it?", "A design system is for shared things.", [("20", "Many teams"), ("15", "A few teams"), ("5", "One team"), ("x", "Only one product")]),
    ("exists", "Do we already have it?", "Filling a real gap beats rebuilding what works.", [("15", "No"), ("10", "Partly"), ("5", "Mostly"), ("x", "Fully solved")]),
    ("effort", "How hard is it to build?", "Quick wins go first.", [("15", "Under a week"), ("10", "1–3 weeks"), ("5", "3+ weeks"), ("x", "Not worth it")]),
]
qs = "".join(
    f'<div class="scorer-q"><fieldset><legend>{q}</legend><p class="help">{h}</p><div class="seg">'
    + "".join(f'<label><input type="radio" name="{n}" value="{v}"><span>{"✕ " if v == "x" else "<b>" + v + "</b> "}{t}</span></label>' for v, t in o)
    + "</div></fieldset></div>" for n, q, h, o in questions)
themes = [("New brand", "#4736fe", "color-blue-500", "color-action-primary"), ("Old brand", "#0059a3", "color-blue-700", "color-action-primary"),
          ("Loans theme", "#1f3a8a", "nbfc-color-navy-500", "nbfc-color-action-primary"), ("Mint accent", "#2bb58a", "color-mint-500", "color-action-accent")]
tbtns = "".join(f'<button type="button" class="btn-line" data-theme-pick data-hex="{h}" data-prim="{p}" data-sem="{s}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (n, h, p, s) in enumerate(themes))
lab_c = f'''
<h1 class="statement">Lab</h1>
<p class="sub muted">Small tools we built to think with. They're the same methods we use on client systems, and they're free to use.</p>
<section class="tool" id="ramp" data-ramp aria-labelledby="ramp-t">
  <div class="tool-head"><div><h3 id="ramp-t">OKLCH ramp builder</h3><p>Pick a hue and a chroma. You get ten perceptually even steps, fitted to the sRGB gamut, with a contrast check on every step and tokens ready to paste.</p></div></div>
  <div class="ctrl">
    <label>Hue <span data-hv></span><input type="range" name="hue" min="0" max="360" value="275"></label>
    <label>Chroma <span data-cv></span><input type="range" name="chroma" min="0.02" max="0.32" step="0.01" value="0.24"></label>
    <label>Name<input class="btn-line" name="rname" value="brand" style="height:32px"></label>
  </div>
  <div class="ramp-out"></div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px;gap:12px;flex-wrap:wrap"><span class="small muted">Contrast is measured against white and black text.</span><button class="btn-line" type="button" data-copy>Copy tokens</button></div>
  <pre class="code-out"></pre>
</section>
<section class="tool" id="chain" data-chain style="--brand:#4736fe" aria-labelledby="chain-t">
  <div class="tool-head"><div><h3 id="chain-t">Token chain</h3><p>The four layers between a hex code and a button, from the CARS24 architecture. Switch the theme: components never change, only the mapping underneath.</p></div></div>
  <div class="ctrl" style="gap:8px">{tbtns}</div>
  <div class="chain">
    <div><span>Value</span><div class="sw"></div><code data-v>#4736FE</code></div>
    <div><span>Primitive</span><code data-p>color-blue-500</code></div>
    <div><span>Semantic</span><code data-s>color-action-primary</code></div>
    <div><span>Component</span><code>button-background-primary</code><div class="sw" style="height:34px;border-radius:8px;display:grid;place-items:center;color:#fff;font-size:13px;font-weight:600">Get best price</div></div>
  </div>
</section>
<section class="tool" id="scorecard" aria-labelledby="sc-t">
  <div class="tool-head"><div><h3 id="sc-t">Request scorecard</h3><p>The 70-point model that ended the loudest-voice backlog at CARS24. Score any component request in four questions.</p></div><a class="btn-line" href="work/cars24-governance.html">Read the case study</a></div>
  <form class="scorer" data-scorer onsubmit="return false">{qs}
    <div class="scorer-out" aria-live="polite"><div class="scorer-total"><span data-total>0</span> <small>/ 70</small></div><div class="scorer-verdict"><strong data-verdict></strong><span data-detail></span></div></div>
  </form>
</section>
'''
write("lab.html", head("Lab — Layer One", "Free design system tools from Layer One: an OKLCH ramp builder, a token chain explorer and a request scorecard.")
      + shell("lab", [("Ramp builder", "#ramp"), ("Token chain", "#chain"), ("Scorecard", "#scorecard")], lab_c, card="bar"))

# ======================= Writing =======================
posts = [
    ("blog-librarian-vs-leader.html", "Most design system leads are just librarians", "Leadership · 12 min", "assets/images/blog/librarian-vs-leader.png", False),
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "Operations · 5 min · Medium", "assets/images/blog/operational-backbone.png", True),
    ("https://medium.com/@layerone_11803/most-design-systems-are-just-expensive-ui-libraries-e0cc8b146f2d", "Most design systems are just expensive UI libraries", "Strategy · 8 min · Medium", "assets/images/blog/scaling.png", True),
    ("https://medium.com/@layerone/foundations-of-modern-design-systems", "Foundations of modern design systems", "Architecture · 5 min · Medium", "assets/images/blog/foundations.png", True),
]
pc = "".join(f'<a class="wcard" href="{h}"{" target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) if e else ""}><div class="m"><img src="{i}" alt="" loading="lazy"></div><h3>{t}</h3><span>{g}</span></a>' for h, t, g, i, e in posts)
bl_c = f'''
<h1 class="statement">Writing</h1>
<p class="sub muted">Long-form notes on governance, tokens and the organisational side of design systems.</p>
<div class="cards2" style="margin-top:24px">{pc}</div>
'''
write("blog.html", head("Writing — Layer One", "Notes on design system governance, tokens and leadership from Layer One.")
      + shell("writing", [("All writing", "#main"), ("Medium", MEDIUM)], bl_c, card="bar"))

# ======================= Short project pages =======================
for p in others:
    c = COMPANIES[p["co"]]
    scope = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in p["scope"])
    pts = "".join(f"<li>{x}</li>" for x in p["points"])
    rel = [q for q in PROJECTS if q["slug"] != p["slug"] and (q["co"] == p["co"] or q["case"])][:2]
    nxt = "".join(f'''<a class="nx" href="{q["slug"]}.html" style="--f:{q["f"]};--ft:{q["ft"]}"><img src="../{q["cover"]}" alt="" loading="lazy"><span>{q["kind"]}</span><h3>{q["title"].split(": ", 1)[1][0].upper() + q["title"].split(": ", 1)[1][1:]}</h3></a>''' for q in rel)
    illus = '<p class="illus-note">This image is an illustration we drew to describe the work. The real screens belong to the company and can\'t be shared.</p>' if p.get("illus") else ""
    body = f'''<main id="main" class="cs" style="--f:{p["f"]}">
  <header class="cs-hero">
    <p class="crumb"><a href="../work.html">Work</a> / {p["client"]}</p>
    <div class="cs-id">{logo_tile(p["co"], depth=1, size=48, label=False)}<span>{p["client"]} · {p["year"]} · {p["kind"]}</span></div>
    <h1>{p["title"].split(": ", 1)[1][0].upper() + p["title"].split(": ", 1)[1][1:]}</h1>
    <p class="cs-lede">{p["blurb"]}</p>
    <dl class="cs-meta cs-meta--3">{scope}</dl>
    <figure class="cs-cover"><img src="../{p["cover"]}" alt="{p["title"]}" width="1800" height="1238"></figure>
    {illus}
  </header>
  <section class="cs-wrap ch" aria-labelledby="what-h">
    <header class="ch-head"><span class="ch-n">01</span><div><h2 id="what-h">What the work covered</h2><p>{c["role"]} at {c["name"]}, {c["years"]}.</p></div></header>
    <div class="ch-body"><ul class="pts">{pts}</ul>
      <div class="m-more" style="border-style:solid;padding:16px"><p style="font-size:16px">A full case study for this project isn't public. <a href="../contact.html">Ask for a walkthrough</a> and we'll take you through the system on a call.</p></div></div>
  </section>
  <section class="cs-wrap cs-end">
    <div class="cs-cta"><div><h2>Need this for your product?</h2><p>Start with a two-week audit, $1,500 fixed.</p></div>
      <div class="btn-row"><a class="pill pill--accent" href="../pricing.html">See pricing</a><a class="pill" href="../contact.html">Start a project</a></div></div>
    <h2 class="nx-h">More work</h2><div class="nxs">{nxt}</div>
  </section>
</main>'''
    write(f"work/{p['slug']}.html", head(f"{p['title']} — Layer One", p["blurb"], depth=1, og=p["cover"])
          + topbar("work", depth=1) + body + close(depth=1))

# services.html now lives at pricing.html
write("services.html", '''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Pricing — Layer One</title>
<meta http-equiv="refresh" content="0; url=pricing.html"><link rel="canonical" href="https://www.layerone.co.in/pricing.html"></head>
<body><p>This page has moved to <a href="pricing.html">pricing</a>.</p></body></html>
''')
