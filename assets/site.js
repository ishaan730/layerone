/* Layer One — shared behaviour (v2). No dependencies. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Mobile menu ---------- */
  var bar = $(".topbar"), menu = $(".menu-btn");
  if (bar && menu) {
    menu.addEventListener("click", function () {
      var open = bar.classList.toggle("is-open");
      menu.setAttribute("aria-expanded", open ? "true" : "false");
      menu.textContent = open ? "Close" : "Menu";
    });
  }

  /* ---------- Hero stage: one system, many brands ---------- */
  $$("[data-stage]").forEach(function (stage) {
    var dots = $$(".brand-dots button", stage);
    var nameEl = $("[data-brand-name]", stage);
    var hexEl = $("[data-brand-hex]", stage);
    var i = 0, timer = null;
    function show(n) {
      i = n;
      var b = dots[n];
      stage.style.setProperty("--brand", b.getAttribute("data-hex"));
      dots.forEach(function (d) { d.setAttribute("aria-pressed", d === b ? "true" : "false"); });
      if (nameEl) nameEl.textContent = b.getAttribute("data-name");
      if (hexEl) hexEl.textContent = b.getAttribute("data-hex").toUpperCase();
    }
    function start() { if (!reduce && !timer) timer = setInterval(function () { show((i + 1) % dots.length); }, 2800); }
    function stop() { clearInterval(timer); timer = null; }
    dots.forEach(function (d, n) { d.addEventListener("click", function () { stop(); show(n); }); });
    stage.addEventListener("mouseenter", function () { stage.classList.add("is-open"); });
    stage.addEventListener("mouseleave", function () { stage.classList.remove("is-open"); });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { e.isIntersecting ? start() : stop(); }); }).observe(stage);
    } else start();
    show(0);
  });

  /* ---------- Colour maths (OKLCH → sRGB, WCAG contrast) ---------- */
  function oklchToRgb(L, C, H) {
    var h = H * Math.PI / 180, a = C * Math.cos(h), b = C * Math.sin(h);
    var l_ = L + 0.3963377774 * a + 0.2158037573 * b;
    var m_ = L - 0.1055613458 * a - 0.0638541728 * b;
    var s_ = L - 0.0894841775 * a - 1.2914855480 * b;
    var l = l_ * l_ * l_, m = m_ * m_ * m_, s = s_ * s_ * s_;
    return [
      4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
      -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
      -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    ];
  }
  function inGamut(c) { return c.every(function (v) { return v >= -0.0005 && v <= 1.0005; }); }
  function fitted(L, C, H) { var c = C, lin = oklchToRgb(L, c, H); while (!inGamut(lin) && c > 0) { c -= 0.004; lin = oklchToRgb(L, c, H); } return { lin: lin, c: Math.max(c, 0) }; }
  function enc(v) { v = Math.min(1, Math.max(0, v)); return v <= 0.0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - 0.055; }
  function hex(lin) { return "#" + lin.map(function (v) { return ("0" + Math.round(enc(v) * 255).toString(16)).slice(-2); }).join(""); }
  function lum(lin) { var c = lin.map(function (v) { return Math.min(1, Math.max(0, v)); }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; }
  function contrast(a, b) { var x = Math.max(a, b), y = Math.min(a, b); return (x + 0.05) / (y + 0.05); }

  /* ---------- Lab: OKLCH ramp builder ---------- */
  var rampTool = $("[data-ramp]");
  if (rampTool) {
    var STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900];
    var LIGHT = [0.97, 0.93, 0.87, 0.79, 0.70, 0.61, 0.53, 0.45, 0.37, 0.29];
    var CSHAPE = [0.22, 0.38, 0.58, 0.78, 0.94, 1, 0.94, 0.84, 0.70, 0.56];
    var hue = $("[name=hue]", rampTool), chroma = $("[name=chroma]", rampTool), nm = $("[name=rname]", rampTool);
    var out = $(".ramp-out", rampTool), code = $(".code-out", rampTool), copyBtn = $("[data-copy]", rampTool);
    var hv = $("[data-hv]", rampTool), cv = $("[data-cv]", rampTool);
    function draw() {
      var H = +hue.value, C = +chroma.value, name = (nm.value || "brand").toLowerCase().replace(/[^a-z0-9-]/g, "") || "brand";
      hv.textContent = H; cv.textContent = C.toFixed(2);
      var css = ":root {\n", html = "";
      STEPS.forEach(function (st, k) {
        var f = fitted(LIGHT[k], C * CSHAPE[k], H), hx = hex(f.lin), Y = lum(f.lin);
        var onW = contrast(Y, 1), onB = contrast(Y, 0);
        var best = onW >= onB ? "#fff" : "#000", ratio = Math.max(onW, onB);
        var aa = onW >= 4.5 ? '<span class="ok">AA on white</span>' : (onB >= 4.5 ? '<span class="ok">AA on black</span>' : '<span class="no">large text only</span>');
        html += '<div><div class="sw" style="background:' + hx + ';color:' + best + '">' + st + '</div><div class="meta">' + hx + "<br>L " + LIGHT[k].toFixed(2) + " C " + f.c.toFixed(3) + "<br>" + ratio.toFixed(1) + ":1 " + aa + "</div></div>";
        css += "  --color-" + name + "-" + st + ": oklch(" + (LIGHT[k] * 100).toFixed(0) + "% " + f.c.toFixed(3) + " " + H + "); /* " + hx + " */\n";
      });
      out.innerHTML = html; code.textContent = css + "}";
    }
    [hue, chroma, nm].forEach(function (el) { el.addEventListener("input", draw); });
    if (copyBtn) copyBtn.addEventListener("click", function () {
      try { navigator.clipboard.writeText(code.textContent); copyBtn.textContent = "Copied"; setTimeout(function () { copyBtn.textContent = "Copy tokens"; }, 1500); } catch (e) {}
    });
    draw();
  }

  /* ---------- Lab: token chain ---------- */
  var chainTool = $("[data-chain]");
  if (chainTool) {
    var btns = $$("[data-theme-pick]", chainTool);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        chainTool.style.setProperty("--brand", b.getAttribute("data-hex"));
        $("[data-v]", chainTool).textContent = b.getAttribute("data-hex").toUpperCase();
        $("[data-p]", chainTool).textContent = b.getAttribute("data-prim");
        $("[data-s]", chainTool).textContent = b.getAttribute("data-sem");
      });
    });
  }

  /* ---------- Request scorecard ---------- */
  $$("[data-scorer]").forEach(function (scorer) {
    var out = $("[data-total]", scorer), verdict = $("[data-verdict]", scorer), detail = $("[data-detail]", scorer);
    function update() {
      var total = 0, wont = false, n = 0, groups = $$("fieldset", scorer);
      groups.forEach(function (g) { var c = $("input:checked", g); if (!c) return; n++; if (c.value === "x") wont = true; else total += parseInt(c.value, 10); });
      out.textContent = wont ? "—" : String(total);
      var v, d;
      if (wont) { v = "Won't fix: reject"; d = "One answer rules it out. The team builds it outside the system, using the design language."; }
      else if (n < groups.length) { v = "Answer all four"; d = "The score only means something once every question has an answer."; }
      else if (total >= 55) { v = "High: accept, the system team builds it"; d = "Picked up first, as soon as there's capacity."; }
      else if (total >= 40) { v = "Medium: accept"; d = "Picked up after high-priority work. The team can contribute to speed it up."; }
      else { v = "Low: defer"; d = "Unlikely to be picked up. The team can build it as a custom or extended component."; }
      verdict.textContent = v; detail.textContent = d;
    }
    scorer.addEventListener("change", update);
    update();
  });

  /* ---------- Contact form → email draft ---------- */
  var form = $("[data-contact]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var subject = "Design system enquiry: " + (f.get("company") || "new project");
      var body = "Name: " + (f.get("name") || "") + "\nCompany: " + (f.get("company") || "") + "\nWhere the system is today: " + (f.get("stage") || "") + "\nInterested in: " + (f.get("offer") || "") + "\n\n" + (f.get("message") || "");
      window.location.href = "mailto:layerone@proton.me?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
