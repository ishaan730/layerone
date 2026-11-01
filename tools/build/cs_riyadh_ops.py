from cs import *

O = "assets/work/ibm-riyadh-air-ops/"

roles = '<div class="m-tiles m-tiles--3">' + "".join(
    f'<div><p class="small muted">{area} · {name}</p><h3>“{q}”</h3><p>{d}</p></div>' for area, name, q, d in [
        ("Design system", "DLS Custodian", "Do we need this, or does it exist?", "Owns the front door: triage, the backlog and the announcement when something ships."),
        ("Design system", "DLS Design Team", "What should it be?", "Designs and updates components, with every state, both languages and both themes."),
        ("Design", "Design Director", "Is it good enough?", "Holds the quality bar in design reviews and in the final review before release."),
        ("Business", "Digital Experience Director", "Is it right for Riyadh Air?", "The business owner's approval. Nothing goes to development without it."),
        ("Engineering", "Front-end Team", "Can we build it well?", "Joins technical review early, builds the component and publishes it to Storybook."),
        ("Product", "Product Development Teams", "What do our users need?", "The squads. They raise requests, contribute components and use what ships.")]) + "</div>"

models = shift([("Solitary: one team builds for itself. Fine until the second product arrives.", "Hybrid: a small central team owns and curates the system."),
                ("Centralised: one team builds for all. Consistent, and everyone waits in one queue.", "Every squad has a designer, an engineer and a product owner who feed it."),
                ("Federated: everyone contributes. Fast, until nobody can say no.", "Squads propose and contribute through one front door.")],
               "Before: the three classic models. After: the middle path most mature systems end up on.")

flow = [("Propose", "DLS Custodian, with the squad", "Gate 1 · Definition of ready", "Is it needed, and where? A use case, where it's used, and a Figma playground link. Many requests end here, pointed to an existing component, often the same day.", "A ticket in the backlog, or a link to what exists"),
        ("Design", "DLS Design Team", "Gate 2 · Proposal criteria", "Used in more than one place? Can't be solved by an existing component? New, or a variant? Then every state, English and Arabic, light and dark.", "A design reviewed by the Design Director"),
        ("Code", "Front-end Team", "Gate 3 · Dev handoff criteria", "Every state, both languages, both themes, tokens only, annotated. The Digital Experience Director signs off before development starts.", "A component built in Storybook"),
        ("Doc", "DLS Design Team and engineering", "Gate 4 · Component handoff", "QA passed, Figma and Storybook match, usage and do's and don'ts written.", "A documented, matching component"),
        ("Release", "DLS Custodian", "Every release", "Published to the library and Storybook, and announced to every stakeholder by mail.", "Changes announced, not discovered")]

intake = '<ol class="m-tiles m-tiles--3" style="list-style:none;padding:0">' + "".join(
    f'<li><div><h3><span class="muted">{i + 1:02d}</span> {t}</h3></div></li>' for i, t in enumerate(
        ["New component", "Change an existing one", "Contribution from a squad", "Changelog from Figma", "Design to dev handoff",
         "Audit an existing component", "Documentation", "Library publish", "File distribution", "Approval checklist"])) + "</ol>"

contribute = [("Identify", "Anyone who hits the problem", "Any day", "Copy the Figma playground file: a checklist, a space for the use case and a space for research.", "A playground file"),
              ("Submit", "The person who raised it", "Any day", "Raise a ticket or post in the design system channel, answering five questions: new or existing, where it's used, the use case, why it's needed, and a playground link.", "A ticket like DS-214: “Seat selector: add a blocked state”"),
              ("Proposal review", "Open forum, any discipline", "Each sprint", "Anyone can join. The checklist decides: will it be used more than once, is it a new problem, and is it a new component or a variant?", "Accept, or point to what exists"),
              ("Define requirements", "Design Owner and at least one developer", "Before the sprint", "A consolidation review to agree variants, states and props.", "A backlog ticket, ready to plan")]

rituals = tiles([("Definition and prioritisation", "Start of sprint. Agree states, behaviour and priority before anyone opens Figma."),
                 ("Component design reviews", "Mid-sprint critique from designers and stakeholders."),
                 ("Engineering handoffs", "Walk through the details, answer questions, agree requirements."),
                 ("Engineering QA", "Asynchronous. Designers and engineers review the build together."),
                 ("Design approvals", "End of sprint. Does it meet the definition of done?"),
                 ("Demos and release", "Package the release, demo it, and update every stakeholder.")], cols=3)

