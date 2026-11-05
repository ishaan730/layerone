// Render the default link-preview card (tools/covers/og.html) to assets/og/layer-one.jpg, 1200 x 630.
// Serve the repo root on :8765 first (python3 tools/serve.py), then: node tools/covers/render_og.js
const path = require("path"), { chromium } = require("playwright");
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await pg.goto("http://localhost:8765/tools/covers/og.html", { waitUntil: "networkidle" }); await pg.evaluate(() => document.fonts.ready);
  const out = path.resolve(__dirname, "..", "..", "assets", "og", "layer-one.jpg");
  await pg.screenshot({ path: out, type: "jpeg", quality: 86 }); console.log(out); await b.close();
})();
