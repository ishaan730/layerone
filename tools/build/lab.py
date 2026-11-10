"""Lab (v3): free design system tools, one page per tool, organised around what designers are trying to do.

/lab                      the hub: search, task filters, a "start from a problem" directory, a five-step workflow, FAQ
/lab/<slug>               one tool per page: a search-intent H1, the playground first, presets, then guidance, FAQ,
                          related tools and reading. Each page has WebApplication, BreadcrumbList and FAQPage JSON-LD.

The playgrounds share one state object in the browser (assets/lab.js), so a palette made on one page feeds the
contrast checker and the token generator. Pages load assets/lab.css, a lean stylesheet purged from site.css.
To add a tool: add an entry to TOOLS (with its panel markup), a module in assets/lab.js keyed by the same name, and
its slug to SLUG in lab.js.
"""
import html as _html
import json
import os
import re

from common import *

SITE = "https://www.layerone.co.in"


def esc(s):
    return _html.escape(s, quote=True)


ICON = {
    "palette": '<circle cx="12" cy="12" r="9"/><circle cx="8" cy="10" r="1.6" fill="currentColor"/><circle cx="12" cy="7.5" r="1.6" fill="currentColor"/><circle cx="16" cy="10" r="1.6" fill="currentColor"/><path d="M12 21a3 3 0 0 1 0-6h1.5a2 2 0 0 0 0-4"/>',
    "contrast": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18a9 9 0 0 0 0-18Z" fill="currentColor"/>',
    "type": '<path d="M4 7V5h11v2M9.5 5v14M7 19h5"/><path d="M14 12v-1.5h7V12M17.5 10.5V19M16 19h3"/>',
    "space": '<path d="M4 4v16M20 4v16"/><path d="M8 12h8M8 12l2.5-2.5M8 12l2.5 2.5M16 12l-2.5-2.5M16 12l-2.5 2.5"/>',
    "grid": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M8 4v16M12 4v16M16 4v16"/>',
    "names": '<path d="M5 7h10M5 12h14M5 17h7"/><path d="m16 16 2 2 4-4"/>',
    "backlog": '<rect x="4" y="4" width="16" height="4" rx="1"/><rect x="4" y="10" width="12" height="4" rx="1"/><rect x="4" y="16" width="8" height="4" rx="1"/>',
    "kit": '<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 17v3h16v-3"/>',
    "roi": '<path d="M4 20V10M10 20V6M16 20v-8M22 20H2"/><path d="m4 7 6-4 6 5 5-4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
}


def ico(n):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'


# ---------------------------------------------------------------- controls (shared by the panels)
def exp(key, formats=("css", "tailwind", "json", "scss")):
    lab = {"css": "CSS", "tailwind": "Tailwind", "json": "JSON (DTCG)", "scss": "SCSS", "csv": "CSV", "md": "Markdown", "txt": "Fixed list"}
    if key in ("names", "backlog", "roi"):
        lab["json"] = "JSON"
    seg_ = "".join(f'<button type="button" data-fmt="{f}" aria-pressed="{"true" if i == 0 else "false"}">{lab[f]}</button>' for i, f in enumerate(formats))
    return f'''<div class="lx-exp" data-exp="{key}">
      <div class="lx-exp-bar"><div class="lx-seg" role="group" aria-label="Export format">{seg_}</div>
        <div class="lx-exp-act"><button type="button" class="lx-btn" data-copy>Copy</button><button type="button" class="lx-btn" data-dl>Download</button></div></div>
      <pre class="lx-code" tabindex="0" aria-label="Exported code"><code></code></pre>
    </div>'''


def field(label, inner, hint=""):
    return f'<label class="lx-f"><span class="lx-l">{label}{f"<em>{hint}</em>" if hint else ""}</span>{inner}</label>'


def rng(name, lo, hi, step, val, label, unit=""):
    return f'<label class="lx-f"><span class="lx-l">{label}<output data-out="{name}"></output>{unit and f"<i>{unit}</i>"}</span><input type="range" name="{name}" min="{lo}" max="{hi}" step="{step}" value="{val}"></label>'


def num(name, label, lo, hi, step=1, hint=""):
    return f'<label class="lx-f"><span class="lx-l">{label}{f"<em>{hint}</em>" if hint else ""}</span><input type="number" inputmode="decimal" name="{name}" min="{lo}" max="{hi}" step="{step}"></label>'


def sel(name, opts, label):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<label class="lx-f"><span class="lx-l">{label}</span><select name="{name}">{o}</select></label>'


def seg(name, opts, label):
    b = "".join(f'<button type="button" data-v="{v}" aria-pressed="false">{t}</button>' for v, t in opts)
    return f'<div class="lx-f"><span class="lx-l">{label}</span><div class="lx-seg" data-name="{name}" role="group" aria-label="{label}">{b}</div></div>'


RATIOS = [("1.067", "1.067 · Minor second"), ("1.125", "1.125 · Major second"), ("1.2", "1.2 · Minor third"), ("1.25", "1.25 · Major third"),
          ("1.333", "1.333 · Perfect fourth"), ("1.414", "1.414 · Augmented fourth"), ("1.5", "1.5 · Perfect fifth"), ("1.618", "1.618 · Golden ratio")]

# ---------------------------------------------------------------- panels (the playgrounds)
P_PALETTE = f'''
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
    <p class="lx-hint">Select a swatch to copy its value. Badges show WCAG 2 contrast with white (W) and black (B) text; struck-through values fail 3:1.</p>
    <div class="lx-prev" data-prev>
      <div class="lx-prev-h"><b>Your palette on a real screen</b><div class="lx-seg" data-prev-mode role="group" aria-label="Preview theme"><button type="button" data-v="both" aria-pressed="true">Light and dark</button><button type="button" data-v="light" aria-pressed="false">Light</button><button type="button" data-v="dark" aria-pressed="false">Dark</button></div></div>
      <div class="lx-prev-grid" data-prev-grid></div>
    </div>
    {exp("palette")}
  </div>
</div>'''

CVD = '''<svg class="lx-defs" aria-hidden="true" focusable="false"><defs>
  <filter id="cvd-protanopia" color-interpolation-filters="linearRGB"><feColorMatrix type="matrix" values="0.152286 1.052583 -0.204868 0 0  0.114503 0.786281 0.099216 0 0  -0.003882 -0.048116 1.051998 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-deuteranopia" color-interpolation-filters="linearRGB"><feColorMatrix type="matrix" values="0.367322 0.860646 -0.227968 0 0  0.280085 0.672501 0.047413 0 0  -0.011820 0.042940 0.968881 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-tritanopia" color-interpolation-filters="linearRGB"><feColorMatrix type="matrix" values="1.255528 -0.076749 -0.178779 0 0  -0.078411 0.930809 0.147602 0 0  0.004733 0.691367 0.303900 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-achromatopsia" color-interpolation-filters="linearRGB"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"/></filter>
</defs></svg>'''

P_CONTRAST = f'''{CVD}
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Contrast settings">
    <div class="lx-card">
      <div class="lx-card-h"><b>Colours</b><button type="button" class="lx-btn lx-btn--sm" data-swap>⇅ Swap</button></div>
      <div class="lx-f"><span class="lx-l">Text</span><div class="lx-hex"><input type="color" name="fgc" aria-label="Pick the text colour"><input type="text" name="fg" maxlength="7" spellcheck="false" aria-label="Text hex"></div></div>
      <div class="lx-f"><span class="lx-l">Background</span><div class="lx-hex"><input type="color" name="bgc" aria-label="Pick the background colour"><input type="text" name="bg" maxlength="7" spellcheck="false" aria-label="Background hex"></div></div>
      <div class="lx-f"><span class="lx-l">From your palette <em>click for text, shift-click for background</em></span><div class="lx-mini" data-mini></div></div>
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Colour vision</b></div>
      {seg("vision", [("none", "Typical"), ("protanopia", "Protanopia"), ("deuteranopia", "Deuteranopia"), ("tritanopia", "Tritanopia"), ("achromatopsia", "No colour")], "Simulate the preview as seen with")}
      <p class="lx-hint" data-vision-note hidden>An approximate simulation (Machado et al., 2009). Contrast ratios don't change; whether colours can still be told apart does.</p>
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
    <p class="lx-hint">Every passing pair in a ramp. Rows are text, columns are backgrounds. Select a cell to load it above.</p>
  </div>
</div>'''

P_TYPE = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Type scale settings">
    <div class="lx-card"><div class="lx-card-h"><b>Scale</b></div>
      {rng("tbase", 12, 20, 1, 16, "Base size", "px")}
      {sel("tratio", RATIOS, "Ratio")}
      {rng("tup", 3, 9, 1, 6, "Steps above base")}
      {rng("tdown", 0, 3, 1, 2, "Steps below base")}
      {seg("tround", [("1", "Whole px"), ("2", "Even px"), ("4", "4px grid"), ("0", "Exact")], "Rounding")}
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Fluid sizes</b></div>
      <label class="lx-check"><input type="checkbox" name="tfluid"><span>Grow sizes with the screen, using CSS <code>clamp()</code></span></label>
      <div class="lx-fluid" data-fluid hidden>
        {rng("tbmin", 12, 20, 1, 15, "Base on small screens", "px")}
        {sel("trmin", RATIOS, "Ratio on small screens")}
        {rng("tvmin", 320, 480, 10, 360, "Small screen width", "px")}
        {rng("tvmax", 1024, 1920, 16, 1440, "Large screen width", "px")}
        {rng("tvw", 320, 1920, 10, 1440, "Preview at", "px")}
      </div>
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

