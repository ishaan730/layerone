from common import *

CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DASH = '<span class="no" aria-label="Not included">–</span>'

plans = [
    dict(id="audit", name="Audit", line="Know exactly what to fix first.", price=1500, per="fixed", time="2 weeks",
         for_="For teams with a system, or the start of one, that isn't working the way it should.",
         items=["Inventory of every style, token and component, in Figma and code", "Scan for hard-coded values and forked components",
                "WCAG contrast check of your key flows", "Maturity score across foundations, components, governance and adoption",
                "A ranked roadmap with effort and impact", "60-minute readout with your leads"],
         cta="Book the audit", note="Credited in full against Foundations if you continue within 60 days."),
    dict(id="foundations", name="Foundations", line="A system your teams can build on.", price=5900, per="fixed", time="6 weeks", featured=True,
         for_="For teams starting a design system, or rebuilding one that never had real foundations.",
         items=["Everything in the Audit, in week one", "Colour palette in OKLCH, contrast-checked at every step", "Token architecture: primitive, semantic and component layers, one naming grammar",
                "Up to 12 core components in Figma, mapped one-to-one to code", "Themes for up to 2 brands or products", "Documentation structure your teams will read",
                "Handover workshop and 30 days of support"],
         cta="Start Foundations", note="50% to start, 50% on handover."),
    dict(id="partner", name="Partner", line="Run it, scale it, get it adopted.", price=2900, per="/ month", time="Pause or stop any time",
         for_="For teams that need the system kept up to date and used, month after month.",
         items=["About two days a week of senior design systems time", "Governance, intake and a scoring model for requests", "Contribution playbook and ownership tiers",
                "New components and patterns from your backlog", "Monthly release with changelog and migration notes", "Quarterly audit and adoption report",
                "Shared Slack channel, replies within one working day"],
         cta="Talk about Partner", note="Billed monthly in advance. Minimum one month."),
]


def money(n):
    return f"${n:,.0f}"


cards = ""
for p in plans:
    lis = "".join(f"<li>{CHECK}<span>{x}</span></li>" for x in p["items"])
    feat = p.get("featured")
    disc = round(p["price"] * 0.8)
    cards += f'''<article class="plan{" plan--feat" if feat else ""}" id="plan-{p["id"]}" data-plan="{p["id"]}">
      {'<p class="plan-flag">Most teams start here</p>' if feat else ""}
      <header><h2>{p["name"]}</h2><p class="plan-line">{p["line"]}</p></header>
      <p class="plan-price"><span class="amt" data-full="{money(p["price"])}" data-disc="{money(disc)}">{money(p["price"])}</span><span class="per">{p["per"]}</span></p>
      <p class="plan-was" data-was hidden><s>{money(p["price"])}</s> founding-partner price</p>
      <p class="plan-time">{p["time"]}</p>
      <a class="pill plan-cta{" pill--accent" if feat else ""}" href="contact.html?offer={p["id"]}">{p["cta"]}</a>
      <p class="plan-for">{p["for_"]}</p>
      <ul class="plan-list">{lis}</ul>
      <p class="plan-note">{p["note"]}</p>
    </article>'''

includes = [("A senior team", "The person on the first call does the work. No hand-off to juniors."),
            ("Your files, your repo", "We work in your Figma and your codebase, not a separate deck."),
            ("Weekly demos", "Progress you can see every week, with written decisions."),
            ("Fixed price, fixed scope", "No hourly billing. If scope changes, we agree it first."),
            ("Your time zone", "Based in IST, with daily overlap for India, Gulf, European and US teams."),
            ("You own everything", "Every file, token and component is yours from day one.")]
inc = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in includes)

