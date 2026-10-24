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

  /* ---------- Hero reel: autoplay, pause control, progress ---------- */
  $$("[data-reel]").forEach(function (fig) {
    var v = $("video", fig), btn = $("[data-reel-toggle]", fig), bar = $(".reel-progress span", fig), userPaused = false;
    function setState() { fig.classList.toggle("is-paused", v.paused); btn.setAttribute("aria-label", v.paused ? "Play the video" : "Pause the video"); }
    function play() { var p = v.play(); if (p && p.catch) p.catch(function () { setState(); }); }
    if (reduce) { v.removeAttribute("autoplay"); v.pause(); userPaused = true; }
    else play();
    btn.addEventListener("click", function () { if (v.paused) { userPaused = false; play(); } else { userPaused = true; v.pause(); } });
    v.addEventListener("play", setState); v.addEventListener("pause", setState);
    v.addEventListener("timeupdate", function () { if (v.duration) bar.style.width = (v.currentTime / v.duration * 100) + "%"; });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { if (userPaused) return; if (e.isIntersecting) play(); else v.pause(); }); }, { threshold: 0.2 }).observe(fig);
    }
    setState();
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

  /* ---------- Contact form → validated email draft ---------- */
  var form = $("[data-contact]");
  if (form) {
    var OFFERS = { audit: "System Audit", foundations: "Foundations", partner: "Partner", workshops: "Workshop", workshop: "Workshop", founding: "Founding partner slot" };
    try { var o = new URLSearchParams(location.search).get("offer"); if (OFFERS[o]) { var r = $('input[name=offer][value="' + OFFERS[o] + '"]', form); if (r) r.checked = true; } } catch (e) {}
    var err = $("[data-f-error]", form);
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form), missing = [];
      $$("input[aria-invalid]", form).forEach(function (i) { i.removeAttribute("aria-invalid"); });
      [["name", "your name"], ["email", "a work email"], ["company", "your company"]].forEach(function (k) {
        var v = (f.get(k[0]) || "").trim(), inp = $("[name=" + k[0] + "]", form);
        if (!v || (k[0] === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v))) { missing.push(k[1]); inp.setAttribute("aria-invalid", "true"); }
      });
      if (!f.get("stage")) missing.push("where your system is today");
      if (!f.get("offer")) missing.push("what you're interested in");
      if (missing.length) { err.textContent = "Please add " + missing.join(", ") + "."; err.hidden = false; var first = $("[aria-invalid=true]", form); if (first) first.focus(); return; }
      err.hidden = true;
      var lines = ["Name: " + f.get("name"), "Email: " + f.get("email"), "Company: " + f.get("company")];
      if (f.get("role")) lines.push("Role: " + f.get("role"));
      lines.push("Where the system is today: " + f.get("stage"), "Interested in: " + f.get("offer"));
      if (f.get("when")) lines.push("Start: " + f.get("when"));
      if (f.get("size")) lines.push("Designers: " + f.get("size"));
      if (f.get("message")) lines.push("", f.get("message"));
      window.location.href = "mailto:layerone@proton.me?subject=" + encodeURIComponent("Design system enquiry: " + f.get("company")) + "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
  $$("[data-copy-email]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.getAttribute("data-copy-email");
      function done() { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1600); }
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () {}); else done();
    });
  });

  /* ---------- Pricing: founding-partner toggle ---------- */
  var tg = $$(".pr-toggle button");
  if (tg.length) {
    tg.forEach(function (b) { b.addEventListener("click", function () {
      var disc = b.getAttribute("data-price") === "disc";
      tg.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      $$(".plan .amt").forEach(function (a) { a.textContent = a.getAttribute(disc ? "data-disc" : "data-full"); });
      $$("[data-was]").forEach(function (w) { w.hidden = !disc; });
      $$("[data-th-price]").forEach(function (th) { var amt = $('[data-plan="' + th.getAttribute("data-th-price") + '"] .amt'); th.textContent = amt.textContent + (th.getAttribute("data-th-price") === "partner" ? " /mo" : ""); });
      var n = $("[data-fp-note]"); if (n) n.hidden = !disc;
    }); });
  }

  /* ---------- Pricing: plan finder ---------- */
  var finder = $("[data-finder]");
  if (finder) {
    var out = $("[data-f-result]", finder);
    var REC = {
      audit: ["Start with the Audit", "Two weeks to find out exactly what to fix first. If you continue, the fee is credited against Foundations.", "audit"],
      foundations: ["Foundations", "Six weeks to put real foundations in place: palette, tokens, core components and docs.", "foundations"],
      foundationsPartner: ["Foundations, then Partner", "Build the foundations in six weeks, then keep them running and adopted month to month.", "foundations"],
      partner: ["Partner", "You have a system. You need it run, scaled and used. Monthly, pause any time.", "partner"]
    };
    finder.addEventListener("change", function () {
      var f = new FormData(finder), a = f.get("f1"), b = f.get("f2"), c = f.get("f3");
      if (!a || !b || !c) return;
      var k;
      if (a === "none") k = c === "ongoing" ? "foundationsPartner" : "foundations";
      else if (b === "unknown") k = "audit";
      else if (b === "foundations") k = (a === "works" && c === "ongoing") ? "partner" : (c === "ongoing" ? "foundationsPartner" : "foundations");
      else k = c === "ongoing" ? "partner" : "audit";
      var r = REC[k];
      out.innerHTML = '<div><p class="small muted" style="margin:0">We\'d recommend</p><h3>' + r[0] + '</h3><p>' + r[1] + '</p></div><a class="pill pill--accent" href="#plan-' + r[2] + '">See the plan</a>';
      $$(".plan").forEach(function (p) { p.classList.toggle("is-rec", p.id === "plan-" + r[2]); });
    });
  }

