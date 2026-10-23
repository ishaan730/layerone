import os

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CAL = "https://cal.com/layerone"
EMAIL = "layerone@proton.me"
LINKEDIN = "https://www.linkedin.com/company/layerone.co.in/"
X = "https://x.com/LayeroneStudios"
MEDIUM = "https://medium.com/@layerone_11803"

ARROW = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_SHIFT = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

LOGO = ('<svg viewBox="0 0 100 100" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" '
        'd="M50 0a50 50 0 1 1 0 100A50 50 0 0 1 50 0Z'
        'M16.3 50A34 34 0 0 0 50 16.3V49.2a.8.8 0 0 1-.8.8Z'
        'M83.7 50A34 34 0 0 0 50 83.7V50.8a.8.8 0 0 1 .8-.8Z"/></svg>')

THEME_ICON = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.25" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.75a6.25 6.25 0 0 1 0 12.5Z" fill="currentColor"/></svg>'

NAV = [("work", "Work", "work.html"), ("services", "Services", "services.html"),
       ("approach", "Approach", "index.html#approach"), ("writing", "Writing", "blog.html")]


def head(title, desc, depth=0, og_image="assets/work/tokens/cover.jpg"):
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
<meta property="og:image" content="https://www.layerone.co.in/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{p}assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css">
<script>try{{var t=localStorage.getItem("l1-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(active=None, depth=0):
    p = "../" * depth
    links = "".join(
        f'<a href="{p}{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for key, label, href in NAV)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}index.html" aria-label="Layer One, home">{LOGO}<span>Layer One</span></a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <button class="menu-toggle" type="button" aria-expanded="false">Menu</button>
    <div class="header-actions">
      <button class="theme-toggle" type="button" data-theme-toggle>{THEME_ICON}</button>
      <a class="btn btn--small" href="{CAL}" target="_blank" rel="noopener">Book a call</a>
    </div>
  </div>
</header>
'''


def cta(title="Tell us where your system is today.",
        body="Thirty minutes is enough to tell whether we're the right fit. If we're not, we'll say so and point you somewhere better."):
    return f'''<section class="cta" aria-labelledby="cta-title">
  <div class="wrap">
    <h2 id="cta-title">{title}</h2>
    <div>
      <p>{body}</p>
      <div class="btn-row">
        <a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a>
        <a class="btn btn--ghost" href="mailto:{EMAIL}">Email {EMAIL}</a>
      </div>
    </div>
  </div>
</section>
'''


def footer(depth=0):
    p = "../" * depth
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html">{LOGO}<span>Layer One</span></a>
        <p class="footer-blurb">A design systems studio. We help product companies build, scale and govern their design systems.</p>
      </div>
      <div>
        <h2>Studio</h2>
        <ul>
          <li><a href="{p}work.html">Work</a></li>
          <li><a href="{p}services.html">Services</a></li>
          <li><a href="{p}index.html#approach">Approach</a></li>
          <li><a href="{p}index.html#pricing">Pricing</a></li>
        </ul>
      </div>
      <div>
        <h2>Case studies</h2>
        <ul>
          <li><a href="{p}work/cars24-tokens.html">Colour and tokens</a></li>
          <li><a href="{p}work/cars24-governance.html">Governance</a></li>
          <li><a href="{p}work/cars24-pattern-library.html">Pattern library</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{CAL}" target="_blank" rel="noopener">Book a call</a></li>
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
          <li><a href="{X}" target="_blank" rel="noopener">X</a></li>
          <li><a href="{MEDIUM}" target="_blank" rel="noopener">Medium</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>&copy; <span data-year>2026</span> Layer One Design Systems</span>
      <span>Made in India, working with teams everywhere</span>
    </div>
  </div>
</footer>
<script src="{p}assets/site.js" defer></script>
</body>
</html>
'''


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path, len(html) // 1024, "KB")


# Shared facts about the three projects, so every page quotes the same numbers.
CASES = {
    "tokens": dict(
        href="work/cars24-tokens.html", img="assets/work/tokens/cover.jpg",
        title="One colour system for 10+ products in three countries",
        short="Colour and token system",
        meta="Foundations at CARS24",
        summary="CARS24 grew from one product to more than six across India, the UAE and Australia, and every team had built its own colours. We rebuilt the palette, designed a four-layer token architecture and gave every product one source of truth. The palette became the colour of the CARS24 rebrand.",
        metrics=[("65%", "faster design-to-development handoff"), ("5 → 1", "button implementations merged into one"),
                 ("10+", "product lines on one token system"), ("~$156k", "estimated yearly engineering savings")],
        scope=["Colour audit", "Palette in OKLCH", "WCAG contrast", "Token architecture", "Multi-brand theming", "Figma to code"]),
    "governance": dict(
        href="work/cars24-governance.html", img="assets/work/governance/cover.jpg",
        title="How the design system team stopped being the bottleneck",
        short="Governance and contribution",
        meta="Operations at CARS24",
        summary="Every team needed something from the design system, and one small team couldn't keep up. Requests arrived by DM, decisions felt random and teams built around the system. We designed one front door, a 70-point scorecard anyone can apply, three ownership tiers and a contribution playbook.",
        metrics=[("70 pts", "scorecard that replaced the loudest-voice backlog"), ("7 steps", "one path for every request, bug or component"),
                 ("3 tiers", "core, extended and custom ownership"), ("Quarterly", "audits that feed drift back into the backlog")],
        scope=["Intake", "Prioritisation model", "Ownership tiers", "Contribution playbook", "Release rituals", "Audits"]),
    "patterns": dict(
        href="work/cars24-pattern-library.html", img="assets/work/patterns/cover.jpg",
        title="Pages built from tested blocks, not from scratch",
        short="Pattern library",
        meta="Adoption at CARS24",
        summary="CARS24 was becoming a super app and launching new services almost every month, and every homepage and landing page started from a blank canvas. We built a pattern library of page blocks with content rules, wired to the CMS and the design tokens, so teams assemble pages instead of designing them.",
        metrics=[("~43%", "less time to design and build a new page"), ("3 months", "to reach every major redesign"),
                 ("~$212k", "saved in design and development time"), ("3", "countries building from one library")],
        scope=["Page audit", "Pattern families", "Content rules", "CMS integration", "Spec sheets", "Request template"]),
}
