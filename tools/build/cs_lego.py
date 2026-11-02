"""CARS24: LEGO, the component system built after the rebrand. Showcase engine (see showcase.py).

Sketch boards (paper, marker notes) only where the story shows a problem or a test: the old screens, the
three teams, the look-and-feel tests, the old mobile web and the planning board. They are drawn in
tools/covers/lego.html and rendered with tools/covers/render_lego.js. Everything else is clean HTML with
crisp component crops cut from 2x Figma renders (tools/covers/lego_crops.py, lego_assets.py).
Images are WebP; boards ship at two widths.
"""
from showcase import *
from cs import compare
from PIL import Image
import html as _h

L = "assets/work/cars24-lego/"


def _wh(src):
    return Image.open(OUT + "/" + src).size


def board(name, cap):
    """A sketch board, served at 1100w and 1920w."""
    w, h = _wh(L + f"b-{name}.webp")
    return (f'<figure class="sc-fig lg-board"><img src="../{L}b-{name}-1100.webp" srcset="../{L}b-{name}-1100.webp 1100w, ../{L}b-{name}.webp {w}w" '
            f'sizes="(max-width: 1240px) 100vw, 1200px" width="{w}" height="{h}" alt="{_h.escape(cap)}" loading="lazy" decoding="async" data-lightbox data-cap="{_h.escape(cap)}">'
            f'<figcaption>{cap}</figcaption></figure>')


def kimg(name, alt):
    src = L + f"k-{name}.webp"
    w, h = _wh(src)
    return f'<img src="../{src}" width="{w}" height="{h}" alt="{_h.escape(alt)}" loading="lazy" decoding="async" data-lightbox data-cap="{_h.escape(alt)}">'


def tile(name, label, c=4, dark=False, h=None, mh=None):
    st = f"--c:{c};" + (f"--h:{h}px;" if h else "") + (f"--mh:{mh}px;" if mh else "")
    return f'<figure style="{st}"{" class=dark" if dark else ""}>{kimg(name, label)}<figcaption>{label}</figcaption></figure>'


def phone(name, cap, sw=None, scroll=False, y=None, t=None):
    src = L + f"p-{name}.webp"
    w, h = _wh(src)
    st = (f"--sw:{sw};" if sw else "") + (f"--y:{y};" if y else "") + (f"--t:{t}s;" if t else "")
    dot = "<i></i>" if sw else ""
    return (f'<figure class="lg-phone{" scroll" if scroll else ""}" style="{st}"><div class="f"><div class="v">'
            f'<img src="../{src}" width="{w}" height="{h}" alt="{_h.escape(cap)}" loading="lazy" decoding="async" data-lightbox data-cap="{_h.escape(cap)}"></div></div>'
            f'<figcaption>{dot}{cap}</figcaption></figure>')


# ---------------------------------------------------------------- 04 type, clean
typespec = '''<div class="lg-type">
  <div class="lg-type-rows">
    <div><code>$lego-font-size-170</code><small>17px · 130% · semibold</small><p style="font-size:clamp(22px,2.6vw,34px);line-height:1.3;font-weight:600">Hyundai Creta SX, 2021</p></div>
    <div><code>$lego-font-size-150</code><small>15px · 150% · regular</small><p style="font-size:clamp(19px,2.3vw,30px);line-height:1.5">32,410 km · Petrol · 1st owner</p></div>
    <div><code>$lego-font-size-130</code><small>13px · 140% · regular</small><p style="font-size:clamp(17px,2vw,26px);line-height:1.4;color:#667085">Inspected at 140+ points · 7-day return</p></div>
  </div>
  <div class="lg-type-side">
    <div class="lg-decode"><p class="lg-k">How a token reads</p><p class="big">$lego-font-size-<b>15</b>0</p><p>The number is the size: 150 means 15px. Every size carries its own line height. Small text gets more space between lines, big text gets less.</p></div>
    <div class="lg-prices"><div><span class="lg-k" style="color:#667085">India</span><b>₹9.85 lakh</b><em>EMI ₹15,640/mo</em></div><div dir="rtl"><span class="lg-k" style="color:#667085" dir="ltr">UAE</span><b>٥٤٬٩٠٠ درهم</b><em>قسط ١٬١٢٠ درهم شهرياً</em></div><div><span class="lg-k" style="color:#667085">Australia</span><b>$24,990</b><em>drive away</em></div></div>
    <p class="sc-note" style="margin:0">Shown at twice the size. Prices are illustrative: every market's longest price had to fit the same slot, and Arabic needed the taller line height.</p>
  </div>
</div>'''

