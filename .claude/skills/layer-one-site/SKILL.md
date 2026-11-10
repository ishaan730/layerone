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
- **Update, 1 November 2026: IBM client projects.** Cardinal Health (Jarvis) and Riyadh Air (design system, and design operations) are back as three full case studies, copied from the founder's portfolio: `work/ibm-cardinal-health.html`, `work/ibm-riyadh-air.html`, `work/ibm-riyadh-air-ops.html` (`cs_cardinal.py`, `cs_riyadh.py`, `cs_riyadh_ops.py`). They are IBM client work: always shown under the IBM logo, client written as "IBM × Cardinal Health" / "IBM × Riyadh Air", credited as employee work. Frame colours: Cardinal red `#E41F35`, Riyadh Air indigo `#240852`, lavender `#DAD8FC`. The employers are still only CARS24, IBM and JPMorgan Chase.
- **Showcase case studies (1 November 2026).** The IBM client case studies use a visual-first engine, `tools/build/showcase.py`, not `cs.py`: a brand-colour hero with proof numbers and the cover, a sticky chapter bar, then short sections (a one-line header plus one big visual each) in three modes, dark, `stage` (the project's colour) and `paper` (light). Building blocks: `carousel` (the work reel, swipe and arrow keys), `bento` (image grids), live component specimens rebuilt in code with the client's real values, `rail`, `nums`, `inventory`, `outcomes`, `lessons` and `playbook` (maps the case study to Audit / Foundations / Partner with prices). Copy: a headline of 8 words or fewer and one sentence per section; numbers and visuals carry the rest. Their covers are drawn at 1920 × 1080, the frame's exact 16:9, on the frame colour so they blend with the frame: `tools/covers/showcase.html`, rendered with `node tools/covers/render_showcase.js` while the repo root is served on :8765 (`python3 tools/serve.py`). Styles live under "Showcase case study (v4)" in `assets/site.css`.
- **CARS24 internal tools (3 November 2026).** `work/cars24-internal-tools.html` (`cs_internal.py`, showcase engine): the design system for CARS24's 30+ internal tools, from the "CARS24 Internal Tool DLS" Figma file (it shares the LEGO name with the consumer system). Facts from the founder: 30+ tools, 100+ designers and engineers, 20+ tools audited, a squad of 8 engineers, 2 engineering maintainers, 1 system designer, a 3–4 month runway to a beta for leadership, Storybook, a contribution model, well received by engineering and leadership. Facts from Figma: 93 component sets, 1,205 variants, 100+ tokens, Tailwind-scale primitives, brand `denim-600 #5546FF`. Frame colour mint `#63FFB1` (from the system's own cover artwork) with ink text. Live modules: surface role × state picker (`data-surf`), Storybook recreation (`data-sb`), data table (`data-dt`); styles under "CARS24 internal tools" in `assets/site.css`. The timeline is labelled approximate, the table data as made up. The cover is the `internal` scene in `tools/covers/showcase.html`.
- **Lab v2 (3 November 2026).** `lab.html` is a full-width workspace (no sidebar) with seven tabbed tools: palette (OKLCH ramps from a brand hex, exact colour pinned to the nearest step, sRGB or P3, light and dark UI preview), contrast (WCAG 2 and APCA, nearest passing colour in the same hue, pair matrix), type scale, spacing and radius, token name linter (with fixes), request backlog (the 70-point scorecard, ranked, CSV/Markdown/JSON) and an export kit (CSS, Tailwind, DTCG JSON, SCSS). State saves to localStorage and shares as a `#s=` link. Built by `tools/build/lab.py`; behaviour in `assets/lab.js`, loaded only on that page; styles under "Lab (v2)" in `assets/site.css`.
- **Writing is an editorial section on the site grid (13 November 2026).** `/writing`, its articles and topic pages use the site's top bar and the same outer container as `.topbar-in` (`page()` in `writing.py`), so sections span from the logo's left edge to "Book a call"'s right edge. Library: two-column intro; featured as one lead story (image 7 columns, text 5) and two stories below with the same horizontal anatomy; latest articles with topic chips beside the heading that filter in place; reading paths two per row; topic index. Articles: three columns at 1200px and up (details 184px: author, date, reading time, topic, reading path, share · one content column that every paragraph, heading, figure, table and callout fills at 100% · a 200px sticky "On this page" rail); two columns from 1024px; one column with a sticky "On this page" bar below. Writing pages load `assets/writing.css`, built by `tools/build/purge_css.py` from `site.css` with only the rules those pages use (about 10 KB gzipped); always edit `site.css` and rebuild. Card images use explicit `sizes`, lazy-load below the fold and show the mark as a placeholder; only the lead image is high priority. Dark like the site; a light reading switch sits in the top bar (stored as `l1-read`).
- **Never use a thick one-sided stroke** (a coloured bar on one edge) on quotes, callouts, alerts, notes or cards. Use a full outline, a tint, a pill label or a quote mark instead.
- **Speed and clean URLs (5 November 2026).** Pages are served without `.html` (`/work/cars24-lego`); `clients.html` became `experience.html` and `blog.html` became `writing.html`, with redirects in `vercel.json`. Always link to pages through the builders (write `x.html` in source); `tools/build/optimize.py` rewrites links to clean paths, adds responsive WebP `srcset`s, canonical and share tags, and speculation rules. Preview locally with `python3 tools/serve.py` (port 8765). Images inside carousels, tabs and galleries must sit in a container the preloader in `site.js` watches (`warmSel`). The default share image is `assets/og/layer-one.jpg`; `404.html`, `sitemap.xml` and `robots.txt` come from `tools/build/extras.py`.
- **Hero is a video** (updated 3 November 2026), not a static or random visual: `assets/video/hero-reel.{webm,mp4}`, a 46-second reel told from a buyer's side, built from the real case study assets. It opens with the Layer One intro (the mark draws on its construction grid, “Layer One, a design systems studio”, a small pull-back, then the camera dives through the mark's dark cut-out) and closes with the mark drawing again above the end card, so the brand bookends the reel. No hard cuts between scenes: each scene is its own layer with a designed entrance (pushes for “next”, vertical pushes for “deeper”, irises that open where the eye already is, a wipe, a curtain, a zoom-through) while the scene underneath recedes (scales down, dims, brief motion blur); expo easing on transitions, a slight overshoot on pops, staggered entrances and a slow camera drift in every scene. Story: the problems a buyer recognises, struck through (five blues, three date pickers, one team for every request) → where the systems were built (JPMorgan Chase, IBM, CARS24; at IBM for Cardinal Health and Riyadh Air) with four counted numbers → CARS24 colour (five blues merge into one token, then the rebrand ramp, 65%) → CARS24 LEGO (before/after wipe, 44 components) → pattern library phones (~43%) → Cardinal Health Jarvis (storefront, a button pressed through its tokens, the 110-colour ramps) → Riyadh Air (Canopy Twist draws on, English light and Arabic dark phones, a watch) → governance (request to release with four gates, 70 pts, ~900 tickets, 3 companies) → JPMorgan Chase checks (labelled illustration) → an eight-shot montage of real work → how to start (Audit, Foundations, Partner with prices) → end card with all five logos and “Start with a two-week audit”. It autoplays muted, loops, pauses off-screen and for reduced motion, and has a pause button. Every number in it must match the case studies and the prices must match the pricing page. Source: `tools/video/hero.html`; render with `node tools/video/render.js` while the repo root is served on :8765 (`python3 tools/serve.py`) (`--preview 1.5,9.6` renders stills only).
- **Case studies must be interactive and scannable**, not long scrolls copied from Hex: sticky chapter bar with progress, a 30-second summary, count-up KPIs, one interactive or visual module per chapter (before/after slider, animated bars, stepper, calculator, live demo), long text folded into "Read the detail", gallery with lightbox. Engine: `tools/build/cs.py`.
- **Pricing stays affordable**, around $5–6k for the main build. The pricing page is the most important conversion page.
- **IBM and JPMorgan imagery:** the portfolio's images for these were placeholders, so project covers are drawn illustrations (`tools/covers/covers.html`), always labelled "Illustration".

