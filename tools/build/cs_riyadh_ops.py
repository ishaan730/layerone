from showcase import *

O = "assets/work/ibm-riyadh-air-ops/"

roles = '<div class="sc-roles">' + "".join(
    f'<article><img src="../{O}{img}" alt="" width="120" height="120" loading="lazy"><span class="r">{area}</span><h3>{name}</h3><q>{q}</q></article>'
    for img, area, name, q in [
        ("role-dls-custodian.png", "Design system", "DLS Custodian", "Do we need this, or does it exist?"),
        ("role-dls-design-team.png", "Design system", "DLS Design Team", "What should it be?"),
        ("role-design-director.png", "Design", "Design Director", "Is it good enough?"),
        ("role-dx-director.png", "Business", "Digital Experience Director", "Is it right for Riyadh Air?"),
        ("role-fe-team.png", "Engineering", "Front-end Team", "Can we build it well?"),
        ("role-product-dev-team.png", "Product", "Product Development Teams", "What do our users need?")]) + "</div>"


def _model(nodes, edges, hub=None):
    """A tiny node diagram. nodes = [(x, y)], edges = [(i, j)]"""
    e = "".join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="currentColor" stroke-opacity=".45" stroke-width="1.5"/>' for a, b in edges)
    n = "".join(f'<circle cx="{x}" cy="{y}" r="{11 if i == hub else 7}" fill="{"currentColor" if i == hub else "none"}" stroke="currentColor" stroke-width="1.5"/>' for i, (x, y) in enumerate(nodes))
    return f'<svg viewBox="0 0 160 100" aria-hidden="true">{e}{n}</svg>'


ring = [(80, 20), (128, 42), (118, 84), (42, 84), (32, 42)]
models = f'''<div class="sc-models">
  <figure>{_model([(80, 50)], [], hub=0)}<b>Solitary</b><p>One team builds for itself. Fine until the second product.</p></figure>
  <figure>{_model([(80, 50)] + ring, [(0, i) for i in range(1, 6)], hub=0)}<b>Centralised</b><p>One team builds for all. Consistent, and everyone queues.</p></figure>
  <figure>{_model(ring, [(i, j) for i in range(5) for j in range(i + 1, 5)])}<b>Federated</b><p>Everyone contributes. Fast, until nobody can say no.</p></figure>
  <figure class="is-ours">{_model([(80, 50)] + ring, [(0, i) for i in range(1, 6)] + [(1, 2), (3, 4), (2, 3)], hub=0)}<b>Hybrid: ours</b><p>A central team curates. Squads contribute through one front door.</p></figure>
</div>'''

gates = '<div class="sc-gates">' + "".join(
    f'<div><span class="g">Gate {i + 1}</span><h3>{t}</h3><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for i, (t, items) in enumerate([
        ("Definition of ready", ["A use case", "Where it's used", "A Figma playground link"]),
        ("Proposal criteria", ["Used in more than one place", "No existing component solves it", "New, or a variant?"]),
        ("Dev handoff", ["Every state", "EN and AR, light and dark", "Tokens only, annotated"]),
        ("Component handoff", ["QA passed", "Figma matches Storybook", "Documented, ready to announce"])])) + "</div>"

ticket = '''<div class="sc-ticket"><header><code>DS-214</code><span>In review</span></header><h3>Seat selector: add a “blocked” state</h3>
  <dl><div><dt>New or existing?</dt><dd>Existing · G06/B05</dd></div><div><dt>Where will it be used?</dt><dd>Booking, check-in, manage trip</dd></div>
  <div><dt>Use case</dt><dd>Seats held for crew or exit rows</dd></div><div><dt>Why do we need it?</dt><dd>Today squads grey it out by hand</dd></div>
  <div><dt>Playground</dt><dd>Figma file linked</dd></div></dl><p class="small" style="color:#6c6789">An illustrative ticket, following the five questions every submission answered.</p></div>'''

playbook_cases = ["New component", "Change an existing one", "Contribution from a squad", "Changelog from Figma", "Design to dev handoff",
                  "Audit a component", "Documentation", "Library publish", "File distribution", "Approval checklist"]
door = ('<ol class="sc-cases">' + "".join(f"<li><b>{i + 1:02d}</b><span>{t}</span></li>" for i, t in enumerate(playbook_cases)) + "</ol>"
        + '<div style="height:20px"></div>'
        + brief([("door", "Requests arrived in chats, reviews and corridors", "One ticket in Azure DevOps, triaged by the DLS Custodian"),
                 ("copy", "Three squads built three date pickers", "“Does it exist?” first. Many requests ended with a link, the same day")]))

R1 = [("Contribution", "Proposals welcome", 1, 11, "var(--f)", "var(--ft)"), ("Definition", "Prioritise", 1, 3, "#6a67e1", "#fff"),
      ("Design reviews", "Critique", 4, 7, "#6a67e1", "#fff"), ("Eng handoffs", "Walk-through", 5, 8, "#6a67e1", "#fff"),
      ("Eng QA", "Build reviewed together", 6, 10, "#9c9fff", "#0b0d12"), ("Approvals", "Done?", 9, 10, "#fbd8d6", "#0b0d12"),
      ("Demo, release", "Announce", 10, 11, "#fbd8d6", "#0b0d12")]