P_SPACE = f'''
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

P_GRID = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Grid settings">
    <div class="lx-card"><div class="lx-card-h"><b>Start from</b></div>
      {seg("gpreset", [("m3", "Material 3"), ("bootstrap", "Bootstrap 5"), ("carbon", "Carbon"), ("product", "Product UI"), ("custom", "Custom")], "Breakpoint set")}
      <p class="lx-hint">Edit any value in the table and the set becomes your own.</p>
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Preview</b></div>
      {rng("gvw", 320, 1920, 10, 1280, "Screen width", "px")}
      <p class="lx-hint">Drag to see where the layout changes and how wide a column gets.</p>
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-gfacts" data-gfacts aria-live="polite"></div>
    <div class="lx-gview" data-gview></div>
    <div class="lx-card"><div class="lx-card-h"><b>Breakpoints</b><button type="button" class="lx-btn lx-btn--sm" data-gadd>+ Add breakpoint</button></div>
      <div class="lx-gtable" data-gtable></div>
      <p class="lx-hint">Max width 0 means the container fills the screen. Column at start is the column width at each breakpoint's smallest screen.</p>
    </div>
    {exp("grid")}
  </div>
</div>'''

P_NAMES = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="Linter settings">
    <div class="lx-card"><div class="lx-card-h"><b>Your convention</b></div>
      {seg("nsep", [("-", "kebab-case"), (".", "dot.case"), ("/", "slash/case")], "Separator")}
      {field("Categories", '<input type="text" name="ncats" spellcheck="false" value="color, space, size, radius, font, line-height, shadow, border, opacity, motion, z">', "first word")}
      {field("States", '<input type="text" name="nstates" spellcheck="false" value="hover, active, pressed, focus, focused, disabled, selected">', "always last")}
      {rng("ndepth", 3, 8, 1, 6, "Most parts allowed")}
      <label class="lx-check"><input type="checkbox" name="nraw" checked><span>Flag raw colour names in semantic tokens</span></label>
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-names">
      <div class="lx-card lx-names-in"><div class="lx-card-h"><b>Your tokens</b><div class="lx-btns"><button type="button" class="lx-btn lx-btn--sm" data-nexample>Load the messy example</button><button type="button" class="lx-btn lx-btn--sm" data-nclear>Clear</button></div></div>
        <textarea name="nlist" rows="14" spellcheck="false" aria-label="Token names, one per line" placeholder="Paste token names, CSS variables or a JSON token file&#10;--color-action-primary&#10;color.text.muted"></textarea>
        <p class="lx-hint" data-nparse></p></div>
      <div class="lx-card lx-names-out"><div class="lx-card-h"><b>Report</b><span class="lx-score" data-nscore></span></div>
        <div class="lx-nsum" data-nsum></div><ul class="lx-nlist" data-nresult></ul></div>
    </div>
    {exp("names", ("txt", "json"))}
  </div>
</div>'''

P_BACKLOG = f'''
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
    <div class="lx-card"><div class="lx-card-h"><b>Backlog, ranked</b><div class="lx-btns"><button type="button" class="lx-btn lx-btn--sm" data-bexample>Add examples</button><button type="button" class="lx-btn lx-btn--sm" data-bclear>Clear all</button></div></div>
      <div class="lx-bstats" data-bstats></div>
      <ol class="lx-blist" data-blist></ol>
      <p class="lx-hint">Any “✕” answer rules a request out. 55+ is high, 40–54 medium, below 40 deferred.</p>
    </div>
    {exp("backlog", ("md", "csv", "json"))}
  </div>
</div>'''

P_KIT = f'''
<div class="lx-ws lx-ws--one">
  <div class="lx-out">
    <div class="lx-kit" data-kit></div>
    <div class="lx-f lx-prefix"><span class="lx-l">Prefix <em>optional, e.g. acme</em></span><input type="text" name="kprefix" maxlength="16" spellcheck="false"></div>
    {exp("kit")}
  </div>
</div>'''

P_ROI = f'''
<div class="lx-ws">
  <aside class="lx-ctl" aria-label="ROI inputs">
    <div class="lx-card"><div class="lx-card-h"><b>Your teams</b></div>
      <div class="lx-2">{num("reng", "Engineers", 0, 100000)}{num("rdes", "Designers", 0, 100000)}</div>
      {rng("ruiEng", 5, 60, 5, 25, "Engineers' time on UI")}
      {rng("ruiDes", 10, 90, 5, 50, "Designers' time on UI")}
      {num("rhours", "Working hours a year, per person", 800, 2400, 10)}
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>The system</b></div>
      <div class="lx-2">{num("rfte", "System team (FTE)", 0, 500, 0.5)}{num("rmonthly", "Cost per FTE a month", 0, 1000000, 100)}</div>
      {num("rrate", "Blended cost of an hour", 0, 10000, 1)}
      {seg("rcur", [("$", "$"), ("€", "€"), ("£", "£"), ("₹", "₹")], "Currency")}
    </div>
    <div class="lx-card"><div class="lx-card-h"><b>Assumptions</b></div>
      {rng("rgain", 5, 40, 1, 20, "Time saved on UI work")}
      {rng("ra1", 0, 100, 5, 40, "Adoption, year 1")}
      {rng("ra2", 0, 100, 5, 70, "Adoption, year 2")}
      {rng("ra3", 0, 100, 5, 85, "Adoption, year 3")}
    </div>
  </aside>
  <div class="lx-out">
    <div class="lx-roi" data-roi aria-live="polite"></div>
    {exp("roi", ("md", "csv", "json"))}
  </div>
</div>'''


# ---------------------------------------------------------------- the catalogue
TASKS = [
    ("colour", "Choose colours", "Palettes and themes from one brand colour"),
    ("access", "Check accessibility", "Contrast, colour vision and readable text"),
    ("type", "Set type and spacing", "Scales engineers can build as written"),
    ("layout", "Lay out screens", "Columns, gutters, margins and breakpoints"),
    ("tokens", "Name and export tokens", "Clean names; CSS, Tailwind, SCSS, DTCG JSON"),
    ("plan", "Plan and make the case", "Rank requests and estimate the return"),
]
TASK = {k: (n, d) for k, n, d in TASKS}


def faq(*qa):
    return list(qa)


TOOLS = [
    dict(key="palette", short="Palette", slug="oklch-palette-generator", name="Palette generator", tasks=["colour", "access"], panel=P_PALETTE,
         kw="color palette generator colour scheme oklch ramp shades tints tailwind colors brand color scale dark mode theme accessible palette 50 900 hex p3",
         title="OKLCH Color Palette Generator for Design Systems",
         desc="Turn one brand colour into even, accessible OKLCH colour ramps. Preview them on a real UI in light and dark, then export CSS, Tailwind or DTCG tokens.",
         h1="OKLCH colour palette generator",
         lede="Start from your brand colour and get full ramps (50 to 900) with even steps, contrast badges on every swatch, and a live interface in light and dark mode. Export tokens you can paste.",
         outcome="Brand colour in, full accessible ramps out",
         gets=["Ramps of 10, 11 or 12 steps for brand, neutral and status colours", "Your exact brand colour kept at its closest step", "WCAG contrast on every swatch, with white and black text", "A live card in light and dark mode built from the ramps", "CSS variables, Tailwind colours, SCSS or DTCG JSON; Display P3 if you want it"],
         steps=[("Paste your brand colour", "Type or pick a hex. The tool finds the step where it belongs and builds the ramp around it."),
                ("Add the ramps you need", "A neutral tinted from your brand, plus success, warning, danger and info."),
                ("Check it on a screen", "Switch the preview between light and dark, then export or carry on to the contrast checker.")],
         presets=[("Indigo SaaS", {"ramps": [{"name": "brand", "h": 279, "c": 0.25, "hex": "#4736fe", "pin": True}, {"name": "neutral", "h": 279, "c": 0.014, "hex": None, "pin": False}], "sel": 0}),
                  ("Fintech teal", {"ramps": [{"name": "brand", "h": 182, "c": 0.12, "hex": "#0f766e", "pin": True}, {"name": "neutral", "h": 200, "c": 0.012, "hex": None, "pin": False}, {"name": "danger", "h": 25, "c": 0.2, "hex": None, "pin": False}], "sel": 0}),
                  ("Commerce orange", {"ramps": [{"name": "brand", "h": 45, "c": 0.2, "hex": "#ea580c", "pin": True}, {"name": "neutral", "h": 60, "c": 0.01, "hex": None, "pin": False}, {"name": "success", "h": 152, "c": 0.16, "hex": None, "pin": False}], "sel": 0}),
                  ("Health green", {"ramps": [{"name": "brand", "h": 150, "c": 0.17, "hex": "#16a34a", "pin": True}, {"name": "neutral", "h": 150, "c": 0.01, "hex": None, "pin": False}, {"name": "info", "h": 245, "c": 0.14, "hex": None, "pin": False}], "sel": 0}),
                  ("Full status set", {"ramps": [{"name": "brand", "h": 279, "c": 0.25, "hex": "#4736fe", "pin": True}, {"name": "neutral", "h": 279, "c": 0.014, "hex": None, "pin": False}, {"name": "success", "h": 152, "c": 0.16, "hex": None, "pin": False}, {"name": "warning", "h": 70, "c": 0.16, "hex": None, "pin": False}, {"name": "danger", "h": 25, "c": 0.2, "hex": None, "pin": False}, {"name": "info", "h": 245, "c": 0.14, "hex": None, "pin": False}], "sel": 0})],
         guide=f'''<h2>Why OKLCH instead of HSL</h2>
