from showcase import *

R = "assets/work/ibm-riyadh-air/"

# ---------------------------------------------------------------- live specimen (light/dark × EN/AR)
specimen = '''<div class="sc-ctls">''' + seg("data-rx-theme", [("light", "Light"), ("dark", "Dark")], "Theme") + seg("data-rx-lang", [("en", "English"), ("ar", "العربية")], "Language") + '''<span>Every component shipped in all four versions.</span></div>
<div class="rx" data-rx data-theme="light">
  <div class="rx-grid">
    <div class="rx-card">
      <p class="rx-k">Route headline · Segmented button</p>
      <div class="rx-route"><div><b>RUH</b><small data-t="ruh">Riyadh</small></div><span class="ln" aria-hidden="true"></span><div style="text-align:end"><b>LHR</b><small data-t="lhr">London</small></div></div>
      <p class="rx-meta" data-t="meta"></p>
      <div class="rx-seg" data-cabin role="group" aria-label="Cabin"><button type="button" data-v="eco" aria-pressed="true" data-t="eco"></button><button type="button" data-v="prem" aria-pressed="false" data-t="prem"></button><button type="button" data-v="bus" aria-pressed="false" data-t="bus"></button></div>
      <div class="rx-badges"><span class="rx-b fomo" data-t="left"></span><span class="rx-b star">5.0</span><span class="rx-b" data-t="liked"></span></div>
      <div class="rx-row"><div><p class="rx-meta" data-t="from"></p><p class="rx-price" data-price></p></div><button type="button" class="rx-btn" data-book><span></span></button></div>
    </div>
    <div class="rx-card">
      <p class="rx-k">Counter · Seat selector · REX</p>
      <div class="rx-row"><span data-t="guests"></span><div class="rx-ctr"><button type="button" data-dec aria-label="Fewer guests">−</button><output data-n>1</output><button type="button" data-inc aria-label="More guests">+</button></div></div>
      <div class="rx-seats" role="group" aria-label="Row 10"><button type="button" data-s="A" aria-pressed="true">A</button><button type="button" data-s="B" aria-pressed="false">B</button><button type="button" data-s="C" disabled aria-label="C, taken">C</button><span></span><button type="button" data-s="D" aria-pressed="false">D</button><button type="button" data-s="E" disabled aria-label="E, taken">E</button><button type="button" data-s="F" aria-pressed="false">F</button></div>
      <p class="rx-meta" data-seatout aria-live="polite"></p>
      <div class="rx-rex"><span class="sp" aria-hidden="true">✦</span><div><p class="rx-k" data-t="rexK"></p><p data-t="rex"></p></div></div>
      <div class="rx-badges"><span class="rx-b" data-t="dist"></span></div>
    </div>
  </div>
</div>
<p class="sc-note">Rebuilt in HTML from the library sheets, with its colours, shapes and states. Fares are illustrative.</p>'''

fams = [("Badges", ["Avatar", "Main badge", "Round badge", "Rating badge", "FOMO social badge", "Location badge"]),
        ("Branding", ["Brand logo", "Canopy Twist uniform", "Canopy Twist dynamic"]),
        ("Buttons", ["Main button", "Segmented button", "Loader button", "Modal button set", "Menu item button", "Zoom button", "Counter", "Double button", "REX button", "Sticky button", "Swipe button"]),
        ("Chat", ["Speech bubble", "Message input bar", "Live voice input"]),
        ("Editorial", ["Accordion", "Tooltip", "Table line", "Bullet point list", "Price", "Route headline"]),
        ("Controls", ["Slider", "Level controller", "Player controller", "Chip", "Seat selector", "Rating stars", "Toggle"]),
        ("Forms", ["Checkbox", "Date selector", "Phone number field", "Radio button", "Security input code", "Price range indicator", "Text area", "Text field", "Destination search", "Prefilled selectors"]),
        ("Lists", ["List item", "Avatar list item", "List", "Dropdown"]),
        ("Loaders", ["Progress bar", "Loader circle", "Loader dots"]),
        ("Nudges", ["Live update", "Nudge message", "Live message bar", "General message"]),
        ("Navigation", ["Breadcrumbs", "Top bar", "Tab item", "Banner carousel", "Tab selector"]),
        ("Tiles", ["Main tile", "Image and text tile", "Progress tile", "Action tile"]),
        ("Structural", ["Progress segment", "Progress indicator", "Divider", "Carousel dots", "QR code"])]
