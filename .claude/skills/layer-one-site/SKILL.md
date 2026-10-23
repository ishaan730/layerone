---
name: layer-one-site
description: Direction for the Layer One website (design systems studio). Use before changing any page, adding a project or case study, or writing copy for layerone.co.in. Captures the Hex-derived visual system, page inventory, offer and voice.
---

# Layer One website: direction

Layer One is a design systems studio based in Bangalore, India, led by Aniket Pandey. The site exists to win the studio's first clients. Every page must make two things obvious within seconds:

1. Layer One only does design systems: building them, scaling them, governing them, and getting teams to adopt them.
2. The proof is real: shipped systems at CARS24, IBM, JPMorgan Chase, Riyadh Air and others, shown with images and numbers.

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

- **Palette:** background `--ink #0B0D12` (graphite with a blue cast), raised `#13161D`, text `#ECECE8`, muted `#9AA0AA`, light card `#ECECE8` with ink text, accent `--signal #FF6B3D` (signal orange, a spec-annotation colour). Case study pages use the light theme `#F6F6F3`.
- **Type:** Schibsted Grotesk (self-hosted), weights 400–600, scale 14/16/20/24/32/44. JetBrains Mono only for literal token names and code.
- **Wordmark artwork:** "Layer One" set large in the accent with offset outline copies stacked behind it (layers), plus the star mark.
- **Hero media:** an animated isometric stack of the four token layers (value, primitive, semantic, component) whose brand colour cycles through real client palettes. This is the studio's signature visual; keep it.
- **Frames:** every project gets a frame colour taken from its own work (CARS24 `#4736FE`, Riyadh Air purple, District purple, pharma red, etc.).
- **Radius** 8px on media and cards, 999px on pill buttons. No shadows.

## Page inventory

| Page | Hex equivalent | Contents |
|---|---|---|
| `index.html` | Home | Hero statement + layer-stack media, company strip, "selected work:" frames, client blurbs, "rules", writings, where to reach out |
| `work.html` | /work | Sidebar sub-nav (Case studies, Projects), all frames with years |
| `work/<slug>.html` | /work/<slug> | Light theme case study: title, hero, intro, scope table, gallery + short text, results, credits, more work |
| `clients.html` | /clients | Companies the team has built systems for: name, sector, one line on the work |
| `studio.html` | /info | About: statement, story (Bangalore), founder, what we do (numbered rows), how we work, rules, founding partners invitation, our work link rows |
| `services.html` | Info → Services/Pricing | Engagements with price, duration, deliverables; process; FAQ |
| `lab.html` | Web Work / Swipe File | Interactive tools that prove craft: token layer explorer, OKLCH ramp builder, request scorecard |
| `blog.html` + articles | /writings | 2-up cards |
| `contact.html` | /contact | Email, call link, what to send |

## The offer (owner's decisions, October 2026)

Specialist studios lead with a fixed-price audit, then a foundations build, then long-term partnership and training (Baseline: systems / strategy / training; Sparkbox: strategy, delivery, organisational readiness; Ariel Salminen: audits from €10k). Layer One is new, so the entry offer is priced to start relationships:

| Engagement | Duration | Price |
|---|---|---|
| System Audit | 2 weeks, fixed | $3,500 |
| Foundations Build | 6–8 weeks | from $14,000 |
| System Partner | monthly, pause any time | from $4,900 / month |
| Workshops | half-day sessions | from $1,200 |

**Founding partners:** three slots in 2027 at 20% off any engagement, in exchange for a jointly published case study. This is how the studio earns its first studio case studies; mention it on Home (sidebar card), Services and Studio.

## Voice

- Plain, specific, confident. Say what the system is and what changed, with numbers.
- Never: "transform", "elevate", "extraordinary", "seamless", "unlock", "world-class".
- Sentence case. Lowercase section labels with a colon are allowed (Hex habit): "selected work:".
- Project titles follow "Client: what we did" ("CARS24: one colour system for 10+ products in three countries").

## Honesty rules (non-negotiable)

- The CARS24, IBM and JPMorgan work was done by the founder as an employee. Pages say "Led by Aniket Pandey as Design Systems Lead at CARS24" (or similar). Never call these Layer One client engagements.
- No testimonials until real quotes exist. No invented metrics. Projects without a full write-up say "Full case study on request" and only state known facts.
- Don't show JPMorgan Chase project imagery (current employer).

## Adding a project

1. Images to `assets/work/<slug>/` (≤1800px wide JPEG).
2. Add the project to `PROJECTS` in `tools/build/common.py` with frame colour, year, tags, title and cover.
3. For a full case study, copy `tools/build/cs_tokens.py` and write sections; otherwise the build makes a short project page from the PROJECTS entry.
4. `python3 tools/build/build_all.py`, then check desktop and 390px mobile.