<p>In HSL, "50% lightness" doesn't look equally light across hues: yellow at 50% is far brighter than blue at 50%. Ramps built in HSL end up with uneven steps, and contrast changes unpredictably from one colour to the next. OKLCH is designed so that equal changes in lightness look like equal changes to people, so a 500 in blue and a 500 in green behave alike.</p>
<div class="lx-tbl"><table><thead><tr><th>What you want</th><th>In HSL</th><th>In OKLCH</th></tr></thead><tbody>
<tr><td>Even steps from 50 to 900</td><td>Hand-tuned per hue</td><td>One lightness curve for every hue</td></tr>
<tr><td>Predictable text contrast</td><td>Varies by hue</td><td>Similar at the same step</td></tr>
<tr><td>A new status colour</td><td>Re-tune the whole ramp</td><td>Change the hue; the curve stays</td></tr>
<tr><td>Wide-gamut screens</td><td>sRGB only</td><td>Display P3 where supported</td></tr>
</tbody></table></div>
<h2>How the ramps are built</h2>
<p>Every ramp shares one lightness curve, from your lightest to your darkest setting, so the same step has about the same lightness in every hue. Chroma (colourfulness) peaks in the middle of the ramp and tapers at both ends, then each colour is fitted into the sRGB or P3 gamut without changing its lightness. If you paste a brand colour, it's pinned to the step with the closest lightness, so your exact hex appears in the system.</p>
<h2>Using the ramps in a design system</h2>
<p>Ramps are <b>primitive tokens</b>: raw values with neutral names like <code>color-brand-600</code>. Product code shouldn't use them directly. Map them to <b>semantic tokens</b> that name a job (<code>color-action-primary</code> → <code>brand-600</code>), so dark mode and rebrands become a change of mapping, not a hunt through every screen.</p>''',
         faq=faq(("What is an OKLCH colour palette?", "A set of colour ramps defined in OKLCH, a colour space where lightness matches how bright colours look to people. It gives evenly spaced steps and more predictable contrast than HSL."),
                 ("Will my exact brand colour be in the palette?", "Yes, if you keep “Keep my exact colour at the closest step” on. Your hex replaces the generated colour at the step with the closest lightness."),
                 ("Can I use the palette with Tailwind?", "Yes. Export as Tailwind to get a colours object for tailwind.config.js, or as CSS variables you can reference from a Tailwind v4 theme."),
                 ("What is Display P3?", "A wider colour gamut supported by most modern phones and laptops. Choosing P3 adds oklch() values for those screens, with the sRGB hex as a fallback."),
                 ("Is it free?", "Yes. It runs entirely in your browser, needs no account, and saves your work locally.")),
         related=["contrast", "kit", "type"], articles=["oklch-color-palette", "dark-mode-design-tokens", "color-contrast-design-system"],
         next=("contrast", "Check these colours for contrast")),

    dict(key="contrast", short="Contrast", slug="color-contrast-checker", name="Contrast checker", tasks=["access", "colour"], panel=P_CONTRAST,
         kw="color contrast checker colour contrast ratio wcag aa aaa apca accessibility a11y text background readable legibility color blind blindness simulator protanopia deuteranopia tritanopia fix failing",
         title="Color Contrast Checker: WCAG 2, APCA and Fixes",
         desc="Check text and background colours against WCAG 2 and APCA, get the closest passing colour in the same hue, and preview them as seen with colour blindness.",
         h1="Colour contrast checker with WCAG, APCA and fixes",
         lede="Check any text and background pair against WCAG 2 AA and AAA and the newer APCA method. If it fails, get the nearest colour that passes, in the same hue, and see how the pair looks with common types of colour blindness.",
         outcome="Check a pair, get the nearest colour that passes",
         gets=["The WCAG 2 contrast ratio and an APCA Lc value", "Pass or fail for AA and AAA, body text, large text and UI parts", "The closest passing text or background colour, keeping your hue", "A preview simulating protanopia, deuteranopia, tritanopia and no colour vision", "A matrix of every passing pair in your palette"],
         steps=[("Enter two colours", "Paste hex values for text and background, or click swatches from your palette."),
                ("Read the verdict", "See the ratio, the APCA value and which WCAG levels pass, on real text sizes."),
                ("Fix what fails", "Apply the nearest passing colour with one click, then check the preview with colour blindness simulated.")],
         presets=[("Grey placeholder text", {"fg": "#9aa0aa", "bg": "#ffffff"}), ("Brand button label", {"fg": "#ffffff", "bg": "#ff6b3d"}),
                  ("Muted text on dark", {"fg": "#6b7280", "bg": "#13161d"}), ("Link on a tinted panel", {"fg": "#4f46e5", "bg": "#e0e7ff"}),
                  ("Red and green status", {"fg": "#16a34a", "bg": "#dc2626", "vision": "deuteranopia"})],
         guide='''<h2>What the numbers mean</h2>
<div class="lx-tbl"><table><thead><tr><th>Level</th><th>Ratio</th><th>Applies to</th></tr></thead><tbody>
<tr><td>AA</td><td>4.5:1</td><td>Body text and anything smaller than large text</td></tr>
<tr><td>AA, large text</td><td>3:1</td><td>Text at least 24px, or 18.66px bold</td></tr>
<tr><td>AA, non-text</td><td>3:1</td><td>Icons, input borders, focus rings and other UI parts (WCAG 1.4.11)</td></tr>
<tr><td>AAA</td><td>7:1</td><td>Body text, for the enhanced level</td></tr>
<tr><td>AAA, large text</td><td>4.5:1</td><td>Large text, for the enhanced level</td></tr>
</tbody></table></div>
<p>WCAG 2's ratio is the legal and procurement standard today. APCA, developed for the next generation of WCAG, models how contrast is perceived more closely: it treats dark text on light differently from light text on dark, and takes text size and weight into account. We show both. Use WCAG 2 to meet requirements and APCA as a second opinion, especially for dark mode and thin text.</p>
<h2>How the fixes are found</h2>
<p>When a pair fails, the checker keeps the colour's hue and chroma in OKLCH and moves only its lightness, a step at a time, until the pair passes. That gives the smallest visible change that meets the target, in the same family as your original colour. It suggests fixes for the text and the background separately, for AA and for AAA.</p>
<h2>Contrast isn't the whole story</h2>
<p>About 1 in 12 men and 1 in 200 women have some form of colour vision deficiency. Two colours can pass contrast and still be hard to tell apart, like a red error and a green success state. Use the colour vision simulation to check, and never rely on colour alone: add an icon, a label or a pattern.</p>''',
         faq=faq(("What contrast ratio do I need for WCAG AA?", "4.5:1 for normal text, 3:1 for large text (24px, or 18.66px bold) and 3:1 for icons and UI parts like input borders."),
                 ("What is APCA?", "The Accessible Perceptual Contrast Algorithm, developed for future versions of WCAG. It gives an Lc value that accounts for polarity, text size and weight. It isn't a legal requirement yet."),
                 ("How do I fix a colour that fails?", "Use the suggested fix: it keeps your hue and changes only the lightness to the nearest value that passes."),
                 ("How accurate is the colour blindness simulation?", "It's an approximation based on Machado et al. (2009), applied to the preview. It's good for spotting colours that become hard to tell apart, not for exact appearance."),
                 ("Does it check my whole palette?", "Yes. The pair matrix shows every text and background combination in a ramp that passes the level you choose.")),
         related=["palette", "type", "names"], articles=["color-contrast-design-system", "oklch-color-palette", "dark-mode-design-tokens"],
         next=("type", "Set up a type scale")),

    dict(key="type", short="Type scale", slug="type-scale-generator", name="Type scale generator", tasks=["type"], panel=P_TYPE,
         kw="type scale generator typography modular scale font size calculator fluid typography clamp calculator responsive font sizes line height letter spacing typescale heading sizes",
         title="Type Scale Generator with Fluid clamp() Sizes",
         desc="Make a modular type scale from a base size and ratio, rounded the way engineers build it, with line heights, fluid clamp() sizes and token export.",
         h1="Type scale generator, with fluid sizes",
         lede="Pick a base size and a ratio and get a full type scale: sizes rounded to whole pixels, line heights that tighten as text grows, and token names. Turn on fluid sizes to get CSS clamp() values that grow with the screen.",
         outcome="Font sizes, line heights and clamp() values",
         gets=["A modular scale from 8 musical ratios, from 3 to 12 steps", "Sizes rounded to whole, even or 4px values, in px and rem", "Line heights and letter spacing per size", "Fluid sizes with clamp(), and a warning where zoom could suffer", "CSS, Tailwind, SCSS or DTCG JSON"],
         steps=[("Choose a base and ratio", "16px with 1.2 suits most product UI; larger ratios suit marketing and editorial pages."),
                ("Tune lines and rounding", "Keep sizes on whole pixels and line heights on even numbers, so design and code match."),
                ("Go fluid if you need to", "Set a smaller base and ratio for phones; the export becomes clamp() values between the two screens.")],
         presets=[("Product UI", {"t": {"base": 16, "ratio": "1.2", "up": 6, "down": 2, "fluid": False}}), ("Dense dashboard", {"t": {"base": 14, "ratio": "1.125", "up": 5, "down": 2, "fluid": False}}),
                  ("Marketing site, fluid", {"t": {"base": 18, "ratio": "1.333", "up": 6, "down": 1, "fluid": True, "bmin": 16, "rmin": "1.2", "vmin": 360, "vmax": 1440, "vw": 1440}}),
                  ("Editorial", {"t": {"base": 18, "ratio": "1.25", "up": 5, "down": 2, "fluid": False, "lh": 1.6}})],
         guide='''<h2>Choosing a ratio</h2>
<div class="lx-tbl"><table><thead><tr><th>Ratio</th><th>Feels like</th><th>Good for</th></tr></thead><tbody>
<tr><td>1.125 · Major second</td><td>Calm, compact</td><td>Dense dashboards and data tools</td></tr>
<tr><td>1.2 · Minor third</td><td>Clear hierarchy without shouting</td><td>Most product UI</td></tr>
<tr><td>1.25 · Major third</td><td>Confident</td><td>Apps with marketing pages; documentation</td></tr>
<tr><td>1.333 · Perfect fourth</td><td>Expressive</td><td>Marketing sites, editorial</td></tr>
<tr><td>1.5 and up</td><td>Dramatic</td><td>Landing pages with few levels</td></tr>
</tbody></table></div>
<p>A ratio is a starting point, not a law. Most teams round the results and adjust one or two sizes by eye. What matters is that the sizes are named, shared and used everywhere.</p>
<h2>Fluid sizes with clamp()</h2>
<p>Fluid type lets headings grow smoothly between a small and a large screen instead of jumping at breakpoints. Each size becomes <code>clamp(min, preferred, max)</code>: a minimum for phones, a maximum for large screens, and a preferred value in <code>rem + vw</code> between them. Using <code>rem</code> in the middle keeps text responsive to the reader's font-size setting.</p>
<p>One caution: if the largest size is more than about 2.5 times the smallest, browser zoom may not be able to double the text, which WCAG 1.4.4 asks for. The scale flags those sizes with “zoom”.</p>''',
         faq=faq(("What is a modular type scale?", "A set of font sizes where each size is the previous one multiplied by the same ratio, like 1.25. It gives a consistent rhythm between body text and headings."),
                 ("What base font size should I use?", "16px for most product UI, since it's the browser default and readable on every screen. 14px can suit dense tools; 18px suits reading-heavy sites."),
                 ("How do I make fluid typography with clamp()?", "Turn on fluid sizes, set the base and ratio for small screens and the screen widths to grow between. The CSS export gives a clamp() value for every size."),
                 ("Should line height be unitless?", "For fluid sizes, yes: the export uses unitless line heights so they scale with the text. Fixed scales export line heights on an even pixel grid."),
                 ("Can I use it with Tailwind?", "Yes. The Tailwind export gives a fontSize object with sizes, line heights and letter spacing.")),
         related=["space", "grid", "kit"], articles=["type-scale-design-system", "spacing-system-4px-vs-8px", "layout-grid-breakpoints"],
         next=("space", "Set up spacing and radius")),

    dict(key="space", short="Spacing", slug="spacing-scale-generator", name="Spacing scale generator", tasks=["type", "layout"], panel=P_SPACE,
         kw="spacing scale generator spacing system 4px 8px grid spacing tokens padding margin gap border radius scale corner radius",
         title="Spacing Scale Generator: 4px or 8px Tokens",
         desc="Build a spacing scale on a 2, 4 or 8px base, try it on a real card, add a radius scale, and export spacing tokens for CSS, Tailwind, SCSS or JSON.",
         h1="Spacing scale generator, with radius",
         lede="Build a spacing scale on a 4px or 8px base, see every step, and try it on a real card before you commit. Add a short radius scale and export both as tokens.",
         outcome="A spacing and radius scale, tried on a card",
         gets=["A spacing scale from four methods: common, linear, doubling or Fibonacci", "Token names in t-shirt sizes, multiples or pixel values", "A live card to try padding and gaps from the scale", "A radius scale, with an optional full radius for pills", "CSS, Tailwind, SCSS or DTCG JSON"],
         steps=[("Pick a base unit", "4px gives fine control for product UI; 8px gives fewer, clearer choices."),
                ("Choose how it grows", "The common method adds the in-between values teams actually use, like 12 and 20."),
                ("Try it on the card", "Change padding and gap from the scale, then export spacing and radius together.")],
         presets=[("4px, common", {"s": {"base": "4", "method": "common", "count": 12, "name": "shirt", "pad": "", "gap": ""}}), ("8px, doubling", {"s": {"base": "8", "method": "double", "count": 8, "name": "shirt", "pad": "", "gap": ""}}),
                  ("Dense data UI", {"s": {"base": "2", "method": "common", "count": 14, "name": "px", "pad": "", "gap": ""}, "r": {"base": 4, "count": 4, "full": True}}),
                  ("Soft and round", {"r": {"base": 10, "count": 5, "full": True}})],
         guide='''<h2>4px or 8px?</h2>
<p>An 8px base gives fewer, more distinct choices and suits marketing pages and simple apps. A 4px base adds the half-steps (4, 12, 20) that dense product UI needs for icons, tight lists and form controls. Many systems use a 4px base with a scale that mostly lands on multiples of 8.</p>
<div class="lx-tbl"><table><thead><tr><th>Method</th><th>Values on a 4px base</th><th>Good for</th></tr></thead><tbody>
<tr><td>Common</td><td>2, 4, 8, 12, 16, 20, 24, 32, 40, 48…</td><td>Most product UI</td></tr>
<tr><td>Linear</td><td>4, 8, 12, 16, 20, 24…</td><td>Small, even steps</td></tr>
<tr><td>Doubling</td><td>4, 8, 16, 32, 64…</td><td>Layouts with few levels</td></tr>
<tr><td>Fibonacci</td><td>4, 8, 12, 20, 32, 52…</td><td>Expressive, editorial layouts</td></tr>
</tbody></table></div>
<h2>Naming spacing tokens</h2>
<p>T-shirt names (<code>space-sm</code>, <code>space-md</code>) are easy to read but hard to extend between steps. Multiples (<code>space-4</code> for 16px on a 4px base) are easy to extend and to reason about. Pixel names (<code>space-16</code>) are the most literal. Pick one and use it everywhere; the scale matters more than the naming.</p>''',
         faq=faq(("Should I use a 4px or 8px spacing system?", "4px for dense product UI that needs half-steps like 12px and 20px; 8px for simpler layouts. A 4px base with mostly 8px multiples gives both."),
                 ("How many spacing tokens do I need?", "Usually 10 to 14. Fewer than that and teams invent values; many more and the differences stop being visible."),
                 ("Should spacing use px or rem?", "The export uses rem, so spacing scales with the reader's font-size setting, with the pixel value noted beside each token."),
                 ("What radius scale should I use?", "Four or five steps, plus a full radius for pills and avatars, is enough for most products.")),
         related=["type", "grid", "kit"], articles=["spacing-system-4px-vs-8px", "layout-grid-breakpoints", "design-tokens"],
         next=("grid", "Set up a layout grid")),

    dict(key="grid", short="Grid", slug="layout-grid-calculator", name="Layout grid calculator", tasks=["layout"], panel=P_GRID, new=True,
         kw="grid calculator layout grid column width calculator gutter margin breakpoints responsive breakpoints css grid 12 column bootstrap material carbon container width",
         title="Layout Grid Calculator: Columns and Breakpoints",
         desc="Plan a responsive layout grid: columns, gutters, margins and breakpoints, with a live preview at any screen width and CSS, SCSS, Tailwind or token export.",
         h1="Layout grid calculator for responsive breakpoints",
         lede="Set columns, gutters, margins and breakpoints, then drag the screen width to see exactly where your layout changes and how wide a column gets. Start from Material 3, Bootstrap 5 or Carbon, and export the grid as CSS or tokens.",
         outcome="Columns, gutters and breakpoints, previewed",
         gets=["Breakpoints with columns, gutter, margin and maximum width for each", "A live preview at any screen width, with column width worked out", "A warning when columns get too narrow", "Starting points from Material 3, Bootstrap 5 and Carbon", "CSS custom properties and a .grid class, SCSS, Tailwind screens or DTCG JSON"],
         steps=[("Start from a familiar set", "Pick Material 3, Bootstrap 5, Carbon or our product UI starting point."),
                ("Drag the screen width", "Watch the active breakpoint, column width and content width change as you go."),
                ("Make it yours and export", "Edit any value in the table, add or remove breakpoints, then copy the CSS or tokens.")],
         presets=[("Material 3", {"g": {"preset": "m3", "bps": None}}), ("Bootstrap 5", {"g": {"preset": "bootstrap", "bps": None}}), ("Carbon 2x Grid", {"g": {"preset": "carbon", "bps": None}}),
                  ("Product UI", {"g": {"preset": "product", "bps": None}}), ("Check a phone", {"g": {"vw": 390}}), ("Check a laptop", {"g": {"vw": 1440}})],
         guide='''<h2>How the column width is worked out</h2>
<p>At any screen width, the container is the screen (or the maximum width, if smaller). Take away the two margins to get the content width, take away the gutters between columns, and divide by the number of columns:</p>
<p class="lx-formula"><code>column = (min(screen, max width) − 2 × margin − (columns − 1) × gutter) ÷ columns</code></p>
<p>When columns get narrower than about 40px, a 12-column grid stops being useful on that screen: use fewer columns at that breakpoint.</p>
<h2>About the starting points</h2>
<div class="lx-tbl"><table><thead><tr><th>Set</th><th>Breakpoints</th><th>Notes</th></tr></thead><tbody>
<tr><td>Material 3</td><td>600, 840, 1200, 1600</td><td>Material 3's window size classes and margins. Material 3 describes panes and margins rather than a fixed column grid, so the 4, 8 and 12 columns here follow the common convention.</td></tr>
<tr><td>Bootstrap 5</td><td>576, 768, 992, 1200, 1400</td><td>12 columns, 24px gutters and fixed container widths from Bootstrap's defaults.</td></tr>
<tr><td>Carbon 2x Grid</td><td>672, 1056, 1312, 1584</td><td>IBM Carbon's breakpoints, with 16 columns on large screens and 32px gutters.</td></tr>
<tr><td>Product UI</td><td>600, 1024, 1440</td><td>Our starting point for business software: 4, 8 and 12 columns, full width up to 1440px.</td></tr>
</tbody></table></div>
<p>Check each system's own documentation before relying on exact values; frameworks change their defaults between versions.</p>
<h2>Breakpoints as tokens</h2>
<p>CSS custom properties can't be used inside media queries, so breakpoints are usually shared as constants (SCSS variables, a Tailwind <code>screens</code> object or JSON for your token pipeline), while columns, gutters and margins can be custom properties that change at each breakpoint. The CSS export does exactly that.</p>''',
         faq=faq(("How do I calculate column width?", "Subtract the two margins and all the gutters from the container width, then divide by the number of columns. The calculator does this at any screen width."),
                 ("What breakpoints should I use?", "Four or five, set where your layout needs to change. Material 3's 600, 840, 1200 and 1600 is a sound start. Name them by size, not device."),
                 ("How many columns should a grid have?", "4 on phones, 8 on tablets and 12 on laptops and desktops is the most common choice. Dense enterprise tools sometimes use 16."),
                 ("Can I export the grid for Tailwind?", "Yes. The Tailwind export gives a screens object with your breakpoints. The CSS export adds custom properties and a .grid class.")),
         related=["space", "type", "kit"], articles=["layout-grid-breakpoints", "spacing-system-4px-vs-8px", "design-system-localization-rtl"],
         next=("kit", "Export everything as one token file")),

    dict(key="names", short="Token names", slug="design-token-name-checker", name="Token name checker", tasks=["tokens"], panel=P_NAMES,
         kw="design token naming convention checker linter lint css variables naming token names validate design tokens naming rules kebab case",
         title="Design Token Name Checker and Linter",
         desc="Paste design token names, CSS variables or a JSON token file. Check them against a naming convention, see every problem explained and get a fixed list.",
         h1="Design token name checker",
         lede="Paste your token names, CSS variables or a JSON token file. The checker tests every name against a naming convention you can adjust, explains each problem in plain words, and gives you a fixed list to rename from.",
         outcome="Every naming problem explained, with a fix",
         gets=["A report on every token: clean, warning or error", "Plain explanations: wrong case, abbreviations, order, raw colours in semantic names", "A suggested fixed name for each problem", "Duplicates found once names are fixed", "A fixed list, or a JSON map of old to new names"],
         steps=[("Paste your tokens", "One per line, a CSS :root block or a DTCG JSON file. A messy example is loaded to start."),
                ("Set your convention", "Separator, category words, state words and how many parts a name can have."),
                ("Fix and export", "Copy the fixed list, or the rename map for a find-and-replace or a codemod.")],
         presets=[("The messy example", {"n": {"list": None}}),
                  ("Tailwind-style names", {"n": {"list": "--color-blue-500\n--color-primary\n--textBase\n--spacing-4\n--rounded-lg\n--shadow-md\n--color-btn-primary-hover\n--font-size-xl\n--z-50"}}),
                  ("A DTCG JSON file", {"n": {"sep": ".", "list": '{\n  "color": {\n    "action": { "primary": { "$value": "#4736fe" }, "Primary-Hover": { "$value": "#3e27b8" } },\n    "text": { "muted": { "$value": "#5b6170" }, "blue": { "$value": "#4f46e5" } }\n  },\n  "space": { "md": { "$value": "16px" } },\n  "bg": { "card": { "$value": "#ffffff" } }\n}'}})],
         guide='''<h2>The convention it checks</h2>
<p>Good token names read from general to specific: <b>category</b> first (colour, space, font), then the <b>job</b> (action, text, surface), then a <b>variant</b> (primary, muted), with any <b>state</b> (hover, disabled) last. One separator, lowercase, no abbreviations.</p>
<p class="lx-formula"><code>color-action-primary-hover</code> = category · job · variant · state</p>
<div class="lx-tbl"><table><thead><tr><th>Problem</th><th>Example</th><th>Fixed</th></tr></thead><tbody>
<tr><td>Capitals or mixed case</td><td><code>--colorTextMuted</code></td><td><code>color-text-muted</code></td></tr>
<tr><td>Abbreviation</td><td><code>--btn-bg-primary</code></td><td><code>color-button-background-primary</code></td></tr>
<tr><td>Category not first</td><td><code>--primary-text-color</code></td><td><code>color-primary-text</code></td></tr>
<tr><td>State not last</td><td><code>--color-surface-hover-brand</code></td><td><code>color-surface-brand-hover</code></td></tr>
<tr><td>Raw colour in a semantic name</td><td><code>--color-button-blue</code></td><td>Name it for its job, like <code>color-action-primary</code></td></tr>
</tbody></table></div>
<p>The rules are adjustable: if your system uses dot.case or different category words, change them on the left and the whole report updates.</p>''',
         faq=faq(("What is a good naming convention for design tokens?", "Category, then the job, then a variant, with any state last, all lowercase with one separator: for example color-action-primary-hover."),
                 ("Can I check a JSON token file?", "Yes. Paste a DTCG or Tokens Studio style JSON file; the checker reads every token path."),
                 ("Does it rename my tokens for me?", "It gives you the fixed names and a JSON map from old to new, which you can use for a find-and-replace or a codemod."),
                 ("Why flag raw colours in semantic tokens?", "A semantic token like color-button-blue breaks the moment the button changes colour, for example in dark mode or a rebrand. Name it for its job instead.")),
         related=["kit", "palette", "backlog"], articles=["design-token-naming-conventions", "design-tokens", "figma-code-sync"],
         next=("kit", "Generate a full token set")),

    dict(key="kit", short="Token export", slug="design-token-generator", name="Design token generator", tasks=["tokens"], panel=P_KIT,
         kw="design token generator design tokens export css variables tailwind config scss dtcg json w3c tokens style dictionary figma variables token file",
         title="Design Token Generator: CSS, Tailwind, DTCG JSON",
         desc="Combine your palette, type scale, spacing, radius and grid into one design token file: CSS variables, a Tailwind config, SCSS or W3C DTCG JSON.",
         h1="Design token generator",
         lede="Everything you've made in the Lab, in one file: colour ramps, type scale, spacing, radius and layout grid, as CSS custom properties, a Tailwind config, SCSS variables or W3C DTCG JSON for your token pipeline.",
         outcome="One token file for CSS, Tailwind or DTCG",
         gets=["Colour, type, spacing, radius and grid tokens in one file", "CSS custom properties, with breakpoints as media queries", "A Tailwind config extending colours, font sizes, spacing, radius and screens", "SCSS variables and a breakpoint mixin", "DTCG JSON for Style Dictionary, Tokens Studio or Figma variables plugins"],
         steps=[("Make your foundations", "Use the palette, type, spacing and grid tools. Each one saves as you go."),
                ("Review them here", "Each card shows what's included. Select one to edit it in its own tool."),
                ("Add a prefix and export", "An optional prefix (acme-color-brand-500) avoids clashes; copy or download the file.")],
         presets=[],
         guide='''<h2>Which format should I use?</h2>
<div class="lx-tbl"><table><thead><tr><th>Format</th><th>Use it when</th></tr></thead><tbody>
<tr><td>CSS custom properties</td><td>You want tokens available in any stylesheet or framework, and themeable at runtime.</td></tr>
<tr><td>Tailwind</td><td>Your product uses Tailwind and you want the tokens as utility classes.</td></tr>
<tr><td>SCSS</td><td>Your codebase uses Sass and compiles values at build time.</td></tr>
<tr><td>DTCG JSON</td><td>You run a token pipeline (Style Dictionary, Tokens Studio, a Figma variables plugin). This is the vendor-neutral format from the W3C Design Tokens Community Group.</td></tr>
</tbody></table></div>
<h2>Primitive tokens first</h2>
<p>The file contains <b>primitive tokens</b>: the raw palette, sizes and steps. The next step in a design system is a layer of <b>semantic tokens</b> that name a job (<code>color-text-muted</code>, <code>space-inset-card</code>) and point at primitives. Product code uses the semantic layer, so themes and rebrands only change the mapping.</p>''',
         faq=faq(("What is a design token file?", "A file of named design decisions (colours, sizes, spacing) that code and design tools read from, so values are defined once and used everywhere."),
                 ("What is the DTCG format?", "The JSON format from the W3C Design Tokens Community Group. Tools like Style Dictionary and Tokens Studio read it, and plugins can turn it into Figma variables."),
                 ("Can I import tokens into Figma?", "Export DTCG JSON and use a Figma variables or tokens plugin that reads the format."),
                 ("Does the export include semantic tokens?", "No. It exports primitives. Map them to semantic tokens that name each job; see our guide to design tokens.")),
         related=["palette", "type", "names"], articles=["design-tokens", "design-token-naming-conventions", "figma-code-sync"],
         next=None),

    dict(key="backlog", short="Requests", slug="component-request-scorecard", name="Request scorecard", tasks=["plan"], panel=P_BACKLOG,
         kw="design system request prioritization component requests backlog prioritisation framework scorecard intake triage roadmap which component to build next",
         title="Design System Request Scorecard and Backlog",
         desc="Score design system component requests with four questions and get a ranked backlog you can share: the 70-point model from a real design system practice.",
         h1="Design system request scorecard",
         lede="Score every component request with the same four questions: where it's needed, who can reuse it, whether you have it already and how hard it is. Get a ranked backlog with clear verdicts you can share with teams.",
         outcome="Four questions, one ranked backlog",
         gets=["A 70-point score for each request, as you answer", "A verdict: build first, build after, defer, or won't fix", "A ranked backlog with the reasons visible", "Markdown for your docs, CSV for a spreadsheet, or JSON"],
         steps=[("Name the request", "What's being asked for, and by which team."),
                ("Answer four questions", "Each answer adds points; any answer that rules it out ends the scoring."),
                ("Share the ranking", "The backlog sorts itself. Export it for your planning or docs.")],
         presets=[],
         guide='''<h2>The four questions</h2>
<div class="lx-tbl"><table><thead><tr><th>Question</th><th>Points</th><th>Rules it out when…</th></tr></thead><tbody>
<tr><td>Where is it needed?</td><td>Main products 20 · smaller products 15 · one team 5</td><td>It's needed nowhere yet</td></tr>
<tr><td>How many teams can reuse it?</td><td>Many 20 · a few 15 · one 5</td><td>Only one product will ever use it</td></tr>
<tr><td>Do we already have it?</td><td>No 15 · partly 10 · mostly 5</td><td>It's already fully solved</td></tr>
<tr><td>How hard is it to build?</td><td>Under a week 15 · 1–3 weeks 10 · 3+ weeks 5</td><td>It isn't worth the effort</td></tr>
</tbody></table></div>
<p><b>55 or more</b> is high: the system team builds it first. <b>40 to 54</b> is medium: accept it after high-priority work, ideally as a contribution. <b>Below 40</b>, defer: the team builds it as a local component, which can be promoted later if a second team needs it.</p>
<p>The model comes from the <a href="/work/cars24-governance">CARS24 governance work</a>, where one front door and a shared scorecard let any team see why a request was ranked where it was.</p>''',
         faq=faq(("How do you prioritise design system requests?", "Score each one with the same questions: how widely it's needed, how many teams can reuse it, whether it exists already and how hard it is. Rank by score, and publish the reasons."),
                 ("What happens to low-scoring requests?", "They're deferred, and the requesting team builds a local component. If a second team needs it later, it can join the system."),
                 ("Can I change the scoring?", "Not in the tool yet, but the export gives you every answer, so you can re-weight in a spreadsheet.")),
         related=["roi", "names", "kit"], articles=["design-system-contribution-model", "which-components-to-build-first", "design-system-governance"],
         next=("roi", "Estimate the return on your system")),

    dict(key="roi", short="ROI", slug="design-system-roi-calculator", name="ROI calculator", tasks=["plan"], panel=P_ROI, new=True,
         kw="design system roi calculator return on investment business case cost savings value of a design system break even payback budget justify design system",
         title="Design System ROI Calculator: Payback and Value",
         desc="Estimate a design system's return over three years from your team size, system cost and adoption. See payback, sensitivity and the method behind it.",
         h1="Design system ROI calculator",
         lede="Estimate what a design system saves over three years from your own numbers: team sizes, the cost of the system team, how much faster UI work gets and how quickly teams adopt it. See when it pays back, and how much the answer depends on each assumption.",
         outcome="Three-year value, cost and payback",
         gets=["Hours saved, value, cost and net for years one to three", "The first profitable year, cumulative payback and the team size needed to break even", "A sensitivity table across time saved and adoption", "Every formula shown, nothing hidden", "Markdown for a business case, CSV or JSON"],
         steps=[("Enter your teams", "Engineers, designers, and how much of their time goes on UI work."),
                ("Enter the system's cost", "How many people run the system, and what they cost."),
                ("Test the assumptions", "Move time saved and adoption, and see which ones change the answer.")],
         presets=[("Playbook example", {"roi": {"eng": 40, "des": 6, "fte": 2, "monthly": 12000, "rate": 90, "gain": 20, "a1": 40, "a2": 70, "a3": 85, "uiEng": 25, "uiDes": 50, "hours": 1600, "cur": "$"}}),
                  ("Startup", {"roi": {"eng": 12, "des": 3, "fte": 0.5, "monthly": 12000, "rate": 90, "gain": 20, "a1": 50, "a2": 80, "a3": 90}}),
                  ("Enterprise", {"roi": {"eng": 300, "des": 50, "fte": 8, "monthly": 12000, "rate": 90, "gain": 20, "a1": 25, "a2": 50, "a3": 70}}),
                  ("Cautious case", {"roi": {"gain": 10, "a1": 30, "a2": 55, "a3": 70}})],
         guide='''<h2>The method</h2>
<p>The calculator counts only time saved, which is the part finance teams accept most easily. It leaves out quality, accessibility, brand consistency and the cost of change, so the result is a floor, not a ceiling.</p>
<div class="lx-tbl"><table><thead><tr><th>Step</th><th>Formula</th></tr></thead><tbody>
<tr><td>UI hours a year</td><td>(engineers × engineers' UI share + designers × designers' UI share) × hours a year</td></tr>
<tr><td>Hours saved</td><td>UI hours × time saved × adoption that year</td></tr>
<tr><td>Value</td><td>hours saved × blended hourly cost</td></tr>
<tr><td>Cost</td><td>system team FTE × monthly cost × 12</td></tr>
<tr><td>Break-even team size</td><td>cost ÷ value per engineer at 70% adoption</td></tr>
</tbody></table></div>
<h2>Choosing honest assumptions</h2>
<p>Published speed-ups are real but come from best-case tasks: Figma measured designers 34% faster on one task with a relevant system, and a study with IBM's Carbon found developers about 47% faster building one form. Across all of a team's UI work the gain is lower, which is why the default is 20%. Adoption is the other big lever: a system that only 40% of new work uses saves less than half as much as one at 90%.</p>
<p>The playbook example (40 engineers, 6 designers, a two-person system team) loses money in years one and two and turns a profit in year three, but on time savings alone it hasn't yet earned back the first two years by the end of year three. That's typical for a team of this size, and it's why design systems are best funded in stages, each earning the next, and why the other benefits belong in the business case too.</p>''',
         faq=faq(("How do you calculate the ROI of a design system?", "Estimate the hours spent on UI work, the share a system saves, and how much of the work uses the system each year. Multiply by the cost of an hour and compare with the cost of the team that runs the system."),
                 ("How long does a design system take to pay back?", "On time savings alone, a mid-sized product team often turns a yearly profit in year two or three and recovers the early losses later, because adoption ramps up slowly. Larger organisations pay back sooner."),
                 ("What time saving should I assume?", "Around 20% of UI work is a defensible default. Published figures like 34% or 47% come from single tasks and overstate the average."),
                 ("Does it include quality and accessibility benefits?", "No. It counts time saved only, so the result is a conservative floor. Mention the other benefits alongside it.")),
         related=["backlog", "palette", "kit"], articles=["design-system-roi", "design-system-metrics", "design-system-team-structure"],
         next=("backlog", "Prioritise what to build first")),
]
BY = {t["key"]: t for t in TOOLS}
ORDER = ["palette", "contrast", "type", "space", "grid", "names", "kit", "backlog", "roi"]
WRITING_TITLES = {}

