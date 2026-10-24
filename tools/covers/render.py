"""Render the cover illustrations in tools/covers/covers.html to assets/work/<slug>/cover.jpg.
Serve the repo root on :8765 first."""
import os
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCENES = {"jpmc-checks": "jpmc-checks", "jpmc-patterns": "jpmc-patterns", "ibm": "ibm-design-systems"}
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1800, "height": 1238})
    pg.goto("http://localhost:8765/tools/covers/covers.html", wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    for scene, slug in SCENES.items():
        pg.evaluate(f"show('{scene}')")
        os.makedirs(os.path.join(ROOT, "assets", "work", slug), exist_ok=True)
        out = os.path.join(ROOT, "assets", "work", slug, "cover.jpg")
        pg.screenshot(path=out, type="jpeg", quality=84)
        print(out, os.path.getsize(out) // 1024, "KB")
    b.close()