spec = dict(
    h1="Three companies, one design system: who decides what ships?",
    lede="A design system is easy to start and hard to run. At Riyadh Air, IBM, Riyadh Air's own design team and Publicis Sapient were building one airline's apps at the same time, with product owners and analysts changing requirements every week. This is the operating model behind the system: who owns what, how a request gets in, how it gets checked, and the routines that kept dozens of people moving in one direction.",
    meta=[("Role", "Design system designer, IBM"), ("Client", "Riyadh Air"), ("Partners", "Riyadh Air design, Publicis Sapient"), ("Focus", "Governance, contribution, rituals")],
    cover=(O + "cover.jpg", "Riyadh Air design operations: the squad design flow, the six roles and the five-step delivery process"),
    tldr=[("The problem", "Three companies and many squads could all change one library, and nobody owned it: duplicate components, Figma drifting from code, and decisions made by whoever spoke last."),
          ("What we did", "An operating model, not a rulebook: named roles, one front door, a contribution model, four quality gates and a rhythm of rituals."),
          ("What changed", "Squads contributed instead of waiting, and what was approved in Figma was what shipped in code.")],
    kpis=[("3", "", "", "companies designing and building on one system"), ("6", "", "", "named roles, each with one decision to make"),
          ("4", "", "", "quality gates between a request and a release"), ("10", "", "", "playbook cases, so nobody had to guess")],
    chapters=[
        ("context", "Context", "Picture the room",
         "Riyadh Air was building an airline from zero, so everything was new at once: the brand, the apps, the teams. Three companies shared one design system, and none of them had worked together before.",
         tiles([("Riyadh Air", "The airline's own design team, the Digital Experience Director and the business owners who signed off."),
                ("IBM", "Product squads, the design system team, and the front-end engineers who built it in code."),
                ("Publicis Sapient", "Designers building their own product areas on the same library, and contributing back to it.")], cols=3)
         + '<p class="small muted">Product owners and business analysts on every squad brought new requirements, redesigns and quick iterations every week.</p>'),
        ("problem", "Problem", "The same six problems every growing system hits",
         "None of these were unique. What made Riyadh Air different was that all six showed up in the first few months, because the system and the product were being born together.",
         tiles([("Snowflakes", "Three squads built three date pickers, because nobody knew the other two existed."),
                ("Drift", "Figma said one thing and Storybook another, and QA couldn't tell which was right."),
                ("Bottleneck", "Every change waited on the central team, so squads detached components to keep moving."),
                ("No owner", "When two companies disagreed about a component, there was no one whose call it was."),
                ("Moving target", "A component approved on Monday could be redesigned by Friday."),
                ("Silent changes", "Library updates landed without notice and broke screens already signed off.")], cols=3)
         + more("The design question: how might three companies move fast on one design system, without it falling apart every time the product changes?",
                "The belief behind the answer: a solid design system begins with people and sound processes. Treat it as a product, give every decision an owner, and make everyone a contributor.")),
        ("roles", "Roles", "Six roles, six clear calls",
         "The first step was writing down who decides what. Not job titles, but the one question each role answers. Once the names were on a page, half the arguments stopped.",
         roles),
        ("model", "Operating model", "Central owners, federated contributors",
         "There are three classic ways to run a system. We took the middle path: a small central team owns the system, and every squad has a designer, an engineer and a product owner who feed it, each with a counterpart in the system team.",
         models),
        ("intake", "Front door", "Ten kinds of work, one way in",
         "Requests used to arrive in chats, in reviews and in corridors. The system got one front door, a ticket in Azure DevOps, and a playbook for the ten kinds of work that came through it.",
         intake
         + lead("The first question at the door: is a component required? The DLS Custodian checks the library first. Many requests ended at “no”, with a link to Figma and Storybook. The cheapest component is the one you don't have to build.")),
        ("flow", "The flow", "From request to release, with a gate at every handoff",
         "Every component went through the same five steps, with a gate between them that had a named owner and a written list of criteria. Fail a gate and the work goes back one step, not back to the start. Step through it.",
         stepper("Component lifecycle", flow)
         + fig(O + "flow-component.jpg", "The working lifecycle diagram shared with all three companies: who is in each step, and which tool it happens in.")),
        ("squads", "Squad reviews", "Four reviews before a screen reaches a developer",
         "The same thinking applied to product screens. Each screen passed four reviews, each by a different pair of eyes: a peer, the design lead, Riyadh Air's design team, then a walkthrough with engineers. Every “no” went back with comments, so feedback was a loop, not a wall.",
         fig(O + "flow-design.jpg", "The squad design flow from a user story to done. Green is yes, red sends the work back, and the icons show where each step happens.")),
        ("contribute", "Contribution", "Anyone can be the one to make things change",
         "The library was the status quo, and anyone was allowed to challenge it: a designer, a developer, even a copywriter. The person who hit the problem started the contribution.",
         stepper("Contribution model", contribute)),
        ("rituals", "Rituals", "Routines that kept everyone in step",
         "Process on paper only works if it has a heartbeat. These ran every sprint, so people knew when to bring a proposal, when a decision would be made, and when they'd see what had shipped. Contributions were welcome any day.",
         rituals
         + more("Tools, one per job and the same for all three companies: Azure DevOps for requests and the backlog, Figma for the library and playground files, Storybook as the source for developers, Teams, Slack and Webex for reviews, and mail for release announcements.")),
        ("learnings", "Learnings", "If you're setting up design ops tomorrow", "Write down who decides before you write down how.",
         tiles([("Write down who decides first", "Most process arguments are really ownership arguments."),
                ("Build one front door, and make “no” fast", "Pointing someone to an existing component in a day beats building a new one in a sprint."),
                ("Put criteria on every gate", "A review without a checklist is an opinion. A review with one is a decision."),
                ("Let anyone contribute, curate centrally", "Federation gives you speed; ownership keeps it coherent.")])),
    ],
    gallery=[(O + "flow-component.jpg", "The component lifecycle"), (O + "flow-design.jpg", "The squad design flow"), (O + "cover.jpg", "The operating model at a glance")],
    credits="Aniket Pandey worked on this as a design system designer at IBM, with IBM design and engineering, Riyadh Air's design team and business owners, and Publicis Sapient. This is IBM client work done as an employee, not Layer One client work. Diagrams belong to Riyadh Air and IBM and are shown for portfolio purposes.",
)
page("riyadh-ops", spec)
