"""Lab: free design system tools. Full-width workspace, one tool per tab.

Tools: palette builder (OKLCH ramps from a brand colour), contrast checker (WCAG 2 + APCA, one-click fixes,
pair matrix), type scale, spacing and radius, token name linter, request backlog (the 70-point scorecard),
and an export kit that bundles palette, type, spacing and radius into one file.
Behaviour: assets/lab.js (loaded only here). Styles: "Lab (v2)" in assets/site.css.
State is saved in the browser (localStorage) and can be shared as a link (#s=...).
"""
from common import *

ICON = {
    "palette": '<circle cx="12" cy="12" r="9"/><circle cx="8" cy="10" r="1.6" fill="currentColor"/><circle cx="12" cy="7.5" r="1.6" fill="currentColor"/><circle cx="16" cy="10" r="1.6" fill="currentColor"/><path d="M12 21a3 3 0 0 1 0-6h1.5a2 2 0 0 0 0-4"/>',
    "contrast": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18a9 9 0 0 0 0-18Z" fill="currentColor"/>',
    "type": '<path d="M4 7V5h11v2M9.5 5v14M7 19h5"/><path d="M14 12v-1.5h7V12M17.5 10.5V19M16 19h3"/>',
    "space": '<path d="M4 4v16M20 4v16"/><path d="M8 12h8M8 12l2.5-2.5M8 12l2.5 2.5M16 12l-2.5-2.5M16 12l-2.5 2.5"/>',
    "names": '<path d="M5 7h10M5 12h14M5 17h7"/><path d="m16 16 2 2 4-4"/>',
    "backlog": '<rect x="4" y="4" width="16" height="4" rx="1"/><rect x="4" y="10" width="12" height="4" rx="1"/><rect x="4" y="16" width="8" height="4" rx="1"/>',
    "kit": '<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 17v3h16v-3"/>',
}


def ico(n):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'


TOOLS = [("palette", "Palette", "From one colour"), ("contrast", "Contrast", "WCAG and APCA"),
         ("type", "Type scale", "Sizes and lines"), ("space", "Spacing", "Space and radius"),
         ("names", "Token names", "Lint and fix"), ("backlog", "Backlog", "Rank requests"),
         ("kit", "Export kit", "One file")]

tabs = "".join(f'<button type="button" role="tab" id="tab-{k}" aria-controls="p-{k}" aria-selected="{"true" if i == 0 else "false"}" data-tab="{k}">{ico(k)}<span><b>{t}</b><small>{d}</small></span></button>' for i, (k, t, d) in enumerate(TOOLS))


def exp(key, formats=("css", "tailwind", "json", "scss")):
    """Export bar: format switch, copy, download, and the code."""
    lab = {"css": "CSS", "tailwind": "Tailwind", "json": "JSON (DTCG)", "scss": "SCSS", "csv": "CSV", "md": "Markdown", "txt": "Fixed list"}
    if key in ("names", "backlog"):
        lab["json"] = "JSON"
    seg = "".join(f'<button type="button" data-fmt="{f}" aria-pressed="{"true" if i == 0 else "false"}">{lab[f]}</button>' for i, f in enumerate(formats))
    return f'''<div class="lx-exp" data-exp="{key}">
      <div class="lx-exp-bar"><div class="lx-seg" role="group" aria-label="Export format">{seg}</div>
        <div class="lx-exp-act"><button type="button" class="lx-btn" data-copy>Copy</button><button type="button" class="lx-btn" data-dl>Download</button></div></div>
      <pre class="lx-code" tabindex="0" aria-label="Exported code"><code></code></pre>
    </div>'''


def field(label, inner, hint=""):
    return f'<label class="lx-f"><span class="lx-l">{label}{f"<em>{hint}</em>" if hint else ""}</span>{inner}</label>'


def rng(name, lo, hi, step, val, label, unit=""):
    return f'<label class="lx-f"><span class="lx-l">{label}<output data-out="{name}"></output>{unit and f"<i>{unit}</i>"}</span><input type="range" name="{name}" min="{lo}" max="{hi}" step="{step}" value="{val}"></label>'


