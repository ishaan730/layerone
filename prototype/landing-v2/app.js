/* Layer One landing prototype v2. No dependencies.
   Everything here is progressive enhancement: the page reads and works with this file missing.
   Motion is skipped entirely when the visitor asks for reduced motion. */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  var $ = function (s, r) { return (r || doc).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || doc).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var still = function () { return reduce.matches; };
  var wide = window.matchMedia("(min-width: 961px)");
  var hasIO = "IntersectionObserver" in window;

  /* ---------- Hero entrance, then the board resolves from drift to system ---------- */
  var hero = $(".hero"), board = $("#board"), count = $("#b-count"), segs = $$(".seg button");
  function setBoard(state, user) {
    if (!board) return;
    var drift = state === "drift";
    board.classList.toggle("is-drift", drift);
    if (count) count.textContent = drift ? "11 styles" : "3 tokens";
    segs.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-state") === state ? "true" : "false"); });
    if (user) played = true;
  }
  var played = false;
  segs.forEach(function (b) { b.addEventListener("click", function () { setBoard(b.getAttribute("data-state"), true); }); });
  function ready() {
    hero.classList.add("is-ready");
    if (still()) { setBoard("system"); return; }
    setTimeout(function () { if (!played) setBoard("system"); }, 2100);
  }
  if (doc.fonts && doc.fonts.ready) { var t = setTimeout(ready, 900); doc.fonts.ready.then(function () { clearTimeout(t); requestAnimationFrame(ready); }); } else ready();

  /* A small parallax on the board: it leans a few pixels toward the pointer. Fine pointers only. */
  if (board && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    var raf = 0;
    hero.addEventListener("pointermove", function (e) {
      if (still() || raf) return;
      raf = requestAnimationFrame(function () {
        raf = 0;
        var r = hero.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        board.style.transform = "translate3d(" + (x * -14).toFixed(1) + "px," + (y * -10).toFixed(1) + "px,0) rotate(" + (x * .6).toFixed(2) + "deg)";
      });
    });
    hero.addEventListener("pointerleave", function () { board.style.transform = ""; });
  }

  /* ---------- One token, the whole page: the accent picker ---------- */
  var picks = $$("[data-accent]");
  picks.forEach(function (b) {
    b.addEventListener("click", function () {
      root.style.setProperty("--accent", b.getAttribute("data-accent"));
      root.style.setProperty("--on-accent", b.getAttribute("data-on"));
      picks.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      setBoard("system", true);
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var reveals = $$("[data-reveal]");
  if (hasIO && !still()) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting || e.boundingClientRect.top < 0) { e.target.classList.add("in"); io.unobserve(e.target); } });  // anything already scrolled past is shown too
    }, { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else reveals.forEach(function (el) { el.classList.add("in"); });

  /* Things that play once when they come into view: symptom cards resolve, the timeline fills */
  function once(els, cls, opts) {
    if (!hasIO || still()) { els.forEach(function (el) { el.classList.add(cls); }); return; }
    var o = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, i = +(el.style.getPropertyValue("--i") || 0);
        setTimeout(function () { el.classList.add(cls); }, (opts.delay || 0) + i * (opts.stagger || 0));
        o.unobserve(el);
      });
    }, { threshold: opts.threshold || .5 });
    els.forEach(function (el) { o.observe(el); });
  }
  var symptoms = $$("[data-fix]");
  once(symptoms, "fixed", { delay: 900, stagger: 450, threshold: .55 });
  symptoms.forEach(function (el) {            // tap or click to compare before and after
    el.addEventListener("click", function () { el.classList.toggle("fixed"); });
  });
  once($$("[data-inview]"), "in", { threshold: .6 });

  /* ---------- Numbers count up ---------- */
  var counters = $$("[data-count]");
  function fmt(n, sep) { return sep ? Math.round(n).toLocaleString("en-US") : String(Math.round(n)); }
  if (hasIO && !still()) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, to = +el.getAttribute("data-count"), sep = el.hasAttribute("data-sep"), t0 = null, dur = 1400;
        co.unobserve(el);
        requestAnimationFrame(function step(ts) {
          if (t0 === null) t0 = ts;
          var p = Math.min(1, (ts - t0) / dur), k = 1 - Math.pow(1 - p, 4);
          el.textContent = fmt(to * k, sep);
          if (p < 1) requestAnimationFrame(step);
        });
      });
    }, { threshold: .6 });
    counters.forEach(function (el) { el.textContent = "0"; co.observe(el); });
  }

  /* ---------- The four layers: pinned on wide screens, a plain list everywhere else ---------- */
  var track = $("#layers-track"), stack = $("#stack"), steps = $$(".step"), plates = $$(".plate");
  var titles = [["Tokens", "the foundation everything inherits"], ["Components", "the parts teams reach for"], ["Patterns", "how the parts combine"], ["Governance", "what keeps it alive"]];
  var active = -1;
  function setLayer(i) {
    if (i === active) return; active = i;
    var pinned = wide.matches && !still();
    steps.forEach(function (s, k) { var on = k === i; s.classList.toggle("on", on || !pinned); $("button", s).setAttribute("aria-expanded", on || !pinned ? "true" : "false"); });
    plates.forEach(function (p, k) { p.classList.toggle("on", k === i); });
    $("#stage-title").textContent = titles[i][0]; $("#stage-sub").textContent = titles[i][1];
  }
  function layerScroll() {
    if (!track) return;
    var r = track.getBoundingClientRect(), vh = window.innerHeight;
    if (wide.matches && !still()) {
      var p = Math.max(0, Math.min(1, -r.top / Math.max(1, r.height - vh)));
      setLayer(Math.min(3, Math.floor(p * 4)));
      // the stack opens up as the section arrives and stays open
      var enter = Math.max(0, Math.min(1, (vh - r.top) / vh));
      stack.style.setProperty("--gap", (18 + enter * 52 + p * 14).toFixed(1) + "px");
    } else {
      stack.style.setProperty("--gap", "54px");
      // on small screens the layer nearest the middle of the viewport lights up
      var best = 0, bd = 1e9;
      steps.forEach(function (s, k) { var b = s.getBoundingClientRect(), d = Math.abs((b.top + b.bottom) / 2 - vh * .55); if (d < bd) { bd = d; best = k; } });
      setLayer(best);
    }
  }
  function goLayer(i) {
    if (wide.matches && !still() && track) {
      var top = track.getBoundingClientRect().top + window.scrollY, span = track.offsetHeight - window.innerHeight;
      window.scrollTo({ top: top + span * ((i + .5) / 4), behavior: "smooth" });
    } else { active = -1; setLayer(i); }
  }
  steps.forEach(function (s, k) { $("button", s).addEventListener("click", function () { goLayer(k); }); });
  plates.forEach(function (p, k) { p.addEventListener("click", function () { goLayer(k); }); });

  /* ---------- Pricing: standard and founding-partner prices ---------- */
  var founding = $("#founding"), plans = $("#plans");
  if (founding) founding.addEventListener("change", function () {
    var on = founding.checked;
    plans.classList.toggle("founding", on);
    $$("[data-price]", plans).forEach(function (b, i) {
      var v = "$" + (+b.getAttribute(on ? "data-founding" : "data-price")).toLocaleString("en-US");
      if (still()) { b.textContent = v; return; }
      setTimeout(function () { b.classList.add("swap"); setTimeout(function () { b.textContent = v; b.classList.remove("swap"); }, 220); }, i * 70);
    });
  });

  /* ---------- Rules marquee: duplicate each row so the loop is seamless ---------- */
  if (!still()) $$(".marquee ul").forEach(function (ul) { var c = ul.cloneNode(true); c.removeAttribute("id"); c.setAttribute("aria-hidden", "true"); ul.parentNode.appendChild(c); });
  root.style.setProperty("--mark", "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath fill-rule='evenodd' d='M50 0a50 50 0 1 1 0 100A50 50 0 0 1 50 0ZM16.3 50A34 34 0 0 0 50 16.3V49.2a.8.8 0 0 1-.8.8ZM83.7 50A34 34 0 0 0 50 83.7V50.8a.8.8 0 0 1 .8-.8Z'/%3E%3C/svg%3E\")");

  /* ---------- A real tool on the page: WCAG contrast ---------- */
  (function () {
    var fg = $("#cc-fg"), bg = $("#cc-bg"); if (!fg || !bg) return;
    var prev = $(".cc-prev"), ratio = $("#cc-ratio"), pass = $("#cc-pass");
    function lum(h) { var c = [1, 3, 5].map(function (i) { var v = parseInt(h.substr(i, 2), 16) / 255; return v <= .04045 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]; }
    function draw() {
      var a = lum(fg.value), b = lum(bg.value), r = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
      prev.style.setProperty("--cc-fg", fg.value); prev.style.setProperty("--cc-bg", bg.value);
      $("#cc-fg-o").textContent = fg.value; $("#cc-bg-o").textContent = bg.value;
      ratio.textContent = r.toFixed(2) + ":1";
      pass.innerHTML = [["AA text", 4.5], ["AA large", 3], ["AAA", 7]].map(function (x) { var ok = r >= x[1]; return '<li class="' + (ok ? "ok" : "no") + '">' + x[0] + (ok ? " ✓" : " ✕") + "</li>"; }).join("");
    }
    fg.addEventListener("input", draw); bg.addEventListener("input", draw); draw();
  })();

  /* ---------- Nav: progress, current section, phone menu, phone dock ---------- */
  var nav = $("#nav"), prog = $(".nav-progress"), dock = $("#dock"), finalSec = $("#start"), links = $$(".nav-links a");
  var secs = links.map(function (a) { return $(a.getAttribute("href")); });
  var ticking = false, wm = $("#wordmark");
  function onScroll() {
    ticking = false;
    var y = window.scrollY, max = doc.documentElement.scrollHeight - window.innerHeight, vh = window.innerHeight;
    if (prog) prog.style.setProperty("--p", max > 0 ? (y / max).toFixed(4) : 0);
    var cur = -1; secs.forEach(function (s, i) { if (s && s.getBoundingClientRect().top < vh * .4) cur = i; });
    links.forEach(function (a, i) { if (i === cur) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    if (dock && finalSec) dock.classList.toggle("show", y > vh * .8 && finalSec.getBoundingClientRect().top > vh * .7);
    layerScroll();
    if (wm && !still()) { var wr = wm.getBoundingClientRect(); if (wr.top < vh) wm.style.setProperty("--spread", (1 + Math.max(0, Math.min(1, (vh - wr.top) / (vh * .6))) * 1.6).toFixed(2)); }
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener("resize", function () { active = -1; onScroll(); });
  if (wide.addEventListener) wide.addEventListener("change", function () { active = -1; onScroll(); });

  var menu = $("#menu"), menuBtn = $(".nav-menu"), menuOpen = false;
  function setMenu(open) {
    menuOpen = open;
    menu.classList.toggle("open", open); menu.inert = !open;
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false"); menuBtn.textContent = open ? "Close" : "Menu";
    doc.body.style.overflow = open ? "hidden" : "";
    if (open) { var f = $("a", menu); if (f) f.focus({ preventScroll: true }); } else menuBtn.focus({ preventScroll: true });
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () { setMenu(!menuOpen); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { if (menuOpen) { menuOpen = false; menu.classList.remove("open"); menu.inert = true; menuBtn.setAttribute("aria-expanded", "false"); menuBtn.textContent = "Menu"; doc.body.style.overflow = ""; } }); });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && menuOpen) setMenu(false); });
    if (wide.addEventListener) wide.addEventListener("change", function () { if (wide.matches && menuOpen) setMenu(false); });
  }

  /* FAQ: one answer open at a time keeps the list scannable */
  var qs = $$(".qa details");
  qs.forEach(function (d) { d.addEventListener("toggle", function () { if (d.open) qs.forEach(function (o) { if (o !== d) o.open = false; }); }); });

  onScroll();
})();
