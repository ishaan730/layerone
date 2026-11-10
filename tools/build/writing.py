"""Writing: the design systems library at /writing.

Builds
  writing.html                         the hub: start here, series, topics, every article, archive table
  writing/<slug>.html                  one page per article (body in content/writing/<slug>.html)
  writing/topics/<topic>.html          one page per topic

Article bodies are plain HTML. Every <h2> becomes an entry in the sidebar's "On this page" list, and
<!--fig:name--> placeholders are replaced by data-driven figures from writing_figs.py.
Direction for the look and voice: .claude/skills/layer-one-site/SKILL.md
"""
import html as H
import json
import re

from common import *
from writing_figs import FIGS

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content", "writing")
AUTHOR = "Aniket Pandey"
PUBLISHED = "2026-11-09"

TOPICS = [
    ("fundamentals", "Fundamentals", "What a design system is, how it differs from a UI kit or a component library, and how to tell whether you need one yet."),
    ("building", "Building a system", "Auditing what you have, choosing what to build first, and documenting it so people can use it."),
    ("foundations-and-tokens", "Foundations & tokens", "Design tokens, colour, theming and dark mode: the decisions every component is built on."),
    ("governance", "Governance", "Who decides what, how requests and contributions flow, and how to keep decisions fast and fair."),
    ("operations", "Operating model & teams", "How design systems are staffed and run day to day, from a startup's part-time owners to an enterprise team."),
    ("business-case", "Business case & measurement", "What a design system costs, what it returns, and how to measure whether it's working."),
]
TOPIC = {k: (n, d) for k, n, d in TOPICS}

SERIES = [
    ("design-systems-101", "Design Systems 101", "The basics, for anyone new to design systems.",
     ["what-is-a-design-system", "design-system-vs-style-guide-vs-component-library", "do-you-need-a-design-system"]),
    ("building-one", "Building one", "From the first audit to a documented system people can use.",
     ["how-to-build-a-design-system", "design-system-audit", "design-system-documentation"]),
    ("tokens-in-practice", "Tokens in practice", "Tokens, colour and themes, with real values you can check.",
     ["design-tokens", "oklch-color-palette", "dark-mode-design-tokens"]),
    ("the-operating-model", "The operating model", "How design systems are run after launch: teams, decisions and requests.",
     ["design-system-operating-model", "design-system-team-structure", "design-system-governance", "design-system-contribution-model"]),
    ("proving-value", "Proving value", "Metrics and money: how to show a design system is working.",
     ["design-system-metrics", "design-system-roi"]),
]