def sel(name, opts, label):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<label class="lx-f"><span class="lx-l">{label}</span><select name="{name}">{o}</select></label>'


def seg(name, opts, label):
    b = "".join(f'<button type="button" data-v="{v}" aria-pressed="false">{t}</button>' for v, t in opts)
    return f'<div class="lx-f"><span class="lx-l">{label}</span><div class="lx-seg" data-name="{name}" role="group" aria-label="{label}">{b}</div></div>'


# ---------------------------------------------------------------- panels
palette = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Palette settings">
    <div class="lx-card">
      <div class="lx-card-h"><b>Ramps</b><div class="lx-add"><button type="button" class="lx-btn lx-btn--sm" data-add-ramp aria-expanded="false">+ Add ramp</button>
        <div class="lx-menu" data-add-menu hidden><button type="button" data-preset="neutral">Neutral, tinted from brand</button><button type="button" data-preset="success">Success</button><button type="button" data-preset="warning">Warning</button><button type="button" data-preset="danger">Danger</button><button type="button" data-preset="info">Info</button><button type="button" data-preset="custom">Custom colour</button></div></div></div>
      <ul class="lx-ramps" data-ramp-list></ul>
    </div>
    <div class="lx-card" data-ramp-editor>
      <div class="lx-card-h"><b>Edit <span data-edit-name>brand</span></b><button type="button" class="lx-icon" data-del-ramp aria-label="Delete this ramp">✕</button></div>
      {field("Name", '<input type="text" name="rname" maxlength="20" spellcheck="false">')}
      <div class="lx-f"><span class="lx-l">Colour <em>paste a hex</em></span><div class="lx-hex"><input type="color" name="rcolor" aria-label="Pick a colour"><input type="text" name="rhex" maxlength="7" spellcheck="false" aria-label="Hex value"></div></div>
      {rng("hue", 0, 360, 1, 275, "Hue", "°")}
      {rng("chroma", 0, 0.37, 0.005, 0.2, "Chroma")}
      <label class="lx-check"><input type="checkbox" name="pin" checked><span>Keep my exact colour at the closest step</span></label>
    </div>
    <div class="lx-card">
      <div class="lx-card-h"><b>Scale</b></div>
      {seg("steps", [("10", "50–900"), ("11", "50–950"), ("12", "25–950")], "Steps")}
      {rng("lmax", 0.9, 0.995, 0.005, 0.975, "Lightest")}
      {rng("lmin", 0.12, 0.4, 0.01, 0.24, "Darkest")}
      {seg("gamut", [("srgb", "sRGB"), ("p3", "Display P3")], "Fit to")}
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-sheet" data-sheet aria-live="polite"></div>
    <p class="lx-hint">Select a swatch to copy its value. Badges show WCAG 2 contrast with white and black text.</p>
    <div class="lx-prev" data-prev>
      <div class="lx-prev-h"><b>Preview</b><div class="lx-seg" data-prev-mode role="group" aria-label="Preview theme"><button type="button" data-v="both" aria-pressed="true">Light and dark</button><button type="button" data-v="light" aria-pressed="false">Light</button><button type="button" data-v="dark" aria-pressed="false">Dark</button></div></div>
      <div class="lx-prev-grid" data-prev-grid></div>
    </div>
    {exp("palette")}
  </div>
