"""Showcase case study engine (v4): visual first, very little text.

Used for the IBM client case studies (Cardinal Health, Riyadh Air). Each page is:
  brand-colour hero (title, one-line lede, proof numbers, cover)
  → sticky chapter bar → sections, each a short header plus one big visual block
  → outcomes → lessons → "same playbook, your team" (the offer) → credits → next case studies.
Section modes: "" (dark), "stage" (the project's brand colour), "paper" (light).
Visual blocks below return HTML strings. Styles: "Showcase case study (v4)" in assets/site.css.
"""
from common import *
from cs import tiles
from PIL import Image
import html as _h


def _dims(src):
    w, h = Image.open(OUT + "/" + src).size
    return w, h


def simg(src, alt, cap=None, lb=True, eager=False):
    w, h = _dims(src)
    lbattr = f' data-lightbox data-cap="{_h.escape(cap or alt)}"' if lb else ""
    return f'<img src="../{src}" alt="{_h.escape(alt)}" width="{w}" height="{h}"{"" if eager else " loading=" + chr(34) + "lazy" + chr(34)} decoding="async"{lbattr}>'


ICONS = {
    "layers": '<path d="M12 3 2 8l10 5 10-5-10-5Z"/><path d="m2 13 10 5 10-5"/><path d="m2 18 10 5 10-5" opacity=".5"/>',
    "broken": '<path d="M9 17H7A5 5 0 0 1 7 7h2"/><path d="M15 7h2a5 5 0 0 1 4 8"/><path d="M8 12h3"/><path d="m3 3 18 18"/>',
    "drift": '<rect x="3" y="4" width="8" height="16" rx="2"/><rect x="13" y="7" width="8" height="13" rx="2" transform="rotate(8 17 13)"/>',
    "squads": '<circle cx="7" cy="8" r="3"/><circle cx="17" cy="8" r="3"/><circle cx="12" cy="16" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    "script": '<path d="M4 6h10M9 4v2c0 5-2 9-5 11"/><path d="M6 11c1.5 2.5 4 4.5 7 5.5"/><path d="m13 20 4-10 4 10M14.5 16.5h5"/>',
    "plane": '<path d="M10.5 21 13 13l7 2v-2l-7-5V3.5a1.5 1.5 0 0 0-3 0V8l-7 5v2l7-2-2.5 8"/>',
    "owner": '<circle cx="12" cy="7" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/><path d="m17 3 3 3" opacity=".6"/>',
    "door": '<path d="M5 21V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v17"/><path d="M3 21h18"/><circle cx="15" cy="12" r="1"/>',
    "gate": '<path d="M4 21V5M20 21V5M4 9h16M4 15h16"/>',
    "copy": '<rect x="8" y="8" width="13" height="13" rx="2"/><path d="M4 16V5a1 1 0 0 1 1-1h11"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


# ---------------------------------------------------------------- blocks
def brief(rows):
    """Problem → answer rows. rows = [(icon, before, after)]"""
    out = "".join(f'<div><span class="ic">{icon(i)}</span><p class="was">{a}</p><span class="arr">{LONG_ARROW}</span><p class="now">{b}</p></div>' for i, a, b in rows)
    return f'<div class="sc-brief">{out}</div>'


def carousel(label, slides):
    """The work reel. slides = [(src, title, line, opts)] opts: bg, pad, cover(bool)"""
    n = len(slides)
    s = ""
    for i, (src, title, line, *o) in enumerate(slides):
        o = o[0] if o else {}
        st = (f"--sb:{o['bg']};" if "bg" in o else "") + (f"--sp:{o['pad']};" if "pad" in o else "")
        s += f'''<figure class="sc-slide" role="group" aria-roledescription="slide" aria-label="{i + 1} of {n}: {_h.escape(title)}">
        <div class="sc-slide-m{" is-cover" if o.get("cover") else ""}" style="{st}">{simg(src, title + ". " + line, cap=title + ". " + line)}</div>
        <figcaption><b>{i + 1:02d}</b><span>{title}</span><em>{line}</em></figcaption></figure>'''
    return f'''<div class="sc-car" data-carousel aria-roledescription="carousel" aria-label="{label}">
      <div class="sc-car-track" tabindex="0" aria-label="{label}. Use the arrow keys to move between slides.">{s}</div>
      <div class="sc-in"><div class="sc-car-ctl"><span class="sc-car-count"><b data-cur>01</b> / {n:02d}</span><div class="sc-car-bar"><i></i></div>
        <button type="button" class="sc-car-btn" data-prev aria-label="Previous slide">{ARROW}</button><button type="button" class="sc-car-btn" data-next aria-label="Next slide">{ARROW}</button></div></div>
    </div>'''


def bento(items):
    """items = [(src, caption, cols, rows, opts)] opts: fit, pos, bg, pad; or ("html", markup, cols, rows, opts)"""
    out = ""
    for src, cap, c, r, *o in items:
        o = o[0] if o else {}
        st = f"--c:{c};--r:{r};" + "".join(f"--{k}:{o[k]};" for k, v in (("fit", 0), ("pos", 0)) if k in o) + (f"--sb:{o['bg']};" if "bg" in o else "") + (f"--sp:{o['pad']};" if "pad" in o else "")
        if src == "html":
            out += f'<figure style="{st}">{cap}</figure>'
        else:
            out += f'<figure style="{st}">{simg(src, cap)}<figcaption>{cap}</figcaption></figure>'
    return f'<div class="sc-bento">{out}</div>'


def bigfig(src, cap, bg=None, pad=None):
    st = (f"--sb:{bg};" if bg else "") + (f"--sp:{pad};" if pad else "")
    return f'<figure class="sc-fig"><div class="m" style="{st}">{simg(src, cap)}</div><figcaption>{cap}</figcaption></figure>'


def nums(items):
    """items = [(pre, value, suf, label, tag)]; value counts up when numeric."""
    out = ""
    for pre, val, suf, label, tag in items:
        v = f'<span data-countup="{val}">{val}</span>' if str(val).replace(".", "").isdigit() else val
        out += f'<div>{f"<span class=t>{tag}</span>" if tag else ""}<strong>{pre}{v}{suf}</strong><p>{label}</p></div>'
    return f'<div class="sc-nums" style="--n:{len(items)}">{out}</div>'


def rail(steps):
    lis = "".join(f'<li style="--i:{i}"><span class="dot">{i + 1:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))
    return f'<ol class="sc-rail" style="--n:{len(steps)};padding:0;margin:0" data-inview>{lis}</ol>'


def inventory(total, label, fams):
    """fams = [(name, [components])]"""
    f = "".join(f'<article class="sc-fam"><header><b>{n}</b><span>{len(c)}</span></header><ul>{"".join(f"<li>{x}</li>" for x in c)}</ul></article>' for n, c in fams)
    return f'<div class="sc-inv"><div class="sc-inv-total"><strong>{total}</strong><span>{label}</span></div><div class="sc-fams">{f}</div></div>'


def outcomes(items):
    return '<div class="sc-out">' + "".join(f'<div><span class="t">{t}</span><div><strong>{b}</strong></div><p>{p}</p></div>' for t, b, p in items) + "</div>"


def lessons(items):
    return '<div class="sc-lessons">' + "".join(f"<div><b>{i + 1:02d}</b><p>{t}</p></div>" for i, t in enumerate(items)) + "</div>"


def seg(attr, opts, label):
    b = "".join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if i == 0 else "false"}"><span>{t}</span></button>' for i, (v, t) in enumerate(opts))
    return f'<div class="sc-seg" {attr} role="group" aria-label="{label}">{b}</div>'


def playbook(rows, employer="IBM"):
    """The offer, mapped to what this project did. rows = {"audit": text, "foundations": text, "partner": text}"""
    plans = [("audit", "Audit", "2 weeks, fixed", "$1,500", "pricing.html#plan-audit", False),
             ("foundations", "Foundations", "6 weeks, fixed", "$5,900", "pricing.html#plan-foundations", True),
             ("partner", "Partner", "Monthly, pause any time", "$2,900<small>/mo</small>", "pricing.html#plan-partner", False)]
    cards = "".join(f'''<a href="../{h}"{" class=" + chr(34) + "is-rec" + chr(34) if rec else ""}>
        <div class="top"><span>{d}</span>{"<span>Most teams start here</span>" if rec else ""}</div>
        <h3>{n}</h3><p class="price"><b>{p}</b></p>
        <p class="from"><em>In this case study</em>{rows[k]}</p>
        <span class="go">See what's included {ARROW}</span></a>''' for k, n, d, p, h, rec in plans)
    employer = ("an " if employer[0] in "AEIOU" else "a ") + employer
    return f'''<div class="sc-play">{cards}</div>
    <div class="sc-cta-row"><p>The work above was done by our founder as {employer} employee. Layer One now runs the same method as a studio, for product teams of any size.</p>
      <div class="btn-row"><a class="pill pill--accent" href="../contact.html">Start a project</a><a class="pill" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div></div>'''


# ---------------------------------------------------------------- story blocks
def prose(*paras):
    """Paragraphs; a string starting with '### ' becomes a subheading, one starting with '> ' a pull quote."""
    out = ""
    for p in paras:
        if p.startswith("### "):
            out += f"<h3>{p[4:]}</h3>"
        elif p.startswith("> "):
            out += f'<blockquote class="sc-quote"><p>{p[2:]}</p></blockquote>'
        else:
            out += f"<p>{p}</p>"
    return f'<div class="sc-prose">{out}</div>'


def story(body, aside_title=None, aside=None):
    """Long-form text: a short side note (facts or 'in short') and a readable prose column."""
    side = ""
    if aside:
        items = "".join(f"<li><b>{a}</b><span>{b}</span></li>" if b else f"<li><span>{a}</span></li>" for a, b in aside)
        side = f'<aside class="sc-side"><p>{aside_title or "In short"}</p><ul>{items}</ul></aside>'
    return f'<div class="sc-story">{side or "<div></div>"}<div>{body}</div></div>'


def quote(text, by=None):
    return f'<blockquote class="sc-quote sc-quote--big"><p>{text}</p>{f"<cite>{by}</cite>" if by else ""}</blockquote>'


def facts(items):
    """Client facts. items = [(big, label)]"""
    return '<dl class="sc-facts">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in items) + "</dl>"


def room(items):
    """Who was in the room. items = [(org, team, text)]"""
    return '<div class="sc-room">' + "".join(f'<div><span>{o}</span><h3>{t}</h3><p>{x}</p></div>' for o, t, x in items) + "</div>"


def timeline(items):
    """Dated milestones. items = [(date, title, text, tag)]"""
    lis = "".join(f'<li style="--i:{n}"><time>{d}</time><div><h3>{t}</h3><p>{x}</p>{f"<span>{g}</span>" if g else ""}</div></li>' for n, (d, t, x, g) in enumerate(items))
    return f'<ol class="sc-time" data-inview>{lis}</ol>'


def ticket(key, status, title, fields, note):
    rows = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in fields)
    return f'<div class="sc-ticket"><header><code>{key}</code><span>{status}</span></header><h3>{title}</h3><dl>{rows}</dl><p class="small" style="color:#6c6789">{note}</p></div>'


