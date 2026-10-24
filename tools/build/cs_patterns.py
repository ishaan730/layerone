from cs import *

P = "assets/work/patterns/"

services = ["Buy a used car", "Sell your car", "Get a loan", "Car check", "New cars", "Insurance", "Pay challan",
            "Recharge FASTag", "Car servicing", "Car wash", "Scrap and earn", "Hire a driver", "Credit cards", "Showrooms"]
svc = '<ul class="m-chips" data-inview>' + "".join(f'<li style="--i:{i}">{s}</li>' for i, s in enumerate(services)) + "</ul>"

cms = '''<div class="m-cms" data-cms>
  <div class="cms-form">
    <p class="cms-path">Homepage / Widgets / <b>contextual_card_slider</b></p>
    <label>Title <span data-cc>34 / 40</span><input data-cms-title maxlength="80" value="Like this car? Take it for a spin!"></label>
    <label>Button <span data-cb>15 / 18</span><input data-cms-btn maxlength="40" value="Book test drive"></label>
    <div class="cms-ratio" role="group" aria-label="Image shape"><span>Image</span><button type="button" aria-pressed="false" data-ratio="16 / 9">16:9</button><button type="button" aria-pressed="true" data-ratio="1 / 1">1:1</button><button type="button" aria-pressed="false" data-ratio="3 / 4">3:4</button></div>
    <p class="cms-lock"><b>Locked by the pattern:</b> size, spacing, type, colours, behaviour. <b>Editable:</b> image, text, button, link, schedule.</p>
  </div>
  <div class="cms-prev"><p class="small muted">Live preview</p>
    <div class="cms-card"><div class="cms-img" data-cms-img></div><div><p class="cms-t" data-cms-t>Like this car? Take it for a spin!</p><span class="cms-b" data-cms-b>Book test drive</span></div></div>
    <p class="cms-warn" data-cms-warn hidden>Over the limit: this title would break the card. Shorten it.</p>
  </div>
</div>'''

families = [("Banners", P + "w-banner-full.jpg", "Banners", "One template, three types: full bleed, padded and carousel, in fixed sizes. Used for campaigns, offers and the top of every homepage."),
            ("Grids", P + "w-grid-2.jpg", "Grids", "Two, three and four columns in landscape, square or portrait tiles, with one header and one button. Cars by body type, explore by brand."),
            ("Sliders", P + "w-slider-2.jpg", "Sliders", "Rails that scroll sideways with one to four cards in view, always with the next card peeking in. Hot deals, trending new cars."),
            ("Lists", P + "w-list.jpg", "Lists", "For content that needs more words than a tile: thumbnail, title, a line of text, a chevron. Showrooms, car checks."),
            ("Stories", P + "w-story.jpg", "Stories and video", "Story bubbles and video cards with autoplay set in the CMS. Customer stories, expert videos."),
            ("Nudges", P + "w-snack.jpg", "Snackbars and drop-off cards", "Small nudges that bring people back to what they left: a car they viewed, a loan application they didn't finish.")]

roles = '''<div class="m-names"><div class="nm-row"><span>Designer</span><code>contextual_card_slider</code><p>Picks patterns and sets the page order.</p></div>
  <div class="nm-row"><span>Developer</span><code>&lt;ContextualCardSlider /&gt;</code><p>Builds each pattern once, mapped to base tokens.</p></div>
  <div class="nm-row"><span>CMS team</span><code>contextual_card_slider</code><p>Fills images, copy and links, and schedules what goes live.</p></div>
  <div class="nm-row"><span>Product manager</span><code>Pattern request · High</code><p>Asks for new patterns with the request template, not one-off screens.</p></div></div>'''

