from showcase import *

C = "assets/work/ibm-cardinal-health/"

# ---------------------------------------------------------------- colour explorer (real Jarvis values)
STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
RAMPS = {
    "red": ["#ffeded", "#facfcd", "#f8817e", "#f1635e", "#f14146", "#e41f35", "#ca2035", "#b22233", "#7d111d", "#6d151f"],
    "green": ["#f4faf7", "#b8e8cf", "#99deb8", "#73d29f", "#55b97b", "#00a85a", "#269952", "#067f47", "#175c32", "#124726"],
    "yellow": ["#fefaf2", "#ffedc4", "#fee8ad", "#ffd98a", "#fcc954", "#fccc4d", "#f9ba1e", "#b18415", "#896611", "#694e0d"],
    "teal": ["#e7f5f7", "#ceebf0", "#bfe5e8", "#90d4d9", "#64c8ce", "#5bb6bb", "#2e92a1", "#20728b", "#164f61", "#0c2d37"],
    "blue": ["#f8fbfe", "#e0eff4", "#bbdde6", "#b6d9e8", "#a6cfe8", "#80b8db", "#549ed1", "#1274bf", "#0d5288", "#0a4069"],
    "magenta": ["#fcf7fb", "#e8bdd9", "#de9cc7", "#cf70ad", "#cb52ab", "#b13590", "#a13083", "#7e2666", "#611d4f", "#4a163c"],
    "violet": ["#f7f6fa", "#e5e2f0", "#d1cce3", "#c4bddb", "#bcb4d9", "#aba1cf", "#9c93bc", "#797293", "#5e5972", "#484457"],
    "purple": ["#f5f0f6", "#ded1e2", "#c4abc7", "#b99cc0", "#b08fb8", "#966ba1", "#896193", "#6f4977", "#533b59", "#3f2d44"],
    "orange": ["#fef5ee", "#fcd1b2", "#fab07d", "#f79c59", "#e18e51", "#be7f5f", "#9e5f49", "#77544b", "#634136", "#492c26"],
    "neutral": ["#ffffff", "#f4f6f6", "#efefef", "#e2e9ea", "#d6d6d5", "#b8bbba", "#6b7070", "#58595b", "#404041", "#27251f"],
    "brown": ["#f7f5f2", "#f1ede9", "#eee9e3", "#cbc7c0", "#a9a19d", "#948a85", "#7b6d68", "#675647", "#493d32", "#392f27"],
}
USE = {
    "red-500": "Cardinal Red. Primary actions, the account bar, brand text and icons.", "red-700": "Primary action, hover.", "red-900": "Primary action, pressed.",
    "green-50": "Success surface.", "green-500": "Success border.", "green-700": "Success text and icons.", "yellow-600": "Warning border and surface.",
    "teal-700": "Tertiary Blue. Tertiary actions.", "teal-800": "Tertiary action, hover.", "teal-900": "Tertiary action, pressed.",
    "blue-50": "Info surface.", "blue-200": "Cardinal Blue. Quiet accents.", "blue-700": "Info text, icons and border.",
    "magenta-50": "Error surface.", "magenta-400": "Error border.", "magenta-500": "Error text and icons.", "purple-700": "Contract badges.",
    "neutral-50": "Page background, inverse text.", "neutral-100": "Alternate background, disabled surfaces.", "neutral-500": "Disabled text and icons.",
    "neutral-600": "Input text and borders.", "neutral-900": "Cardinal Black. Text, icons, borders.",
}
rows = "".join(
    f'<div class="sc-ramp-row"><span>{name}</span>' + "".join(
        f'<button type="button" style="--c:{h}" data-hex="{h}" data-name="{name}-{s}" data-use="{USE.get(f"{name}-{s}", "")}"'
        f'{" data-default" if name == "red" and s == 500 else ""} aria-label="{name}-{s}, {h}"></button>' for s, h in zip(STEPS, hexes)) + "</div>"
    for name, hexes in RAMPS.items())
