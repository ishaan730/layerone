from cs import *

T = "assets/work/tokens/"

# --- custom modules -------------------------------------------------------
blues = ["#0059A3", "#005AA5", "#0058A1", "#0A5BA4", "#0059A4"]
files = ["seller-app/colors.ts", "loans/theme.js", "buyer-web/_vars.scss", "uae/styles.css", "new-cars/tokens.json"]
unify = f'''<div class="m-unify" data-unify>
  <div class="u-grid">{"".join(f'<div class="u-sw"><i style="background:{c}"></i><code>{c}</code><span>{f}</span></div>' for c, f in zip(blues, files))}</div>
  <div class="u-one"><i></i><div><code>color-brand-primary</code><span>One token. Every product reads it.</span></div></div>
  <div class="u-ctl"><p class="small muted">An illustration of the audit finding: one blue, five codes.</p><button type="button" class="pill pill--accent" data-unify-btn>Merge into one token</button></div>
</div>'''

gradients = '''<div class="m-grad">
  <div><p>Brand blue → orange, mixed in <b>sRGB</b></p><div class="g" style="background:linear-gradient(90deg in srgb, #4736fe, #ff6b3d)"></div></div>
  <div><p>The same two colours, mixed in <b>OKLCH</b></p><div class="g" style="background:linear-gradient(90deg in oklch, #4736fe, #ff6b3d)"></div></div>
  <div><p>Six hues at <b>HSL</b> 50% lightness</p><div class="hues">''' + "".join(f'<span style="background:hsl({h} 100% 50%)"></span>' for h in (0, 55, 120, 185, 235, 300)) + '''</div></div>
  <div><p>Six hues at <b>OKLCH</b> 70% lightness</p><div class="hues">''' + "".join(f'<span style="background:oklch(70% 0.15 {h})"></span>' for h in (25, 85, 145, 200, 265, 330)) + '''</div></div>
</div>'''

ramp_steps = [("50", "#f1f0ff"), ("100", "#dcd9ff"), ("200", "#bdb6ff"), ("300", "#998eff"), ("400", "#7466ff"), ("500", "#4736fe"), ("600", "#3a26e0"), ("700", "#2e1db4"), ("800", "#231788"), ("900", "#19105e")]
ramp = '<div class="m-ramp" data-ramp-live>' + "".join(f'<button type="button" style="--c:{c}" data-hex="{c}" data-name="color-blue-{s}"><span>{s}</span></button>' for s, c in ramp_steps) + '''
  <div class="r-read" aria-live="polite"><code data-r-name>color-blue-500</code><code data-r-hex>#4736FE</code><span data-r-w></span><span data-r-b></span></div></div>'''

chain = '''<div class="m-chain" data-brand style="--b:#4736fe;--b2:#4736fe1f;--acc:#9de7c8">
  <div class="seg-toggle" role="group" aria-label="Brand"><button type="button" aria-pressed="false" data-b="#0059a3" data-b2="#0059a31f" data-acc="#ef6e0b" data-p="color-blue-700 · color-orange-500">Old brand</button><button type="button" aria-pressed="true" data-b="#4736fe" data-b2="#4736fe1f" data-acc="#9de7c8" data-p="color-blue-500 · color-mint-300">New brand</button></div>
  <div class="ch-grid">
    <div class="layers">
      <div><span>Primitive</span><code data-prim>color-blue-500 · color-mint-300</code><i class="sw"></i></div>
      <div><span>Semantic</span><code>color-action-primary</code><code>color-surface-accent</code></div>
      <div><span>Component</span><code>button-background-primary</code><code>badge-background-rest</code></div>
    </div>
    <div class="mini-app">
      <div class="ma-top"><b>CARS24</b><span>Dubai</span></div>
      <span class="ma-badge">Best price guarantee</span>
      <p class="ma-h">Sell your car in a few steps</p>
      <div class="ma-card"><span>Hyundai Creta, 2021</span><b>₹ 9.8 lakh</b><span class="ma-ok">Inspected</span></div>
      <span class="ma-btn">Get best price</span>
    </div>
  </div>
  <p class="small muted">Switch the brand. Only the primitive values change; every component picks them up through its semantic tokens.</p>
</div>'''

