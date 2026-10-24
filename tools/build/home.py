from common import *

frames = "".join(frame(p) for p in PROJECTS)

exp = ""
for key, stat, what in [
    ("cars24", ("10+", "products on one token system, in 3 countries"),
     "Led the design system for 70+ designers and 200+ engineers: a new palette and token architecture for the rebrand, governance, and a pattern library."),
    ("ibm", ("Several", "product design systems built and launched"),
     "Built design systems for products used around the world, with a contribution process, regular releases and training."),
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
    ("blog-librarian-vs-leader.html", "Most design system leads are just librarians", "Leadership", "assets/images/blog/librarian-vs-leader.png", False),
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "Operations", "assets/images/blog/operational-backbone.png", True),
]
post_html = "".join(
    f'<a class="wcard" href="{h}"{" target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) if ext else ""}><div class="m"><img src="{img}" alt="" loading="lazy"></div><h3>{t}</h3><span>{tag}</span></a>'
    for h, t, tag, img, ext in posts)

content = f'''
<h1 class="statement hero-statement"><span class="accent">Layer One</span> builds and scales design systems for product companies.</h1>
<p class="sub muted">A design systems studio in Bangalore. We set up the foundations, scale them across products and markets, and put in the governance that keeps teams using them.</p>
{reel()}
<div class="trust">
  <p>Built by the team behind the design systems at</p>
  <ul>{"".join("<li>" + logo_tile(k) + "</li>" for k in ("cars24", "ibm", "jpmc"))}</ul>
</div>

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
    <a class="pill" href="pricing.html">See pricing</a>
  </div>
</div>

<h2 class="label" id="rules">rules we work by:</h2>
<ol class="rules">{rules_html}</ol>

<div class="label-row"><h2 class="label" id="writing">writing:</h2><a class="pill" href="blog.html">Read it all</a></div>
<div class="cards2">{post_html}</div>

<section class="reach" aria-labelledby="reach-t">
  <h2 id="reach-t">Where to reach out?</h2>
  <p>Send an email to <a href="mailto:{EMAIL}">{EMAIL}</a>, or <a href="contact.html">tell us about your system</a>.</p>
</section>
'''

sub = [("Work", "#work"), ("Experience", "#experience"), ("How to start", "#offer"), ("Rules", "#rules"), ("Writing", "#writing")]
html = head("Layer One — Design systems studio",
            "Layer One is a design systems studio in Bangalore. We build, scale and govern design systems for product companies.",
            og="assets/video/hero-poster.jpg") + shell("home", sub, content)
write("index.html", html)
