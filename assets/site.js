/* Layer One — shared behaviour. No dependencies. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Theme ---------- */
  function storedTheme() {
    try { return localStorage.getItem("l1-theme"); } catch (e) { return null; }
  }
  var saved = storedTheme();
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  function currentTheme() {
    var t = root.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    function label() { btn.setAttribute("aria-label", currentTheme() === "dark" ? "Switch to light theme" : "Switch to dark theme"); }
    label();
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("l1-theme", next); } catch (e) {}
      label();
    });
  });

  /* ---------- Header ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    var menuBtn = header.querySelector(".menu-toggle");
    if (menuBtn) {
      menuBtn.addEventListener("click", function () {
        var open = header.classList.toggle("is-open");
        menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
        menuBtn.firstChild.textContent = open ? "Close" : "Menu";
      });
    }
  }

  /* ---------- Layer stack: change one value, watch it travel up ---------- */
  var stack = document.querySelector("[data-stack]");
  if (stack) {
    var layers = Array.prototype.slice.call(stack.querySelectorAll(".layer")).reverse(); // value first
    var valueText = stack.querySelector("[data-value-text]");
    var primitiveText = stack.querySelector("[data-primitive-text]");
    var buttons = stack.querySelectorAll(".value-picker button");
    var timers = [];
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        var hex = b.getAttribute("data-hex");
        valueText.textContent = hex.toUpperCase();
        primitiveText.textContent = b.getAttribute("data-primitive");
        timers.forEach(clearTimeout);
        timers = [];
        layers.forEach(function (layer, i) {
          var delay = reduceMotion ? 0 : i * 160;
          timers.push(setTimeout(function () {
            layer.classList.add("is-pulse");
            if (i === layers.length - 1) stack.style.setProperty("--brand", hex);
          }, delay));
          timers.push(setTimeout(function () { layer.classList.remove("is-pulse"); }, delay + 520));
        });
        if (reduceMotion) stack.style.setProperty("--brand", hex);
      });
    });
  }

  /* ---------- Tabs (situations) ---------- */
  document.querySelectorAll("[role=tablist]").forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll("[role=tab]"));
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t, false); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = null;
        if (k === "ArrowDown" || k === "ArrowRight") n = tabs[(i + 1) % tabs.length];
        if (k === "ArrowUp" || k === "ArrowLeft") n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (k === "Home") n = tabs[0];
        if (k === "End") n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n, true); }
      });
    });
  });

  /* ---------- Case study contents: highlight the section in view ---------- */
  var toc = document.querySelector(".cs-toc");
  if (toc && "IntersectionObserver" in window) {
    var links = toc.querySelectorAll("a");
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          links.forEach(function (a) { a.classList.remove("is-active"); });
          var a = map[en.target.id];
          if (a) a.classList.add("is-active");
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  /* ---------- Request scorecard ---------- */
  var scorer = document.querySelector("[data-scorer]");
  if (scorer) {
    var out = scorer.querySelector("[data-total]");
    var verdict = scorer.querySelector("[data-verdict]");
    var detail = scorer.querySelector("[data-detail]");
    var update = function () {
      var total = 0, wontFix = false, answered = 0;
      var groups = scorer.querySelectorAll("fieldset");
      groups.forEach(function (g) {
        var c = g.querySelector("input:checked");
        if (!c) return;
        answered++;
        if (c.value === "x") wontFix = true; else total += parseInt(c.value, 10);
      });
      out.textContent = wontFix ? "—" : String(total);
      var v, d;
      if (wontFix) { v = "Won't fix: reject"; d = "One question rules it out. The team builds it outside the system, using the design language."; }
      else if (answered < groups.length) { v = "Answer all four"; d = "The score only means something once every question has an answer."; }
      else if (total >= 55) { v = "High: accept, we build it"; d = "Picked up first, as soon as the design system team has capacity."; }
      else if (total >= 40) { v = "Medium: accept"; d = "Picked up after high-priority work. If the team needs it sooner, it can contribute."; }
      else { v = "Low: defer"; d = "Unlikely to be picked up. The team can build it as a custom or extended component."; }
      verdict.textContent = v;
      detail.textContent = d;
    };
    scorer.addEventListener("change", update);
    update();
  }

  /* ---------- Year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