# slug, H1, <title>, meta description, topic, cover, cta, related slugs
A = [
    dict(slug="what-is-a-design-system", pillar=True, topic="fundamentals",
         h1="What is a design system? A plain-English guide for product teams",
         title="What Is a Design System? A Complete Guide with Examples",
         desc="A design system is the shared decisions, parts and agreements behind a product's UI. What's inside one, how it differs from a UI kit, when you need one.",
         dek="A design system is the set of decisions, parts and agreements a company uses to build its product's interface the same way every time. Here's what that means in practice, what's inside one, and how to tell whether you need one.",
         cta="next", related=["design-system-vs-style-guide-vs-component-library", "do-you-need-a-design-system", "how-to-build-a-design-system"]),
    dict(slug="design-system-vs-style-guide-vs-component-library", topic="fundamentals",
         h1="Design system vs style guide vs component library vs UI kit: what's the difference?",
         title="Design System vs Style Guide vs Component Library vs UI Kit",
         desc="Four terms people use interchangeably, and what each actually includes. A comparison table, a diagram of how they nest, and how to tell which one you have.",
         dek="People use these four terms as if they meant the same thing. They don't, and the difference decides what you should build next. A comparison table, a diagram of how they fit together, and a quick test to find out which one you have.",
         cta="next", related=["what-is-a-design-system", "do-you-need-a-design-system", "design-system-audit"]),
    dict(slug="do-you-need-a-design-system", topic="fundamentals",
         h1="Do you need a design system? A decision guide for startups and growing teams",
         title="Do You Need a Design System? A Decision Guide for Startups",
         desc="Seven questions, five maturity stages and the signs you've outgrown a UI kit. A practical way to decide whether your team needs a design system yet.",
         dek="Not every team needs a design system, and building one too early is an expensive way to slow down. Seven questions, five stages and a readiness checklist to tell you what you need now, and what can wait.",
         cta="audit", related=["design-system-roi", "how-to-build-a-design-system", "design-system-audit"]),
    dict(slug="how-to-build-a-design-system", pillar=True, topic="building",
         h1="How to build a design system: a step-by-step plan for the first 12 months",
         title="How to Build a Design System: A Step-by-Step Guide",
         desc="Audit, foundations, tokens, first components, docs and governance, in order. A staged 12-month plan with gates, so you invest only as fast as it pays off.",
         dek="Most guides start with colours and end with components. The systems that last start with a sponsor, a scope and a pilot. Seven steps in order, a 12-month plan, and the mistakes that sink most first attempts.",
         cta="audit", related=["design-system-audit", "design-tokens", "design-system-documentation"]),
    dict(slug="design-system-audit", topic="building",
         h1="How to run a design system audit (with an interface inventory method)",
         title="Design System Audit: How to Run an Interface Inventory",
         desc="Screenshot, group, count and prioritise every button, field and colour in your product. A step-by-step UI audit that ends in a ranked plan, not a slide.",
         dek="An audit shows you what you really have: how many buttons, how many blues, which screens drift. Done well, it ends in a ranked plan and a number leadership understands. Here's the method, step by step.",
         cta="audit", related=["how-to-build-a-design-system", "do-you-need-a-design-system", "design-system-roi"]),
    dict(slug="design-tokens", pillar=True, topic="foundations-and-tokens",
         h1="Design tokens: the complete guide to primitive, semantic and component tokens",
         title="Design Tokens: The Complete Guide (Primitive to Semantic)",
         desc="What design tokens are, the three tiers, naming, the DTCG 2025.10 format and how tokens reach code. Examples and JSON you can adapt for your system.",
         dek="Design tokens are named design decisions, stored once and used everywhere: in Figma, in code, on every platform. The three tiers, how to name them, the stable DTCG format and how tokens travel from a design file to production.",
         cta="lab", related=["oklch-color-palette", "dark-mode-design-tokens", "design-system-governance"]),
    dict(slug="dark-mode-design-tokens", topic="foundations-and-tokens",
         h1="Dark mode with design tokens: a step-by-step guide using semantic tokens",
         title="Dark Mode Design Tokens: A Step-by-Step Guide",
         desc="Build dark mode by swapping semantic tokens, not redesigning screens. A worked example with checked contrast ratios, naming rules and the common traps.",
         dek="Dark mode isn't a second design. It's a second set of answers to the same questions: what's the background, what's the text, what's the action? Set those answers up as semantic tokens and the whole product switches at once.",
         cta="lab", related=["design-tokens", "oklch-color-palette", "design-system-documentation"]),
    dict(slug="oklch-color-palette", topic="foundations-and-tokens",
         h1="How to build an accessible colour palette in OKLCH",
         title="OKLCH Color Palette: Build Accessible Design System Colors",
         desc="Why OKLCH beats HSL for UI colour, and how to build even, accessible ramps step by step. With a computed palette and contrast numbers you can check.",
         dek="HSL promises that colours with the same lightness look equally light. They don't, and that's why so many palettes fail contrast checks. OKLCH fixes it. A method for building even, accessible ramps, with every number computed.",
         cta="lab", related=["design-tokens", "dark-mode-design-tokens", "how-to-build-a-design-system"]),
    dict(slug="design-system-governance", pillar=True, topic="governance",
         h1="Design system governance: who decides what, and how",
         title="Design System Governance: Models, Roles and Process",
         desc="Governance without bureaucracy: decision rights, a lightweight review process, escalation paths and a decision log. How it should change as you grow.",
         dek="Good governance isn't a committee. It's what lets most decisions happen quickly, by the right person, without a meeting. A decision-rights matrix, processes matched to the size of the decision, an escalation path and a decision log.",
         cta="audit", related=["design-system-contribution-model", "design-system-operating-model", "design-system-team-structure"]),
    dict(slug="design-system-team-structure", topic="operations",
         h1="Design system team structure: roles, org charts and how teams grow",
         title="Design System Team Structure: Roles and Org Charts",
         desc="Who you need on a design system team, at what company size, and where they report. Org charts, a role table and the signs it's time to grow the team.",
         dek="Who actually does the work of a design system, who do they report to, and how many of them do you need? Every role, three org charts from two people to twenty, and how to run a system with no dedicated team at all.",
         cta="call", related=["design-system-operating-model", "design-system-governance", "design-system-roi"]),
    dict(slug="design-system-operating-model", pillar=True, topic="operations",
         h1="The design system operating model: how to run one at every company size",
         title="Design System Operating Model: How to Run One at Any Size",
         desc="Launch is the easy part. How design systems actually run day to day, from intake and office hours to releases and roadmaps, by company size.",
         dek="Launch is the easy part. Whether a design system thrives or fades depends on how it's run: who owns it, how work flows in and out, and how often everyone meets. The operating model, part by part, for five company sizes.",
         cta="call", related=["design-system-team-structure", "design-system-governance", "design-system-metrics"]),
    dict(slug="design-system-contribution-model", topic="governance",
         h1="Design system contribution model: how to take requests without becoming a bottleneck",
         title="Design System Contribution Model and Request Process",
         desc="A contribution model that scales: one front door, a request form, a scoring formula for priorities, contribution levels and the review flow.",
         dek="Ten teams, forty requests, one small system team. Without a clear way in, the loudest team wins and the quiet ones build their own. One front door, a scoring formula, contribution levels and a review flow that keeps work moving.",
         cta="lab", related=["design-system-governance", "design-system-operating-model", "design-system-documentation"]),
    dict(slug="design-system-documentation", topic="building",
         h1="Design system documentation: what to include, with a component page template",
         title="Design System Documentation: What to Include (Template)",
         desc="What people actually read in design system docs, the sections every component page needs and how to structure the portal. A page template to copy.",
         dek="Docs decide adoption. A component nobody can find, or can't work out how to use, doesn't exist. Who reads design system docs, what they're looking for, a component page template and how to keep it all current.",
         cta="audit", related=["design-system-contribution-model", "how-to-build-a-design-system", "design-system-metrics"]),
    dict(slug="design-system-metrics", topic="business-case",
         h1="How to measure design system success: adoption metrics and KPIs that matter",
         title="Design System Metrics: How to Measure Adoption and Success",
         desc="Which design system metrics to track at each stage: adoption, coverage, detach rate, satisfaction, time saved. With a dashboard layout and survey questions.",
         dek="A team can ship forty components in a year and still not be helping. The right measures tell you whether the system is used, whether work flows, and whether people trust it. What to track at each stage, and a one-page dashboard.",
         cta="audit", related=["design-system-roi", "design-system-operating-model", "design-system-documentation"]),
    dict(slug="design-system-roi", topic="business-case",
         h1="Design system ROI: an honest model for cost, savings and break-even",
         title="Design System ROI: Cost, Savings and an Honest Model",
         desc="What a design system really costs, where savings come from and when it pays back. A transparent model with break-even by team size and its limits.",
         dek="\"Design systems make teams 47% faster\" sounds great on a slide and falls over at the first good question. Here's a model you can defend: what a system costs, where the savings come from, and how big your team needs to be before it pays back.",
         cta="audit", related=["design-system-metrics", "do-you-need-a-design-system", "design-system-team-structure"]),
    dict(slug="librarian-vs-leader", topic="operations", legacy=True, date="2026-02-27",
         h1="Most design system leads are just librarians",
         title="Most Design System Leads Are Just Librarians",
         desc="Why maintaining a library isn't the same as leading a design system, and what leading one actually involves.",
         dek="Why maintaining a library isn't the same as leading a design system.",
         cover="assets/images/blog/librarian-vs-leader.jpg", cta="call",
         related=["design-system-operating-model", "design-system-team-structure", "design-system-governance"]),
]
BY = {a["slug"]: a for a in A}
NEW = [a for a in A if not a.get("legacy")]

