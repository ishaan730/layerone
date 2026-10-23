from common import *

frames = "".join(frame(p) for p in PROJECTS)

notes = [
    ("CARS24", "Used cars, loans, insurance; India, UAE, Australia",
     "Led the design system for <b>10+ products in three countries</b>: a new palette, a token architecture, governance and a pattern library, through a full rebrand."),
    ("IBM", "Enterprise software, worldwide",
     "Built and launched design systems for products used around the world, and set up a clear way for other teams to contribute to them."),
    ("JPMorgan Chase", "Financial services",
     "Design patterns and design-system checking tools used by a community of <b>500+ designers and 1,000+ engineers</b>."),
    ("Riyadh Air", "Airline, Saudi Arabia",
     "A bilingual design system and pattern library for a new airline's digital products, in English and Arabic."),
    ("District by Zomato", "Movies, events and dining",
     "A visual design system for Zomato's going-out app, from colour and illustration to category navigation."),
    ("US pharmaceutical company", "B2B healthcare",
     "Framework-agnostic web components on a semantic token layer for a next-generation B2B ordering platform."),
]
note_html = "".join(f"<div><h3>{a}</h3><p class='stage-tag'>{b}</p><p>{c}</p></div>" for a, b, c in notes)

rules = [
    "A design system is an agreement, not a library",
    "Audit before you build",
    "Name things so people can guess them",
    "Tokens first, components second",
    "Accessible by default, not by audit",
    "Every decision comes with a reason",
    "Build where the system lives: your files, your repo",
    "Measure time saved, not usage",
    "Docs decide adoption",
    "Leave the team able to run it without us",
]
rules_html = "".join(f"<li>{r}<span>RULE #{i + 1}</span></li>" for i, r in enumerate(rules))

posts = [
    ("blog-librarian-vs-leader.html", "Most design system leads are just librarians", "Leadership", "assets/images/blog/librarian-vs-leader.png", False),
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "Operations", "assets/images/blog/operational-backbone.png", True),
    ("https://medium.com/@layerone/foundations-of-modern-design-systems", "Foundations of modern design systems", "Architecture", "assets/images/blog/foundations.png", True),
    ("https://medium.com/@layerone/scaling-ui-engineering", "Scaling UI engineering across organisations", "Engineering", "assets/images/blog/scaling.png", True),
]
post_html = "".join(
    f'<a class="wcard" href="{h}"{" target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) if ext else ""}><div class="m"><img src="{img}" alt="" loading="lazy"></div><h3>{t}</h3><span>{tag}</span></a>'
    for h, t, tag, img, ext in posts)

content = f'''
<div class="banner">{BANNER}</div>
<h1 class="statement"><span class="accent">Layer One</span> is a design systems studio for product companies.</h1>
<p class="sub muted">We build design systems, scale them across products, brands and markets, and set up the governance that keeps teams using them. Design systems are all we do.</p>
{stage()}
<ul class="strip" aria-label="Where our team has built design systems">
  <li>CARS24</li><li>IBM</li><li>JPMorgan Chase</li><li>Riyadh Air</li><li>Zomato</li><li>HDFC</li>
</ul>

<h2 class="label" id="work">select work:</h2>
<div class="frames">{frames}</div>
<a class="more-bar" href="work.html">View all work</a>

<h2 class="label" id="where">where we've built systems:</h2>
<div class="blurbs">{note_html}</div>
<a class="more-bar" href="clients.html" style="margin-top:32px">All clients</a>

<h2 class="label" id="offer">how to start:</h2>
<div class="invite">
  <div>
    <h3>Start with a two-week audit.</h3>
  </div>
  <div>
    <p>We map every style, component and token you have in Figma and code, check accessibility, and hand you a ranked plan for what to fix first. Fixed price, $3,500.</p>
    <div class="slots" aria-label="Founding partner slots for 2027: three open"><span></span><span></span><span></span></div>
    <p>Three founding partners in 2027 get 20% off any engagement, and we publish the case study together.</p>
    <a class="pill" href="services.html">See engagements and pricing</a>
  </div>
</div>

<h2 class="label" id="rules">rules we work by:</h2>
<ol class="rules">{rules_html}</ol>

<div class="label-row"><h2 class="label" id="writing">writing:</h2><a class="pill" href="blog.html">Read it all</a></div>
<div class="cards2">{post_html}</div>

<section class="reach" aria-labelledby="reach-t">
  <h2 id="reach-t">Where to reach out?</h2>
  <p>Send an email to <a href="mailto:{EMAIL}">{EMAIL}</a>, or <a href="{CAL}" target="_blank" rel="noopener">book a 30-minute call</a>.</p>
</section>
'''

sub = [("Work", "#work"), ("Clients", "#where"), ("How to start", "#offer"), ("Rules", "#rules"), ("Writing", "#writing")]
html = head("Layer One — Design systems studio",
            "Layer One is a design systems studio in Bangalore. We build, scale and govern design systems for product companies.") + shell("home", sub, content)
write("index.html", html)
