"""CARS24: LEGO, the component system built after the rebrand. Showcase engine (see showcase.py).

Sources: the founder's working Figma file "Cars24_Design_system_2025" (component sheets, look-and-feel tests,
planning boards, landing pages built with the new system) and the founder's own account of the project.
Interactive modules are rebuilt in HTML from the library's values; styles live under "LEGO case study" in site.css.
"""
from showcase import *
from cs import compare

L = "assets/work/cars24-lego/"

# ---------------------------------------------------------------- 03 · look-and-feel lab
lab = '''<div class="lg-lab" data-lglab>
  <div class="lg-lab-ctl">
    <div><p>Surface</p>''' + seg("data-k=surface", [("stroke", "Stroke"), ("fill", "Fill"), ("none", "None")], "Surface") + '''</div>
    <div><p>Shadow</p>''' + seg("data-k=shadow", [("none", "None"), ("xs", "xs"), ("sm", "sm"), ("lg", "lg")], "Shadow") + '''</div>
    <div><p>Radius</p>''' + seg("data-k=radius", [("4", "4"), ("8", "8"), ("12", "12"), ("20", "20")], "Radius") + '''</div>
    <div><p>Body size</p>''' + seg("data-k=type", [("130", "13"), ("150", "15"), ("170", "17")], "Body size") + '''</div>
    <button type="button" class="pill pill--accent" data-lgreset>Where LEGO landed</button>
    <p class="lg-lab-why" aria-live="polite"></p>
  </div>
  <div class="lg-lab-stage">
    <div class="lg-phone" data-surface="stroke" data-shadow="none" data-radius="12" data-type="150">
      <div class="lg-ph-top"><span class="lg-ph-loc">Gurugram ▾</span><span class="lg-ph-av">W</span></div>
      <div class="lg-ph-search">Search for cars, loans, checks</div>
      <p class="lg-ph-h">Buy vehicle</p>
      <div class="lg-ph-cards"><div class="lg-c"><b>Used car</b><small>From ₹2.1 lakh</small></div><div class="lg-c"><b>New car</b><small>40+ brands</small></div><div class="lg-c"><b>Bike</b><small>New</small></div></div>
      <div class="lg-ph-list">
        <div class="lg-c lg-row"><span class="lg-ic"></span><div><b>Vehicle history report</b><small>30% of cars have a past accident</small></div><i>›</i></div>
        <div class="lg-c lg-row"><span class="lg-ic"></span><div><b>Odometer fraud check</b><small>Know the real kilometres</small></div><i>›</i></div>
      </div>
      <div class="lg-ph-chips"><span class="on">All</span><span>SUV</span><span>Hatchback</span><span>Sedan</span></div>
      <span class="lg-ph-btn">View 2,340 cars</span>
    </div>
  </div>
</div>
<p class="sc-note">Rebuilt in HTML from the look-and-feel tests. Every combination here was tried on real screens before a single component was drawn.</p>'''

# ---------------------------------------------------------------- 04 · type, three markets
typelab = '''<div class="lg-type" data-lgtype>
  <div class="sc-ctls">''' + seg("data-k=lang", [("en", "English · India"), ("ar", "العربية · UAE"), ("au", "English · Australia")], "Market") + seg("data-k=size", [("130", "13 / 140%"), ("150", "15 / 150%"), ("170", "17 / 130%")], "Body size") + '''</div>
  <div class="lg-type-grid">
    <div class="lg-listing" dir="ltr">
      <div class="lg-l-img" aria-hidden="true"><span data-t="badge"></span></div>
      <p class="lg-l-t" data-t="title"></p>
      <p class="lg-l-m" data-t="meta"></p>
      <div class="lg-l-p"><b data-t="price"></b><span data-t="emi"></span></div>
      <p class="lg-l-n" data-t="note"></p>
    </div>
    <dl class="lg-type-spec">
      <div><dt>Token</dt><dd><code data-o="tok">$lego-font-size-150</code></dd></div>
      <div><dt>Size / line height</dt><dd data-o="lh">15px / 150%</dd></div>
      <div><dt>Lines in the card</dt><dd data-o="lines">–</dd></div>
      <div><dt>What we looked for</dt><dd data-o="why"></dd></div>
    </dl>
  </div>
</div>
<p class="sc-note">The card is rebuilt in HTML. Prices and listings are illustrative; the type tokens are LEGO's own.</p>'''