def changelog(version, date, items, note):
    lis = "".join(f'<li><b class="t-{k.lower()}">{k}</b>{t}</li>' for k, t in items)
    return f'<div class="sc-log"><header><code>{version}</code><span>{date}</span></header><ul>{lis}</ul><p>{note}</p></div>'


def flowline(states, active):
    """A ticket's statuses, with the current one highlighted."""
    return '<ol class="sc-states">' + "".join(f'<li class="{"is-done" if i < active else "is-on" if i == active else ""}">{t}</li>' for i, t in enumerate(states)) + "</ol>"


def gap(px=24):
    return f'<div style="height:{px}px"></div>'


# ---------------------------------------------------------------- page
def section(sid, nav, k, h2, lede, body, mode=""):
    cls = "sc-sec" + (f" sc-sec--{mode}" if mode else "")
    return nav, sid, f'''<section class="{cls}" id="{sid}" aria-labelledby="{sid}-h">
    <div class="sc-in"><header class="sc-h"><div><p class="sc-k">{k}</p><h2 id="{sid}-h">{h2}</h2></div>{f"<p>{lede}</p>" if lede else ""}</header></div>
    {body}
  </section>'''


def wrap(html):
    """Constrain a block to the content column (carousels run full-bleed, so they skip this)."""
    return f'<div class="sc-in">{html}</div>'