MEDIUM_POSTS = [
    ("https://medium.com/@layerone_11803/design-systems-as-operational-backbones-95b782c17f71", "Design systems as operational backbones", "operations", 5, "assets/images/blog/operational-backbone.jpg"),
    ("https://medium.com/@layerone_11803/most-design-systems-are-just-expensive-ui-libraries-e0cc8b146f2d", "Most design systems are just expensive UI libraries", "fundamentals", 8, "assets/images/blog/ui-libraries.jpg"),
    ("https://medium.com/@layerone/foundations-of-modern-design-systems", "Foundations of modern design systems", "foundations-and-tokens", 5, "assets/images/blog/foundations.jpg"),
]

CTAS = {
    "audit": ("Not sure where your system stands?",
              "A two-week audit maps every style, component and token you have in Figma and code, checks accessibility, and gives you a ranked plan. $1,500, fixed.",
              [("See pricing", "pricing.html", True), ("Book a call", CAL, False)]),
    "lab": ("Try it on your own values",
            "The Lab has free tools for this: OKLCH palettes, contrast checks, type and spacing scales, a token name linter and an export kit for CSS, Tailwind and DTCG JSON.",
            [("Open the Lab", "lab.html", True), ("See pricing", "pricing.html", False)]),
    "call": ("Want to talk through your setup?",
             "Thirty minutes, no pitch: tell us how your system is run today and we'll tell you what we'd change first.",
             [("Book a call", CAL, True), ("See pricing", "pricing.html", False)]),
    "next": ("Ready for the next step?",
             "When you're ready to look at your own product, a two-week audit gives you a baseline and a ranked plan. $1,500, fixed.",
             [("See pricing", "pricing.html", True), ("Book a call", CAL, False)]),
}


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", t).lower()).strip("-")[:60]


