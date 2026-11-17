"""Services: /services (hub) and one page per service, /services/<slug>.

Why these pages exist: buyers search for "design system agency", "design system consultant", "design system audit"
and "AI-ready design system". Pricing explains what each engagement costs; these pages explain what each one is,
who it's for and how it runs, in the words people search with. Prices must match pricing.py.
"""
from common import *
from optimize import ld, crumbs, SITE as _SITE, ORG_ID, AREA

SERVICES = [
    dict(slug="design-system-audit", name="Design system audit", short="Audit",
         title="Design System Audit Service: Know What to Fix First | Layer One",
         desc="A two-week design system audit: every style, token and component in Figma and code, accessibility checks and a ranked roadmap. $1,500 fixed.",
         h1="Design system audit: know exactly what to fix first",
         lede="In two weeks we map every colour, type style, token and component you have in Figma and in code, check accessibility on your key flows, score your system's maturity, and give you a ranked plan with effort and impact. You leave with a baseline leadership understands and a clear first step.",
         price="$1,500", per="fixed", time="2 weeks", who="Teams with a system, or the start of one, that isn't working the way it should",
         signs=[("Five blues, three date pickers", "The same thing exists in several versions and nobody knows which is right."),
                ("Figma and code disagree", "Designs use values that don't exist in code, and the other way round."),
                ("Teams build around the system", "Products detach components or keep their own copies."),
                ("Nobody can say what's there", "No one knows how many components, tokens or patterns you really have."),
                ("Accessibility is unknown", "Contrast, focus and labels have never been checked across products."),
                ("You need a plan to get budget", "Leadership wants to know what's wrong, what it costs and what comes first.")],
         gets=["Inventory of every style, token and component, in Figma and code", "Scan for hard-coded values and forked components",
               "WCAG contrast check of your key flows", "Maturity score across foundations, components, governance and adoption",
               "AI-readiness check: how coding agents behave with your system today", "A ranked roadmap with effort and impact", "60-minute readout with your leads"],
         steps=[("Days 1–2", "Kick-off, access to Figma and repositories, interviews with design and engineering leads."),
                ("Days 3–6", "Inventory and scans: styles, tokens, components, hard-coded values, detached instances."),
                ("Days 7–8", "Accessibility checks on key flows; three real tasks run with a coding agent."),
                ("Days 9–10", "Maturity score, ranked roadmap and the readout with your leads.")],
         proof=["cars24-tokens", "ibm-riyadh-air"],
         reading=["design-system-audit", "design-system-maturity-model", "why-design-systems-fail"],
         faqs=[("What does a design system audit include?", "An inventory of every style, token and component in Figma and code, a scan for hard-coded values and duplicated components, a WCAG contrast check of key flows, a maturity score and a ranked roadmap, presented in a 60-minute readout."),
               ("How long does a design system audit take?", "Two weeks, at a fixed price of $1,500. We need access to your Figma files and repositories and about three hours of your leads' time."),
               ("Do we need a design system already?", "No. If you don't have one, the audit inventories what your products use today, which is the starting point for building one."),
               ("What happens after the audit?", "You can act on the roadmap yourselves, or continue with a Foundations build. The audit fee is credited in full if you start Foundations within 60 days.")],
         og="assets/images/writing/design-system-audit.jpg", plan="audit"),
    dict(slug="design-system-development", name="Design system development", short="Foundations",
         title="Design System Development: Foundations in Six Weeks | Layer One",
         desc="Design system development in six weeks: OKLCH colour, a token architecture, up to 12 components in Figma mapped to code, themes and documentation. $5,900 fixed.",
         h1="Design system development: foundations, tokens and components in six weeks",
         lede="We build the foundations every screen inherits: an accessible colour palette, a token architecture with one naming grammar, type and spacing scales, and up to 12 core components in Figma mapped one-to-one to code, with themes for up to two brands. Then we document it and hand it over to a team that can run it.",
         price="$5,900", per="fixed", time="6 weeks", who="Teams starting a design system, or rebuilding one that never had real foundations",
         signs=[("Starting from scratch", "You've outgrown a UI kit and need a real system before more products ship."),
                ("A rebrand is coming", "New colours and type need to reach every product at once, not screen by screen."),
                ("Dark mode or a second brand", "Your current values can't switch themes without a redesign."),
                ("Components don't match code", "Figma components and coded components drifted apart long ago."),
                ("Contrast fails keep coming back", "Colour choices are made one screen at a time."),
                ("Agents produce off-brand UI", "AI tools can't find or follow your system, so they invent one.")],
         gets=["Everything in the audit, in week one", "Colour palette in OKLCH, contrast-checked at every step",
               "Token architecture: primitive, semantic and component layers, one naming grammar, in DTCG JSON",
               "Type and spacing scales", "Up to 12 core components in Figma, mapped one-to-one to code",
               "Themes for up to 2 brands or products", "Documentation structure your teams will read, written for people and AI agents",
               "Handover workshop and 30 days of support"],
         steps=[("Week 1", "Audit: inventory, accessibility and a ranked plan."),
                ("Weeks 2–3", "Foundations: palette, tokens, type, spacing, themes; Figma variables matched to code."),
                ("Weeks 4–5", "Components: the 12 that matter most, with states, variants, props and Code Connect where available."),
                ("Week 6", "Documentation, AGENTS.md and handover workshop; 30 days of support begin.")],
         proof=["cars24-lego", "ibm-cardinal-health"],
         reading=["how-to-build-a-design-system", "design-tokens", "which-components-to-build-first"],
         faqs=[("How long does it take to build a design system?", "The foundations and first 12 components take six weeks in our Foundations engagement. Larger component sets, more brands or a migration of existing products take longer and are quoted separately."),
               ("Do you build the code as well as Figma?", "We map every component one-to-one to code and pair with your engineers on the token pipeline and component APIs. For larger builds in React or web components we quote a component pack."),
               ("Which tools do you use?", "Your tools: Figma variables and libraries, your repository, Style Dictionary or a similar token build, and Storybook if you have it. Tokens are stored in the vendor-neutral DTCG format."),
               ("How much does design system development cost?", "Foundations is $5,900 fixed for six weeks: 50% to start, 50% on handover. Extra themes are $900 each and extra component packs $1,500 per six components.")],
         og="assets/images/writing/how-to-build-a-design-system.jpg", plan="foundations"),
    dict(slug="design-system-consulting", name="Design system consulting", short="Partner",
         title="Design System Consulting & Monthly Partnership | Layer One",
         desc="Design system consulting on a monthly retainer: governance, contribution, releases, new components and adoption reporting. $2,900 a month, pause any time.",
         h1="Design system consulting: run it, scale it and get it adopted",
         lede="About two days a week of senior design system time, every month. We set up governance and a fair way to take requests, run releases with changelogs and migration notes, build components from your backlog, and report on adoption every quarter, so the system keeps up with your products instead of slowing them down.",
         price="$2,900", per="/ month", time="Monthly", facts=[("$2,900", "a month, billed in advance"), ("~2 days", "a week of senior design system time"), ("Monthly", "pause or stop any time, with notice")], who="Teams that need the system kept up to date and used, month after month",
         signs=[("The system team is a bottleneck", "Requests pile up and teams build their own versions while they wait."),
                ("Decisions take weeks", "Nobody is sure who decides what, so everything goes to a meeting."),
                ("Releases break products", "Changes ship without changelogs, migration notes or a version policy."),
                ("Adoption is unclear", "You can't say who uses the system, or whether it saves time."),
                ("No dedicated team", "The system is someone's side project and keeps slipping."),
                ("Agents are a new user group", "AI-generated UI needs rules, metadata and checks someone has to own.")],
         gets=["About two days a week of senior design systems time", "Governance, intake and a scoring model for requests",
               "Contribution playbook and ownership tiers", "New components and patterns from your backlog",
               "Monthly release with changelog and migration notes", "Quarterly audit and adoption report",
               "Ownership of AI rules: AGENTS.md, component metadata and evals", "Shared Slack channel, replies within one working day"],
         steps=[("Month 1", "Audit, governance model, request intake and a 90-day plan."),
                ("Every week", "Office hours, request triage, components and patterns from the backlog."),
                ("Every month", "A release with changelog and migration notes."),
                ("Every quarter", "Audit and adoption report, and a plan for the next quarter.")],
         proof=["cars24-governance", "ibm-riyadh-air-ops"],
         reading=["design-system-governance", "design-system-operating-model", "design-system-contribution-model"],
         faqs=[("What does a design system consultant do?", "Helps a team build, run and scale its design system: setting up governance and contribution, building components and patterns, running releases, and measuring adoption, with or without an in-house system team."),
               ("How is Partner different from hiring?", "You get senior design system experience about two days a week from day one, without a hiring process, and can pause or stop with notice before the next billing date."),
               ("Can you work with our existing system team?", "Yes. Most Partner engagements support an existing team: we take on governance, tooling or specific components while your team keeps ownership."),
               ("How much does design system consulting cost?", "$2,900 a month, billed in advance, with no minimum beyond the first month. Founding partners in 2027 pay $2,320.")],
         og="assets/images/writing/design-system-governance.jpg", plan="partner"),
    dict(slug="ai-ready-design-system", name="AI-ready design systems", short="AI-ready",
         title="AI-Ready Design System Consulting for AI Agents | Layer One",
         desc="Make your design system usable by AI agents: described tokens, component metadata, AGENTS.md, an MCP server, Figma Code Connect and guardrails. From $1,500.",
         h1="AI-ready design systems: make your system usable by AI agents",
         lede="Coding agents, Figma's MCP server and AI prototyping tools are now some of your design system's busiest users, and they ignore whatever they can't find or understand. We make your system readable by machines (described tokens, component metadata, AGENTS.md, an MCP server, Figma variables and Code Connect) and add the lint rules and evals that prove agents stay on-system.",
         price="$1,500", per="to start", time="Audit, then Foundations or Partner", facts=[("$1,500", "to start: an audit with an AI-readiness focus"), ("2 weeks", "to a baseline, scored evals and a ranked plan"), ("20 parts", "of free, step-by-step writing behind the method")], who="Teams whose engineers and designers already use AI tools, and get off-system UI back",
         signs=[("AI ignores your components", "Agents produce generic buttons and Tailwind blues instead of your system."),
                ("Legacy code gets copied", "Agents follow old components because they're easier to find than new ones."),
                ("Figma-to-code makes divs", "Design-to-code output has hard-coded values and no real components."),
                ("Prototypes look off-brand", "Figma Make, v0 or Lovable fall back to their own defaults."),
                ("Review can't keep up", "AI-assisted pull requests double, and design system comments with them."),
                ("No one owns the rules", "AGENTS.md, metadata and MCP tools appeared without an owner.")],
         gets=["Agent's-eye audit: real tasks run with your teams' agents, scored", "Token descriptions and an agent manifest from DTCG tokens",
               "Component metadata: purpose, usage rules, accessibility, examples", "AGENTS.md section generated and shipped with your package",
               "A read-only MCP server for components, tokens and patterns", "Figma variables and Code Connect for your most-used components",
               "Lint rules with fix-it messages and a monthly eval", "A phased plan for legacy code"],
         steps=[("Weeks 1–2", "Audit with an AI-readiness focus: baseline evals, inventory, ranked plan ($1,500)."),
                ("Weeks 3–6", "As a Foundations build ($5,900): tokens, metadata, AGENTS.md, MCP server, Code Connect."),
                ("Ongoing", "As Partner ($2,900 a month): lint ratchet, codemods, monthly evals and rule ownership."),
                ("Throughout", "Every step measured against the same eval tasks, so you see the improvement.")],
         proof=["jpmc-patterns", "jpmc-system-checks"],
         reading=["ai-ready-design-system", "why-ai-ignores-design-system", "design-system-mcp-server", "legacy-design-system-ai-ready"],
         faqs=[("What is an AI-ready design system?", "A design system AI agents can find, understand and use correctly: one source of truth, machine-readable tokens and component metadata, access through rules files and MCP servers, and checks that catch off-system output. Our free 20-part course explains it in depth."),
               ("How much does it cost to make a design system AI-ready?", "It runs as our standard engagements: an Audit with an AI-readiness focus ($1,500), then a Foundations build ($5,900) or a monthly Partner engagement ($2,900) for implementation."),
               ("Which AI tools does this work with?", "Any agent that reads rules files or connects to MCP servers, including Claude Code, Cursor, GitHub Copilot and Codex, plus Figma's MCP server and AI prototyping tools such as Figma Make, v0 and Lovable."),
               ("Do we need to rebuild our design system?", "No. Most of the work is making what you have readable and consistent: descriptions, metadata, deprecations and checks, in phases while the system stays in use.")],
         og="assets/images/writing/ai-ready-design-system.jpg", plan="audit"),
]
BY = {s["slug"]: s for s in SERVICES}
PROJ = {p["slug"]: p for p in PROJECTS}


