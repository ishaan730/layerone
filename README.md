# Layer One website

The website for Layer One, a design systems studio. Plain static HTML, CSS and JavaScript: no framework, no runtime dependencies, deployed on Vercel from the repo root.

## Pages

Direction for every page lives in `.claude/skills/layer-one-site/SKILL.md` (Hex analysis, palette, offer, voice, honesty rules). Read it before changing anything.

| Page | What it is |
|---|---|
| `index.html` | Home: statement, hero reel video, logos, work, experience, offer, rules, writing |
| `work.html` | All work |
| `work/cars24-*.html` | Three interactive case studies |
| `work/jpmc-*.html`, `work/ibm-*.html`, `work/cars24-consumer.html`, `work/cars24-internal-tools.html` | Short project pages |
| `clients.html` | Experience: CARS24, IBM, JPMorgan Chase |
| `studio.html` | About the studio and founder |
| `pricing.html` | Pricing (`services.html` redirects here) |
| `lab.html` | Free tools: OKLCH ramp builder, token chain, request scorecard |
| `blog.html`, `blog-librarian-vs-leader.html` | Writing |
| `contact.html` | Project enquiry (validated form that opens an email draft) |

## Assets

```
assets/
├── site.css        all styles; tokens layered primitive → semantic; dark listing pages, light case studies
├── site.js         menu, hero reel controls, case study modules, pricing toggle and plan finder, Lab tools, contact form
├── video/          hero reel (webm, mp4) and poster
├── logos/          CARS24, IBM, JPMorgan Chase tiles
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

## Re-rendering the hero video and covers

With the site served on port 8765 (`python3 -m http.server 8765`):

```bash
python3 tools/video/render.py      # assets/video/hero-reel.mp4, .webm and poster (needs ffmpeg + playwright)
python3 tools/covers/render.py     # illustrated covers for IBM and JPMorgan Chase projects
```

## Run it locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

`tools/` and this README are excluded from the deployment by `.vercelignore`.