</div>'''

contrast = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Contrast settings">
    <div class="lx-card">
      <div class="lx-card-h"><b>Colours</b><button type="button" class="lx-btn lx-btn--sm" data-swap>⇅ Swap</button></div>
      <div class="lx-f"><span class="lx-l">Text</span><div class="lx-hex"><input type="color" name="fgc" aria-label="Pick the text colour"><input type="text" name="fg" maxlength="7" spellcheck="false" aria-label="Text hex"></div></div>
      <div class="lx-f"><span class="lx-l">Background</span><div class="lx-hex"><input type="color" name="bgc" aria-label="Pick the background colour"><input type="text" name="bg" maxlength="7" spellcheck="false" aria-label="Background hex"></div></div>
      <div class="lx-f"><span class="lx-l">From your palette <em>click for text, shift-click for background</em></span><div class="lx-mini" data-mini></div></div>
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Pair matrix</b></div>
      {sel("mramp", [], "Ramp")}
      {seg("mmin", [("3", "3:1"), ("4.5", "4.5:1"), ("7", "7:1")], "Show pairs that pass")}
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-cview" data-cview>
      <div class="lx-cpreview" data-cpreview>
        <p class="t-l">Design systems ship faster</p>
        <p class="t-b">Body text at 16px. Your team reads this all day, so it needs to pass comfortably, not just barely.</p>
        <p class="t-s">Small print at 13px · Last updated 2 hours ago</p>
        <div class="t-ui"><span class="t-btn">Button</span><span class="t-out">Outlined</span><span class="t-ic" aria-hidden="true">★</span></div>
      </div>
      <div class="lx-cres">
        <div class="lx-ratio"><strong data-ratio>—</strong><span>WCAG 2 ratio</span></div>
        <div class="lx-apca"><strong data-apca>—</strong><span>APCA Lc</span></div>
        <ul class="lx-pass" data-pass></ul>
        <p class="lx-apca-note" data-apca-note></p>
      </div>
    </div>
    <div class="lx-fix" data-fix></div>
    <div class="lx-matrix-wrap"><div class="lx-matrix" data-matrix></div></div>
    <p class="lx-hint">Rows are text, columns are backgrounds. Select a cell to load the pair above.</p>
  </div>
</div>'''

types = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Type scale settings">
    <div class="lx-card"><div class="lx-card-h"><b>Scale</b></div>
      {rng("tbase", 12, 20, 1, 16, "Base size", "px")}
      {sel("tratio", [("1.067", "1.067 · Minor second"), ("1.125", "1.125 · Major second"), ("1.2", "1.2 · Minor third"), ("1.25", "1.25 · Major third"), ("1.333", "1.333 · Perfect fourth"), ("1.414", "1.414 · Augmented fourth"), ("1.5", "1.5 · Perfect fifth"), ("1.618", "1.618 · Golden ratio")], "Ratio")}
      {rng("tup", 3, 9, 1, 6, "Steps above base")}
      {rng("tdown", 0, 3, 1, 2, "Steps below base")}
      {seg("tround", [("1", "Whole px"), ("2", "Even px"), ("4", "4px grid"), ("0", "Exact")], "Rounding")}
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Lines and names</b></div>
      {rng("tlh", 1.3, 1.7, 0.05, 1.5, "Body line height")}
      {rng("tlhd", 1.0, 1.3, 0.05, 1.1, "Display line height")}
      {seg("tname", [("shirt", "xs · md · 2xl"), ("num", "100 · 400 · 900"), ("role", "body · heading")], "Token names")}
      {sel("tfont", [("Schibsted Grotesk, sans-serif", "Schibsted Grotesk"), ("ui-sans-serif, system-ui, sans-serif", "System sans"), ("Georgia, ui-serif, serif", "Serif"), ("ui-monospace, Menlo, monospace", "Monospace")], "Preview font")}
      {field("Sample text", '<input type="text" name="ttext" maxlength="60" value="Ship the system, not the screenshots">')}
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-tscale" data-tscale></div>
    {exp("type")}
  </div>
