"""CARS24: LEGO for internal tools, one design system for 30+ data-heavy tools. Showcase engine (see showcase.py).

Sources: the CARS24 Internal Tool DLS Figma file (tokens, component sheets, user guide, component docs).
Real screens and sheets are cut from Figma renders into assets/work/cars24-internal-tools/. The token
explorer, the Storybook panel and the data table are rebuilt in code with the system's real values.
Behaviour: data-surf, data-sb and data-dt in assets/site.js. Styles: "CARS24 internal tools" in assets/site.css.
"""
from showcase import *
import html as _h

I = "assets/work/cars24-internal-tools/"

# ---------------------------------------------------------------- 03 primitives (real values from the token file)
STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
RAMPS = {
    "slate": ["#f8fafc", "#f1f5f9", "#e2e8f0", "#cbd5e1", "#94a3b8", "#64748b", "#475569", "#334155", "#1e293b", "#0f172a", "#020617"],
    "gray": ["#f9fafb", "#f3f4f6", "#e5e7eb", "#d1d5db", "#9ca3af", "#6b7280", "#4b5563", "#374151", "#1f2937", "#111827", "#030712"],
    "zinc": ["#fafafa", "#f4f4f5", "#e4e4e7", "#d4d4d8", "#a1a1aa", "#71717a", "#52525b", "#3f3f46", "#27272a", "#18181b", "#09090b"],
    "neutral": ["#fafafa", "#f5f5f5", "#e5e5e5", "#d4d4d4", "#a3a3a3", "#737373", "#525252", "#404040", "#262626", "#171717", "#0a0a0a"],
    "stone": ["#fafaf9", "#f5f5f4", "#e7e5e4", "#d6d3d1", "#a8a29e", "#78716c", "#57534e", "#44403c", "#292524", "#1c1917", "#0c0a09"],
    "red": ["#fef2f2", "#fee2e2", "#fecaca", "#fca5a5", "#f87171", "#ef4444", "#dc2626", "#b91c1c", "#991b1b", "#7f1d1d", "#450a0a"],
    "orange": ["#fff7ed", "#ffedd5", "#fed7aa", "#fdba74", "#fb923c", "#f97316", "#ea580c", "#c2410c", "#9a3412", "#7c2d12", "#431407"],
    "amber": ["#fffbeb", "#fef3c7", "#fde68a", "#fcd34d", "#fbbf24", "#f59e0b", "#d97706", "#b45309", "#92400e", "#78350f", "#451a03"],
    "yellow": ["#fefce8", "#fef9c3", "#fef08a", "#fde047", "#facc15", "#eab308", "#ca8a04", "#a16207", "#854d0e", "#713f12", "#422006"],
    "lime": ["#f7fee7", "#ecfccb", "#d9f99d", "#bef264", "#a3e635", "#84cc16", "#65a30d", "#4d7c0f", "#3f6212", "#365314", "#1a2e05"],
    "green": ["#f0fdf4", "#dcfce7", "#bbf7d0", "#86efac", "#4ade80", "#22c55e", "#16a34a", "#15803d", "#166534", "#14532d", "#052e16"],
}
USE = {
    "slate-50": "color-surface-primary-default. The page and table background.", "slate-100": "color-surface-primary-focused and -disabled.",
    "slate-200": "color-surface-primary-hover and -pressed. Table rows on hover.", "slate-300": "color-surface-primary-active.",
    "gray-50": "color-surface-secondary-default. Toolbars and table headers.", "gray-200": "color-surface-secondary-hover.",
    "zinc-50": "color-surface-tertiary-default.", "neutral-50": "color-surface-subtle-default.",
    "red-600": "Destructive actions and error text.", "red-300": "Destructive button border, on hover.",
    "green-600": "Success states.", "amber-500": "Warnings.",
}
rows = "".join(
    f'<div class="sc-ramp-row"><span>{name}</span>' + "".join(
        f'<button type="button" style="--c:{h}" data-hex="{h}" data-name="{name}-{s}" data-use="{USE.get(f"{name}-{s}", "")}"'
        f'{" data-default" if name == "slate" and s == 50 else ""} aria-label="{name}-{s}, {h}"></button>' for s, h in zip(STEPS, hexes)) + "</div>"
    for name, hexes in RAMPS.items())
