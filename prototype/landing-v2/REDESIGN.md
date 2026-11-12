# Layer One landing page: audit, strategy and redesign rationale

Prototype v2 · November 2026 · branch `prototype/landing-v2` · nothing in production was changed

**Open the prototype:** `prototype/landing-v2/layer-one-landing-v2.html` (one self-contained file; double-click it).
Source: `index.html`, `styles.css`, `app.js` in the same folder.

---

## 1. The business, as the site itself describes it

| | |
|---|---|
| What Layer One is | A design systems studio in Bangalore, led by Aniket Pandey. Design systems are the only work it takes. |
| Stage | New. It opened for studio work in 2026 and has no studio clients yet. The site's job is to win the first ones. |
| Offer | Audit: $1,500, 2 weeks, fixed. Foundations: $5,900, 6 weeks, fixed. Partner: $2,900 a month. Three founding-partner slots for 2027 at 20% off. |
| Proof | Six years inside design system teams at IBM, CARS24 and JPMorgan Chase, as an employee. Eight interactive case studies, nine free tools, 51 guides. |
| Buyer | Heads of design, engineering leaders and founders at product companies with several squads or products, where UI has started to drift. |
| Desired action | Book a 30-minute call. The audit is the low-risk first purchase. |

**The positioning I'd hold.** *The specialist studio that builds the design system your teams ship on: foundations in six weeks, at a published fixed price, by the person who has run systems at enterprise scale.*

**Where I pushed back on the brief.** The brief suggests positioning as a "design systems and digital product design partner". I kept Layer One a specialist. Three reasons:
- A new studio wins on focus, not breadth.
- Every piece of proof it has is design systems work.
- "We only do this" is the most credible line on the page.

**Why choose Layer One over a general agency or a larger consultancy:**

1. **Specialist only.** Not a product agency that also does design systems.
2. **Published, fixed prices.** Listings I found for comparable agency work quote monthly subscriptions and enterprise projects that cost many times more, usually without a public price. I haven't verified individual competitors' prices.
3. **The senior person does the work**, in the client's Figma and repository.
4. **Governance and adoption are included**, not just components. That's where systems actually fail.
5. **The thinking is public.** Tools and guides let a buyer judge the method before any call.
6. **Honesty.** The site says plainly that it's new and where the experience comes from.

---

## 2. Audit of the current home page

Measured on the current production build at 1440px wide: 10,468px tall, 620 words, 21 images.

| Area | Finding | Why it costs conversions |
|---|---|---|
| Structure | The page is a portfolio layout: 11 identical project frames take about 7,000 of its 10,468 pixels. | A buyer has to scroll past the whole archive before learning what they can buy. |
| Offer | The first mention of an engagement or a price is at roughly 80% scroll depth. | Transparent pricing is the studio's sharpest differentiator, and it's nearly hidden. |
| Headline | "Layer One builds and scales design systems for product companies." | It describes the studio, not the buyer's problem or the outcome. Any competitor could say it. |
| Hero media | A 46-second video that opens on a dark, nearly empty frame. | The first impression is a mostly black box. The value sits 20 seconds in, and it's passive. |
| Narrative | Statement → video → logos → work → experience → offer → rules → writing → email. | No problem, no explanation of what a design system engagement is, no objections handled. |
| Calls to action | Five different ones ("Book a call", "See pricing", "View all work", "Read it all", an email link), none dominant. | No clear next step. The primary action is a small white pill in the nav. |
| Proof | Strong, real numbers exist but sit in three small cards far down the page. | The best evidence isn't where the doubt is. |
| Depth | Nine free tools and 51 guides get four thumbnail cards. | The clearest evidence of expertise is treated as a footer item. |
| Trust | No founder on the page, no FAQ, no answer to "you're new, why you?". | The biggest objection goes unanswered. |
| Visual identity | A competent adaptation of one reference studio's layout: sidebar, 44px maximum type, flat frames. | Tidy, but it reads as a template. Nothing on it could only be Layer One's. |
| Type and hierarchy | Six sizes between 14 and 44px; every section label looks the same. | No moment of emphasis, so no rhythm. |
| Motion | The video, plus hover states. | Nothing responds to the visitor. |
| Mobile | The sidebar disappears, leaving a 9,500px stack of frames. | The phone experience is the desktop one with pieces removed. |
| Performance | The hero video is 3.2–4.1 MB. | Heavy for what it adds on a phone connection. |

