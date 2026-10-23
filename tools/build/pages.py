from common import *

# ======================= Work =======================
cases = [p for p in PROJECTS if p["case"]]
others = [p for p in PROJECTS if not p["case"]]
work_c = f'''
<h1 class="statement" id="case-studies">featured work</h1>
<p class="sub muted">Full case studies, with the problem, the decisions and the numbers.</p>
<div class="frames" style="margin-top:20px">{"".join(frame(p, show_year=True) for p in cases)}</div>
<h2 class="label" id="projects">more projects</h2>
<p class="sub muted" style="margin:-8px 0 20px">Systems the team has shipped. Full write-ups on request.</p>
<div class="frames frames--2">{"".join(frame(p, show_year=True) for p in others)}</div>
<p class="small muted" style="margin-top:28px;max-width:72ch">The CARS24, IBM and JPMorgan Chase work was led by Aniket Pandey while employed at those companies. Client names and imagery are shown for portfolio purposes.</p>
'''
write("work.html", head("Work — Layer One", "Design systems built by the Layer One team for CARS24, Riyadh Air, District by Zomato and others.")
      + shell("work", [("Featured", "#case-studies"), ("More projects", "#projects")], work_c, card="bar"))

# ======================= Clients =======================
clients = [
    ("CARS24", "10+ products · India, UAE, Australia", "CARS24 is one of India's largest platforms for buying and selling used cars, with loans, insurance and servicing alongside.", "work/cars24-tokens.html"),
    ("IBM", "Enterprise software · worldwide", "IBM builds software and infrastructure for businesses around the world. The team designed and rolled out several product design systems there.", None),
    ("JPMorgan Chase", "Financial services · global", "JPMorgan Chase is one of the world's largest banks. Work there covers design patterns and tools that check work against the design system.", None),
    ("Riyadh Air", "Airline · Saudi Arabia", "Riyadh Air is Saudi Arabia's new national carrier. Its digital products run on a bilingual system in English and Arabic.", "work/riyadh-air.html"),
    ("District by Zomato", "Consumer app · India", "District is Zomato's app for movies, events and dining out in one place.", "work/district.html"),
    ("US pharmaceutical company", "B2B healthcare · USA", "A large US healthcare company rebuilding its B2B ordering platform on web components.", "work/pharma-b2b.html"),
    ("HDFC", "Banking · India", "One of India's largest private-sector banks.", None),
    ("Loans24 and Insure24", "CARS24 businesses · India", "CARS24's lending and insurance businesses, themed from the same core token system.", "work/cars24-tokens.html"),
    ("CARS24 internal tools", "Operations software", "The dashboards and tools CARS24 teams use every day, on their own enterprise design system.", "work/cars24-internal-tools.html"),
]
grid = ""
for n, t, d, h in clients:
    link = f'<p><a href="{h}">See the work</a></p>' if h else ""
    grid += f"<div><h2>{n}</h2><p class='stage-tag'>{t}</p><p>{d}</p>{link}</div>"
cl_c = f'''
<h1 class="statement">Clients</h1>
<p class="sub muted">Companies where our team has built, scaled or governed a design system.</p>
<hr class="hr" style="margin:28px 0 32px">
<div class="client-grid">{grid}</div>
<p class="small muted" style="margin-top:40px;max-width:72ch">Some of this work was done by our founder while employed at the companies named. Layer One opened for studio engagements in 2026; our first studio clients will be listed here as their case studies are published.</p>
'''
write("clients.html", head("Clients — Layer One", "Companies where the Layer One team has built and scaled design systems.")
      + shell("clients", [("All clients", "#main")], cl_c))

# ======================= Studio (about) =======================
STUDIO_ART = ('<svg viewBox="0 0 1000 300" role="img" aria-label="Layer One pattern">'
              '<defs><pattern id="tile" width="100" height="100" patternUnits="userSpaceOnUse">'
              f'<g transform="translate(14 14) scale(.72)"><path fill="currentColor" fill-rule="evenodd" d="{STAR}"/></g></pattern>'
              '<pattern id="tile2" width="100" height="100" patternUnits="userSpaceOnUse">'
              '<text x="50" y="66" text-anchor="middle" font-family="Schibsted Grotesk, sans-serif" font-weight="800" font-size="52" fill="currentColor" letter-spacing="-3">L1</text></pattern></defs>'
              '<rect width="1000" height="300" fill="url(#tile)"/>'
              '<rect x="100" y="0" width="100" height="300" fill="#ecece8"/><rect x="100" y="0" width="100" height="300" fill="url(#tile2)"/>'
              '<rect x="500" y="0" width="100" height="300" fill="#ecece8"/><rect x="500" y="0" width="100" height="300" fill="url(#tile2)"/>'
              '<rect x="800" y="0" width="100" height="300" fill="#ecece8"/><rect x="800" y="0" width="100" height="300" fill="url(#tile2)"/>'
              '</svg>')

