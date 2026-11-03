// Render tools/video/hero.html to assets/video/hero-reel.{mp4,webm} and a poster.
// Serve the repo root on :8765 first (python3 -m http.server 8765), then:
//   node tools/video/render.js                 full render
//   node tools/video/render.js --preview 1,7.5  stills only, to $PREVIEW_DIR (default: the OS temp folder)
const path = require("path"), fs = require("fs"), os = require("os"), { spawn, spawnSync } = require("child_process");
const { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..", ".."), OUT = path.join(ROOT, "assets", "video");
const FPS = 30, W = 1600, H = 900, POSTER_T = 40.2;
(async () => {
  const args = process.argv.slice(2);
  const preview = args[0] === "--preview" ? args[1].split(",").map(Number) : null;
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await pg.goto("http://localhost:8765/tools/video/hero.html", { waitUntil: "networkidle" });
  await pg.evaluate(() => document.fonts.ready);
  await pg.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(() => 0))));
  const dur = await pg.evaluate(() => window.DUR);
  if (preview) {
    const dir = process.env.PREVIEW_DIR || os.tmpdir();
    for (const t of preview) {
      await pg.evaluate(t => seek(t), t);
      await pg.screenshot({ path: path.join(dir, `frame_${t.toFixed(2).padStart(5, "0")}.jpg`), type: "jpeg", quality: 80 });
    }
    await b.close(); return;
  }
  fs.mkdirSync(OUT, { recursive: true });
  const mp4 = path.join(OUT, "hero-reel.mp4");
  const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
    "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", mp4], { stdio: ["pipe", "inherit", "inherit"] });
  const n = Math.round(dur * FPS);
  for (let i = 0; i < n; i++) {
    await pg.evaluate(t => seek(t), i / FPS);
    const buf = await pg.screenshot({ type: "jpeg", quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    if (i % 150 === 0) console.log(`frame ${i}/${n}`);
  }
  ff.stdin.end(); await new Promise(r => ff.on("close", r));
  await pg.evaluate(t => seek(t), POSTER_T);
  await pg.screenshot({ path: path.join(OUT, "hero-poster.jpg"), type: "jpeg", quality: 82 });
  await b.close();
  spawnSync("ffmpeg", ["-y", "-loglevel", "error", "-i", mp4, "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "38", "-row-mt", "1",
    "-deadline", "good", "-cpu-used", "4", "-an", path.join(OUT, "hero-reel.webm")], { stdio: "inherit" });
  for (const f of ["hero-reel.mp4", "hero-reel.webm", "hero-poster.jpg"]) console.log(f, Math.round(fs.statSync(path.join(OUT, f)).size / 1024), "KB");
})();