/* =================== Case study modules =================== */
  var io = "IntersectionObserver" in window;
  function onView(el, fn, opts) {
    if (!io || reduce) { fn(); return; }
    var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { fn(); o.disconnect(); } }); }, opts || { threshold: 0.35 });
    o.observe(el);
  }
  $$("[data-inview]").forEach(function (el) { onView(el, function () { el.classList.add("in"); }); });

  /* Count-up numbers */
  $$("[data-countup]").forEach(function (el) {
    var end = parseFloat(el.getAttribute("data-countup"));
    if (reduce || !io) return;
    el.textContent = "0";
    onView(el, function () {
      var t0 = null, d = 1100;
      function step(ts) { if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / d), e = 1 - Math.pow(1 - p, 3); el.textContent = Math.round(end * e).toLocaleString(); if (p < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    }, { threshold: 0.6 });
  });

  /* Before/after compare */
  $$("[data-compare]").forEach(function (c) {
    var r = $("input", c);
    function set() { c.style.setProperty("--pos", r.value + "%"); }
    r.addEventListener("input", set); set();
  });

  /* Generic tabs (also stepper, rings) */
  $$("[data-tabs]").forEach(function (box) {
    var tabs = $$("[role=tab]", box), stepper = box.hasAttribute("data-stepper");
    var prog = $(".sp-prog span", box), cur = 0;
    function select(i, focus) {
      cur = i;
      tabs.forEach(function (t, j) {
        var on = j === i; t.setAttribute("aria-selected", on ? "true" : "false"); t.tabIndex = on ? 0 : -1;
        var pnl = document.getElementById(t.getAttribute("aria-controls")); if (pnl) pnl.hidden = !on;
      });
      if (focus) tabs[i].focus();
      if (prog) prog.style.width = ((i + 1) / tabs.length * 100) + "%";
      var ring = tabs[i].getAttribute("data-ring"); if (ring) box.setAttribute("data-active", ring);
      if (stepper) { $("[data-prev]", box).disabled = i === 0; $("[data-next]", box).textContent = i === tabs.length - 1 ? "Start again" : "Next step"; }
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = null;
        if (k === "ArrowRight" || k === "ArrowDown") n = (i + 1) % tabs.length;
        if (k === "ArrowLeft" || k === "ArrowUp") n = (i - 1 + tabs.length) % tabs.length;
        if (k === "Home") n = 0; if (k === "End") n = tabs.length - 1;
        if (n !== null) { e.preventDefault(); select(n, true); }
      });
    });
    if (stepper) {
      $("[data-prev]", box).addEventListener("click", function () { if (cur > 0) select(cur - 1); });
      $("[data-next]", box).addEventListener("click", function () { select((cur + 1) % tabs.length); });
    }
    select(0);
  });

  /* Before/after list toggle */
  $$("[data-shift]").forEach(function (box) {
    var b = $$(".seg-toggle button", box);
    b.forEach(function (btn) { btn.addEventListener("click", function () {
      b.forEach(function (o) { o.setAttribute("aria-pressed", o === btn ? "true" : "false"); });
      box.classList.toggle("is-after", btn.getAttribute("data-v") === "1");
    }); });
    onView(box, function () { setTimeout(function () { if (!box.dataset.touched) b[1].click(); }, 900); }, { threshold: 0.6 });
    b.forEach(function (btn) { btn.addEventListener("pointerdown", function () { box.dataset.touched = "1"; }); });
  });

  /* Merge five blues into one token */
  $$("[data-unify]").forEach(function (box) {
    var btn = $("[data-unify-btn]", box);
    btn.addEventListener("click", function () {
      var one = box.classList.toggle("is-one");
      btn.textContent = one ? "Show the five codes again" : "Merge into one token";
    });
  });

  /* Live ramp read-out */
  $$("[data-ramp-live]").forEach(function (box) {
    var btns = $$("button", box);
    function hexLum(h) { var c = [1, 3, 5].map(function (i) { var v = parseInt(h.substr(i, 2), 16) / 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; }
    function rate(r) { return r >= 7 ? "AAA" : r >= 4.5 ? "AA" : r >= 3 ? "AA large" : "fail"; }
    function pick(b) {
      btns.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      var h = b.getAttribute("data-hex"), L = hexLum(h), w = 1.05 / (L + 0.05), k = (L + 0.05) / 0.05;
      $("[data-r-name]", box).textContent = b.getAttribute("data-name");
      $("[data-r-hex]", box).textContent = h.toUpperCase();
      $("[data-r-w]", box).textContent = "White text " + w.toFixed(1) + ":1 (" + rate(w) + ")";
      $("[data-r-b]", box).textContent = "Black text " + k.toFixed(1) + ":1 (" + rate(k) + ")";
      btns.forEach(function (o) { var l = hexLum(o.getAttribute("data-hex")); o.style.color = (1.05 / (l + 0.05)) >= ((l + 0.05) / 0.05) ? "#fff" : "#000"; });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { pick(b); }); b.addEventListener("mouseenter", function () { pick(b); }); });
    pick(btns[5]);
  });

  /* Brand switch on the token chain demo */
  $$("[data-brand]").forEach(function (box) {
    var b = $$(".seg-toggle button", box);
    b.forEach(function (btn) { btn.addEventListener("click", function () {
      b.forEach(function (o) { o.setAttribute("aria-pressed", o === btn ? "true" : "false"); });
      box.style.setProperty("--b", btn.getAttribute("data-b")); box.style.setProperty("--b2", btn.getAttribute("data-b2")); box.style.setProperty("--acc", btn.getAttribute("data-acc"));
      $("[data-prim]", box).textContent = btn.getAttribute("data-p");
    }); });
  });

  /* Cost calculator */
  $$("[data-calc]").forEach(function (box) {
    var g = function (k) { return +$('[data-i="' + k + '"]', box).value; };
    function fmtT(s) { return s >= 3600 ? "~" + (s / 3600).toFixed(1) + " h" : s >= 60 ? Math.round(s / 60) + " min" : s + " s"; }
    function upd() {
      var n = g("places"), s = g("secs"), r = g("rate");
      $('[data-o="places"]', box).textContent = n.toLocaleString(); $('[data-o="secs"]', box).textContent = s; $('[data-o="rate"]', box).textContent = r;
      var hand = n * s, cost = hand / 3600 * r, tcost = s / 3600 * r;
      $("[data-hand]", box).textContent = fmtT(hand) + " · $" + Math.round(cost).toLocaleString();
      $("[data-tok]", box).textContent = fmtT(s) + " · $" + tcost.toFixed(2);
      $("[data-bar-tok]", box).style.width = Math.max(0.4, s / hand * 100) + "%";
      var pct = (1 - 1 / n) * 100; $("[data-saved]", box).textContent = (pct >= 99.9 ? Math.min(pct, 99.99).toFixed(2) : pct.toFixed(1)) + "%";
    }
    $$("input", box).forEach(function (i) { i.addEventListener("input", upd); }); upd();
  });

  /* CMS text-limit demo */
  $$("[data-cms]").forEach(function (box) {
    var ti = $("[data-cms-title]", box), bi = $("[data-cms-btn]", box), card = $(".cms-card", box), warn = $("[data-cms-warn]", box);
    function upd() {
      var tl = ti.value.length, bl = bi.value.length, over = tl > 40 || bl > 18;
      $("[data-cc]", box).textContent = tl + " / 40"; $("[data-cb]", box).textContent = bl + " / 18";
      $("[data-cc]", box).classList.toggle("over", tl > 40); $("[data-cb]", box).classList.toggle("over", bl > 18);
      ti.classList.toggle("over", tl > 40); bi.classList.toggle("over", bl > 18);
      $("[data-cms-t]", box).textContent = ti.value || "Title"; $("[data-cms-b]", box).textContent = bi.value || "Button";
      card.classList.toggle("over", over); warn.hidden = !over;
    }
    [ti, bi].forEach(function (i) { i.addEventListener("input", upd); });
    $$("[data-ratio]", box).forEach(function (r, _, all) { r.addEventListener("click", function () {
      all.forEach(function (o) { o.setAttribute("aria-pressed", o === r ? "true" : "false"); });
      $("[data-cms-img]", box).style.aspectRatio = r.getAttribute("data-ratio");
    }); });
    upd();
  });

  /* Lightbox */
  var lb = $("[data-lb]");
  if (lb && lb.showModal) {
    var lbImg = $("img", lb), lbCap = $("p", lb);
    $$("[data-lightbox]").forEach(function (im) {
      im.tabIndex = 0;
      function open() { lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt; lbCap.textContent = im.getAttribute("data-cap") || ""; lb.showModal(); }
      im.addEventListener("click", open);
      im.addEventListener("keydown", function (e) { if (e.key === "Enter") open(); });
    });
    $(".lb-x", lb).addEventListener("click", function () { lb.close(); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lb.close(); });
  }

  /* Chapter bar: active chapter + reading progress */
  var chBar = $("[data-chapters]");
  if (chBar) {
    var links = $$("a", chBar), prog = $(".ch-prog span", chBar), secs = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });
    function onScroll() {
      var y = window.scrollY + 140, act = -1;
      secs.forEach(function (s, i) { if (s && s.offsetTop <= y) act = i; });
      links.forEach(function (a, i) { a.classList.toggle("is-active", i === act); });
      if (act >= 0) { var a = links[act]; var box = a.parentNode; if (a.offsetLeft < box.scrollLeft || a.offsetLeft + a.offsetWidth > box.scrollLeft + box.clientWidth) box.scrollLeft = a.offsetLeft - 20; }
      var h = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.width = (h > 0 ? window.scrollY / h * 100 : 0) + "%";
    }
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
