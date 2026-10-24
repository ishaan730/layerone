---
name: layer-one-site
description: Direction for the Layer One website (design systems studio). Use before changing any page, adding a project or case study, or writing copy for layerone.co.in. Captures the Hex-derived visual system, page inventory, offer and voice.
---

# Layer One website: direction

Layer One is a design systems studio based in Bangalore, India, led by Aniket Pandey. The site exists to win the studio's first clients. Every page must make two things obvious within seconds:

1. Layer One only does design systems: building them, scaling them, governing them, and getting teams to adopt them.
2. The proof is real: shipped systems at CARS24, IBM and JPMorgan Chase, shown with images and numbers.

## The two references, and what each is for

- **Hex (hex.inc) → everything visual and structural.** Layout, page types, navigation, imagery, type, interaction, how work is presented.
- **Baseline (baselinedesign.com) → strategy only.** How a specialist studio packages services, entry offers and training. Never borrow Baseline's layout or look.

## Hex, analysed (October 2026)

Studied in a live browser across home, /work, /work/grafana, /clients, /info and /writings.

**Shell**
- Dark theme on every listing page: background `#031B1D` (near-black teal), text `#EBEBEB`, one accent `#21FFBC` (mint) used for the wordmark, the first word of the headline and the primary CTA fill.
- Top bar: small logo left, centred text nav (Home, Work, Clients, Info, Web Work, Swipe File, Writings, /Rejected), one white pill button right ("Get in touch").
- Fixed left sidebar (~300px) on desktop: a section sub-nav at top (changes per page: Featured / Web Work / Archive on Work; Overview / Services / Clients / ... on Info), a contact card in the middle (animated media + "Get in touch →", or a filled accent bar on inner listing pages), then a one-line studio description ("... Led by Ayush Soni."), a huge custom wordmark artwork in the accent colour, and a row of socials + email at the bottom.
- Content column on the right, about 900px wide, 16px gutters.

**Type**
- One grotesk family (Lausanne) for everything. Weights 300 (card titles), 400 (body and headings), 500/700 rarely.
- Scale is modest: 14 / 16 / 20 / 24 / 32 / 40px. The biggest headline on the homepage is 40px. Letter-spacing -0.4px on headings. Lowercase section labels ("select case studies:", "featured work", "writings").
- The drama comes from imagery, not type size.

**Project frames (the core component)**
- A full-width card whose background is the project's own colour (white, electric blue, sky blue, yellow, cyan, green...). 15px of frame around a large media panel (looping video / animation, 8px radius, roughly 16:9).
- Under the media: one-line title in sentence case, "Client: what we did" style, 24px weight 300; then a 14px category tag line ("Brand, Strategy"). On /work the date sits right-aligned on the tag line.
- Text colour flips to suit the frame colour. Frames stack vertically with ~16px gaps. 20+ of them on the homepage. A light "View More Work" bar ends the list.

**Other recurring components**
- Logo strip: two rows of client wordmarks in the accent tint.
- Client blurbs: 3-column grid, logo + one sentence ("We partnered with X to...").
- Clients page: 3-column grid of logo, funding stage in bold, one-line description of the company.
- "Laws": a stack of light `#EBEBEB` rows, statement left, "LAW #n" right, 8px radius.
- Writings: 2-up light cards with media, title, tag.
- Info page: statement headline + wide banner artwork, a paragraph about how they think, Services as outlined numbered rows (01–13), Select Clients, Features (press links as outlined rows), Invitation (a hiring poster), Our Work (centred link bars), Client Notes (big quote cards with logo, quote, headshot, name and role), Pricing.
- Case study page switches to a LIGHT theme (`#FAFAFA`), no sidebar, centred ~1000px column: title (32px), hero media, two short paragraphs, Press link, a bordered scope table (deliverable left, disciplines right), then a long gallery of full-width and 2-up media with 8px gaps, a showreel, Credits, "More Work" (2 cards) and stacked link rows (Web Work, Swipe File, Start a project).
- Closing is plain: "Where to reach out?" + email, plus a small looping artwork tile.

**Feel**: confident, terse, image-heavy, lots of work shown, very little marketing copy, playful details (/Rejected, swipe file), everything rounded at 8px.

## How Layer One adapts it (do not copy Hex's colours, artwork or copy)

