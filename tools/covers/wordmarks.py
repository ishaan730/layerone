"""Cut the white wordmark out of each brand tile in assets/logos/ into a transparent PNG for the logo strip.
Run: python3 tools/covers/wordmarks.py (needs pillow)."""
import os
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOGOS = os.path.join(ROOT, "assets", "logos")
TILES = {"cars24": "cars24.png", "ibm": "ibm.png", "jpmc": "jpmorgan-chase.jpg"}


def cut(src, dst):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    px = im.load()
    # Background level: the brightest "darkest channel" found along the tile's border, plus a margin.
    edge = [min(px[x, y]) for x in range(w) for y in (0, h - 1)] + [min(px[x, y]) for y in range(h) for x in (0, w - 1)]
    t = min(max(edge) + 24, 200)
    a = Image.new("L", (w, h))
    ap = a.load()
    for y in range(h):
        for x in range(w):
            ap[x, y] = max(0, min(255, round((min(px[x, y]) - t) * 255 / (255 - t))))
    out = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    out.putalpha(a)
    out = out.crop(a.point(lambda v: 255 if v > 40 else 0).getbbox())
    out.save(dst, optimize=True)
    print("wrote", os.path.relpath(dst, ROOT), out.size)


if __name__ == "__main__":
    for key, f in TILES.items():
        cut(os.path.join(LOGOS, f), os.path.join(LOGOS, f"wordmark-{key}.png"))
