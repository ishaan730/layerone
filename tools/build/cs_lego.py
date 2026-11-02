"""CARS24: LEGO, the component system built after the rebrand. Showcase engine (see showcase.py).

Visual-first and static: every chapter is a short story plus one or two annotated boards. The boards
(paper, marker notes, real screens and component sheets from the CARS24 LEGO Figma file) are drawn in
tools/covers/lego.html and rendered with node tools/covers/render_lego.js.
"""
from showcase import *

L = "assets/work/cars24-lego/"


def board(name, cap, alt=None):
    """One full-width annotated board, with a caption that says what to look at."""
    return f'<figure class="sc-fig lg-board">{simg(L + "b-" + name + ".jpg", alt or cap, cap=cap)}<figcaption>{cap}</figcaption></figure>'


fams = [("Actions", ["Button", "Pill button", "Icon button", "Link button", "Social button", "Button group", "Stack button", "Caption button", "Search button"]),
        ("Inputs", ["Text input", "Number input", "Phone input", "Car registration input", "Verification input", "OTP generate", "File upload", "Slider"]),
        ("Selection", ["Checkbox", "Radio button", "Switch", "Choice chips", "Segment control", "Rating"]),
        ("Feedback", ["Global alert", "System alert", "Inline alert", "Toast", "Snackbar", "Tooltip", "Loader", "Circular loader", "Loader dots"]),
        ("Navigation", ["Tab", "Breadcrumb", "Bottom bar", "App header", "Home header", "Stepper, horizontal", "Stepper, vertical"]),
        ("Display", ["Badge", "Tag", "Avatar", "Divider", "Accordion"])]