</div>'''

space = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Spacing settings">
    <div class="lx-card"><div class="lx-card-h"><b>Spacing</b></div>
      {seg("sbase", [("2", "2px"), ("4", "4px"), ("8", "8px")], "Base unit")}
      {sel("smethod", [("common", "Common: 1, 2, 3, 4, 6, 8, 12, 16…"), ("linear", "Linear: every multiple"), ("double", "Doubling: 1, 2, 4, 8, 16…"), ("fib", "Fibonacci: 1, 2, 3, 5, 8, 13…")], "Method")}
      {rng("scount", 6, 16, 1, 12, "Steps")}
      {seg("sname", [("shirt", "xs · md · xl"), ("mult", "space-1 · space-4"), ("px", "space-8 · space-16")], "Token names")}
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Radius</b></div>
      {rng("rbase", 2, 12, 1, 6, "Base radius", "px")}
      {rng("rcount", 3, 7, 1, 5, "Steps")}
      <label class="lx-check"><input type="checkbox" name="rfull" checked><span>Add radius-full for pills</span></label>
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-spacebox">
      <div class="lx-sbars" data-sbars></div>
      <div class="lx-sdemo" data-sdemo>
        <p class="lx-k">Applied to a card</p>
        <div class="lx-demo-card"><div class="lx-demo-top"><i></i><div><b>Loan application</b><span>Updated 2h ago</span></div></div><p>Spacing tokens set every gap here: padding, the gap between rows, and the space around the buttons.</p><div class="lx-demo-btns"><span>Approve</span><span>Review</span></div></div>
        <label class="lx-f"><span class="lx-l">Card padding</span><select data-pad></select></label>
        <label class="lx-f"><span class="lx-l">Gap</span><select data-gap></select></label>
      </div>
    </div>
    <div class="lx-radii" data-radii></div>
    {exp("space")}
  </div>
</div>'''

names = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Linter settings">
    <div class="lx-card"><div class="lx-card-h"><b>Convention</b></div>
      {seg("nsep", [("-", "kebab-case"), (".", "dot.case"), ("/", "slash/case")], "Separator")}
      {field("Categories", '<input type="text" name="ncats" spellcheck="false" value="color, space, size, radius, font, line-height, shadow, border, opacity, motion, z">', "first word")}
      {field("States", '<input type="text" name="nstates" spellcheck="false" value="hover, active, pressed, focus, focused, disabled, selected">', "always last")}
      {rng("ndepth", 3, 8, 1, 6, "Most parts allowed")}
      <label class="lx-check"><input type="checkbox" name="nraw" checked><span>Flag raw colour names in semantic tokens</span></label>
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-names">
      <div class="lx-card lx-names-in"><div class="lx-card-h"><b>Your tokens</b><div style="display:flex;gap:6px"><button type="button" class="lx-btn lx-btn--sm" data-nexample>Load a messy example</button><button type="button" class="lx-btn lx-btn--sm" data-nclear>Clear</button></div></div>
        <textarea name="nlist" rows="14" spellcheck="false" aria-label="Token names, one per line" placeholder="Paste token names, CSS variables or a JSON token file&#10;--color-action-primary&#10;color.text.muted"></textarea>
        <p class="lx-hint" data-nparse></p></div>
      <div class="lx-card lx-names-out"><div class="lx-card-h"><b>Report</b><span class="lx-score" data-nscore></span></div>
        <div class="lx-nsum" data-nsum></div><ul class="lx-nlist" data-nresult></ul></div>
    </div>
    {exp("names", ("txt", "json"))}
  </div>
</div>'''

backlog = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="New request">
    <form class="lx-card" data-bform onsubmit="return false">
      <div class="lx-card-h"><b data-bform-title>New request</b></div>
      {field("Component or change", '<input type="text" name="bname" maxlength="60" placeholder="Date range picker" required>')}
      {field("Asked by", '<input type="text" name="bteam" maxlength="40" placeholder="Loans team">')}
      {seg("where", [("20", "Main products"), ("15", "Smaller products"), ("5", "One team"), ("x", "Nowhere")], "Where is it needed?")}
      {seg("reuse", [("20", "Many teams"), ("15", "A few teams"), ("5", "One team"), ("x", "One product")], "How many can reuse it?")}
      {seg("exists", [("15", "No"), ("10", "Partly"), ("5", "Mostly"), ("x", "Fully solved")], "Do we already have it?")}
      {seg("effort", [("15", "Under a week"), ("10", "1–3 weeks"), ("5", "3+ weeks"), ("x", "Not worth it")], "How hard is it to build?")}
      <div class="lx-bscore"><strong data-blive>0</strong><small>/ 70</small><span data-bverdict>Answer all four</span></div>
      <div class="lx-bact"><button type="submit" class="lx-btn lx-btn--accent" data-bsave>Add to backlog</button><button type="button" class="lx-btn" data-bcancel hidden>Cancel</button></div>
    </form>
  </aside>
  <div class="lx-out">
    <div class="lx-card"><div class="lx-card-h"><b>Backlog, ranked</b><div style="display:flex;gap:6px"><button type="button" class="lx-btn lx-btn--sm" data-bexample>Load examples</button><button type="button" class="lx-btn lx-btn--sm" data-bclear>Clear all</button></div></div>
      <div class="lx-bstats" data-bstats></div>
      <ol class="lx-blist" data-blist></ol>
      <p class="lx-hint">The 70-point model from the <a href="work/cars24-governance.html">CARS24 governance case study</a>. Any “✕” answer rules a request out. 55+ is high, 40–54 medium, below 40 deferred.</p>
    </div>
    {exp("backlog", ("md", "csv", "json"))}
  </div>
</div>'''

