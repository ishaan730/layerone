from cs import *

C = "assets/work/ibm-cardinal-health/"

red = ["#ffeded", "#facfcd", "#f8817e", "#f1635e", "#f14146", "#e41f35", "#ca2035", "#b22233", "#7d111d", "#6d151f"]
ramp = '<div class="m-ramp" data-ramp-live>' + "".join(
    f'<button type="button" style="--c:{c}" data-hex="{c}" data-name="red-{s}"><span>{s}</span></button>'
    for s, c in zip((50, 100, 200, 300, 400, 500, 600, 700, 800, 900), red)) + '''
  <div class="r-read" aria-live="polite"><code data-r-name>red-500</code><code data-r-hex>#E41F35</code><span data-r-w></span><span data-r-b></span></div></div>'''

chain = '''<div class="chainrow"><div><span>What is it?</span><h3>Value</h3><code>#E41F35</code><p>The raw colour. Nobody uses it directly.</p></div>
  <div><span>Which step of which ramp?</span><h3>Primitive</h3><code>red-500</code><p>A step in a ramp, the same in every theme.</p></div>
  <div><span>What is it for?</span><h3>Semantic</h3><code>color-action-primary-surface</code><p>Says what it's for. Squads use this layer.</p></div>
  <div><span>Exactly where?</span><h3>Component</h3><code>Add to cart</code><p>Hover is red-700, pressed is red-900.</p></div></div>'''

sheets = [("Buttons", C + "c-buttons.jpg", "Buttons", "Three types, five states and two sizes, with and without icons."),
          ("Header", C + "c-header.jpg", "Global header", "Logo, navigation, account bar and search, at desktop, tablet and mobile."),
          ("Inputs", C + "c-inputs.jpg", "Inputs", "Text, dropdown, quantity stepper, text area and phone number, each with helper and error text in every state."),
          ("Pickers", C + "c-pickers.jpg", "Date picker and upload", "Calendars, ranges, and file upload with drag and drop."),
          ("Alerts", C + "c-alerts.jpg", "Alerts and banners", "Inline alerts, full-width banners and toasts for success, info, error and warning."),
          ("Tabs", C + "c-tabs.jpg", "Tabs", "Two sizes, on white and on grey, with the active red underline.")]

screens = [("Home", C + "screen-home.jpg", "Home", "A personalised pharmacy home: account bar, search, promotions and quick actions, all from Jarvis."),
           ("Product", C + "screen-pdp.jpg", "Product page", "Product cards, contract badges, quantity steppers and the add-to-cart button."),
           ("Orders", C + "screen-orders.jpg", "Orders", "Tables, filters, status badges and pagination for daily ordering."),
           ("Order details", C + "screen-order-details.jpg", "Order details", "Tabs, shipment status and alerts for a single order."),
           ("Rebates", C + "screen-rebates.jpg", "Rebates", "Insights for a pharmacy's contracts, from the same tokens and components.")]

flow = [("Request", "Any squad", "Any time", "A Jira ticket with the squad's need: what it's for and which screens it touches.", "A ticket in the design system backlog"),
        ("Audit", "Design system owner", "Before design", "Who uses it today, which screens and squads a change would reach, and what could break.", "A scope and a risk list"),
        ("Design", "Design system team", "In the sprint", "Every state and breakpoint, on tokens, annotated for developers.", "A component page in Figma"),
        ("Review", "Design, copy, then engineering", "Mid-sprint", "Design and copy review first, then a technical review with the developers who'll build it.", "An approved design"),
        ("Build", "Engineering", "Next sprint", "Built in Storybook from the annotations.", "A component in code"),
        ("QA", "QA, then the design system owner", "Before release", "QA tests the build, then the owner checks it against the Figma page.", "A build that matches the design"),
        ("Release", "Design system team", "Every release", "A new Storybook version and a changelog, so dev and QA can match a build to its handoff date.", "A versioned release and a changelog")]