**The underlying problem:** the page shows that the work is good, but never tells a buyer what their problem is, what Layer One would do about it, what it costs, or what to do next.

---

## 3. The new structure, and the job of each section

A visitor's questions, in the order they ask them:

| # | Section | The question it answers | Proof or action placed here |
|---|---|---|---|
| 1 | Hero | "Is this for me?" | Primary CTA, price anchor, three employer logos |
| 2 | Numbers | "Have they done this at real scale?" | Four counted figures, with an honest source line |
| 3 | The problem | "Do they understand my situation?" | Three symptoms that resolve on screen |
| 4 | Four layers | "What would they actually build?" | The method, as an interactive stack |
| 5 | Work, by problem | "Has it worked for someone like me?" | Four case studies, each tagged with the problem it solved |
| 6 | Engagements | "What does it cost, and how do I start?" | Three prices, a founding-partner toggle, three CTAs |
| 7 | Ten rules | "What do they believe?" | Point of view, as a band of moving type |
| 8 | Tools and guides | "Can I check their thinking myself?" | A working contrast checker on the page |
| 9 | Founder | "Who will I be working with?" | A face, a history, the "small on purpose" line |
| 10 | Questions | "What's the catch?" | Seven objections, including "you're new" |
| 11 | Start | "What happens if I click?" | Three steps, CTA, founding slots |

**What I removed:** seven of the eleven project frames (they live on `/work`), the sidebar, the hero video, the three experience cards (merged into the numbers and the founder section) and the writing thumbnails (replaced by a list that loads no images).

The page is about 40% taller on desktop than the current one (about 14,900px against 10,468px). That's intended:
- Roughly 2,500px of it is the pinned four-layer story, which is one screen of content.
- The rest is content the old page didn't have: the problem, prices, the founder and the questions.

---

## 4. Messaging

**Headline: "Your product has five blues. It should have one."**
- It names a symptom every product leader has seen in their own codebase.
- It needs no knowledge of what a design system is.
- It implies the outcome.
- It gives the hero its visual: five mismatched blue chips, one accent chip.
- It's also Layer One's own material: the CARS24 case study is literally about this.

| Old | New | Why |
|---|---|---|
| "Layer One builds and scales design systems for product companies." | "Your product has five blues. It should have one." | Starts with the buyer's problem, not the seller. |
| "We set up the foundations, scale them across products and markets…" | "…tokens, components and the rules that keep them in use. In your Figma and your repo, at a fixed price. Foundations take six weeks." | Says what, where, how much risk and how long, in one breath. |
| "select work:" | "Find your problem. See how it was solved." | Turns a gallery into a self-diagnosis. |
| "how to start:" | "Three ways in. Every price on the page." | Makes the differentiator the headline. |
| "Where to reach out?" | "Count your blues. It takes two weeks." | Closes the loop from the hero and sells the smallest first step. |
| (none) | "Design debt doesn't announce itself. It shows up like this." | Names the problem before the solution. |
| (none) | "A design system has four layers. Most teams only build one." | Reframes the purchase: it isn't components. |
| (none) | "You're a new studio. Why should we trust you?" | Takes the biggest objection head-on. |

**Voice rules I kept from the existing guide:**
- plain, specific and confident
- numbers over adjectives
- none of the banned words (the guide bans "world-class", "transform", "seamless" and similar)

**Honesty rules I kept:**
- Every number on the page comes from the live site.
- Employee work is labelled as employee work, in two places.
- There are no testimonials, because none exist yet.

---

## 5. Visual direction: "the page is the system"

The idea is that the landing page should demonstrate the product. Three decisions follow from it.