explorer = f'''<div class="sc-ramps it-ramps" data-rampgrid>
  <div><div class="sc-ramp-steps"><span></span>{"".join(f"<span>{s}</span>" for s in STEPS)}</div><div class="sc-ramp-grid">{rows}</div></div>
  <aside class="sc-ramp-read" aria-live="polite"><div class="sw"><span data-n>slate-50</span><span>Aa</span></div>
    <dl><div><dt>Value</dt><dd data-h>#F8FAFC</dd></div><div><dt>On white</dt><dd data-w></dd></div><div><dt>On slate-950</dt><dd data-k></dd></div></dl>
    <p data-u></p></aside>
</div>'''

# ---------------------------------------------------------------- 03 surface roles × states (real mapping)
STATES = ["default", "hover", "active", "pressed", "focused", "disabled"]
ROLES = [  # role, label, [(primitive, hex) per state], text colour on it
    ("primary", "Primary", [("slate-50", "#f8fafc"), ("slate-200", "#e2e8f0"), ("slate-300", "#cbd5e1"), ("slate-200", "#e2e8f0"), ("slate-100", "#f1f5f9"), ("slate-100", "#f1f5f9")], "#0f172a"),
    ("secondary", "Secondary", [("grey-50", "#f9fafb"), ("grey-200", "#e5e7eb"), ("grey-300", "#d1d5db"), ("grey-200", "#e5e7eb"), ("grey-100", "#f3f4f6"), ("grey-100", "#f3f4f6")], "#111827"),
    ("brand", "Brand", [("denim-600", "#5546ff"), ("denim-800", "#0f0fa9"), ("denim-700", "#2323c7"), ("denim-800", "#0f0fa9"), ("denim-600", "#5546ff"), ("denim-100", "#eef2fb")], "#ffffff"),
    ("accent-blue", "Accent blue", [("blue-50", "#eff6ff"), ("blue-100", "#dbeafe"), ("blue-200", "#bfdbfe"), ("blue-300", "#93c5fd"), ("blue-100", "#dbeafe"), ("blue-100", "#dbeafe")], "#1e3a8a"),
    ("accent-pink", "Accent pink", [("pink-50", "#fdf2f8"), ("pink-100", "#fce7f3"), ("pink-200", "#fbcfe8"), ("pink-300", "#f9a8d4"), ("pink-100", "#fce7f3"), ("pink-100", "#fce7f3")], "#831843"),
    ("accent-teal", "Accent teal", [("teal-50", "#f0fdfa"), ("teal-100", "#ccfbf1"), ("teal-200", "#99f6e4"), ("teal-300", "#5eead4"), ("teal-100", "#ccfbf1"), ("teal-100", "#ccfbf1")], "#134e4a"),
]
surf_data = "|".join(f'{r};{lab};{tx};' + ",".join(f"{p}:{h}" for p, h in v) for r, lab, v, tx in ROLES)
surf = f'''<div class="it-surf" data-surf data-roles="{surf_data}">
  <div class="it-surf-pick">
    <p class="it-k">Role</p><div class="it-chips" data-role>{"".join(f'<button type="button" aria-pressed="{"true" if i == 2 else "false"}" data-v="{i}">{lab}</button>' for i, (r, lab, v, tx) in enumerate(ROLES))}</div>
    <p class="it-k">State</p><div class="it-chips" data-state>{"".join(f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" data-v="{i}">{s}</button>' for i, s in enumerate(STATES))}</div>
    <div class="it-surf-grid" aria-hidden="true">{"".join("<div>" + "".join(f'<i style="--c:{h}"></i>' for p, h in v) + "</div>" for r, lab, v, tx in ROLES)}</div>
  </div>
  <div class="it-surf-out" aria-live="polite">
    <div class="it-surf-sw" data-sw><span data-sl>Continue</span></div>
    <ol class="it-surf-chain"><li><span>Semantic</span><code data-sem>color-surface-brand-default</code></li><li><span>Primitive</span><code data-pri>denim-600</code></li><li><span>Value</span><code data-hex>#5546FF</code></li></ol>
    <p class="it-note">Six of the nine surface roles, each with six states. Engineers pick a role and a state; the primitive underneath can change without touching a screen.</p>
  </div>
</div>'''