JOBS = [
    ("Turn one brand colour into a full palette", "palette", "colour"), ("Make a palette that works in dark mode", "palette", "colour"),
    ("Get Tailwind colours from our brand colour", "palette", "colour"), ("Check if my text colour passes WCAG", "contrast", "access"),
    ("Fix a brand button that fails contrast", "contrast", "access"), ("See how my UI looks with colour blindness", "contrast", "access"),
    ("Compare WCAG 2 and APCA contrast", "contrast", "access"), ("Pick font sizes that work together", "type", "type"),
    ("Make headings grow with the screen using clamp()", "type", "type"), ("Set up spacing tokens on a 4px or 8px grid", "space", "type"),
    ("Choose columns, gutters and breakpoints", "grid", "layout"), ("Work out how wide a column is at any screen size", "grid", "layout"),
    ("Check our token names before we ship", "names", "tokens"), ("Export tokens as CSS, Tailwind or DTCG JSON", "kit", "tokens"),
    ("Get a token file for Style Dictionary or Figma variables", "kit", "tokens"), ("Decide which component to build next", "backlog", "plan"),
    ("Estimate what a design system will save", "roi", "plan"), ("Work out when a design system pays back", "roi", "plan"),
]

FLOW = ["palette", "contrast", "type", "space", "grid", "kit"]


