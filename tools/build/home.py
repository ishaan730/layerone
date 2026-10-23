from common import *

# ---------- Hero ----------
hero = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>We build and scale design systems.</h1>
      <p class="lede">Layer One is a design systems studio. We help product companies create a system from scratch, scale the one they already have across products and markets, and set up the governance that keeps teams using it.</p>
      <div class="btn-row">
        <a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a>
        <a class="btn btn--ghost" href="work.html">See the work</a>
      </div>
      <p class="hero-note">Design systems are all we do. No marketing sites, no app builds.</p>
    </div>

    <figure class="stack" data-stack style="--brand:#4736FE" aria-labelledby="stack-cap">
      <figcaption class="stack-title" id="stack-cap">One button, built from four token layers</figcaption>
      <ol class="stack-layers">
        <li class="layer">
          <span class="layer-name">Component<span class="layer-hint">What people see</span></span>
          <span class="demo-ui"><span class="demo-button">Get best price</span><span class="demo-link">See how it works</span></span>
        </li>
        <li class="layer">
          <span class="layer-name">Semantic<span class="layer-hint">What it's for</span></span>
          <span class="layer-token">color-action-primary</span>
        </li>
        <li class="layer">
          <span class="layer-name">Primitive<span class="layer-hint">Its place in the scale</span></span>
          <span class="layer-token" data-primitive-text>color-blue-500</span>
        </li>
        <li class="layer">
          <span class="layer-name">Value<span class="layer-hint">The raw colour</span></span>
          <span class="layer-token"><span class="swatch-chip"></span><span data-value-text>#4736FE</span></span>
        </li>
      </ol>
      <div class="stack-controls">
        <p>Change the value once. Everything above it follows.</p>
        <div class="value-picker" role="group" aria-label="Brand value">
          <button type="button" aria-pressed="true" aria-label="Electric blue, #4736FE" data-hex="#4736fe" data-primitive="color-blue-500" style="background:#4736fe"></button>
          <button type="button" aria-pressed="false" aria-label="Old CARS24 blue, #0059A3" data-hex="#0059a3" data-primitive="color-blue-700" style="background:#0059a3"></button>
          <button type="button" aria-pressed="false" aria-label="Teal, #0E7C6B" data-hex="#0e7c6b" data-primitive="color-teal-600" style="background:#0e7c6b"></button>
          <button type="button" aria-pressed="false" aria-label="Pink, #C3128A" data-hex="#c3128a" data-primitive="color-pink-600" style="background:#c3128a"></button>
        </div>
      </div>
    </figure>
  </div>
</section>
'''

logos = '''<section class="logos" aria-label="Where our team has built design systems">
  <div class="wrap">
    <p class="logos-label">Our team has built and run design systems at</p>
    <ul>
      <li>CARS24</li><li>IBM</li><li>JPMorgan Chase</li><li>Zomato</li><li>HDFC</li><li>Riyadh Air</li>
    </ul>
  </div>
</section>
'''

# ---------- Situations ----------
situations = [
    ("start", "We don't have a design system yet",
     "Every team keeps its own styles. The same button exists five ways in code, designers copy colours from old screens, and every new product starts from scratch.",
     "We audit what you already have, agree the foundations with design and engineering, and build tokens, core components and documentation that match one-to-one in Figma and code.",
     ["Audit", "Token architecture", "Core components", "Documentation"],
     "tokens", "5 → 1", "button implementations merged into one shared component"),
    ("scale", "Our system doesn't scale past one product",
     "It worked when there was one product. Now there are several products, brands or countries, and each of them overrides the core until nobody trusts it.",
     "We restructure your tokens into layers, set up theming so each brand overrides only what it needs, and give every team a clear place for its own components.",
     ["Multi-brand theming", "Token layers", "Library architecture", "Migration plan"],
     "tokens", "10+", "product lines and 3 countries on one token system"),
    ("govern", "Our design system team is a bottleneck",
     "Requests arrive by DM, Slack and hallway chats. Decisions depend on who asks loudest, and teams build around you while they wait.",
     "We set up one front door for requests, a scoring model any team can apply, clear ownership tiers and a contribution playbook, then run it with you until it holds.",
     ["Intake", "Prioritisation", "Ownership tiers", "Contribution"],
     "governance", "70 pts", "a shared scorecard that replaced the loudest-voice backlog"),
    ("adopt", "Teams aren't really using it",
     "The library exists, but pages are still designed from a blank canvas, and adoption is something you hope for rather than something you measure.",
     "We build patterns for the pages teams actually ship, connect them to your CMS and code, and run the rituals and audits that keep adoption visible.",
     ["Pattern libraries", "CMS integration", "Workshops", "Adoption metrics"],
     "patterns", "~43%", "less time to design and build a new page"),
]
tabs = "".join(
    f'<button class="situation-tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span>{label}</span>{ARROW}</button>'
    for i, (k, label, *_) in enumerate(situations))
panels = ""
for i, (k, label, problem, approach, items, case, num, numlabel) in enumerate(situations):
    c = CASES[case]
    chips = "".join(f"<li>{x}</li>" for x in items)
    panels += f'''<div class="situation-panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>
      <div class="panel-body">
        <div><h3>What's usually going on</h3><p>{problem}</p></div>
        <div><h3>What we do</h3><p>{approach}</p><ul>{chips}</ul></div>
      </div>
      <a class="panel-proof" href="{c["href"]}">
        <img src="{c["img"]}" alt="" loading="lazy" width="1800" height="1238">
        <div><strong>{num}</strong><span>{numlabel}</span><em>Read the {c["short"].lower()} case study</em></div>
      </a>
    </div>
