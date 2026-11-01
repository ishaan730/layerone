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
S = [
    section("brief", "Brief", "<b>01</b> the brief:", "A new brand, many squads, nothing holding them together",
            "Cardinal Health was retiring ordering tools from the 90s for one storefront, Vantus HQ. IBM built it.",
            wrap(brief([("squads", "Every squad designed its own buttons, tables and forms", "One system every squad builds from"),
                        ("broken", "Adobe XD libraries broke so often that updates were frozen", "A Figma library with colour variables"),
                        ("drift", "What design approved didn't reach production", "Versioned Storybook, checked against Figma")]))),
    section("work", "The work", "<b>02</b> the work, in twelve frames:", "Swipe through it", "From the colour ramps to the screens squads shipped. Select any frame to see it full size.",
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
    section("colour", "Colour", "<b>03</b> colour:", "One brand red became 110 colours", "Hover any swatch. Every value is the real one from the Jarvis library.",
            wrap(explorer + '<div style="height:16px"></div>' + bento([
                (C + "ramps.jpg", "The ramps in Figma, with a contrast check on every swatch", 8, 4, {"fit": "contain", "bg": "#fff", "pad": "16px"}),
                (C + "anatomy-red.jpg", "The annotated red ramp", 4, 4, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
            ])), mode="paper"),
    section("type", "Type and space", "<b>04</b> type and space:", "A calm scale for dense ordering screens", "Roboto on a 1.125 scale, rounded to whole pixels so QA could match the build.",
            wrap(bento([
                (C + "f-type.jpg", "Major Second type scale, 16px base", 7, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                ("html", '<div style="height:100%;display:grid;align-content:space-between;padding:20px;background:var(--f);color:#fff;border-radius:12px"><span class="small" style="opacity:.8">The fix QA asked for</span><div><p style="font-size:clamp(28px,3.4vw,48px);letter-spacing:-.04em;line-height:1"><s style="opacity:.55">51.96px</s><br>52px</p><p class="small" style="margin-top:10px;opacity:.85">A pure scale rendered blurry. Whole pixels ended the rework.</p></div></div>', 5, 4, {}),
                (C + "f-spacing.jpg", "Spacing in steps of 4 and 8", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
                (C + "f-icons.jpg", "Icon sizes, 8 to 48px", 6, 3, {"fit": "contain", "bg": "#fff", "pad": "12px"}),
            ]))),
    section("tokens", "Tokens", "<b>05</b> tokens:", "Colours named for what they do", "Squads use the semantic name. Change the mapping once and every component follows.",
            wrap(chain + '<div style="height:16px"></div>' + bigfig(C + "colour-method.jpg", "The colour method: five layers, ten roles, and stackable states like --pressedFocused.", bg="#fff", pad="16px"))),
    section("components", "Components", "<b>06</b> components, live:", "Try the real thing", "Rebuilt in code from the Jarvis specs. Hover and press Add to cart to see its tokens change.",
            wrap(specimen + '<div style="height:28px"></div>' + inventory("46", "components across six families, from buttons to the global header", fams)), mode="stage"),
    section("sheets", "Spec sheets", "<b>07</b> every state, drawn:", "One layout for every component page", "Variants in a grid, states across the top, sizes down the side.",
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
    section("product", "In the product", "<b>08</b> in the product:", "Five squads, one storefront", "Home, catalogue, orders and insights were owned by different squads. It reads as one product.",
            wrap(devices)),
    section("running", "Running it", "<b>09</b> running it:", "When adoption became the bottleneck", "Every new screen turned into requests. So the system was run like a product.",
            wrap(nums([("~", "120", "", "tickets when Jarvis got a full-time owner, Sep 2022", "Before"), ("~", "900", "", "tickets by Oct 2023, most of them done", "After"),
                       ("", "5", "×", "more work handled in a single year", "Throughput"), ("1 → ", "7", "", "people on the system in four months", "Team")])
                 + '<div style="height:16px"></div>' + bento([
                     (C + "jira-chart.jpg", "Cumulative tickets in Jira, Feb 2022 to Oct 2023", 7, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                     (C + "sprint-board.jpg", "One board shared with every squad", 5, 4, {"fit": "contain", "bg": "#fff", "pad": "14px"}),
                 ])
                 + '<div style="height:32px"></div>' + rail([("Request", "A Jira ticket with the squad's need"), ("Audit", "Who uses it, what could break"), ("Design", "Every state and breakpoint"),
                                                         ("Review", "Design and copy, then tech"), ("Build", "In Storybook, from annotations"), ("QA", "QA, then the owner's own check"), ("Release", "A version and a changelog")]))),
    section("impact", "Impact", "<b>10</b> what changed:", "Consistent, faster, and in step with code", "",
            wrap(outcomes([("Consistency", "One look", "Home, catalogue, orders and insights from the same 40+ components."),
                           ("Throughput", "5× tickets", "Close to 900 by October 2023, planned with squads every sprint."),
                           ("Quality", "Design = code", "Storybook versions and a changelog cut the work QA flagged."),
                           ("Team", "1 → 7", "From one owner to a central team, with docs on Confluence.")])
                 + '<div style="height:16px"></div>' + lessons(["A system is a product: it needs a backlog and a roadmap, not just a library.",
                                                               "A component isn't done when Figma approves it. It's done when the build matches.",
                                                               "People adopt what they help shape. Share the ownership."]))),
    section("playbook", "For your team", "<b>11</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "The four questions every Jarvis request had to answer, run across your library.",
                           "foundations": "Ramps with contrast built in, purpose-named tokens and your core components, like Jarvis.",
                           "partner": "Run it as a product: intake, versions, a changelog and planning with your squads."}))),
]

page("ibm-cardinal-health", dict(
    h1="Jarvis: the design system behind a pharmacy storefront",
    lede="Built from scratch at IBM for Cardinal Health's Vantus HQ, then run as a product while requests grew five times over.",
    tags=["Foundations", "Tokens", "40+ components", "Design operations"],
    proof=[("", "40", "+", "components, every state drawn"), ("", "110", "", "colours in 11 ramps"), ("", "5", "×", "more tickets handled in a year"), ("1 → ", "7", "", "people on the system")],
    cover_alt="Jarvis for Cardinal Health: the pharmacy home page, a mobile product page and Jarvis components on Cardinal red",
    client_logo=C + "logo-white.png",
    sections=S,
    credits="Led by Aniket Pandey as design system owner at IBM (2022–23), with two IBM India designers, the IBM Columbus studio, and Cardinal Health's product, engineering and QA teams. This is IBM client work done as an employee, not Layer One client work. Images belong to Cardinal Health and IBM and are shown for portfolio purposes; screens use sample data.",
))