calc = '''<div class="m-calc" data-calc>
  <div class="calc-in">
    <label>Places a colour is used <output data-o="places">1,000</output><input type="range" min="50" max="5000" step="50" value="1000" data-i="places"></label>
    <label>Seconds per manual change <output data-o="secs">30</output><input type="range" min="10" max="120" step="5" value="30" data-i="secs"></label>
    <label>Designer rate, $ per hour <output data-o="rate">24</output><input type="range" min="10" max="120" step="1" value="24" data-i="rate"></label>
  </div>
  <div class="calc-out">
    <div class="co-row"><span>By hand</span><div class="co-bar"><i data-bar-hand style="width:100%"></i></div><b data-hand>~8.3 h · $200</b></div>
    <div class="co-row"><span>With a token</span><div class="co-bar"><i class="t" data-bar-tok></i></div><b data-tok>30 s · $0.20</b></div>
    <p class="co-big"><strong data-saved>99.9%</strong> less time on every colour change</p>
  </div>
</div>'''

arch = tiles([("Base system, India theme", "Base tokens and components. Every other theme is an extended Figma file and code package."),
              ("Australia", "au tokens and components override only what they must."),
              ("Loans (NBFC)", "nbfc-prefixed tokens, so an override is easy to spot in review."),
              ("UAE", "uae tokens and components, Arabic-ready.")], cols=2)