S = [
    section("context", "Context", "<b>01</b> the starting point:", "New colours. Same old parts.",
            "The 2024 rebrand changed how CARS24 looked. The components underneath it hadn't changed at all.",
            wrap(board("audit", "Audit of the live app and mobile web in early 2025: campaign art in the header, one-off title styles, three badge styles, and two different homepages.")
                 + gap(40)
                 + story(prose(
                     "The rebrand moved the palette to OKLCH and carried a new blue through a four-layer token system. That is its own case study. But tokens only recolour what's already there. The buttons, chips, cards and headers were the same old components in new colours, and the app and mobile web still had two different homepages.",
                     "So the rebrand became the chance to rebuild the interface too. The team called the new system LEGO: small, solid parts that any team can put together.",
                     "Aniket led it as Design Systems Lead at CARS24, with a small group of system designers and product designers from each country."),
                     "The project", [("2025", "CARS24"), ("Role", "Design Systems Lead"), ("Platforms", "Android, iOS, mobile web"), ("Built on", "The 2024 rebrand tokens")])
                 + '<p class="sc-note">The chapter before this one: <a href="cars24-tokens.html">one colour system for 10+ products in three countries</a>.</p>')),
    section("teams", "Three teams", "<b>02</b> who it was for:", "Like three companies inside one",
            "India, the UAE and Australia each had their own business, product and design teams, and their own plans.",
            wrap(board("teams", "Each country ran almost as its own company. Left alone, each would keep building its own version of the same component.")
                 + gap(40)
                 + story(prose(
                     "That was the hardest part of the job. A system made for one team would be ignored by the other two. The UAE also needed every screen in Arabic, reading right to left. And redesigns of the homepage, listing and product pages were already planned, so LEGO had to be ready before those teams started, or they would build their own again.",
                     "> How might we give three teams with three roadmaps one set of components they'd actually choose?")))),
    section("feel", "Look and feel", "<b>03</b> look and feel, first:", "Tested on real pages before drawing a component",
            "Shadows, strokes, fills, radius, icons and contrast, each tried on real pages and reviewed with designers from every country.",
            wrap(board("lookfeel", "The same components in four looks, side by side on one page. The notes are what the review decided.")
                 + gap(24)
                 + story(prose(
                     "Before building anything, the team decided how LEGO should look and feel for the next few years. Nothing was too small to test: should shadows pop or barely show, what colour should they be, how dark can a border get before everything looks like a form, which corner radii are allowed.",
                     "Every option went onto real pages, not empty artboards: busy listing pages, light marketing pages, banners and forms. Designers from the country teams reviewed them side by side, so the decisions belonged to them too."),
                     "What came out", [("Stroke", "for structure"), ("Fill", "for grouping"), ("Shadow", "only for things that lift"), ("Radius", "a short list of allowed values")])
                 + gap(40) + board("surfaces", "Surface studies: hairline strokes against fills, and a shadow scale whose shadows were named after the components that use them.")
                 + gap(16) + board("contrast", "Icon containers, a contrast check on every fill step, and text buttons tested by weight."))),
    section("type", "Typography", "<b>04</b> typography:", "A type scale built for busy pages",
            "Listing cards carry price, EMI, kilometres, fuel, owners and badges. Fonts were tested there first.",
            wrap(board("type", "LEGO's type tokens carry their size in their name, and each size has its own line height. Prices and Arabic set the limits.")
                 + gap(24)
                 + story(prose(
                     "Candidate fonts were set into real pages from the apps: listings and product pages packed with information first, then light landing pages and marketing banners. The team checked how each font handled numbers and prices, how it sat next to Arabic, and how many lines a listing card took at each size.",
                     "The scale that came out of it names each size by its numbers. In $lego-font-size-150, 150 means 15px, and every size carries its own line height. Small text gets more space between lines, big text gets less.")))),
    section("before", "Before and after", "<b>05</b> on real screens:", "Same page. New parts.",
            "Every foundation decision was checked against the live homepage, so we could see what users would actually get.",
            wrap(board("ba", "The CARS24 app homepage before LEGO (left) and rebuilt on it (right). Numbers link each change to the part that replaced it.")
                 + gap(16) + board("baweb", "Mobile web before and after. The web and the app now share every component; only the browser bar is different.")), mode="stage"),
    section("pick", "What to build first", "<b>06</b> what to build first:", "Not the button",
            "Start with what the next roadmap is blocked on, used by the most teams and hardest to get right.",
            wrap(board("pick", "The planning board, recreated: components spotted in each team's product walkthroughs, the first list of 26, and the first batch of 12.")
                 + gap(24)
                 + story(prose(
                     "Most design systems start with a button. It looks simple and safe, but no team needs another team to give them a button. So the team did the opposite: collected each country's roadmap, sat through product walkthroughs, and noted every component on the screen.",
                     "Components that showed up for many teams, and on next quarter's plans, went first. That put the hard ones early: inputs, chips and filters, alerts and tabs. Building those first is what earned the system credibility.",
                     "Before drawing anything, the team looked for the best version a country team had already built and started from it. Product designers kept designing products; the system team did the merging."),
                     "Batches", [("Batch 1", "12 components every form and listing needed"), ("Batch 2", "Split across three system designers"), ("Batch 3", "The rest, plus what teams asked for along the way")])
                 + gap(40) + board("batches", "Three batches in the order the roadmaps needed them. Every component followed the same steps from skeleton to QA."))),
    section("compose", "Composability", "<b>07</b> built to be composed:", "Slots, not a variant for every case",
            "Small private atoms, public components with slots, then compositions teams could copy and change.",
            wrap(board("anatomy", "One text input built from five private atoms. Turning slots on and off makes it a phone field, a registration field, a verification code or a search box.")
                 + gap(16) + board("compose", "Search, composed from LEGO parts: header, input, choice chips, icon buttons and cards. Compositions like this became the pattern library.")
                 + '<p class="sc-note">The next chapter: <a href="cars24-pattern-library.html">a pattern library that builds pages from tested blocks</a>.</p>'), mode="stage"),
    section("library", "Library", "<b>08</b> the library:", "44 components in six families", "Every sheet carries its states, sizes, usage notes and the date it last changed.",
            wrap(board("kit", "A selection from the LEGO library: buttons, toasts, chips, alerts, switches, tabs, segments, steppers, avatars and snackbars.")
                 + gap(24) + inventory("44", "components, each built from shared atoms", fams))),
    section("qa", "QA", "<b>09</b> definition of done:", "One prop per concern",
            "Every state is its own property, named the same in Figma and in code, and every component was QA'd before release.",
            wrap(board("states", "The text input across its states, the state model from the guideline, and the steps every component went through before release.")
                 + gap(24)
                 + story(prose(
                     "The state modelling guideline set one rule: don't merge states into a single property like hoverErrorDisabled. Interaction, disabled, read-only and validation are separate props, with the same names designers see in Figma and engineers use in code.",
                     "For every component the team found its skeleton in the live product, defined its properties and variants, wrote the basic documentation, then ran it through a QA checklist and recorded the result.")))),
    section("adoption", "Adoption", "<b>10</b> adoption:", "Run like a launch, team by team",
            "A library nobody uses is a museum. The rollout was planned as carefully as the components.",
            wrap(board("rollout", "Rollout in 2025: research, three batches, workshops and office hours, then the homepages in all three countries.")
                 + gap(24)
                 + room([("Workshops", "How composability works", "Hands-on sessions where designers rebuilt their own screens from LEGO slots and atoms."),
                         ("Office hours", "Weekly, open to everyone", "Bring a screen, leave with an answer. Questions that kept coming up became usage notes."),
                         ("Arabic", "A loop with the UAE team", "Right-to-left checks on every component, and help adapting their screens to the new system.")]))),
    section("shipped", "Shipped", "<b>11</b> shipped:", "The theme changes. The parts don't.",
            "Buy, sell, loans and car check, rebuilt on LEGO, each business line on its own theme.",
            wrap(board("verticals", "Sell on green, car check on brown, loans on blue, explore on the brand colour: the same header, search, tabs, cards and list rows.")
                 + gap(16) + board("pages", "Pages rebuilt on LEGO, top to bottom: buy, the homepage, sell, car check and loans.")), mode="stage"),
    section("impact", "Impact", "<b>12</b> what changed:", "From an old kit to one system in three countries", "",
            wrap(outcomes([("Reach", "3 countries", "The homepages for India, the UAE and Australia moved to LEGO."),
                           ("Pages", "Core flows", "Buy, sell, listing cards and product pages, redesigned on the new system."),
                           ("Library", "44 components", "Built from five shared atoms, with slots instead of endless variants."),
                           ("Teams", "Adopted, not imposed", "Built in the order the teams' own roadmaps needed it.")])
                 + gap(16) + lessons(["Don't start with the button. Start with the component the next roadmap is blocked on.",
                                      "Test the look and feel on real pages before drawing a single component.",
                                      "Composable slots beat a variant for every case, and let teams make their own versions."]))),
    section("playbook", "For your team", "<b>13</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "Roadmap and product walkthroughs, an audit of your live screens, and a scored list of what to build first.",
                           "foundations": "Look-and-feel tests on your real pages, then the first batch of composable components.",
                           "partner": "Next batches, QA, office hours and workshops, team by team, until it's in the product."}, employer="CARS24"))),
]

page("cars24-lego", dict(
    h1="LEGO: the component system after the rebrand",
    lede="How CARS24 tested a new look and feel on real screens, picked its first components from teams' roadmaps, and got 44 composable parts adopted in three countries.",
    meta=[("Role", "Design Systems Lead, CARS24"), ("Markets", "India, UAE, Australia"), ("Platforms", "Android, iOS, mobile web"), ("Timeline", "2025")],
    proof=[("", "44", "", "components in six families"), ("", "26", "", "on the first, roadmap-led list"), ("", "3", "", "countries' apps rebuilt on it"), ("", "3", "", "build batches, in roadmap order")],
    hero=L + "b-hero.jpg",
    cover_alt="Three CARS24 app screens built with LEGO (sell, home and loans) on brand blue, with component pieces floating around them",
    sections=S,
    credits="Aniket Pandey led this as Design Systems Lead at CARS24 (2025), with the CARS24 system designers and the product design teams in India, the UAE and Australia. This is employee work, not Layer One client work. Screens and component sheets belong to CARS24 and are shown for portfolio purposes. The boards are annotated for this page; the planning board is a recreation and its tallies are illustrative.",
))
