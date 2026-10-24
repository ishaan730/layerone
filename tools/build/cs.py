"""Case study engine (v3). Dark, chaptered, interactive.

page(key, spec) builds work/<slug>.html from a spec dict:
  h1, lede, meta [(label, value)], tldr [(title, text)] x3, kpis [(value, suffix, prefix, label)],
  chapters [(id, nav, title, lede, body_html)], gallery [(src, caption)], credits
Module helpers below return HTML strings for chapter bodies.
"""
from common import *
from PIL import Image
import html as _h

KEY = {"tokens": "cars24-tokens", "governance": "cars24-governance", "patterns": "cars24-pattern-library"}


def dims(src):
    w, h = Image.open(OUT + "/" + src).size
    return f'width="{w}" height="{h}"'


def img(src, alt="", cls="", lb=True, cap=None):
    lbattr = f' data-lightbox data-cap="{_h.escape(cap or alt)}"' if lb else ""
    return f'<img class="{cls}" src="../{src}" alt="{_h.escape(alt)}" {dims(src)} loading="lazy"{lbattr}>'


def fig(src, cap, alt=""):
    return f'<figure class="m-fig">{img(src, alt or cap, cap=cap)}<figcaption>{cap}</figcaption></figure>'


def pair(a, b, cap):
    return f'<figure class="m-fig"><div class="m-pair">{img(a[0], a[1], cap=cap)}{img(b[0], b[1], cap=cap)}</div><figcaption>{cap}</figcaption></figure>'


def more(*paras):
    """Long-form detail, folded away so the page stays scannable."""
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'<details class="m-more"><summary><span>Read the detail</span></summary><div class="prose">{body}</div></details>'


def lead(text):
    return f'<p class="m-lead">{text}</p>'


def tiles(items, cols=2):
    return f'<div class="m-tiles m-tiles--{cols}">' + "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in items) + "</div>"


def compare(before, after, labels=("Before", "After"), cap="", ratio="16 / 9", tall=False):
    """Drag-to-compare slider. before/after = (src, alt)."""
    cls = "m-compare m-compare--tall" if tall else "m-compare"
    return f'''<figure class="m-fig"><div class="{cls}" data-compare style="--pos:50%;aspect-ratio:{ratio}">
      <img src="../{after[0]}" alt="{after[1]}" loading="lazy" class="c-after">
      <div class="c-before"><img src="../{before[0]}" alt="{before[1]}" loading="lazy"></div>
      <span class="c-tag c-tag--l">{labels[0]}</span><span class="c-tag c-tag--r">{labels[1]}</span>
      <div class="c-handle" aria-hidden="true"><span></span></div>
      <input type="range" min="0" max="100" value="50" aria-label="Drag to compare {labels[0].lower()} and {labels[1].lower()}">
    </div>{f"<figcaption>{cap}</figcaption>" if cap else ""}</figure>'''


def bars(rows, cap="", unit=""):
    """Grouped before/after bars. rows = [(label, before, after, before_txt, after_txt)] scaled to the row max."""
    out = '<figure class="m-fig"><div class="m-bars" data-inview>'
    for label, b, a, bt, at in rows:
        mx = max(b, a)
        out += f'''<div class="br"><span class="br-l">{label}</span>
          <div class="br-track"><i class="b0" style="--w:{b / mx * 100:.1f}%"></i><em>{bt}</em></div>
          <div class="br-track"><i class="b1" style="--w:{a / mx * 100:.1f}%"></i><em>{at}</em></div></div>'''
    out += '<p class="br-key"><span class="k0">Before</span><span class="k1">After</span></p></div>'
    return out + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>"


def tabs(name, items):
    """Tabs with image + text. items = [(label, img_src, title, text)]"""
    t = "".join(f'<button role="tab" type="button" id="t-{name}-{i}" aria-controls="p-{name}-{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{lbl}</button>' for i, (lbl, *_r) in enumerate(items))
    p = ""
    for i, (lbl, src, title, text) in enumerate(items):
        p += f'''<div role="tabpanel" id="p-{name}-{i}" aria-labelledby="t-{name}-{i}"{"" if i == 0 else " hidden"} class="tp">
          <div class="tp-img">{img(src, title, cap=title)}</div><div class="tp-txt"><h3>{title}</h3><p>{text}</p></div></div>'''
    return f'<div class="m-tabs" data-tabs><div role="tablist" aria-label="{name}">{t}</div>{p}</div>'


def stepper(name, steps):
    """Clickable sequence. steps = [(title, who, when, text, out)]"""
    nav = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="s-{name}-{i}" id="sb-{name}-{i}" tabindex="{0 if i == 0 else -1}"><b>{i + 1:02d}</b>{t}</button>' for i, (t, *_r) in enumerate(steps))
    pan = ""
    for i, (t, who, when, text, outp) in enumerate(steps):
        pan += f'''<div role="tabpanel" id="s-{name}-{i}" aria-labelledby="sb-{name}-{i}"{"" if i == 0 else " hidden"} class="sp">
          <p class="sp-n">Step {i + 1} of {len(steps)}</p><h3>{t}</h3><p>{text}</p>
          <dl><div><dt>Who</dt><dd>{who}</dd></div><div><dt>When</dt><dd>{when}</dd></div><div><dt>What comes out</dt><dd>{outp}</dd></div></dl></div>'''
    return f'''<div class="m-stepper" data-tabs data-stepper><div role="tablist" aria-label="{name}">{nav}</div>
      <div class="sp-wrap"><div class="sp-prog"><span></span></div>{pan}
      <div class="sp-ctl"><button type="button" class="btn-line" data-prev>Previous</button><button type="button" class="btn-line" data-next>Next step</button></div></div></div>'''


