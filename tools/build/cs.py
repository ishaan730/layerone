"""Full case study template: light theme, no sidebar, Hex case-page structure.
Title → hero → intro → scope table → results → sections with galleries → credits → more work → link rows."""
from common import *
from PIL import Image

KEY = {"tokens": "cars24-tokens", "governance": "cars24-governance", "patterns": "cars24-pattern-library"}


def dims(src):
    w, h = Image.open(OUT + "/" + src).size
    return f'width="{w}" height="{h}"'


def fig(src, cap, alt=""):
    return f'<figure class="gallery" style="margin:20px 0 0"><img src="../{src}" alt="{alt}" {dims(src)} loading="lazy"><figcaption class="cap">{cap}</figcaption></figure>'


def pair(a, b, cap):
    return (f'<figure style="margin:20px 0 0"><div class="g2"><img src="../{a[0]}" alt="{a[1]}" {dims(a[0])} loading="lazy">'
            f'<img src="../{b[0]}" alt="{b[1]}" {dims(b[0])} loading="lazy"></div><figcaption class="cap">{cap}</figcaption></figure>')


def prose(*paras):
    return '<div class="prose">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def cards(items, cols=2):
    return f'<div class="tiles{" tiles--3" if cols == 3 else ""}">' + "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in items) + "</div>"


def page(key, h1, lede, facts, results, cover, cover_alt, sections, file):
    proj = next(p for p in PROJECTS if p["slug"] == KEY[key])
    scope = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts)
    res = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in results)
    body = ""
    for sid, label, kicker, h2, content in sections:
        body += f'''<section class="sec" id="{sid}" aria-labelledby="{sid}-h">
      <div class="sec-head"><p class="k">{kicker}</p><h2 id="{sid}-h">{h2}</h2></div>
      <div class="sec-body">{content}</div>
    </section>'''
    others = [p for p in PROJECTS if p["slug"] != proj["slug"] and p["case"]][:2]
    mh = "".join(f'<a class="frame frame--named" href="{p["slug"]}.html"><h3>{p["title"].split(": ", 1)[1][0].upper() + p["title"].split(": ", 1)[1][1:]}</h3><div class="frame-media"><img src="../{p["cover"]}" alt="" loading="lazy"></div></a>' for p in others)
    html = (head(f"{proj['title']} — Layer One", proj["blurb"], depth=1, theme="light", og=proj["cover"])
            + topbar("work", depth=1) + f'''<main id="main" class="page">
  <p class="crumb"><a href="../work.html">Work</a> / {proj["client"]}</p>
  <h1>{h1}</h1>
  <figure class="hero-media" style="margin:24px 0 0"><img src="../{cover}" alt="{cover_alt}" {dims(cover)}></figure>
  <div class="intro"><p>{lede}</p></div>
  <dl class="scope">{scope}</dl>
  <dl class="results" aria-label="Results">{res}</dl>
  {body}
  <section class="credits"><h2>Credits</h2>
    <p>Led by Aniket Pandey as Design Systems Lead at CARS24, with CARS24's design, engineering, brand and content teams. Images belong to CARS24 and are shown for portfolio purposes.</p></section>
  <section class="more"><h2>More work</h2><div class="frames frames--2">{mh}</div>
    <div class="rowlinks" style="margin-top:8px">
      <a href="../work.html">All work<span>Case studies and projects</span></a>
      <a href="../lab.html">Lab<span>Try the tools from this case study</span></a>
      <a href="../contact.html">Start a project<span>Get in touch with Layer One</span></a>
    </div></section>
</main>''' + close(depth=1))
    write(f"work/{file}", html)