def article_title(slug):
    """The article's H1 up to its first colon, for compact link lists (read from the built page)."""
    import re
    path = os.path.join(OUT, "writing", slug + ".html")
    try:
        h1 = re.search(r'<h1 class="ed-title">(.*?)</h1>', open(path).read(), re.S).group(1)
    except Exception:
        return slug.replace("-", " ").capitalize()
    for sep in ("? ", ": "):
        if sep in h1:
            return h1.split(sep)[0] + ("?" if sep == "? " else "")
    return h1


def service_ld(s):
    url = f"{_SITE}/services/{s['slug']}"
    price = s["price"].replace("$", "").replace(",", "")
    offer = {"@type": "Offer", "price": price, "priceCurrency": "USD", "url": f"{_SITE}/pricing#plan-{s['plan']}", "seller": {"@id": ORG_ID}}
    if s["per"] == "/ month":
        offer["priceSpecification"] = {"@type": "UnitPriceSpecification", "price": price, "priceCurrency": "USD", "unitText": "MONTH"}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"], "url": url,
           "description": s["desc"], "provider": {"@id": ORG_ID}, "areaServed": AREA, "offers": offer,
           "image": f"{_SITE}/{s['og']}"}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]}
    return ld(svc) + ld(faq) + ld(crumbs(("Services", "/services"), (s["name"], f"/services/{s['slug']}")))