# ---------------------------------------------------------------- 03 scales (real values)
SPACE = [("3xs", 2), ("2xs", 4), ("xs", 6), ("sm", 8), ("md", 12), ("lg", 14), ("xl", 16), ("2xl", 20), ("3xl", 24), ("4xl", 28), ("5xl", 32), ("6xl", 40), ("7xl", 44), ("8xl", 48), ("9xl", 56), ("10xl", 64)]
space = '<div class="it-scale"><p class="it-k">Spacing · 16 steps</p>' + "".join(f'<div><code>space-{n}</code><i style="--w:{px}"></i><span>{px}</span></div>' for n, px in SPACE) + "</div>"
RADIUS = [("2xs", 2), ("xs", 4), ("sm", 8), ("md", 12), ("lg", 16), ("2xl", 24), ("full", 999)]
radius = '<div class="it-radius"><p class="it-k">Radius</p><div>' + "".join(f'<figure><i style="--r:{px}px"></i><figcaption><code>radius-{n}</code><span>{"9999" if px == 999 else px}</span></figcaption></figure>' for n, px in RADIUS) + "</div></div>"
BP = [("xs", 320, "Small mobile"), ("sm", 480, "Mobile landscape"), ("md", 768, "Tablet"), ("lg", 1024, "Laptop"), ("xl", 1280, "Large desktop"), ("2xl", 1440, "Wide"), ("3xl", 1600, "Wide"), ("4xl", 1920, "HD")]
bps = '<div class="it-bp"><p class="it-k">Breakpoints · 8</p>' + "".join(f'<div><code>bp-{n}</code><i style="--w:{px / 1920 * 100:.1f}%"></i><span>{px}</span></div>' for n, px, d in BP) + "</div>"
TYPE = [(900, 68, 68), (800, 60, 66), (700, 48, 53), (600, 40, 52), (500, 32, 45), (400, 24, 34), (350, 20, 28)]
types = '<div class="it-type"><p class="it-k">Type · font-size tokens, 4 weights</p>' + "".join(
    f'<div><code>--font-size-{t}</code><small>{s}/{lh}</small><p style="font-size:{s / 68 * 2.3:.2f}em">Leads</p></div>' for t, s, lh in TYPE) + '<p class="it-note">Each size has a matching line-height and letter-spacing token. Weights 400, 500, 600 and 700.</p></div>'

scales = f'<div class="it-scales">{space}<div class="it-scales-r">{radius}{bps}</div>{types}</div>'

# ---------------------------------------------------------------- 04 Storybook, recreated
sb = '''<div class="it-sb" data-sb>
  <div class="it-sb-bar"><span class="dots"><i></i><i></i><i></i></span><span>storybook · LEGO internal</span><span class="tab">Canvas</span><span class="tab off">Docs</span></div>
  <div class="it-sb-body">
    <nav class="it-sb-nav" aria-label="Storybook stories (recreation)">
      <p>Foundations</p><a>Colour tokens</a><a>Spacing</a><a>Typography</a>
      <p>Components</p><a class="on">Button</a><a>Button group</a><a>Text input</a><a>Table</a><a>Toast</a><a>Date picker</a><a>Sidebar navigation</a>
    </nav>
    <div class="it-sb-main">
      <div class="it-sb-canvas"><button type="button" class="ib" data-ib data-variant="primary" data-size="md" data-state="default"><span class="sp" aria-hidden="true"></span><span data-lbl>Continue</span><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3v10M3 8h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button></div>
      <pre class="it-sb-code" data-code></pre>
      <div class="it-sb-ctl">
        <div><span>variant</span><div class="it-chips" data-ctl="variant"><button type="button" aria-pressed="true" data-v="primary">primary</button><button type="button" aria-pressed="false" data-v="secondary">secondary</button><button type="button" aria-pressed="false" data-v="minimal">minimal</button><button type="button" aria-pressed="false" data-v="destructive">destructive</button></div></div>
        <div><span>size</span><div class="it-chips" data-ctl="size"><button type="button" aria-pressed="true" data-v="md">md</button><button type="button" aria-pressed="false" data-v="sm">sm</button></div></div>
        <div><span>state</span><div class="it-chips" data-ctl="state"><button type="button" aria-pressed="true" data-v="default">default</button><button type="button" aria-pressed="false" data-v="hover">hover</button><button type="button" aria-pressed="false" data-v="focus">focus</button><button type="button" aria-pressed="false" data-v="loading">loading</button><button type="button" aria-pressed="false" data-v="disabled">disabled</button></div></div>
        <div><span>label</span><input type="text" value="Continue" maxlength="24" data-ctl-label aria-label="Button label"></div>
      </div>
    </div>
  </div>
</div>'''

