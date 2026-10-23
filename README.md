# Layer One website

The website for Layer One, a design systems studio. Plain static HTML, CSS and JavaScript: no framework, no runtime dependencies, deployed on Vercel from the repo root.

## Pages

Direction for every page lives in `.claude/skills/layer-one-site/SKILL.md` (Hex analysis, palette, offer, voice, honesty rules). Read it before changing anything.

| Page | What it is |
|---|---|
| `index.html` | Home: banner, statement, animated token-layer stage, select work frames, where we've built systems, how to start, rules, writing |
| `work.html` | All work: featured case studies and more projects |
| `work/cars24-*.html` | Three full case studies (light theme) |
| `work/riyadh-air.html` and four others | Short project pages |
| `clients.html` | Companies the team has built systems for |
| `studio.html` | About: story, founder, what we do, how we work, founding partners invitation |
| `services.html` | Engagements and pricing, founding partners, process, FAQ |
| `lab.html` | Free tools: OKLCH ramp builder, token chain, request scorecard |
| `blog.html`, `blog-librarian-vs-leader.html` | Writing |
| `contact.html` | Project enquiry (opens an email draft) |

## Assets

```
assets/
├── site.css        all styles; tokens layered primitive → semantic; dark listing pages, light case studies
├── site.js         mobile menu, hero stage, Lab tools (OKLCH ramp, token chain, scorecard), contact form
├── fonts/          Schibsted Grotesk and JetBrains Mono, self-hosted (SIL Open Font License)
├── favicon.svg
├── studio/         founder portrait
├── work/           case study images, grouped by case study
└── images/         older images (logo, blog art, previous work thumbnails)
```

## Editing

- **Copy:** edit the HTML directly, or edit the generator (below) and rebuild.
- **Colours, type, spacing:** primitives and semantic tokens are at the top of `assets/site.css`. Dark mode overrides the semantic layer only.
- **Projects:** titles, colours, covers and blurbs come from `PROJECTS` in `tools/build/common.py`.

## Adding a case study

The pages are generated once by small Python scripts in `tools/build/` so that the header, footer and case study layout stay identical everywhere. The output is plain HTML, so the site still deploys with no build step.

1. Put the images in `assets/work/<name>/` (around 1800px wide, JPEG).
2. Add an entry to `PROJECTS` in `tools/build/common.py`. With `case=False` it gets a short project page automatically; for a full case study set `case=True`, copy `tools/build/cs_tokens.py` to `cs_<name>.py`, add its slug to `KEY` in `cs.py` and add the script to `build_all.py`.
3. Run:

```bash
pip install pillow
python3 tools/build/build_all.py
```

The article text lives in `tools/build/content/`.

## Run it locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

`tools/` and this README are excluded from the deployment by `.vercelignore`.
