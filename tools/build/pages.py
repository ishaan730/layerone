from common import *

# ---------- Work index ----------
items = ""
for key in ["tokens", "governance", "patterns"]:
    c = CASES[key]
    a, b = c["metrics"][0]
    items += f'''<li><a href="{c["href"]}">
      <img src="{c["img"]}" alt="" loading="lazy" width="1800" height="1238">
      <div><p class="work-meta">{c["meta"]}</p><h2>{c["title"]}</h2><p>{c["summary"]}</p></div>
      <div class="side"><strong>{a}</strong><span>{b}</span></div>
    </a></li>'''

work = (head("Work — Layer One", "Design system case studies from Layer One: colour and tokens, governance, and a pattern library, at CARS24.")
        + header("work") + f'''<main id="main">
<section class="page-head">
  <div class="wrap">
    <h1>Work</h1>
    <p class="lede">Three case studies from one company, CARS24, that follow a design system from its foundations to how it's run to how teams adopt it. Each one starts with the problem and ends with what changed, in numbers.</p>
  </div>
</section>
<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <ul class="work-index">{items}</ul>
    <p class="credit">These projects were led by Layer One's founder as Design Systems Lead at CARS24, working with CARS24's design, engineering, brand and content teams. Images belong to CARS24.</p>
  </div>
</section>
</main>''' + cta("Your system could be the next case study.", "Tell us where it is today. Thirty minutes is enough to tell whether we can help.") + footer())
write("work.html", work)

# ---------- Services ----------
services = [
    ("audit", "Systems", "The parts of the system itself: the decisions every product inherits.",
     [("Design system audit", "Two to three weeks across your Figma libraries, codebase and live product. You get a written report, a debt inventory and a ranked list of what to fix first."),
      ("Token architecture", "Primitive, semantic and component layers with one naming grammar, so a change made once shows up everywhere."),
      ("Core components", "Accessible, tokenised components designed with your engineers, with clear APIs and states."),
      ("Multi-brand theming", "One base system with themes for each brand, product or country that override only what they need."),
      ("Colour and accessibility", "Palettes built in perceptual colour (OKLCH), every step checked against WCAG AA and AAA."),
      ("Documentation", "Guidance people actually read: when to use what, with examples from your own product.")],
     ("tokens", "65% faster handoff at CARS24 after the token rebuild.")),
    ("operations", "Operations", "How the system is run, so it keeps up with the company instead of slowing it down.",
     [("Governance model", "Who decides what, how decisions are recorded, and how the system changes without breaking teams."),
      ("Intake and prioritisation", "One front door for requests and a scoring model any team can apply to its own ask."),
      ("Ownership tiers", "Core, extended and custom: what the design system team owns, what's shared, and what stays with product teams."),
      ("Contribution playbook", "Step-by-step templates so teams can add to the system without lowering its quality."),
      ("Releases and versioning", "A release rhythm with changelogs and migration notes your teams can plan around."),
      ("Quarterly audits", "Regular checks of live screens that feed drift and forks back into the backlog.")],
     ("governance", "A 70-point scorecard that ended the loudest-voice backlog at CARS24.")),
    ("adoption", "Adoption", "How teams come to build with the system, because it's the fastest way to ship.",
     [("Pattern libraries", "Page-level blocks such as banners, grids, rails and lists, each with sizes, content rules and behaviour."),
      ("CMS and page building", "Patterns wired to your CMS so editors change content, never layout."),
      ("Team workshops", "Hands-on sessions for designers and engineers on the system, tokens and contribution."),
      ("Design and engineering pairing", "We sit with your teams on real features until the system becomes the default way of working."),
      ("Adoption metrics", "What to measure beyond usage: time saved, duplicate work avoided, consistency in audits."),
      ("Leadership reporting", "The business case for the system, in numbers your leadership already tracks.")],
     ("patterns", "Pages built about 43% faster with the CARS24 pattern library.")),
]
blocks = ""
for id_, name, intro, its, (case, proof) in services:
    c = CASES[case]
    its_html = "".join(f'<div class="service-item"><h3>{a}</h3><p>{b}</p></div>' for a, b in its)
    blocks += f'''<section class="service-block" id="{id_}" aria-labelledby="h-{id_}">
      <div><h2 id="h-{id_}">{name}</h2><p class="intro">{intro}</p></div>
      <div class="service-items">{its_html}
        <p class="service-proof"><span>{proof}</span><a class="link-arrow" href="{c["href"]}">See the case study {ARROW_SHIFT}</a></p>
      </div>
    </section>'''

who = [("Scaling product companies", "You've gone from one product to several, design has grown faster than its foundations, and every team is solving the same problems separately."),
       ("Multi-brand and multi-market teams", "Several brands, countries or business lines need to feel like one company without being identical."),
       ("Teams with a system nobody uses", "There's a library, but teams build around it. You need governance and adoption, not another component.")]
who_html = "".join(f"<div class='card'><h3>{a}</h3><p>{b}</p></div>" for a, b in who)

svc = (head("Services — Layer One", "Design system audits, token architecture, governance, contribution models and pattern libraries.")
       + header("services") + f'''<main id="main">
<section class="page-head">
  <div class="wrap">
    <h1>Services</h1>
    <p class="lede">We work on three things: the system itself, how it's run, and how teams come to use it. Every engagement starts with an audit, and most end up touching all three.</p>
  </div>
</section>
<div class="wrap">{blocks}</div>
<section class="section" aria-labelledby="who-title">
  <div class="wrap">
    <div class="section-head"><h2 id="who-title">Who we work with</h2><p>Teams that have outgrown how they work today and need a system that grows with them.</p></div>
    <div class="cards cards--3">{who_html}</div>
    <p style="margin-top:40px"><a class="link-arrow" href="index.html#pricing">See pricing {ARROW_SHIFT}</a></p>
  </div>
</section>
</main>''' + cta() + footer())
write("services.html", svc)

# ---------- Writing index ----------
posts = [
    ("blog-librarian-vs-leader.html", "Most design system leads are just librarians", "Leadership", "12 min read", "Why maintaining a library isn't the same as leading a system, and what changes when you design the agreements between teams.", False),
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "Operations", "5 min read", "The real value of a design system in a large organisation isn't speed. It's structure.", True),
    ("https://medium.com/@layerone_11803/most-design-systems-are-just-expensive-ui-libraries-e0cc8b146f2d", "Most design systems are just expensive UI libraries", "Strategy", "8 min read", "Why the most expensive systems often deliver the least, and what's missing from them.", True),
    ("https://medium.com/@layerone/foundations-of-modern-design-systems", "Foundations of modern design systems", "Architecture", "5 min read", "Why most systems fail at the token level, and how to build structure that lasts years.", True),
    ("https://medium.com/@layerone/scaling-ui-engineering", "Scaling UI engineering across organisations", "Engineering", "8 min read", "Keeping UI consistent when the product is spread across many teams and codebases.", True),
]
pl = "".join(f'<li class="post"><a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if ext else ""}><h3>{t}</h3><span>{tag}</span><span>{rt}{" on Medium" if ext else ""}</span><p>{d}</p></a></li>' for h, t, tag, rt, d, ext in posts)
blog = (head("Writing — Layer One", "Notes on design system governance, tokens and leadership from Layer One.")
        + header("writing") + f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>Writing</h1><p class="lede">Notes on governance, tokens and the organisational side of design systems.</p></div></section>
<section class="section--tight" style="padding-top:0"><div class="wrap"><ul class="posts">{pl}</ul></div></section>
</main>''' + cta() + footer())
write("blog.html", blog)