def words(html):
    return len(re.sub(r"<[^>]+>", " ", re.sub(r"<(svg|script|style)\b.*?</\1>", " ", html, flags=re.S)).split())


def load(a):
    """Read an article body, fill figures, give every h2 an id, collect the table of contents."""
    path = os.path.join(CONTENT, a["slug"] + ".html")
    if a.get("legacy"):
        path = os.path.join(HERE, "content", "librarian-vs-leader.html")
    body = open(path).read()
    body = re.sub(r"<!--fig:([\w-]+)-->", lambda m: FIGS[m.group(1)](), body)
    toc = []

    def h2(m):
        attrs, text = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        hid = idm.group(1) if idm else slugify(text)
        toc.append((re.sub(r"<[^>]+>", "", text), hid))
        rest = re.sub(r' id="[^"]+"', "", attrs)
        return f'<h2 id="{hid}"{rest}>{text}</h2>'

    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2, body)
    a["body"], a["toc"] = body, toc
    a["minutes"] = max(3, round(words(body) / 230))
    a.setdefault("cover", f"assets/images/writing/{a['slug']}.jpg")
    a.setdefault("date", PUBLISHED)


def series_of(slug):
    for s in SERIES:
        if slug in s[3]:
            return s
    return None


def nice_date(iso):
    import datetime
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def card(a, p, extra=""):
    t = TOPIC[a["topic"]][0]
    return (f'<a class="wcard" href="{p}writing/{a["slug"]}.html"><div class="m"><img src="{p}{a["cover"]}" alt="" loading="lazy" width="1600" height="900"></div>'
            f'<h3>{short_title(a)}</h3><span>{t} · {a["minutes"]} min{extra}</span></a>')


def short_title(a):
    t = a["h1"]
    return t.split(":")[0] if ":" in t and len(t) > 62 else t