# ---------------------------------------------------------------- 05 · picking the first components
inventory26 = ["Accordion", "Alert", "Snack bar", "Badge", "Breadcrumbs", "Button", "Chips and filter", "Checkbox", "Radio button", "Divider",
               "Bottom sheet", "File upload", "Header", "Info strip", "Input field", "Loader", "Navigation", "OTP input field", "Page control",
               "Progress indicator", "Rating", "Slider", "Tabs", "Tags", "Tooltip", "App bar"]
batch = {1: ["Checkbox", "Radio button", "Input field", "Accordion", "Breadcrumbs", "Badge", "Tabs", "Chips and filter", "Button", "Alert"],
         2: ["Snack bar", "Info strip", "Divider", "File upload", "Header", "Loader", "OTP input field", "Page control", "Progress indicator", "Slider", "Rating", "Tooltip", "Navigation", "Tags"],
         3: ["App bar", "Bottom sheet"]}
seg_b = seg("data-k=batch", [("all", "All 26"), ("1", "Batch 1"), ("2", "Batch 2"), ("3", "Batch 3")], "Batch")
cells = "".join(f'<li data-b="{next((k for k, v in batch.items() if n in v), 3)}">{n}</li>' for n in inventory26)
planner = f'''<div class="lg-plan" data-lgplan>
  <div class="sc-ctls">{seg_b}<span data-o="note">26 components on the first list, from walkthroughs of every team's roadmap.</span></div>
  <ol class="lg-plan-grid">{cells}</ol>
</div>'''

score_rows = [("Chips and filter", [3, 3, 3, 2], "Every listing, every vertical, three countries"),
              ("Input field", [3, 3, 3, 3], "Sell, loans and checkout all blocked on it"),
              ("Button", [3, 2, 1, 3], "Everywhere, but every team already had one"),
              ("Alert", [2, 3, 2, 2], "Loans and car check needed new states"),
              ("Bottom sheet", [2, 1, 3, 1], "Only two flows on the next roadmap"),
              ("Rating", [1, 1, 1, 2], "One page, one team")]
crit = ["Teams using it", "On next quarter's roadmap", "Hard to get right", "Parts already built"]
srow = "".join(f'''<tr><th scope="row">{n}</th>{"".join(f'<td><i class="lg-h{v}" aria-label="{v} of 3"></i></td>' for v in s)}<td class="sum">{sum(s)}</td><td class="why">{w}</td></tr>''' for n, s, w in score_rows)
scoring = f'''<div class="lg-score"><table><thead><tr><th scope="col">Component</th>{"".join(f'<th scope="col">{c}</th>' for c in crit)}<th scope="col">Score</th><th scope="col">Why</th></tr></thead><tbody>{srow}</tbody></table></div>
<p class="sc-note">The scoring, reconstructed for six of the 26 to show the method. Marks are illustrative, not a record of the original sheet.</p>'''

# ---------------------------------------------------------------- 07 · composability
compose = '''<div class="lg-comp" data-lgcomp>
  <div class="lg-comp-ctl">
    <p>Slots</p>
    <label><input type="checkbox" data-s="label" checked> Label</label>
    <label><input type="checkbox" data-s="optional" checked> “Optional”</label>
    <label><input type="checkbox" data-s="info"> Info icon</label>
    <label><input type="checkbox" data-s="lead" checked> Leading icon</label>
    <label><input type="checkbox" data-s="trail"> Trailing icon</label>
    <label><input type="checkbox" data-s="button"> Attached button</label>
    <label><input type="checkbox" data-s="helper" checked> Helper text</label>
    <p>State</p>''' + seg("data-k=state", [("rest", "Rest"), ("focus", "Focus"), ("error", "Error"), ("disabled", "Disabled")], "State") + '''
  </div>
  <div class="lg-comp-out">
    <div class="lg-comp-stage">
      <div class="lg-field" data-state="rest">
        <p class="lg-f-label"><b>Registration number</b> <span class="opt">(optional)</span> <span class="inf" aria-hidden="true">i</span></p>
        <div class="lg-f-row"><div class="lg-f-box"><span class="lead" aria-hidden="true"></span><span class="val">DL 10 CQ 7291</span><span class="trail" aria-hidden="true">×</span></div><span class="lg-f-btn">Check</span></div>
        <p class="lg-f-help">We'll fetch the car's details from this number</p>
      </div>
    </div>
    <pre class="lg-comp-code" aria-label="Props"><code data-o="code"></code></pre>
    <div class="lg-atoms"><span>Built from</span><b>_Base Input Label</b><b>.iconplaceholder</b><b>.Text container</b><b>_Base Input Helper Text</b></div>
  </div>
</div>'''