def build_service(s):
    p = "../"
    facts = (f'<div class="facts3">' + "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in s["facts"]) + '</div>') if s.get("facts") else (f'<div class="facts3"><div><strong>{s["price"]}</strong><span>{s["per"] if s["per"] != "fixed" else "fixed price, in US dollars"}</span></div>'
             f'<div><strong>{s["time"].split(",")[0]}</strong><span>{"how long it takes" if s["per"] == "fixed" else "how it runs"}</span></div>'
             f'<div><strong>{s["short"]}</strong><span>{s["who"]}</span></div></div>')
    signs = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in s["signs"])
    gets = "".join(f"<li>{g}<span>{i + 1:02d}</span></li>" for i, g in enumerate(s["gets"]))
    steps = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in s["steps"])
    proof = "".join(frame(PROJ[x], depth=1) for x in s["proof"] if x in PROJ)
    reading = "".join(f'<a href="{p}writing/{x}.html">{article_title(x)}</a>' for x in s["reading"])
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faqs"])
    others = "".join(f'<a href="{o["slug"]}.html">{o["name"]}: {o["price"]} {"" if o["per"] == "fixed" else o["per"]}</a>' for o in SERVICES if o is not s)
    content = f'''
<p class="crumb small muted"><a href="{p}services.html">Services</a> / {s["name"]}</p>
<h1 class="statement">{s["h1"]}</h1>
<p class="about-p">{s["lede"]}</p>
{facts}
<div class="btn-row" style="margin-top:20px"><a class="pill pill--accent" href="{p}contact.html?offer={s["plan"]}">Start with a call {ARROW}</a><a class="pill" href="{p}pricing.html#plan-{s["plan"]}">See pricing</a></div>

<h2 class="label" id="signs">signs you need this:</h2>
<ul class="incl">{signs}</ul>

<h2 class="label" id="included">what you get:</h2>
<ol class="rows">{gets}</ol>

<h2 class="label" id="how">how it works:</h2>
<ul class="incl incl--steps">{steps}</ul>

<h2 class="label" id="proof">related work:</h2>
<div class="frames frames--2">{proof}</div>
<p class="small muted" style="margin-top:12px;max-width:72ch">This work was led by Aniket Pandey while employed at CARS24, IBM and JPMorgan Chase. Images marked "Illustration" are drawn to describe the work.</p>

<h2 class="label" id="reading">read more:</h2>
<div class="link-bars">{reading}</div>

<h2 class="label" id="faq">questions:</h2>
<div class="faq">{faqs}</div>

<h2 class="label" id="other">other services:</h2>
<div class="link-bars">{others}<a href="{p}services.html">All design system services</a></div>

<div class="pr-final">
  <div><h2>Working with teams worldwide</h2><p>Based in Bangalore, India, with daily overlap for US, European, Gulf and Asia-Pacific teams. Fixed prices in US dollars.</p></div>
  <div class="btn-row"><a class="pill pill--accent pill--lg" href="{p}contact.html?offer={s["plan"]}">Start a project {ARROW}</a><a class="pill pill--lg" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div>
</div>
'''
    sub = [("Overview", "#main"), ("Signs", "#signs"), ("What you get", "#included"), ("How it works", "#how"), ("Related work", "#proof"), ("Questions", "#faq")]
    html = head(s["title"], s["desc"], depth=1, og=s["og"]).replace("</head>", service_ld(s) + "\n</head>", 1)
    write(f"services/{s['slug']}.html", html + shell("services", sub, content, card="bar", depth=1))