def ld(a):
    url = f"https://www.layerone.co.in/writing/{a['slug']}"
    post = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"],
            "image": f"https://www.layerone.co.in/{a['cover']}", "datePublished": a["date"], "dateModified": a.get("updated", a["date"]),
            "mainEntityOfPage": url, "wordCount": words(a["body"]), "articleSection": TOPIC[a["topic"]][0],
            "author": {"@type": "Person", "name": AUTHOR, "url": "https://www.layerone.co.in/studio", "jobTitle": "Founder, Layer One"},
            "publisher": {"@type": "Organization", "name": "Layer One", "url": "https://www.layerone.co.in/",
                          "logo": {"@type": "ImageObject", "url": "https://www.layerone.co.in/assets/og/layer-one.jpg"}}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Writing", "item": "https://www.layerone.co.in/writing"},
        {"@type": "ListItem", "position": 2, "name": TOPIC[a["topic"]][0], "item": f"https://www.layerone.co.in/writing/topics/{a['topic']}"},
        {"@type": "ListItem", "position": 3, "name": short_title(a), "item": url}]}
    return "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (post, crumbs))


def article_head(a, depth):
    h = reader_head(f'{a["title"]} | Layer One', H.escape(a["desc"], quote=True), depth, og=a["cover"])
    h = h.replace('<meta property="og:type" content="website">',
                  f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{a["date"]}">'
                  f'\n<meta property="article:modified_time" content="{a.get("updated", a["date"])}">\n<meta property="article:author" content="{AUTHOR}">'
                  f'\n<meta property="article:section" content="{TOPIC[a["topic"]][0]}">')
    return h.replace("</head>", ld(a) + "\n</head>", 1)


SUN = '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="3.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M4.2 15.8l1.5-1.5M14.3 5.7l1.5-1.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
MOON = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M16.5 12.6A6.8 6.8 0 0 1 7.4 3.5a6.8 6.8 0 1 0 9.1 9.1Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>'
# The site is dark. Readers can switch the writing pages to a light reading theme; the choice is remembered.
THEME_JS = "<script>try{if(localStorage.getItem('l1-read')==='light')document.documentElement.dataset.read='light';}catch(e){}</script>"


def reader_head(title, desc, depth, og="assets/og/layer-one.jpg", extra=""):
    """The site's own <head> and body, plus the reading-theme switch."""
    h = head(title, desc, depth=depth, og=og)
    h = h.replace('<body class="theme-dark">', '<body class="theme-dark reader">')
    return h.replace("</head>", THEME_JS + extra + "\n</head>", 1)


def theme_toggle():
    return (f'<button class="ed-theme" type="button" data-rd-theme aria-label="Switch between dark and light reading">'
            f'{SUN}{MOON}<span class="ed-theme-l">Light reading</span><span class="ed-theme-d">Dark reading</span></button>')


def page(p, depth, rail, content, active="writing"):
    """Every writing page uses the site's top navigation and its shell grid: a 300px rail on the left
    (where the home page has its sidebar) and the content column starting on the same grid line."""
    return (topbar(active, depth)
            + f'<div class="shell ed-shell"><aside class="ed-rail" aria-label="Writing">{rail}</aside>'
            + f'<main id="main" class="content ed-main">{content}</main></div>'
            + close(depth))


def meta_line(a):
    s = series_of(a["slug"])
    return f'{TOPIC[a["topic"]][0]}', f'{a["minutes"]} min read' + (" · Guide" if a.get("pillar") else "")


def ecard(a, p, size="", ext=None, eager=False):
    """The one article card used everywhere: cover, topic, title, summary, reading time."""
    lazy = "" if eager else ' loading="lazy"'
    if ext:
        u, t, k, m, img = ext
        return (f'<a class="ec {size}" href="{u}" target="_blank" rel="noopener" data-topic="{k}">'
                f'<span class="ec-m"><img src="{p}{img}" alt=""{lazy}></span>'
                f'<span class="ec-k">{TOPIC[k][0]}</span><b class="ec-t">{t}</b>'
                f'<span class="ec-f">{m} min read · on Medium ↗</span></a>')
    topic, mins = meta_line(a)
    return (f'<a class="ec {size}" href="{p}writing/{a["slug"]}.html" data-topic="{a["topic"]}">'
            f'<span class="ec-m"><img src="{p}{a["cover"]}" alt="" width="1600" height="900"{lazy}></span>'
            f'<span class="ec-k">{topic}</span><b class="ec-t">{short_title(a)}</b>'
            f'<span class="ec-d">{a["desc"]}</span><span class="ec-f">{mins}</span></a>')