rows = [
    ("Discovery", None),
    ("Inventory of Figma and code", ("y", "y", "Quarterly")),
    ("Accessibility check of key flows", ("y", "y", "Quarterly")),
    ("Ranked roadmap", ("y", "y", "Updated monthly")),
    ("Foundations", None),
    ("Colour palette in OKLCH", ("–", "y", "Changes as needed")),
    ("Token architecture and naming", ("Recommendations", "y", "Extended")),
    ("Themes for brands or products", ("–", "Up to 2", "Added as needed")),
    ("Components and patterns", None),
    ("Core components in Figma, mapped to code", ("–", "Up to 12", "From your backlog")),
    ("Pattern libraries for pages", ("–", "–", "y")),
    ("Running the system", None),
    ("Governance, intake and scoring", ("–", "Starter guide", "y")),
    ("Contribution playbook", ("–", "–", "y")),
    ("Releases and changelogs", ("–", "First release", "Monthly")),
    ("Adoption reporting", ("–", "–", "Quarterly")),
    ("Support", None),
    ("Documentation", ("Audit report", "Structure and core pages", "Kept up to date")),
    ("Workshops", ("Readout", "Handover workshop", "Included as needed")),
    ("Support after delivery", ("–", "30 days", "Ongoing")),
]
tb = ""
for name, vals in rows:
    if vals is None:
        tb += f'<tr class="grp"><th colspan="4" scope="colgroup">{name}</th></tr>'
        continue
    cells = "".join(f"<td>{CHECK if v == 'y' else (DASH if v == '–' else v)}</td>" for v in vals)
    tb += f'<tr><th scope="row">{name}</th>{cells}</tr>'
table = f'''<div class="cmp-wrap"><table class="cmp">
  <thead><tr><th scope="col"><span class="visually-hidden">Feature</span></th>{"".join(f'<th scope="col">{p["name"]}<span data-th-price="{p["id"]}">{money(p["price"])}{"" if p["per"] == "fixed" else " /mo"}</span></th>' for p in plans)}</tr></thead>
  <tbody>{tb}</tbody></table></div>'''

finder = '''<form class="finder" data-finder onsubmit="return false" aria-labelledby="finder-h">
  <div class="fq"><p class="fq-q">1. Do you have a design system today?</p><div class="opts opts--chip">
    <label class="opt opt--chip"><input type="radio" name="f1" value="none"><span><b>No, not really</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f1" value="messy"><span><b>Yes, but it's inconsistent</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f1" value="works"><span><b>Yes, and it mostly works</b></span></label></div></div>
  <div class="fq"><p class="fq-q">2. What's the biggest problem?</p><div class="opts opts--chip">
    <label class="opt opt--chip"><input type="radio" name="f2" value="unknown"><span><b>We don't know where to start</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f2" value="foundations"><span><b>Colours, tokens and components</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f2" value="ops"><span><b>Too many requests, slow decisions</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f2" value="adoption"><span><b>Teams don't use it</b></span></label></div></div>
  <div class="fq"><p class="fq-q">3. How long do you need help?</p><div class="opts opts--chip">
    <label class="opt opt--chip"><input type="radio" name="f3" value="once"><span><b>A defined project</b></span></label>
    <label class="opt opt--chip"><input type="radio" name="f3" value="ongoing"><span><b>Ongoing</b></span></label></div></div>
  <div class="f-result" aria-live="polite" data-f-result><p class="muted">Answer the three questions to see a recommendation.</p></div>
</form>'''

addons = [("Workshop", "$450", "per half-day session", "Tokens and naming, governance, accessible colour, or design systems for leadership. Remote or in Bangalore."),
          ("Extra theme", "$900", "per brand or product", "Add a brand, product line or market to a Foundations build."),
          ("Component pack", "$1,500", "per 6 components", "More components on top of the 12 in Foundations, designed and mapped to code.")]
ad = "".join(f'<div class="addon"><h3>{a}</h3><p class="addon-p"><b>{b}</b> {c}</p><p>{d}</p></div>' for a, b, c, d in addons)

