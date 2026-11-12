"""Bundle the prototype into one self-contained HTML file (fonts, images, CSS and JS inlined).

    python3 prototype/landing-v2/build_standalone.py

Writes prototype/landing-v2/layer-one-landing-v2.html, which opens from disk, an email or any static host
with no other files. The source of truth stays index.html + styles.css + app.js; never edit the bundle.
"""
import base64, mimetypes, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
MIME = {".woff2": "font/woff2", ".webp": "image/webp", ".svg": "image/svg+xml"}


def data_uri(rel):
    path = os.path.normpath(os.path.join(HERE, rel))
    ext = os.path.splitext(path)[1].lower()
    mime = MIME.get(ext) or mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def main():
    html = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
    css = open(os.path.join(HERE, "styles.css"), encoding="utf-8").read()
    js = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
    css = re.sub(r'url\("(\.\./[^"]+)"\)', lambda m: f'url("{data_uri(m.group(1))}")', css)
    html = html.replace('<link rel="stylesheet" href="styles.css">', f"<style>\n{css}</style>")
    html = html.replace('<script src="app.js" defer></script>', f"<script>\n{js}</script>")
    html = re.sub(r'<link rel="preload"[^>]+as="font"[^>]*>\n', "", html)
    html = re.sub(r'(src|href)="(\.\./\.\./assets/[^"]+)"', lambda m: f'{m.group(1)}="{data_uri(m.group(2))}"', html)
    assert "../../assets" not in html, "an asset was not inlined"
    out = os.path.join(HERE, "layer-one-landing-v2.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {os.path.relpath(out, os.path.dirname(os.path.dirname(HERE)))}  {os.path.getsize(out) // 1024} KB")


if __name__ == "__main__":
    main()