def shift(rows, cap=""):
    """Before/after toggle list."""
    lis = "".join(f'<li><span class="s0">{a}</span><span class="s1">{b}</span></li>' for a, b in rows)
    return f'''<div class="m-shift" data-shift><div class="seg-toggle" role="group" aria-label="Show before or after">
      <button type="button" aria-pressed="true" data-v="0">Before</button><button type="button" aria-pressed="false" data-v="1">After</button></div>
      <ul>{lis}</ul>{f"<p class='cap'>{cap}</p>" if cap else ""}</div>'''


def page(key, spec):
    proj = next(p for p in PROJECTS if p["slug"] == KEY[key])
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in spec["meta"])
    tldr = "".join(f'<div class="tl"><h2>{a}</h2><p>{b}</p></div>' for a, b in spec["tldr"])
    kpis = "".join(
        f'<div class="kpi"><dt><span>{pre}</span><span data-countup="{val}">{val}</span><span>{suf}</span></dt><dd>{lab}</dd></div>'
        for val, suf, pre, lab in spec["kpis"])
    chips = "".join(f'<a href="#{cid}">{nav}</a>' for cid, nav, *_r in spec["chapters"])
    chs = ""
    for n, (cid, nav, title, ledetext, body) in enumerate(spec["chapters"]):
        chs += f'''<section class="ch" id="{cid}" aria-labelledby="{cid}-h">
      <header class="ch-head"><span class="ch-n">{n + 1:02d}</span><div><h2 id="{cid}-h">{title}</h2><p>{ledetext}</p></div></header>
      <div class="ch-body">{body}</div></section>'''
    gal = "".join(f'<figure>{img(s, c, cap=c)}<figcaption>{c}</figcaption></figure>' for s, c in spec["gallery"])
    others = [p for p in PROJECTS if p["case"] and p["slug"] != proj["slug"]]
    nxt = "".join(f'''<a class="nx" href="{p["slug"]}.html" style="--f:{p["f"]};--ft:{p["ft"]}"><img src="../{p["cover"]}" alt="" loading="lazy"><span>{p["kind"]}</span><h3>{p["title"].split(": ", 1)[1][0].upper() + p["title"].split(": ", 1)[1][1:]}</h3></a>''' for p in others)
    html = (head(f"{proj['title']} — Layer One", proj["blurb"], depth=1, og=proj["cover"])
            + topbar("work", depth=1) + f'''<main id="main" class="cs" style="--f:{proj["f"]}">
  <header class="cs-hero">
    <p class="crumb"><a href="../work.html">Work</a> / {proj["client"]}</p>
    <div class="cs-id">{logo_tile(proj["co"], depth=1, size=48, label=False)}<span>{proj["client"]} · {proj["year"]} · {proj["kind"]}</span></div>
    <h1>{spec["h1"]}</h1>
    <p class="cs-lede">{spec["lede"]}</p>
    <dl class="cs-meta">{meta}</dl>
    <figure class="cs-cover">{img(spec["cover"][0], spec["cover"][1], cap=spec["cover"][1])}</figure>
  </header>
  <nav class="chapters" aria-label="Chapters" data-chapters><div class="ch-chips">{chips}</div><div class="ch-prog"><span></span></div></nav>
  <section class="cs-wrap" aria-label="The short version">
    <p class="eyebrow">The 30-second version</p>
    <div class="tldr">{tldr}</div>
    <dl class="kpis" data-inview>{kpis}</dl>
  </section>
  <div class="cs-wrap">{chs}</div>
  <section class="cs-wrap ch" aria-labelledby="gal-h">
    <header class="ch-head"><span class="ch-n">+</span><div><h2 id="gal-h">From the files</h2><p>Select any image to see it full size.</p></div></header>
    <div class="cs-gallery" tabindex="0" aria-label="Gallery, scrolls sideways">{gal}</div>
  </section>
  <section class="cs-wrap cs-end">
    <p class="cs-credit">{spec["credits"]}</p>
    <div class="cs-cta"><div><h2>Need this for your product?</h2><p>We do this work for product teams now. Start with a two-week audit.</p></div>
      <div class="btn-row"><a class="pill pill--accent" href="../pricing.html">See pricing</a><a class="pill" href="../contact.html">Start a project</a></div></div>
    <h2 class="nx-h">Next case studies</h2>
    <div class="nxs">{nxt}</div>
  </section>
</main>
<dialog class="lightbox" data-lb><button type="button" class="lb-x" aria-label="Close">Close</button><img alt=""><p></p></dialog>''' + close(depth=1))
    write(f"work/{proj['slug']}.html", html)