def thumb(k):
    """A tiny live-looking preview for each card, in HTML and CSS (no images to load)."""
    if k == "palette":
        cols = ["#f5f6fe", "#c9d0fe", "#a8b0ff", "#858aff", "#675eff", "#4736fe", "#3e27b8", "#2b158a", "#19045e"]
        return '<div class="th th-pal">' + "".join(f'<i style="background:{c}"></i>' for c in cols) + "</div>"
    if k == "contrast":
        return '<div class="th th-con"><span class="a">Aa</span><span class="r">6.2:1</span><span class="p">AA ✓</span></div>'
    if k == "type":
        return '<div class="th th-typ">' + "".join(f'<span style="font-size:{s}px">Aa</span>' for s in (13, 16, 20, 25, 31)) + "</div>"
    if k == "space":
        return '<div class="th th-spc">' + "".join(f'<i style="width:{w}%"></i>' for w in (8, 14, 22, 32, 46, 66, 92)) + "</div>"
    if k == "grid":
        return '<div class="th th-grd">' + "<i></i>" * 12 + "</div>"
    if k == "names":
        return '<div class="th th-nam"><code><s>--btnBg</s></code><code>color-button-background</code><code class="ok">color-text-muted ✓</code></div>'
    if k == "kit":
        return '<div class="th th-kit"><code>--color-brand-500</code><code>--font-size-lg</code><code>--space-md</code></div>'
    if k == "backlog":
        return '<div class="th th-bkl">' + "".join(f'<i style="width:{w}%"></i>' for w in (92, 78, 61, 44)) + "</div>"
    if k == "roi":
        return '<div class="th th-roi">' + "".join(f'<span><i class="v" style="height:{v}%"></i><i class="c" style="height:{c}%"></i></span>' for v, c in ((47, 90), (82, 90), (100, 90))) + "</div>"
    return ""