explorer = f'''<div class="sc-ramps" data-rampgrid>
  <div><div class="sc-ramp-steps"><span></span>{"".join(f"<span>{s}</span>" for s in STEPS)}</div><div class="sc-ramp-grid">{rows}</div></div>
  <aside class="sc-ramp-read" aria-live="polite"><div class="sw"><span data-n>red-500</span><span>Aa</span></div>
    <dl><div><dt>Value</dt><dd data-h>#E41F35</dd></div><div><dt>On white</dt><dd data-w></dd></div><div><dt>On Cardinal Black</dt><dd data-k></dd></div></dl>
    <p data-u></p></aside>
</div>'''

# ---------------------------------------------------------------- token chain
chain = '''<div class="sc-chain">
  <div><span>Value</span><div class="sw" style="--c:#e41f35"></div><h3>#E41F35</h3><p class="small muted">Stored once.</p></div>
  <div><span>Primitive</span><div class="sw" style="--c:linear-gradient(90deg,#ffeded,#f8817e,#e41f35,#b22233,#6d151f);background:var(--c)"></div><code>red-500</code><p class="small muted">A step in a ramp.</p></div>
  <div><span>Semantic</span><div class="sw" style="--c:#e41f35;display:grid;place-items:center;color:#fff;font-size:13px">action · primary · surface</div><code>color-action-primary-surface</code><p class="small muted">Named for what it does.</p></div>
  <div><span>Component</span><div class="sw" style="--c:#fff;display:grid;place-items:center"><span style="background:#e41f35;color:#fff;padding:7px 14px;border-radius:4px;font:500 13px Roboto,Arial,sans-serif">Add to cart</span></div><code>button / primary</code><p class="small muted">What squads place.</p></div>
</div>'''

# ---------------------------------------------------------------- live specimen
specimen = f'''<div class="jv" data-jv>
  <div class="jv-top"><img src="../{C}logo-white.png" alt="Cardinal Health" width="480" height="155"><span class="acct">Medical Village Apothecary · #6293333444</span><span class="search"><span>Search for products</span><span aria-hidden="true">⌕</span></span></div>
  <div class="jv-body">
    <div class="jv-cell"><p class="jv-k">Buttons</p>
      <div class="jv-row"><button type="button" class="jb jb-p" data-tokbtn>Add to cart</button><button type="button" class="jb jb-s">Quick view</button><button type="button" class="jb jb-t">View all</button></div>
      <div class="jv-row"><button type="button" class="jb jb-p jb-sm">Buy now</button><button type="button" class="jb jb-s jb-sm">Add to list</button><button type="button" class="jb jb-p jb-sm" disabled>Disabled</button></div></div>
    <div class="jv-cell"><p class="jv-k">Inputs</p>
      <div class="jf"><span>Quantity</span><span class="jq"><button type="button" data-d="-1" aria-label="Decrease">−</button><output>1</output><button type="button" data-d="1" aria-label="Increase">+</button></span></div>
      <label class="jf err"><span>PO number</span><input type="text" value="PO-88A"><em>Use 6 digits, like 104452</em></label></div>
    <div class="jv-cell"><p class="jv-k">Selection</p>
      <label class="jc"><input type="checkbox" checked>Include backorders</label><label class="jc"><input type="checkbox">Generics only</label>
      <label class="jc"><input type="radio" name="jv-ship" checked>Standard delivery</label><label class="jc"><input type="radio" name="jv-ship">Next day</label>
      <button type="button" class="jt" role="switch" aria-checked="true"><i></i>Notifications</button></div>
    <div class="jv-cell"><p class="jv-k">Alerts</p>
      <p class="ja" style="--b:#00a85a;--bg2:#f4faf7"><b>Success.</b> Order 162620413 was placed.</p>
      <p class="ja" style="--b:#1274bf;--bg2:#f8fbfe"><b>Info.</b> Prices update at 9:00 AM.</p>
      <p class="ja" style="--b:#f9ba1e;--bg2:#fefaf2"><b>Warning.</b> 1 shipment is delayed.</p>
      <p class="ja" style="--b:#cb52ab;--bg2:#fcf7fb"><b>Error.</b> 3 items need a backorder.</p></div>
    <div class="jv-cell"><p class="jv-k">Product card</p>
      <article class="jpc"><span class="flag">New launch</span><span class="img" aria-hidden="true">💊</span><span class="ct">CONTRACT 335</span>
        <a href="#components" onclick="return false">Fluticasone Prop Hfa 44mcg 10.6g</a><span style="color:#6b7070">Fluticasone Propionate</span>
        <div class="pr"><span style="font-size:11px;color:#6b7070">INVOICE COST</span><b>$119.66</b></div><button type="button" class="jb jb-s jb-sm">Quick view</button></article></div>
    <div class="jv-cell"><p class="jv-k">Tabs, badges, pagination</p>
      <div class="jtabs"><button type="button" aria-selected="true">Overview</button><button type="button" aria-selected="false">Shipments<i>1</i></button><button type="button" aria-selected="false">Activity<i>2</i></button></div>
      <div class="jbadges"><span class="jbd" style="--b:#067f47">In stock</span><span class="jbd" style="--b:#1274bf">Recommended</span><span class="jbd" style="--b:#b13590">Exception</span><span class="jbd y">Delayed</span><span class="jbd" style="--b:#6f4977">Contract</span></div>
      <div class="jpg"><button type="button" data-d="-1" aria-label="Previous page">‹</button><span>1 of 5</span><button type="button" data-d="1" aria-label="Next page">›</button></div></div>
  </div>
  <div class="jv-tok" data-tokout aria-live="polite"></div>
</div>'''