# ---------------------------------------------------------------- 06 the data table, live (illustrative data, real columns)
DT = [("123456", 742, "+91 98450 31254", "Guaranteed", 120000, "CC Intent", "Jaipur", "Interest"),
      ("456767", 688, "+91 99018 77383", "Partner", 85000, "RA Lead", "Delhi", "All Docs"),
      ("3456767", 801, "+91 98338 27728", "Guaranteed", 240000, "SA Inspect", "Noida", "Interest"),
      ("456788", 655, "+91 91057 37860", "Partner", 60000, "CC Intent", "Gurgaon", "All Docs"),
      ("4567889", 712, "+91 97290 82910", "Guaranteed", 150000, "RA Lead", "Jaipur", "Approved"),
      ("2345678", 774, "+91 96062 89487", "Guaranteed", 120700, "RA Lead", "Delhi", "Interest"),
      ("6789054", 630, "+91 98724 30099", "Partner", 45000, "SA Inspect", "Noida", "Rejected"),
      ("876543", 795, "+91 98026 34591", "Guaranteed", 320000, "RA Lead", "Gurgaon", "Approved"),
      ("9876543", 701, "+91 98687 49716", "Guaranteed", 92000, "SA Inspect", "Delhi", "All Docs"),
      ("4356789", 668, "+91 92520 31349", "Partner", 120000, "RA Lead", "Jaipur", "Interest")]
ST = {"Interest": "b", "All Docs": "n", "Approved": "g", "Rejected": "r"}
trs = "".join(
    f'<tr data-city="{c}"><td><input type="checkbox" aria-label="Select {a}"></td><td>{a}</td><td data-n="{s}">{s}</td><td>{p}</td><td>{co}</td><td data-n="{m}">₹{m:,}</td><td>{src}</td><td>{c}</td><td><span class="it-st {ST[st]}">{st}</span></td></tr>'
    for a, s, p, co, m, src, c, st in DT)
cities = ["Delhi", "Gurgaon", "Jaipur", "Noida"]
dtable = f'''<div class="it-dt" data-dt data-density="46">
  <div class="it-dt-top">
    <b>Loan leads</b>
    <label class="it-dt-search"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m10.5 10.5 3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg><input type="search" placeholder="Search by ID or phone" data-dt-q aria-label="Search the table"></label>
    <div class="it-dt-tools">
      <div class="it-dt-pop"><button type="button" class="ob" data-dt-open aria-expanded="false"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 3h11l-4.2 5v4.5l-2.6 1V8z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>City<i data-dt-count hidden></i></button>
        <div class="it-dt-menu" data-dt-menu hidden><p>Filter by city</p>{"".join(f'<label><input type="checkbox" value="{c}">{c}</label>' for c in cities)}<div class="r"><button type="button" class="pb" data-dt-apply>Continue</button><button type="button" class="ob" data-dt-clear>Clear</button></div></div></div>
      <div class="it-dt-dens" role="group" aria-label="Row height"><button type="button" data-d="40" aria-pressed="false">40</button><button type="button" data-d="46" aria-pressed="true">46</button><button type="button" data-d="56" aria-pressed="false">56</button></div>
    </div>
  </div>
  <div class="it-dt-scroll"><table>
    <thead><tr><th scope="col"><input type="checkbox" aria-label="Select all" data-dt-all></th><th scope="col">Application ID</th><th scope="col"><button type="button" data-sort="2">CIBIL score <span aria-hidden="true">↕</span></button></th><th scope="col">Phone number</th><th scope="col">Company</th><th scope="col"><button type="button" data-sort="5">Max loan <span aria-hidden="true">↕</span></button></th><th scope="col">Lead source</th><th scope="col">City</th><th scope="col">Status</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
  <div class="it-dt-foot"><span data-dt-sum>10 of 10 leads</span><span data-dt-sel></span><span class="pg"><button type="button" class="ob" disabled>Previous</button><b>1</b><span>2</span><span>3</span><span>…</span><span>10</span><button type="button" class="ob">Next</button></span></div>
</div>'''