spec = dict(
    h1="Pages built from tested blocks, not from scratch",
    lede="CARS24 was turning into a super app and launching new services almost every month. Every homepage and landing page was designed and built from zero. We built a pattern library that lets teams assemble pages from tested blocks, so they ship faster and every page feels like one product.",
    meta=[("Role", "Lead System Designer"), ("Team", "2 designers, 2 developers, a PM, a CMS lead"), ("Platforms", "App and mobile web"), ("Markets", "India, UAE, Australia")],
    cover=(P + "hero-hand.jpg", "A phone showing a CARS24 homepage built from pattern library blocks"),
    tldr=[("The problem", "Every new page started from a blank canvas. The same cards and carousels were built again and again, and no two services felt alike."),
          ("What we did", "Six families of page blocks with grid, text, image and behaviour rules, wired to the CMS and the tokens, with one name from Figma to code."),
          ("What changed", "Pages took about 43% less time. Within three months every major redesign in three countries was built on the library.")],
    kpis=[("43", "%", "~", "less time to design and build a page"), ("3", " months", "", "to reach every major redesign"),
          ("212", "k", "~$", "saved in design and development"), ("3", "", "", "countries building from one library")],
    chapters=[
        ("context", "Context", "A car company turning into a super app",
         "Loans, car checks, fines, FASTag, servicing, car wash: new services launched almost every month, each needing its own homepage, landing and offer pages.",
         svc + lead("The back end kept up. The screens didn't: several redesigns ran at once, and the app started to feel like many apps stitched together.")),
        ("problem", "Problem", "Every page started from a blank canvas",
         "Nothing was shared, so the same work was repeated, it cost more, took longer, and moving between services felt like changing apps.",
         compare((P + "audit-india.jpg", "Audit of the India homepages before the library"), (P + "rollout-india.jpg", "India screens rebuilt on the pattern library"),
                 ("Before", "After"), "Drag to compare the India audit with the screens rebuilt on the library.", ratio="2 / 1")
         + bars([("Time per new page", 100, 57, "100%", "~57%")], "Total time to design and build a page, before and after. The drop is what was measured: about 43%.")),
        ("research", "Research", "Borrowing what people already know",
         "Our users also lived in Swiggy, Zepto and Blinkit. Service grids became quick-action rows, offer banners became the banner family, scrolling rails became sliders.",
         pair((P + "insp-banners.jpg", "Offer banners from other consumer apps"), (P + "insp-grids.jpg", "Service grids from other consumer apps"),
              "Patterns customers already understood meant less to learn.")
         + more("We audited homepages, landing pages and exit flows in every market and sat with product managers, engineers and visual designers. Layouts were all over the place, one component existed in many builds, there were no rules for content, and nobody knew how a section should adapt across screens.")),
        ("rules", "Rules", "Every pattern comes with its own rules",
         "Grid, text limits, image shapes and behaviour, set in the CMS, so an editor can fill a pattern and still get a page that looks right. Try it: type a longer title, or change the image shape.",
         cms + fig(P + "w-grid-2.jpg", "One pattern fully specified: the two-column grid in three image shapes, every size marked for design and engineering.")),
        ("library", "Library", "Six families of page blocks",
         "Built on the base design system, with layout templates, ready-made combinations, tokens, specs and usage guidance.",
         tabs("families", families)),
        ("handoff", "Handoff", "One name from Figma to code to CMS",
         "The library only works if four groups can use it without waiting on each other. Every pattern has one name everywhere.",
         roles + pair((P + "spec-sheet.jpg", "Pattern implementation spreadsheet"), (P + "request-template.jpg", "Pattern request form"),
                      "The implementation sheet engineering builds from, and the request template for anything the library doesn't cover.")),
        ("pattern-to-page", "Pattern to page", "From empty patterns to a live page",
         "A page is now a stack of patterns. Drag the divider: on the left, the empty blocks with their rules; on the right, the same page filled in through the CMS. Scroll inside the frame.",
         '<div class="m-phonecmp">' + compare((P + "home-system.jpg", "The homepage as empty patterns"), (P + "home-live.jpg", "The same homepage, live"),
                                              ("Patterns", "Live"), "", ratio="720 / 10192", tall=True) + '</div>'),
        ("rollout", "Rollout", "One library, every market and service",
         "India's new homepage, the UAE app revamp, Australia's homepage in five themes, and new service apps for loans, servicing, car wash and car care.",
         fig(P + "rollout-uae.jpg", "The UAE revamp, built from library patterns.")
         + bars([("Faster pages (target 30–40%)", 40, 43, "target 40%", "43%"), ("Redesigns on the library (target 50%)", 50, 100, "target 50%", "all major redesigns")],
                "Both targets were beaten.")),
        ("learnings", "Learnings", "What we'd do again", "Small, token-driven blocks scale, and documentation decides adoption.",
         tiles([("Small, token-driven blocks scale", "They made fast experiments possible without new design debt."),
                ("Follow what users already know", "Familiar patterns leave room to innovate where it matters."),
                ("Docs decide adoption", "Clear guidelines kept people using it after launch."),
                ("Bring engineering in early", "It caught performance limits before they became rework.")])),
    ],
    gallery=[(P + "audit-different.jpg", "Six services, six different looks"), (P + "audit-uae.jpg", "Audit of the UAE app"),
             (P + "w-grid-3.jpg", "Three-column grid specification"), (P + "rollout-au.jpg", "Australia, one homepage in five themes"),
             (P + "rollout-dark.jpg", "Service apps in four colours, one set of patterns"), (P + "services.jpg", "Service themes side by side")],
    credits="Led by Aniket Pandey as Lead System Designer at CARS24, with two designers, two developers, a product manager and the CMS lead. Images belong to CARS24 and are shown for portfolio purposes.",
)
page("patterns", spec)