- **Palette:** background `--ink #0B0D12` (graphite with a blue cast), raised `#13161D`, text `#ECECE8`, muted `#9AA0AA`, light card `#ECECE8` with ink text, accent `--signal #FF6B3D` (signal orange, a spec-annotation colour). Every page is dark, case studies included.
- **Type:** Schibsted Grotesk (self-hosted), weights 400–600, scale 14/16/20/24/32/44. JetBrains Mono only for literal token names and code.
- **Wordmark artwork:** "Layer One" set large in the accent with offset outline copies stacked behind it (layers), plus the star mark.
- **Hero media:** the hero reel video (see Founder's decisions).
- **Frames:** every project gets a frame colour taken from its own work (CARS24 `#4736FE`, JPMorgan Chase brown `#8A5434`, IBM blue `#0F62FE`).
- **Radius** 8px on media and cards, 999px on pill buttons. No shadows.

## Founder's decisions (24 October 2026)

- **Only three companies appear anywhere:** CARS24, IBM, JPMorgan Chase. Use the logo tiles in `assets/logos/` wherever a company is named (`logo_tile()` in `tools/build/common.py`). Riyadh Air, District/Zomato, HDFC and the pharma project were removed: that work was done by other designers and can't be claimed.
- **Hero is a video**, not a static or random visual: `assets/video/hero-reel.{webm,mp4}`, a 24-second cinematic recap of the real projects (token-layer intro → CARS24 old-to-new blue → campaign → colour montage → governance → pattern library → component systems → IBM and JPMorgan → end card with the three logos). It autoplays muted, loops, pauses off-screen and for reduced motion, and has a pause button. Source: `tools/video/hero.html`; render with `tools/video/render.py`.
- **Case studies must be interactive and scannable**, not long scrolls copied from Hex: sticky chapter bar with progress, a 30-second summary, count-up KPIs, one interactive or visual module per chapter (before/after slider, animated bars, stepper, calculator, live demo), long text folded into "Read the detail", gallery with lightbox. Engine: `tools/build/cs.py`.
- **Pricing stays affordable**, around $5–6k for the main build. The pricing page is the most important conversion page.
- **IBM and JPMorgan imagery:** the portfolio's images for these were placeholders, so project covers are drawn illustrations (`tools/covers/covers.html`), always labelled "Illustration".

## Page inventory

| Page | Contents |
|---|---|
| `index.html` | Statement, hero reel, logo row, select work frames, three experience cards, how to start, rules, writing, reach out |
| `work.html` | Featured case studies and more projects |
| `work/cars24-*.html` | Three interactive case studies (dark, chaptered) |
| `work/jpmc-*.html`, `work/ibm-*.html`, `work/cars24-consumer.html`, `work/cars24-internal-tools.html` | Short project pages |
| `clients.html` (nav: Experience) | CARS24, IBM, JPMorgan Chase with logos, facts and linked projects |
| `studio.html` | About: story (Bangalore), founder, what we do, how we work, founding partners invitation |
| `pricing.html` | Pricing (services.html redirects here) |
| `lab.html` | OKLCH ramp builder, token chain, request scorecard |
| `blog.html` + articles | Writing |
| `contact.html` | Enquiry form (choice cards and chips, validated, opens an email draft), founder card, what happens next |

## The offer

| Engagement | Duration | Price | Founding partner (−20%) |
|---|---|---|---|
| Audit | 2 weeks, fixed | $1,500 | $1,200 |
| Foundations (recommended) | 6 weeks, fixed | $5,900 | $4,720 |
| Partner | monthly, pause any time | $2,900 / month | $2,320 / month |
| Add-ons | Workshop $450 / half day · Extra theme $900 · Component pack (6) $1,500 | | |

Terms: Audit fee credited in full against Foundations within 60 days. Foundations 50% to start, 50% on handover. Partner billed monthly in advance. USD invoices.

Pricing page structure: standard / founding-partner toggle → three tier cards (Foundations highlighted) → every engagement includes → comparison table → three-question plan finder → founding partners → add-ons → logos and promises → pricing FAQ → final CTA.

**Founding partners:** three slots in 2027 at 20% off, in exchange for a jointly published case study.

## Voice

- Plain, specific, confident. Say what the system is and what changed, with numbers.
- Never: "transform", "elevate", "extraordinary", "seamless", "unlock", "world-class".
- Sentence case. Lowercase section labels with a colon are allowed (Hex habit): "selected work:".
- Project titles follow "Client: what we did".

## Honesty rules (non-negotiable)

- The CARS24, IBM and JPMorgan Chase work was done by the founder as an employee. Say so on work, experience and case study pages. Never call it Layer One client work.
- No testimonials until real quotes exist. No invented metrics. Illustrative numbers (like the scorecard queue) are labelled as illustrative.
- Drawn covers are labelled "Illustration". Don't present placeholders as real screens.

## Adding a project

1. Images to `assets/work/<slug>/` (≤1800px wide JPEG), or draw a cover in `tools/covers/covers.html` and render it.
2. Add it to `PROJECTS` in `tools/build/common.py` (company key, frame colour, year, kind, title, cover, blurb, points, scope).
3. For a full case study set `case=True`, copy `tools/build/cs_tokens.py`, add the slug to `KEY` in `cs.py` and the script to `build_all.py`.
4. If it should appear in the hero, add a scene to `tools/video/hero.html` and re-render.
5. `python3 tools/build/build_all.py`, then check 1440px and 390px.
