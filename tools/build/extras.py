"""404 page, sitemap.xml and robots.txt. Runs last in build_all.

The 404 page can be served at any depth (/work/anything), so every asset path in it is made root-absolute.
"""
import glob, datetime
from common import *
from optimize import SITE, url_path

best = [p for p in PROJECTS if p["case"]][:4]
frames = "".join(frame(p) for p in best)
body = f'''<main id="main" class="nf"><div class="nf-in">
  <p class="lx-eyebrow">404:</p>
  <h1>This page moved, or never existed.</h1>
  <p class="nf-lede">The link may be old: our pages now live at short addresses like <code>/work/cars24-lego</code>. Here's the work most people come for.</p>
  <div class="btn-row"><a class="pill pill--accent" href="work.html">See all work</a><a class="pill" href="index.html">Home</a><a class="pill" href="contact.html">Contact</a></div>
  <div class="nf-grid">{frames}</div>
</div></main>'''
write("404.html", head("Page not found — Layer One", "This page moved or never existed. See Layer One's design system case studies.")
      + topbar() + body + close())
f = os.path.join(OUT, "404.html")
html = open(f).read()
for a, b in (('="assets/', '="/assets/'), (', assets/', ', /assets/'), ('content="assets/', 'content="/assets/')):
    html = html.replace(a, b)
html = html.replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
open(f, "w").write(html)

# sitemap.xml and robots.txt
today = datetime.date.today().isoformat()
pages = sorted(p for p in (os.path.relpath(x, OUT) for x in glob.glob(os.path.join(OUT, "*.html")) + glob.glob(os.path.join(OUT, "work", "*.html")))
               if p != "404.html")
prio = {"/": "1.0", "/work": "0.9", "/pricing": "0.9", "/contact": "0.8", "/lab": "0.7"}
urls = "".join(f"  <url><loc>{SITE}{url_path(p)}</loc><lastmod>{today}</lastmod><priority>{prio.get(url_path(p), '0.8' if p.startswith('work/') else '0.6')}</priority></url>\n" for p in pages)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("wrote sitemap.xml", len(pages), "pages; robots.txt")