kit = f'''
<div class="lx-ws lx-ws--one">
  <div class="lx-out">
    <div class="lx-kit" data-kit></div>
    <div class="lx-f" style="max-width:420px"><span class="lx-l">Prefix <em>optional, e.g. acme</em></span><input type="text" name="kprefix" maxlength="16" spellcheck="false"></div>
    {exp("kit")}
    <div class="lx-cta"><div><b>Want this done properly, for your product?</b><p>Our two-week audit turns your real screens into a token plan, a first-components list and a rollout plan.</p></div><a class="pill pill--accent" href="pricing.html#plan-audit">See the audit</a></div>
  </div>
</div>'''

PANELS = {"palette": palette, "contrast": contrast, "type": types, "space": space, "names": names, "backlog": backlog, "kit": kit}
HEAD = {"palette": ("Palette", "Start from your brand colour. Get even, accessible ramps in OKLCH, a live UI preview in light and dark, and tokens you can paste."),
        "contrast": ("Contrast", "Check any text and background against WCAG 2 and APCA. If it fails, get the closest colour that passes, in the same hue."),
        "type": ("Type scale", "Pick a base size and a ratio. Sizes are rounded the way engineers will build them, with line heights that tighten as text grows."),
        "space": ("Spacing and radius", "A spacing scale on a base unit, tried on a real card, and a short radius scale."),
        "names": ("Token names", "Paste a token list. The linter checks it against a naming convention, explains every problem and suggests a fix."),
        "backlog": ("Request backlog", "Score every component request with the same four questions, and get a ranked backlog you can share."),
        "kit": ("Export kit", "Palette, type, spacing and radius from the other tools, in one file.")}
panels = "".join(f'''<section class="lx-panel" role="tabpanel" id="p-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"} data-panel="{k}">
  <header class="lx-ph"><h2>{HEAD[k][0]}</h2><p>{HEAD[k][1]}</p></header>{PANELS[k]}
</section>''' for i, k in enumerate(PANELS))

body = f'''<main id="main" class="lx">
  <header class="lx-hero"><div class="lx-in">
    <p class="lx-eyebrow">lab:</p>
    <div class="lx-hero-row"><div><h1>Free tools for building a design system</h1>
      <p class="lx-lede">Seven tools from the method we use on client systems: palette, contrast, type, spacing, token names and request triage. They run in your browser, save as you go, and export tokens you can paste.</p></div>
      <div class="lx-hero-act"><button type="button" class="lx-btn" data-share>Copy share link</button><button type="button" class="lx-btn" data-reset>Start over</button><span class="lx-status" data-status role="status" aria-live="polite"></span></div></div>
  </div></header>
  <nav class="lx-tabs" aria-label="Tools"><div class="lx-in"><div class="lx-tablist" role="tablist" aria-label="Lab tools">{tabs}</div></div></nav>
  <div class="lx-in">{panels}</div>
</main>'''

write("lab.html", head("Lab — Layer One", "Free design system tools: an OKLCH palette builder, a WCAG and APCA contrast checker, type and spacing scales, a token name linter, a request backlog and a token export kit.")
      + topbar("lab") + body
      + f'<script src="assets/lab.js?v={ver("assets/lab.js")}" defer></script>\n' + close())
