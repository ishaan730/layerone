# Layer One website

The website for Layer One, a design systems studio. Plain static HTML, CSS and JavaScript: no framework, no runtime dependencies, deployed on Vercel from the repo root.

## Pages

| Page | What it is |
|---|---|
| `index.html` | Home: positioning, "where is your system today?", selected work, services, engagement and pricing, beliefs, studio, writing, FAQ |
| `work.html` | Work index |
| `work/cars24-tokens.html` | Case study: colour and token system (foundations) |
| `work/cars24-governance.html` | Case study: governance and contribution (operations), with a working request scorecard |
| `work/cars24-pattern-library.html` | Case study: pattern library (adoption) |
| `services.html` | Services in detail: Systems, Operations, Adoption |
| `blog.html`, `blog-librarian-vs-leader.html` | Writing index and one article |

## Assets

```
assets/
├── site.css        all styles; tokens are layered primitive → semantic → component, light and dark
├── site.js         theme switch, mobile menu, hero layer stack, tabs, case study contents, scorecard
├── fonts/          Schibsted Grotesk and JetBrains Mono, self-hosted (SIL Open Font License)
├── favicon.svg
├── studio/         founder portrait
├── work/           case study images, grouped by case study
└── images/         older images (logo, blog art, previous work thumbnails)
```

## Editing

- **Copy:** edit the HTML directly, or edit the generator (below) and rebuild.
- **Colours, type, spacing:** primitives and semantic tokens are at the top of `assets/site.css`. Dark mode overrides the semantic layer only.
- **Project numbers:** every page quotes the same figures from the `CASES` dictionary in `tools/build/common.py`, so change them there.

## Adding a case study

The pages are generated once by small Python scripts in `tools/build/` so that the header, footer and case study layout stay identical everywhere. The output is plain HTML, so the site still deploys with no build step.

1. Put the images in `assets/work/<name>/` (around 1800px wide, JPEG).
2. Add an entry to `CASES` in `tools/build/common.py` and to `ORDER` in `tools/build/cs.py`.
3. Copy `tools/build/cs_tokens.py` to `cs_<name>.py` and write the sections.
4. Add the new script to `tools/build/build_all.py` and run:

```bash
pip install pillow
python3 tools/build/build_all.py
```

`blog-librarian-vs-leader.html` is hand-written and isn't touched by the build.

## Run it locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

`tools/` and this README are excluded from the deployment by `.vercelignore`.
