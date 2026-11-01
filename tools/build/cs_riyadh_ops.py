from showcase import *

O = "assets/work/ibm-riyadh-air-ops/"

# A text-led case study: the story of how three companies ran one design system without it becoming the bottleneck.
# "We" is the design system team at IBM; the credit line says who did what.

S = [
    section("room", "The room", "<b>01</b> the room:", "Three companies, one library, and requirements that changed every week",
            "Riyadh Air was building an airline from zero, so everything was new at once: the brand, the apps, the teams.",
            wrap(story(prose(
                "Picture the people working on Riyadh Air's apps in 2023. IBM was the lead digital partner, with product squads, a design system team and the front-end engineers who built it in code. Riyadh Air had its own design team, a Digital Experience Director and the business owners who signed things off. Publicis Sapient's designers were building their own product areas on the same library and contributing back to it.",
                "None of these teams had worked together before. Every squad had a product owner and a business analyst, and the client brought new requirements, redesigns and quick iterations every week. All of it landed on one Figma library and one Storybook.",
                "A design system is easy to start and hard to run. This is the story of the operating model behind this one: who owned what, how a request got in, how it got checked, and the routines that kept dozens of people moving in one direction."),
                "At a glance", [("3", "companies on one system"), ("6", "named roles"), ("4", "quality gates"), ("10", "playbook cases")]))),
    section("problem", "The problem", "<b>02</b> the problem:", "Everyone could change it. Nobody owned it.",
            "The same six problems every growing system hits, all in the first few months.",
            wrap(story(prose(
                "None of these were unique to us. Ask anyone who has run a design system at scale and they'll name most of them. What made Riyadh Air different was that all six showed up early, because the system and the product were being born together.",
                "<b>Snowflakes.</b> Three squads built three date pickers, because nobody knew the other two existed.",
                "<b>Drift.</b> The Figma library said one thing and Storybook another, and QA couldn't tell which was right.",
                "<b>A bottleneck.</b> Every change waited on the central team, so squads detached components to keep moving, which created more snowflakes.",
                "<b>No owner.</b> When two companies disagreed about a component, there was no one whose call it was. Decisions went to whoever spoke last.",
                "<b>A moving target.</b> A component approved on Monday could be redesigned by Friday.",
                "<b>Silent changes.</b> Library updates landed without notice and broke screens that had already been signed off.",
                "> How might three companies move fast on one design system, without it falling apart every time the product changes?"),
                "Six problems", [("Snowflakes", ""), ("Drift", ""), ("Bottleneck", ""), ("No owner", ""), ("Moving target", ""), ("Silent changes", "")]))),
    section("belief", "The belief", "<b>03</b> the belief:", "Start with people, not files",
            "",
            wrap(quote("A solid design system begins with people and sound processes. It goes beyond detailed design files and reusable code.")
                 + gap(24)
                 + story(prose(
                     "Everything that followed came from three ideas.",
                     "<b>Treat it as a product.</b> The system has customers (the squads), a backlog, a roadmap and releases, like anything else the airline ships.",
                     "<b>Give every decision an owner.</b> Not a committee: one named role per decision, so nothing waits on a meeting.",
                     "<b>Make everyone a contributor.</b> Every designer is a co-owner. The central team curates; it doesn't gatekeep.")))),
    section("roles", "Roles", "<b>04</b> who decides:", "Six roles, six clear calls",
            "The first thing we did was write down who decides what. Not job titles, but the one question each role answers.",
            wrap(story(prose(
                "<b>The DLS Custodian</b> asks: do we need this, or does it already exist? They own the front door: triage, the backlog, and the announcement when something ships.",
                "<b>The DLS Design Team</b> asks: what should it be? They design and update components, with every state, both languages and both themes.",
                "<b>The Design Director</b> asks: is it good enough? They hold the quality bar in design reviews and in the final review before release.",
                "<b>The Digital Experience Director</b> asks: is it right for Riyadh Air? This is the business owner's approval. Nothing goes to development without it.",
                "<b>The Front-end Team</b> asks: can we build it well? They join technical review early, build the component and publish it to Storybook.",
                "<b>The Product Development Teams</b> ask: what do our users need? These are the squads. They raise requests, contribute components and use what ships.",
                "Once the names were on a page, half the arguments stopped. Most process arguments are really ownership arguments.",
                "Underneath sat a small core team with three owners: a product owner keeping the system delivering the most value to squads, a design owner leading component design and handoff, and an engineering owner leading development and release."),
                "Six roles", [("Custodian", "Does it exist?"), ("Design team", "What should it be?"), ("Design Director", "Is it good enough?"), ("DX Director", "Is it right for us?"), ("Front-end", "Can we build it well?"), ("Squads", "What do users need?")]))),
    section("model", "Operating model", "<b>05</b> the operating model:", "Central owners, federated contributors",
            "Somewhere between one team building everything and everyone building anything.",
            wrap(story(prose(
                "There are three classic ways to run a design system. In a <b>solitary</b> model one team builds for itself, which works until the second product arrives. In a <b>centralised</b> model one team builds for everyone; it stays consistent, and everyone waits in one queue. In a <b>federated</b> model everyone contributes; it's fast, until nobody can say no.",
                "We took the middle path that most mature systems end up on. A small central team owned and curated the system. Every squad had three seats, a designer, an engineer and a product owner, and each seat had a counterpart in the system team. Squads didn't wait for the system; they fed it, through one front door.",
                "The central team stopped being the place where all the work happened and became the place where all the work was checked."),
                "The model", [("Central", "Owns and curates"), ("Federated", "Squads propose and contribute"), ("3 seats", "Designer, engineer, product owner per squad")]))),
    section("door", "Front door", "<b>06</b> one front door:", "Ten kinds of work, one way in",
            "Requests used to arrive in chats, in reviews and in corridors.",
            wrap(story(prose(
                "We gave the system one front door, a ticket in Azure DevOps, and wrote a playbook for the ten kinds of work that came through it: a new component, a change to an existing one, a contribution from a squad, a changelog from Figma, a design-to-development handoff, an audit of an existing component, documentation, a library publish, file distribution and the approval checklist. If you knew which case you were in, you knew the next step.",
                "The first question at the door was always the same: is a component required? The DLS Custodian checked the library first. If the answer was no, the requester got a link to the existing solution in Figma and Storybook, often the same day. If it was yes, the request went into the backlog to be defined, prioritised and planned into a sprint.",
                "> The cheapest component is the one you don't have to build.",
                "Many requests ended at no. That was the point: a fast no kept squads moving and kept the library from filling up with near-duplicates."),
                "The door", [("1 ticket", "In Azure DevOps"), ("10 cases", "Each with a next step"), ("Same day", "For many “it already exists” answers")]))),
    section("flow", "The flow", "<b>07</b> request to release:", "A gate, with an owner, at every handoff",
            "Every component went through the same five steps: propose, design, code, document, release.",
            wrap(story(prose(
                "Each step ran the same small loop inside it: start, compose, test, present, review, deliver. Between the big steps sat a gate, and every gate had a named owner and a written list of criteria. Fail a gate and the work went back one step, not back to the start.",
                "<b>Gate 1, definition of ready.</b> Is the request ready to plan? A use case, where it's used, and a Figma playground link.",
                "<b>Gate 2, proposal criteria.</b> Is it used in more than one place? Can it be solved by an existing component? Is it new, or a variant?",
                "<b>Gate 3, development handoff.</b> Every state, both languages, both themes, tokens only, annotated for developers. The Digital Experience Director signs off before development starts.",
                "<b>Gate 4, component handoff.</b> QA passed, Figma and Storybook match, documented and ready to announce. Changes were announced, not discovered.",
                "> A review without a checklist is an opinion. A review with one is a decision.")
                + bigfig(O + "flow-component.jpg", "The working lifecycle diagram we shared with all three companies: who is in each step, and which tool it happens in.", bg="#fff", pad="14px"),
                "Five steps", [("Propose", "Gate 1: ready"), ("Design", "Gate 2: proposal"), ("Code", "Gate 3: dev handoff"), ("Doc", "Gate 4: component handoff"), ("Release", "Announced")]))),
    section("reviews", "Squad reviews", "<b>08</b> squad reviews:", "Four pairs of eyes before a developer",
            "The same thinking applied to product screens, not just components.",
            wrap(story(prose(
                "With three companies designing at once, a screen passed four reviews, each by a different pair of eyes. First a peer review, by another designer in Figma and Slack. Then the design lead. Then Riyadh Air's own design team, in Teams. Finally a handover, where engineers walked through the screen with the designer before it moved to development.",
                "Every no went back to the designer with comments, so feedback was a loop, not a wall. And because each review had a different owner, no single person became the place where screens piled up.")
                + bigfig(O + "flow-design.jpg", "The squad design flow from a user story to done. Green is yes; red sends the work back with comments.", bg="#fff", pad="14px"),
                "Four reviews", [("Peer", "Another designer"), ("Design lead", "Quality bar"), ("Riyadh Air", "The client's design team"), ("Dev handover", "Walk-through with engineers")]))),
    section("contribute", "Contribution", "<b>09</b> contribution:", "Anyone could be the one to make things change",
            "The library was the status quo, and anyone was allowed to challenge it.",
            wrap(story(prose(
                "A designer, a developer, even a copywriter: if a component fell short, the person who hit the problem started the contribution, owned together with the design owner. It had four steps.",
                "<b>Identify.</b> Copy the Figma playground file, which holds a checklist, a space for the use case and a space for research.",
                "<b>Submit.</b> Raise a ticket or post in the design system channel, answering five questions: is it new or existing, where will it be used, what's the use case, why do we need it, and where's the playground.",
                "<b>Proposal review.</b> An open forum. Anyone could join, whatever their discipline, and the checklist decided: will it be used more than once, is it a new problem, and is it a new component or a variant of one we have? Most proposals ended up as a variant.",
                "<b>Define requirements.</b> A consolidation review with at least one developer to agree variants, states and props, then a ticket in the backlog.")
                + ticket("DS-214", "In review", "Seat selector: add a “blocked” state", [
                    ("New or existing?", "Existing · G06/B05"), ("Where will it be used?", "Booking, check-in, manage trip"),
                    ("Use case", "Seats held for crew or exit rows"), ("Why do we need it?", "Today squads grey it out by hand"), ("Playground", "Figma file linked")],
                    "An illustrative ticket, following the five questions every submission answered."),
                "Four steps", [("Identify", "Playground file"), ("Submit", "Five questions"), ("Review", "Open forum"), ("Define", "With a developer")]))),
    section("rituals", "Rituals", "<b>10</b> rituals:", "A heartbeat every sprint",
            "Process on paper only works if it has a rhythm people can plan around.",
            wrap(story(prose(
                "Seven routines ran every sprint, so people knew when to bring a proposal, when a decision would be made, and when they'd see what had shipped.",
                "Contributions were welcome any day. At the start of the sprint came <b>definition and prioritisation</b>: agree a component's states, behaviour and priority before anyone opens Figma. Mid-sprint, <b>component design reviews</b> for critique from designers and stakeholders, and <b>engineering handoffs</b> to walk through details and agree requirements. <b>Engineering QA</b> ran asynchronously, with designers and engineers reviewing the build together. At the end of the sprint, <b>design approvals</b> checked the work against the definition of done, and <b>demos and release</b> packaged it, showed it and told every stakeholder.",
                "The tools were the same for all three companies, one per job: Azure DevOps for requests and the backlog, Figma for the library and playground files, Storybook as the source for developers, Teams, Slack and Webex for reviews, and mail for release announcements.",
                "> Routines on the calendar did more for adoption than any document."),
                "Every sprint", [("Start", "Define and prioritise"), ("Mid-sprint", "Reviews and handoffs"), ("Async", "Engineering QA"), ("End", "Approvals, demo, release")]))),
    section("impact", "What changed", "<b>11</b> what changed:", "Fast and consistent, at the same time", "",
            wrap(story(prose(
                "<b>Clarity.</b> Every decision had one owner. Disagreements between companies had a named person to settle them, and new joiners learnt the process from one page.",
                "<b>Speed.</b> Squads proposed and contributed components themselves, through one front door, instead of waiting in a queue. Many requests ended the same day with a link to something that already existed.",
                "<b>Quality.</b> Every component passed the same four gates before release, so what was approved in Figma was what shipped in code. Changes were announced, not discovered.",
                "<b>Adoption.</b> IBM, Riyadh Air and Publicis Sapient ran the same routines, and the model held through weekly changes from zero to launch."),
                "Outcomes", [("1 owner", "For every decision"), ("No queue", "Squads contribute"), ("Figma = code", "Four gates"), ("3 companies", "One rhythm")]))
                 + gap(16) + lessons(["Write down who decides before you write down how.", "Build one front door, and make “no” fast.", "Let anyone contribute, but curate centrally."])),
    section("playbook", "For your team", "<b>12</b> for your team:", "The same operating model, set up for you",
            "If your design system team has become the slowest step in shipping, this is how we'd start.",
            wrap(playbook({"audit": "Map who decides what today, where requests come from, and where design and code drift.",
                           "foundations": "Set up the front door, the gates and the roles alongside your core system.",
                           "partner": "Run the rituals with your teams until they run themselves."}))),
]

page("ibm-riyadh-air-ops", dict(
    h1="Three companies, one design system: who decides what ships?",
    lede="How IBM, Riyadh Air and Publicis Sapient ran one library without it becoming the bottleneck: roles, one front door, four gates and a sprint rhythm.",
    meta=[("Role", "Design system designer, IBM"), ("Client", "Riyadh Air"), ("Partners", "Riyadh Air design, Publicis Sapient"), ("Focus", "Governance, contribution, rituals")],
    proof=[("", "3", "", "companies, one system"), ("", "6", "", "named roles"), ("", "4", "", "quality gates"), ("", "10", "", "playbook cases")],
    cover_alt="Riyadh Air design operations: the five-step flow with its gates and the six roles, on lavender",
    sections=S,
    credits="Told by Aniket Pandey, who worked on this as a design system designer at IBM (2023–24), with IBM design and engineering, Riyadh Air's design team and business owners, and Publicis Sapient. “We” is the IBM design system team. This is IBM client work done as an employee, not Layer One client work. Diagrams belong to Riyadh Air and IBM and are shown for portfolio purposes.",
))