1. **Tokens you can touch.** The whole page is styled from a small set of semantic tokens. In the hero, the visitor can change `--color-accent`. Every button, tag, chart and the footer wordmark re-themes at once. That's the pitch, experienced instead of explained.
2. **Layers, literally.** Each section is a "sheet" with rounded top corners that slides over the one before it, alternating ink, raised ink, paper and one full-bleed accent sheet. The page is built from layers, like the name and like the product. No gradients, glass or drop shadows are used for decoration.
3. **Spec-sheet details.** Mono labels, token names, a faint construction grid and annotation dots: the visual language of a design handoff, used as texture.

**Type.** The same two families as production (Schibsted Grotesk, JetBrains Mono), so it's still recognisably Layer One. The range is much wider: display type up to 104px against the current 44px maximum, on a fluid scale. Headlines use a two-tone device: the statement in full colour, the turn of thought in muted grey.

**Colour.** The existing ink, paper and signal-orange palette, unchanged. Orange appears only where something is actionable or resolved.

---

## 6. Motion and interaction

Every animation shows a state change that means something. Nothing loops for decoration except the rules band, which pauses on hover and focus.

| Interaction | What it communicates |
|---|---|
| Hero board: a checkout screen with 11 mismatched styles snaps into three tokens, about two seconds after load. A Drift / System toggle replays it. | The before and after of the product, in two seconds, with no reading. |
| Headline lines rise in sequence; five blue chips grow in, then one accent chip. | Sets reading order and lands the headline's point. |
| Accent token picker | "Change one token, change everything": the core promise, made tangible. |
| Numbers count up once when they scroll into view. | Draws the eye to proof without shouting. |
| Symptom cards resolve as they scroll into view: five swatches merge, three calendars become one, a queue re-ranks, and each title is struck through. Tap to toggle. | Problem to solution, per symptom. |
| Four layers: a pinned scroll story on desktop. An isometric stack opens up as you arrive, and each layer lifts and lights as its text expands. Click a layer to jump. | Explains the method spatially. Tokens are literally layer one. |
| Case cards: the image eases in scale and an arrow badge appears. | Signals that the whole card is a link. |
| Timeline bar fills 2 weeks → 6 weeks → monthly. | Shows the engagement model as time. |
| Founding-partner toggle swaps the three prices. | Makes the offer concrete. |
| Live contrast checker | A real tool, working on the page: capability shown, not claimed. |
| Footer wordmark's outline layers spread as it scrolls in. | A closing brand moment built from the layers idea. |
| Scroll progress hairline in the nav | Orientation on a long page. |

**Restraint:**
- no scroll-jacking outside the one pinned section
- no custom cursor
- no autoplaying video
- no parallax on text
- pointer parallax on the hero board is limited to a few pixels, on fine pointers only

---

## 7. Responsive behaviour and accessibility

Designed per size, not shrunk. Checked at 1920, 1440, 1280, 1024, 768, 390 and 320px wide.

| Size | What changes |
|---|---|
| ≥ 1800px | Wider container (1520px) and a larger hero board. |
| 961–1799px | The full layout: two-column hero, pinned layer story, 2×2 cases, three plans side by side. |
| ≤ 960px (tablet) | The nav collapses to a Menu button. The hero stacks with the board below the calls to action. The layer story stops pinning: heading, then the stack, then all four layers open, with the layer nearest the middle of the screen lit. Foundations moves to the top of the plans. |
| ≤ 680px (phone) | Single column throughout. Numbers in a 2×2 grid. Full-width primary button. Case cards show their arrow permanently, because there's no hover. A sticky bar ("Audit from $1,500 · Book a call") appears after the hero and hides over the final section. |
| ≤ 380px | Tighter nav and numbers. No sideways scroll at 320px. |

**Accessibility**
- **Structure:** one `h1`, headings in order, landmarks, a skip link as the first tab stop.
- **Keyboard:** visible focus on every surface. The phone menu takes focus, closes on Escape and is inert when closed.
- **Controls:** every control is a real `button`, `a`, `input` or `details`. Toggles expose `aria-pressed`, and the steps expose `aria-expanded`.
- **Reduced motion:** nothing animates. The board starts resolved, counters show final values, the layer story is unpinned and fully open, and the marquee becomes a static wrapped list.
- **Without JavaScript:** all content is visible. Reveal animations are opt-in through a `.js` class.
- **Decoration:** decorative visuals are `aria-hidden`. The hero board has a text alternative.
- **Contrast:** the four accent options were chosen so ink text passes on each of them.