sprint = ('<div class="sc-sprint" data-inview><div class="sc-sprint-h"><span>Two-week sprint</span>' + "".join(f"<span>D{d}</span>" for d in range(1, 11)) + "</div>"
          + "".join(f'<div class="sc-sprint-r"><span>{n}</span><i style="--a:{a + 1};--b:{b + 1};--c:{c};--ct:{ct};--d:{k}">{t}</i></div>' for k, (n, t, a, b, c, ct) in enumerate(R1))
          + '</div><p class="sc-note">An illustrative sprint. The routines are the ones the teams ran; their exact days moved with each calendar.</p>')

S = [
    section("brief", "Brief", "<b>01</b> the brief:", "Everyone could change it. Nobody owned it.",
            "IBM, Riyadh Air's design team and Publicis Sapient shared one library, with requirements changing weekly.",
            wrap(nums([("", "3", "", "companies on one design system", "Who"), ("", "6", "", "named roles, each with one decision", "Roles"),
                       ("", "4", "", "quality gates from request to release", "Gates"), ("", "10", "", "playbook cases, so nobody guessed", "Playbook")])
                 + '<div style="height:16px"></div>'
                 + brief([("copy", "Snowflakes: three squads, three date pickers", "One front door that checks the library first"),
                          ("drift", "Figma said one thing, Storybook another", "Four gates, the last one: Figma matches code"),
                          ("owner", "Disagreements settled by whoever spoke last", "One named owner for every decision")]))),
    section("roles", "Roles", "<b>02</b> roles:", "Six roles, six clear calls", "Not job titles: the one question each role answers. Once the names were on a page, half the arguments stopped.",
            wrap(roles), mode="stage"),
    section("model", "Operating model", "<b>03</b> operating model:", "Central owners, federated contributors", "The middle path most mature systems end up on.",
            wrap(models)),
    section("door", "Front door", "<b>04</b> one front door:", "Ten kinds of work, one way in", "The cheapest component is the one you don't have to build.",
            wrap(door)),
    section("flow", "The flow", "<b>05</b> request to release:", "A gate with an owner at every handoff", "Fail a gate and the work goes back one step, not back to the start.",
            wrap(rail([("Propose", "Is it needed, and where?"), ("Design", "Every state, EN and AR"), ("Code", "Built and in Storybook"), ("Doc", "Usage, do and don't"), ("Release", "Published and announced")])
                 + '<div style="height:24px"></div>' + gates + '<div style="height:16px"></div>'
                 + bigfig(O + "flow-component.jpg", "The working lifecycle diagram, shared with all three companies.", bg="#fff", pad="16px")), mode="paper"),
    section("reviews", "Squad reviews", "<b>06</b> squad reviews:", "Four pairs of eyes before a developer", "Peer, design lead, Riyadh Air, then a walk-through with engineering. Every “no” came back with comments.",
            wrap(bigfig(O + "flow-design.jpg", "The squad design flow from a user story to done. Green is yes, red sends the work back.", bg="#fff", pad="16px"))),
    section("contribute", "Contribution", "<b>07</b> contribution:", "Anyone could challenge the library", "A designer, a developer, even a copywriter. The person who hit the problem started the change.",
            wrap('<div class="sc-split">' + ticket + "<div>" + rail([("Identify", "Copy the Figma playground file"), ("Submit", "A ticket with five answers"),
                                                                 ("Review", "An open forum; the checklist decides"), ("Define", "Variants, states and props, with a developer")]).replace("sc-rail", "sc-rail sc-rail--v")
                 + "</div></div>"), mode="stage"),
    section("rituals", "Rituals", "<b>08</b> rituals:", "A heartbeat every sprint", "People knew when to bring a proposal, when it would be decided, and when they'd see it ship.",
            wrap(sprint)),
    section("impact", "Impact", "<b>09</b> what changed:", "Fast and consistent, at the same time", "",
            wrap(outcomes([("Clarity", "One owner", "Every decision had a named person to settle it."), ("Speed", "No queue", "Squads contributed through one front door."),
                           ("Quality", "Figma = code", "Checked at four gates before release."), ("Adoption", "3 companies", "One rhythm, held from zero to launch.")])
                 + '<div style="height:16px"></div>' + lessons(["Write down who decides before you write down how.", "Put criteria on every gate. A review without a checklist is an opinion.",
                                                               "Let anyone contribute, but curate centrally."]))),
    section("playbook", "For your team", "<b>10</b> for your team:", "The same operating model, set up for you", "Each part of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "Map who decides what today, where requests come from, and where design and code drift.",
                           "foundations": "Set up the front door, the gates and the roles alongside your core system.",
                           "partner": "Run the rituals with your teams until they run themselves."}))),
]

page("ibm-riyadh-air-ops", dict(
    h1="Three companies, one design system: who decides what ships?",
    lede="The operating model behind the Riyadh Air system: roles, one front door, four gates and a sprint rhythm.",
    tags=["Governance", "Contribution", "Rituals", "Design operations"],
    proof=[("", "3", "", "companies, one system"), ("", "6", "", "named roles"), ("", "4", "", "quality gates"), ("", "10", "", "playbook cases")],
    cover_alt="Riyadh Air design operations: the five-step flow with its gates and the six roles, on lavender",
    sections=S,
    credits="Aniket Pandey worked on this as a design system designer at IBM (2023–24), with IBM design and engineering, Riyadh Air's design team and business owners, and Publicis Sapient. This is IBM client work done as an employee, not Layer One client work. Diagrams belong to Riyadh Air and IBM and are shown for portfolio purposes.",
))
