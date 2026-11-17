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
# lastmod is the date a page's content last changed, not the build date: Google ignores lastmod values that
# change on every build. Each page's content is hashed (ignoring cache-busting ?v= strings); the hash and date
# are kept in lastmod.json, which is committed. A new page, or one without an entry, takes the date of its last
# commit if its content matches the committed version, and today otherwise. <priority> is left out: Google ignores it.
import hashlib, json, re, subprocess

today = datetime.date.today().isoformat()
LASTMOD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lastmod.json")
cache = json.load(open(LASTMOD)) if os.path.exists(LASTMOD) else {}


def _norm(html):
    return hashlib.sha1(re.sub(r"\?v=[0-9a-f]{8}", "", html).encode()).hexdigest()


def _git(*args):
    try:
        return subprocess.run(["git", *args], cwd=OUT, capture_output=True, text=True, check=True).stdout
    except Exception:
        return ""


pages = sorted(p for p in (os.path.relpath(x, OUT) for x in glob.glob(os.path.join(OUT, "*.html")) + glob.glob(os.path.join(OUT, "work", "*.html"))
                                                       + glob.glob(os.path.join(OUT, "writing", "*.html")) + glob.glob(os.path.join(OUT, "writing", "topics", "*.html"))
                                                       + glob.glob(os.path.join(OUT, "lab", "*.html")) + glob.glob(os.path.join(OUT, "services", "*.html")))
               if p != "404.html")
urls = ""
for p in pages:
    h = _norm(open(os.path.join(OUT, p)).read())
    entry = cache.get(p)
    if entry and entry["hash"] == h:
        date = entry["date"]
    elif entry:
        date = today
    else:
        committed = _git("show", f"HEAD:{p}")
        date = (_git("log", "-1", "--format=%cs", "--", p).strip() or today) if committed and _norm(committed) == h else today
    cache[p] = {"hash": h, "date": date}
    urls += f"  <url><loc>{SITE}{url_path(p)}</loc><lastmod>{date}</lastmod></url>\n"
cache = {k: v for k, v in sorted(cache.items()) if k in pages}
json.dump(cache, open(LASTMOD, "w"), indent=1)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("wrote sitemap.xml", len(pages), "pages; robots.txt")