fams = [(f"G{i + 1:02d} · {n}", c) for i, (n, c) in enumerate(fams)]

palette = '''<div class="sc-pal">
  <div style="--c:#240852"><span>Dark theme surface</span><div><b>Indigo</b><br><code>#240852</code></div></div>
  <div style="--c:#6a67e1"><span>Actions, badges</span><div><b>Violet</b><br><code>#6A67E1</code></div></div>
  <div style="--c:#dad8fc;--t:#240852"><span>Brand moments</span><div><b>Lavender</b><br><code>#DAD8FC</code></div></div>
  <div style="--c:#fbd8d6;--t:#240852"><span>Brand moments</span><div><b>Sunset peach</b><br><code>#FBD8D6</code></div></div>
  <div style="--c:#f6f7fc;--t:#240852"><span>Light theme surface</span><div><b>Mist</b><br><code>#F6F7FC</code></div></div>
</div>
<div class="sc-pal-status"><div style="--c:#328936"><i></i>Success</div><div style="--c:#ffcd36"><i></i>Warning</div><div style="--c:#f63b42"><i></i>Error</div><div style="--c:#9c9fff"><i></i>Highlight</div><div style="--c:#9747ff"><i></i>Social proof</div></div>'''

canopy = '''<div class="sc-canopy" data-canopy><svg viewBox="0 0 600 300" role="img" aria-label="The Canopy Twist line art, redrawn live"><defs><linearGradient id="cnG" x1="0" x2="1"><stop offset="0" stop-color="#FBD8D6"/><stop offset=".5" stop-color="#DAD8FC"/><stop offset="1" stop-color="#6A67E1"/></linearGradient></defs></svg><span>Canopy Twist · G02/B03 · move across it to twist</span></div>'''

bp = '''<div class="sc-bp" data-bp><div class="sc-bp-list" role="tablist" aria-label="Breakpoints"></div>
  <div><div class="sc-bp-stage"><div class="sc-bp-dev"><div class="sc-bp-cols"></div></div></div><dl class="sc-bp-spec"></dl></div></div>'''

scripts = '''<div data-scripts><div class="sc-ctls">''' + seg("", [("en", "English"), ("ar", "العربية"), ("ja", "日本語"), ("th", "ไทย")], "Script") + '''</div>
  <div class="sc-type"><div class="row"><span>XX Large</span><p class="xxl" data-f="h"></p></div><div class="row"><span>Large</span><p class="l" data-f="l"></p></div>
  <div class="row"><span>Body</span><p class="b" data-f="b"></p></div><div class="row"><span>Family</span><p class="s" data-f="s"></p></div></div></div>'''

stress = '''<div class="sc-stress" data-stress>
  <div class="sc-stress-ctl">
    <div><p class="small" style="opacity:.7;margin-bottom:8px">Language</p>''' + seg("data-sl", [("en", "English"), ("ar", "العربية"), ("de", "Deutsch"), ("ja", "日本語")], "Language") + '''</div>
    <div><p class="small" style="opacity:.7;margin-bottom:8px">Currency</p>''' + seg("data-sc", [("SAR", "SAR"), ("INR", "INR"), ("IDR", "IDR"), ("JPY", "JPY"), ("KWD", "KWD")], "Currency") + '''</div>
    <p class="why" aria-live="polite"></p>
  </div>
  <div class="sx-card"><p class="h"></p><p class="sub"></p><div class="tot"><span class="pk"></span><span class="amt"></span></div><div class="cta"></div></div>
</div>'''