'''
situation_section = f'''<section class="section" id="situations" aria-labelledby="sit-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="sit-title">Where is your system today?</h2>
      <p>Most teams come to us at one of four points. Pick the one closest to yours to see what we'd do about it, and where we've done it before.</p>
    </div>
    <div class="situations">
      <div class="situation-tabs" role="tablist" aria-label="Where your system is today" aria-orientation="vertical">{tabs}</div>
      <div>{panels}</div>
    </div>
  </div>
</section>
'''

# ---------- Work ----------
rows = ""
for key in ["tokens", "governance", "patterns"]:
    c = CASES[key]
    m = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["metrics"])
    s = "".join(f"<li>{x}</li>" for x in c["scope"])
    rows += f'''<article class="work-row">
      <a class="work-media" href="{c["href"]}" tabindex="-1" aria-hidden="true"><img src="{c["img"]}" alt="" loading="lazy" width="1800" height="1238"></a>
      <div>
        <p class="work-meta">{c["meta"]}</p>
        <h3><a href="{c["href"]}">{c["title"]}</a></h3>
        <p class="summary">{c["summary"]}</p>
        <dl class="metrics">{m}</dl>
        <ul class="scope" aria-label="Scope">{s}</ul>
        <a class="link-arrow" href="{c["href"]}">Read the case study {ARROW_SHIFT}</a>
      </div>
    </article>
'''
work = f'''<section class="section" id="work" aria-labelledby="work-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="work-title">Selected work</h2>
      <p>Three projects at one company, CARS24, that together cover the whole life of a design system: getting the foundations right, running it as a service, and getting teams to build with it.</p>
    </div>
    <ol class="lifecycle" aria-label="The three stages">
      <li><strong>Foundations</strong>Colour, tokens and the architecture every product sits on</li>
      <li><strong>Operations</strong>How requests come in, get decided and get built</li>
      <li><strong>Adoption</strong>Patterns that make the system the fastest way to ship</li>
    </ol>
    <div class="work-list">{rows}</div>
    <p class="credit">These projects were led by Layer One's founder as Design Systems Lead at CARS24, working with CARS24's design, engineering, brand and content teams. Images belong to CARS24 and are shown with that context.</p>
  </div>
</section>
'''

# ---------- Services ----------
pillars = [
    ("Systems", "The parts of the system itself.",
     [("Design system audit", "2–3 weeks"), ("Token architecture", ""), ("Core components", ""), ("Multi-brand theming", ""), ("Documentation", ""), ("Figma-to-code parity", "")]),
    ("Operations", "How the system is run, day to day.",
     [("Governance model", ""), ("Intake and prioritisation", ""), ("Ownership tiers", ""), ("Contribution playbook", ""), ("Releases and versioning", ""), ("Quarterly system audits", "")]),
    ("Adoption", "How teams come to build with it.",
     [("Pattern libraries", ""), ("CMS and page building", ""), ("Team workshops", ""), ("Design and engineering pairing", ""), ("Adoption metrics", ""), ("Leadership reporting", "")]),
]
pill = ""
for name, intro, items in pillars:
    lis = "".join(f"<li>{a}<span>{b}</span></li>" if b else f"<li>{a}</li>" for a, b in items)
    pill += f'<div class="pillar"><h3>{name}</h3><p>{intro}</p><ul>{lis}</ul></div>'
services = f'''<section class="section" id="services" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="svc-title">What we do</h2>
      <p>A design system is three things at once: a set of decisions, a way of working, and a habit across teams. We work on all three, and most engagements touch more than one.</p>
    </div>
    <div class="pillars">{pill}</div>
    <p style="margin-top:32px"><a class="link-arrow" href="services.html">Services in detail {ARROW_SHIFT}</a></p>
  </div>