anno = f'''<div class="it-anno">
  <figure>{simg(I + "screen-filter.webp", "A dense lead table from the system: search, sort, show column, per-column filters, bulk select and pagination")}
    <span class="pin" style="left:35%;top:4%">1</span><span class="pin" style="left:62%;top:4%">2</span><span class="pin" style="left:78%;top:4%">3</span><span class="pin" style="left:88%;top:4%">4</span>
    <span class="pin" style="left:2%;top:13%">5</span><span class="pin" style="left:73%;top:28%">6</span><span class="pin" style="left:38%;top:98%">7</span></figure>
  <ol><li>Search across every column</li><li>Sort by any column</li><li>Show and hide columns</li><li>Filters that combine</li><li>Bulk select, for actions on many rows</li><li>A filter on one column, with its own search</li><li>Pagination for tens of thousands of rows</li></ol>
</div>'''

# ---------------------------------------------------------------- 02 audit
audit_cards = [("In nearly every tool", "h", ["Data table", "Filters", "Search", "Side navigation", "Top bar", "Pagination", "Status badge", "Button"]),
               ("In most tools", "m", ["Text input", "Dropdown", "Date picker", "Modal", "Toast", "Tabs", "Checkbox", "Breadcrumbs"]),
               ("In some tools", "l", ["File upload", "Stepper", "Slider", "Carousel", "Avatar", "Time picker", "Accordion", "Segment control"])]
audit = '<div class="it-audit">' + "".join(
    f'<article class="{k}"><header><b>{t}</b><span>{len(c)}</span></header><ul>{"".join(f"<li>{x}</li>" for x in c)}</ul></article>' for t, k, c in audit_cards) + "</div>"

# ---------------------------------------------------------------- 07 docs
docs = '''<div class="it-docs">
  <article><header><code>Toast</code><span>Feedback</span></header><dl>
    <div><dt>Variants</dt><dd>error · warning · success · info · neutral</dd></div><div><dt>Styles</dt><dd>filled · lighter · stroke</dd></div>
    <div><dt>Sizes</dt><dd>32px · 40px (default) · 132px with description</dd></div><div><dt>Spacing</dt><dd>16px gap · 10px sides · radius 8px / 12px</dd></div>
    <div><dt>Behaviour</dt><dd>One or two at a time · dismiss after 5–7s</dd></div></dl>
    <p class="dont"><b>Don't</b> use a toast for anything the user must acknowledge.</p></article>
  <article><header><code>Alert banner</code><span>Feedback</span></header><dl>
    <div><dt>Statuses</dt><dd>error · warning · success · info · neutral</dd></div><div><dt>Type</dt><dd>title 14 medium · body 14 regular · link 14</dd></div>
    <div><dt>Padding</dt><dd>14px × 12px · 12px between alerts</dd></div><div><dt>Instead</dt><dd>toast for transient news · modal to interrupt</dd></div></dl>
    <p class="dont"><b>Don't</b> stack several banners on one dashboard.</p></article>
  <article><header><code>Stepper</code><span>Navigation</span></header><dl>
    <div><dt>States</dt><dd>default · error · ongoing · success · disabled</dd></div><div><dt>Use when</dt><dd>a process has several steps the user must track</dd></div>
    <div><dt>Labels</dt><dd>"Enter details", never "Step 1"</dd></div><div><dt>Mobile</dt><dd>switch to the vertical stepper</dd></div></dl>
    <p class="dont"><b>Don't</b> lock navigation in a non-linear process.</p></article>
</div>'''
rules = '''<div class="it-rules">
  <div><b>All designs are tokenised</b><span>No hard-coded colour, spacing or type. Ever.</span></div>
  <div><b>Components are used as provided</b><span>A custom version needs the maintainers' approval.</span></div>
  <div><b>Names match Figma</b><span>Same component, prop and token names in design and code.</span></div>
  <div><b>QA before release</b><span>Viewports, token use and accessibility, checked and written down.</span></div>
</div>'''

