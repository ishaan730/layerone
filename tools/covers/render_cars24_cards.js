// Render the CARS24 preview cards in tools/covers/cars24_cards.html to assets/work/<folder>/card.jpg (1920 × 1080).
// Serve the repo root on :8765 first (python3 -m http.server 8765), then: node tools/covers/render_cars24_cards.js
const path = require("path"), fs = require("fs");
const { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..", "..");
const SCENES = { tokens: "tokens", gov: "governance", pat: "patterns" };
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto("http://localhost:8765/tools/covers/cars24_cards.html", { waitUntil: "networkidle" });
  await pg.evaluate(() => document.fonts.ready);
  for (const [scene, dir] of Object.entries(SCENES)) {
    await pg.evaluate((s) => show(s), scene);
    await pg.waitForTimeout(300);
    const out = path.join(ROOT, "assets", "work", dir, "card.jpg");
    await pg.screenshot({ path: out, type: "jpeg", quality: 86 });
    console.log(out, Math.round(fs.statSync(out).size / 1024), "KB");
  }
  await b.close();
})();