services_list = ["Design system audits", "Token architecture", "Colour systems and accessibility", "Core component libraries",
                 "Multi-brand and multi-market theming", "Pattern libraries", "Documentation", "Governance and contribution models",
                 "Design and engineering workflows", "Figma and code parity", "Team workshops and training", "Adoption measurement"]
svc_rows = "".join(f"<li>{s}<span>{i + 1:02d}</span></li>" for i, s in enumerate(services_list))

st_c = f'''
<h1 class="statement" id="overview">A design systems studio in Bangalore, building the shared foundations product teams ship on.</h1>
<div class="studio-banner">{STUDIO_ART}</div>
<p class="about-p">Layer One was started by Aniket Pandey after six years inside design systems teams: first at IBM in Bangalore, then leading the CARS24 design system through a rebrand across three countries, and now on the design systems team at JPMorgan Chase. Along the way the team has worked on systems for Riyadh Air, District by Zomato, a US pharmaceutical company and a number of startups.</p>
<p class="about-p muted">The same problems came up everywhere. Teams didn't need another component kit. They needed decisions that hold across products, a way to run the system without becoming a bottleneck, and a reason for people to use it. That's the work Layer One exists to do, and it's the only work we do.</p>
<div class="facts3">
  <div><strong>6 years</strong><span>building and running design systems</span></div>
  <div><strong>70+ / 200+</strong><span>designers and engineers on one system at CARS24</span></div>
  <div><strong>10+</strong><span>product lines on a single token architecture</span></div>
</div>

<h2 class="label" id="founder">founder</h2>
<div class="founder">
  <img src="assets/studio/aniket.jpg" alt="Aniket Pandey" width="240" height="240">
  <div>
    <h3>Aniket Pandey</h3>
    <p class="role">Founder, Layer One. Bangalore, India.</p>
    <p>A designer who has spent most of his career on design systems, and who is comfortable close to code. He runs office hours, workshops and mentoring for designers new to systems, and writes about governance and tokens.</p>
    <ol class="timeline">
      <li><b>JPMorgan Chase</b><span>Design systems: patterns used across the company, an AI workflow that drafts new patterns, and tools that check design files and code against the system for 500+ designers and 1,000+ engineers.</span></li>
      <li><b>CARS24</b><span>Design Systems Lead, 2024–25. A system for 60+ designers and 100+ engineers across 10+ products; new palette and tokens for the rebrand; governance; pattern library. System Architect Award.</span></li>
      <li><b>IBM</b><span>UX Designer, 2021–24, Bangalore. Built and launched design systems for products used worldwide; contribution process, releases and training.</span></li>
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
  <li>Specialists in front-end, accessibility and brand join when a project needs them.<span>05</span></li>
  <li>We leave documentation and a governance model your team can run alone.<span>06</span></li>
</ol>

<h2 class="label" id="invitation">invitation</h2>
<div class="invite">
  <div><h3>Founding partners, 2027.</h3></div>
  <div>
    <p>We're choosing three teams to be Layer One's first studio partners. You get 20% off any engagement and a senior team that treats your system as its flagship. We get to publish what we build together.</p>
    <div class="slots" aria-label="Three slots open"><span></span><span></span><span></span></div>
    <a class="pill" href="contact.html">Apply for a slot</a>
  </div>
</div>

<h2 class="label" id="our-work">our work.</h2>
<div class="link-bars">
  <a href="work.html">Case studies: colour, tokens, governance and patterns at CARS24</a>
  <a href="work.html#projects">Projects: Riyadh Air, District, a US pharma platform and more</a>
  <a href="lab.html">Lab: tools we built to think with</a>
  <a href="blog.html">Writing: notes on governance and tokens</a>
</div>
'''
write("studio.html", head("Studio — Layer One", "Layer One is a design systems studio in Bangalore, India, founded by Aniket Pandey.")
      + shell("studio", [("Overview", "#overview"), ("Founder", "#founder"), ("What we do", "#services"), ("How we work", "#how"), ("Invitation", "#invitation"), ("Our work", "#our-work")], st_c, card="bar"))

