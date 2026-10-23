from common import *
from PIL import Image


def dims(src):
    w, h = Image.open(OUT + "/" + src).size
    return f'width="{w}" height="{h}"'

ORDER = ["tokens", "governance", "patterns"]


def fig(src, cap, alt="", extra=""):
    return f'<figure class="figure{extra}"><img src="../{src}" alt="{alt}" {dims(src)} loading="lazy"><figcaption>{cap}</figcaption></figure>'


def pair(a, b, cap):
    return (f'<figure class="figure"><div class="figure-pair"><img src="../{a[0]}" alt="{a[1]}" {dims(a[0])} loading="lazy">'
            f'<img src="../{b[0]}" alt="{b[1]}" {dims(b[0])} loading="lazy"></div><figcaption>{cap}</figcaption></figure>')


def prose(*paras):
    return '<div class="prose">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def cards(items, cols=2):
    cls = "cards" + (" cards--3" if cols == 3 else "")
    return f'<div class="{cls}">' + "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in items) + "</div>"


def page(key, h1, lede, facts, results, cover, cover_alt, sections, file):
    c = CASES[key]
    facts_html = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts)
    res_html = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in results)
    toc = "".join(f'<li><a href="#{sid}">{label}</a></li>' for sid, label, *_ in sections)
    body = ""
    for sid, label, kicker, h2, content in sections:
        body += f'''<section class="cs-section" id="{sid}" aria-labelledby="{sid}-h">
        <p class="cs-kicker">{kicker}</p><h2 id="{sid}-h">{h2}</h2>{content}</section>'''
    nxt = CASES[ORDER[(ORDER.index(key) + 1) % 3]]
    html = (head(f"{c['short']} at CARS24 — Layer One case study", c["summary"][:155], depth=1, og_image=c["img"])
            + header("work", depth=1) + f'''<main id="main">
<div class="wrap">
  <header class="cs-head">
    <p class="crumb"><a href="../work.html">Work</a><span aria-hidden="true">/</span><span>{c["meta"]}</span></p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <dl class="facts">{facts_html}</dl>
  </header>
  <figure class="cs-cover"><img src="../{cover}" alt="{cover_alt}" {dims(cover)}></figure>
  <dl class="results" aria-label="Results">{res_html}</dl>
  <div class="cs-layout">
    <nav class="cs-toc" aria-label="On this page"><p>On this page</p><ol>{toc}</ol></nav>
    <div class="cs-body">{body}</div>
  </div>
  <aside class="next-case">
    <a href="../{nxt["href"]}"><div><p>Next case study</p><h2>{nxt["title"]}</h2></div><img src="../{nxt["img"]}" alt="" loading="lazy"></a>
  </aside>
  <p class="credit" style="margin-bottom:64px">Led by Layer One's founder, Aniket Pandey, as Design Systems Lead at CARS24, with CARS24's design, engineering, brand and content teams. Images belong to CARS24.</p>
</div>
</main>''' + cta("Facing something similar?", "Tell us where your system is today. We'll tell you honestly what we'd do and whether we're the right people to do it.") + footer(depth=1))
    write(f"work/{file}", html)