# ---------------------------------------------------------------- library
fams = [("Actions", ["Button", "Icon button", "Button group", "Link"]),
        ("Inputs", ["Text input", "Text area", "Verification code", "Dropdown", "Multi select", "Search", "File upload", "Slider", "Date picker", "Range calendar", "Time picker"]),
        ("Selection", ["Checkbox", "Radio", "Switch", "Checkbox card", "Radio card", "Switch card", "Choice chips", "Chip", "Segment control"]),
        ("Feedback", ["Alert banner", "Toast and notification", "Tooltip", "Loader", "Progress bar", "Status modal", "Modal dialogue"]),
        ("Navigation", ["Sidebar navigation", "Header", "Tabs", "Tab group", "Breadcrumbs", "Pagination", "Stepper", "Timeline stepper", "Menu", "Drawer"]),
        ("Data display", ["Table header", "Table cell", "Table row", "Badge", "Avatar", "Card", "Carousel", "Accordion", "Divider", "Kbd", "Grid count"])]

S = [
    section("brief", "The brief", "<b>01</b> the brief:", "30+ tools. No shared language.",
            "CARS24 runs on internal tools: for loans, inspections, dealers, sales and operations. Each one had been built its own way.",
            wrap(facts([("30+", "internal tools, across every vertical"), ("100+", "designers and engineers building them"), ("None", "shared tokens, components or docs"), ("3–4", "months to a beta for leadership")])
                 + gap(32)
                 + brief([("squads", "Every tool team drew its own tables, filters and navigation", "One library that every tool builds from"),
                          ("clock", "Engineers rebuilt the same data table in every tool", "Build the table once, reuse it everywhere"),
                          ("layers", "Engineers who had never worked with a design system", "Tokens and Storybook, taught from day one"),
                          ("drift", "Tools used by employees, dealers and partners looked unrelated", "One look and feel, inside and outside the company")])
                 + gap(40)
                 + story(prose(
                     "Internal tools are where much of CARS24 actually runs. Dealers manage their cars in them, loan teams work through lead queues, inspectors log reports and operations track every deal. Some are used only by employees; others are used by dealers and partners outside the company.",
                     "Each tool had been built by a different team, at a different time, with no shared language between design and engineering. The same table, filter bar and side navigation existed in dozens of versions. Every new tool started from a blank file.",
                     "The ask from leadership was simple: make every internal tool look and feel good, and make sure the next ones cost less to build. Better quality, fewer engineering hours, and tools that feel like one company.",
                     "> How might we give 100+ people who had never used a design system one they would rely on?"),
                     "The project", [("2025", "CARS24"), ("Role", "Design Systems Lead"), ("Users", "Employees, dealers, partners"), ("Built with", "A squad of 8 engineers")]))),
    section("audit", "Audit", "<b>02</b> the audit:", "20+ tools, opened one by one",
            "Before drawing anything, every screen of 20+ live tools was taken apart and sorted into components and patterns.",
            wrap(rail([("Get access", "Logins to 20+ tools across verticals"),
                       ("Map the screens", "Every page, dialog and state, tool by tool"),
                       ("Cut it apart", "Each element on each screen, grouped by what it does"),
                       ("Find the patterns", "Tables, filters, navigation and forms that repeat"),
                       ("Rank", "By how many tools use it and how painful it was"),
                       ("Shortlist", "What to build first, agreed with engineering")])
                 + gap(40) + audit
                 + '<p class="sc-note">Grouping summarised from the audit. These are dense, enterprise-style tools: the hard parts were never buttons, they were tables with tens of thousands of rows.</p>'), mode="paper"),
    section("foundations", "Foundations", "<b>03</b> foundations first:", "Tokens before a single component",
            "The token file came first: colour, type, spacing, radius, border width, opacity, icon sizes and breakpoints.",
            wrap(explorer
                 + '<p class="sc-note">11 primitive ramps of 11 steps. They follow the Tailwind scale, which most of the engineers already knew, so the first conversation was about meaning, not hex values. Hover a swatch.</p>'
                 + gap(56) + '<p class="it-k" style="margin-bottom:14px">Semantic surfaces: pick a role and a state</p>' + surf
                 + gap(56) + scales)),
    section("storybook", "Storybook", "<b>04</b> into code:", "Same names in Figma and in Storybook",
            "Engineers were new to tokens and Storybook, so both were set up together with them, one component at a time. Try the controls.",
            wrap(sb + '<p class="sc-note" style="color:inherit">A recreation of the Storybook setup, rebuilt in code with the button\'s real values from Figma: four variants, two sizes, five states.</p>'
                 + gap(32)
                 + room([("Tokens", "One source, two outputs", "Design tokens exported for Figma and for code, so a change to denim-600 reaches both."),
                         ("Storybook", "A story per component", "Every variant and state, with controls that use the same prop names as Figma."),
                         ("Handoff", "No redlines", "Engineers read token and prop names off the component instead of measuring screens.")])), mode="stage"),
    section("library", "Library", "<b>05</b> the library:", "93 component sets, 1,205 variants",
            "Every sheet carries its states, sizes and usage, and a version number.",
            wrap(bento([(I + "tokens-surface.webp", "Surface tokens: nine roles, six states each", 7, 4, {"bg": "#f8fafc", "pad": "12px", "fit": "contain"}),
                        (I + "sheet-button.webp", "Button v2.0: four variants, five states, two sizes", 5, 4, {"bg": "#ffffff", "pad": "12px", "fit": "contain"}),
                        (I + "tokens-primitive.webp", "Primitive colour tokens", 6, 3, {"bg": "#f8fafc", "fit": "cover", "pos": "top"}),
                        (I + "artwork.webp", "The system's own cover artwork", 6, 3, {"bg": "#4736fe", "fit": "cover", "pos": "center"})])
                 + gap(24) + inventory("93", "component sets in Figma, built from private base parts", fams))),
    section("table", "The table", "<b>06</b> the hardest part:", "The table carried the whole system",
            "In a data-heavy tool, the table is the product. It got the most time: cells, headers, filters, density and pagination.",
            wrap(dtable + '<p class="sc-note">Rebuilt in code with the system\'s table columns. Sort the scores, filter by city, change the row height. Data is made up.</p>'
                 + gap(48) + '<p class="it-k" style="margin-bottom:14px">From the Figma file</p>' + anno
                 + gap(16) + bigfig(I + "screen-dashboard.webp", "A dashboard built from the system: sidebar navigation, summary cards, toolbar and the table", bg="#f8fafc", pad="0")), mode="paper"),
    section("docs", "Docs and rules", "<b>07</b> written for engineers:", "Docs that answer the next question",
            "Every component page says what it is, when to use it, its specs, and what not to do.",
            wrap(docs + gap(24) + rules
                 + '<p class="sc-note">Specs quoted from the component documentation in the Figma file. Help lived in one Slack channel, #design-system-help.</p>')),
    section("contribution", "Contribution", "<b>08</b> who builds what:", "Teams build it. Two maintainers guard it.",
            "The system team couldn't build everything. So the engineers who needed a component built it into the system.",
            wrap(room([("Squad", "8 engineers", "Building internal tools across verticals. When a feature needed a component, they built it into the system."),
                       ("Maintainers", "2 engineers", "Reviewed every contribution against the tokens, the props and the docs before it shipped."),
                       ("Design", "A system designer and a lead", "One designer full time on the system; Aniket on direction, quality and the roadmap.")])
                 + gap(32)
                 + rail([("Need", "A tool's roadmap needs a component"), ("Check", "Is it in the library already?"), ("Design", "Drawn on the tokens, every state"),
                         ("Build", "The squad engineer builds it, with a story"), ("Review", "Maintainers check tokens, props, docs"), ("Release", "Published, announced in Slack")])
                 + gap(24)
                 + flowline(["Requested", "In design", "In build", "In review", "Released"], 3)), mode="stage"),
    section("timeline", "Timeline", "<b>09</b> the runway:", "Three to four months to a beta",
            "Leadership set the deadline. The order was fixed: understand, then foundations, then components, then process.",
            wrap(timeline([("Month 1", "Audit", "Access to 20+ tools, every screen taken apart, the shortlist agreed with engineering.", "20+ tools"),
                           ("Month 1–2", "Foundations", "Primitive and semantic tokens, type, spacing, radius, breakpoints. Exported for Figma and code.", "100+ tokens"),
                           ("Month 2", "Storybook", "Set up with the squad. How tokens work, how a story works, how props map to Figma.", "With 8 engineers"),
                           ("Month 2–3", "Components", "Table, filters and navigation first, then forms and feedback. Each with docs and QA.", "93 sets"),
                           ("Month 3–4", "Contribution model", "Two maintainers, a review checklist, a Slack channel and a request process.", "Running"),
                           ("Month 4", "Beta to leadership", "The library, the docs and the first tools rebuilt on it, presented as a beta.", "Shipped")])
                 + '<p class="sc-note">Approximate months.</p>')),
    section("impact", "Impact", "<b>10</b> what changed:", "One system behind every new tool", "",
            wrap(outcomes([("Library", "93 component sets", "1,205 variants and 100+ tokens, in beta, with a roadmap for complex patterns."),
                           ("Teams", "Built with, not for", "A squad of 8 engineers contributed; 2 maintainers kept the bar."),
                           ("Reach", "CARS24's global teams", "Teams building internal tools across the company were asked to start from it."),
                           ("Leadership", "A clear yes", "Well received by the engineering teams and by leadership at the beta review.")])
                 + gap(16) + lessons(["In data-heavy tools, start with the table. Everything else hangs off it.",
                                      "Teach tokens before you ship components. Engineers who understand the chain stop hard-coding.",
                                      "Let the teams who need a component build it, and give two people the right to say no."]))),
    section("playbook", "For your team", "<b>11</b> for your team:", "The same playbook, as a studio engagement", "Each step of this case study maps to how we work with clients now.",
            wrap(playbook({"audit": "Access to your tools, every screen taken apart, and a shortlist of what to build first.",
                           "foundations": "Tokens for Figma and code, Storybook set up with your engineers, and the first components.",
                           "partner": "A contribution model, maintainers, docs and reviews, until your teams build it themselves."}, employer="CARS24"))),
]

page("cars24-internal-tools", dict(
    h1="LEGO for internal tools: one system, 30+ tools",
    lede="How CARS24 audited 20+ data-heavy tools, built tokens and Storybook with engineers new to design systems, and set up a contribution model, in about four months.",
    meta=[("Role", "Design Systems Lead, CARS24"), ("Users", "Employees, dealers and partners"), ("Platform", "Web, desktop-first"), ("Timeline", "2025, 3–4 months to beta")],
    proof=[("", "30", "+", "internal tools on one system"), ("", "20", "+", "tools audited, screen by screen"), ("", "93", "", "component sets in Figma"), ("", "1205", "", "variants, every state drawn")],
    cover_alt="The CARS24 internal tools design system: a lead dashboard, a column filter, a brand token and buttons, on mint",
    sections=S,
    credits="Aniket Pandey led this as Design Systems Lead at CARS24 (2025), with a system designer, a squad of eight engineers and two engineering maintainers. This is employee work, not Layer One client work. Screens and component sheets belong to CARS24 and are shown for portfolio purposes. The Storybook panel, the table and the token tools are recreated in code from the Figma values; the table data is made up and the timeline is approximate.",
))