## Page inventory

| Page | Contents |
|---|---|
| `index.html` | Statement, hero reel, logo row, select work frames, three experience cards, how to start, rules, writing, reach out |
| `work.html` | Featured case studies and more projects |
| `work/cars24-*.html`, `work/ibm-cardinal-health.html`, `work/ibm-riyadh-air*.html` | Eight interactive case studies (dark, chaptered) |
| `work/jpmc-*.html`, `work/ibm-design-systems.html` | Short project pages |
| `experience.html` at `/experience` (nav: Experience) | CARS24, IBM, JPMorgan Chase with logos, facts and linked projects |
| `studio.html` | About: story (Bangalore), founder, what we do, how we work, founding partners invitation |
| `pricing.html` | Pricing (services.html redirects here) |
| `lab.html` | Seven tools in one tabbed workspace: palette, contrast, type scale, spacing and radius, token name linter, request backlog, export kit (`lab.py`, `assets/lab.js`) |
| `writing.html` at `/writing`, `writing/<slug>.html`, `writing/topics/<topic>.html` | Writing library (`writing.py`): hub with start here, topics, five reading series, guides and archive; articles with an "On this page" sidebar, short answer, figures (`writing_figs.py`, data from the playbook), FAQ, author box, CTA and series navigation; Article and BreadcrumbList JSON-LD. `/blog-librarian-vs-leader` redirects to `/writing/librarian-vs-leader` |
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
