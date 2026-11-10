/* Layer One Lab (v3). One script for every tool page; each module runs only when its panel is on the page.
   State lives in one object shared by all tools (a palette made on one page feeds contrast and the export kit),
   saved to localStorage and shareable as #s=<base64>. Presets are JSON patches merged into the state. No dependencies. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = $(".lx"); if (!root) return;
  var KEY = "layerone-lab-v2";

  /* ================================================================ colour maths */
  function oklchToLin(L, C, H) {
    var h = H * Math.PI / 180, a = C * Math.cos(h), b = C * Math.sin(h);
    var l_ = L + 0.3963377774 * a + 0.2158037573 * b, m_ = L - 0.1055613458 * a - 0.0638541728 * b, s_ = L - 0.0894841775 * a - 1.2914855480 * b;
    var l = l_ * l_ * l_, m = m_ * m_ * m_, s = s_ * s_ * s_;
    return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s];
  }
  function linToOklch(c) {
    var l = Math.cbrt(0.4122214708 * c[0] + 0.5363325363 * c[1] + 0.0514459929 * c[2]);
    var m = Math.cbrt(0.2119034982 * c[0] + 0.6806995451 * c[1] + 0.1073969566 * c[2]);
    var s = Math.cbrt(0.0883024619 * c[0] + 0.2817188376 * c[1] + 0.6299787005 * c[2]);
    var L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s, a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s, b = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;
    var H = Math.atan2(b, a) * 180 / Math.PI; if (H < 0) H += 360;
    return { L: L, C: Math.sqrt(a * a + b * b), H: H };
  }
  function toP3(c) { return [0.8224621 * c[0] + 0.177538 * c[1], 0.0331941 * c[0] + 0.9668058 * c[1], 0.0170827 * c[0] + 0.0723974 * c[1] + 0.9105199 * c[2]]; }
  function inG(c) { return c.every(function (v) { return v >= -0.0005 && v <= 1.0005; }); }
  function fit(L, C, H, p3) {
    var c = C, lin = oklchToLin(L, c, H);
    while (!inG(p3 ? toP3(lin) : lin) && c > 0) { c -= 0.002; lin = oklchToLin(L, c, H); }
    return { lin: lin, c: Math.max(c, 0) };
  }
  function enc(v) { v = Math.min(1, Math.max(0, v)); return v <= 0.0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - 0.055; }
  function dec(v) { return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
  function linToHex(lin) { return "#" + lin.map(function (v) { return ("0" + Math.round(enc(v) * 255).toString(16)).slice(-2); }).join(""); }
  function hexToLin(h) { return [1, 3, 5].map(function (i) { return dec(parseInt(h.substr(i, 2), 16) / 255); }); }
  function normHex(v) {
    v = String(v || "").trim().replace(/^#?/, "#").toLowerCase();
    if (/^#[0-9a-f]{3}$/.test(v)) v = "#" + v[1] + v[1] + v[2] + v[2] + v[3] + v[3];
    return /^#[0-9a-f]{6}$/.test(v) ? v : null;
  }
  function Y(h) { var c = hexToLin(h); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; }
  function ratio(a, b) { var x = Y(a), y = Y(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function apca(txt, bg) { // APCA-W3 0.0.98G-4g
    function sy(h) { var c = [1, 3, 5].map(function (i) { return Math.pow(parseInt(h.substr(i, 2), 16) / 255, 2.4); }); return 0.2126729 * c[0] + 0.7151522 * c[1] + 0.0721750 * c[2]; }
    var t = sy(txt), b = sy(bg), th = 0.022;
    t = t > th ? t : t + Math.pow(th - t, 1.414); b = b > th ? b : b + Math.pow(th - b, 1.414);
    if (Math.abs(b - t) < 0.0005) return 0;
    var o;
    if (b > t) { o = (Math.pow(b, 0.56) - Math.pow(t, 0.57)) * 1.14; o = o < 0.1 ? 0 : o - 0.027; }
    else { o = (Math.pow(b, 0.65) - Math.pow(t, 0.62)) * 1.14; o = o > -0.1 ? 0 : o + 0.027; }
    return o * 100;
  }
  function onColor(h) { return ratio(h, "#ffffff") >= ratio(h, "#0b0d12") ? "#ffffff" : "#0b0d12"; }

  /* ================================================================ state */
  var DEF = {
    tab: "palette",
    ramps: [{ name: "brand", h: 279, c: 0.25, hex: "#4736fe", pin: true }, { name: "neutral", h: 279, c: 0.014, hex: null, pin: false }],
    sel: 0, steps: "10", lmax: 0.975, lmin: 0.24, gamut: "srgb", prev: "both",
    fg: "#5b6170", bg: "#ffffff", mramp: 0, mmin: "4.5",
    t: { base: 16, ratio: "1.25", up: 6, down: 2, round: "1", lh: 1.5, lhd: 1.1, name: "shirt", font: "Schibsted Grotesk, sans-serif", text: "Ship the system, not the screenshots", fluid: false, bmin: 15, rmin: "1.2", vmin: 360, vmax: 1440, vw: 1440 },
    s: { base: "4", method: "common", count: 12, name: "shirt", pad: "", gap: "" },
    r: { base: 6, count: 5, full: true },
    n: { sep: "-", cats: "color, space, size, radius, font, line-height, shadow, border, opacity, motion, z", states: "hover, active, pressed, focus, focused, disabled, selected", depth: 6, raw: true, list: null },
    b: { items: null, draft: {} },
    k: { prefix: "" },
    vision: "none",
    g: { preset: "m3", bps: null, vw: 1280 },
    roi: { cur: "$", eng: 40, des: 6, fte: 2, monthly: 12000, rate: 90, gain: 20, a1: 40, a2: 70, a3: 85, uiEng: 25, uiDes: 50, hours: 1600 },
    fmt: {}
  };
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function merge(d, s) { Object.keys(s || {}).forEach(function (k) { if (d[k] && typeof d[k] === "object" && !Array.isArray(d[k]) && s[k] && typeof s[k] === "object" && !Array.isArray(s[k])) merge(d[k], s[k]); else if (s[k] !== undefined) d[k] = s[k]; }); return d; }
  var S = clone(DEF);
  function fromHash() {
    var m = location.hash.match(/s=([^&]+)/); if (!m) return null;
    try { return JSON.parse(decodeURIComponent(escape(atob(m[1].replace(/-/g, "+").replace(/_/g, "/"))))); } catch (e) { return null; }
  }
  var shared = fromHash();
  if (shared) { merge(S, shared); }
  else { try { var saved = JSON.parse(localStorage.getItem(KEY) || "null"); if (saved) merge(S, saved); } catch (e) {} }
  if (!S.ramps.length) S.ramps = clone(DEF.ramps);
  var saveT;
  function flush() { clearTimeout(saveT); try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function save() { clearTimeout(saveT); saveT = setTimeout(flush, 250); }
  window.addEventListener("pagehide", flush);
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") flush(); });

  var statusEl = $("[data-status]"), stT;
  function status(msg) { if (!statusEl) return; statusEl.textContent = msg; statusEl.classList.add("on"); clearTimeout(stT); stT = setTimeout(function () { statusEl.classList.remove("on"); }, 2200); }
  function copy(text, btn) {
    function done() { if (btn) { var t = btn.textContent; btn.textContent = "Copied"; btn.classList.add("ok"); setTimeout(function () { btn.textContent = t; btn.classList.remove("ok"); }, 1400); } else status("Copied"); }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done, fallback); else fallback();
    function fallback() { var ta = document.createElement("textarea"); ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0"; document.body.appendChild(ta); ta.select(); try { document.execCommand("copy"); done(); } catch (e) {} ta.remove(); }
  }
  function download(name, text) {
    var a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([text], { type: "text/plain" })); a.download = name;
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function slug(s, d) { return (String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")) || d; }

  /* ================================================================ UI helpers */
  var SYNC = [];
  function seg(panel, name, value, fn) {
    var g = $('[data-name="' + name + '"]', panel); if (!g) return function () {};
    var bs = $$("button", g);
    function set(v) { bs.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-v") === String(v) ? "true" : "false"); }); }
    if (typeof value === "function") { var get = value; SYNC.push(function () { set(get()); }); value = get(); }
    set(value);
    bs.forEach(function (b) { b.addEventListener("click", function () { set(b.getAttribute("data-v")); fn(b.getAttribute("data-v")); }); });
    return set;
  }
  function inp(panel, name) { return $('[name="' + name + '"]', panel); }
  function bindRange(panel, name, get, set, fmt) {
    var el = inp(panel, name), out = $('[data-out="' + name + '"]', panel);
    function show() { if (out) out.textContent = fmt ? fmt(+el.value) : el.value; }
    el.value = get(); show();
    el.addEventListener("input", function () { set(+el.value); show(); });
    var sync = function () { el.value = get(); show(); }; SYNC.push(sync);
    return sync;
  }

  /* ================================================================ page */
  var SLUG = { palette: "oklch-palette-generator", contrast: "color-contrast-checker", type: "type-scale-generator", space: "spacing-scale-generator",
               grid: "layout-grid-calculator", names: "design-token-name-checker", backlog: "component-request-scorecard", kit: "design-token-generator", roi: "design-system-roi-calculator" };
  var OWN = { palette: ["ramps", "sel", "steps", "lmax", "lmin", "gamut", "prev"], contrast: ["fg", "bg", "mramp", "mmin", "vision"], type: ["t"], space: ["s", "r"],
              grid: ["g"], names: ["n"], backlog: ["b"], kit: ["k"], roi: ["roi"] };
  var TOOL = root.getAttribute("data-tool") || "", renders = {};
  function renderAll() { Object.keys(renders).forEach(function (k) { if (k[0] !== "_") try { renders[k](); } catch (e) { if (window.console) console.error(e); } }); }
  function bindVal(el, get) { if (el) SYNC.push(function () { if (el.type === "checkbox") el.checked = !!get(); else el.value = get(); }); }

  /* ================================================================ export bars */
  var GEN = {}, FILES = {};
  function exportBar(key) {
    var box = $('[data-exp="' + key + '"]'); if (!box) return function () {};
    var code = $("code", box), fbs = $$("[data-fmt]", box);
    var fmt = S.fmt[key] || fbs[0].getAttribute("data-fmt");
    function render() { fbs.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-fmt") === fmt ? "true" : "false"); }); code.textContent = GEN[key](fmt); }
    fbs.forEach(function (b) { b.addEventListener("click", function () { fmt = b.getAttribute("data-fmt"); S.fmt[key] = fmt; save(); render(); }); });
    $("[data-copy]", box).addEventListener("click", function (e) { copy(GEN[key](fmt), e.currentTarget); });
    $("[data-dl]", box).addEventListener("click", function () { download(FILES[key](fmt), GEN[key](fmt)); status("Downloaded " + FILES[key](fmt)); });
    return render;
  }
  var EXT = { css: "css", tailwind: "js", json: "json", scss: "scss", csv: "csv", md: "md", txt: "txt" };

  /* ================================================================ 1. palette */
  var STEPSETS = { "10": [50, 100, 200, 300, 400, 500, 600, 700, 800, 900], "11": [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950], "12": [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950] };
  var LSHAPE = [0, 0.059, 0.147, 0.265, 0.397, 0.529, 0.647, 0.765, 0.882, 1];
  var CSHAPE = [0.22, 0.38, 0.58, 0.78, 0.94, 1, 0.94, 0.84, 0.70, 0.56];
  function shapeAt(arr, t) { var x = t * (arr.length - 1), i = Math.floor(x), f = x - i; return i >= arr.length - 1 ? arr[arr.length - 1] : arr[i] + (arr[i + 1] - arr[i]) * f; }
  function stepsOf() { return STEPSETS[S.steps] || STEPSETS["10"]; }
  function rampOf(r) {
    var st = stepsOf(), n = st.length, p3 = S.gamut === "p3", out = [];
    var pinK = -1, pin = r.hex && r.pin ? linToOklch(hexToLin(r.hex)) : null;
    for (var k = 0; k < n; k++) {
      var t = n === 1 ? 0 : k / (n - 1), L = S.lmax - (S.lmax - S.lmin) * shapeAt(LSHAPE, t), f = fit(L, r.c * shapeAt(CSHAPE, t), r.h, p3);
      out.push({ step: st[k], L: L, C: f.c, H: r.h, hex: linToHex(f.lin) });
    }
    if (pin) {
      var best = 1e9; out.forEach(function (s, k) { var d = Math.abs(s.L - pin.L); if (d < best) { best = d; pinK = k; } });
      out[pinK] = { step: out[pinK].step, L: pin.L, C: pin.C, H: pin.H, hex: r.hex, pinned: true };
    }
    return out;
  }
  function setFromHex(r, h) {
    var o = linToOklch(hexToLin(h)), st = stepsOf(), n = st.length, best = 1e9, bk = 0;
    for (var k = 0; k < n; k++) { var L = S.lmax - (S.lmax - S.lmin) * shapeAt(LSHAPE, k / (n - 1)); if (Math.abs(L - o.L) < best) { best = Math.abs(L - o.L); bk = k; } }
    r.hex = h; r.h = Math.round(o.C < 0.01 ? r.h : o.H); r.c = Math.min(0.37, +(o.C / Math.max(0.2, shapeAt(CSHAPE, bk / (n - 1)))).toFixed(3));
  }
  var PRESETS = { success: ["success", 152, 0.16], warning: ["warning", 70, 0.16], danger: ["danger", 25, 0.2], info: ["info", 245, 0.14] };

  GEN.palette = function (fmt, prefix) {
    var px = prefix ? slug(prefix, "") + "-" : "", all = S.ramps.map(function (r) { return { n: r.name, s: rampOf(r) }; });
    if (fmt === "css") {
      var o = ":root {\n" + all.map(function (r) { return r.s.map(function (s) { return "  --" + px + "color-" + r.n + "-" + s.step + ": " + s.hex + ";"; }).join("\n"); }).join("\n\n") + "\n}";
      if (S.gamut === "p3") o += "\n\n@supports (color: oklch(0% 0 0)) {\n  @media (color-gamut: p3) {\n    :root {\n" + all.map(function (r) { return r.s.map(function (s) { return "      --" + px + "color-" + r.n + "-" + s.step + ": oklch(" + (s.L * 100).toFixed(1) + "% " + s.C.toFixed(3) + " " + Math.round(s.H) + ");"; }).join("\n"); }).join("\n") + "\n    }\n  }\n}";
      return o;
    }
    if (fmt === "scss") return all.map(function (r) { return r.s.map(function (s) { return "$" + px + "color-" + r.n + "-" + s.step + ": " + s.hex + ";"; }).join("\n"); }).join("\n\n");
    if (fmt === "tailwind") return "/** tailwind.config.js */\nmodule.exports = {\n  theme: {\n    extend: {\n      colors: {\n" + all.map(function (r) { return "        " + JSON.stringify(px + r.n) + ": {\n" + r.s.map(function (s) { return "          " + s.step + ": '" + s.hex + "',"; }).join("\n") + "\n        },"; }).join("\n") + "\n      },\n    },\n  },\n};";
    var j = {}; all.forEach(function (r) { j[px + r.n] = {}; r.s.forEach(function (s) { j[px + r.n][s.step] = { $type: "color", $value: s.hex }; }); });
    return JSON.stringify({ color: j }, null, 2);
  };
  (function () {
    var P = $("#p-palette"); if (!P) return;
    var list = $("[data-ramp-list]", P), sheet = $("[data-sheet]", P), grid = $("[data-prev-grid]", P);
    var nameI = inp(P, "rname"), hexI = inp(P, "rhex"), colI = inp(P, "rcolor"), pinI = inp(P, "pin"), menu = $("[data-add-menu]", P), addB = $("[data-add-ramp]", P);
    var syncHue, syncChroma, renderExp;
    function cur() { if (S.sel >= S.ramps.length) S.sel = 0; return S.ramps[S.sel]; }
    function mid(r) { var rr = rampOf(r); var p = rr.filter(function (s) { return s.pinned; })[0]; return (p || rr[Math.floor(rr.length * 0.55)]).hex; }
    function editor() {
      var r = cur(); nameI.value = r.name; $("[data-edit-name]", P).textContent = r.name;
      var h = r.hex || mid(r); hexI.value = h.toUpperCase(); colI.value = h; pinI.checked = !!r.pin; pinI.disabled = !r.hex;
      syncHue(); syncChroma(); $("[data-del-ramp]", P).disabled = S.ramps.length < 2;
    }
    function drawList() {
      list.innerHTML = S.ramps.map(function (r, i) {
        var rr = rampOf(r), strip = rr.map(function (s) { return '<i style="background:' + s.hex + '"></i>'; }).join("");
        return '<li><button type="button" aria-pressed="' + (i === S.sel) + '" data-i="' + i + '"><span class="nm">' + esc(r.name) + '</span><span class="strip">' + strip + "</span></button></li>";
      }).join("");
      $$("button", list).forEach(function (b) { b.addEventListener("click", function () { S.sel = +b.getAttribute("data-i"); save(); renderAll(); }); });
    }
    function badge(rv) { return rv >= 7 ? "AAA" : rv >= 4.5 ? "AA" : rv >= 3 ? "AA18" : ""; }
    function drawSheet() {
      sheet.style.setProperty("--n", stepsOf().length);
      sheet.innerHTML = S.ramps.map(function (r, i) {
        return '<div class="lx-row' + (i === S.sel ? " on" : "") + '"><span class="lx-rn">' + esc(r.name) + "</span>" + rampOf(r).map(function (s) {
          var w = ratio(s.hex, "#ffffff"), k = ratio(s.hex, "#000000"), fg = w >= k ? "#fff" : "#000";
          return '<button type="button" class="lx-sw' + (s.pinned ? " pin" : "") + '" style="--c:' + s.hex + ";--t:" + fg + '" data-hex="' + s.hex + '" data-tok="' + esc(r.name) + "-" + s.step + '" title="Copy ' + s.hex + '"><span class="st">' + s.step + (s.pinned ? " ●" : "") + '</span><span class="hx">' + s.hex.slice(1) + '</span><span class="cr"><b class="' + (badge(w) ? "" : "x") + '">W ' + w.toFixed(1) + '</b><b class="' + (badge(k) ? "" : "x") + '">B ' + k.toFixed(1) + "</b></span></button>";
        }).join("") + "</div>";
      }).join("") + '<div class="lx-row lx-row-h"><span></span>' + stepsOf().map(function (s) { return "<span>" + s + "</span>"; }).join("") + "</div>";
      $$(".lx-sw", sheet).forEach(function (b) { b.addEventListener("click", function () { copy(b.getAttribute("data-hex").toUpperCase()); status("Copied " + b.getAttribute("data-tok") + " · " + b.getAttribute("data-hex").toUpperCase()); }); });
    }
    function pick(rr, t) { return rr[Math.max(0, Math.min(rr.length - 1, Math.round(t * (rr.length - 1))))].hex; }
    function neutralRamp() {
      var n = S.ramps.filter(function (r) { return /neutral|gray|grey|slate/.test(r.name); })[0];
      return rampOf(n || { h: cur().h, c: 0.012, hex: null });
    }
    function drawPrev() {
      var b = rampOf(cur()), n = neutralRamp(), modes = S.prev === "both" ? ["light", "dark"] : [S.prev];
      grid.className = "lx-prev-grid" + (modes.length === 1 ? " one" : "");
      grid.innerHTML = modes.map(function (m) {
        var L = m === "light";
        var v = L ? { bg: pick(n, 0.02), sf: "#ffffff", tx: pick(n, 0.95), mu: pick(n, 0.62), bd: pick(n, 0.18), pr: pick(b, 0.62), ph: pick(b, 0.75), sub: pick(b, 0.1), sut: pick(b, 0.78) }
                  : { bg: pick(n, 1), sf: pick(n, 0.88), tx: pick(n, 0.04), mu: pick(n, 0.38), bd: pick(n, 0.75), pr: pick(b, 0.42), ph: pick(b, 0.3), sub: pick(b, 0.92), sut: pick(b, 0.22) };
        var on = onColor(v.pr), cr = ratio(v.pr, on);
        var st = Object.keys(v).map(function (k) { return "--" + k + ":" + v[k]; }).join(";") + ";--on:" + on;
        return '<div class="lx-ui" style="' + st + '"><p class="lx-ui-k">' + (L ? "Light" : "Dark") + '</p><div class="lx-ui-card"><div class="lx-ui-top"><b>Monthly report</b><span class="lx-ui-badge">New</span></div>' +
          '<p>Every surface, border and action on this card comes from your ramps.</p><label class="lx-ui-in"><span>Workspace</span><input type="text" value="Acme Finance" aria-label="Sample input" tabindex="-1"></label>' +
          '<div class="lx-ui-alert"><b>Info.</b> Tokens update across every screen.</div><div class="lx-ui-row"><span class="lx-ui-btn">Publish</span><span class="lx-ui-sec">Preview</span><a href="#p-palette" onclick="return false" tabindex="-1">Learn more</a><span class="lx-ui-tg" aria-hidden="true"><i></i></span></div>' +
          '<p class="lx-ui-note">Button text ' + cr.toFixed(1) + ":1 " + (cr >= 4.5 ? "✓" : "· below 4.5") + "</p></div></div>";
      }).join("");
    }
    function renderAll() { drawList(); editor(); drawSheet(); drawPrev(); renderExp(); refreshMini(); }
    renders.palette = renderAll;
    SYNC.push(function () { pm.forEach(function (x) { x.setAttribute("aria-pressed", x.getAttribute("data-v") === S.prev ? "true" : "false"); }); });

    nameI.addEventListener("input", function () { cur().name = slug(nameI.value, "ramp"); $("[data-edit-name]", P).textContent = cur().name; save(); drawList(); drawSheet(); renderExp(); });
    function takeHex(v) { var h = normHex(v); if (!h) return; setFromHex(cur(), h); cur().pin = pinI.checked || !cur().hex; save(); renderAll(); }
    hexI.addEventListener("change", function () { takeHex(hexI.value); });
    hexI.addEventListener("keydown", function (e) { if (e.key === "Enter") takeHex(hexI.value); });
    colI.addEventListener("input", function () { takeHex(colI.value); });
    pinI.addEventListener("change", function () { cur().pin = pinI.checked; save(); drawList(); drawSheet(); drawPrev(); renderExp(); });
    function slid() { cur().hex = null; cur().pin = false; save(); var h = mid(cur()); hexI.value = h.toUpperCase(); colI.value = h; pinI.checked = false; pinI.disabled = true; drawList(); drawSheet(); drawPrev(); renderExp(); }
    syncHue = bindRange(P, "hue", function () { return cur().h; }, function (v) { cur().h = v; slid(); });
    syncChroma = bindRange(P, "chroma", function () { return cur().c; }, function (v) { cur().c = v; slid(); }, function (v) { return v.toFixed(3); });
    var r1 = bindRange(P, "lmax", function () { return S.lmax; }, function (v) { S.lmax = v; save(); drawList(); drawSheet(); drawPrev(); renderExp(); }, function (v) { return "L " + v.toFixed(3); });
    var r2 = bindRange(P, "lmin", function () { return S.lmin; }, function (v) { S.lmin = v; save(); drawList(); drawSheet(); drawPrev(); renderExp(); }, function (v) { return "L " + v.toFixed(2); });
    seg(P, "steps", function () { return S.steps; }, function (v) { S.steps = v; save(); renderAll(); });
    seg(P, "gamut", function () { return S.gamut; }, function (v) { S.gamut = v; save(); renderAll(); });
    var pm = $$("[data-prev-mode] button", P);
    pm.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-v") === S.prev ? "true" : "false"); b.addEventListener("click", function () { S.prev = b.getAttribute("data-v"); pm.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); save(); drawPrev(); }); });
    $("[data-del-ramp]", P).addEventListener("click", function () { if (S.ramps.length < 2) return; var gone = S.ramps.splice(S.sel, 1)[0]; S.sel = Math.max(0, S.sel - 1); save(); renderAll(); status("Deleted " + gone.name); });
    addB.addEventListener("click", function (e) { e.stopPropagation(); var o = menu.hidden; menu.hidden = !o; addB.setAttribute("aria-expanded", o ? "true" : "false"); if (o) $("button", menu).focus(); });
    document.addEventListener("click", function (e) { if (!menu.hidden && !e.target.closest(".lx-add")) { menu.hidden = true; addB.setAttribute("aria-expanded", "false"); } });
    menu.addEventListener("keydown", function (e) { if (e.key === "Escape") { menu.hidden = true; addB.focus(); } });
    $$("[data-preset]", menu).forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-preset"), base = S.ramps[0], r;
        if (k === "neutral") r = { name: "neutral", h: base.h, c: 0.014, hex: null, pin: false };
        else if (k === "custom") r = { name: "accent", h: (base.h + 160) % 360, c: 0.17, hex: null, pin: false };
        else r = { name: PRESETS[k][0], h: PRESETS[k][1], c: PRESETS[k][2], hex: null, pin: false };
        var names = S.ramps.map(function (x) { return x.name; }), nm = r.name, i = 2; while (names.indexOf(nm) > -1) nm = r.name + "-" + i++;
        r.name = nm; S.ramps.push(r); S.sel = S.ramps.length - 1; menu.hidden = true; addB.setAttribute("aria-expanded", "false"); save(); renderAll(); nameI.focus();
      });
    });

    FILES.palette = function (f) { return f === "tailwind" ? "tailwind.colors.js" : "palette." + EXT[f]; };
    renderExp = exportBar("palette");
    renders._palette = renderAll;
  })();

  /* ================================================================ 2. contrast */
  var refreshMini = function () {};
  (function () {
    var P = $("#p-contrast"); if (!P) return;
    var fgI = inp(P, "fg"), bgI = inp(P, "bg"), fgC = inp(P, "fgc"), bgC = inp(P, "bgc"), mrS = inp(P, "mramp");
    var prev = $("[data-cpreview]", P), mini = $("[data-mini]", P), mat = $("[data-matrix]", P), fix = $("[data-fix]", P);
    function setFg(h) { S.fg = h; save(); draw(); }
    function setBg(h) { S.bg = h; save(); draw(); }
    function draw() {
      fgI.value = S.fg.toUpperCase(); bgI.value = S.bg.toUpperCase(); fgC.value = S.fg; bgC.value = S.bg;
      prev.style.setProperty("--fg", S.fg); prev.style.setProperty("--bg", S.bg);
      var r = ratio(S.fg, S.bg), lc = apca(S.fg, S.bg), a = Math.abs(lc);
      $("[data-ratio]", P).textContent = r.toFixed(2) + ":1"; $("[data-apca]", P).textContent = (lc >= 0 ? "" : "−") + a.toFixed(1);
      var rows = [["AA · body text", 4.5], ["AA · large text", 3], ["AAA · body text", 7], ["AAA · large text", 4.5], ["UI parts and icons", 3]];
      $("[data-pass]", P).innerHTML = rows.map(function (x) { var ok = r >= x[1]; return '<li class="' + (ok ? "ok" : "no") + '"><span>' + (ok ? "Pass" : "Fail") + "</span>" + x[0] + "<em>" + x[1] + ":1</em></li>"; }).join("");
      var note = a >= 90 ? "Lc 90+: preferred for body text." : a >= 75 ? "Lc 75+: fine for body text." : a >= 60 ? "Lc 60+: fine for content text that isn't body copy, like labels." : a >= 45 ? "Lc 45+: headlines and large text only." : a >= 30 ? "Lc 30+: placeholder text, disabled states and non-text only." : "Below Lc 30: hard to read for anyone.";
      $("[data-apca-note]", P).textContent = "APCA: " + note;
      // fixes: nearest lightness, same hue and chroma
      var out = [];
      [4.5, 7].forEach(function (target) {
        if (r >= target) return;
        [["fg", S.fg, S.bg], ["bg", S.bg, S.fg]].forEach(function (x) {
          var o = linToOklch(hexToLin(x[1])), best = null;
          for (var d = 0.005; d <= 1; d += 0.005) {
            [o.L - d, o.L + d].forEach(function (L) { if (best || L < 0 || L > 1) return; var h = linToHex(fit(L, o.C, o.H).lin); if (ratio(h, x[2]) >= target) best = h; });
            if (best) break;
          }
          if (best) out.push({ which: x[0], hex: best, t: target, r: ratio(best, x[2]) });
        });
      });
      fix.innerHTML = out.length ? '<p class="lx-k">Closest colours that pass, in the same hue</p><div>' + out.map(function (f) {
        return '<button type="button" class="lx-fixb" data-w="' + f.which + '" data-h="' + f.hex + '"><i style="background:' + f.hex + '"></i><span><b>' + (f.which === "fg" ? "Text" : "Background") + " → " + f.hex.toUpperCase() + "</b><small>" + f.r.toFixed(2) + ":1 · " + (f.t === 7 ? "AAA" : "AA") + " body text</small></span><em>Use</em></button>";
      }).join("") + "</div>" : '<p class="lx-k ok">Passes AAA for body text. Nothing to fix.</p>';
      $$(".lx-fixb", fix).forEach(function (b) { b.addEventListener("click", function () { (b.getAttribute("data-w") === "fg" ? setFg : setBg)(b.getAttribute("data-h")); status("Applied " + b.getAttribute("data-h").toUpperCase()); }); });
      drawMatrix();
    }
    function drawMatrix() {
      var ri = Math.min(S.mramp, S.ramps.length - 1), ramp = rampOf(S.ramps[ri]), min = +S.mmin;
      var cols = [{ step: "white", hex: "#ffffff" }].concat(ramp, [{ step: "black", hex: "#000000" }]);
      var h = '<table><thead><tr><th scope="col"><span class="sr">Text \\ background</span></th>' + cols.map(function (c) { return '<th scope="col"><i style="background:' + c.hex + '"></i>' + c.step + "</th>"; }).join("") + "</tr></thead><tbody>";
      cols.forEach(function (row) {
        h += '<tr><th scope="row"><i style="background:' + row.hex + '"></i>' + row.step + "</th>";
        cols.forEach(function (c) {
          var v = ratio(row.hex, c.hex), ok = v >= min && row.hex !== c.hex;
          h += ok ? '<td><button type="button" style="background:' + c.hex + ";color:" + row.hex + '" data-f="' + row.hex + '" data-b="' + c.hex + '" aria-label="' + row.step + " on " + c.step + ", " + v.toFixed(1) + ':1">' + v.toFixed(1) + "</button></td>" : '<td class="x" aria-hidden="true">·</td>';
        });
        h += "</tr>";
      });
      mat.innerHTML = h + "</tbody></table>";
      $$("button", mat).forEach(function (b) { b.addEventListener("click", function () { S.fg = b.getAttribute("data-f"); S.bg = b.getAttribute("data-b"); save(); draw(); P.scrollIntoView({ behavior: "smooth", block: "start" }); }); });
    }
    refreshMini = function () {
      mini.innerHTML = S.ramps.map(function (r) { return '<div><span>' + esc(r.name) + "</span>" + rampOf(r).map(function (s) { return '<button type="button" style="background:' + s.hex + '" data-h="' + s.hex + '" title="' + esc(r.name) + "-" + s.step + " " + s.hex + '" aria-label="' + esc(r.name) + "-" + s.step + '"></button>'; }).join("") + "</div>"; }).join("") +
        '<div><span>base</span><button type="button" style="background:#ffffff" data-h="#ffffff" aria-label="White"></button><button type="button" style="background:#000000" data-h="#000000" aria-label="Black"></button></div>';
      $$("button", mini).forEach(function (b) { b.addEventListener("click", function (e) { (e.shiftKey ? setBg : setFg)(b.getAttribute("data-h")); }); });
      mrS.innerHTML = S.ramps.map(function (r, i) { return '<option value="' + i + '"' + (i === S.mramp ? " selected" : "") + ">" + esc(r.name) + "</option>"; }).join("");
    };
    function hexIn(el, fn) { el.addEventListener("change", function () { var h = normHex(el.value); if (h) fn(h); else el.value = (el === fgI ? S.fg : S.bg).toUpperCase(); }); el.addEventListener("keydown", function (e) { if (e.key === "Enter") el.dispatchEvent(new Event("change")); }); }
    hexIn(fgI, setFg); hexIn(bgI, setBg);
    fgC.addEventListener("input", function () { setFg(fgC.value); }); bgC.addEventListener("input", function () { setBg(bgC.value); });
    $("[data-swap]", P).addEventListener("click", function () { var t = S.fg; S.fg = S.bg; S.bg = t; save(); draw(); });
    mrS.addEventListener("change", function () { S.mramp = +mrS.value; save(); drawMatrix(); });
    seg(P, "mmin", function () { return S.mmin; }, function (v) { S.mmin = v; save(); drawMatrix(); });
    function vision() { prev.style.filter = S.vision && S.vision !== "none" ? "url(#cvd-" + S.vision + ")" : ""; var n = $("[data-vision-note]", P); if (n) n.hidden = !S.vision || S.vision === "none"; }
    seg(P, "vision", function () { return S.vision || "none"; }, function (v) { S.vision = v; save(); vision(); });
    renders.contrast = function () { refreshMini(); draw(); vision(); };
  })();

  /* ================================================================ 3. type scale */
  function typeScale(base, ratio) {
    var t = S.t, out = [], rr = +(ratio || t.ratio), unit = +t.round, prev = 0, b0 = base || t.base;
    for (var i = -t.down; i <= t.up; i++) {
      var raw = b0 * Math.pow(rr, i), px = unit ? Math.max(unit, Math.round(raw / unit) * unit) : +raw.toFixed(2);
      if (px <= prev) px = prev + (unit || 1);
      prev = px; out.push({ i: i, px: px });
    }
    var maxPx = out[out.length - 1].px;
    out.forEach(function (s) {
      var k = s.i <= 0 ? 0 : (s.px - b0) / Math.max(1, maxPx - b0), lh = t.lh + (t.lhd - t.lh) * Math.min(1, k * 1.25);
      s.lhPx = Math.round(s.px * lh / 2) * 2; s.lh = s.lhPx / s.px;
      s.ls = s.px >= 24 ? -Math.min(0.03, 0.006 + (s.px - 24) * 0.0008) : (s.px <= 13 ? 0.01 : 0);
      s.name = tName(s.i, t.up, t.down);
    });
    return out;
  }
  function tName(i, up, down) {
    var n = S.t.name;
    if (n === "num") return String(400 + i * 100);
    if (n === "role") {
      if (i === 0) return "body"; if (i < 0) return ["small", "caption", "micro"][-i - 1];
      if (i === 1 && up > 2) return "lead"; var j = up - i; return j === 0 ? "display" : "h" + j;
    }
    if (i === 0) return "md"; if (i < 0) return ["sm", "xs", "2xs"][-i - 1];
    return ["lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl"][i - 1];
  }
  function fluidPairs() {
    var hi = typeScale(), lo = typeScale(S.t.bmin, S.t.rmin);
    return hi.map(function (s, i) { var m = lo[i] || s; return { name: s.name, i: s.i, min: Math.min(m.px, s.px), max: Math.max(m.px, s.px), lh: s.lh, ls: s.ls }; });
  }
  function clampOf(min, max) {
    var r = function (v) { return +(v / 16).toFixed(4) + "rem"; };
    if (min === max || S.t.vmax <= S.t.vmin) return r(max);
    var slope = (max - min) / (S.t.vmax - S.t.vmin), icpt = min - slope * S.t.vmin;
    return "clamp(" + r(min) + ", " + r(icpt) + " + " + +(slope * 100).toFixed(4) + "vw, " + r(max) + ")";
  }
  function fluidAt(f, w) { var k = Math.max(0, Math.min(1, (w - S.t.vmin) / Math.max(1, S.t.vmax - S.t.vmin))); return f.min + (f.max - f.min) * k; }
  GEN.type = function (fmt, prefix) {
    var px = prefix ? slug(prefix, "") + "-" : "", sc = typeScale(), rem = function (v) { return +(v / 16).toFixed(4) + "rem"; };
    if (S.t.fluid) {
      var fp = fluidPairs(), note = "fluid between " + S.t.vmin + "px and " + S.t.vmax + "px screens";
      if (fmt === "css") return ":root {\n  /* " + note + " */\n" + fp.map(function (f) { return "  --" + px + "font-size-" + f.name + ": " + clampOf(f.min, f.max) + "; /* " + f.min + "–" + f.max + "px */\n  --" + px + "line-height-" + f.name + ": " + f.lh.toFixed(3) + ";" + (f.ls ? "\n  --" + px + "letter-spacing-" + f.name + ": " + f.ls.toFixed(3) + "em;" : ""); }).join("\n") + "\n}";
      if (fmt === "scss") return "// " + note + "\n" + fp.map(function (f) { return "$" + px + "font-size-" + f.name + ": " + clampOf(f.min, f.max) + ";\n$" + px + "line-height-" + f.name + ": " + f.lh.toFixed(3) + ";"; }).join("\n");
      if (fmt === "tailwind") return "/** tailwind.config.js · " + note + " */\nmodule.exports = {\n  theme: {\n    extend: {\n      fontSize: {\n" + fp.map(function (f) { return "        " + JSON.stringify(px + f.name) + ": ['" + clampOf(f.min, f.max) + "', { lineHeight: '" + f.lh.toFixed(3) + "'" + (f.ls ? ", letterSpacing: '" + f.ls.toFixed(3) + "em'" : "") + " }],"; }).join("\n") + "\n      },\n    },\n  },\n};";
      var jf = { "font-size": {}, "line-height": {} };
      fp.forEach(function (f) { jf["font-size"][px + f.name] = { $type: "dimension", $value: f.max + "px", $extensions: { "in.co.layerone.fluid": { min: f.min + "px", max: f.max + "px", minViewport: S.t.vmin + "px", maxViewport: S.t.vmax + "px", css: clampOf(f.min, f.max) } } }; jf["line-height"][px + f.name] = { $type: "number", $value: +f.lh.toFixed(3) }; });
      return JSON.stringify(jf, null, 2);
    }
    if (fmt === "css") return ":root {\n" + sc.map(function (s) { return "  --" + px + "font-size-" + s.name + ": " + rem(s.px) + "; /* " + s.px + "px */\n  --" + px + "line-height-" + s.name + ": " + rem(s.lhPx) + ";" + (s.ls ? "\n  --" + px + "letter-spacing-" + s.name + ": " + s.ls.toFixed(3) + "em;" : ""); }).join("\n") + "\n}";
    if (fmt === "scss") return sc.map(function (s) { return "$" + px + "font-size-" + s.name + ": " + rem(s.px) + ";\n$" + px + "line-height-" + s.name + ": " + rem(s.lhPx) + ";"; }).join("\n");
    if (fmt === "tailwind") return "/** tailwind.config.js */\nmodule.exports = {\n  theme: {\n    extend: {\n      fontSize: {\n" + sc.map(function (s) { return "        " + JSON.stringify(px + s.name) + ": ['" + rem(s.px) + "', { lineHeight: '" + rem(s.lhPx) + "'" + (s.ls ? ", letterSpacing: '" + s.ls.toFixed(3) + "em'" : "") + " }],"; }).join("\n") + "\n      },\n    },\n  },\n};";
    var j = { "font-size": {}, "line-height": {} };
    sc.forEach(function (s) { j["font-size"][px + s.name] = { $type: "dimension", $value: s.px + "px" }; j["line-height"][px + s.name] = { $type: "dimension", $value: s.lhPx + "px" }; });
    return JSON.stringify(j, null, 2);
  };
  (function () {
    var P = $("#p-type"); if (!P) return;
    var box = $("[data-tscale]", P), fl = $("[data-fluid]", P), renderExp;
    function drawFluid(txt) {
      var fp = fluidPairs().slice().reverse(), w = S.t.vw;
      box.innerHTML = '<div class="lx-trow lx-trow-h"><span>Token</span><span>Size</span><span>At ' + w + 'px</span><span>Sample at ' + w + "px wide</span></div>" + fp.map(function (f) {
        var now = fluidAt(f, w), big = f.max / Math.max(1, f.min) > 2.5;
        return '<div class="lx-trow' + (f.i === 0 ? " base" : "") + '"><code>font-size-' + f.name + "</code><span>" + f.min + "→" + f.max + "px<small>" + (f.min === f.max ? "fixed" : "fluid") + (big ? ' · <b class="warn" title="The largest size is more than 2.5 times the smallest. Browser zoom may not reach 200% (WCAG 1.4.4).">zoom</b>' : "") + "</small></span><span>" + now.toFixed(1) + "px<small>" + f.lh.toFixed(2) + '</small></span><p style="font-size:' + now.toFixed(2) + "px;line-height:" + f.lh + ";letter-spacing:" + f.ls + 'em">' + txt + "</p></div>";
      }).join("");
    }
    function draw() {
      var sc = typeScale(), txt = esc(S.t.text || "Ship the system, not the screenshots");
      box.style.fontFamily = S.t.font;
      if (fl) fl.hidden = !S.t.fluid;
      P.classList.toggle("is-fluid", !!S.t.fluid);
      if (S.t.fluid) { drawFluid(txt); renderExp(); return; }
      box.innerHTML = '<div class="lx-trow lx-trow-h"><span>Token</span><span>Size</span><span>Line</span><span>Sample</span></div>' + sc.slice().reverse().map(function (s) {
        return '<div class="lx-trow' + (s.i === 0 ? " base" : "") + '"><code>font-size-' + s.name + '</code><span>' + s.px + "px<small>" + (s.px / 16).toFixed(3).replace(/\.?0+$/, "") + "rem</small></span><span>" + s.lhPx + "px<small>" + s.lh.toFixed(2) + (s.ls ? " · " + s.ls.toFixed(3) + "em" : "") + '</small></span><p style="font-size:' + s.px + "px;line-height:" + s.lh + ";letter-spacing:" + s.ls + 'em">' + txt + "</p></div>";
      }).join("");
      renderExp();
    }
    renders.type = draw;
    function up() { save(); draw(); }
    bindRange(P, "tbase", function () { return S.t.base; }, function (v) { S.t.base = v; up(); });
    bindRange(P, "tup", function () { return S.t.up; }, function (v) { S.t.up = v; up(); });
    bindRange(P, "tdown", function () { return S.t.down; }, function (v) { S.t.down = v; up(); });
    bindRange(P, "tlh", function () { return S.t.lh; }, function (v) { S.t.lh = v; up(); }, function (v) { return v.toFixed(2); });
    bindRange(P, "tlhd", function () { return S.t.lhd; }, function (v) { S.t.lhd = v; up(); }, function (v) { return v.toFixed(2); });
    var rs = inp(P, "tratio"); rs.value = S.t.ratio; bindVal(rs, function () { return S.t.ratio; }); rs.addEventListener("change", function () { S.t.ratio = rs.value; up(); });
    var fs = inp(P, "tfont"); fs.value = S.t.font; bindVal(fs, function () { return S.t.font; }); fs.addEventListener("change", function () { S.t.font = fs.value; up(); });
    var tx = inp(P, "ttext"); tx.value = S.t.text; bindVal(tx, function () { return S.t.text; }); tx.addEventListener("input", function () { S.t.text = tx.value; up(); });
    seg(P, "tround", function () { return S.t.round; }, function (v) { S.t.round = v; up(); });
    var fx = inp(P, "tfluid"); if (fx) { fx.checked = S.t.fluid; bindVal(fx, function () { return S.t.fluid; }); fx.addEventListener("change", function () { S.t.fluid = fx.checked; up(); }); }
    if (inp(P, "tbmin")) {
      bindRange(P, "tbmin", function () { return S.t.bmin; }, function (v) { S.t.bmin = v; up(); });
      bindRange(P, "tvmin", function () { return S.t.vmin; }, function (v) { S.t.vmin = v; up(); });
      bindRange(P, "tvmax", function () { return S.t.vmax; }, function (v) { S.t.vmax = v; up(); });
      bindRange(P, "tvw", function () { return S.t.vw; }, function (v) { S.t.vw = v; up(); });
      var rm = inp(P, "trmin"); rm.value = S.t.rmin; bindVal(rm, function () { return S.t.rmin; }); rm.addEventListener("change", function () { S.t.rmin = rm.value; up(); });
    }
    seg(P, "tname", function () { return S.t.name; }, function (v) { S.t.name = v; up(); });
    FILES.type = function (f) { return f === "tailwind" ? "tailwind.type.js" : "type." + EXT[f]; };
    renderExp = exportBar("type");
  })();

  /* ================================================================ 4. spacing and radius */
  function spaceScale() {
    var b = +S.s.base, n = S.s.count, m;
    if (S.s.method === "linear") { m = []; for (var i = 1; i <= n; i++) m.push(i); }
    else if (S.s.method === "double") m = [1, 2, 4, 8, 16, 32, 64, 128, 256];
    else if (S.s.method === "fib") m = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597];
    else m = [0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48];
    var vals = m.slice(0, n).map(function (x) { return Math.round(x * b * 2) / 2; }).filter(function (v) { return v <= 640; });
    var mid = 0, best = 1e9; vals.forEach(function (v, i) { if (Math.abs(v - 16) < best) { best = Math.abs(v - 16); mid = i; } });
    var below = ["sm", "xs", "2xs", "3xs", "4xs", "5xs"], above = ["lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl", "9xl", "10xl", "11xl", "12xl", "13xl", "14xl"];
    return vals.map(function (v, i) {
      var name = S.s.name === "px" ? String(v).replace(".", "_") : S.s.name === "mult" ? String(+(v / b).toFixed(2)).replace(".", "_") : (i === mid ? "md" : i < mid ? below[mid - i - 1] : above[i - mid - 1]);
      return { name: name, px: v };
    });
  }
  function radiusScale() {
    var m = [0.5, 1, 1.5, 2, 3, 4, 6], nm = ["xs", "sm", "md", "lg", "xl", "2xl", "3xl"], o = [];
    for (var i = 0; i < S.r.count; i++) o.push({ name: nm[i], px: Math.max(1, Math.round(S.r.base * m[i])) });
    if (S.r.full) o.push({ name: "full", px: 9999 });
    return o;
  }
  GEN.space = function (fmt, prefix) {
    var px = prefix ? slug(prefix, "") + "-" : "", sc = spaceScale(), rs = radiusScale(), u = function (v) { return v === 9999 ? "9999px" : (v === 0 ? "0" : +(v / 16).toFixed(4) + "rem"); };
    if (fmt === "css") return ":root {\n" + sc.map(function (s) { return "  --" + px + "space-" + s.name + ": " + u(s.px) + "; /* " + s.px + "px */"; }).join("\n") + "\n\n" + rs.map(function (r) { return "  --" + px + "radius-" + r.name + ": " + (r.px === 9999 ? "9999px" : r.px + "px") + ";"; }).join("\n") + "\n}";
    if (fmt === "scss") return sc.map(function (s) { return "$" + px + "space-" + s.name + ": " + u(s.px) + ";"; }).join("\n") + "\n\n" + rs.map(function (r) { return "$" + px + "radius-" + r.name + ": " + r.px + "px;"; }).join("\n");
    if (fmt === "tailwind") return "/** tailwind.config.js */\nmodule.exports = {\n  theme: {\n    extend: {\n      spacing: {\n" + sc.map(function (s) { return "        " + JSON.stringify(px + s.name) + ": '" + u(s.px) + "',"; }).join("\n") + "\n      },\n      borderRadius: {\n" + rs.map(function (r) { return "        " + JSON.stringify(px + r.name) + ": '" + r.px + "px',"; }).join("\n") + "\n      },\n    },\n  },\n};";
    var j = { space: {}, radius: {} };
    sc.forEach(function (s) { j.space[px + s.name] = { $type: "dimension", $value: s.px + "px" }; }); rs.forEach(function (r) { j.radius[px + r.name] = { $type: "dimension", $value: r.px + "px" }; });
    return JSON.stringify(j, null, 2);
  };
  (function () {
    var P = $("#p-space"); if (!P) return;
    var bars = $("[data-sbars]", P), demo = $(".lx-demo-card", P), padS = $("[data-pad]", P), gapS = $("[data-gap]", P), radii = $("[data-radii]", P), renderExp;
    function draw() {
      var sc = spaceScale(), max = sc[sc.length - 1].px;
      bars.innerHTML = '<p class="lx-k">' + sc.length + " spacing tokens</p>" + sc.map(function (s) { return '<div><code>space-' + s.name + '</code><i style="width:' + Math.max(0.6, s.px / max * 100) + '%"></i><span>' + s.px + "</span></div>"; }).join("");
      function opts(sel, cur, def) { sel.innerHTML = sc.map(function (s) { return '<option value="' + s.px + '"' + (String(s.px) === String(cur || def) ? " selected" : "") + ">space-" + s.name + " · " + s.px + "px</option>"; }).join(""); return +sel.value; }
      var near = function (t) { var b = sc[0].px, d = 1e9; sc.forEach(function (s) { if (Math.abs(s.px - t) < d) { d = Math.abs(s.px - t); b = s.px; } }); return b; };
      var pad = opts(padS, S.s.pad, near(24)), gap = opts(gapS, S.s.gap, near(12));
      demo.style.padding = pad + "px"; demo.style.gap = gap + "px";
      var rs = radiusScale(), rmd = (rs[2] || rs[rs.length - 1]).px;
      demo.style.borderRadius = Math.min(rmd, 32) + "px";
      radii.innerHTML = '<p class="lx-k">Radius</p><div>' + rs.map(function (r) { return '<figure><i style="border-radius:' + Math.min(r.px, 999) + 'px"></i><figcaption><code>radius-' + r.name + "</code>" + (r.px === 9999 ? "9999" : r.px + "px") + "</figcaption></figure>"; }).join("") + "</div>";
      renderExp();
    }
    renders.space = draw;
    function up() { save(); draw(); }
    seg(P, "sbase", function () { return S.s.base; }, function (v) { S.s.base = v; S.s.pad = S.s.gap = ""; up(); });
    seg(P, "sname", function () { return S.s.name; }, function (v) { S.s.name = v; up(); });
    var ms = inp(P, "smethod"); ms.value = S.s.method; bindVal(ms, function () { return S.s.method; }); ms.addEventListener("change", function () { S.s.method = ms.value; S.s.pad = S.s.gap = ""; up(); });
    bindRange(P, "scount", function () { return S.s.count; }, function (v) { S.s.count = v; up(); });
    bindRange(P, "rbase", function () { return S.r.base; }, function (v) { S.r.base = v; up(); });
    bindRange(P, "rcount", function () { return S.r.count; }, function (v) { S.r.count = v; up(); });
    var rf = inp(P, "rfull"); rf.checked = S.r.full; bindVal(rf, function () { return S.r.full; }); rf.addEventListener("change", function () { S.r.full = rf.checked; up(); });
    padS.addEventListener("change", function () { S.s.pad = padS.value; up(); }); gapS.addEventListener("change", function () { S.s.gap = gapS.value; up(); });
    FILES.space = function (f) { return f === "tailwind" ? "tailwind.spacing.js" : "spacing." + EXT[f]; };
    renderExp = exportBar("space");
  })();

  /* ================================================================ 5. token name linter */
  var EXAMPLE = ["--color-action-primary", "--color-action-primary-hover", "--colorTextMuted", "--btn-bg-primary", "--color-surface-hover-brand", "--color-blue-500", "--color-button-blue", "--Space_MD", "--space-md", "color.text.secondary", "--radius-sm", "--shadow-elevation-card-modal-dialog-overlay-strong", "--font-size-lg", "--Font-Size-LG", "--border-width-1", "--primary-text-color", "--color-feedback-error-text", "--color-border-focus-disabled", "--z-modal", "--clr-sec-bg"].join("\n");
  var ABBR = { bg: "background", btn: "button", txt: "text", clr: "color", col: "color", sec: "secondary", prim: "primary", pri: "primary", brdr: "border", bdr: "border", desc: "description", img: "image", nav: "navigation", err: "error", warn: "warning", hov: "hover", dis: "disabled" };
  var RAW = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "teal", "cyan", "indigo", "violet", "gray", "grey", "black", "white", "lime", "amber"];
  var SEMW = ["action", "text", "surface", "background", "border", "button", "primary", "secondary", "brand", "error", "success", "warning", "info", "link", "icon", "feedback", "input", "card"];
  function parseTokens(raw) {
    raw = String(raw || "").trim(); if (!raw) return [];
    if (/^[\[{]/.test(raw)) {
      try {
        var j = JSON.parse(raw), out = [];
        (function walk(o, p) {
          if (Array.isArray(o)) { o.forEach(function (x) { if (typeof x === "string") out.push(x); }); return; }
          if (o && typeof o === "object") {
            if ("$value" in o || "value" in o) { out.push(p.join(S.n.sep)); return; }
            Object.keys(o).forEach(function (k) { if (k[0] !== "$") walk(o[k], p.concat(k)); });
          }
        })(j, []);
        return out;
      } catch (e) {}
    }
    return raw.split(/\n|;/).map(function (l) {
      l = l.replace(/\/\*.*?\*\//g, "").replace(/\/\/.*$/, "").trim();
      if (!l || /^[{}]$/.test(l) || /^:root|^@/.test(l)) return "";
      return l.split(":")[0].trim().replace(/^(--|\$|@)/, "").replace(/[,'"]/g, "").trim();
    }).filter(Boolean);
  }
  function lint(list) {
    var sep = S.n.sep, cats = S.n.cats.split(",").map(function (s) { return s.trim().toLowerCase(); }).filter(Boolean), states = S.n.states.split(",").map(function (s) { return s.trim().toLowerCase(); }).filter(Boolean);
    var seen = {};
    return list.map(function (name) {
      var issues = [], sev = 0;
      function add(level, msg) { issues.push([level, msg]); sev = Math.max(sev, level === "err" ? 2 : 1); }
      var words = name.replace(/([a-z0-9])([A-Z])/g, "$1 $2").split(/[\s\-_.\/]+/).filter(Boolean);
      if (/[A-Z]/.test(name)) add("err", "Uses capital letters");
      if (/\s/.test(name)) add("err", "Contains spaces");
      var seps = (name.replace(/(\d)\.(\d)/g, "$1$2").match(/[\-_.\/]/g) || []).filter(function (c) { return c !== sep; });
      if (seps.length) add("err", "Uses “" + seps.filter(function (c, i, a) { return a.indexOf(c) === i; }).join(" ") + "” instead of “" + sep + "”");
      if (/[^A-Za-z0-9\-_.\/\s]/.test(name)) add("err", "Has characters other than letters, numbers and the separator");
      var p = words.map(function (w) { return w.toLowerCase(); });
      p = p.map(function (w) { if (ABBR[w]) { add("warn", "“" + w + "” is an abbreviation; write “" + ABBR[w] + "”"); return ABBR[w]; } return w; });
      if (cats.length && cats.indexOf(p[0]) < 0 && !(p[0] === "line" && p[1] === "height")) {
        var ci = -1; p.some(function (w, i) { if (cats.indexOf(w) > -1) { ci = i; return true; } });
        if (ci > 0) { add("warn", "Category “" + p[ci] + "” should come first"); var c = p.splice(ci, 1)[0]; p.unshift(c); }
        else add("warn", "Doesn't start with a category (" + cats.slice(0, 4).join(", ") + "…)");
      }
      var st = p.filter(function (w) { return states.indexOf(w) > -1; });
      if (st.length > 1) add("warn", "Has more than one state: " + st.join(", "));
      if (st.length === 1 && p[p.length - 1] !== st[0]) { add("warn", "State “" + st[0] + "” should be last"); p.splice(p.indexOf(st[0]), 1); p.push(st[0]); }
      if (p.length > S.n.depth) add("warn", p.length + " parts; your limit is " + S.n.depth);
      if (S.n.raw && p.some(function (w) { return RAW.indexOf(w) > -1; }) && p.some(function (w) { return SEMW.indexOf(w) > -1; })) add("warn", "A semantic token names a raw colour. Name it for its job, not its hue");
      var fixed = p.join(sep);
      if (seen[fixed]) add("err", "Duplicate of “" + seen[fixed] + "” once fixed"); else seen[fixed] = name;
      return { name: name, fixed: fixed, issues: issues, sev: sev };
    });
  }
  (function () {
    var P = $("#p-names"); if (!P) return;
    var ta = inp(P, "nlist"), res = $("[data-nresult]", P), sum = $("[data-nsum]", P), sc = $("[data-nscore]", P), renderExp, last = [];
    function draw() {
      if (S.n.list == null) { S.n.list = EXAMPLE; ta.value = EXAMPLE; }
      var list = parseTokens(S.n.list); last = lint(list);
      $("[data-nparse]", P).textContent = list.length ? list.length + " tokens found." : "Paste one token per line, a CSS block, or a JSON token file.";
      var ok = last.filter(function (x) { return !x.sev; }).length, w = last.filter(function (x) { return x.sev === 1; }).length, e = last.filter(function (x) { return x.sev === 2; }).length;
      sc.textContent = last.length ? Math.round(ok / last.length * 100) + "% clean" : "";
      sum.innerHTML = last.length ? '<span class="ok">' + ok + " clean</span><span class=\"warn\">" + w + " warnings</span><span class=\"err\">" + e + " errors</span>" : "";
      res.innerHTML = last.length ? last.slice().sort(function (a, b) { return b.sev - a.sev; }).map(function (x) {
        return '<li class="s' + x.sev + '"><div class="nm"><span class="ic" aria-hidden="true">' + (x.sev === 2 ? "✕" : x.sev ? "!" : "✓") + "</span><code>" + esc(x.name) + "</code>" + (x.fixed !== x.name && x.sev ? '<span class="to">→</span><code class="fx">' + esc(x.fixed) + "</code>" : "") + "</div>" +
          (x.issues.length ? "<ul>" + x.issues.map(function (i) { return '<li class="' + i[0] + '">' + esc(i[1]) + "</li>"; }).join("") + "</ul>" : "") + "</li>";
      }).join("") : '<li class="empty">No tokens yet. Paste some, or load the messy example.</li>';
      renderExp();
    }
    renders.names = draw;
    ta.value = S.n.list == null ? EXAMPLE : S.n.list; bindVal(ta, function () { return S.n.list == null ? EXAMPLE : S.n.list; });
    var dt; ta.addEventListener("input", function () { S.n.list = ta.value; save(); clearTimeout(dt); dt = setTimeout(draw, 180); });
    $("[data-nexample]", P).addEventListener("click", function () { ta.value = S.n.list = EXAMPLE; save(); draw(); });
    $("[data-nclear]", P).addEventListener("click", function () { ta.value = S.n.list = ""; save(); draw(); ta.focus(); });
    seg(P, "nsep", function () { return S.n.sep; }, function (v) { S.n.sep = v; save(); draw(); });
    ["ncats", "nstates"].forEach(function (n) { var el = inp(P, n), k = n === "ncats" ? "cats" : "states"; el.value = S.n[k]; bindVal(el, function () { return S.n[k]; }); el.addEventListener("input", function () { S.n[k] = el.value; save(); draw(); }); });
    bindRange(P, "ndepth", function () { return S.n.depth; }, function (v) { S.n.depth = v; save(); draw(); });
    var rw = inp(P, "nraw"); rw.checked = S.n.raw; bindVal(rw, function () { return S.n.raw; }); rw.addEventListener("change", function () { S.n.raw = rw.checked; save(); draw(); });
    GEN.names = function (fmt) {
      if (!last.length) return fmt === "json" ? "{}" : "# Paste tokens to get a fixed list";
      if (fmt === "json") { var o = {}; last.forEach(function (x) { if (x.fixed !== x.name) o[x.name] = x.fixed; }); return JSON.stringify(o, null, 2); }
      return last.map(function (x) { return x.fixed; }).filter(function (v, i, a) { return a.indexOf(v) === i; }).join("\n");
    };
    FILES.names = function (f) { return f === "json" ? "token-renames.json" : "tokens-fixed.txt"; };
    renderExp = exportBar("names");
  })();

  /* ================================================================ 6. backlog */
  var QS = ["where", "reuse", "exists", "effort"];
  var QL = { where: { 20: "Main products", 15: "Smaller products", 5: "One team", x: "Nowhere" }, reuse: { 20: "Many teams", 15: "A few teams", 5: "One team", x: "One product" }, exists: { 15: "No", 10: "Partly", 5: "Mostly", x: "Fully solved" }, effort: { 15: "Under a week", 10: "1–3 weeks", 5: "3+ weeks", x: "Not worth it" } };
  var BEX = [["Date range picker", "Loans", "20", "20", "15", "10"], ["Data table with filters", "Operations", "20", "20", "10", "5"], ["Promo banner, Diwali", "Marketing", "15", "5", "10", "15"], ["OTP input", "Login", "20", "15", "5", "15"], ["3D car viewer", "Buy", "5", "5", "15", "5"], ["Secondary button", "Sell", "20", "20", "x", "15"]];
  function bexamples() { return BEX.map(function (e, i) { return { id: "ex" + Date.now().toString(36) + i, name: e[0], team: e[1], a: { where: e[2], reuse: e[3], exists: e[4], effort: e[5] } }; }); }
  function score(a) {
    var tot = 0, x = false, n = 0; QS.forEach(function (q) { var v = a[q]; if (v === undefined || v === null || v === "") return; n++; if (v === "x") x = true; else tot += +v; });
    var v = x ? ["no", "Won't fix", "Rejected: build it outside the system"] : n < 4 ? ["", "Answer all four", "The score only means something once every question has an answer."] : tot >= 55 ? ["hi", "High", "Accept. The system team builds it first."] : tot >= 40 ? ["md", "Medium", "Accept, after high-priority work. The team can contribute."] : ["lo", "Low", "Defer. The team builds it as a custom component."];
    return { total: x ? null : tot, done: n === 4, v: v };
  }
  (function () {
    var P = $("#p-backlog"); if (!P) return;
    var form = $("[data-bform]", P), list = $("[data-blist]", P), stats = $("[data-bstats]", P), nameI = inp(P, "bname"), teamI = inp(P, "bteam"), saveB = $("[data-bsave]", P), cancelB = $("[data-bcancel]", P), renderExp;
    var draft = S.b.draft || {}, editing = null, setters = {};
    QS.forEach(function (q) { setters[q] = seg(P, q, draft[q] || "", function (v) { draft[q] = v; S.b.draft = draft; save(); live(); }); });
    nameI.value = draft.name || ""; teamI.value = draft.team || "";
    nameI.addEventListener("input", function () { draft.name = nameI.value; S.b.draft = draft; save(); });
    teamI.addEventListener("input", function () { draft.team = teamI.value; S.b.draft = draft; save(); });
    function live() { var s = score(draft); $("[data-blive]", P).textContent = s.total === null ? "—" : s.total; var vv = $("[data-bverdict]", P); vv.textContent = s.v[1]; vv.className = "v " + s.v[0]; }
    function resetForm() { draft = {}; S.b.draft = draft; editing = null; nameI.value = teamI.value = ""; QS.forEach(function (q) { setters[q](""); }); saveB.textContent = "Add to backlog"; cancelB.hidden = true; $("[data-bform-title]", P).textContent = "New request"; live(); save(); }
    form.addEventListener("submit", function () {
      var nm = nameI.value.trim(); if (!nm) { nameI.focus(); status("Name the request first"); return; }
      if (!score(draft).done) { status("Answer all four questions"); return; }
      var item = { id: editing || Date.now().toString(36), name: nm, team: teamI.value.trim(), a: { where: draft.where, reuse: draft.reuse, exists: draft.exists, effort: draft.effort } };
      if (editing) S.b.items = S.b.items.map(function (x) { return x.id === editing ? item : x; }); else S.b.items.push(item);
      status(editing ? "Saved" : "Added " + nm); resetForm(); draw();
    });
    cancelB.addEventListener("click", resetForm);
    function ranked() { if (!S.b.items) S.b.items = bexamples(); return S.b.items.map(function (x) { return { x: x, s: score(x.a) }; }).sort(function (a, b) { return (b.s.total === null ? -1 : b.s.total) - (a.s.total === null ? -1 : a.s.total); }); }
    function draw() {
      var r = ranked(), c = { hi: 0, md: 0, lo: 0, no: 0 }; r.forEach(function (y) { c[y.s.v[0]]++; });
      stats.innerHTML = r.length ? '<span class="hi">' + c.hi + ' high</span><span class="md">' + c.md + ' medium</span><span class="lo">' + c.lo + ' low</span><span class="no">' + c.no + " won't fix</span>" : "";
      list.innerHTML = r.length ? r.map(function (y, i) {
        var a = y.x.a, why = QS.map(function (q) { return QL[q][a[q]]; }).join(" · ");
        return '<li class="' + y.s.v[0] + '"><span class="rk">' + (y.s.total === null ? "—" : i + 1) + '</span><div class="bd"><b>' + esc(y.x.name) + "</b><small>" + (y.x.team ? esc(y.x.team) + " · " : "") + why + '</small><span class="bar"><i style="width:' + ((y.s.total || 0) / 70 * 100) + '%"></i></span></div><span class="sc">' + (y.s.total === null ? "✕" : y.s.total) + '</span><span class="v ' + y.s.v[0] + '">' + y.s.v[1] + '</span><div class="act"><button type="button" class="lx-icon" data-ed="' + y.x.id + '" aria-label="Edit ' + esc(y.x.name) + '">✎</button><button type="button" class="lx-icon" data-rm="' + y.x.id + '" aria-label="Remove ' + esc(y.x.name) + '">✕</button></div></li>';
      }).join("") : '<li class="empty">No requests yet. Add one on the left, or load the examples.</li>';
      $$("[data-rm]", list).forEach(function (b) { b.addEventListener("click", function () { S.b.items = S.b.items.filter(function (x) { return x.id !== b.getAttribute("data-rm"); }); save(); draw(); }); });
      $$("[data-ed]", list).forEach(function (b) {
        b.addEventListener("click", function () {
          var it = S.b.items.filter(function (x) { return x.id === b.getAttribute("data-ed"); })[0]; if (!it) return;
          editing = it.id; draft = { name: it.name, team: it.team, where: it.a.where, reuse: it.a.reuse, exists: it.a.exists, effort: it.a.effort }; S.b.draft = draft;
          nameI.value = it.name; teamI.value = it.team; QS.forEach(function (q) { setters[q](it.a[q]); }); live();
          saveB.textContent = "Save changes"; cancelB.hidden = false; $("[data-bform-title]", P).textContent = "Edit request"; nameI.focus();
        });
      });
      save(); renderExp();
    }
    renders.backlog = function () { live(); draw(); };
    $("[data-bexample]", P).addEventListener("click", function () {
      S.b.items = (S.b.items || []).concat(bexamples());
      draw(); status("Loaded 6 example requests");
    });
    $("[data-bclear]", P).addEventListener("click", function () { if (!(S.b.items || []).length || confirm("Remove every request from the backlog?")) { S.b.items = []; draw(); } });
    GEN.backlog = function (fmt) {
      var r = ranked();
      if (fmt === "json") return JSON.stringify(r.map(function (y) { return { name: y.x.name, team: y.x.team, score: y.s.total, verdict: y.s.v[1], answers: y.x.a }; }), null, 2);
      if (fmt === "csv") return "Rank,Request,Team,Score,Verdict,Where,Reuse,Exists,Effort\n" + r.map(function (y, i) { var a = y.x.a; return [y.s.total === null ? "" : i + 1, y.x.name, y.x.team, y.s.total === null ? "" : y.s.total, y.s.v[1], QL.where[a.where], QL.reuse[a.reuse], QL.exists[a.exists], QL.effort[a.effort]].map(function (v) { v = String(v == null ? "" : v); return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }).join(","); }).join("\n");
      if (!r.length) return "| # | Request | Team | Score | Verdict |\n|---|---|---|---|---|";
      return "| # | Request | Team | Score | Verdict |\n|---|---|---|---|---|\n" + r.map(function (y, i) { return "| " + (y.s.total === null ? "—" : i + 1) + " | " + y.x.name + " | " + (y.x.team || "") + " | " + (y.s.total === null ? "✕" : y.s.total + " / 70") + " | " + y.s.v[1] + " |"; }).join("\n");
    };
    FILES.backlog = function (f) { return "backlog." + EXT[f]; };
    renderExp = exportBar("backlog");
  })();

  /* ================================================================ 7. export kit */
  (function () {
    var P = $("#p-kit"); if (!P) return;
    var box = $("[data-kit]", P), pre = inp(P, "kprefix"), renderExp;
    pre.value = S.k.prefix;
    function draw() {
      var sc = spaceScale(), ts = typeScale(), rs = radiusScale();
      box.innerHTML = [
        ["palette", "Palette", S.ramps.length + " ramps × " + stepsOf().length + " steps", S.ramps.map(function (r) { return '<span class="strip">' + rampOf(r).map(function (s) { return '<i style="background:' + s.hex + '"></i>'; }).join("") + "</span>"; }).join("")],
        ["type", "Type scale", ts.length + " sizes, " + ts[0].px + "–" + ts[ts.length - 1].px + "px", '<span class="ts">' + ts.slice(-4).map(function (s) { return '<b style="font-size:' + Math.min(s.px, 40) + 'px">Aa</b>'; }).join("") + "</span>"],
        ["space", "Spacing", sc.length + " steps, " + sc[0].px + "–" + sc[sc.length - 1].px + "px", '<span class="sp">' + sc.slice(0, 10).map(function (s) { return '<i style="height:' + Math.min(40, s.px) + 'px"></i>'; }).join("") + "</span>"],
        ["space", "Radius", rs.length + " steps", '<span class="rd">' + rs.slice(0, 5).map(function (r) { return '<i style="border-radius:' + Math.min(r.px, 20) + 'px"></i>'; }).join("") + "</span>"],
        ["grid", "Layout grid", gridBps().length + " breakpoints", '<span class="gd">' + gridBps().map(function (b) { return "<i>" + b.cols + "</i>"; }).join("") + "</span>"]
      ].map(function (c) { return '<a class="lx-kc" href="/lab/' + SLUG[c[0]] + '"><span class="h"><b>' + c[1] + "</b><small>" + c[2] + '</small></span><span class="vis">' + c[3] + '</span><span class="e">Edit →</span></a>'; }).join("");
      renderExp();
    }
    renders.kit = draw;
    pre.addEventListener("input", function () { S.k.prefix = slug(pre.value, ""); save(); renderExp(); });
    GEN.kit = function (fmt) {
      var p = S.k.prefix, head = "Layer One Lab · design tokens · " + new Date().toISOString().slice(0, 10);
      if (fmt === "json") { var o = {}; [GEN.palette, GEN.type, GEN.space, GEN.grid].forEach(function (g) { merge(o, JSON.parse(g("json", p))); }); return JSON.stringify(o, null, 2); }
      if (fmt === "tailwind") {
        var grab = function (s) { return s.split("extend: {\n")[1].split("\n    },\n  },\n};")[0]; };
        return "/** " + head + " · tailwind.config.js */\nmodule.exports = {\n  theme: {\n    extend: {\n" + [GEN.palette, GEN.type, GEN.space, GEN.grid].map(function (g) { return grab(g("tailwind", p)); }).join("\n") + "\n    },\n  },\n};";
      }
      if (fmt === "scss") return "// " + head + "\n\n// Colour\n" + GEN.palette("scss", p) + "\n\n// Type\n" + GEN.type("scss", p) + "\n\n// Spacing and radius\n" + GEN.space("scss", p) + "\n\n// Layout grid\n" + GEN.grid("scss", p);
      var strip = function (s) { return s.replace(/^:root \{\n|\n\}$/g, ""); }, pal = GEN.palette("css", p), extra = "";
      var i = pal.indexOf("\n\n@supports"); if (i > -1) { extra = pal.slice(i); pal = pal.slice(0, i); }
      return "/* " + head + " */\n:root {\n  /* Colour */\n" + strip(pal) + "\n\n  /* Type */\n" + strip(GEN.type("css", p)) + "\n\n  /* Spacing and radius */\n" + strip(GEN.space("css", p)) + "\n}" + extra + "\n\n/* Layout grid */\n" + GEN.grid("css", p);
    };
    FILES.kit = function (f) { return f === "tailwind" ? "tailwind.config.js" : "tokens." + EXT[f]; };
    renderExp = exportBar("kit");
  })();

  /* ================================================================ 8. layout grid */
  var GRIDP = {
    m3: [{ n: "compact", min: 0, cols: 4, gut: 16, mar: 16, max: 0 }, { n: "medium", min: 600, cols: 8, gut: 24, mar: 24, max: 0 }, { n: "expanded", min: 840, cols: 12, gut: 24, mar: 24, max: 0 },
         { n: "large", min: 1200, cols: 12, gut: 24, mar: 24, max: 0 }, { n: "xlarge", min: 1600, cols: 12, gut: 24, mar: 24, max: 0 }],
    bootstrap: [{ n: "xs", min: 0, cols: 12, gut: 24, mar: 12, max: 0 }, { n: "sm", min: 576, cols: 12, gut: 24, mar: 12, max: 540 }, { n: "md", min: 768, cols: 12, gut: 24, mar: 12, max: 720 },
                { n: "lg", min: 992, cols: 12, gut: 24, mar: 12, max: 960 }, { n: "xl", min: 1200, cols: 12, gut: 24, mar: 12, max: 1140 }, { n: "xxl", min: 1400, cols: 12, gut: 24, mar: 12, max: 1320 }],
    carbon: [{ n: "sm", min: 0, cols: 4, gut: 32, mar: 0, max: 0 }, { n: "md", min: 672, cols: 8, gut: 32, mar: 16, max: 0 }, { n: "lg", min: 1056, cols: 16, gut: 32, mar: 16, max: 0 },
             { n: "xlg", min: 1312, cols: 16, gut: 32, mar: 16, max: 0 }, { n: "max", min: 1584, cols: 16, gut: 32, mar: 24, max: 1584 }],
    product: [{ n: "phone", min: 0, cols: 4, gut: 16, mar: 16, max: 0 }, { n: "tablet", min: 600, cols: 8, gut: 16, mar: 24, max: 0 }, { n: "laptop", min: 1024, cols: 12, gut: 24, mar: 32, max: 0 },
              { n: "desktop", min: 1440, cols: 12, gut: 24, mar: 32, max: 1440 }]
  };
  function gridBps() { if (!S.g.bps || !S.g.bps.length) S.g.bps = clone(GRIDP[S.g.preset] || GRIDP.m3); return S.g.bps.slice().sort(function (a, b) { return a.min - b.min; }); }
  function gridAt(w) {
    var bs = gridBps(), b = bs[0]; bs.forEach(function (x) { if (x.min <= w) b = x; });
    var box = b.max ? Math.min(w, b.max) : w, content = Math.max(0, box - 2 * b.mar), col = (content - (b.cols - 1) * b.gut) / b.cols;
    return { bp: b, box: box, content: content, col: col };
  }
  GEN.grid = function (fmt, prefix) {
    var px = prefix ? slug(prefix, "") + "-" : "", bs = gridBps(), first = bs[0];
    var vars = function (b, ind) { return ind + "--" + px + "grid-columns: " + b.cols + ";\n" + ind + "--" + px + "grid-gutter: " + b.gut + "px;\n" + ind + "--" + px + "grid-margin: " + b.mar + "px;\n" + ind + "--" + px + "grid-max-width: " + (b.max ? b.max + "px" : "none") + ";"; };
    if (fmt === "css") {
      return ":root {\n" + vars(first, "  ") + "\n}\n" + bs.slice(1).map(function (b) { return "@media (min-width: " + b.min + "px) { /* " + b.n + " */\n  :root {\n" + vars(b, "    ") + "\n  }\n}"; }).join("\n") +
        "\n\n." + px + "grid {\n  display: grid;\n  grid-template-columns: repeat(var(--" + px + "grid-columns), minmax(0, 1fr));\n  column-gap: var(--" + px + "grid-gutter);\n  padding-inline: var(--" + px + "grid-margin);\n  max-width: var(--" + px + "grid-max-width);\n  margin-inline: auto;\n  box-sizing: border-box;\n}";
    }
    if (fmt === "scss") return "$" + px + "breakpoints: (\n" + bs.map(function (b) { return "  " + b.n + ": " + b.min + "px,"; }).join("\n") + "\n);\n$" + px + "grid: (\n" + bs.map(function (b) { return "  " + b.n + ": (columns: " + b.cols + ", gutter: " + b.gut + "px, margin: " + b.mar + "px, max-width: " + (b.max ? b.max + "px" : "none") + "),"; }).join("\n") + "\n);\n\n@mixin " + px + "from($name) {\n  $min: map-get($" + px + "breakpoints, $name);\n  @if $min == 0px { @content; } @else { @media (min-width: $min) { @content; } }\n}";
    if (fmt === "tailwind") return "/** tailwind.config.js */\nmodule.exports = {\n  theme: {\n    extend: {\n      screens: {\n" + bs.slice(1).map(function (b) { return "        " + JSON.stringify(px + b.n) + ": '" + b.min + "px',"; }).join("\n") + "\n      },\n    },\n  },\n};";
    var j = { breakpoint: {}, grid: { columns: {}, gutter: {}, margin: {} } };
    bs.forEach(function (b) { j.breakpoint[px + b.n] = { $type: "dimension", $value: b.min + "px" }; j.grid.columns[px + b.n] = { $type: "number", $value: b.cols }; j.grid.gutter[px + b.n] = { $type: "dimension", $value: b.gut + "px" }; j.grid.margin[px + b.n] = { $type: "dimension", $value: b.mar + "px" }; });
    return JSON.stringify(j, null, 2);
  };
  FILES.grid = function (f) { return f === "tailwind" ? "tailwind.screens.js" : "grid." + EXT[f]; };
  (function () {
    var P = $("#p-grid"); if (!P) return;
    var tbl = $("[data-gtable]", P), view = $("[data-gview]", P), facts = $("[data-gfacts]", P), renderExp;
    function draw() {
      var bs = gridBps(), g = gridAt(S.g.vw), b = g.bp, w = S.g.vw, pct = function (v) { return (v / w * 100).toFixed(3) + "%"; };
      var cols = ""; for (var i = 0; i < b.cols; i++) cols += "<i></i>";
      var spans = b.cols >= 12 ? [[3, 3, 3, 3], [8, 4], [6, 6], [12]] : b.cols >= 8 ? [[4, 4], [2, 6], [8]] : [[2, 2], [4]];
      if (b.cols === 16) spans = [[4, 4, 4, 4], [12, 4], [8, 8], [16]];
      view.innerHTML = '<div class="lx-gv-frame" style="--w:' + w + '"><span class="lx-gv-w">' + w + 'px</span>' +
        '<div class="lx-gv-box" style="width:' + pct(g.box) + ';padding-inline:' + (g.box ? (b.mar / g.box * 100).toFixed(3) : 0) + '%">' +
        '<div class="lx-gv-cols" style="grid-template-columns:repeat(' + b.cols + ',minmax(0,1fr));column-gap:' + (g.content ? (b.gut / g.content * 100).toFixed(3) : 0) + '%">' + cols + "</div>" +
        '<div class="lx-gv-demo" style="grid-template-columns:repeat(' + b.cols + ',minmax(0,1fr));column-gap:' + (g.content ? (b.gut / g.content * 100).toFixed(3) : 0) + '%">' +
        spans.map(function (r) { return r.map(function (n) { return '<b style="grid-column:span ' + n + '">' + n + "</b>"; }).join(""); }).join("") + "</div></div></div>";
      var narrow = g.col < 40;
      facts.innerHTML = '<div><b>' + esc(b.n) + "</b><span>active breakpoint</span></div><div><b>" + b.cols + "</b><span>columns</span></div><div" + (narrow ? ' class="warn"' : "") + "><b>" + g.col.toFixed(1) + "px</b><span>column width" + (narrow ? " · narrow" : "") + "</span></div><div><b>" + b.gut + "px</b><span>gutter</span></div><div><b>" + b.mar + "px</b><span>margin</span></div><div><b>" + Math.round(g.content) + "px</b><span>content width</span></div>";
      tbl.innerHTML = '<table><thead><tr><th scope="col">Name</th><th scope="col">From</th><th scope="col">Columns</th><th scope="col">Gutter</th><th scope="col">Margin</th><th scope="col">Max width</th><th scope="col">Column at start</th><th scope="col"><span class="sr">Remove</span></th></tr></thead><tbody>' +
        bs.map(function (x) {
          var at = gridAt(Math.max(x.min, 320)), id = S.g.bps.indexOf(x), on = x === b;
          var num = function (k, lo, hi) { return '<input type="number" inputmode="numeric" min="' + lo + '" max="' + hi + '" value="' + x[k] + '" data-k="' + k + '" data-i="' + id + '" aria-label="' + esc(x.n) + " " + k + '">'; };
          return '<tr' + (on ? ' class="on"' : "") + '><td><input type="text" value="' + esc(x.n) + '" data-k="n" data-i="' + id + '" aria-label="Breakpoint name" maxlength="16" spellcheck="false"></td><td>' + num("min", 0, 3840) + "</td><td>" + num("cols", 1, 24) + "</td><td>" + num("gut", 0, 96) + "</td><td>" + num("mar", 0, 200) + "</td><td>" + num("max", 0, 3840) + '</td><td class="r">' + at.col.toFixed(1) + 'px</td><td><button type="button" class="lx-icon" data-grm="' + id + '" aria-label="Remove ' + esc(x.n) + '"' + (bs.length < 2 ? " disabled" : "") + ">✕</button></td></tr>";
        }).join("") + "</tbody></table>";
      $$("input", tbl).forEach(function (el) {
        el.addEventListener("change", function () {
          var it = S.g.bps[+el.getAttribute("data-i")], k = el.getAttribute("data-k"); if (!it) return;
          it[k] = k === "n" ? slug(el.value, "bp") : Math.max(0, Math.round(+el.value || 0)); if (k === "cols") it.cols = Math.max(1, Math.min(24, it.cols));
          S.g.preset = "custom"; presetSet("custom"); save(); draw();
        });
      });
      $$("[data-grm]", tbl).forEach(function (bt) { bt.addEventListener("click", function () { S.g.bps.splice(+bt.getAttribute("data-grm"), 1); S.g.preset = "custom"; presetSet("custom"); save(); draw(); }); });
      renderExp();
    }
    renders.grid = draw;
    var presetSet = seg(P, "gpreset", function () { return S.g.preset; }, function (v) { if (v === "custom") return; S.g.preset = v; S.g.bps = clone(GRIDP[v]); save(); draw(); });
    bindRange(P, "gvw", function () { return S.g.vw; }, function (v) { S.g.vw = v; save(); draw(); });
    $("[data-gadd]", P).addEventListener("click", function () { var bs = gridBps(), last = bs[bs.length - 1]; S.g.bps.push({ n: "bp-" + (bs.length + 1), min: last.min + 320, cols: last.cols, gut: last.gut, mar: last.mar, max: 0 }); S.g.preset = "custom"; presetSet("custom"); save(); draw(); });
    renderExp = exportBar("grid");
  })();

  /* ================================================================ 9. ROI calculator */
  function roiModel(o) {
    o = o || S.roi;
    var g = o.gain / 100, cost = o.fte * o.monthly * 12, ui = function (a) { return (o.eng * o.uiEng / 100 + o.des * o.uiDes / 100) * o.hours * g * a; };
    var years = [o.a1, o.a2, o.a3].map(function (a, i) { var hrs = ui(a / 100), val = hrs * o.rate; return { y: i + 1, a: a, hours: hrs, value: val, cost: cost, net: val - cost, roi: cost ? (val - cost) / cost * 100 : 0 }; });
    var cum = 0, be = null, first = null; years.forEach(function (y) { cum += y.net; y.cum = cum; if (be === null && cum >= 0) be = y.y; if (first === null && y.net >= 0) first = y.y; });
    var perEng = (o.uiEng / 100 + (o.eng ? o.des / o.eng : 0) * o.uiDes / 100) * o.hours * g * 0.7 * o.rate;
    return { years: years, cost: cost, beYear: be, firstYear: first, beEng: perEng > 0 ? Math.ceil(cost / perEng) : null };
  }
  GEN.roi = function (fmt) {
    var m = roiModel(), o = S.roi, c = o.cur;
    var rows = m.years.map(function (y) { return { year: y.y, adoption: y.a + "%", hoursSaved: Math.round(y.hours), value: Math.round(y.value), cost: Math.round(y.cost), net: Math.round(y.net), cumulative: Math.round(y.cum) }; });
    if (fmt === "json") return JSON.stringify({ inputs: o, years: rows, firstProfitableYear: m.firstYear, cumulativePaybackYear: m.beYear, breakEvenEngineersAt70: m.beEng, method: "UI hours = (engineers × UI share + designers × UI share) × hours per year; saved = UI hours × time gain × adoption; value = saved × hourly rate; cost = system FTE × monthly cost × 12." }, null, 2);
    if (fmt === "csv") return "Year,Adoption,Hours saved,Value,Cost,Net,Cumulative\n" + rows.map(function (r) { return [r.year, r.adoption, r.hoursSaved, r.value, r.cost, r.net, r.cumulative].join(","); }).join("\n");
    var f = function (v) { return (v < 0 ? "−" : "") + c + Math.abs(Math.round(v)).toLocaleString("en-US"); };
    return "# Design system ROI estimate\n\n" + o.eng + " engineers, " + o.des + " designers; a system team of " + o.fte + " FTE at " + f(o.monthly) + " a month; " + o.gain + "% time gain on UI work; " + f(o.rate) + " an hour.\n\n| Year | Adoption | Hours saved | Value | Cost | Net | Cumulative |\n|---|---|---|---|---|---|---|\n" +
      m.years.map(function (y) { return "| " + y.y + " | " + y.a + "% | " + Math.round(y.hours).toLocaleString("en-US") + " | " + f(y.value) + " | " + f(y.cost) + " | " + f(y.net) + " | " + f(y.cum) + " |"; }).join("\n") +
      "\n\n" + (m.firstYear ? "First profitable year: " + m.firstYear + ". " : "Not profitable in any of the first three years. ") + (m.beYear ? "Fully paid back, cumulatively, in year " + m.beYear + "." : "The early losses aren't recovered within three years on these inputs.") + (m.beEng ? " At 70% adoption, this team size breaks even with about " + m.beEng + " engineers." : "") + "\n\nMethod: Layer One Lab, design system ROI calculator. Time saved only; quality, accessibility and brand consistency are not counted.";
  };
  FILES.roi = function (f) { return "design-system-roi." + EXT[f]; };
  (function () {
    var P = $("#p-roi"); if (!P) return;
    var out = $("[data-roi]", P), renderExp;
    var money = function (v) { var a = Math.abs(Math.round(v)), c = S.roi.cur; return (v < 0 ? "−" : "") + c + (a >= 1e6 ? (a / 1e6).toFixed(a >= 1e7 ? 1 : 2) + "M" : a >= 1e4 ? Math.round(a / 1e3) + "k" : a.toLocaleString("en-US")); };
    function draw() {
      var m = roiModel(), y3 = m.years[2], peak = Math.max.apply(null, m.years.map(function (y) { return Math.max(y.value, y.cost); }).concat([1]));
      var grid = [10, 20, 34].map(function (g) { return "<tr><th scope=\"row\">" + g + "%</th>" + [40, 70, 90].map(function (a) { var o = clone(S.roi); o.gain = g; o.a1 = a; var n = roiModel(o).years[0].net; return '<td class="' + (n >= 0 ? "pos" : "neg") + '">' + money(n) + "</td>"; }).join("") + "</tr>"; }).join("");
      out.innerHTML = '<div class="lx-roi-stats"><div class="' + (y3.net >= 0 ? "pos" : "neg") + '"><b>' + money(y3.net) + "</b><span>net in year 3</span></div><div class=\"" + (m.years[2].cum >= 0 ? "pos" : "neg") + '"><b>' + money(m.years[2].cum) + "</b><span>three years, cumulative</span></div><div><b>" + (m.firstYear ? "Year " + m.firstYear : "Not in 3 years") + "</b><span>first profitable year" + (m.firstYear && !m.beYear ? "; early losses not yet recovered" : m.beYear ? "; fully paid back in year " + m.beYear : "") + "</span></div><div><b>" + (m.beEng || "—") + "</b><span>engineers to break even at 70% adoption</span></div></div>" +
        '<div class="lx-roi-bars" role="img" aria-label="Value and cost per year">' + m.years.map(function (y) { return '<div class="yr"><span class="k">Year ' + y.y + " · " + y.a + '% adoption</span><div class="b"><i class="v" style="width:' + (y.value / peak * 100).toFixed(1) + '%"></i><em>' + money(y.value) + ' value</em></div><div class="b"><i class="c" style="width:' + (y.cost / peak * 100).toFixed(1) + '%"></i><em>' + money(y.cost) + " cost</em></div></div>"; }).join("") + "</div>" +
        '<div class="lx-roi-tbl"><table><thead><tr><th scope="col">Year</th><th scope="col">Adoption</th><th scope="col" class="r">Hours saved</th><th scope="col" class="r">Value</th><th scope="col" class="r">Cost</th><th scope="col" class="r">Net</th><th scope="col" class="r">Cumulative</th></tr></thead><tbody>' +
        m.years.map(function (y) { return "<tr><td>" + y.y + "</td><td>" + y.a + '%</td><td class="r">' + Math.round(y.hours).toLocaleString("en-US") + '</td><td class="r">' + money(y.value) + '</td><td class="r">' + money(y.cost) + '</td><td class="r ' + (y.net >= 0 ? "pos" : "neg") + '">' + money(y.net) + '</td><td class="r ' + (y.cum >= 0 ? "pos" : "neg") + '">' + money(y.cum) + "</td></tr>"; }).join("") + "</tbody></table></div>" +
        '<div class="lx-roi-sens"><p class="lx-k">How sensitive is it? Net in one year, by time gain (rows) and adoption (columns)</p><table><thead><tr><th scope="col">Gain \\ adoption</th><th scope="col">40%</th><th scope="col">70%</th><th scope="col">90%</th></tr></thead><tbody>' + grid + "</tbody></table></div>";
      renderExp();
    }
    renders.roi = draw;
    function up() { save(); draw(); }
    [["reng", "eng"], ["rdes", "des"], ["rfte", "fte"], ["rmonthly", "monthly"], ["rrate", "rate"], ["rhours", "hours"]].forEach(function (x) {
      var el = inp(P, x[0]); if (!el) return; el.value = S.roi[x[1]]; bindVal(el, function () { return S.roi[x[1]]; });
      el.addEventListener("input", function () { var v = +el.value; if (!isFinite(v) || v < 0) return; S.roi[x[1]] = v; up(); });
    });
    ["gain", "a1", "a2", "a3", "uiEng", "uiDes"].forEach(function (k) { if (inp(P, "r" + k)) bindRange(P, "r" + k, function () { return S.roi[k]; }, function (v) { S.roi[k] = v; up(); }, function (v) { return v + "%"; }); });
    seg(P, "rcur", function () { return S.roi.cur; }, function (v) { S.roi.cur = v; up(); });
    renderExp = exportBar("roi");
  })();

  /* ================================================================ presets, share, reset, start */
  $$("[data-lx-preset]").forEach(function (b) {
    b.addEventListener("click", function () {
      var patch; try { patch = JSON.parse(b.getAttribute("data-lx-preset")); } catch (e) { return; }
      merge(S, patch); save(); SYNC.forEach(function (f) { f(); }); renderAll();
      $$("[data-lx-preset]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      status("Loaded: " + b.textContent.trim());
    });
  });
  var shareB = $("[data-share]"), resetB = $("[data-reset]");
  if (shareB) shareB.addEventListener("click", function (e) {
    var s = clone(S); delete s.b.draft;
    var enc64 = btoa(unescape(encodeURIComponent(JSON.stringify(s)))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
    copy(location.origin + location.pathname + "#s=" + enc64, e.currentTarget); status("Link copied. It opens this tool exactly as it is now.");
  });
  if (resetB) resetB.addEventListener("click", function () {
    var keys = OWN[TOOL] || [];
    keys.forEach(function (k) { S[k] = clone(DEF[k]); });
    save(); SYNC.forEach(function (f) { f(); }); renderAll();
    $$("[data-lx-preset]").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
    status("Reset to the defaults");
  });
  if (shared) { status("Opened a shared link"); try { history.replaceState(null, "", location.pathname); } catch (e) {} }
  renderAll();
})();