def tool_nav(active):
    items = "".join(f'<a href="/lab/{BY[k]["slug"]}"{" aria-current=" + chr(34) + "page" + chr(34) if k == active else ""}>{ico(k)}<span><b>{BY[k]["short"]}</b></span></a>' for k in ORDER)
    return f'<nav class="lx-tabs" aria-label="Lab tools"><div class="lx-in"><div class="lx-tablist lx-toolnav"><a class="lx-all" href="/lab">All tools</a>{items}</div></div></nav>'


def ld_script(o):
    return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def strip_tags(h):
    return re.sub(r"<[^>]+>", "", h)


def writing_title(slug):
    """Short titles for linked articles, read from writing.py's catalogue when available."""
    if not WRITING_TITLES:
        try:
            import writing
            for a in writing.A:
                WRITING_TITLES[a["slug"]] = writing.short_title(a)
        except Exception:
            pass
    return WRITING_TITLES.get(slug, slug.replace("-", " ").capitalize())


def tool_page(t):
    k = t["key"]
    url = f'{SITE}/lab/{t["slug"]}'
    task = t["tasks"][0]
    presets = ""
    if t["presets"]:
        chips = "".join(f'<button type="button" class="lx-chip" data-lx-preset="{esc(json.dumps(p))}" aria-pressed="false">{esc(n)}</button>' for n, p in t["presets"])
        presets = f'<div class="lx-presets" role="group" aria-label="Examples"><span>Try an example</span>{chips}</div>'
    nxt = ""
    if t.get("next"):
        nk, nl = t["next"]
        nxt = f'<a class="lx-next" href="/lab/{BY[nk]["slug"]}"><span>Next step</span><b>{nl}</b>{ico(nk)}<i aria-hidden="true">→</i></a>'
    steps = "".join(f'<li><b>{a}</b><p>{b}</p></li>' for a, b in t["steps"])
    gets = "".join(f"<li>{g}</li>" for g in t["gets"])
    faqs = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t["faq"])
    rel = "".join(f'<a class="lx-rel" href="/lab/{BY[r]["slug"]}">{ico(r)}<span><b>{BY[r]["name"]}</b><small>{BY[r]["outcome"]}</small></span></a>' for r in t["related"])
    arts = "".join(f'<li><a href="/writing/{s}">{esc(writing_title(s))}</a></li>' for s in t["articles"])
    body = f'''<main id="main" class="lx lx-page" data-tool="{k}">
  <header class="lx-hero lx-hero--tool"><div class="lx-in">
    <nav class="lx-crumb" aria-label="Breadcrumb"><a href="/lab">Lab</a><span aria-hidden="true">/</span><a href="/lab?task={task}">{TASK[task][0]}</a><span aria-hidden="true">/</span><span aria-current="page">{t["name"]}</span></nav>
    <div class="lx-hero-row"><div><h1>{t["h1"]}</h1>
      <p class="lx-lede">{t["lede"]}</p>
      <ul class="lx-facts"><li>Free, no sign-up</li><li>Runs in your browser</li><li>Saves as you go</li></ul></div>
      <div class="lx-hero-act"><button type="button" class="lx-btn" data-share>Copy link to this</button><button type="button" class="lx-btn" data-reset>Reset</button><span class="lx-status" data-status role="status" aria-live="polite"></span></div></div>
  </div></header>
  {tool_nav(k)}
  <div class="lx-in">
    {presets}
    <section class="lx-panel" id="p-{k}" data-panel="{k}" aria-label="{t["name"]}">{t["panel"]}</section>
    {nxt}
  </div>
  <div class="lx-in lx-doc">
    <div class="lx-doc-main">
      <section aria-labelledby="how-h"><h2 id="how-h">How to use it</h2><ol class="lx-steps">{steps}</ol></section>
      <section class="lx-guide">{t["guide"]}</section>
      <section aria-labelledby="faq-h"><h2 id="faq-h">Questions</h2><div class="lx-faq">{faqs}</div></section>
    </div>
    <aside class="lx-doc-side" aria-label="More">
      <div class="lx-side-card"><h2>What you get</h2><ul class="lx-gets">{gets}</ul></div>
      <div class="lx-side-card"><h2>Related tools</h2>{rel}</div>
      <div class="lx-side-card"><h2>Read more</h2><ul class="lx-arts">{arts}</ul></div>
    </aside>
  </div>
  <div class="lx-in"><div class="lx-cta"><div><b>Want this done properly, for your product?</b><p>Our two-week audit turns your real screens into a token plan, a first-components list and a rollout plan.</p></div><a class="pill pill--accent" href="../pricing.html#plan-audit">See the audit</a></div></div>
</main>'''
    ld = [
        {"@context": "https://schema.org", "@type": "WebApplication", "name": t["h1"][0].upper() + t["h1"][1:], "url": url, "description": t["desc"],
         "applicationCategory": "DesignApplication", "operatingSystem": "Any (runs in the browser)", "browserRequirements": "Requires JavaScript",
         "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "featureList": [strip_tags(g) for g in t["gets"]], "publisher": {"@type": "Organization", "name": "Layer One", "url": SITE}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lab", "item": f"{SITE}/lab"},
            {"@type": "ListItem", "position": 2, "name": t["name"], "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in t["faq"]]},
    ]
    h = head(f'{t["title"]} | Layer One', t["desc"], depth=1)
    h = h.replace("</head>", "".join(ld_script(o) for o in ld) + "\n</head>")
    write(f'lab/{t["slug"]}.html', h + topbar("lab", 1) + body + f'<script src="../assets/lab.js?v={ver("assets/lab.js")}" defer></script>\n' + close(1))


def card(t):
    k = t["key"]
    tasks = " ".join(t["tasks"])
    words = " ".join([t["name"], t["outcome"], t["h1"], t["kw"], " ".join(TASK[x][0] for x in t["tasks"])]).lower()
    new = '<span class="lh-new">New</span>' if t.get("new") else ""
    return f'''<a class="lh-card" href="/lab/{t["slug"]}" data-task="{tasks}" data-k="{esc(words)}">
      <div class="lh-thumb" aria-hidden="true">{thumb(k)}</div>
      <div class="lh-body"><span class="lh-task">{ico(k)}{TASK[t["tasks"][0]][0]}{new}</span>
        <h3>{t["name"]}</h3><p>{t["outcome"]}</p></div>
      <span class="lh-go">Open the tool <i aria-hidden="true">→</i></span>
    </a>'''


def hub():
    chips = '<button type="button" class="lx-chip" data-task="" aria-pressed="true">All tools</button>' + "".join(
        f'<button type="button" class="lx-chip" data-task="{k}" aria-pressed="false">{n}</button>' for k, n, d in TASKS)
    cards = "".join(card(BY[k]) for k in ORDER)
    jobs = "".join(f'<li data-task="{task}" data-k="{esc((j + " " + BY[k]["name"] + " " + BY[k]["kw"]).lower())}"><a href="/lab/{BY[k]["slug"]}"><span>{j}</span><b>{ico(k)}{BY[k]["name"]}</b><i aria-hidden="true">→</i></a></li>' for j, k, task in JOBS)
    flow = "".join(f'<li><a href="/lab/{BY[k]["slug"]}"><span class="n">{i}</span>{ico(k)}<b>{BY[k]["name"]}</b><small>{BY[k]["outcome"]}</small></a></li>' for i, k in enumerate(FLOW, 1))
    suggest = "".join(f'<button type="button" class="lh-sug" data-q="{q}">{q}</button>' for q in ("contrast", "palette", "clamp", "breakpoints", "tailwind", "ROI"))
    hub_faq = [("Are the Lab tools free?", "Yes. Every tool is free, needs no account and runs in your browser. Nothing you enter is sent to a server."),
               ("Do the tools work together?", "Yes. They share your work in this browser: a palette you make is available in the contrast checker and the token generator, and the token generator combines your palette, type, spacing and grid into one file."),
               ("Can I share what I've made?", "Every tool has a “Copy link to this” button that encodes your settings in the link, so a colleague opens exactly what you see."),
               ("What formats can I export?", "CSS custom properties, Tailwind config, SCSS and W3C DTCG JSON for tokens; Markdown, CSV and JSON for the planning tools."),
               ("Who made these tools?", "Layer One, a design systems studio. They come from the method we use on client systems at companies like CARS24, IBM and JPMorgan Chase.")]
    faqs = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in hub_faq)
    body = f'''<main id="main" class="lx lx-hub">
  <header class="lx-hero lh-hero"><div class="lx-in">
    <p class="lx-eyebrow">lab:</p>
    <h1>Free design system tools</h1>
    <p class="lx-lede">Practical tools for the jobs that come up when you build and run a design system: palettes, contrast, type, spacing, grids, token names, exports and the business case. Pick what you're trying to do, or search.</p>
    <div class="lh-search" role="search">
      <label for="lh-q" class="sr">Search the tools</label>
      {ico("search")}<input id="lh-q" type="search" placeholder="What do you want to do? Try “contrast”, “clamp” or “Tailwind colours”" autocomplete="off" spellcheck="false">
      <span class="lh-count" data-count aria-live="polite"></span>
    </div>
    <div class="lh-sugs"><span>Popular:</span>{suggest}</div>
  </div></header>
  <div class="lx-in">
    <div class="lh-tasks" role="group" aria-label="Filter by task">{chips}</div>
    <section aria-labelledby="tools-h" class="lh-sec"><h2 id="tools-h" class="lh-h">tools:</h2><div class="lh-grid" data-list>{cards}</div></section>
    <p class="lh-empty" data-empty hidden>No tool matches that yet. <a href="contact.html">Tell us what you were looking for</a>; it's how we decide what to build next.</p>
    <section aria-labelledby="jobs-h" class="lh-sec"><div class="lh-sec-bar"><h2 id="jobs-h" class="lh-h">start from a problem:</h2><p>Common jobs, and the tool that does each one.</p></div><ul class="lh-jobs" data-jobs>{jobs}</ul></section>
    <section aria-labelledby="flow-h" class="lh-sec"><div class="lh-sec-bar"><h2 id="flow-h" class="lh-h">build a token set in six steps:</h2><p>Each tool saves as you go and feeds the next, ending in one token file.</p></div><ol class="lh-flow">{flow}</ol></section>
    <section aria-labelledby="faq-h" class="lh-sec lh-faq-sec"><h2 id="faq-h" class="lh-h">questions:</h2><div class="lx-faq">{faqs}</div></section>
    <div class="lx-cta"><div><b>Want this done properly, for your product?</b><p>Our two-week audit turns your real screens into a token plan, a first-components list and a rollout plan.</p></div><a class="pill pill--accent" href="pricing.html#plan-audit">See the audit</a></div>
  </div>
</main>'''
    old = json.dumps({k: BY[k]["slug"] for k in BY})
    script = '''<script>
(function () {
  // Old links (/lab#contrast, /lab#s=...) open the matching tool page.
  var OLD = ''' + old + ''', h = location.hash;
  if (h) {
    var m = h.match(/^#([a-z]+)$/), s = h.match(/^#s=([^&]+)/), k = m && m[1];
    if (s) { try { k = JSON.parse(decodeURIComponent(escape(atob(s[1].replace(/-/g, "+").replace(/_/g, "/"))))).tab; } catch (e) {} }
    if (k && OLD[k]) { location.replace("/lab/" + OLD[k] + (s ? h : "")); return; }
  }
  var q = document.getElementById("lh-q"), cards = [].slice.call(document.querySelectorAll("[data-list] > a")), jobs = [].slice.call(document.querySelectorAll("[data-jobs] > li"));
  var chips = [].slice.call(document.querySelectorAll(".lh-tasks [data-task]")), count = document.querySelector("[data-count]"), empty = document.querySelector("[data-empty]"), task = "";
  var SYN = { colour: "color", colours: "color", colors: "color", grey: "gray", a11y: "accessibility", accessible: "accessibility", wcag: "wcag", fonts: "font", typography: "type", tokens: "token", columns: "column", breakpoint: "breakpoints", prioritise: "prioritization", prioritize: "prioritization", roi: "roi", savings: "roi" };
  function terms(v) { return v.toLowerCase().replace(/[“”"']/g, "").split(/[^a-z0-9().]+/).filter(Boolean).map(function (w) { return SYN[w] || w.replace(/s$/, ""); }); }
  function run(push) {
    var t = terms(q.value), n = 0;
    function hit(el) { var k = el.getAttribute("data-k"), okT = !task || (" " + el.getAttribute("data-task") + " ").indexOf(" " + task + " ") > -1; return okT && t.every(function (w) { return k.indexOf(w) > -1; }); }
    cards.forEach(function (c) { var on = hit(c); c.hidden = !on; if (on) n++; });
    jobs.forEach(function (j) { j.hidden = !hit(j); });
    count.textContent = q.value || task ? n + (n === 1 ? " tool" : " tools") : "";
    empty.hidden = n > 0;
    chips.forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-task") === task ? "true" : "false"); });
    if (push) { var u = new URLSearchParams(); if (q.value) u.set("q", q.value); if (task) u.set("task", task); try { history.replaceState(null, "", location.pathname + (u.toString() ? "?" + u : "")); } catch (e) {} }
  }
  var p = new URLSearchParams(location.search); q.value = p.get("q") || ""; task = p.get("task") || "";
  q.addEventListener("input", function () { run(true); });
  q.addEventListener("keydown", function (e) { if (e.key === "Enter") { var f = cards.filter(function (c) { return !c.hidden; })[0]; if (f) location.href = f.href; } });
  chips.forEach(function (c) { c.addEventListener("click", function () { task = c.getAttribute("data-task"); run(true); }); });
  [].forEach.call(document.querySelectorAll("[data-q]"), function (b) { b.addEventListener("click", function () { q.value = b.getAttribute("data-q"); run(true); q.focus(); }); });
  run(false);
})();
</script>'''
    items = [{"@type": "ListItem", "position": i, "url": f'{SITE}/lab/{BY[k]["slug"]}', "name": BY[k]["h1"][0].upper() + BY[k]["h1"][1:]} for i, k in enumerate(ORDER, 1)]
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Free design system tools", "url": f"{SITE}/lab",
           "description": "Free online tools for designers and design system teams.", "mainEntity": {"@type": "ItemList", "itemListElement": items}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in hub_faq]}]
    h = head("Free Design System Tools: Color, Type, Tokens | Layer One",
             "Free online design system tools: OKLCH palette generator, WCAG and APCA contrast checker, type scale, spacing, grid, token tools and an ROI calculator.")
    h = h.replace("</head>", "".join(ld_script(o) for o in ld) + "\n</head>")
    write("lab.html", h + topbar("lab") + body + script + close())


def main():
    os.makedirs(os.path.join(OUT, "lab"), exist_ok=True)
    for t in TOOLS:
        tool_page(t)
    hub()
    # Lean stylesheet for the Lab pages only (site.css also styles the home page, case studies and writing).
    from purge_css import purge
    pages = [os.path.join(OUT, "lab.html")] + [os.path.join(OUT, "lab", t["slug"] + ".html") for t in TOOLS]
    full, lean = purge(pages, "assets/lab.css", js=("assets/lab.js",))
    v = ver("assets/lab.css")
    for f in pages:
        h = open(f).read()
        h = re.sub(r'(href="(?:\.\./)*)assets/site\.css\?v=\w+"', lambda m: f'{m.group(1)}assets/lab.css?v={v}"', h)
        open(f, "w").write(h)
    print(f"lab.css: {lean // 1024} KB (site.css {full // 1024} KB), used by {len(pages)} pages")


main()