faqs = [
    ("Why fixed prices instead of hourly?", "Because you should know the cost before you start. We agree scope, timeline and price up front. If something new comes up, we price it separately and you decide."),
    ("What does the founding-partner discount need from us?", "Permission to name you as a client and to publish a case study together once the work ships. Three slots are open for engagements starting in 2027."),
    ("Is the Audit worth doing if we already know we need Foundations?", "Foundations includes the audit in week one, so you don't need both. If you do the Audit first, its full fee is credited against Foundations within 60 days."),
    ("How do payments work?", "Audit: in full at the start. Foundations: 50% to start, 50% on handover. Partner: monthly in advance, with no minimum beyond the first month. We invoice in US dollars."),
    ("Can we pause Partner?", "Yes. Give us notice before the next billing date and we'll pause or stop. Everything we've made is already yours."),
    ("Do you build the code too?", "We pair with your engineers on token pipelines and component APIs, and map every component to code. For larger builds in React or web components, we'll quote a component pack."),
    ("Our system is very large. Do these prices still apply?", "These prices cover most product teams. For several systems, many brands or a large migration, we'll send a fixed quote after the call."),
]
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

content = f'''
<header class="pr-head">
  <h1 class="statement">Fixed prices for design systems work.</h1>
  <p class="sub muted">Start with an audit, build the foundations, then keep the system running. Every engagement has a fixed price, a fixed timeline and a senior team. Prices in US dollars.</p>
  <div class="pr-toggle" role="group" aria-label="Pricing">
    <button type="button" aria-pressed="true" data-price="full">Standard</button>
    <button type="button" aria-pressed="false" data-price="disc">Founding partner <span>−20%</span></button>
  </div>
  <p class="pr-fp" data-fp-note hidden>Founding-partner prices apply to three teams starting in 2027, in exchange for a case study we publish together.</p>
</header>

<div class="plans" data-plans>{cards}</div>

<section aria-labelledby="inc-h"><h2 class="label" id="inc-h">every engagement includes:</h2><ul class="incl">{inc}</ul></section>

<section aria-labelledby="cmp-h"><h2 class="label" id="cmp-h">compare in detail:</h2>{table}</section>

<section aria-labelledby="finder-h"><h2 class="label" id="finder-h">not sure where to start?</h2>{finder}</section>

<section aria-labelledby="founding"><h2 class="label" id="founding">founding partners:</h2>
<div class="invite">
  <div><h3>Three slots in 2027.</h3></div>
  <div><p>Our first three studio clients get 20% off any engagement: Audit $1,200, Foundations $4,720, Partner $2,320 a month. In return, we publish the case study together.</p>
    <div class="slots" aria-label="Three slots open"><span></span><span></span><span></span></div>
    <a class="pill" href="contact.html?offer=founding">Apply for a slot</a></div>
</div></section>

<section aria-labelledby="add-h"><h2 class="label" id="add-h">add-ons:</h2><div class="addons">{ad}</div></section>

<section class="assure" aria-label="Our promises">
  <div class="trust"><p>Built by the team behind the design systems at</p><ul>{"".join("<li>" + logo_tile(k) + "</li>" for k in ("cars24", "ibm", "jpmc"))}</ul></div>
  <ul class="promises">
    <li><b>Audit credited in full</b><span>if you go on to Foundations within 60 days.</span></li>
    <li><b>Fixed price, fixed scope</b><span>agreed before we start. No surprise invoices.</span></li>
    <li><b>Pause Partner any time</b><span>with notice before the next billing date.</span></li>
  </ul>
</section>

<section aria-labelledby="pfaq-h"><h2 class="label" id="pfaq-h">pricing questions:</h2><div class="faq">{fq}</div></section>

<div class="pr-final">
  <div><h2>Not sure which one fits?</h2><p>Tell us where your system is today. We'll recommend one, or tell you honestly if you don't need us yet.</p></div>
  <div class="btn-row"><a class="pill pill--accent pill--lg" href="contact.html">Start a project {ARROW}</a><a class="pill pill--lg" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div>
</div>
'''
write("pricing.html", head("Pricing — Layer One", "Fixed-price design system engagements: a two-week audit, a six-week foundations build and a monthly system partnership.")
      + shell("pricing", [("Plans", "#main"), ("Includes", "#inc-h"), ("Compare", "#cmp-h"), ("Find your plan", "#finder-h"), ("Founding partners", "#founding"), ("Add-ons", "#add-h"), ("Questions", "#pfaq-h")], content, card="bar"))