</section>
'''

# ---------- Approach ----------
steps = [
    ("Audit", "Typically 2–3 weeks", "We look at your files, your code and how work actually moves between teams. You get a written report and a ranked list of what to fix first."),
    ("Decide", "Typically 1–2 weeks", "We agree the structure with your design and engineering leads: token layers, naming, what belongs in the core and who owns what."),
    ("Build", "Ongoing, in releases", "We build alongside your team, in your Figma files and your repository, and ship in releases your teams can plan around."),
    ("Hand over", "Last month of the engagement", "Documentation, training and a governance model your team can run without us. Success is how little you need us at the end."),
]
step_html = "".join(f'<li><h3>{a}</h3><p class="duration">{b}</p><p>{c}</p></li>' for a, b, c in steps)

plans = [
    ("Core", "For teams setting up their first structured foundation.", "$3,299", "/ month", False,
     ["Audit of your current styles and components", "Token structure and naming conventions", "Core component library in Figma", "Design-to-development handoff guidelines", "Documentation set-up", "Roadmap from UI kit to system"]),
    ("Growth", "For product teams that need a system with an operating model.", "$4,899", "/ month", True,
     ["Everything in Core", "Full audit and debt clean-up", "Multi-product and multi-brand architecture", "Governance, intake and contribution model", "Pairing with engineers on key components", "Adoption tracking and reporting", "Team workshops"]),
    ("Scale", "For organisations running several systems at once.", "Custom", "", False,
     ["Architecture advisory for a system of systems", "Migration from legacy libraries", "Enterprise adoption strategy", "Custom tooling and plugins", "Role-based governance", "Agreed scope, contract and SLA"]),
]
plan_html = ""
for name, for_, price, per, feat, items in plans:
    lis = "".join(f"<li>{x}</li>" for x in items)
    tag = '<span class="plan-tag">Most teams start here</span>' if feat else ""
    btn = f'<a class="btn{"" if feat else " btn--ghost"}" href="{CAL if name != "Scale" else "mailto:" + EMAIL}"{" target=\"_blank\" rel=\"noopener\"" if name != "Scale" else ""}>{"Book a call" if name != "Scale" else "Email us about Scale"}</a>'
    plan_html += f'''<div class="plan{" plan--featured" if feat else ""}">
      <div class="plan-head"><h3>{name}</h3>{tag}</div><p class="for">{for_}</p>
      <p class="price">{price} <small>{per}</small></p>
      <ul>{lis}</ul>{btn}
    </div>'''

approach = f'''<section class="section" id="approach" aria-labelledby="ap-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="ap-title">How an engagement runs</h2>
      <p>Every engagement starts with an audit, because the right answer depends on where your system is now. After that we build with your team, not for it.</p>
    </div>
    <ol class="process">{step_html}</ol>
    <div id="pricing" class="plans">{plan_html}</div>
    <p class="plans-note">Monthly, with no long-term contract. Pause or cancel at any time. A standalone audit is available on its own; ask us for a quote.</p>
  </div>
</section>
'''

# ---------- Beliefs ----------
beliefs = [
    ("A system is an agreement, not a library.", "Components are the easy part. Ownership, contribution and release cadence are what keep a system alive once it's out in the world."),
    ("Tie it to what the business is trying to do.", "Systems keep their funding when they show time saved and cost avoided. Usage counts alone don't make that case."),
    ("Build where the system will live.", "We work in your files and your codebase, next to your designers and engineers. Nothing is designed in isolation and thrown over a wall."),
    ("Every decision comes with a reason.", "Scored, written down and visible to everyone, so a no is understood and a yes can be planned around."),
    ("Accessible by default.", "Contrast and responsive behaviour are built into the tokens from day one, not patched in after an audit."),
    ("Leave the team able to run it.", "Documentation, training and governance are part of the work. We measure ourselves by how little you need us at the end."),
]
bel = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in beliefs)
beliefs_html = f'''<section class="section" aria-labelledby="bel-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="bel-title">What we believe about systems</h2>
      <p>Learned the slow way, at companies with dozens of designers, hundreds of engineers and more than one country to keep consistent.</p>
    </div>
    <ul class="beliefs">{bel}</ul>
  </div>