def build_hub():
    cards = "".join(f'''<a class="addon svc-card" href="services/{s["slug"]}.html"><h3>{s["name"]}</h3>
      <p class="addon-p"><b>{s["price"]}</b> {s["per"] if s["per"] != "fixed" else "fixed"} · {s["time"]}</p><p>{s["lede"].split(". ")[0]}.</p>
      <span class="go">How it works {ARROW}</span></a>''' for s in SERVICES)
    faqs = [("What does a design system agency do?", "It helps product teams build, scale and run a design system: auditing what exists, creating foundations such as colour, tokens and components, setting up governance and contribution, and getting teams to adopt it. Layer One works only on design systems."),
            ("Where is Layer One based, and do you work with teams abroad?", "We're based in Bangalore, India, and work remotely with product teams worldwide, with daily overlap for US, European, Gulf and Asia-Pacific time zones. Prices are fixed and in US dollars."),
            ("Which service should we start with?", "Most teams start with the two-week audit, which gives a baseline and a ranked plan. Teams that already know they need foundations can start with Foundations, which includes the audit in week one."),
            ("Can you make our design system work with AI tools?", "Yes. We make design systems usable by coding agents, Figma's MCP server and AI prototyping tools: described tokens, component metadata, AGENTS.md, an MCP server, Code Connect and guardrails.")]
    fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    content = f'''
<h1 class="statement">Design system services</h1>
<p class="about-p">Layer One is a design system agency and consultancy. We do one thing: design systems. We audit what you have, build the foundations and components, run and scale the system with your teams, and make it ready for AI agents. Every engagement has a fixed price and a senior team.</p>
<div class="addons svc-grid" style="margin-top:24px">{cards}</div>

<h2 class="label" id="fit">which one fits?</h2>
<ul class="incl">
  <li><b>You're not sure what's wrong</b><span>Start with the <a href="services/design-system-audit.html">audit</a>: two weeks, a baseline and a ranked plan.</span></li>
  <li><b>You need foundations</b><span><a href="services/design-system-development.html">Design system development</a>: palette, tokens and core components in six weeks.</span></li>
  <li><b>You need it run and adopted</b><span><a href="services/design-system-consulting.html">Consulting</a>: governance, releases and adoption, monthly.</span></li>
  <li><b>AI tools ignore your system</b><span><a href="services/ai-ready-design-system.html">AI-ready design systems</a>: metadata, AGENTS.md, MCP and checks.</span></li>
  <li><b>You want to compare everything</b><span>See the side-by-side table and the three-question finder on <a href="pricing.html">pricing</a>.</span></li>
  <li><b>You'd rather talk it through</b><span>A <a href="{CAL}" target="_blank" rel="noopener">30-minute call</a>, no pitch.</span></li>
</ul>

{trust("Built by the team behind the design systems at")}

<h2 class="label" id="faq">questions:</h2>
<div class="faq">{fq}</div>

<div class="pr-final">
  <div><h2>Based in Bangalore, working worldwide</h2><p>Remote engagements with product teams in India, the US, Europe, the Gulf and Asia-Pacific.</p></div>
  <div class="btn-row"><a class="pill pill--accent pill--lg" href="contact.html">Start a project {ARROW}</a><a class="pill pill--lg" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div>
</div>
'''
    items = ld({"@context": "https://schema.org", "@type": "ItemList", "name": "Design system services", "itemListElement": [
        {"@type": "ListItem", "position": i, "url": f"{_SITE}/services/{s['slug']}", "name": s["name"]} for i, s in enumerate(SERVICES, 1)]})
    faq_ld = ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    html = head("Design System Services: Audit, Build, Consulting, AI | Layer One",
                "Design system services from Layer One: a two-week audit, a six-week build, monthly consulting and AI-ready design systems, for product teams worldwide.",
                og="assets/og/layer-one.jpg").replace("</head>", items + faq_ld + "\n</head>", 1)
    sub = [("Services", "#main"), ("Which one fits", "#fit"), ("Questions", "#faq")]
    write("services.html", html + shell("services", sub, content, card="bar"))


if __name__ == "__main__":
    for s in SERVICES:
        build_service(s)
    build_hub()
