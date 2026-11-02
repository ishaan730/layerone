"""Page assets for work/cars24-lego.html: phones, the before/after pair, the guideline crop and board WebPs.
Phones come from the 2x Figma section renders when they exist (scratch folder argv[1]), else from lego-src (1x).
Run after render_lego.js (which writes b-*.jpg) to turn the boards into WebP at 1920w and 1100w."""
import sys, os, glob
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
HI = sys.argv[1] if len(sys.argv) > 1 else ""
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "lego-src")
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "assets", "work", "cars24-lego"))

# 1x boxes of each phone inside its landing-page section (section node, 1x section width, x, y, w, h)
PH = {"live-app": ("115130_14621", 1507, 235, 713, 360, 3668), "live-msite": ("115130_14621", 1507, 711, 766, 360, 4195),
      "home": ("115130_90175", 2972, 396, 508, 360, 2582), "home-web": ("115130_90175", 2972, 1709, 503, 360, 2624),
      "buy": ("115130_112037", 1524, 588, 386, 360, 5593), "sell": ("115130_112054", 1644, 643, 386, 360, 4016),
      "explore": ("115130_127064", 1771, 713, 411, 360, 5198), "carcheck": ("40000020_33146", 1835, 459, 453, 360, 3426),
      "carcheck-b": ("40000020_33146", 1835, 1011, 453, 360, 3284), "loans": ("40000020_48870", 1379, 468, 447, 360, 3782),
      "loans-b": ("40000020_48870", 1379, 852, 447, 360, 3636)}
LEGACY = {"live-app": "ph-live-app", "live-msite": "ph-live-msite", "home": "ph-new-app", "home-web": "ph-new-msite", "buy": "ph-buy",
          "sell": "ph-sell", "explore": "ph-explore", "carcheck": "ph-carcheck-a", "carcheck-b": "ph-carcheck-b", "loans": "ph-loans-a", "loans-b": "ph-loans-b"}


def phone(k):
    f, W1, x, y, w, h = PH[k]
    p = os.path.join(HI, f + ".png")
    if HI and os.path.exists(p):
        im = Image.open(p).convert("RGB"); s = im.width / W1
        return im.crop((round(x * s), round(y * s), round((x + w) * s), round((y + h) * s))).resize((720, round(h * 720 / w)), Image.LANCZOS)
    return Image.open(os.path.join(SRC, LEGACY[k] + ".jpg")).convert("RGB")


ims = {k: phone(k) for k in PH}
# The buy page's header doesn't render in Figma: borrow it from the explore page (same "Buy used car" tab).
b, e = ims["buy"], ims["explore"]
k = b.width / 360
b.paste(e.crop((0, 0, e.width, round(238 * k))), (0, 0))
for name in ["buy", "sell", "explore", "carcheck", "carcheck-b", "loans", "loans-b", "home"]:
    ims[name].save(os.path.join(OUT, f"p-{name}.webp"), quality=84, method=6)

# search, before (old parts) and after (LEGO)
for name, f, legacy in [("search-old", "397_8322", "x-397_8322"), ("search-new", "397_9105", "x-397_9105")]:
    p = os.path.join(HI, f + ".png")
    im = Image.open(p if HI and os.path.exists(p) else os.path.join(SRC, legacy + ".jpg")).convert("RGB")
    im = im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, f"p-{name}.webp"), quality=84, method=6)


def pair(a, c, name, H=1440):
    out = []
    for im in (ims[a], ims[c]):
        im = im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS).crop((0, 0, 720, H))
        out.append(im)
    S = Image.new("RGB", (720 * 2 + 240, H + 160), (236, 236, 232))
    m = Image.new("L", (720, H), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 719, H - 1), radius=56, fill=255)
    for n, im in enumerate(out): S.paste(im, (80 + n * 800, 80), m)
    S.save(os.path.join(OUT, name), quality=84, method=6)


pair("live-app", "live-msite", "ba-before.webp"); pair("home", "home-web", "ba-after.webp")

# guideline crop
g = os.path.join(HI, "115058_20269.png")
im = Image.open(g if HI and os.path.exists(g) else os.path.join(SRC, "x-115058_20269.jpg")).convert("RGB")
s = im.width / 2132
im.crop((0, 0, im.width, round(1300 * s))).resize((1600, round(1300 * s * 1600 / im.width)), Image.LANCZOS).save(os.path.join(OUT, "k-states-guide.webp"), quality=84, method=6)

# boards: b-*.jpg → b-*.webp (1920w) + b-*-1100.webp
for f in glob.glob(os.path.join(OUT, "b-*.jpg")):
    im = Image.open(f).convert("RGB"); base = f[:-4]
    im.save(base + ".webp", quality=82, method=6)
    im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS).save(base + "-1100.webp", quality=80, method=6)
    os.remove(f)
print("ok")