def topic_nav(p, active=None, filt=False):
    """Topics in the rail. On the library page they filter the list in place; elsewhere they are links."""
    allc = len(A) + len(MEDIUM_POSTS)
    def link(href, label, count, key, cur):
        attrs = ' aria-current="page"' if cur else ""
        f = f' data-filter="{key}"' if filt else ""
        return f'<a href="{href}"{attrs}{f}><span>{label}</span><em>{count}</em></a>'
    out = link(f"{p}writing.html#articles", "All writing", allc, "all", active is None)
    for k, n, _ in TOPICS:
        c = sum(1 for a in A if a["topic"] == k) + sum(1 for m in MEDIUM_POSTS if m[2] == k)
        out += link(f"{p}writing/topics/{k}.html", n, c, k, k == active)
    return f'<p class="ed-rail-h">Topics</p><nav class="ed-topics" aria-label="Topics">{out}</nav>'


def rail_foot():
    return f'<div class="ed-rail-foot">{theme_toggle()}</div>'


NUDGE = {
    "audit": ("Working on this in your own product?", "Most teams we work with start with a two-week audit: every style, component and token, checked and ranked.", "How the audit works", "pricing.html"),
    "lab": ("Try it on your own values", "The Lab has the free tools we use ourselves: OKLCH palettes, contrast checks, scales, a token name linter and an export kit.", "Open the Lab", "lab.html"),
    "call": ("Thinking about how your system is run?", "If you'd like a second opinion on your team or process, a thirty-minute call is a good place to start.", "Book a call", CAL),
    "next": ("Looking at your own product next?", "Most teams we work with start with a two-week audit that ends in a ranked plan.", "How the audit works", "pricing.html"),
}


def build_article(a):
    p = "../"
    s = series_of(a["slug"])
    topic = TOPIC[a["topic"]][0]
    series_line = series_steps = ""
    nxt = None
    if s:
        i = s[3].index(a["slug"])
        series_line = f'<span>Part {i + 1} of {len(s[3])} · <a href="{p}writing.html#{s[0]}">{s[1]}</a></span>'
        nxt = BY[s[3][i + 1]] if i + 1 < len(s[3]) else None
        steps = "".join(
            f'<li{" aria-current=" + chr(34) + "step" + chr(34) if x == a["slug"] else ""}><a href="{x}.html">{path_title(BY[x])}</a></li>' for x in s[3])
        series_steps = f'<div class="ed-rail-sec"><p class="ed-rail-h">{s[1]}</p><ol class="ed-steps">{steps}</ol></div>'
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for t, i in a["toc"])
    rail = (f'<a class="ed-back" href="{p}writing.html">← All writing</a>'
            f'<div class="ed-rail-sec"><p class="ed-rail-h">On this page</p><nav class="ed-toc" aria-label="On this page"><ol>{toc}</ol></nav></div>'
            f'{series_steps}{rail_foot()}')
    nh, nt, nl, nu = NUDGE[a["cta"]]
    ext = nu.startswith("http")
    nattr = ' target="_blank" rel="noopener"' if ext else ""
    nhref = nu if ext else p + nu
    nexts = ([nxt] if nxt else []) + [BY[r] for r in a["related"] if not nxt or r != nxt["slug"]]
    nexts = nexts[:3]
    lead = (f'<p class="ed-end-k">{"Next in " + s[1] if nxt else "Read next"}</p>')
    cards = "".join(ecard(x, p) for x in nexts)
    upd = f' · Updated {nice_date(a["updated"])}' if a.get("updated") else ""
    mtoc = (f'<details class="ed-mtoc"><summary><span>On this page</span><b data-mtoc-current>{a["toc"][0][0] if a["toc"] else ""}</b></summary>'
            f'<ol>{toc}</ol>{theme_toggle()}</details>')
    content = f'''<article class="ed-article">
  <header class="ed-head">
    <p class="ed-kicker"><a href="{p}writing/topics/{a["topic"]}.html">{topic}</a>{series_line}</p>
    <h1 class="ed-title">{a["h1"]}</h1>
    <p class="ed-dek">{a["dek"]}</p>
    <p class="ed-byline"><img src="{p}assets/studio/aniket.jpg" alt="" width="36" height="36"><span><b>{AUTHOR}</b><span>{a["minutes"]} min read · {nice_date(a["date"])}{upd}</span></span></p>
  </header>
  {mtoc}
  <figure class="ed-cover"><img src="{p}{a["cover"]}" alt="" width="1600" height="900"></figure>
  <div class="ed-body post-body">{a["body"]}</div>
  <footer class="ed-end">
    <div class="ed-author"><img src="{p}assets/studio/aniket.jpg" alt="" width="56" height="56" loading="lazy"><p><b>{AUTHOR}</b> is the founder of Layer One. He has built and run design systems as an employee at <a href="{p}experience.html">CARS24, IBM and JPMorgan Chase</a>.</p></div>
    {lead}
    <div class="ec-grid ec-grid--3">{cards}</div>
    <aside class="ed-note" aria-label="From Layer One"><div><p class="ed-note-k">From Layer One</p><h2>{nh}</h2><p>{nt}</p></div><a href="{nhref}"{nattr}>{nl} {ARROW}</a></aside>
  </footer>
</article>
<div class="ed-progress" aria-hidden="true"><span></span></div>'''
    write(f"writing/{a['slug']}.html", article_head(a, 1) + page(p, 1, rail, content))


