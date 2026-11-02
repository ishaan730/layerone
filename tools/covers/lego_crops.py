"""Cut crisp component crops from the 2x Figma sheet renders (scratch folder given as argv[1]).
Coordinates are in 1x sheet pixels; output is 2x, written to assets/work/cars24-lego/k-<name>.webp."""
import sys, os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
HI = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "assets", "work", "cars24-lego")
C = {
  "button": ("40000001_93521", 115, 330, 915, 820, 1149),
  "button-primary": ("40000001_93521", 560, 330, 470, 400, 1149),
  "chips": ("1180_13973", 232, 452, 700, 460, 1148),
  "toast": ("1185_11742", 205, 625, 735, 205, 1148),
  "inline": ("1185_11996", 200, 410, 730, 450, 1148),
  "snackbar": ("40000001_89626", 100, 400, 945, 600, 1148),
  "segment": ("1180_12349", 180, 450, 780, 580, 1148),
  "tabs": ("40000001_97146", 348, 500, 410, 370, 1640),
  "tabs-dark": ("40000001_97146", 792, 512, 410, 356, 1640),
  "switch": ("40000001_87425", 180, 380, 840, 620, 1148),
  "checkbox": ("40000001_87236", 180, 380, 420, 900, 1148),
  "avatar": ("1204_14893", 330, 440, 510, 560, 1148),
  "stepper": ("1212_19672", 170, 470, 1160, 250, 1500),
  "rating": ("1191_12883", 290, 1585, 720, 330, 1148),
  "badge": ("1185_12250", 1740, 330, 420, 430, 2669),
  "input": ("40000001_92577", 150, 375, 360, 100, 1148),
  "input-states": ("40000001_92577", 150, 375, 360, 880, 1148),
  "input-grid": ("40000001_92577", 150, 375, 800, 620, 1148),
  "phone": ("40000001_86683", 380, 470, 380, 640, 1148),
  "reg": ("40000001_83559", 390, 430, 350, 620, 1148),
  "otp": ("1215_12420", 250, 400, 600, 560, 2528),
  "tooltip": ("1180_15167", 395, 380, 320, 420, 1148),
  "header": ("40000001_105743", 40, 650, 1260, 340, 1333),
}
for k, (f, x, y, w, h, W1) in C.items():
    im = Image.open(os.path.join(HI, f + ".png")).convert("RGB")
    s = im.width / W1
    c = im.crop((round(x * s), round(y * s), round((x + w) * s), round((y + h) * s)))
    c.save(os.path.join(OUT, "k-" + k + ".webp"), quality=86, method=6)
    print(k, c.size)