S = [
    section("client", "Client", "<b>01</b> the client:", "An airline with no past to inherit",
            "Riyadh Air is Saudi Arabia's new national carrier, founded by the Public Investment Fund and built digital-first.",
            wrap(facts([("2023", "founded, with IBM named lead digital partner"), ("100+", "destinations planned by 2030"), ("787-9", "a new Boeing Dreamliner fleet"), ("Oct 2025", "first flight, Riyadh to London Heathrow")])
                 + gap(48)
                 + story(prose(
                     "Most airlines carry decades of booking engines, loyalty platforms and check-in kiosks. Riyadh Air started with none of it. Every screen a guest would touch, from booking to boarding, had to be designed and built for the first time, while the airline itself was being stood up.",
                     "IBM was the lead digital partner. Its design team proposed the design system and built it with Publicis Sapient, and IBM engineers turned it into code. Riyadh Air's product owners, brand and engineering teams reviewed and signed off. Aniket worked on the system as a design system designer at IBM."),
                     "The engagement", [("2023–24", "IBM for Riyadh Air"), ("3 companies", "IBM, Publicis Sapient, Riyadh Air"), ("Role", "Design system designer, IBM")])
                 + gap(32)
                 + room([("Client", "Riyadh Air", "Product owners, brand and engineering, standing up an airline and its digital estate together."),
                         ("Lead digital partner", "IBM", "The design team proposed the system and built it. IBM engineers built the components in code."),
                         ("Agency", "Publicis Sapient", "Our partner on the design system, shaping and reviewing the library with us.")]))),
    section("problem", "Problem", "<b>02</b> the problem:", "Many apps, many teams, one launch date",
            "Booking, check-in, loyalty and the trip itself, across web, phone and watch, all designed at once.",
            wrap(nums([("", "8", "+", "web and mobile apps, designed at once", "Scale"), ("", "2", "", "scripts, reading in opposite directions", "Language"),
                       ("", "6", "", "breakpoints, from a watch to a wide desktop", "Devices"), ("", "1", "", "launch date that couldn't move", "Deadline")])
                 + gap(48)
                 + story(prose(
                     "Five to six web apps and two to three mobile apps were being designed in parallel, each with its own team. Left alone, every app would drift into its own version of the brand, and every team would rebuild the same button under a deadline set by the first flights.",
                     "Two things made it harder. Every screen had to work in English and Arabic, which read in opposite directions and need different line heights. And the brand was brand new: a lavender identity made for liveries and billboards, with nothing yet that could carry a seat map, a price or an error message.",
                     "> How might we give every team, on every device and in both languages, one way to build Riyadh Air, before there was a Riyadh Air to copy?"),
                     "What made it hard", [("8+ apps", "In parallel, one deadline"), ("EN + AR", "Left to right and right to left"), ("New brand", "Not yet a UI language")])
                 + gap(32)
                 + brief([("squads", "Every app team designing its own interface", "One library every team builds from"),
                          ("script", "Arabic as a translation pass at the end", "Every component drawn in English and Arabic"),
                          ("plane", "A lavender brand made for liveries and billboards", "A brand that can carry a seat map and an error")]))),
    section("work", "The work", "<b>03</b> the work, in twelve frames:", "Swipe through it", "Foundations, components and brand, as the library shows them. Select any frame to see it full size.",
            carousel("The Riyadh Air design system, in twelve frames", [
                (R + "f-colour.jpg", "Colour", "From a lavender brand to product UI.", {"bg": "#f6f7fc"}),
                (R + "btn-rex.jpg", "REX button", "The AI assist, in English and Arabic, light and dark.", {"bg": "#240852"}),
                (R + "f-type.jpg", "Typography", "Two scripts, one scale.", {"bg": "#f6f7fc"}),
                (R + "btn-counter.jpg", "Counter", "Mirrored for right to left.", {"bg": "#240852"}),
                (R + "f-grid.jpg", "Grids", "Six breakpoints, from wrist to wide screen.", {"bg": "#f6f7fc"}),
                (R + "avatar.jpg", "Avatar", "Five sizes, four statuses, aircraft included.", {"bg": "#240852"}),
                (R + "f-icons.jpg", "Iconography", "Material Symbols, used everywhere.", {"bg": "#f6f7fc"}),
                (R + "btn-swipe.jpg", "Swipe button", "Idle, confirmed and loading.", {"bg": "#240852"}),
                (R + "f-space.jpg", "Increments", "Thirteen steps of space, 1 to 64px.", {"bg": "#f6f7fc"}),
                (R + "logo.jpg", "Brand logo", "English-first and Arabic-first lockups.", {"bg": "#240852"}),
                (R + "f-effects.jpg", "Effects", "Four shadows and two blurs, each with a job.", {"bg": "#f6f7fc"}),
                (R + "canopy-dynamic.jpg", "Canopy Twist", "The brand's line art, as a component.", {"bg": "#240852"}),
            ])),
    section("pilot", "Pilot", "<b>04</b> the pilot:", "Prove it on one project, then scale", "Rather than pitch a system on a slide, the team ran a small one on real work and let the results make the case.",
            wrap(story(prose("A design system is a big ask of a client building everything else at the same time. So the team didn't pitch it on a slide. It ran a small system on one IBM project, watched whether it helped, and let the results make the case. The teams outside the pilot asked for it, and it delivered a clear efficiency gain on real work. That was enough to build the full system."))
                 + gap(32) + rail([("Propose", "A shared system to speed up delivery"), ("Pilot", "One IBM team builds with an early library"),
                       ("Measure", "Faster? Consistent? Do teams want it?"), ("Scale", "The full system, with Publicis Sapient")])
                 + '<div style="height:24px"></div>' + outcomes([("Result", "Faster", "A clear efficiency gain on real work."), ("Result", "Wanted", "Teams outside the pilot asked for it."),
                                                               ("Result", "Approved", "The go-ahead to build the full system."), ("Partner", "Publicis Sapient", "Shaped and reviewed the library with IBM.")])), mode="stage"),
    section("brand", "Brand to UI", "<b>05</b> brand to UI:", "A lavender brand, made usable", "Indigo and mist carry every screen. Violet does the work. Lavender and peach stay for brand moments.",
            wrap(palette + '<div style="height:16px"></div>' + canopy + '<div style="height:16px"></div>' + bento([
                (R + "canopy-uniform.jpg", "Canopy Twist uniform pattern", 6, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "logo.jpg", "Logo lockups, chosen by page language", 6, 3, {"fit": "contain", "bg": "#240852"}),
            ])), mode="stage"),
    section("foundations", "Foundations", "<b>06</b> foundations:", "Styles that travel through all 71 components", "Pick a breakpoint, switch the script. The grids and the type are drawn from the library's own values.",
            wrap(bp + '<div style="height:24px"></div>' + scripts + '<div style="height:16px"></div>' + bento([
                (R + "f-space.jpg", "Increments: 1 to 64px", 6, 3, {"fit": "contain", "bg": "#f6f7fc"}),
                (R + "f-effects.jpg", "Effects: depth, used sparingly", 6, 3, {"fit": "contain", "bg": "#f6f7fc"}),
                (R + "f-icons.jpg", "Iconography: Material Symbols", 6, 3, {"fit": "contain", "bg": "#f6f7fc"}),
                (R + "f-grid.jpg", "Grids: six breakpoints", 6, 3, {"fit": "contain", "bg": "#f6f7fc"}),
                (R + "src-type.jpg", "Library: Typography page", 3, 4, {"bg": "#fff"}),
                (R + "src-increments.jpg", "Library: Increments page", 3, 4, {"bg": "#fff"}),
                (R + "src-effects.jpg", "Library: Effects page", 3, 4, {"bg": "#fff"}),
                (R + "src-grids.jpg", "Library: Grids page", 3, 4, {"bg": "#fff"}),
            ])), mode="paper"),
    section("components", "Components", "<b>07</b> components, live:", "Switch the theme. Switch the language.", "Everything flips: direction, arrows, numbers and currency formatting.",
            wrap(specimen)),
    section("library", "Library", "<b>08</b> the library:", "71 components in 13 numbered families", "Read the families and you can read the product: an assistant, selling nudges, and the trip itself.",
            wrap(inventory("71", "components, each in English and Arabic, light and dark", fams) + '<div style="height:20px"></div>' + bento([
                (R + "btn-rex.jpg", "REX button · G03/B09", 5, 5, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-counter.jpg", "Counter · G03/B07", 7, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "badge-fomo.jpg", "FOMO badge · G01/B05", 7, 2, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-loader.jpg", "Loader button · G03/B03", 4, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-modal.jpg", "Modal button set · G03/B04", 4, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "avatar.jpg", "Avatar · G01/B01", 4, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-zoom.jpg", "Zoom · G03/B06", 4, 2, {"fit": "contain", "bg": "#240852"}),
                (R + "badge-location.jpg", "Location badge · G01/B06", 4, 2, {"fit": "contain", "bg": "#240852"}),
                (R + "badge-rating.jpg", "Rating badge · G01/B04", 4, 2, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-menu.jpg", "Menu item · G03/B05", 4, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "btn-double.jpg", "Double button · G03/B08", 4, 3, {"fit": "contain", "bg": "#240852"}),
                (R + "badge-round.jpg", "Round badge · G01/B03", 4, 3, {"fit": "contain", "bg": "#240852"}),
            ])), mode="stage"),
    section("done", "Definition of done", "<b>09</b> definition of done:", "Tested in four languages before it shipped", "Arabic for direction, German for long words, Japanese for a third script, and currencies with very long numbers.",
            wrap(stress + '<div style="height:24px"></div>' + rail([("Build", "Fewest frames; every text on a style, every colour on a variable"),
                                                                   ("Structure", "Named to convention, every useful variant, placed and described"),
                                                                   ("Test", "EN and AR, light and dark, long words, long numbers, in a real layout")]))),
    section("working", "How we worked", "<b>10</b> how we worked:", "Three companies, one way from idea to code",
            "The system sat between three organisations and many teams. It worked because the path from an idea to a component in code was the same every time.",
            wrap(timeline([("Phase 1", "The pilot", "An early library on one IBM project, to test whether a shared system would speed the teams up.", "IBM"),
                           ("Phase 2", "The system", "Styles, structure and components built from scratch in Figma, reviewed with Publicis Sapient and Riyadh Air's product team.", "IBM · Publicis Sapient"),
                           ("Phase 3", "Into code", "IBM engineers built the components in code, so every app used the same ones.", "IBM design · IBM engineering"),
                           ("Oct 2025", "Launch", "The apps launched with the airline. The first flight left Riyadh for London Heathrow.", "Riyadh Air")])
                 + gap(32)
                 + room([("Rules", "One page of rules", "The library opened with its own guide: what ready means, how it's structured, how to name things."),
                         ("Language", "Bilingual from day one", "Arabic wasn't a translation pass at the end. Every component shipped with its right-to-left version."),
                         ("Handoff", "Design and code in step", "Variant names matched the props engineers built, so handoff was a lookup, not a translation.")])
                 + '<p class="sc-note">How the three companies decided what shipped is its own case study: <a href="ibm-riyadh-air-ops.html">who decides what ships</a>.</p>')),
    section("impact", "Impact", "<b>11</b> what changed:", "From Figma to code to launch", "",
            wrap(outcomes([("Speed", "Proven first", "A pilot showed a clear efficiency gain before the full build."),
                           ("Consistency", "One airline", "71 components and six breakpoints, used by every team."),
                           ("Reach", "EN + AR", "Every component in both directions, light and dark."),
                           ("Adoption", "Shipped", "Built in code by IBM engineering. The apps launched with the airline in October 2025.")])
                 + '<div style="height:16px"></div>' + lessons(["Prove it small. A pilot on real work persuades faster than any deck.",
                                                               "Design the second language first. Arabic and German break what English never will.",
                                                               "Start at the smallest screen. A 184px watch made every larger layout simpler."])
                 )),
    section("playbook", "For your team", "<b>12</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "The pilot: one team, real work, and a clear answer on whether a system will pay off.",
                           "foundations": "Styles, a naming grammar and core components, tested in your languages and themes.",
                           "partner": "Grow the library with your teams, with a shared definition of done."}))),
]

page("ibm-riyadh-air", dict(
    h1="A design system for an airline that started from zero",
    lede="A pilot first, then 71 components that every Riyadh Air team built from, in English and Arabic, light and dark.",
    meta=[("Role", "Design system designer, IBM"), ("Client", "Riyadh Air"), ("Partners", "Publicis Sapient, IBM engineering"), ("Timeline", "2023–24")],
    proof=[("", "71", "", "components in 13 families"), ("2 × ", "2", "", "EN and AR, light and dark"), ("", "6", "", "breakpoints, watch to desktop"), ("", "8", "+", "apps from one library")],
    cover_alt="The Riyadh Air design system: Canopy Twist line art, a booking card and component sheets on indigo",
    client_logo=R + "logo-lockup.png",
    sections=S,
    credits="Aniket Pandey worked on this as a design system designer at IBM (2023–24), with the IBM design team, IBM engineering, Publicis Sapient and Riyadh Air's product, design and engineering teams. This is IBM client work done as an employee, not Layer One client work. Images belong to Riyadh Air and IBM and are shown for portfolio purposes.",
))