# ---------------------------------------------------------------- 06 what to build first
why_rows = [("Choice chips and filters", "Listing, search and filters, in all three countries", "Used on almost every page; four versions already existed to merge"),
            ("Input field", "Sell car, loans, login", "Every form on the roadmap was blocked on it, and it's the hardest to get right"),
            ("Alert", "Loans, car check", "New verticals needed clear states for errors, warnings and success"),
            ("Tabs and segment control", "Homepage, explore, listing", "The homepage redesign was built around them"),
            ("Badge", "Every listing card", "Three badge styles on one screen were the loudest problem in the audit"),
            ("Button", "Everywhere", "In batch 1 because every form needs one, but never the starting point: every team already had their own")]
why = '<div class="lg-why"><table><thead><tr><th scope="col">Component</th><th scope="col">Who needed it next</th><th scope="col">Why it went in batch 1</th></tr></thead><tbody>' + "".join(
    f"<tr><th scope=row>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in why_rows) + "</tbody></table></div>"

batches = f'''<div class="lg-batches">
  <article class="lg-batch"><figure>{kimg("chips", "Choice chips, batch 1")}</figure><div><span class="lg-k">Batch 1 · 12</span><h3>What every roadmap was blocked on</h3><p>The parts of every form and listing the country teams were about to redesign.</p>
    <ul><li>Checkbox</li><li>Radio</li><li>Toggle</li><li>Input field</li><li>Accordion</li><li>Breadcrumb</li><li>Segment</li><li>Badge</li><li>Tab</li><li>Chip</li><li>Button</li><li>Alert</li></ul></div></article>
  <article class="lg-batch"><figure>{kimg("toast", "Toast, batch 2")}</figure><div><span class="lg-k">Batch 2</span><h3>Feedback and inputs, three owners</h3><p>Split across three system designers, each owning a set from skeleton to QA.</p>
    <ul><li>Snackbar</li><li>Info strip</li><li>Divider</li><li>File upload</li><li>Header</li><li>Loader</li><li>OTP input</li><li>Page control</li><li>Progress</li><li>Rating</li><li>Slider</li><li>Tooltip</li><li>Tab bar</li><li>Search</li><li>Tags</li></ul></div></article>
  <article class="lg-batch"><figure>{kimg("stepper", "Progress stepper, batch 3")}</figure><div><span class="lg-k">Batch 3</span><h3>The rest, and what teams asked for</h3><p>Navigation and overlays, plus components teams requested during the first two batches.</p>
    <ul><li>App bar</li><li>Bottom sheet</li><li>Steppers</li><li>Avatar</li><li>Phone input</li><li>Car registration input</li><li>Stack button</li></ul></div></article>
</div>'''

# ---------------------------------------------------------------- 07 composability
cells = "".join("<i></i>" for _ in range(448))
vs = f'''<div class="lg-vs">
  <div class="was"><span class="lg-k">One variant for every case</span><strong>448</strong><p>2 labels × 2 info icons × 2 leading icons × 2 trailing icons × 2 buttons × 2 helper texts × 7 states. Every one drawn, named and kept in sync, and still missing the case a team needs next.</p><div class="lg-grid448" aria-hidden="true">{cells}</div></div>
  <div class="now"><span class="lg-k" style="color:#667085">LEGO: one component with slots</span><strong style="color:#4736fe">1</strong><p style="opacity:1;color:#475467">One text input. Designers switch slots on and off and pick a state. Nothing gets detached, so a fix to the input reaches every screen.</p>
    <div class="lg-slots"><span>label</span><span>optional</span><span>info</span><span>leading icon</span><span>trailing icon</span><span>attached button</span><span>helper text</span></div>
    <div class="lg-slots"><span class="st">rest</span><span class="st">filled</span><span class="st">read-only</span><span class="st">focus</span><span class="st">disabled</span><span class="st">error</span><span class="st">error + filled</span></div></div>
</div>'''

anat = f'''<div class="lg-anat"><div style="position:relative">
  {kimg("input", "The LEGO text input, with its slots")}
  <span class="tag" style="left:0;top:-42px">_Base Input Label ↓</span>
  <span class="tag v" style="left:40%;top:-42px">info · optional · required ↓</span>
  <span class="tag" style="right:calc(100% + 12px);top:44%">.iconplaceholder →</span>
  <span class="tag v" style="left:calc(100% + 12px);top:44%">← .Text container</span>
  <span class="tag" style="left:0;top:calc(100% + 14px)">↑ _Base Input Helper Text</span>
</div></div>'''

products = '<div class="lg-bento">' + tile("phone", "Phone input", 4, h=560, mh=500) + tile("reg", "Car registration input", 4, h=560, mh=500) + tile("otp", "Verification code", 4, h=560, mh=420) + tile("header", "Search, in the app header", 12, dark=False, mh=260) + "</div>"

# ---------------------------------------------------------------- 08 library bento
kit = ('<div class="lg-bento">'
       + tile("button", "Actions · Button", 7, mh=520) + tile("chips", "Selection · Choice chips", 5, mh=340)
       + tile("toast", "Feedback · Toast", 5, mh=200) + tile("inline", "Feedback · Inline alert", 7, mh=360)
       + tile("tabs-dark", "Navigation · Tabs, dark", 4, dark=True, mh=380) + tile("segment", "Selection · Segment control", 8, mh=380)
       + tile("switch", "Selection · Switch", 6, mh=360) + tile("avatar", "Display · Avatar", 3, mh=360) + tile("badge", "Display · Badge", 3, mh=320)
       + tile("stepper", "Navigation · Stepper", 8, mh=220) + tile("rating", "Selection · Rating", 4, mh=220)
       + tile("snackbar", "Feedback · Snackbar", 6, mh=420) + tile("checkbox", "Selection · Checkbox", 3, mh=420) + tile("tooltip", "Feedback · Tooltip", 3, mh=420)
       + "</div>")

fams = [("Actions", ["Button", "Pill button", "Icon button", "Link button", "Social button", "Button group", "Stack button", "Caption button", "Search button"]),
        ("Inputs", ["Text input", "Number input", "Phone input", "Car registration input", "Verification input", "OTP generate", "File upload", "Slider"]),
        ("Selection", ["Checkbox", "Radio button", "Switch", "Choice chips", "Segment control", "Rating"]),
        ("Feedback", ["Global alert", "System alert", "Inline alert", "Toast", "Snackbar", "Tooltip", "Loader", "Circular loader", "Loader dots"]),
        ("Navigation", ["Tab", "Breadcrumb", "Bottom bar", "App header", "Home header", "Stepper, horizontal", "Stepper, vertical"]),
        ("Display", ["Badge", "Tag", "Avatar", "Divider", "Accordion"])]

# ---------------------------------------------------------------- 09 QA
qa = f'''<div class="lg-qa">
  <div class="lg-states"><ol><li>rest</li><li>filled</li><li>read-only</li><li>focus</li><li>disabled</li><li>error</li><li>error + filled</li></ol>{kimg("input-states", "The text input in all seven states")}</div>
  <div class="lg-model">
    <div class="lg-code"><span class="lg-k" style="color:#9aa0aa">From the state modelling guideline</span><br><span class="x">state = "hoverErrorDisabled"</span><br><b>interaction</b> rest | hover | active | focus<br><b>disabled</b> true | false<br><b>readonly</b> true | false<br><b>validation</b> none | error | success<br><span class="ok">Same names in Figma and in code.</span></div>
    <ol class="lg-steps"><li>Find the skeleton in the live product</li><li>Define the properties</li><li>Define the variants</li><li>Write the basic docs</li><li>Run the QA checklist</li><li>Record the result, file the bugs</li></ol>
    <figure class="sc-fig lg-sheet" style="margin:0">{kimg("states-guide", "State modelling guidelines in Figma")}</figure>
  </div>
</div>'''

# ---------------------------------------------------------------- 11 shipped
homes = ('<div class="lg-phones" style="--n:4">' + phone("sell", "Sell", "#2e6b4a") + phone("carcheck", "Car check", "#7a2e12")
         + phone("loans", "Loans", "#1f5fe0") + phone("explore", "Explore", "#4736fe") + "</div>")
pages = ('<div class="lg-phones" style="--n:5">' + phone("buy", "Buy", scroll=True, y="-80%", t=30) + phone("home", "Home", scroll=True, y="-62%", t=26)
         + phone("sell", "Sell", scroll=True, y="-72%", t=28) + phone("carcheck-b", "Car check", scroll=True, y="-70%", t=28) + phone("loans-b", "Loans", scroll=True, y="-70%", t=28) + "</div>")
search = ('<div class="lg-pair">' + phone("search-old", "<b>Before</b>&nbsp;· search on the old parts") + phone("search-new", "<b>With LEGO</b>&nbsp;· the same search, composed") + "</div>")

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
    section("type", "Typography", "<b>04</b> typography:", "A type scale named by its numbers",
            "Fonts were tested on the busiest pages first: listings and product pages full of prices, EMIs, kilometres and badges.",
            wrap(typespec + gap(32)
                 + story(prose(
                     "Candidate fonts were set into real pages from the apps: listings and product pages first, then light landing pages and marketing banners. The team checked how each font handled numbers and prices, how it sat next to Arabic, and how many lines a listing card took at each size.",
                     "The scale that came out of it is short, and every token says what it is. Designers and engineers read the same name and know the size without opening a spec.")))),
    section("before", "Before and after", "<b>05</b> on real screens:", "Same page. New parts.",
            "Every decision was checked against the live homepage, so we could see what users would actually get. Drag to compare.",
            wrap(compare((L + "ba-before.webp", "The CARS24 homepage before LEGO, app and mobile web"), (L + "ba-after.webp", "The CARS24 homepage rebuilt on LEGO, app and mobile web"),
                         ("Before", "With LEGO"), "App on the left, mobile web on the right.", ratio="21 / 20")
                 + gap(24) + board("baweb", "The old mobile web homepage and what was wrong with it, next to web and app rebuilt on LEGO.")), mode="stage"),
    section("pick", "What to build first", "<b>06</b> what to build first:", "Not the button",
            "Three teams, redesigns already planned, and a small system team. What we built first would decide whether anyone used LEGO.",
            wrap(story(prose(
                     "### The challenge",
                     "The obvious first step is the button, then type, colour and the other basics. But no product team needs another team to give them a button, and every team already had one. A system that starts there spends months on parts nobody is waiting for, while the teams redesign their pages with their own components.",
                     "### The approach",
                     "We treated LEGO like a product with customers. Instead of asking what a complete design system should contain, we asked who we could help next, and with what. The product teams were in it from the start: their roadmaps set the order, their screens showed us the components, and their best versions became our starting point."))
                 + gap(32) + rail([("Collect roadmaps", "What each country planned to ship next quarter"),
                                   ("Walk through products", "Product and design leads showed us their screens and drafts"),
                                   ("Inventory", "Every component we saw, by team: 26 on the first list"),
                                   ("Pick the hard, shared ones", "Most teams, on the roadmap, hardest to get right"),
                                   ("Harvest", "Start from the best version a team already built"),
                                   ("Ship with the team", "Test it in their screens, then install it together")])
                 + gap(40) + board("pick", "The planning board, recreated: components spotted in each team's walkthrough, the first list of 26, and the first batch of 12.")
                 + gap(32) + why + '<p class="sc-note">Reasons summarised from the walkthroughs and the audit.</p>'
                 + gap(32) + batches)),
    section("compose", "Composability", "<b>07</b> built to be composed:", "One component with slots, not a variant for every case",
            "Every team needs its own version of an input. Drawing each one as a variant doesn't scale. Slots do.",
            wrap(vs + gap(16) + anat
                 + '<p class="sc-note" style="color:inherit">Five private atoms sit inside the input. Designers never place them directly; they switch the slots.</p>'
                 + gap(32) + products
                 + gap(48) + '<p class="lg-k" style="margin-bottom:16px">Search: before and after</p>' + search
                 + gap(24) + '<p class="sc-note" style="color:inherit;text-align:center">The new search is made of LEGO parts: the header, the text input, choice chips for recent and trending searches, icon buttons and cards. Compositions like this became the <a href="cars24-pattern-library.html" style="color:inherit">pattern library</a>.</p>'), mode="stage"),
    section("library", "Library", "<b>08</b> the library:", "44 components in six families", "Every sheet carries its states, sizes, usage notes and the date it last changed.",
            wrap(kit + gap(24) + inventory("44", "components, each built from shared atoms", fams))),
    section("qa", "QA", "<b>09</b> definition of done:", "One prop per concern",
            "Every state is its own property, named the same in Figma and in code, and every component was QA'd before release.",
            wrap(qa + gap(24)
                 + story(prose(
                     "The guideline set one rule: never merge states into one property like hoverErrorDisabled. Interaction, disabled, read-only and validation are separate props. That keeps the number of variants small, makes impossible combinations impossible, and gives engineers the same API they see in Figma.",
                     "Every component then went through the same six steps, and nothing shipped until its QA result was written down.")))),
    section("adoption", "Adoption", "<b>10</b> adoption:", "Run like a launch, team by team",
            "A library nobody uses is a museum. Getting LEGO into three products took as much work as building it.",
            wrap(story(prose(
                     "Designers had to change habits, not just files. LEGO's props worked differently from the old kit: states became separate properties, and variations came from slots instead of detaching a component and drawing over it. If teams didn't understand that, they would detach LEGO too, and we'd be back where we started.",
                     "So the rollout was planned as carefully as the components. Each batch shipped with a session that showed what was new. Office hours ran every week. And the system team sat with each country team while they rebuilt their first screens, fixing what broke straight away."))
                 + gap(32)
                 + timeline([("Spring 2025", "Look and feel", "Type, surfaces, shadows, radius and icons tested on real pages, with designers from all three countries reviewing.", "Research"),
                             ("Early summer", "Batch 1 ships", "The 12 components every roadmap was blocked on, each shown to the teams in a walkthrough.", "12 components"),
                             ("Summer", "Batches 2 and 3, with QA", "Split across three system designers; each component QA'd and the result recorded before release.", "44 components"),
                             ("Summer", "Workshops", "How the new props work, how slots compose, and how to make your own version without detaching.", "All three teams"),
                             ("Every week", "Office hours", "Bring a screen, leave with an answer. Questions that kept coming up became usage notes on the sheets.", "Ongoing"),
                             ("From August", "Into the products", "The homepages in India, the UAE and Australia, then buy, sell, listing and product pages.", "Shipped")])
                 + gap(32)
                 + room([("Workshops", "Composability, hands on", "Designers rebuilt one of their own screens from LEGO slots and atoms, in the session."),
                         ("Office hours", "Weekly, open to everyone", "The fastest way to find the gaps. Each repeated question became a note on the component's sheet."),
                         ("Arabic", "A loop with the UAE team", "Right-to-left checks on every component, and help adapting their screens to the new system.")]))),
    section("shipped", "Shipped", "<b>11</b> shipped:", "Every business, its own homepage, the same parts",
            "Sell, car check, loans and explore each got their own homepage. Header, search, tabs, cards and list rows are all LEGO.",
            wrap(homes + gap(56)
                 + '<p class="lg-k" style="margin-bottom:16px">Pages rebuilt on LEGO, top to bottom</p>' + pages
                 + '<p class="sc-scroll-hint">Each phone scrolls through the full page. Select one to see it whole.</p>'), mode="stage"),
    section("impact", "Impact", "<b>12</b> what changed:", "From an old kit to one system in three countries", "",
            wrap(outcomes([("Reach", "3 countries", "The homepages for India, the UAE and Australia moved to LEGO."),
                           ("Pages", "Core flows", "Buy, sell, listing cards and product pages, redesigned on the new system."),
                           ("Library", "44 components", "Built from five shared atoms, with slots instead of endless variants."),
                           ("Teams", "Adopted, not imposed", "Built in the order the teams' own roadmaps needed it.")])
                 + gap(16) + lessons(["Don't start with the button. Start with the component the next roadmap is blocked on.",
                                      "Test the look and feel on real pages before drawing a single component.",
                                      "Composable slots beat a variant for every case, and let teams make their own versions."]))),
    section("playbook", "For your team", "<b>13</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "Roadmap and product walkthroughs, an audit of your live screens, and a list of what to build first, with the reasons.",
                           "foundations": "Look-and-feel tests on your real pages, then the first batch of composable components.",
                           "partner": "Next batches, QA, office hours and workshops, team by team, until it's in the product."}, employer="CARS24"))),
]

page("cars24-lego", dict(
    h1="LEGO: the component system after the rebrand",
    lede="How CARS24 tested a new look and feel on real screens, picked its first components from teams' roadmaps, and got 44 composable parts adopted in three countries.",
    meta=[("Role", "Design Systems Lead, CARS24"), ("Markets", "India, UAE, Australia"), ("Platforms", "Android, iOS, mobile web"), ("Timeline", "2025")],
    proof=[("", "44", "", "components in six families"), ("", "26", "", "on the first, roadmap-led list"), ("", "3", "", "countries' apps rebuilt on it"), ("", "3", "", "build batches, in roadmap order")],
    hero=L + "b-hero.webp",
    cover_alt="Three CARS24 app screens built with LEGO (sell, home and loans) on brand blue, with component pieces floating around them",
    sections=S,
    credits="Aniket Pandey led this as Design Systems Lead at CARS24 (2025), with the CARS24 system designers and the product design teams in India, the UAE and Australia. This is employee work, not Layer One client work. Screens and component sheets belong to CARS24 and are shown for portfolio purposes. The sketch boards are annotated for this page; the planning board is a recreation and its tallies are illustrative.",
))