layers = '''<div class="lg-layers">
  <div><span class="t">Atoms</span><h3>5 private parts</h3><p>Label, helper text, text container, icon slot, slider bar. Designers never place them directly.</p><ul><li>_Base Input Label</li><li>_Base Input Helper Text</li><li>.Text container</li><li>.iconplaceholder</li><li>_Base Slider Bar</li></ul></div>
  <div><span class="t">Components</span><h3>44 public components</h3><p>Each one assembled from the atoms, with slots that can be turned on and off instead of variants for every case.</p><ul><li>Text input</li><li>Phone input</li><li>Car reg. input</li><li>Choice chips</li><li>Segment control</li><li>Button</li></ul></div>
  <div><span class="t">Compositions</span><h3>Forms, filters, empty states</h3><p>Groups of components teams could copy and change, the first step towards the pattern library.</p><ul><li>Sell-car form</li><li>Listing filter</li><li>No results</li><li>OTP login</li></ul></div>
</div>'''

fams = [("Actions", ["Button", "Pill button", "Icon button", "Link button", "Social button", "Button group", "Stack button", "Caption button", "Search button"]),
        ("Inputs", ["Text input", "Number input", "Phone input", "Car registration input", "Verification input", "OTP generate", "File upload", "Slider"]),
        ("Selection", ["Checkbox", "Radio button", "Switch", "Choice chips", "Segment control", "Rating"]),
        ("Feedback", ["Global alert", "System alert", "Inline alert", "Toast", "Snackbar", "Tooltip", "Loader", "Circular loader", "Loader dots"]),
        ("Navigation", ["Tab", "Breadcrumb", "Bottom bar", "App header", "Home header", "Stepper, horizontal", "Stepper, vertical"]),
        ("Display", ["Badge", "Tag", "Avatar", "Divider", "Accordion"])]

# ---------------------------------------------------------------- 09 · definition of done (QA)
qa = [("Build", ["Skeleton found in the live product first", "Properties defined before variants", "Every colour on a lego- token, every text on a style", "Auto layout resizes with long labels"]),
      ("States", ["Rest, hover, focus, pressed, disabled", "Loading where an action can wait", "Error and helper text for every input", "Focus ring visible on every surface"]),
      ("Markets", ["Long Hindi and English labels truncate cleanly", "Arabic mirrors: icons, arrows, alignment", "Prices in INR, AED and AUD fit the slot", "Tested on the smallest Android in use"]),
      ("Handoff", ["Figma property names match code props", "Usage notes written on the sheet", "QA result recorded, bugs filed", "Shown in office hours before release"])]
qahtml = '<div class="lg-qa" data-lgqa><div class="lg-qa-top"><strong><span data-o="n">0</span> / 16</strong><span>checks, grouped the way the team ran QA. Tick them off.</span><div class="lg-qa-bar"><i></i></div></div><div class="lg-qa-grid">' + "".join(
    f'<fieldset><legend>{g}</legend>{"".join(f"<label><input type=checkbox><span>{t}</span></label>" for t in items)}</fieldset>' for g, items in qa) + "</div></div>" + '<p class="sc-note">The checklist, reconstructed from the QA board for this page. The original lived beside each component sheet.</p>'

# ---------------------------------------------------------------- 11 · themed verticals (phone tabs)
phones = [("sell", "Sell", "#2e6b4a", "Sell car, on the green theme"), ("carcheck-a", "Car check", "#7a2e12", "Car check, on the brown theme"),
          ("loans-a", "Loans", "#1f5fe0", "Loans, on the blue theme"), ("explore", "Explore", "#4736fe", "Explore, on the brand theme")]
ptabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-src="../{L}p-{k}.jpg" data-alt="{a}" style="--sw:{c}"><i></i>{t}</button>' for i, (k, t, c, a) in enumerate(phones))
verticals = f'''<div class="lg-vert" data-lgphones>
  <div class="lg-vert-txt"><div class="sc-screen-tabs" role="tablist" aria-label="Business line">{ptabs}</div>
    <p>One component set. Each business line gets a theme: the header, accents and illustrations change, the components don't.</p>
    <ul class="lg-vert-list"><li><b>Same</b> search, tabs, cards, chips, list rows, buttons</li><li><b>Themed</b> header colour, accent, illustration style</li><li><b>Owned by</b> the business team, inside the rules</li></ul></div>
  <div class="sc-phone"><div class="sc-view" tabindex="0" aria-label="Scrollable screen"><img src="../{L}p-sell.jpg" alt="{phones[0][3]}" loading="lazy" data-lightbox data-cap="{phones[0][3]}"></div></div>
</div>
<p class="sc-scroll-hint">Scroll inside the phone to see the whole page.</p>'''

S = [
    section("context", "Context", "<b>01</b> the context:", "After the rebrand, the interface",
            "The new colours and tokens had shipped. The components underneath were still the old ones.",
            wrap(facts([("3", "countries: India, the UAE and Australia"), ("3", "business teams, run almost like separate companies"), ("10+", "products and verticals on one app"), ("2025", "the year after the rebrand")])
                 + gap(48)
                 + story(prose(
                     "In 2024 CARS24 rebranded. The palette moved to OKLCH, the brand blue changed, and a four-layer token system carried it to every product. That work is its own case study. It changed what the apps looked like, but not how they were built: the buttons, inputs, chips and cards were the same old components, recoloured.",
                     "So the rebrand became a chance to rebuild the interface too. The team started LEGO, a new component system for the mobile apps and mobile web, named for what it had to be: small, solid pieces that teams snap together.",
                     "Aniket led the design system as Design Systems Lead at CARS24, with a small group of system designers and partners from the product design teams in each country."),
                     "The project", [("2025", "CARS24"), ("Role", "Design Systems Lead"), ("Platforms", "Android, iOS, mobile web"), ("Built on", "The 2024 rebrand tokens")])
                 + '<p class="sc-note">Read the first chapter: <a href="cars24-tokens.html">one colour system for 10+ products in three countries</a>.</p>')),
    section("problem", "Problem", "<b>02</b> the problem:", "Three companies inside one company",
            "India, the UAE and Australia each had their own business, product and design teams, and their own roadmaps.",
            wrap(nums([("", "3", "", "teams with their own business goals", "Teams"), ("", "2", "", "scripts, reading in opposite directions", "Language"),
                       ("", "26", "", "components on the first list", "Scope"), ("", "1", "", "redesign of every core page, already planned", "Deadline")])
                 + gap(48)
                 + story(prose(
                     "Each country team solved its own problems with its own components. The same chip existed four times with four paddings. Arabic in the UAE was handled at the end, if at all. And a redesign of the homepage, listing and product pages was already planned for the next few quarters, so whatever the system offered had to be ready before those teams started, or they would build their own again.",
                     "> How might we give three teams with three roadmaps one set of components they would actually choose, before their redesigns began?"),
                     "What made it hard", [("3 teams", "Different goals, one app"), ("EN + AR", "Left to right and right to left"), ("Redesigns", "Already on the roadmap")])
                 + gap(32)
                 + brief([("squads", "Each country team building its own components", "One library all three teams build from"),
                          ("script", "Arabic fixed at the end, screen by screen", "Every component checked in Arabic before release"),
                          ("drift", "A new brand on old components", "A new look and feel, tested before it was drawn")]))),
    section("work", "The work", "<b>03</b> the work, in ten frames:", "Swipe through it", "Component sheets from the LEGO library, each with its states, sizes and usage notes. Select any frame to see it full size.",
            carousel("The LEGO design system, in ten frames", [
                (L + "r-button.jpg", "Button", "Four sizes, six states, primary to tertiary.", {"bg": "#f4f5fb"}),
                (L + "c-chips.jpg", "Choice chips", "The first component the listing teams asked for.", {"bg": "#f4f5fb"}),
                (L + "r-input.jpg", "Text input", "One field, eight optional slots.", {"bg": "#f4f5fb"}),
                (L + "c-global-alert.jpg", "Global alert", "Four intents, written for mobile.", {"bg": "#f4f5fb"}),
                (L + "r-tab.jpg", "Tab", "Light and dark, with icons and counts.", {"bg": "#f4f5fb"}),
                (L + "r-otp.jpg", "Verification input", "OTP, PIN and registration codes.", {"bg": "#f4f5fb"}),
                (L + "r-badge.jpg", "Badge", "Every intent, every size, solid and soft.", {"bg": "#f4f5fb"}),
                (L + "c-segment.jpg", "Segment control", "Two to five options, with icons.", {"bg": "#f4f5fb"}),
                (L + "r-snackbar.jpg", "Snackbar", "Message, action and dismiss.", {"bg": "#f4f5fb"}),
                (L + "r-avatar.jpg", "Avatar", "Initials, images and status, seven sizes.", {"bg": "#f4f5fb"}),
            ])),
    section("research", "Look and feel", "<b>04</b> look and feel, first:", "Test the feel before drawing a component",
            "Shadow or stroke, how soft, which radius, how big the body text. Try the combinations the team tested.",
            wrap(lab + gap(40) + story(prose(
                "Before any component was drawn, the team worked out how LEGO should feel for the next few years. Nothing was too small to test: whether shadows should pop or barely show, what colour a shadow should be, how dark a border stroke could go before it looked like a form, which corner radii were allowed and which were not.",
                "Each option was put on real screens, not on blank artboards: dense listing pages, light marketing pages, banners and forms. A group of product designers from the country teams reviewed them side by side, so the choice was theirs as much as the system team's.",
                "### What came out of it",
                "Strokes for structure, shadows only where something lifts off the page: cards, chips, sheets and snackbars each got a named shadow (card-rest, card-selected, chip-surface-rest, snackbar-shadow-surface) instead of one global scale. A short list of allowed radii. And a body size chosen for dense pages, not for the hero."),
                "Tested", [("Surfaces", "Stroke, shadow, fill"), ("Shadows", "Strength and colour"), ("Radius", "What's allowed, what isn't"), ("Icons", "Scale, stroke, radius")])
                 + gap(32) + bento([
                (L + "t-lookfeel.jpg", "The same components in four looks, on one page", 7, 4, {"fit": "contain", "bg": "#fff"}),
                (L + "t-icons.jpg", "Icon containers: size, fill and state", 5, 4, {"fit": "contain", "bg": "#fff"}),
                (L + "t-surfaces.jpg", "Surface studies: stroke against fill, six ways", 12, 3, {"fit": "cover", "bg": "#fff"}),
                (L + "t-textbuttons.jpg", "Text buttons by weight", 4, 3, {"fit": "contain", "bg": "#fff"}),
                (L + "f-shadows.jpg", "The shadow scale, 2xs to 2xl", 4, 3, {"fit": "cover", "pos": "left center", "bg": "#fff"}),
                (L + "f-elevation.jpg", "Elevation tokens: base and modifiers", 4, 3, {"fit": "contain", "bg": "#fff"}),
            ])), mode="paper"),
    section("type", "Typography", "<b>05</b> typography:", "Type that holds a dense listing, in three markets",
            "Fonts were tested on the heaviest pages first. Switch the market and the body size.",
            wrap(typelab + gap(32) + story(prose(
                "CARS24 pages carry a lot: price, EMI, kilometres, fuel, owners, inspection badges, offers. The type had to keep all of that readable on a small Android phone, in English for India and Australia and in Arabic for the UAE.",
                "Candidate fonts were set into real pages across the apps: content-heavy listings, light landing pages and marketing banners. The team checked how each one handled numbers and prices, how it paired with Arabic, and how many lines a listing card took at each size.",
                "The result was a short scale named by its numbers. In $lego-font-size-150 the 150 means 15px, and every size carries its own line height: 13px at 140%, 15px at 150%, 17px at 130%. Small text gets more room; large text gets less."),
                "The scale", [("$lego-font-size-130", "13px, 140%"), ("$lego-font-size-150", "15px, 150%"), ("$lego-font-size-170", "17px, 130%"), ("Weights", "Regular, medium, semibold, bold")])
                 )),
    section("realscreens", "Real screens", "<b>06</b> on real screens:", "Same page, before and after",
            "Every foundation decision was checked on live pages. Drag to compare the homepage as it was with the homepage on LEGO.",
            wrap(compare((L + "ba-before.jpg", "The CARS24 homepage before LEGO, app and mobile web"), (L + "ba-after.jpg", "The CARS24 homepage rebuilt on LEGO, app and mobile web"),
                         ("Live, before", "Built with LEGO"), "App on the left, mobile web on the right. Drag the handle.", ratio="21 / 20")
                 + gap(24) + bigfig(L + "t-search.jpg", "Search, redesigned on LEGO: services and cars in one result list, with empty states", bg="#1fa01f", pad="0")), mode="stage"),
    section("pick", "What to build first", "<b>07</b> what to build first:", "Start with what teams need next",
            "Not the button. The components on the next quarter's roadmaps, used by the most teams, and hardest to get right.",
            wrap(rail([("Collect roadmaps", "What each country team planned to ship next quarter"),
                       ("Walk through products", "Screens and drafts, every component noted"),
                       ("Inventory", "26 components, mapped across teams"),
                       ("Score and batch", "Most used, most needed, hardest first"),
                       ("Harvest", "Start from the best version a team already built")])
                 + gap(40) + planner + gap(24) + scoring + gap(32)
                 + story(prose(
                     "The order followed a simple rule from design system practice: begin with the end in mind, and take the first step where it helps someone now. The team collected each country's roadmap, sat through product walkthroughs, and wrote down every component they saw. Components that showed up in many teams and on the next quarter's plans went first.",
                     "That put the hard ones early: inputs, chips and filters, alerts. Building those first earned the system credibility with teams who had no use for another button.",
                     "Before drawing anything, the team looked for the best version a country team had already built and started from it. Product designers kept designing products; the system team did the merging."),
                     "Batches", [("Batch 1", "12 components: every form and listing needed them"), ("Batch 2", "Split across three system designers"), ("Batch 3", "The rest, plus what teams asked for on the way"), ("Next", "Compositions and patterns")]))),
    section("compose", "Composability", "<b>08</b> built to be composed:", "Slots, not a variant for every case",
            "Turn the slots on and off. The same input becomes a registration field, a phone field or a search box.",
            wrap(compose + gap(32) + layers
                 + '<p class="sc-note">Compositions grew into the next chapter: <a href="cars24-pattern-library.html">a pattern library that builds pages from tested blocks</a>.</p>'), mode="stage"),
    section("library", "Library", "<b>09</b> the library:", "44 components in six families", "Every sheet carries its states, sizes, usage notes and the date it last changed.",
            wrap(inventory("44", "components, each built from shared atoms", fams) + gap(20) + bento([
                (L + "c-button.jpg", "Button", 4, 6, {"fit": "cover", "bg": "#fff"}),
                (L + "c-input.jpg", "Text input", 4, 6, {"fit": "cover", "bg": "#fff"}),
                (L + "c-stepper-v.jpg", "Progress stepper, vertical", 4, 6, {"fit": "cover", "bg": "#fff"}),
                (L + "c-inline-alert.jpg", "Inline alerts", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-toast.jpg", "Toast", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-switch.jpg", "Switch", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-checkbox.jpg", "Checkbox", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-header.jpg", "App header", 6, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-file-upload.jpg", "File upload", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-tooltip.jpg", "Tooltip", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-phone-input.jpg", "Phone input", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-reg-input.jpg", "Car registration input", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-link.jpg", "Link button", 6, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-rating.jpg", "Rating", 3, 4, {"fit": "cover", "bg": "#fff"}),
                (L + "c-loader.jpg", "Loader", 3, 4, {"fit": "cover", "bg": "#fff"}),
            ])), mode="paper"),
    section("qa", "QA", "<b>10</b> definition of done:", "A checklist before anything shipped",
            "Every component was QA'd against a checklist, and every result was written down.",
            wrap(qahtml + gap(24) + bigfig(L + "f-states.jpg", "State modelling guidelines: every state is a separate prop (interaction, disabled, read-only, validation), named the same in Figma and in code", bg="#fff", pad="0"))),
    section("adoption", "Adoption", "<b>11</b> adoption:", "Office hours, workshops, then three apps",
            "A library nobody uses is a museum. The rollout was run like a launch, team by team.",
            wrap(timeline([("Spring 2025", "Look and feel", "Typography, surfaces, shadows, radius and icons tested on real pages with designers from each country.", "Research"),
                           ("Early summer", "Batch 1", "Inputs, chips, alerts, tabs and buttons: what every team's roadmap needed first.", "12 components"),
                           ("Summer", "Batches 2 and 3, and QA", "Split across three system designers, each component QA'd against the checklist before release.", "44 components"),
                           ("Summer", "Workshops and office hours", "How the new props work, how slots compose, and how to build your own variation without forking.", "All three teams"),
                           ("From August", "Into the products", "The homepages for India, the UAE and Australia, then buy, sell, listing and product pages, rebuilt on LEGO.", "Shipped")])
                 + gap(32)
                 + room([("Workshops", "How composability works", "Hands-on sessions where designers rebuilt their own screens from LEGO slots and atoms."),
                         ("Office hours", "Weekly, open to everyone", "Bring a screen, leave with an answer. Questions that repeated became usage notes on the sheet."),
                         ("Arabic", "A loop with the UAE team", "Right-to-left checks on every component, and help adapting their screens to the new language.")]))),
    section("shipped", "Shipped", "<b>12</b> shipped:", "Every business line, one set of components",
            "Buy, sell, loans and car check rebuilt on LEGO, each on its own theme.",
            wrap(verticals), mode="stage"),
    section("impact", "Impact", "<b>13</b> what changed:", "From an old kit to one system in three countries", "",
            wrap(outcomes([("Reach", "3 countries", "The homepages for India, the UAE and Australia moved to LEGO."),
                           ("Pages", "Core flows", "Buy, sell, listing cards and product detail pages, redesigned on the new system."),
                           ("Library", "44 components", "Built from five shared atoms, with slots instead of endless variants."),
                           ("Teams", "Adopted, not imposed", "Built in the order the teams' own roadmaps needed it.")])
                 + gap(16) + lessons(["Don't start with the button. Start with the component the next roadmap is blocked on.",
                                      "Test the feel on real pages before drawing a single component.",
                                      "Composable slots beat a variant for every case, and let teams make their own variations."]))),
    section("playbook", "For your team", "<b>14</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "Roadmap and product walkthroughs, a component inventory, and a scored list of what to build first.",
                           "foundations": "Look-and-feel tests on your real screens, then the first batch of composable components.",
                           "partner": "Next batches, QA, office hours and workshops, team by team, until it's in the product."}, employer="CARS24"))),
]

page("cars24-lego", dict(
    h1="LEGO: the component system after the rebrand",
    lede="Look and feel tested on real screens, the first components picked from teams' roadmaps, and 44 composable pieces adopted in three countries.",
    meta=[("Role", "Design Systems Lead, CARS24"), ("Markets", "India, UAE, Australia"), ("Platforms", "Android, iOS, mobile web"), ("Timeline", "2025")],
    proof=[("", "44", "", "components in six families"), ("", "26", "", "on the first, roadmap-led list"), ("", "3", "", "countries' apps rebuilt on it"), ("", "3", "", "build batches, in roadmap order")],
    cover_alt="The CARS24 design systems 2025 cover: pixel type reading design systems on brand blue, with wireframe components around it",
    sections=S,
    credits="Aniket Pandey led this as Design Systems Lead at CARS24 (2025), with the CARS24 system designers and the product design teams in India, the UAE and Australia. This is employee work, not Layer One client work. Images belong to CARS24 and are shown for portfolio purposes; some planning views and figures are reconstructions and are labelled as such.",
))
