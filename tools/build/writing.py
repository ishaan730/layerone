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
    h = head(f'{a["title"]} | Layer One', H.escape(a["desc"], quote=True), depth=depth, og=a["cover"])
    h = h.replace('<meta property="og:type" content="website">',
                  f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{a["date"]}">'
                  f'\n<meta property="article:modified_time" content="{a.get("updated", a["date"])}">\n<meta property="article:author" content="{AUTHOR}">'
                  f'\n<meta property="article:section" content="{TOPIC[a["topic"]][0]}">')
    return h.replace("</head>", ld(a) + "\n</head>", 1)


def build_article(a):
    p = "../"
    s = series_of(a["slug"])
    series_pill = ""
    series_nav = ""
    if s:
        i = s[3].index(a["slug"])
        series_pill = f'<a class="post-series" href="{p}writing.html#{s[0]}"><b>{s[1]}</b>&nbsp;· Part {i + 1} of {len(s[3])}</a>'
        prv = BY[s[3][i - 1]] if i > 0 else None
        nxt = BY[s[3][i + 1]] if i + 1 < len(s[3]) else None
        cells = ""
        cells += (f'<a class="sn-prev" href="{prv["slug"]}.html"><span>Previous in {s[1]}</span><b>{short_title(prv)}</b></a>' if prv else "<span></span>")
        cells += (f'<a class="sn-next" href="{nxt["slug"]}.html"><span>Next in {s[1]}</span><b>{short_title(nxt)}</b></a>' if nxt else
                  f'<a class="sn-next" href="{p}writing.html#series"><span>You finished {s[1]}</span><b>Pick another series</b></a>')
        series_nav = f'<nav class="series-nav" aria-label="{s[1]} series">{cells}</nav>'
    head_t, text, btns = CTAS[a["cta"]]
    btn_html = "".join(f'<a class="pill{" pill--accent" if acc else ""}" href="{h if h.startswith("http") else p + h}"{" target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) if h.startswith("http") else ""}>{t}</a>' for t, h, acc in btns)
    rel = "".join(card(BY[r], p) for r in a["related"][:2])
    toc_inline = "".join(f'<li><a href="#{i}">{t}</a></li>' for t, i in a["toc"])
    upd = f' · Updated {nice_date(a["updated"])}' if a.get("updated") else ""
    content = f'''
<article class="post">
  <header class="post-head">
    <p class="crumb small muted"><a href="{p}writing.html">Writing</a> / <a href="{p}writing/topics/{a["topic"]}.html">{TOPIC[a["topic"]][0]}</a></p>
    {series_pill}
    <h1 class="post-title">{a["h1"]}</h1>
    <p class="post-dek">{a["dek"]}</p>
    <div class="post-meta"><img src="{p}assets/studio/aniket.jpg" alt="" width="40" height="40" loading="lazy"><div><b>By {AUTHOR}</b><span>{a["minutes"]} min read · Published {nice_date(a["date"])}{upd}</span></div></div>
    <div class="post-cover"><img src="{p}{a["cover"]}" alt="" width="1600" height="900"></div>
  </header>
  <details class="post-toc"><summary>In this article</summary><ol>{toc_inline}</ol></details>
  <div class="post-body">{a["body"]}</div>
  <aside class="post-author" aria-label="About the author">
    <img src="{p}assets/studio/aniket.jpg" alt="Aniket Pandey" width="72" height="72" loading="lazy">
    <div><b>{AUTHOR}</b><p>Founder of Layer One, a design systems studio in Bangalore. Built and ran design systems as an employee at <a href="{p}experience.html">CARS24, IBM and JPMorgan Chase</a>: tokens, components, governance and the teams behind them. <a href="{p}studio.html">More about the studio</a>.</p></div>
  </aside>
  <aside class="post-cta"><div><h2>{head_t}</h2><p>{text}</p></div><div class="btn-row">{btn_html}</div></aside>
  {series_nav}
  <h2 class="label">keep reading:</h2>
  <div class="cards2">{rel}</div>
</article>'''
    sub = [(t, "#" + i) for t, i in a["toc"]]
    write(f"writing/{a['slug']}.html", article_head(a, 1) + shell("writing", [("← All writing", p + "writing.html")] + sub, content, card="bar", depth=1))


def archive_rows(items, p):
    rows = ""
    for n, a in enumerate(items, 1):
        rows += (f'<tr><td class="n">{n:02d}</td><td><a href="{p}writing/{a["slug"]}.html">{short_title(a)}</a>{" <span class=" + chr(34) + "tag" + chr(34) + ">Guide</span>" if a.get("pillar") else ""}</td>'
                 f'<td class="t">{TOPIC[a["topic"]][0]}</td><td class="r">{a["minutes"]} min</td></tr>')
    return f'<div class="w-archive"><table><thead><tr><th>No.</th><th>Title</th><th class="t">Topic</th><th class="r">Length</th></tr></thead><tbody>{rows}</tbody></table></div>'


def topic_chips(p, active=None):
    counts = {k: sum(1 for a in A if a["topic"] == k) + sum(1 for m in MEDIUM_POSTS if m[2] == k) for k, _, _ in TOPICS}
    return '<ul class="w-topics">' + "".join(
        f'<li><a href="{p}writing/topics/{k}.html"{" aria-current=" + chr(34) + "page" + chr(34) if k == active else ""}>{n} <span>{counts[k]}</span></a></li>' for k, n, _ in TOPICS) + "</ul>"