---

## 8. Technical notes

- **Stack:** plain HTML, CSS and about 200 lines of dependency-free JavaScript. That matches the production site, which is a static build with no framework, so the prototype can be ported into `tools/build/home.py` without new tooling.
- **Isolation:** everything is in `prototype/landing-v2/` on the branch `prototype/landing-v2`. No production page, stylesheet, script or build step references it, and `main` is untouched.
- **Assets:** the page reuses the production fonts, logos, covers (existing WebP variants) and founder photo, by relative path. `build_standalone.py` inlines them into the single file.

**Weight**

| | Current home page | Prototype (served as separate files) |
|---|---|---|
| Above the fold | Hero video, 3.2–4.1 MB, plus poster | No images at all: the hero is HTML and CSS. One 47 KB font. |
| CSS + JS | Shared site stylesheet (about 49 KB gzipped) plus `site.js` | About 15 KB gzipped in total |
| Images | 21 | 14, about 250 KB in total; the 8 photographs lazy-load below the fold |

The standalone file is 541 KB because the images are embedded as text.

**Performance choices**
- Only `transform` and `opacity` animate, apart from a handful of small elements in the hero board.
- One `requestAnimationFrame`-throttled scroll handler.
- `IntersectionObserver` drives reveals and counters.
- No layout work in the scroll path beyond three `getBoundingClientRect` reads.

**SEO**
- A descriptive title and meta description.
- `ProfessionalService` structured data carrying the three offers.
- Semantic headings that carry the search-relevant phrases.
- The prototype itself is marked `noindex`; remove that when it ships.

**Verified**
- No console errors and no sideways scroll at the seven widths above.
- All 14 images load from the single file.
- 14 automated checks pass: the board resolving, the Drift toggle, the token picker, prices, pinned layers, the contrast tool, the skip link, links, heading structure, reduced motion, the phone menu, Escape, the sticky bar and no-JavaScript.
- I checked the layouts by screenshot at desktop, tablet and phone sizes.

---

## 9. Assumptions, gaps and what I need from you

| Item | What I assumed | What would improve it |
|---|---|---|
| Positioning | A design-systems specialist, not a general product design partner. | Tell me if you do want to sell broader product design; the hero and the layers section would change. |
| Testimonials | None exist, so none are shown. | Even one real quote from a former colleague or manager at CARS24, IBM or JPMorgan Chase would go beside the numbers. |
| Team size | The page says Aniket leads every engagement himself. The live site also says "a senior team". | Confirm who else works on engagements, so the founder section is accurate. |
| "200+ engineers and 70+ designers" at CARS24 | Taken from the home and experience pages. The studio page says "60+ designers and 100+ engineers". | Confirm which is right, and fix the other on the live site. |
| "65% faster design handoff" | Taken from the experience page. | Confirm it can be stated on the home page without more context. |
| Founder photo | The existing 4:5 crop, shown in greyscale. | A higher-resolution portrait would hold up better at this size. |
| Hero reel | Removed from the hero. | It could return as a "watch the 45-second version" link in the work section. |
| Booking link | `cal.com/layerone`, as on the live site. | Confirm it's current. |
| Analytics | None in the prototype. | When it ships, track clicks on each CTA separately so we can see which section converts. |
| Reference sites | Direction comes from my own knowledge of studio sites and the patterns above. | If there are specific sites you admire, name them and I'll compare. |
| Light theme | The page is dark-led with paper sections; no separate light mode. | Not needed, in my view. |

---

## 10. If you want to ship it

1. Port `index.html` into `tools/build/home.py`, with the copy as data, as the other builders do.
2. Move `styles.css` into a `home.css` built the same way as `lab.css` and `writing.css`.
3. Decide the fate of the hero reel and the old sidebar on the other listing pages. They would look dated next to this.
4. Remove `noindex` and the "Prototype" badge.
5. Add per-CTA analytics events.
6. Test on real devices: iOS Safari and Android Chrome at least.