# ======================= Services =======================
engagements = [
    ("audit", "System Audit", "The place to start. For teams that know something's wrong with their system and need to know what to fix first.",
     ["Inventory of every style, token and component in Figma and code", "Scan of the codebase for hard-coded values and forks", "WCAG contrast and accessibility check of key flows",
      "Maturity score across foundations, components, governance and adoption", "Ranked roadmap with effort and impact", "One flow refactored as proof, measured before and after"],
     "$3,500", "fixed", "2 weeks", True),
    ("foundations", "Foundations Build", "For teams starting a system, or rebuilding one that never had real foundations.",
     ["Colour, type, spacing and motion as tokens, built in OKLCH", "Primitive, semantic and component token layers, with one naming grammar",
      "Core components in Figma, mapped one-to-one to code", "Theming for brands, products or markets", "Documentation your teams will read", "Handover workshop"],
     "from $14,000", "", "6–8 weeks", False),
    ("partner", "System Partner", "For organisations that need the system run, scaled and adopted, month after month.",
     ["Governance, intake and prioritisation model", "Ownership tiers and a contribution playbook", "Pattern libraries for the pages teams ship most",
      "Release rhythm with changelogs and migration notes", "Quarterly audits and adoption reporting", "Pairing with your designers and engineers"],
     "from $4,900", "/ month", "Pause or stop any time", False),
    ("workshops", "Workshops", "For teams that want to run their own system well.",
     ["Tokens and naming", "Governance and contribution", "Accessible colour", "Design systems for leadership"],
     "from $1,200", "/ session", "Half day, remote or in person", False),
]
eng_html = ""
for id_, name, for_, items, price, per, dur, feat in engagements:
    lis = "".join(f"<li>{x}</li>" for x in items)
    flag = '<p class="flag">Start here</p>' if feat else ""
    eng_html += f'''<article class="engage{" engage--feature" if feat else ""}" id="{id_}">
      <div>{flag}<h3>{name}</h3><p class="for">{for_}</p><ul>{lis}</ul></div>
      <aside><span class="price">{price} <small>{per}</small></span><span class="dur">{dur}</span><a class="pill" href="contact.html?offer={id_}">Book this</a></aside>
    </article>'''

steps = [("Week 0", "Call", "Thirty minutes on where your system is today. If we're not the right fit, we'll say so."),
         ("Weeks 1–2", "Audit", "Evidence first: files, code, accessibility and how work moves between teams."),
         ("Weeks 3–10", "Build", "In your Figma and your repo, alongside your team, with weekly demos."),
         ("After", "Run", "Governance, docs and training, so the system keeps working without us.")]
steps_html = "".join(f"<li><b>{a}</b><h3>{b}</h3><p>{c}</p></li>" for a, b, c in steps)

faqs = [
    ("Why start with an audit?", "Because the right answer depends on what you already have. Most teams have more working parts than they think, and a few problems causing most of the pain. The audit finds both, and its fee is credited if you go on to a Foundations Build within 60 days."),
    ("Do you only work on design systems?", "Yes. No marketing sites, no app builds. Tokens, components, patterns, documentation and the governance around them."),
    ("Can you work with our existing system?", "Yes. Most engagements improve or scale a system that exists. We keep what works."),
    ("Do you write code?", "We pair with your engineers on token pipelines and component APIs, and can build components in React or as web components when you need extra hands."),
    ("Which tools?", "Figma, Storybook, Tokens Studio, Style Dictionary and whatever your teams already use. The structure we design isn't tied to a tool."),
    ("Where are you based? Which time zones?", "Bangalore, India (IST). We work with teams in India, the Middle East, Europe and the US, with at least two hours of overlap every day."),
    ("What does a founding partner commit to?", "Being named as a client and working with us on a published case study once the work ships. In return you get 20% off and our full attention."),
]
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

sv_c = f'''
<h1 class="statement" id="engagements">Engagements</h1>
<p class="sub muted">Four ways to work with us. Every one is scoped to where your system is today, and every price is in US dollars.</p>
<div class="offer" style="margin-top:24px">{eng_html}</div>

<h2 class="label" id="founding">founding partners</h2>
<div class="invite">
  <div><h3>Three slots in 2027.</h3></div>
  <div>
    <p>20% off any engagement for our first three studio partners, in exchange for a case study we publish together.</p>
    <div class="slots" aria-label="Three slots open"><span></span><span></span><span></span></div>
    <a class="pill" href="contact.html?offer=founding">Apply for a slot</a>
  </div>
</div>

<h2 class="label" id="process">how it runs</h2>
<ol class="steps">{steps_html}</ol>

<h2 class="label" id="faq">questions</h2>
<div class="faq">{fq}</div>
'''
write("services.html", head("Services and pricing — Layer One", "Design system audits, foundations builds, ongoing system partnership and workshops, with pricing.")
      + shell("services", [("Engagements", "#engagements"), ("Founding partners", "#founding"), ("How it runs", "#process"), ("Questions", "#faq")], sv_c, card="bar"))

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