def path_title(a):
    """The shortest honest name for an article, for compact lists: the H1 up to its first colon or question mark."""
    t = a["h1"]
    for sep in ("? ", ": ", " ("):
        if sep in t:
            t = t.split(sep)[0] + ("?" if sep == "? " else "")
    return t


def paths_html(p):
    out = ""
    for i, (k, n, d, items) in enumerate(SERIES, 1):
        mins = sum(BY[s]["minutes"] for s in items)
        steps = "".join(f'<li><a href="{p}writing/{s}.html"><span class="ep-n">{j}</span><b>{path_title(BY[s])}</b><em>{BY[s]["minutes"]} min</em></a></li>'
                        for j, s in enumerate(items, 1))
        out += (f'<section class="ep" id="{k}"><header class="ep-h"><span class="ep-no">Path {i:02d}</span><h3>{n}</h3><p>{d}</p>'
                f'<span class="ep-meta">{len(items)} articles · {mins} min</span>'
                f'<a class="ep-start" href="{p}writing/{items[0]}.html">Start the path {ARROW}</a></header><ol class="ep-steps">{steps}</ol></section>')
    return out


def build_hub():
    p = ""
    lead = BY["what-is-a-design-system"]
    second = [BY["design-system-operating-model"], BY["design-tokens"]]
    shown = {lead["slug"]} | {x["slug"] for x in second}
    rest = [a for a in NEW if a["slug"] not in shown] + [BY["librarian-vs-leader"]]
    cards = "".join(ecard(a, p) for a in rest) + "".join(ecard(None, p, ext=m) for m in MEDIUM_POSTS)
    topics = "".join(
        f'<a class="et" href="writing/topics/{k}.html"><b>{n}</b><span>{d}</span><em>{sum(1 for a in A if a["topic"] == k) + sum(1 for m in MEDIUM_POSTS if m[2] == k)} articles</em></a>'
        for k, n, d in TOPICS)
    content = f'''<header class="ed-intro">
  <p class="ed-kicker"><span>Writing</span></p>
  <h1>Field notes on design systems</h1>
  <p>How design systems are built, run and measured: tokens and components, governance and teams, and what actually changes once a system is in use. From work at CARS24, IBM and JPMorgan Chase.</p>
  <p class="ed-intro-n"><span>{len(A) + len(MEDIUM_POSTS)} articles</span><span>{len(SERIES)} reading paths</span><span>{len(TOPICS)} topics</span></p>
</header>

<section class="ed-sec ed-sec--first" aria-labelledby="featured-h">
  <h2 class="ed-sec-h" id="featured-h">featured:</h2>
  <div class="ed-featured">
    {ecard(lead, p, "ec--lead", eager=True)}
    <div class="ed-featured-side">{"".join(ecard(x, p, "ec--side", eager=True) for x in second)}</div>
  </div>
</section>

<section class="ed-sec" id="articles" aria-labelledby="latest-h">
  <div class="ed-sec-row"><h2 class="ed-sec-h" id="latest-h">latest articles:</h2><p class="ed-filter-state" data-filter-state aria-live="polite"></p></div>
  <div class="ec-grid ec-grid--latest" data-filter-list>{cards}</div>
</section>

<section class="ed-sec" id="series" aria-labelledby="paths-h">
  <div class="ed-sec-intro"><h2 class="ed-sec-h" id="paths-h">reading paths:</h2><p>Curated sequences for learning a subject from the start. Read them in order; each article still stands on its own.</p></div>
  <div class="ep-list">{paths_html(p)}</div>
</section>

<section class="ed-sec" id="topics" aria-labelledby="topics-h">
  <h2 class="ed-sec-h" id="topics-h">explore by topic:</h2>
  <div class="et-grid">{topics}</div>
  <p class="ed-also">Older essays are on <a href="{MEDIUM}" target="_blank" rel="noopener">Medium</a>.</p>
</section>'''
    rail = topic_nav(p, filt=True) + '<div class="ed-rail-sec"><p class="ed-rail-h">On this page</p><nav class="ed-toc ed-toc--static"><ol><li><a href="#featured-h">Featured</a></li><li><a href="#articles">Latest articles</a></li><li><a href="#series">Reading paths</a></li><li><a href="#topics">Explore by topic</a></li></ol></nav></div>' + rail_foot()
    items = [{"@type": "ListItem", "position": i, "url": f"https://www.layerone.co.in/writing/{a['slug']}", "name": short_title(a)} for i, a in enumerate(NEW + [BY["librarian-vs-leader"]], 1)]
    ldj = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "Layer One: Writing", "url": "https://www.layerone.co.in/writing",
                      "description": "A practical library on building and running design systems.", "publisher": {"@type": "Organization", "name": "Layer One"},
                      "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False)
    h = reader_head("Writing: design systems guides | Layer One",
                    "Practical guides on design systems: what they are, tokens and colour, governance, team structure, operating models, metrics and ROI. From Layer One.",
                    0, extra=f'<script type="application/ld+json">{ldj}</script>')
    write("blog.html", h + page(p, 0, rail, content))


