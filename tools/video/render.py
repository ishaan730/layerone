"""Render tools/video/hero.html to assets/video/hero-reel.{mp4,webm} and a poster.
Serve the repo root on :8765 first:  python3 -m http.server 8765
Usage: python3 tools/video/render.py [--preview t1,t2,...]"""
import os, subprocess, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "assets", "video")
FPS = 30
W, H = 1600, 900

def main():
    preview = None
    if len(sys.argv) > 2 and sys.argv[1] == "--preview":
        preview = [float(x) for x in sys.argv[2].split(",")]
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM") or None)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("http://localhost:8765/tools/video/hero.html", wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.evaluate("Promise.all([...document.images].map(i => i.decode().catch(()=>0)))")
        dur = pg.evaluate("window.DUR")
        if preview:
            for t in preview:
                pg.evaluate(f"seek({t})")
                pg.screenshot(path=os.path.join(os.environ.get("PREVIEW_DIR", "/tmp"), f"frame_{t:05.2f}.jpg"), type="jpeg", quality=80)
            b.close(); return
        n = int(dur * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                               "-an", os.path.join(OUT, "hero-reel.mp4")], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f"seek({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=94))
            if i % 90 == 0: print(f"frame {i}/{n}", flush=True)
        ff.stdin.close(); ff.wait()
        pg.evaluate("seek(27.6)")
        pg.screenshot(path=os.path.join(OUT, "hero-poster.jpg"), type="jpeg", quality=82)
        b.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(OUT, "hero-reel.mp4"), "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "38",
                    "-row-mt", "1", "-deadline", "good", "-cpu-used", "4", "-an", os.path.join(OUT, "hero-reel.webm")], check=True)
    for f in ("hero-reel.mp4", "hero-reel.webm", "hero-poster.jpg"):
        print(f, os.path.getsize(os.path.join(OUT, f)) // 1024, "KB")

if __name__ == "__main__":
    main()
