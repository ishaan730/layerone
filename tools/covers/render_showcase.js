// Render the IBM client case study covers in tools/covers/showcase.html to assets/work/<slug>/cover.jpg (1920 × 1080).
// Serve the repo root on :8765 first (python3 -m http.server 8765), then: node tools/covers/render_showcase.js
const path = require("path"), fs = require("fs");
const { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..", "..");
const SCENES = { cardinal: "ibm-cardinal-health", riyadh: "ibm-riyadh-air", ops: "ibm-riyadh-air-ops" };
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto("http://localhost:8765/tools/covers/showcase.html", { waitUntil: "networkidle" });
  await pg.evaluate(() => document.fonts.ready);
  for (const [scene, slug] of Object.entries(SCENES)) {
    await pg.evaluate((s) => show(s), scene);
    await pg.waitForTimeout(300);
    const out = path.join(ROOT, "assets", "work", slug, "cover.jpg");
    await pg.screenshot({ path: out, type: "jpeg", quality: 86 });
    console.log(out, Math.round(fs.statSync(out).size / 1024), "KB");
  }
  await b.close();
})();