fams = [("Actions", ["Primary button", "Secondary button", "Tertiary button", "Icon button", "Link", "Option group"]),
        ("Forms", ["Text input", "Text area", "Dropdown", "Native select", "Quantity stepper", "Phone number", "Search field", "Date picker", "Calendar", "File upload", "Drag and drop"]),
        ("Selection", ["Checkbox", "Radio button", "Toggle", "Chip"]),
        ("Feedback", ["Inline alert", "Banner", "Toast", "Badge", "Tooltip", "Status indicator", "Progress bar"]),
        ("Navigation", ["Global header", "Account bar", "Menu", "Mobile menu", "Tabs", "Vertical tabs", "Breadcrumb", "Pagination", "Footer", "Mobile footer"]),
        ("Data display", ["Data table", "Accordion", "Avatar", "Product card", "Metric card", "Chart card", "Carousel", "Order summary"])]

# ---------------------------------------------------------------- product screens
screens = [("Home", "screen-home.jpg", "Pharmacy home"), ("Product", "screen-pdp.jpg", "Product page"), ("Orders", "screen-orders.jpg", "Order history"),
           ("Order details", "screen-order-details.jpg", "Order details"), ("Rebates", "screen-rebates.jpg", "Rebates and compliance")]
tabs_html = "".join(f'<button type="button" aria-selected="{"true" if i == 0 else "false"}" data-src="../{C}{f}" data-alt="Vantus HQ, {a}, built from Jarvis">{t}</button>' for i, (t, f, a) in enumerate(screens))
devices = f'''<div data-screens><div class="sc-screen-tabs" role="group" aria-label="Screens">{tabs_html}</div>
  <div class="sc-devices">
    <div class="sc-browser"><div class="sc-browser-bar"><i></i><i></i><i></i><span>Vantus HQ</span></div><div class="sc-view" tabindex="0" aria-label="Screen, scrolls">{simg(C + "screen-home.jpg", "Vantus HQ, Pharmacy home, built from Jarvis")}</div></div>
    <div class="sc-phone"><div class="sc-view" tabindex="0" aria-label="Mobile product page, scrolls">{simg(C + "mobile-pdp.jpg", "Vantus HQ product page on mobile")}</div></div>
  </div>
  <p class="sc-scroll-hint">Pick a screen, then scroll inside the frames. Screens use sample data.</p></div>'''

# ---------------------------------------------------------------- sections
JIRA = ["Backlog", "Audit", "Design", "Design review", "Tech review", "Ready for dev", "In Storybook", "QA", "Owner check", "Released"]

