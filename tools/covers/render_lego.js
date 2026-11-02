// Render the boards in tools/covers/lego.html to assets/work/cars24-lego/b-<id>.jpg (cover → cover.jpg).
// Serve the repo root on :8765 first (python3 -m http.server 8765), then: node tools/covers/render_lego.js [id ...]
const path = require("path"), fs = require("fs");
const { chromium } = require("playwright");
const OUT = path.resolve(__dirname, "..", "..", "assets", "work", "cars24-lego");
(async () => {
  const only = process.argv.slice(2);
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto("http://localhost:8765/tools/covers/lego.html", { waitUntil: "networkidle" });
  await pg.evaluate(() => document.fonts.ready);
  await pg.waitForTimeout(600);
  const ids = await pg.$$eval("section.board", (s) => s.map((e) => e.id));
  for (const id of ids) {
    if (only.length && !only.includes(id)) continue;
    const out = path.join(OUT, id === "cover" ? "cover.jpg" : `b-${id}.jpg`);
    await (await pg.$("#" + id)).screenshot({ path: out, type: "jpeg", quality: 84 });
    console.log(path.basename(out), Math.round(fs.statSync(out).size / 1024), "KB");
  }
  await b.close();
})();