def medium_cards(p, topic=None):
    return "".join(f'<a class="wcard" href="{u}" target="_blank" rel="noopener"><div class="m"><img src="{p}{img}" alt="" loading="lazy"></div><h3>{t}</h3><span>{TOPIC[k][0]} · {m} min · Medium</span></a>'
                   for u, t, k, m, img in MEDIUM_POSTS if topic in (None, k))


def build_hub():
    p = ""
    start = BY["what-is-a-design-system"]
    series = ""
    for i, (k, n, d, items) in enumerate(SERIES, 1):
        lis = "".join(f'<li><a href="writing/{s}.html"><span class="n">{j:02d}</span><b>{short_title(BY[s])}</b><span class="m">{BY[s]["minutes"]} min</span></a></li>' for j, s in enumerate(items, 1))
        series += f'<section class="w-series" id="{k}"><header><span class="w-sno">{i:02d}</span><div><h3>{n}</h3><p>{d}</p></div><span class="w-count">{len(items)} parts</span></header><ol>{lis}</ol></section>'
    pillars = "".join(card(a, p, " · Guide") for a in NEW if a.get("pillar") and a["slug"] != start["slug"])
    latest = "".join(card(a, p) for a in NEW if not a.get("pillar")) + card(BY["librarian-vs-leader"], p) + medium_cards(p)
    content = f'''
<h1 class="statement">Writing</h1>
<p class="sub muted">A practical library on building and running design systems: foundations, components, governance and the teams behind them. Written from systems built at CARS24, IBM and JPMorgan Chase, and from <a href="https://github.com/smishra280199-oss/Design-System-Handbook" target="_blank" rel="noopener">our design systems playbook</a>.</p>

<h2 class="label" id="start">start here:</h2>
<a class="w-feature" href="writing/{start["slug"]}.html">
  <div class="m"><img src="{start["cover"]}" alt="" width="1600" height="900"></div>
  <div class="w-feature-t"><span class="w-kicker">Guide · {start["minutes"]} min</span><h3>{start["h1"]}</h3><p>{start["dek"]}</p><span class="w-go">Read the guide {LONG_ARROW}</span></div>
</a>

<h2 class="label" id="topics">topics:</h2>
{topic_chips(p)}

<h2 class="label" id="series">reading series:</h2>
<p class="sub muted" style="margin-top:-6px;margin-bottom:16px">Short, ordered paths through the library. Each article stands on its own; together they build a full picture.</p>
<div class="w-series-list">{series}</div>

<h2 class="label" id="guides">the big guides:</h2>
<div class="cards2">{pillars}</div>

<h2 class="label" id="all">all articles:</h2>
<div class="cards2">{latest}</div>

<h2 class="label" id="archive">archive:</h2>
{archive_rows(NEW + [BY["librarian-vs-leader"]], p)}
'''
    sub = [("Start here", "#start"), ("Topics", "#topics"), ("Series", "#series"), ("Guides", "#guides"), ("All articles", "#all"), ("Archive", "#archive"), ("Medium", MEDIUM)]
    items = [{"@type": "ListItem", "position": i, "url": f"https://www.layerone.co.in/writing/{a['slug']}", "name": short_title(a)} for i, a in enumerate(NEW + [BY["librarian-vs-leader"]], 1)]
    ldj = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "Layer One: Writing", "url": "https://www.layerone.co.in/writing",
                      "description": "A practical library on building and running design systems.", "publisher": {"@type": "Organization", "name": "Layer One"},
                      "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False)
    h = head("Writing: design systems guides | Layer One",
             "Practical guides on design systems: what they are, tokens and colour, governance, team structure, operating models, metrics and ROI. From Layer One.")
    write("blog.html", h.replace("</head>", f'<script type="application/ld+json">{ldj}</script>\n</head>', 1)
          + shell("writing", sub, content, card="bar"))


def build_topics():
    p = "../../"
    for k, n, d in TOPICS:
        arts = [a for a in A if a["topic"] == k]
        cards = "".join(card(a, p, " · Guide" if a.get("pillar") else "") for a in arts) + medium_cards(p, k)
        guide = next((a for a in arts if a.get("pillar")), None)
        lead = (f'<p class="sub muted">Start with the guide: <a href="{p}writing/{guide["slug"]}.html">{short_title(guide)}</a>.</p>' if guide else "")
        content = f'''
<p class="crumb small muted"><a href="{p}writing.html">Writing</a> / Topics</p>
<h1 class="statement" style="margin-top:12px">{n}</h1>
<p class="sub muted">{d}</p>
{lead}
<div style="margin-top:24px">{topic_chips(p, k)}</div>
<h2 class="label">{len(arts) + sum(1 for m in MEDIUM_POSTS if m[2] == k)} articles:</h2>
<div class="cards2">{cards}</div>
{archive_rows(arts, p) if len(arts) > 2 else ""}
'''
        write(f"writing/topics/{k}.html", head(f"{n}: design systems articles | Layer One", d, depth=2)
              + shell("writing", [("← All writing", p + "writing.html")] + [(t, f"{p}writing/topics/{kk}.html") for kk, t, _ in TOPICS], content, card="bar", depth=2))


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
