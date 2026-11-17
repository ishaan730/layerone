from common import *

frames = "".join(frame(p) for p in PROJECTS)

exp = ""
for key, stat, what in [
    ("cars24", ("10+", "products on one token system, in 3 countries"),
     "Led the design system for 70+ designers and 200+ engineers: a new palette and token architecture for the rebrand, governance, and a pattern library."),
    ("ibm", ("71", "components for an airline, 40+ for a pharmacy storefront"),
     "Built design systems for IBM clients Cardinal Health and Riyadh Air, from foundations and tokens to governance, contribution and releases."),
    ("jpmc", ("500+", "designers and 1,000+ engineers using the checks"),
     "Company-wide design patterns, an AI workflow that drafts them, and tools that check design files and code against the system."),
]:
    c = COMPANIES[key]
    links = "".join(f'<a href="{href(p)}">{short(p)}</a>' for p in PROJECTS if p["co"] == key)
    exp += f'''<article class="xp">
      <header>{logo_tile(key, label=False)}<div><h3>{c["name"]}</h3><p>{c["role"]} · {c["years"]}</p></div></header>
      <p class="xp-stat"><strong>{stat[0]}</strong> {stat[1]}</p>
      <p class="xp-what">{what}</p>
      <nav aria-label="{c["name"]} projects">{links}</nav>
    </article>'''

rules = ["A design system is an agreement, not a library", "Audit before you build", "Name things so people can guess them",
         "Tokens first, components second", "Accessible by default, not by audit", "Every decision comes with a reason",
         "Build where the system lives: your files, your repo", "Measure time saved, not usage", "Docs decide adoption",
         "Leave the team able to run it without us"]
rules_html = "".join(f"<li>{r}<span>RULE #{i + 1}</span></li>" for i, r in enumerate(rules))

posts = [
    ("writing/what-is-a-design-system.html", "What is a design system? A plain-English guide", "Fundamentals · Guide", "assets/images/writing/what-is-a-design-system.jpg", False),
    ("writing/design-system-operating-model.html", "The design system operating model", "Operating model · Guide", "assets/images/writing/design-system-operating-model.jpg", False),
    ("writing/design-tokens.html", "Design tokens: the complete guide", "Foundations & tokens · Guide", "assets/images/writing/design-tokens.jpg", False),
    ("writing/design-system-roi.html", "Design system ROI: an honest model", "Business case", "assets/images/writing/design-system-roi.jpg", False),
]
post_html = "".join(
    f'<a class="wcard" href="{h}"{" target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) if ext else ""}><div class="m"><img src="{img}" alt="" loading="lazy"></div><h3>{t}</h3><span>{tag}</span></a>'
    for h, t, tag, img, ext in posts)

content = f'''
<h1 class="statement hero-statement"><span class="accent">Layer One</span> builds, scales and governs design systems for product teams worldwide.</h1>
<p class="sub muted">A design system agency and consultancy, based in Bangalore, India. We audit what you have, build the foundations and components, put in the governance that keeps teams using them, and make the system ready for AI agents. Fixed prices in US dollars, with working hours that overlap the US, Europe and the Gulf.</p>
{reel()}
{trust("Built by the team behind the design systems at")}

<h2 class="label" id="work">select work:</h2>
<div class="frames">{frames}</div>
<a class="more-bar" href="work.html">View all work</a>

<h2 class="label" id="experience">where we've built systems:</h2>
<div class="xps">{exp}</div>

<h2 class="label" id="offer">how to start:</h2>
<div class="invite">
  <div><h3>Start with a two-week audit.</h3></div>
  <div>
    <p>We map every style, component and token you have in Figma and code, check accessibility, and give you a ranked plan for what to fix first. <b>$1,500, fixed.</b> Credited in full if you go on to a Foundations build.</p>
    <div class="slots" aria-label="Founding partner slots for 2027: three open"><span></span><span></span><span></span></div>
    <p>Three founding partners in 2027 get 20% off, and we publish the case study together.</p>
    <div class="btn-row"><a class="pill" href="services/design-system-audit.html">How the audit works</a><a class="pill" href="pricing.html">See pricing</a></div>
  </div>
</div>

<h2 class="label" id="services">design system services:</h2>
<div class="link-bars">
  <a href="services/design-system-audit.html">Design system audit: two weeks, $1,500 fixed</a>
  <a href="services/design-system-development.html">Design system development: foundations in six weeks, $5,900</a>
  <a href="services/design-system-consulting.html">Design system consulting: monthly, $2,900, pause any time</a>
  <a href="services/ai-ready-design-system.html">AI-ready design systems: make your system usable by AI agents</a>
</div>
<p class="small muted" style="margin-top:12px">Based in Bangalore, India. Working with product teams in the US, Europe, the Gulf and Asia-Pacific. <a href="studio.html#worldwide">How we work across time zones</a>.</p>

<h2 class="label" id="rules">rules we work by:</h2>
<ol class="rules">{rules_html}</ol>

<div class="label-row"><h2 class="label" id="writing">writing:</h2><a class="pill" href="blog.html">Read it all</a></div>
<div class="cards2">{post_html}</div>

<section class="reach" aria-labelledby="reach-t">
  <h2 id="reach-t">Where to reach out?</h2>
  <p>Send an email to <a href="mailto:{EMAIL}">{EMAIL}</a>, or <a href="contact.html">tell us about your system</a>.</p>
</section>
'''

sub = [("Work", "#work"), ("Experience", "#experience"), ("How to start", "#offer"), ("Services", "#services"), ("Rules", "#rules"), ("Writing", "#writing")]
html = head("Design System Agency & Consultancy | Layer One",
            "Layer One is a design system agency and consultancy for product teams worldwide: audits, builds, governance and AI-ready design systems, at fixed prices.",
            ).replace("</head>", f'<link rel="preload" as="image" href="assets/video/hero-poster.jpg?v={ver("assets/video/hero-poster.jpg")}" fetchpriority="high">\n</head>', 1) + shell("home", sub, content)
write("index.html", html)
