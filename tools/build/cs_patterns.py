from cs import *

P = "assets/work/patterns/"

services = ["Buy a used car", "Sell your car", "Get a loan", "Car check", "New cars", "Insurance", "Pay challan",
            "Recharge FASTag", "Car servicing", "Car wash", "Scrap and earn", "Hire a driver", "Credit cards", "Showrooms"]
svc_chips = '<ul class="scope" style="margin-top:24px">' + "".join(f"<li>{s}</li>" for s in services) + "</ul>"

rules = '''<div class="table-wrap"><table class="data"><thead><tr><th>Rule</th><th>What it fixes</th><th>Example values</th></tr></thead><tbody>
<tr><td><strong>Grid structure</strong></td><td>Columns, gaps and scrolling, so every page has the same rhythm.</td><td>12px gap; 2, 3 or 4 columns; scroll only when the next card peeks in</td></tr>
<tr><td><strong>Text limits</strong></td><td>Every text slot has a size and a line limit. The CMS counts characters as editors type.</td><td>18px section title, 1 line; 15px card title, 2 lines; 13px body, 2 lines</td></tr>
<tr><td><strong>Image shapes</strong></td><td>Three ratios cover almost everything, so the CMS can crop and compress ahead of time.</td><td>16:9 banners; 1:1 tiles; 3:4 stories</td></tr>
<tr><td><strong>Behaviour</strong></td><td>Switches in the CMS, not new designs: the same carousel can autoplay on one page and sit still on another.</td><td>Breakpoints 360, 412, 768+; image, Rive or video; autoplay; infinite scroll</td></tr>
</tbody></table></div>'''

families = [("Banners", "One template in three types: full bleed, padded and carousel, in fixed sizes.", "Campaigns, offers, the top of every homepage"),
            ("Grids", "Two, three and four columns, in landscape, square or portrait tiles, with one header and one button.", "Help and support, cars by body type, explore by brand"),
            ("Sliders", "Rails that scroll sideways, one to four cards in view, always with the next card peeking in.", "Hot deals, trending new cars, loans that fit"),
            ("Lists", "Two sizes for content that needs more words than a tile: thumbnail, title, one line and a chevron.", "Showrooms, car checks, fraud warnings"),
            ("Stories and video", "Story bubbles and video cards, with autoplay set in the CMS.", "Customer stories, expert videos, how CARS24 works"),
            ("Snackbars and drop-off cards", "Small nudges that bring people back to what they left.", "Resume your search, finish your loan application")]
fam = '<div class="table-wrap"><table class="data"><thead><tr><th>Family</th><th>What it is</th><th>Used for</th></tr></thead><tbody>' + "".join(
    f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in families) + "</tbody></table></div>"

roles = cards([("Designer", "Picks patterns and variants and sets the order of the page. Works with <code>contextual_card_slider</code>."),
               ("Developer", "Builds each pattern once, mapped to base tokens, and reuses it everywhere: <code>&lt;ContextualCardSlider /&gt;</code>."),
               ("CMS team", "Fills in images, copy and links, and schedules what goes live. Editors change content, never layout."),
               ("Product manager", "Asks for new patterns with the request template, not a one-off screen.")])

