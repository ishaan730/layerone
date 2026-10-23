from cs import *

T = "assets/work/tokens/"

sections = [
("context", "Context", "Context", "A company that grew faster than its design",
 prose("CARS24 started as a place to buy and sell used cars. In three years it became a family of products, including loans, insurance, servicing and new cars, and it expanded from India into the UAE and Australia.",
       "The teams grew just as fast. Design went from 20 people to 70, and engineering from about 100 to more than 200. Nothing shared held the work together, so each product and each country slowly built its own look.")
 + '<div class="table-wrap"><table class="data"><thead><tr><th>Measure</th><th>Three years earlier</th><th>At the start of the project</th></tr></thead><tbody>'
   '<tr><td>Product lines</td><td class="num">1</td><td class="num">6+</td></tr>'
   '<tr><td>Countries</td><td class="num">1</td><td class="num">3</td></tr>'
   '<tr><td>Designers</td><td class="num">20</td><td class="num">70</td></tr>'
   '<tr><td>Engineers</td><td class="num">~100</td><td class="num">200+</td></tr></tbody></table></div>'
 + fig(T + "products.jpg", "The CARS24 family when the project started. Every product had drifted into its own style.", "Logos of CARS24 products including Loans24, Insure24 and Autopilot")),

("problem", "The problem", "The problem", "Five codes for one colour",
 prose("One shade of blue lived in the codebase as five different values. There was no central home for colour, type or spacing, so each team defined its own. Designers copied colours from old screens, developers copied them again in code, and the small differences kept piling up.")
 + cards([("Design", "Every team kept its own styles. Buttons, inputs, alerts and tabs looked different from product to product, and nothing was documented."),
          ("Engineering", "With no shared UI code, each team rebuilt the same values. Handoffs broke and the same bugs kept coming back."),
          ("Brand", "India, the UAE and Australia each had their own design language. New products launched with styles of their own."),
          ("People", "Nobody owned the foundations, and with an average tenure of six to seven months, context kept walking out the door.")])
 + fig(T + "before.jpg", "The old visual language: off-brand promo colours, mixed icon styles, three illustration styles, and one orange doing every job.", "A collage of inconsistent CARS24 UI before the project")),

("research", "Research", "Research", "Listening before changing anything",
 prose("The existing setup was closer to a starter template than a system. Before touching it, we learned how teams were organised, where they got stuck, and where the business was heading over the next six to twelve months, including a rebrand.",
       "We interviewed stakeholders, sat in on team rituals and looked at how styles were really used in files and in code. Then we brought design, engineering, marketing, brand, product managers and a few external users into the same workshops to map problems, desired outcomes and priorities.",
       "The aim was a system people would want to use, not one they were told to use.")
 + pair((T + "workshop-1.jpg", "A cross-team workshop in progress"), (T + "workshop-2.jpg", "Workshop participants sorting sticky notes"), "Cross-team workshops with design, engineering, marketing, brand and product.")
 + fig(T + "insights-board.jpg", "Everything from the workshops went onto one board, grouped into themes and ranked.", "A large board of grouped workshop findings")),

("palette", "The palette", "Colour", "The colours had to go first",
 prose("While planning the tokens, it became clear the colours themselves were the biggest problem. Many pairs failed basic contrast checks, nobody could say which colours were brand and which were UI, and the palette couldn't stretch across many products and markets.",
       "A design system team doesn't change a brand colour on its own. We built a deck with the accessibility failures, the dated visuals and what designers had told us in interviews, took it to the Head of Design, and leadership agreed to a full overhaul.")
 + fig(T + "buyin-deck.jpg", "The deck that got leadership on board.", "Slides from the rebrand proposal deck")
 + prose("We moved the CARS24 blue from the older, darker <code>#0059A3</code> to an electric <code>#4736FE</code> that holds its contrast on screens and still prints true. Swatches were matched against Pantone cards, because printers, sign makers and vendors all work from Pantone.",
         "To find the blue's partner we tested teal, pink and mint on the same real layouts, with the same photos and copy, so the only thing that changed was the colour. Mint won.")
 + pair((T + "pantone.jpg", "Testing blues against Pantone shade cards"), (T + "dir-mint.jpg", "Campaign layouts using the final blue and mint pairing"), "Testing against Pantone cards, and the final blue and mint pairing on real campaign layouts.")
 + fig(T + "colour-studies.jpg", "Poster studies that pushed shape and colour hard before the strongest ideas went back into the brand graphics.", "Bold geometric poster studies in the new palette")),

("oklch", "Why OKLCH", "Colour science", "Describing colour the way people see it",
 prose("The old palette only existed as HEX and RGB, which tell a screen how much red, green and blue to mix but say nothing about how bright a colour looks to a person.",
       "We specified the new palette in OKLCH as well. OKLCH describes colour by lightness, chroma and hue, and its lightness follows human perception. That made it much easier to build even ten-step ramps, predict contrast before testing, and keep colours steady between screen and print.",
       "Every step of every ramp was checked against WCAG: AA as the minimum for product and marketing, AAA for important text and key actions.")
 + '<figure class="figure"><div class="hue-compare"><p>HSL, 50% lightness</p><div class="hue-row"><span style="background:hsl(0 100% 50%)"></span><span style="background:hsl(55 100% 50%)"></span><span style="background:hsl(120 100% 50%)"></span><span style="background:hsl(185 100% 50%)"></span><span style="background:hsl(235 100% 50%)"></span><span style="background:hsl(300 100% 50%)"></span></div><p>OKLCH, 70% lightness</p><div class="hue-row"><span style="background:oklch(70% 0.17 25)"></span><span style="background:oklch(70% 0.17 85)"></span><span style="background:oklch(70% 0.17 145)"></span><span style="background:oklch(70% 0.17 200)"></span><span style="background:oklch(70% 0.17 265)"></span><span style="background:oklch(70% 0.17 330)"></span></div></div><figcaption>Six hues at one lightness value, rendered live. In HSL, yellow and cyan glare while blue looks dark. In OKLCH they read as equally bright.</figcaption></figure>'),

("tokens", "Token architecture", "Tokens", "Four layers between a hex code and a button",
 prose("We studied Shopify Polaris, Salesforce Lightning, IBM Carbon and Material. None fitted how CARS24 was organised: one company, three countries and several businesses sharing one system. So we built our own, and started with colour because the rebrand was about to change every colour anyway.")
 + '''<ol class="token-chain">
   <li><span class="q">What is it?</span><h3>Value</h3><code>#4736FE</code><p>A raw colour. Nobody uses these directly.</p></li>
   <li><span class="q">Which step of which ramp?</span><h3>Primitive</h3><code>color-blue-500</code><p>Gives every value a name and a place in a scale.</p></li>
   <li><span class="q">What is it for?</span><h3>Semantic</h3><code>color-surface-background-primary</code><p>Names the purpose. Themes and dark mode swap values here.</p></li>
   <li><span class="q">Exactly where is it used?</span><h3>Component</h3><code>button-background-primary</code><p>Scoped to one component, so it can be tuned on its own.</p></li>
 </ol>'''
 + prose("The question we heard most in reviews was whether something should be a new semantic token. Too many and nobody can find the right one; too few and teams hard-code values. So we wrote two short rules: make it semantic when the idea is shared by several components, is about intent rather than colour, and is likely to change between themes. Keep it a component token when it's specific to one component and might need overriding.",
         "Names were where teams disagreed most. One file had <code>primaryBtnBg</code>, another <code>blue-button-new</code>, and both meant the same thing. We agreed one grammar, with parts in a fixed order, and wrote documentation and onboarding so any team could extend it and contribute back.")
 + fig(T + "benchmarking.jpg", "Benchmarking other systems, and the first drafts of base and alias colour tokens.", "Figma frames comparing token structures")),

("architecture", "Architecture", "Architecture", "One system, many products",
 prose("Everything sits on one base system. India is the default theme; each other country and business adds a theme that overrides only what it has to, with its name at the front of its tokens so an override is easy to spot.",
       "Teams plug in at three levels, each a Figma library and a GitHub repository: the core system owned by the design system team, a pattern library per vertical, and shared pattern libraries for verticals that look alike. Components move up a level when more teams need them.")
 + cards([("Core system", "Tokens, components and docs. Owned by the design system team."),
          ("Vertical pattern libraries", "Buy and sell, Loans, Australia, Dubai, New cars. Unique components for one business."),
          ("Shared pattern libraries", "For verticals that look alike, such as Dubai and Australia."),
          ("Labs", "Where foundation and pattern experiments are tested before they're promoted.")])),

("impact", "Impact", "Impact", "What one colour change costs",
 prose("Say a colour used in more than a thousand places needs to change. At a mid-level designer's rate of $24 an hour, here's the same job done two ways.")
 + '''<div class="cost" role="img" aria-label="By hand: about 9 hours and $216. With a token: 30 seconds and $0.19.">
   <div class="cost-row"><span>By hand</span><div class="cost-bar" style="width:100%"></div><span>~9 h, $216</span></div>
   <div class="cost-row"><span>With a token</span><div class="cost-bar cost-bar--tiny"></div><span>30 s, $0.19</span></div>
 </div>'''
 + prose("That's 99.9% less time on every colour change from then on. Across the company it added up to an estimated $156k a year in engineering time, and the rebrand rolled out 60% faster across three countries.")
 + fig(T + "apps.jpg", "The same palette now runs through the apps, campaigns and brand graphics in India and the UAE.", "CARS24 app screens in the new palette")),

("learnings", "Learnings", "Learnings", "What we'd tell ourselves at the start",
 cards([("Tie it to business goals", "A system earns support when it clearly helps what the company is trying to do, and the success measures should show that."),
        ("Measure more than adoption", "Time saved, cost avoided and quality gained tell a far better story than usage alone."),
        ("Show, don't tell", "Demos and regular rituals changed more minds than any document."),
        ("Governance keeps it alive", "Clear ownership and a clear token structure are what stop a system drifting again.")])),
]

page("tokens",
     "One colour system for 10+ products in three countries",
     "CARS24 grew from one product to more than six, across three countries, in about three years, and its design didn't keep up. We gave every team one colour palette and one set of design tokens, and that palette became the colour of the CARS24 rebrand.",
     [("Client", "CARS24"), ("Duration", "4 months"), ("Team", "2 designers, 3 developers"), ("Scope", "Colour overhaul and token architecture")],
     [("65%", "faster design-to-development handoff"), ("5 → 1", "button implementations merged into one"),
      ("100%", "of Figma tokens map one-to-one to code"), ("~$156k", "estimated yearly savings in engineering time")],
     T + "hero.jpg", "CARS24 campaign graphics in the new electric blue and mint palette", sections, "cars24-tokens.html")