spec = dict(
    h1="Jarvis: the design system behind Cardinal Health's new storefront",
    lede="Cardinal Health was rebranding and retiring ordering tools built in the 90s. Its new storefront, Vantus HQ, had many squads and no shared visual language. At IBM, our founder built Jarvis from scratch in Figma: the global styles, tokens and 40+ components every squad built with. Then he ran it as a product, as requests grew five times over in a year.",
    meta=[("Role", "Design system owner, IBM"), ("Client", "Cardinal Health"), ("Team", "IBM India and Columbus, with Cardinal's squads"), ("Timeline", "2022–23")],
    cover=(C + "cover.jpg", "Jarvis for Cardinal Health: the pharmacy home page, a mobile product page, buttons, badges, alerts and colour tokens"),
    tldr=[("The problem", "A rebrand and a new storefront, built by many squads with no shared language. Libraries kept breaking, and what design approved didn't always reach production."),
          ("What we did", "A palette of 110 colours in 11 ramps, tokens named by purpose, 40+ components, and a way of working with engineering and QA."),
          ("What changed", "Every squad built on Jarvis. Tickets grew 5× in a year, and the system went from one owner to a central team of seven.")],
    kpis=[("40", "+", "", "components, from buttons to date pickers"), ("110", "", "", "colours in 11 ramps, each contrast-checked"),
          ("5", "×", "", "more system tickets handled in one year"), ("7", "", "1 → ", "people on the system, from one owner")],
    chapters=[
        ("context", "Context", "A rebrand, and a new storefront",
         "Cardinal Health distributes pharmaceuticals and medical products to about 90% of U.S. hospitals and 60,000+ U.S. pharmacies. It brought in IBM to turn legacy ordering tools into Vantus HQ: one personalised storefront for pharmacies and hospitals.",
         tiles([("Cardinal Health", "Product owners, brand, engineering squads and QA, all moving to the new brand."),
                ("IBM, Columbus studio", "Strategy, research and the day-to-day partnership with the client."),
                ("IBM, India design team", "Five to six designers across squads. Our founder owned Jarvis, with two designers beside him.")], cols=3)),
        ("problem", "Problem", "A new brand, with nothing to hold it together",
         "The rebrand changed how Cardinal looked, but each squad still designed its own screens, and the tools and handoffs in between kept pulling design and code apart.",
         shift([("Every squad, its own UI. Legacy screens from the 90s beside new ones.", "One system every squad builds from."),
                ("Adobe XD libraries broke so often that updates were frozen.", "A Figma library with variables for colour."),
                ("Storybook changes didn't reach production.", "A Storybook version for every structural change."),
                ("Decimal font sizes and a custom grid had QA flagging correct work.", "Whole-pixel type and a grid agreed with engineering.")],
               "Toggle to see what each problem became.")
         + tiles([("Is it versatile enough?", "Will it meet the needs of every squad, not just the one asking?"),
                  ("Who uses this today?", "Which screens and squads would a change reach?"),
                  ("Can it improve without breaking?", "Is there room to change it without undoing work already shipped?"),
                  ("Is the benefit real?", "Does it help the team and the project, or is it just nice to have?")])
         + more("The design question: how might we give every squad one source of truth, in design and in code, that can grow without breaking what's already built?",
                "Those four questions became the test every request had to pass before it went into Jarvis.")),
        ("colour", "Colour", "From one brand red to 110 colours",
         "The rebrand handed over Cardinal Red and a few brand colours. Product UI needs far more: hover and pressed states, quiet backgrounds, status colours that work on white, and text that stays readable. So each brand colour grew into a ten-step ramp, with ramps added for status and neutrals.",
         fig(C + "ramps.jpg", "Eleven ramps, ten steps each, as they live in the Jarvis Figma library. Every swatch carries its own contrast check.")
         + lead("The red ramp, with the real Jarvis values. Select a step to see its contrast.")
         + ramp
         + fig(C + "anatomy-red.jpg", "The annotated ramp: colour space, variable, tones, index and value. Once someone knew them, a name like red-700 told them the family, the step and roughly how dark it was.")
         + more("Five brand colours to start from: Cardinal Red #E41F35 for primary actions and brand moments, Cardinal Black #27251F for text, Cardinal Blue #BBDDE6 for quiet accents, Tertiary Blue #20728B for tertiary actions, and Purple #6F4977 for contracts.",
                "Each ramp runs from 50, a near-white tint, to 900, the darkest shade, with 500 as the true colour. A tick marks the steps that pass where they're meant to be used, so nobody had to guess which red was safe for text.")),
        ("type", "Type and space", "A calm scale for dense ordering screens",
         "Roboto on a Major Second scale, each level 1.125 times the one below from a 16px base. A pure scale gave sizes like 51.96px that browsers rendered blurry and QA couldn't match, so the library was rounded to whole pixels.",
         fig(C + "f-type.jpg", "The type scale page from the Jarvis library, from a 52px H1 down to table text.")
         + fig(C + "f-spacing.jpg", "Spacing in steps of 4 and 8, with rules for the space around icons. Icon sizes run from 8 to 48px.")),
        ("tokens", "Tokens", "Naming colours by what they do",
         "Components used a mix of classes and hard-coded values. Changing the text size in one badge meant editing every badge by hand. So every colour got a name that says what it's for, pointing at a ramp step.",
         chain
         + fig(C + "colour-method.jpg", "The colour method page: five layers from values to variants, ten roles, and stackable suffixes like --pressedFocused for the edge cases.")
         + more("Fourteen semantic sets cover every surface, border, text, icon, action, input and status in Vantus HQ. Swap a mapping and every component that uses the name follows.",
                "A colour changes only through a variant: a status, an emphasis or a state. Worked examples on the same page covered the cases people asked about most.")),
        ("components", "Components", "40+ components, every state drawn",
         "Each component was built on the tokens, with every size, state and breakpoint drawn in Figma, annotated for developers and rebuilt in Storybook. Every page had the same layout: variants in a grid, states across the top, sizes down the side.",
         fig(C + "component-board.jpg", "A selection of component pages from the Jarvis library.")
         + tabs("Component sheets", sheets)),
        ("product", "In the product", "What squads built with it",
         "Different squads owned home, catalogue, orders and insights. Because they all built from Jarvis, Vantus HQ reads as one product.",
         tabs("Vantus HQ screens", screens)
         + '<p class="small muted">Screens use sample data and are shown for portfolio purposes only.</p>'),
        ("running", "Running it", "When the system became the bottleneck",
         "As squads adopted Jarvis, every new screen turned into requests: a new variant, a fix, a question. The design system went from a side project to a product team.",
         bars([("Tickets", 120, 900, "~120, Sep 2022", "~900, Oct 2023"), ("People on the system", 1, 7, "1", "7")],
              "When our founder took over as dedicated owner, and thirteen months later.")
         + fig(C + "jira-chart.jpg", "Cumulative design system tickets in Jira, February 2022 to October 2023.")
         + tiles([("Process refinement", "A defined workflow for design, development and QA, with a definition of done for every step."),
                  ("Governance", "Clear rules for what goes into Jarvis, who decides, and how squads contribute."),
                  ("Planning with squads", "Backlog refinement every sprint, so work landed in the order squads needed it."),
                  ("Docs and training", "A design system site in Confluence, one place for questions, playbacks and reviews.")])
         + fig(C + "sprint-board.jpg", "One board shared with every squad: one sprint per column, one kind of work per row.")),
        ("code", "Design to code", "Keeping Figma and Storybook in step",
         "Every component went through the same seven steps, and the owner checked each one himself before it went out. Step through them.",
         stepper("Jarvis workflow", flow)
         + more("Months in, structural changes in Storybook turned out not to reach production, so QA kept flagging work. With engineering, a new version was added for every structural change.",
                "A changelog just for developers recorded every update, and was later automated. When XD libraries were frozen, Jarvis was rebuilt in Figma with variables for colour.")),
        ("learnings", "Learnings", "What we'd take to the next system", "A system is a product, and it isn't done until the build matches the design.",
         tiles([("A system is a product", "It needs planning, a backlog and a roadmap, not just a library."),
                ("Check that design reaches production", "A component is done when the build matches it, not when it's approved in Figma."),
                ("Quality over speed", "Rushed fixes for urgent requests became debt. A little longer meant less maintenance later."),
                ("Share the ownership", "People adopt what they help shape. Docs and training answer the same question a hundred times.")])),
    ],
    gallery=[(C + "f-icons.jpg", "Icon sizes, and where each one is used"), (C + "c-footer.jpg", "Footer, desktop and tablet"), (C + "c-accordion.jpg", "Accordion, light and dark"),
             (C + "c-toggles.jpg", "Toggle switches"), (C + "mobile-pdp.jpg", "A product page on mobile"),
             (C + "arcs.jpg", "Brand arcs from the rebrand")],
    credits="Led by Aniket Pandey as design system owner at IBM, with two IBM India designers, the IBM Columbus studio, and Cardinal Health's product, engineering and QA teams. This is IBM client work done as an employee, not Layer One client work. Images belong to Cardinal Health and IBM and are shown for portfolio purposes.",
)
page("cardinal", spec)