sections = [
("context", "Context", "Context", "A car company turning into a super app",
 prose("By the time of this project, CARS24 was more than a place to buy and sell used cars. In one app you could get a loan, check a car's history, pay a fine, recharge FASTag, book a service or a car wash. New services launched almost every month, in India, the UAE and Australia.",
       "The back end was keeping up. The screens people saw were not. Several redesigns were running at once, each with its own team, and the app was starting to feel like many apps stitched together.")
 + svc_chips + '<p class="figure" style="margin-top:10px;font-size:14px;color:var(--color-text-muted)">Some of the services sharing one app. Each needed its own homepage, landing pages and offer pages.</p>'),

("problem", "The problem", "The problem", "Every page started from a blank canvas",
 prose("Whenever a team needed a homepage or a landing page, they designed and built it from scratch. Nothing was shared, so the same cards, buttons and carousels were made again and again, it cost more, it took longer, and the app felt different on every screen.")
 + fig(P + "audit-different.jpg", "Six services, six different looks: what the audit found inside one app.", "Six CARS24 app screens each with a different visual style")
 + cards([("No shared direction", "Every team made its own design calls."),
          ("The same work, again", "Cards, CTAs and carousels were rebuilt by each team."),
          ("Higher cost", "Design and engineering hours went into repeats."),
          ("Slow launches", "New features waited for pages to be made.")])),

("goal", "The goal", "The goal", "Build a page once, reuse it everywhere",
 prose("The goal was a reusable, scalable pattern library that helps teams ship consistent pages faster, with less effort, while leaving room to experiment without breaking the brand.")
 + '<div class="table-wrap"><table class="data"><thead><tr><th>How we\'d know it worked</th><th>Target</th></tr></thead><tbody>'
   '<tr><td>New or redesigned pages built from patterns</td><td class="num">50%+</td></tr>'
   '<tr><td>Faster design and development</td><td class="num">30–40%</td></tr>'
   '<tr><td>One look across services and flows</td><td>Consistent in audits</td></tr>'
   '<tr><td>Handoff between design and engineering</td><td>No rework</td></tr></tbody></table></div>'),

("research", "Research", "Research", "What we had, and what people already knew",
 prose("We audited the homepages, landing pages and exit flows in every market, and sat with product managers, engineers and visual designers to collect the work they kept repeating. Layouts were all over the place, one component existed in many versions, there were no rules for content, and nobody knew how a section should adapt across screens.",
       "Our users also used Swiggy, Zepto, Blinkit and District every day. Building on patterns they already understood, like service grids, offer banners and scrolling rails, meant less to learn. Service grids became quick-action rows, offer banners became the banner family, and scrolling rails became sliders.")
 + pair((P + "audit-india.jpg", "Audit of India homepages"), (P + "insp-banners.jpg", "Offer banners from other consumer apps"), "Left: the India audit. Right: offer banners from apps CARS24 customers already use.")),

("rules", "Pattern rules", "Rules", "Every pattern comes with its own rules",
 prose("We started with the blocks every page needs: banners, grids, rails, lists and story widgets. Each one got the same four kinds of rules, so a content editor can fill a pattern in the CMS and still get a page that looks right. We also worked with engineering on performance, because a homepage carries a lot of these at once.")
 + rules
 + fig(P + "w-grid-2.jpg", "One pattern, fully specified: the two-column grid in three image shapes, with every size marked for design and engineering.", "Spec of the two-column grid pattern with redline measurements")),

("library", "The library", "The library", "Six families of patterns, and a toolbox around them",
 prose("We turned the blocks into a modular library on top of the base design system. It came with layout templates for homepages and landing pages, ready-made combinations, content rules set up in the CMS, tokens and specs for every pattern, and guidance on which pattern to use when.")
 + fam
 + pair((P + "w-slider-2.jpg", "Slider pattern specification"), (P + "w-story.jpg", "Story and video pattern specification"), "Specs for the slider and story families.")),

("handoff", "Handoff", "Handoff", "One name from Figma to code to CMS",
 prose("The library only works if four groups can use it without waiting on each other. Every pattern has one name everywhere, so a designer, a developer and a content editor are always talking about the same thing.")
 + roles
 + pair((P + "spec-sheet.jpg", "Pattern specification spreadsheet"), (P + "request-template.jpg", "Pattern request form template"), "The spec sheet engineering builds from, and the request template product managers use to ask for new patterns.")),

("rollout", "Rollout", "Rollout", "One library, every market and service",
 prose("The library became the base for every major redesign: the India homepage, the UAE app revamp, the Australia homepage with its five themes, and the new service apps for loans, servicing, car care and car wash. Different colours and content, the same building blocks underneath.",
        "Both targets were beaten. New pages took about 43% less time to design and build, against a target of 30–40%, and every major redesign was on the library within three months, against a target of half. Teams could test ideas without new builds, and the savings in design and development came to an estimated $212k.")
 + fig(P + "rollout-uae.jpg", "The UAE revamp, built from library patterns.", "Redesigned CARS24 UAE app screens")
 + pair((P + "rollout-india.jpg", "India app screens built from patterns"), (P + "rollout-au.jpg", "Australia app screens built from patterns"), "India and Australia, from the same library.")
 + '<figure class="figure"><div class="figure-scroll" tabindex="0" aria-label="Scrollable full homepage"><img src="../' + P + 'home-live.jpg" alt="A full CARS24 homepage assembled entirely from library patterns" width="720" height="10192" loading="lazy"></div><figcaption>A full homepage assembled from patterns. Scroll inside the frame to see all of it.</figcaption></figure>'),

("learnings", "Learnings", "Learnings", "What we'd do again",
 cards([("Small, token-driven blocks scale", "They made fast experiments possible without new design debt."),
        ("Follow what users already know", "Familiar patterns leave room to innovate where it matters."),
        ("Docs decide adoption", "Clear guidelines are what kept people using the library after launch."),
        ("Bring engineering in early", "It caught performance limits before they became rework.")])),
]

page("patterns",
     "Pages built from tested blocks, not from scratch",
     "CARS24 was becoming a super app and launching new services almost every month, and every homepage and landing page was designed and built from zero. We built a pattern library that lets teams assemble pages from tested blocks, so they ship faster and every page feels like part of one product.",
     [("Client", "CARS24"), ("Team", "2 designers, 2 developers, a PM and a CMS lead"), ("Platforms", "App and mobile web"), ("Markets", "India, UAE, Australia")],
     [("~43%", "less time to design and build a new page"), ("3 months", "to reach every major redesign"),
      ("~$212k", "saved in design and development time"), ("3", "countries building from one library")],
     P + "hero-hand.jpg", "A phone showing a CARS24 homepage built from pattern library blocks", sections, "cars24-pattern-library.html")