themes = [("CARS24", "#4736fe", "color-blue-500", "color-action-primary"), ("Riyadh Air", "#5b2d90", "color-violet-600", "color-action-primary"),
          ("Loans", "#1f3a8a", "nbfc-color-navy-500", "nbfc-color-action-primary"), ("District", "#7b3fe4", "color-purple-500", "color-action-primary")]
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

# ======================= Contact =======================
ct_c = f'''
<h1 class="statement">Start a project</h1>
<p class="sub muted">Tell us where your system is today. We reply within one working day, from Bangalore (IST).</p>
<form class="contact-form" data-contact>
  <label>Your name<input name="name" autocomplete="name" required></label>
  <label>Company<input name="company" autocomplete="organization" required></label>
  <label>Where is your system today?
    <select name="stage"><option>We don't have one yet</option><option>We have one, but it doesn't scale</option><option>Our design system team is a bottleneck</option><option>Teams aren't using it</option><option>Something else</option></select></label>
  <label>Interested in
    <select name="offer"><option value="System Audit">System Audit</option><option value="Foundations Build">Foundations Build</option><option value="System Partner">System Partner</option><option value="Workshops">Workshops</option><option value="Founding partner slot">Founding partner slot</option><option value="Not sure yet">Not sure yet</option></select></label>
  <label>Anything else<textarea name="message" placeholder="Team size, products, deadlines, links to your system"></textarea></label>
  <button class="pill" type="submit">Open as an email</button>
</form>
<p class="small muted" style="margin-top:12px">This opens a draft in your email app addressed to {EMAIL}. Nothing is sent until you send it.</p>
<h2 class="label">or</h2>
<div class="link-bars">
  <a href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a>
  <a href="mailto:{EMAIL}">Email {EMAIL}</a>
  <a href="{LINKEDIN}" target="_blank" rel="noopener">Message us on LinkedIn</a>
</div>
<script>try{{var o=new URLSearchParams(location.search).get("offer");var m={{audit:"System Audit",foundations:"Foundations Build",partner:"System Partner",workshops:"Workshops",founding:"Founding partner slot"}};if(m[o])document.querySelector("[name=offer]").value=m[o]}}catch(e){{}}</script>
'''
write("contact.html", head("Contact — Layer One", "Start a design system project with Layer One.")
      + shell("contact", [("Start a project", "#main")], ct_c))

# ======================= Short project pages =======================
for p in others:
    more = [q for q in PROJECTS if q["slug"] != p["slug"]][:2]
    scope = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in p["scope"])
    mh = "".join(f'<a class="frame frame--named" href="{q["slug"]}.html"><h3>{q["title"].split(": ", 1)[1][0].upper() + q["title"].split(": ", 1)[1][1:]}</h3><div class="frame-media"><img src="../{q["cover"]}" alt="" loading="lazy"></div></a>' for q in more)
    body = f'''<main id="main" class="page">
  <p class="crumb"><a href="../work.html">Work</a> / {p["client"]}</p>
  <h1>{p["title"]}</h1>
  <figure class="hero-media" style="margin-top:24px"><img src="../{p["cover"]}" alt="{p["client"]} design system overview" width="1800" height="1350"></figure>
  <div class="intro"><p>{p["blurb"]}</p></div>
  <dl class="scope">{scope}</dl>
  <p class="note">A full case study for this project is in progress. <a href="../contact.html">Ask us for a walkthrough</a> and we'll take you through the system on a call.</p>
  <section class="more"><h2>More work</h2><div class="frames frames--2">{mh}</div>
    <div class="rowlinks" style="margin-top:8px"><a href="../work.html">All work</a><a href="../lab.html">Lab<span>Tools we built to think with</span></a><a href="../contact.html">Start a project<span>Get in touch with Layer One</span></a></div></section>
</main>'''
    write(f"work/{p['slug']}.html", head(f"{p['client']} — Layer One", p["blurb"], depth=1, theme="light", og=p["cover"])
          + topbar("work", depth=1) + body + close(depth=1))