S = [
    section("client", "Client", "<b>01</b> the client:", "The company behind the pharmacy shelf",
            "Cardinal Health distributes pharmaceuticals and medical products, and gives healthcare providers the data to run better. Its customers order through its platforms every day.",
            wrap(facts([("~90%", "of U.S. hospitals"), ("60,000+", "U.S. pharmacies"), ("10,000+", "specialty offices and clinics"), ("23M+", "patients reached by its adherence tools")])
                 + gap(48)
                 + story(prose(
                     "In 2022 Cardinal Health was in the middle of a rebrand, and retiring the ordering tools its customers had used since the 90s. IBM was brought in to build the replacement: <b>Vantus HQ</b>, one personalised storefront where pharmacies and hospitals order products, track shipments, manage contracts and see their rebates.",
                     "The work was split across squads, each owning part of the product: home, catalogue, orders, insights. IBM's Columbus studio led strategy, research and the day-to-day partnership with the client. The design team in India, five to six designers, designed the product. Aniket owned the design system, with two designers beside him."),
                     "The engagement", [("2022–23", "IBM for Cardinal Health"), ("Vantus HQ", "A storefront for pharmacies and hospitals"), ("Owner", "Aniket Pandey, design system")])
                 + gap(32)
                 + room([("Client", "Cardinal Health", "Product owners, brand, engineering squads and QA, all moving to the new brand."),
                         ("IBM, U.S.", "Columbus studio", "Strategy, research and the day-to-day partnership with the client."),
                         ("IBM, India", "Design team", "Five to six designers across squads, and the design system: one owner and two designers.")]))),
    section("problem", "Problem", "<b>02</b> the problem:", "A new brand, with nothing to hold it together",
            "The rebrand changed how Cardinal looked. It didn't change how its screens were made.",
            wrap(story(prose(
                "Each squad designed its own buttons, tables and forms, so the same element looked different from page to page, and screens from the 90s sat right beside new ones. A customer moving from the home page to their orders could feel the seams.",
                "The tools made it worse. The Adobe XD libraries broke so often that updates were frozen to spare designers the rework. Changes made in Storybook didn't always reach production. Decimal font sizes and a custom grid had QA flagging work that was built exactly as specified, and the same bugs kept coming back.",
                "> How might we give every squad one source of truth, in design and in code, that can grow without breaking what's already built?"),
                "What was breaking", [("Many squads", "Each with its own UI"), ("Frozen", "XD libraries, to avoid rework"), ("Drift", "Approved design ≠ production")])
                 + gap(32)
                 + brief([("squads", "Every squad designed its own buttons, tables and forms", "One system every squad builds from"),
                          ("broken", "Adobe XD libraries broke so often that updates were frozen", "A Figma library with colour variables"),
                          ("drift", "What design approved didn't reach production", "Versioned Storybook, checked against Figma")])
                 + gap(32) + '<p class="sc-sub">Four questions every request had to answer</p>'
                 + tiles([("Is it versatile enough?", "Will it meet the needs of every squad, not just the one asking?"),
                          ("Who uses this today?", "Which screens and squads would a change reach?"),
                          ("Can it improve without breaking?", "Is there room to change it without undoing work already shipped?"),
                          ("Is the benefit real?", "Does it help the team and the project, or is it just nice to have?")]))),
    section("process", "Process", "<b>03</b> how it unfolded:", "From one problem to a team of seven",
            "The system began with one complaint, inconsistent screens, and grew into a product with its own backlog and team.",
            wrap(rail([("Audit", "What every squad had built, and where it broke"), ("Foundations", "Colour, type, spacing and icons"), ("Tokens", "Colours named for what they do"),
                       ("Components", "40+, every state drawn"), ("Run it", "Intake, versions, changelog, training")])
                 + gap(48)
                 + timeline([("Early 2022", "A problem, then a first release", "The first months went into choosing tools, defining the first components and agreeing what the system would support.", "Team: shared"),
                             ("Sep 2022", "A dedicated owner", "Aniket took Jarvis on full time, to manage and maintain it, with the wider design team helping where it could. About 120 tickets.", "Team: 1"),
                             ("Nov 2022", "Squads adopt Jarvis", "Every squad now built from the library, and every new screen turned into requests: a variant, a fix, a question.", "Requests jump"),
                             ("Jan 2023", "A central team of seven", "The system became a dedicated group, still welcoming help from squads as bandwidth allowed.", "Team: 7"),
                             ("Oct 2023", "Close to 900 tickets", "Five times more work handled than a year before, most of it done.", "5× throughput")]))),
    section("work", "The work", "<b>04</b> the work, in twelve frames:", "Swipe through it", "From the colour ramps to the screens squads shipped. Select any frame to see it full size.",
            carousel("The Jarvis work, in twelve frames", [
                (C + "screen-home.jpg", "Pharmacy home", "Every part of the page comes from Jarvis.", {"cover": True}),
                (C + "component-board.jpg", "The component library", "40+ components, each with every state.", {"bg": "#f3f3f1", "pad": "20px"}),
                (C + "ramps.jpg", "110 colours", "Eleven ramps, ten steps, contrast on every swatch.", {"bg": "#fff"}),
                (C + "screen-pdp.jpg", "Product page", "Contract badges, steppers and the add-to-cart button.", {"cover": True}),
                (C + "c-header.jpg", "Global header", "Desktop, tablet and mobile.", {"bg": "#fff"}),
                (C + "colour-method.jpg", "The colour method", "Values, roles and variants on one page.", {"bg": "#fff", "pad": "18px"}),
                (C + "screen-orders.jpg", "Order history", "Tables, filters and status badges.", {"cover": True}),
                (C + "c-alerts.jpg", "Alerts and banners", "Success, info, warning and error.", {"bg": "#fff"}),
                (C + "anatomy-red.jpg", "How to read a ramp", "Family, step and value, annotated.", {"bg": "#fff", "pad": "18px"}),
                (C + "screen-rebates.jpg", "Rebates", "Insights from the same tokens.", {"cover": True}),
                (C + "jira-chart.jpg", "~900 tickets", "Requests grew five times over in a year.", {"bg": "#fff"}),
                (C + "sprint-board.jpg", "One board", "Shared with every squad, one sprint per column.", {"bg": "#fff", "pad": "18px"}),
            ])),
    section("colour", "Colour", "<b>05</b> colour:", "One brand red became 110 colours",
            "The rebrand handed over Cardinal Red and a few brand colours. Product UI needs far more: hover and pressed states, quiet backgrounds, status colours that work on white. Hover any swatch; every value is the real one.",
            wrap(explorer + gap(16) + bento([
                (C + "ramps.jpg", "The ramps in Figma, with a contrast check on every swatch", 8, 4, {"fit": "contain", "bg": "#fff", "pad": "16px"}),
                (C + "anatomy-red.jpg", "The annotated red ramp", 4, 4, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
            ])), mode="paper"),
    section("type", "Type and space", "<b>06</b> type and space:", "A calm scale for dense ordering screens", "Roboto on a 1.125 scale from a 16px base, rounded to whole pixels so QA could match the build.",
            wrap(bento([
                (C + "f-type.jpg", "Major Second type scale, 16px base", 7, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                ("html", '<div style="height:100%;display:grid;align-content:space-between;padding:20px;background:var(--f);color:#fff;border-radius:12px"><span class="small" style="opacity:.8">The fix QA asked for</span><div><p style="font-size:clamp(28px,3.4vw,48px);letter-spacing:-.04em;line-height:1"><s style="opacity:.55">51.96px</s><br>52px</p><p class="small" style="margin-top:10px;opacity:.85">A pure scale rendered blurry. Whole pixels ended the rework.</p></div></div>', 5, 4, {}),
                (C + "f-spacing.jpg", "Spacing in steps of 4 and 8", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
                (C + "f-icons.jpg", "Icon sizes, 8 to 48px", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
            ]))),
    section("tokens", "Tokens", "<b>07</b> tokens:", "Colours named for what they do",
            "Components used a mix of classes and hard-coded values; changing one badge meant editing every badge by hand. Now squads use a name that says what a colour is for, and the name points at a ramp step.",
            wrap(chain + gap(16) + bigfig(C + "colour-method.jpg", "The colour method: five layers, ten roles, and stackable states like --pressedFocused.", bg="#fff", pad="16px"))),
    section("components", "Components", "<b>08</b> components, live:", "Try the real thing", "Rebuilt in code from the Jarvis specs. Hover and press Add to cart to see its tokens change.",
            wrap(specimen + gap(28) + inventory("46", "components across six families, from buttons to the global header", fams)), mode="stage"),
    section("sheets", "Spec sheets", "<b>09</b> every state, drawn:", "One layout for every component page", "Variants in a grid, states across the top, sizes down the side, then links to Storybook and Zeplin.",
            wrap(bento([
                (C + "c-buttons.jpg", "Buttons · 3 types, 5 states, 2 sizes", 4, 6, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-header.jpg", "Global header", 8, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-inputs.jpg", "Inputs", 4, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-pickers.jpg", "Date picker and upload", 4, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-alerts.jpg", "Alerts and banners", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-tabs.jpg", "Tabs", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-accordion.jpg", "Accordion", 4, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-toggles.jpg", "Toggle", 4, 3, {"fit": "contain", "bg": "#fff", "pad": "10px"}),
                (C + "c-footer.jpg", "Footer", 4, 3, {"fit": "contain", "bg": "#27251f", "pad": "10px"}),
            ])), mode="paper"),
    section("product", "In the product", "<b>10</b> in the product:", "Five squads, one storefront", "Home, catalogue, orders and insights were owned by different squads. Because they all built from Jarvis, Vantus HQ reads as one product.",
            wrap(devices)),
    section("bottleneck", "The bottleneck", "<b>11</b> the bottleneck:", "When adoption made the system the slowest step",
            "Shipping Jarvis was the start. Every screen squads built turned into requests, and the system went from a side project to a product with customers.",
            wrap(nums([("~", "120", "", "tickets when Jarvis got a full-time owner, Sep 2022", "Before"), ("~", "900", "", "tickets by Oct 2023, most of them done", "After"),
                       ("", "5", "×", "more work handled in a single year", "Throughput"), ("1 → ", "7", "", "people on the system in four months", "Team")])
                 + gap(48)
                 + story(prose(
                     "### What went wrong first",
                     "<b>Squads waited on us.</b> As a team of one, Aniket prioritised with what he knew at the time. More squads meant more work that couldn't move until the system did.",
                     "<b>Maintenance mode.</b> Rushed fixes for urgent requests, broken XD libraries and too few people left design and technical debt, and little time for anything new.",
                     "<b>Answers lived in one head.</b> Much of the day went into answering the same questions and chasing updates. The designers needed it written down.",
                     "### What we put in place",
                     "A defined workflow for design, development and QA, with a definition of done for every step. Clear rules for what goes into Jarvis, who decides and how squads contribute. Backlog refinement every sprint with the project manager and team lead, so work landed in the order squads needed it. One place for questions, so answers could be reused. And a design system site in Confluence, with playbacks and reviews built from designers' feedback.",
                     "> A system is a product. It needs planning, a backlog and a roadmap, not just a library."),
                     "In short", [("Sep 2022", "One owner, ~120 tickets"), ("Jan 2023", "A team of seven"), ("Oct 2023", "~900 tickets, most done")])
                 + gap(16) + bento([
                     (C + "jira-chart.jpg", "Cumulative tickets in Jira, Feb 2022 to Oct 2023", 7, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                     (C + "sprint-board.jpg", "One board shared with every squad, one sprint per column", 5, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                 ]))),
    section("journey", "A request's journey", "<b>12</b> a request's journey:", "From a Jira ticket to a versioned release",
            "Every change, big or small, took the same path. Here is what one looked like, with the statuses it moved through and the release note at the end.",
            wrap(flowline(JIRA, 7) + gap(8)
                 + '<div class="sc-pair2">'
                 + ticket("JARVIS-412", "In QA", "Quantity stepper: add an error state", [
                     ("Requested by", "Orders squad"), ("Need", "Customers can enter more than a contract allows; the field gives no warning"),
                     ("Audit", "Used on product, cart and quick order: 3 squads, 11 screens"), ("Design", "Error border red-500, helper text, desktop and mobile"),
                     ("Handoff", "Annotated in Figma, linked to Zeplin"), ("Build", "Storybook, next release")],
                     "Illustrative. The fields follow the Jarvis workflow; the ticket itself is an example.")
                 + "<div>" + changelog("Jarvis · Storybook release", "Changelog for developers", [
                     ("Added", "Quantity stepper: error state with helper text"),
                     ("Changed", "Type scale rounded to whole pixels (51.96px → 52px)"),
                     ("Fixed", "Tabs: active underline uses red-500 on grey backgrounds"),
                     ("Breaking", "Grid: custom grid replaced by the agreed 12-column grid")],
                     "Illustrative entries in the format of the automated changelog. Every structural change got a new Storybook version, so dev and QA could match a build to its handoff date.")
                 + gap(16) + prose("Months in, it turned out that structural changes in Storybook weren't reaching production, so QA kept flagging work. With engineering, every structural change got its own version. A changelog just for developers recorded every update, and was later automated.") + "</div></div>"
                 + gap(32) + rail([("Request", "A Jira ticket with the squad's need"), ("Audit", "Who uses it, what could break"), ("Design", "Every state and breakpoint"),
                                   ("Review", "Design and copy, then tech"), ("Build", "In Storybook, from annotations"), ("QA", "QA, then the owner's own check"), ("Release", "A version and a changelog")])), mode="paper"),
    section("impact", "Impact", "<b>13</b> what changed:", "Consistent, faster, and in step with code", "",
            wrap(outcomes([("Consistency", "One look", "Home, catalogue, orders and insights from the same 40+ components."),
                           ("Throughput", "5× tickets", "Close to 900 by October 2023, planned with squads every sprint."),
                           ("Quality", "Design = code", "Storybook versions and a changelog cut the work QA flagged."),
                           ("Team", "1 → 7", "From one owner to a central team, with docs on Confluence.")])
                 + gap(16) + lessons(["A system is a product: it needs a backlog and a roadmap, not just a library.",
                                      "A component isn't done when Figma approves it. It's done when the build matches.",
                                      "People adopt what they help shape. Share the ownership."]))),
    section("playbook", "For your team", "<b>14</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "The four questions every Jarvis request had to answer, run across your library.",
                           "foundations": "Ramps with contrast built in, purpose-named tokens and your core components, like Jarvis.",
                           "partner": "Run it as a product: intake, versions, a changelog and planning with your squads."}))),
]

page("ibm-cardinal-health", dict(
    h1="Jarvis: the design system behind a pharmacy storefront",
    lede="Built from scratch at IBM for Cardinal Health's Vantus HQ, then run as a product while requests grew five times over.",
    meta=[("Role", "Design system owner, IBM"), ("Client", "Cardinal Health"), ("Team", "IBM India and Columbus, with Cardinal's squads"), ("Timeline", "2022–23")],
    proof=[("", "40", "+", "components, every state drawn"), ("", "110", "", "colours in 11 ramps"), ("", "5", "×", "more tickets handled in a year"), ("1 → ", "7", "", "people on the system")],
    cover_alt="Jarvis for Cardinal Health: the pharmacy home page, a mobile product page and Jarvis components on Cardinal red",
    client_logo=C + "logo-white.png",
    sections=S,
    credits="Led by Aniket Pandey as design system owner at IBM (2022–23), with two IBM India designers, the IBM Columbus studio, and Cardinal Health's product, engineering and QA teams. This is IBM client work done as an employee, not Layer One client work. Images belong to Cardinal Health and IBM and are shown for portfolio purposes; screens use sample data. Tickets and changelog entries marked illustrative are examples in the format the team used.",
))