spec = dict(
    h1="One colour system for 10+ products in three countries",
    lede="CARS24 grew from one product to more than six, across three countries, in about three years, and its design didn't keep up. One blue lived in the code as five different values. We gave every team one palette and one set of design tokens, and that palette became the colour of the CARS24 rebrand.",
    meta=[("Role", "Design Systems Lead"), ("Timeline", "4 months"), ("Team", "2 designers, 3 developers"), ("Scope", "Colour overhaul, token architecture")],
    cover=(T + "hero.jpg", "CARS24 campaign graphics in the new electric blue and mint"),
    tldr=[("The problem", "Six products, three countries, no shared foundations. The same blue existed as five codes and every team rebuilt the basics."),
          ("What we did", "A new palette specified in OKLCH, contrast-checked at every step, and a four-layer token architecture with a theme for each business."),
          ("What changed", "Handoff got 65% faster, five button builds became one, and the rebrand rolled out 60% faster across three countries.")],
    kpis=[("65", "%", "", "faster design-to-development handoff"), ("5", " → 1", "", "button implementations merged into one"),
          ("10", "+", "", "product lines on one token system"), ("156", "k", "~$", "estimated yearly engineering savings")],
    chapters=[
        ("context", "Context", "A company that grew faster than its design",
         "In three years CARS24 went from one used-car marketplace to a family of products in India, the UAE and Australia. Teams grew faster still.",
         bars([("Product lines", 1, 6, "1", "6+"), ("Countries", 1, 3, "1", "3"), ("Designers", 20, 70, "20", "70"), ("Engineers", 100, 200, "~100", "200+")],
              "Three years before the project, and at its start.")
         + fig(T + "products.jpg", "The CARS24 family when the project started. Every product had drifted into its own style.")),
        ("problem", "Problem", "Five codes for one colour",
         "There was no central home for colour, type or spacing. Designers copied colours from old screens, developers copied them again in code.",
         unify
         + compare((T + "before.jpg", "The old CARS24 visual language"), (T + "apps.jpg", "The CARS24 apps in the new palette"), ("Before", "After"),
                   "Drag to compare the old visual language with the apps after the rebrand.")
         + more("Every team kept its own styles, so buttons, inputs, alerts and tabs looked different from product to product. Nothing was documented, and many designers worried a system would box them in.",
                "With no shared UI code each team rebuilt the same values; handoffs broke and the same bugs came back. India, the UAE and Australia each had their own design language, and new products launched with styles of their own. With an average tenure of six to seven months, context kept walking out the door.")),
        ("research", "Research", "Listening before changing anything",
         "We interviewed stakeholders, sat in on rituals and audited how styles were really used. Then we put design, engineering, brand, marketing and product in one room.",
         pair((T + "workshop-1.jpg", "A cross-team workshop in progress"), (T + "workshop-2.jpg", "Workshop participants sorting findings"),
              "Cross-team workshops. The aim was a system people would want to use, not one they were told to use.")
         + more("The existing setup was closer to a starter template than a system. Before touching it, we learned how teams were organised, where they got stuck, and where the business was heading over the next six to twelve months, including a rebrand.",
                "Everything from the workshops went onto one board, where we grouped it into themes and ranked what to fix first. The same problems kept coming up: screens built differently from how they were designed, values nobody could reuse, an outdated palette, and no shared vocabulary.")),
        ("colour", "Colour", "An electric blue that works everywhere",
         "The old palette failed basic contrast checks and couldn't stretch across products. We moved to an electric #4736FE, matched against Pantone cards so it prints true, and chose mint as its partner after testing three on the same layouts.",
         compare((T + "dir-teal.jpg", "Campaign layout tested with teal"), (T + "dir-mint.jpg", "Campaign layout with the final mint"), ("Teal", "Mint, final"),
                 "Same layouts, same photos, same copy. Only the partner colour changes.", ratio="1800 / 923")
         + fig(T + "colour-studies.jpg", "Poster studies that pushed shape and colour before the strongest ideas went into the brand graphics.")
         + more("A design system team doesn't change a brand colour on its own. With other designers we built a deck that showed the accessibility failures, how dated the visuals felt, and what designers had told us in interviews. We took it to the Head of Design, and leadership agreed to a full overhaul.",
                "We split the palette in two: a calm set for product UI, and a bright set marketing can use for campaigns without it leaking into the product.")),
        ("oklch", "OKLCH", "Describing colour the way people see it",
         "HEX and RGB tell a screen how much red, green and blue to mix, not how bright a colour looks. OKLCH's lightness follows human perception, so even ramps and predictable contrast come for free. Both comparisons below are rendered live by your browser.",
         gradients
         + lead("Every core colour got a ten-step ramp, each step checked against WCAG. Select a step to see its contrast.")
         + ramp),
        ("tokens", "Tokens", "Four layers between a hex code and a button",
         "We studied Polaris, Lightning, Carbon and Material; none fitted one company with three countries and several businesses. So we built our own, starting with colour.",
         '''<div class="chainrow"><div><span>What is it?</span><h3>Value</h3><code>#4736FE</code><p>A raw colour. Nobody uses these directly.</p></div>
            <div><span>Which step of which ramp?</span><h3>Primitive</h3><code>color-blue-500</code><p>Names a value and gives it a place in a scale.</p></div>
            <div><span>What is it for?</span><h3>Semantic</h3><code>color-action-primary</code><p>Names the purpose. Themes and dark mode swap here.</p></div>
            <div><span>Exactly where?</span><h3>Component</h3><code>button-background-primary</code><p>Scoped to one component, tunable on its own.</p></div></div>'''
         + chain
         + more("The most common question in reviews was whether something should be a new semantic token. Too many and nobody can find the right one; too few and teams hard-code values. Two rules settled it: make it semantic when it's shared by several components, is about intent rather than colour, and is likely to change between themes. Keep it a component token when it's specific to one component.",
                "Names were where teams disagreed most. One file had primaryBtnBg, another blue-button-new, and both meant the same thing. We agreed one grammar with parts in a fixed order, and wrote documentation and onboarding so any team could extend it.")),
        ("architecture", "Architecture", "One system, many products",
         "Everything sits on one base. Each country and business adds a theme that overrides only what it needs, with its name at the front of its tokens. Teams plug in at three levels: core, a pattern library per vertical, and shared libraries for verticals that look alike.",
         arch + fig(T + "benchmarking.jpg", "Benchmarking other systems, and the first drafts of base and alias colour tokens.")),
        ("impact", "Impact", "What one colour change costs",
         "Say a colour is used in a thousand places and needs to change. Move the sliders: the token version is always one change.",
         calc
         + tiles([("Speed", "65% faster handoff. Five button builds became one shared component."), ("Money", "About $156k a year in engineering time, estimated. Rebrand rolled out 60% faster."),
                  ("Scale", "Every Figma token maps one-to-one to code, across 10+ product lines in 3 countries."), ("Culture", "Joint design and engineering reviews became a habit, not an exception.")])),
        ("learnings", "Learnings", "What we'd tell ourselves at the start", "Short version: tie it to the business, measure more than adoption, and show rather than tell.",
         tiles([("Tie it to business goals", "A system earns support when it clearly helps what the company is trying to do."),
                ("Measure more than adoption", "Time saved, cost avoided and quality gained tell a better story than usage."),
                ("Show, don't tell", "Demos and regular rituals changed more minds than any document."),
                ("Governance keeps it alive", "Clear ownership and a clear token structure stop a system drifting again.")])),
    ],
    gallery=[(T + "insights-board.jpg", "The workshop board, grouped and ranked"), (T + "buyin-deck.jpg", "The deck that got leadership on board"),
             (T + "pantone.jpg", "Testing blues against Pantone cards"), (T + "dir-pink.jpg", "The partner-colour test, in pink"),
             (T + "posters.jpg", "Early poster studies"), (T + "process-plan.jpg", "The week-by-week plan from audit to palette"),
             (T + "brainstorm.jpg", "Working sessions on categories, states and naming")],
    credits="Led by Aniket Pandey as Design Systems Lead at CARS24, with Vibhu (design) and Priyesh, Harish and Piyush (engineering), and CARS24's brand and product teams. Images belong to CARS24 and are shown for portfolio purposes.",
)
page("tokens", spec)
