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
    if (reduce) { v.pause(); userPaused = true; }
    else if (document.readyState === "complete") play();
    else window.addEventListener("load", function () { if (!userPaused) play(); }, { once: true });
    btn.addEventListener("click", function () { if (v.paused) { userPaused = false; play(); } else { userPaused = true; v.pause(); } });
    v.addEventListener("play", setState); v.addEventListener("pause", setState);
    v.addEventListener("timeupdate", function () { if (v.duration) bar.style.width = (v.currentTime / v.duration * 100) + "%"; });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { if (userPaused) return; if (e.isIntersecting) play(); else v.pause(); }); }, { threshold: 0.2 }).observe(fig);
    }
    setState();
  });

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
      function open() { lbImg.src = im.getAttribute("data-full") || im.currentSrc || im.src; lbImg.alt = im.alt; lbCap.textContent = im.getAttribute("data-cap") || ""; lb.showModal(); }
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

  /* =================== Showcase case study (v4) =================== */
  function hexLum2(h) { var c = [1, 3, 5].map(function (i) { var v = parseInt(h.substr(i, 2), 16) / 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; }
  function cr(a, b) { var x = hexLum2(a), y = hexLum2(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function segPress(group, btn) { $$("button", group).forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); }); }

  /* Carousel: scroll-snap track, buttons, counter, progress, mouse drag, arrow keys */
  $$("[data-carousel]").forEach(function (car) {
    var track = $(".sc-car-track", car), slides = $$(".sc-slide", track);
    var prev = $("[data-prev]", car), next = $("[data-next]", car), cur = $("[data-cur]", car), bar = $(".sc-car-bar i", car), idx = 0;
    function centreOf(s) { return s.offsetLeft + s.offsetWidth / 2 - track.clientWidth / 2; }
    function go(i) { i = Math.max(0, Math.min(slides.length - 1, i)); track.scrollTo({ left: centreOf(slides[i]), behavior: reduce ? "auto" : "smooth" }); }
    function upd() {
      var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
      slides.forEach(function (s, i) { var d = Math.abs(s.offsetLeft + s.offsetWidth / 2 - mid); if (d < bd) { bd = d; best = i; } });
      idx = best;
      cur.textContent = String(idx + 1).padStart(2, "0");
      bar.style.width = ((idx + 1) / slides.length * 100) + "%";
      prev.disabled = idx === 0; next.disabled = idx === slides.length - 1;
      slides.forEach(function (s, i) { s.setAttribute("aria-hidden", i === idx ? "false" : "true"); });
    }
    prev.addEventListener("click", function () { go(idx - 1); });
    next.addEventListener("click", function () { go(idx + 1); });
    track.addEventListener("keydown", function (e) { if (e.key === "ArrowRight") { e.preventDefault(); go(idx + 1); } if (e.key === "ArrowLeft") { e.preventDefault(); go(idx - 1); } });
    var t; track.addEventListener("scroll", function () { cancelAnimationFrame(t); t = requestAnimationFrame(upd); }, { passive: true });
    // Mouse drag (touch uses native scrolling)
    var down = false, sx = 0, sl = 0, moved = 0;
    track.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") return; down = true; moved = 0; sx = e.clientX; sl = track.scrollLeft; });
    window.addEventListener("pointermove", function (e) { if (!down) return; var dx = e.clientX - sx; moved = Math.max(moved, Math.abs(dx)); if (moved > 4) { track.classList.add("is-drag"); track.scrollLeft = sl - dx; } });
    window.addEventListener("pointerup", function () { if (!down) return; down = false; if (track.classList.contains("is-drag")) { track.classList.remove("is-drag"); upd(); go(idx); } });
    track.addEventListener("click", function (e) { if (moved > 4) { e.stopPropagation(); e.preventDefault(); moved = 0; } }, true);
    upd();
  });

  /* Colour explorer: every ramp step, with live contrast */
  $$("[data-rampgrid]").forEach(function (box) {
    var btns = $$(".sc-ramp-row button", box), rd = $(".sc-ramp-read", box);
    function pick(b) {
      btns.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      var h = b.getAttribute("data-hex"), w = cr(h, "#ffffff"), k = cr(h, "#27251f");
      rd.style.setProperty("--c", h);
      var sw = $(".sw", rd); sw.style.color = w >= k ? "#fff" : "#27251f";
      $("[data-n]", rd).textContent = b.getAttribute("data-name"); $("[data-h]", rd).textContent = h.toUpperCase();
      function badge(r) { var p = r >= 4.5 ? "AA" : r >= 3 ? "AA large" : "Fails"; return r.toFixed(2) + ':1<span class="pass' + (r >= 3 ? "" : " no") + '">' + p + "</span>"; }
      $("[data-w]", rd).innerHTML = badge(w); $("[data-k]", rd).innerHTML = badge(k);
      $("[data-u]", rd).textContent = b.getAttribute("data-use") || "";
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { pick(b); }); b.addEventListener("mouseenter", function () { pick(b); }); });
    var d = $('[data-default]', box) || btns[0]; pick(d);
  });

  /* Jarvis: live specimen behaviour and token read-out */
  $$("[data-jv]").forEach(function (jv) {
    var out = $("[data-tokout]", jv);
    var map = { rest: ["color-action-primary-surface", "red-500", "#e41f35"], hover: ["color-action-primary-surface--hover", "red-700", "#b22233"], pressed: ["color-action-primary-surface--pressed", "red-900", "#6d151f"] };
    function show(s) { var m = map[s]; out.innerHTML = '<span>Add to cart</span> → <b>' + m[0] + '</b> → <span><i style="--c:' + m[2] + '"></i>' + m[1] + "</span>"; }
    var main = $("[data-tokbtn]", jv);
    if (main && out) {
      main.addEventListener("pointerenter", function () { show("hover"); }); main.addEventListener("pointerleave", function () { show("rest"); });
      main.addEventListener("pointerdown", function () { show("pressed"); }); main.addEventListener("pointerup", function () { show("hover"); });
      main.addEventListener("focus", function () { if (main.matches(":focus-visible")) show("hover"); }); main.addEventListener("blur", function () { show("rest"); });
      show("rest");
    }
    $$(".jq", jv).forEach(function (q) { var o = $("output", q), n = 1; $$("button", q).forEach(function (b) { b.addEventListener("click", function () { n = Math.max(0, Math.min(99, n + (+b.getAttribute("data-d")))); o.textContent = n; }); }); });
    $$(".jt", jv).forEach(function (t) { t.addEventListener("click", function () { t.setAttribute("aria-checked", t.getAttribute("aria-checked") === "true" ? "false" : "true"); }); });
    $$(".jtabs", jv).forEach(function (g) { $$("button", g).forEach(function (b) { b.addEventListener("click", function () { $$("button", g).forEach(function (x) { x.setAttribute("aria-selected", x === b ? "true" : "false"); }); }); }); });
    $$(".jpg", jv).forEach(function (p) { var s = $("span", p), n = 1; $$("button", p).forEach(function (b) { b.addEventListener("click", function () { n = Math.max(1, Math.min(5, n + (+b.getAttribute("data-d")))); s.textContent = n + " of 5"; }); }); });
  });

  /* Riyadh Air: live specimen with theme and language */
  var RX = {
    en: { ruh: "Riyadh", lhr: "London", meta: "Non-stop · 6h 50m · Boeing 787-9", eco: "Economy", prem: "Premium", bus: "Business", from: "From", book: "Book now", booked: "Booked", left: "Only 5 left", liked: "345 people liked this", dist: "2km · 45 min", guests: "Guests", seat: "Choose a seat in row 10", seatP: "Seat 10{s} selected", rex: "Seat 10A has extra legroom and a window, two rows from the exit.", rexK: "REX · AI assist", loc: "en-GB" },
    ar: { ruh: "الرياض", lhr: "لندن", meta: "رحلة مباشرة · 6 س 50 د · بوينغ 787-9", eco: "الاقتصادية", prem: "المميزة", bus: "الأعمال", from: "ابتداءً من", book: "احجز الآن", booked: "تم الحجز", left: "تبقّى 5 فقط", liked: "أعجب 345 شخصًا بهذا", dist: "2 كم · 45 د", guests: "الضيوف", seat: "اختر مقعدًا في الصف 10", seatP: "تم اختيار المقعد 10{s}", rex: "المقعد 10A فيه مساحة إضافية للساقين ونافذة، على بعد صفين من المخرج.", rexK: "ريكس · مساعد ذكي", loc: "ar-SA" }
  };
  $$("[data-rx]").forEach(function (rx) {
    var st = { lang: "en", cabin: "eco", n: 1, seat: "A", booked: false };
    var fares = { eco: 2445, prem: 4890, bus: 9780 };
    function render() {
      var L = RX[st.lang];
      rx.dir = st.lang === "ar" ? "rtl" : "ltr"; rx.lang = st.lang;
      $$("[data-t]", rx).forEach(function (el) { el.textContent = L[el.getAttribute("data-t")]; });
      var amt; try { amt = new Intl.NumberFormat(L.loc, { style: "currency", currency: "SAR", maximumFractionDigits: 0 }).format(fares[st.cabin] * st.n); } catch (e) { amt = "SAR " + fares[st.cabin] * st.n; }
      $("[data-price]", rx).textContent = amt;
      $("[data-n]", rx).textContent = st.n.toLocaleString(L.loc);
      $("[data-dec]", rx).disabled = st.n <= 1; $("[data-inc]", rx).disabled = st.n >= 9;
      $("[data-seatout]", rx).textContent = st.seat ? L.seatP.replace("{s}", st.seat) : L.seat;
      var bk = $("[data-book]", rx); bk.classList.toggle("is-done", st.booked); $("span", bk).textContent = st.booked ? L.booked : L.book;
    }
    var host = rx.closest(".sc-sec") || document;
    $$("[data-rx-theme] button", host).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); rx.setAttribute("data-theme", b.getAttribute("data-v")); }); });
    $$("[data-rx-lang] button", host).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); st.lang = b.getAttribute("data-v"); render(); }); });
    $$("[data-cabin] button", rx).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); st.cabin = b.getAttribute("data-v"); st.booked = false; render(); }); });
    $("[data-dec]", rx).addEventListener("click", function () { st.n--; st.booked = false; render(); });
    $("[data-inc]", rx).addEventListener("click", function () { st.n++; st.booked = false; render(); });
    $$(".rx-seats button", rx).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); st.seat = b.getAttribute("data-s"); render(); }); });
    $("[data-book]", rx).addEventListener("click", function () { st.booked = !st.booked; render(); });
    render();
  });

  /* Breakpoints: draw the real grid of each */
  var BPS = [
    { n: "Smart watch", w: 184, h: 224, cols: 2, m: 16, g: 16, mode: "Stretch", dw: "150px", dr: "40px" },
    { n: "Mobile", w: 393, h: 852, cols: 4, m: 16, g: 16, mode: "Stretch", dw: "160px", dr: "24px" },
    { n: "Tablet portrait", w: 834, h: 1194, cols: 8, m: 32, g: 16, mode: "Stretch", dw: "240px", dr: "18px" },
    { n: "Tablet landscape", w: 1194, h: 834, cols: 12, m: 40, g: 24, mode: "Stretch", dw: "460px", dr: "18px" },
    { n: "Desktop", w: 1440, h: 900, cols: 12, m: 56, g: 24, mode: "Stretch", dw: "540px", dr: "10px" },
    { n: "Desktop large", w: 1920, h: 1080, cols: 12, col: 88, g: 24, mode: "Centred", dw: "600px", dr: "10px" }
  ];
  $$("[data-bp]").forEach(function (box) {
    var list = $(".sc-bp-list", box), dev = $(".sc-bp-dev", box), cols = $(".sc-bp-cols", box), spec = $(".sc-bp-spec", box);
    list.innerHTML = BPS.map(function (b, i) { return '<button type="button" role="tab" aria-selected="false"><span>0' + (i + 1) + "</span><b>" + b.n + "</b><em>" + b.w + "px</em></button>"; }).join("");
    var btns = $$("button", list);
    function pick(i) {
      var b = BPS[i]; btns.forEach(function (x, j) { x.setAttribute("aria-selected", j === i ? "true" : "false"); });
      dev.style.setProperty("--ar", b.w + " / " + b.h); dev.style.setProperty("--dw", b.dw); dev.style.setProperty("--dr", b.dr);
      var content = b.col ? b.cols * b.col + (b.cols - 1) * b.g : b.w - 2 * b.m;
      cols.style.setProperty("--side", ((b.w - content) / 2 / b.w * 100) + "%");
      cols.style.setProperty("--gap", (b.g / b.w * 100) + "cqw"); cols.style.setProperty("--n", b.cols);
      cols.innerHTML = new Array(b.cols + 1).join("<i></i>");
      spec.innerHTML = [["Width", b.w + "px"], ["Columns", b.cols], [b.col ? "Column" : "Margin", (b.col || b.m) + "px"], ["Gutter", b.g + "px"], ["Layout", b.mode]].map(function (r) { return "<div><dt>" + r[0] + "</dt><dd>" + r[1] + "</dd></div>"; }).join("");
    }
    btns.forEach(function (x, i) { x.addEventListener("click", function () { pick(i); }); });
    pick(1);
  });

  /* Four scripts, one scale */
  var SCRIPTS = {
    en: { dir: "ltr", h: "Welcome aboard", l: "A brand-new chapter in the sky", b: "Riyadh to London, non-stop. Choose your seat and add extra baggage.", s: "SF Pro Display · SF Pro Text" },
    ar: { dir: "rtl", h: "مرحبًا بكم على متن الطائرة", l: "فصل جديد تمامًا في السماء", b: "من الرياض إلى لندن، رحلة مباشرة. اختر مقعدك وأضف أمتعة إضافية.", s: "SF Arabic" },
    ja: { dir: "ltr", h: "ご搭乗ありがとうございます", l: "空の新たな章", b: "リヤドからロンドンへ直行便。座席を選んで手荷物を追加できます。", s: "Third language · Japanese" },
    th: { dir: "ltr", h: "ยินดีต้อนรับบนเครื่อง", l: "บทใหม่บนท้องฟ้า", b: "ริยาดสู่ลอนดอน บินตรง เลือกที่นั่งและเพิ่มสัมภาระ", s: "Third language · Thai" }
  };
  $$("[data-scripts]").forEach(function (box) {
    var sp = $(".sc-type", box);
    function set(k) { var d = SCRIPTS[k]; sp.dir = d.dir; sp.lang = k; ["h", "l", "b", "s"].forEach(function (f) { $("[data-f=" + f + "]", sp).textContent = d[f]; }); }
    $$(".sc-seg button", box).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); set(b.getAttribute("data-v")); }); });
    set("en");
  });

  /* Stress test: language × currency */
  var SX = {
    en: { loc: "en-GB", dir: "ltr", h: "Riyadh to London", sub: "Non-stop · 6h 50m · 2 guests", pk: "Total", cta: "Continue to payment", why: "The baseline every layout is drawn in." },
    ar: { loc: "ar-SA", dir: "rtl", h: "الرياض إلى لندن", sub: "رحلة مباشرة · 6 س 50 د · ضيفان", pk: "الإجمالي", cta: "المتابعة إلى الدفع", why: "Right to left: icons, arrows and alignment flip." },
    de: { loc: "de-DE", dir: "ltr", h: "Riad nach London", sub: "Nonstop · 6 Std. 50 Min. · 2 Fluggäste", pk: "Gesamtbetrag", cta: "Weiter zur Zahlungsabwicklung", why: "Long compound words test every button width." },
    ja: { loc: "ja-JP", dir: "ltr", h: "リヤドからロンドンへ", sub: "直行便 · 6時間50分 · 2名", pk: "合計", cta: "お支払いへ進む", why: "A third script, with no spaces between words." }
  };
  var CUR = { SAR: 4890, INR: 109450.5, IDR: 21245000, JPY: 195600, KWD: 401.375 };
  var CURWHY = { SAR: "", INR: "Rupees group digits differently in some locales.", IDR: "Rupiah runs to eight digits.", JPY: "Yen has no decimals at all.", KWD: "Dinars use three decimals." };
  $$("[data-stress]").forEach(function (box) {
    var st = { l: "en", c: "SAR" }, card = $(".sx-card", box), why = $(".why", box);
    function render() {
      var L = SX[st.l]; card.dir = L.dir; card.lang = st.l;
      $(".h", card).textContent = L.h; $(".sub", card).textContent = L.sub; $(".pk", card).textContent = L.pk; $(".cta", card).textContent = L.cta;
      var a; try { a = new Intl.NumberFormat(L.loc, { style: "currency", currency: st.c }).format(CUR[st.c]); } catch (e) { a = st.c + " " + CUR[st.c]; }
      $(".amt", card).textContent = a; why.textContent = [L.why, CURWHY[st.c]].filter(Boolean).join(" ");
      card.classList.remove("is-swap"); void card.offsetWidth; card.classList.add("is-swap");
    }
    $$("[data-sl] button", box).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); st.l = b.getAttribute("data-v"); render(); }); });
    $$("[data-sc] button", box).forEach(function (b) { b.addEventListener("click", function () { segPress(b.parentNode, b); st.c = b.getAttribute("data-v"); render(); }); });
    render();
  });

  /* Canopy Twist, drawn live: move across it to twist */
  $$("[data-canopy]").forEach(function (box) {
    var svg = $("svg", box), N = 72, NS = "http://www.w3.org/2000/svg", lines = [], twist = 0.5, target = 0.5, raf = 0;
    function lerp(a, b, t) { return a + (b - a) * t; }
    function quad(p0, p1, p2, t) { return [lerp(lerp(p0[0], p1[0], t), lerp(p1[0], p2[0], t), t), lerp(lerp(p0[1], p1[1], t), lerp(p1[1], p2[1], t), t)]; }
    for (var i = 0; i <= N; i++) { var l = document.createElementNS(NS, "line"); l.setAttribute("stroke", "url(#cnG)"); l.setAttribute("stroke-width", "1"); svg.appendChild(l); lines.push(l); }
    function draw() {
      var apex = [lerp(150, 290, twist), lerp(20, 60, twist)], tail = [lerp(560, 520, twist), lerp(70, 40, twist)], ctrl = [lerp(260, 360, 1 - twist), lerp(160, 90, twist)];
      lines.forEach(function (l, i) {
        var t = i / N, a = t < 0.42 ? [lerp(30, apex[0], t / 0.42), lerp(210, apex[1], t / 0.42)] : [lerp(apex[0], tail[0], (t - 0.42) / 0.58), lerp(apex[1], tail[1], (t - 0.42) / 0.58)], b = quad([30, 210], ctrl, [575, 280], t);
        l.setAttribute("x1", a[0].toFixed(1)); l.setAttribute("y1", a[1].toFixed(1)); l.setAttribute("x2", b[0].toFixed(1)); l.setAttribute("y2", b[1].toFixed(1));
        l.setAttribute("opacity", (0.3 + 0.7 * Math.sin(Math.PI * t)).toFixed(2));
      });
    }
    function tick() { twist += (target - twist) * 0.12; draw(); raf = Math.abs(target - twist) > 0.002 ? requestAnimationFrame(tick) : 0; }
    function go() { if (!raf) raf = requestAnimationFrame(tick); }
    box.addEventListener("pointermove", function (e) { var r = box.getBoundingClientRect(); target = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width)); go(); });
    box.addEventListener("pointerleave", function () { target = 0.5; go(); });
    draw();
    if (!reduce && io) {
      var on = false, t0 = 0, touching = false;
      function breathe(ts) { if (!on || touching) return; if (!t0) t0 = ts; if (!raf) { twist = 0.5 + 0.2 * Math.sin((ts - t0) / 1400); target = twist; draw(); } requestAnimationFrame(breathe); }
      new IntersectionObserver(function (es) { on = es[0].isIntersecting; if (on) requestAnimationFrame(breathe); }).observe(box);
      box.addEventListener("pointerenter", function () { touching = true; });
      box.addEventListener("pointerleave", function () { setTimeout(function () { touching = false; t0 = 0; if (on) requestAnimationFrame(breathe); }, 600); });
    }
  });

  /* Screen tabs (browser and phone frames) */
  $$("[data-screens]").forEach(function (box) {
    var tabs = $$(".sc-screen-tabs button", box), img = $(".sc-browser .sc-view img", box), view = $(".sc-browser .sc-view", box);
    tabs.forEach(function (b) { b.addEventListener("click", function () { tabs.forEach(function (x) { x.setAttribute("aria-selected", x === b ? "true" : "false"); }); img.removeAttribute("srcset"); img.src = b.getAttribute("data-src"); img.setAttribute("data-full", b.getAttribute("data-full") || b.getAttribute("data-src")); img.alt = b.getAttribute("data-alt"); img.setAttribute("data-cap", b.getAttribute("data-alt")); view.scrollTop = 0; }); });
  });

  /* CARS24 internal tools: one pressed chip in a group */
  function chips(group, fn) {
    var bs = $$("button", group);
    bs.forEach(function (b) { b.addEventListener("click", function () { bs.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); fn(b.getAttribute("data-v")); }); });
  }

  /* Surface roles × states: semantic token → primitive → value */
  var STATES = ["default", "hover", "active", "pressed", "focused", "disabled"];
  $$("[data-surf]").forEach(function (box) {
    var roles = box.getAttribute("data-roles").split("|").map(function (r) {
      var p = r.split(";"); return { id: p[0], label: p[1], text: p[2], v: p[3].split(",").map(function (x) { return x.split(":"); }) };
    });
    var role = 2, st = 0, cells = $$(".it-surf-grid > div", box), sw = $("[data-sw]", box);
    function show() {
      var r = roles[role], v = r.v[st];
      sw.style.setProperty("--c", v[1]); sw.style.setProperty("--t", st === 5 && r.id === "brand" ? "#a5a3f5" : r.text);
      $("[data-sl]", box).textContent = r.label + " · " + STATES[st];
      $("[data-sem]", box).textContent = "color-surface-" + r.id + "-" + STATES[st];
      $("[data-pri]", box).textContent = v[0]; $("[data-hex]", box).textContent = v[1].toUpperCase();
      cells.forEach(function (row, i) { $$("i", row).forEach(function (c, j) { c.classList.toggle("on", i === role && j === st); }); });
    }
    chips($("[data-role]", box), function (v) { role = +v; show(); });
    chips($("[data-state]", box), function (v) { st = +v; show(); });
    show();
  });

  /* Storybook recreation: controls drive the button and the code line */
  $$("[data-sb]").forEach(function (sb) {
    var btn = $("[data-ib]", sb), code = $("[data-code]", sb), lbl = $("[data-lbl]", btn), input = $("[data-ctl-label]", sb);
    var TOK = { primary: "color-surface-brand", secondary: "color-surface-secondary", minimal: "color-surface-subtle", destructive: "color-border-error" };
    function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
    function render() {
      var v = btn.getAttribute("data-variant"), s = btn.getAttribute("data-size"), st = btn.getAttribute("data-state");
      btn.disabled = st === "disabled";
      var tokState = { default: "default", hover: "hover", focus: "focused", loading: "default", disabled: "disabled" }[st];
      code.innerHTML = "<u>&lt;</u><b>Button</b> <i>variant</i>=\"" + v + "\" <i>size</i>=\"" + s + "\"" + (st === "loading" ? " <i>loading</i>" : st === "disabled" ? " <i>disabled</i>" : "") + "<u>&gt;</u>" + esc(lbl.textContent) + "<u>&lt;/</u><b>Button</b><u>&gt;</u>\n<u>// surface</u> " + TOK[v] + "-" + tokState + "   <u>// radius</u> radius-sm   <u>// height</u> " + (s === "md" ? "36" : "30") + "px";
    }
    $$("[data-ctl]", sb).forEach(function (g) { var k = g.getAttribute("data-ctl"); chips(g, function (val) { btn.setAttribute("data-" + k, val); render(); }); });
    if (input) input.addEventListener("input", function () { lbl.textContent = input.value.trim() || "Button"; render(); });
    render();
  });

  /* Live data table: search, city filter, sort, density, selection */
  $$("[data-dt]").forEach(function (dt) {
    var tbody = $("tbody", dt), rows = $$("tbody tr", dt), q = $("[data-dt-q]", dt), menu = $("[data-dt-menu]", dt), open = $("[data-dt-open]", dt), count = $("[data-dt-count]", dt);
    var cities = [], sortCol = -1, dir = 1;
    function apply() {
      var term = (q.value || "").toLowerCase().replace(/\s/g, ""), shown = 0;
      rows.forEach(function (r) {
        var ok = (!cities.length || cities.indexOf(r.getAttribute("data-city")) > -1) && (!term || r.textContent.toLowerCase().replace(/\s/g, "").indexOf(term) > -1);
        r.hidden = !ok; if (ok) shown++;
      });
      $("[data-dt-sum]", dt).textContent = shown + " of " + rows.length + " leads";
      var sel = rows.filter(function (r) { return !r.hidden && $("input", r).checked; }).length;
      $("[data-dt-sel]", dt).textContent = sel ? sel + " selected" : "";
      count.hidden = !cities.length; count.textContent = cities.length;
    }
    q.addEventListener("input", apply);
    open.addEventListener("click", function () { var o = menu.hidden; menu.hidden = !o; open.setAttribute("aria-expanded", o ? "true" : "false"); });
    $("[data-dt-apply]", dt).addEventListener("click", function () { cities = $$("input:checked", menu).map(function (i) { return i.value; }); menu.hidden = true; open.setAttribute("aria-expanded", "false"); apply(); });
    $("[data-dt-clear]", dt).addEventListener("click", function () { $$("input", menu).forEach(function (i) { i.checked = false; }); cities = []; apply(); });
    document.addEventListener("click", function (e) { if (!menu.hidden && !e.target.closest(".it-dt-pop")) { menu.hidden = true; open.setAttribute("aria-expanded", "false"); } });
    $$("[data-sort]", dt).forEach(function (b) {
      b.addEventListener("click", function () {
        var c = +b.getAttribute("data-sort"); dir = sortCol === c ? -dir : -1; sortCol = c;
        $$("[data-sort]", dt).forEach(function (x) { x.removeAttribute("data-dir"); $("span", x).textContent = "↕"; });
        b.setAttribute("data-dir", dir); $("span", b).textContent = dir > 0 ? "↑" : "↓";
        rows.slice().sort(function (a, z) { return (+a.children[c].getAttribute("data-n") - +z.children[c].getAttribute("data-n")) * dir; }).forEach(function (r) { tbody.appendChild(r); });
      });
    });
    var dens = $$(".it-dt-dens button", dt);
    dens.forEach(function (b) { b.addEventListener("click", function () { dens.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); dt.setAttribute("data-density", b.getAttribute("data-d")); }); });
    var all = $("[data-dt-all]", dt);
    all.addEventListener("change", function () { rows.forEach(function (r) { if (!r.hidden) { $("input", r).checked = all.checked; r.classList.toggle("sel", all.checked); } }); apply(); });
    rows.forEach(function (r) { $("input", r).addEventListener("change", function (e) { r.classList.toggle("sel", e.target.checked); apply(); }); });
    apply();
  });

  /* ---------- Speed: preload hidden and off-screen media before it's needed ---------- */
  // Images inside carousels, tabs and screen viewers are lazy and often off-screen sideways or hidden, so the browser
  // only fetches them on swipe or click. Warm them as soon as the component comes near the viewport.
  function warm(box) {
    $$("img[loading=lazy]", box).forEach(function (im) { im.loading = "eager"; });
    $$("[data-src]", box).forEach(function (b) { var i = new Image(); i.decoding = "async"; i.src = b.getAttribute("data-src"); });
  }
  var warmSel = "[data-carousel], [data-tabs], [data-screens], [data-compare], .lg-phones, .lg-pair, .cs-gallery";
  if ("IntersectionObserver" in window) {
    var warmIO = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { warm(e.target); warmIO.unobserve(e.target); } }); }, { rootMargin: "900px 0px" });
    $$(warmSel).forEach(function (el) { warmIO.observe(el); });
  } else $$(warmSel).forEach(warm);

  /* ---------- Speed: prefetch pages on hover or touch, for browsers without speculation rules ---------- */
  if (!(window.HTMLScriptElement && HTMLScriptElement.supports && HTMLScriptElement.supports("speculationrules"))) {
    var seen = {};
    var pre = function (e) {
      var a = e.target.closest && e.target.closest("a[href]"); if (!a) return;
      var u = new URL(a.href, location.href);
      if (u.origin !== location.origin || u.pathname === location.pathname || /\.[a-z0-9]{2,4}$/i.test(u.pathname) || seen[u.pathname]) return;
      seen[u.pathname] = 1; var l = document.createElement("link"); l.rel = "prefetch"; l.href = u.pathname; document.head.appendChild(l);
    };
    document.addEventListener("pointerover", pre, { passive: true }); document.addEventListener("touchstart", pre, { passive: true });
  }

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