def build_topics():
    p = "../../"
    for k, n, d in TOPICS:
        arts = [a for a in A if a["topic"] == k]
        arts.sort(key=lambda a: not a.get("pillar"))
        cards = "".join(ecard(a, p) for a in arts) + "".join(ecard(None, p, ext=m) for m in MEDIUM_POSTS if m[2] == k)
        content = f'''<header class="ed-intro ed-intro--topic">
  <p class="ed-kicker"><a href="{p}writing.html">Writing</a><span>Topic</span></p>
  <h1>{n}</h1>
  <p>{d}</p>
</header>
<section class="ed-sec ed-sec--first" aria-label="Articles"><div class="ec-grid">{cards}</div></section>'''
        rail = f'<a class="ed-back" href="{p}writing.html">← All writing</a>' + topic_nav(p, k) + rail_foot()
        write(f"writing/topics/{k}.html", reader_head(f"{n}: design systems articles | Layer One", d, 2) + page(p, 2, rail, content))


def _exists(a):
    return a.get("legacy") or os.path.exists(os.path.join(CONTENT, a["slug"] + ".html"))


if __name__ == "__main__":
    missing = [a["slug"] for a in A if not _exists(a)]
    if missing:
        print("writing: no body yet for", ", ".join(missing))
        A[:] = [a for a in A if _exists(a)]
        NEW[:] = [a for a in NEW if _exists(a)]
        SERIES[:] = [(k, n, d, [s for s in items if s in {x["slug"] for x in A}]) for k, n, d, items in SERIES]
        SERIES[:] = [s for s in SERIES if s[3]]
        for a in A:
            a["related"] = [r for r in a["related"] if r in {x["slug"] for x in A}] or [x["slug"] for x in NEW if x is not a][:2]
    for a in A:
        load(a)
    for a in A:
        build_article(a)
    build_hub()
    build_topics()