def page(slug, spec):
    proj = next(p for p in PROJECTS if p["slug"] == slug)
    proof = "".join(
        f'<div><dt>{pre}<span data-countup="{val}">{val}</span>{suf}</dt><dd>{lab}</dd></div>' if str(val).isdigit()
        else f'<div><dt>{pre}{val}{suf}</dt><dd>{lab}</dd></div>' for pre, val, suf, lab in spec["proof"])
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in spec["meta"])
    secs = spec["sections"]
    chips = "".join(f'<a href="#{sid}">{nav}</a>' for nav, sid, _ in secs)
    body = "".join(h for *_r, h in secs)
    cases = [p for p in PROJECTS if p["case"]]
    i = cases.index(proj)
    others = [cases[(i + 1) % len(cases)], cases[(i + 2) % len(cases)]]
    nxt = "".join(f'''<a class="nx" href="{p["slug"]}.html" style="--f:{p["f"]};--ft:{p["ft"]}"><img src="../{p["cover"]}" alt="" loading="lazy"><span>{p["kind"]}</span><h3>{short(p)}</h3></a>''' for p in others)
    logo = spec.get("client_logo")
    cl = f'<img class="cl" src="../{logo}" alt="{proj["client"].split(" × ")[-1]}">' if logo else f'<span class="cl">{proj["client"].split(" × ")[-1]}</span>'
    # IBM client work shows "IBM × client"; work for the employer itself shows just the employer's logo.
    ident = (f'{logo_tile("ibm", depth=1, size=36, label=False)}<span class="x">×</span>{cl}' if " × " in proj["client"]
             else f'{logo_tile(proj["co"], depth=1, size=36, label=False)}<span class="cl">{COMPANIES[proj["co"]]["name"]}</span>')
    html = (head(f"{proj['title']} — Layer One", proj["blurb"], depth=1, og=proj["cover"])
            + topbar("work", depth=1) + f'''<main id="main" class="sc" style="--f:{proj["f"]};--ft:{proj["ft"]}">
  <header class="sc-hero"><div class="sc-in">
    <div class="sc-hero-bar"><p class="sc-crumb"><a href="../work.html">Work</a> / {proj["client"]}</p><div class="sc-id">{ident}</div></div>
    <div class="sc-top">
      <div><h1>{spec["h1"]}</h1><p class="sc-lede">{spec["lede"]}</p></div>
      <dl class="sc-proof" data-inview>{proof}</dl>
    </div>
    <dl class="sc-meta">{meta}</dl>
    <figure class="sc-hero-media">{simg(proj["cover"], spec["cover_alt"], eager=True)}</figure>
  </div></header>
  <nav class="chapters" aria-label="Chapters" data-chapters style="margin-top:0"><div class="ch-chips">{chips}</div><div class="ch-prog"><span></span></div></nav>
  {body}
  <section class="sc-end"><div class="sc-in">
    <p class="sc-credit">{spec["credits"]}</p>
    <h2 class="nx-h">Next case studies</h2>
    <div class="nxs">{nxt}</div>
  </div></section>
</main>
<dialog class="lightbox" data-lb><button type="button" class="lb-x" aria-label="Close">Close</button><img alt=""><p></p></dialog>''' + close(depth=1))
    write(f"work/{slug}.html", html)
