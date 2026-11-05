"""Build-time optimisation, applied by common.write() to every page.

1. Responsive images: every raster <img> wider than 700px gets WebP copies at 480/800/1200/1800px
   (made once, next to the original, as name.w800.webp) and a srcset, so phones and small slots download
   a fraction of the bytes. Lightbox images keep the full-size file in data-full.
2. Clean URLs: links are rewritten to root-relative paths without .html ("/work/cars24-lego").
   Vercel serves them via cleanUrls in vercel.json; tools/serve.py does the same locally.
3. Head extras: canonical URL, og:url, og:site_name, Twitter card fields, speculation rules
   (pages prerender on hover in Chromium browsers) and the Organization JSON-LD on the home page.
"""
import os, re
from PIL import Image

SITE = "https://www.layerone.co.in"
WIDTHS = (480, 800, 1200, 1800)
RENAME = {"clients.html": "experience.html", "blog.html": "writing.html"}
_dims = {}


def _size(full):
    if full not in _dims:
        try:
            with Image.open(full) as im:
                _dims[full] = im.size
        except Exception:
            _dims[full] = None
    return _dims[full]


def _variant(full, w):
    stem, _ = os.path.splitext(full)
    out = f"{stem}.w{w}.webp"
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(full):
        with Image.open(full) as im:
            im = im.convert("RGBA") if im.mode in ("P", "LA", "RGBA") else im.convert("RGB")
            h = round(im.size[1] * w / im.size[0])
            im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=80, method=6)
    return out


def url_path(page):
    """'work/cars24-lego.html' -> '/work/cars24-lego', 'index.html' -> '/'."""
    page = RENAME.get(page, page)
    p = "/" + page[:-5] if page.endswith(".html") else "/" + page
    return "/" if p == "/index" else p


def _attr(tag, name):
    m = re.search(r'\s' + name + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def _set(tag, name, val):
    if _attr(tag, name) is not None:
        return re.sub(r'(\s' + name + r'=")[^"]*(")', lambda m: m.group(1) + val + m.group(2), tag, count=1)
    return tag[:-1].rstrip("/").rstrip() + f' {name}="{val}">'


def responsive(html, page, out_dir):
    base = os.path.dirname(os.path.join(out_dir, page))

    def full_of(src):
        if not src or src.startswith(("http", "data:", "//")):
            return None
        f = os.path.normpath(os.path.join(base, src.split("?")[0]))
        return f if os.path.isfile(f) and f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) else None

    def srcset_for(src, full):
        dims = _size(full)
        if not dims or dims[0] <= 700:
            return None
        w0 = dims[0]
        ws = [w for w in WIDTHS if w < w0 * 0.92]
        rel = os.path.dirname(src)
        items = [(w, f"{rel}/{os.path.basename(_variant(full, w))}") for w in ws]
        if w0 <= 2400:
            items.append((w0, src))  # the original is the largest size; no full-size copy
        else:
            items.append((2400, f"{rel}/{os.path.basename(_variant(full, 2400))}"))
        return items, dims

    def fix_img(m):
        tag = m.group(0)
        if _attr(tag, "srcset") is not None:
            return tag
        src = _attr(tag, "src")
        full = full_of(src)
        if not full:
            return tag
        r = srcset_for(src, full)
        if not r:
            return tag
        items, (w0, h0) = r
        mid = next((u for w, u in items if w >= 1200), items[-1][1])
        lazy = _attr(tag, "loading") == "lazy"
        tag = _set(tag, "srcset", ", ".join(f"{u} {w}w" for w, u in items))
        tag = _set(tag, "sizes", "auto, (max-width: 760px) 100vw, 60vw" if lazy else "(max-width: 1280px) 100vw, 1240px")
        if " data-lightbox" in tag:
            tag = _set(tag, "data-full", src)
        tag = _set(tag, "src", mid)
        w, h = _attr(tag, "width"), _attr(tag, "height")
        if w and h and w.isdigit() and h.isdigit() and abs(int(w) / int(h) - w0 / h0) > 0.02:
            tag = _set(_set(tag, "width", str(w0)), "height", str(h0))
        if _attr(tag, "decoding") is None:
            tag = _set(tag, "decoding", "async")
        return tag

    html = re.sub(r"<img\b[^>]*>", fix_img, html)

    def fix_data_src(m):  # image tab viewers swap src from data-src: point them at the 1200px copy
        src = m.group(1)
        full = full_of(src)
        if full:
            r = srcset_for(src, full)
            if r:
                return f'data-src="{next((u for w, u in r[0] if w >= 1200), r[0][-1][1])}" data-full="{src}"'
        return m.group(0)

    return re.sub(r'data-src="([^"]+)"', fix_data_src, html)


def clean_links(html, page):
    base = os.path.dirname(page)

    def fix(m):
        attr, val = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|tel:|#|data:|//)", val) or ".html" not in val:
            return m.group(0)
        path, _, frag = val.partition("#")
        if not path.endswith(".html"):
            return m.group(0)
        target = os.path.normpath(os.path.join(base, path)).replace("\\", "/")
        return f'{attr}="{url_path(target)}{"#" + frag if frag else ""}"'

    return re.sub(r'\b(href)="([^"]*)"', fix, html)


ORG = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Layer One",'
       '"description":"A design systems studio: building, scaling and governing design systems, and getting teams to adopt them.",'
       f'"url":"{SITE}/","logo":"{SITE}/assets/favicon.svg","image":"{SITE}/assets/og/layer-one.jpg","email":"layerone@proton.me",'
       '"founder":{"@type":"Person","name":"Aniket Pandey"},"address":{"@type":"PostalAddress","addressLocality":"Bangalore","addressCountry":"IN"},'
       '"areaServed":"Worldwide","sameAs":["https://www.linkedin.com/company/layerone.co.in/","https://x.com/LayeroneStudios","https://medium.com/@layerone_11803"]}</script>')

SPEC = ('<script type="speculationrules">{"prerender":[{"where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":"/assets/*"}}]},"eagerness":"moderate"}],'
        '"prefetch":[{"where":{"href_matches":"/*"},"eagerness":"moderate"}]}</script>')


def head_extras(html, page):
    url = SITE + url_path(page)
    extra = ""
    if 'rel="canonical"' not in html:
        extra += f'<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">\n<meta property="og:site_name" content="Layer One">\n'
        t = re.search(r"<title>(.*?)</title>", html)
        d = re.search(r'<meta name="description" content="([^"]*)"', html)
        img = re.search(r'<meta property="og:image" content="([^"]*)"', html)
        if t:
            extra += f'<meta name="twitter:title" content="{t.group(1)}">\n'
        if d:
            extra += f'<meta name="twitter:description" content="{d.group(1)}">\n'
        if img:
            extra += f'<meta name="twitter:image" content="{img.group(1)}">\n'
    if "speculationrules" not in html:
        extra += SPEC + "\n"
    if page == "index.html" and "application/ld+json" not in html:
        extra += ORG + "\n"
    return html.replace("</head>", extra + "</head>", 1) if extra and "</head>" in html else html


def process(html, page, out_dir):
    html = responsive(html, page, out_dir)
    html = clean_links(html, page)
    return head_extras(html, page)