</section>
'''

studio = '''<section class="section" id="studio" aria-labelledby="studio-title">
  <div class="wrap studio">
    <h2 id="studio-title">Small and senior, on purpose</h2>
    <div class="studio-body">
      <p>Layer One is a specialist studio. The person you talk to on the first call is the person doing the work.</p>
      <p>We've built and governed design systems for organisations with 70+ designers, 200+ engineers and products in several countries. We stay small, take on a few engagements at a time, and bring in trusted specialists in front-end engineering, accessibility and brand when a project needs them.</p>
      <div class="person">
        <img src="assets/studio/aniket.jpg" alt="" width="52" height="52" loading="lazy">
        <div><strong>Aniket Pandey</strong><span>Founder. Previously Design Systems Lead at CARS24.</span></div>
      </div>
    </div>
  </div>
</section>
'''

posts = [
    ("blog-librarian-vs-leader.html", "Most design system leads are just librarians", "Leadership", "12 min read",
     "Why maintaining a library isn't the same as leading a system, and what changes when you design the agreements between teams.", False),
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "Operations", "5 min read",
     "The real value of a design system in a large organisation isn't speed. It's structure.", True),
    ("https://medium.com/@layerone_11803/most-design-systems-are-just-expensive-ui-libraries-e0cc8b146f2d", "Most design systems are just expensive UI libraries", "Strategy", "8 min read",
     "Why the most expensive systems often deliver the least, and what's missing from them.", True),
]
pl = "".join(
    f'<li class="post"><a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if ext else ""}><h3>{t}</h3><span>{tag}</span><span>{rt}</span><p>{d}</p></a></li>'
    for h, t, tag, rt, d, ext in posts)
writing = f'''<section class="section" id="writing" aria-labelledby="wr-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="wr-title">Writing</h2>
      <p>Notes on governance, tokens and the organisational side of design systems.</p>
    </div>
    <ul class="posts">{pl}</ul>
    <p style="margin-top:32px"><a class="link-arrow" href="blog.html">All writing {ARROW_SHIFT}</a></p>
  </div>
</section>
'''

faqs = [
    ("Do you design products or marketing websites?", "No. We only work on design systems and the shared UI infrastructure around them: tokens, components, patterns, documentation and governance."),
    ("Can you work with the system we already have?", "Yes, and most of our work is exactly that. We start with an audit of what exists and keep everything that's working."),
    ("Do you work with engineers directly?", "Always. A design system that only lives in Figma isn't a system. We pair with your engineers on token pipelines and component APIs, and we can build components in React, Vue or web components when you need extra hands."),
    ("Do you support multiple brands, products or countries?", "Yes. Multi-brand token architecture is one of our specialities. At CARS24 the same token system runs 10+ product lines across India, the UAE and Australia, with each theme overriding only what it needs."),
    ("How long does it take?", "An audit typically takes two to three weeks. Building or restructuring a system usually runs for three to six months, depending on scope and how many teams are involved. We agree the plan before we start."),
    ("Which tools do you work in?", "Figma, Storybook, Tokens Studio and Style Dictionary are common, but the structure we design isn't tied to a tool. We work in whatever your teams already use."),
    ("Why monthly instead of a fixed project fee?", "Design systems are products, not projects. They keep changing as your company does. A monthly engagement lets the scope follow what you actually need, and you can pause or stop at any time."),
]
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
faq = f'''<section class="section" id="faq" aria-labelledby="faq-title">
  <div class="wrap">
    <div class="section-head"><h2 id="faq-title">Questions</h2><p>If yours isn't here, ask it on a call or by email.</p></div>
    <div class="faq">{fq}</div>
  </div>
</section>
'''

html = (head("Layer One — Design systems studio",
             "Layer One is a design systems studio. We help product companies build, scale and govern their design systems.")
        + header(None) + '<main id="main">' + hero + logos + situation_section + work + services + approach
        + beliefs_html + studio + writing + faq + "</main>" + cta() + footer())
write("index.html", html)
