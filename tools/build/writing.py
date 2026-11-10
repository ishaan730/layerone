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
THEME_JS = ("<script>try{var t=localStorage.getItem('l1-read');if(t==='dark'||t==='light')document.documentElement.dataset.read=t;"
            "else if(matchMedia('(prefers-color-scheme: dark)').matches)document.documentElement.dataset.read='dark';}catch(e){}</script>")


def reader_head(title, desc, depth, og="assets/og/layer-one.jpg", extra=""):
    """The site's <head>, switched to the reading theme: light by default, dark if the reader chose it or their system is dark."""
    h = head(title, desc, depth=depth, theme="light", og=og)
    h = h.replace('<body class="theme-light">', '<body class="reader">')
    return h.replace("</head>", THEME_JS + extra + "\n</head>", 1)


def reader_bar(p, toc=None):
    """A quiet bar: the studio's mark, a way back to the library, contents (articles only) and the theme switch."""
    toc_btn = toc_panel = ""
    if toc:
        items = "".join(f'<li><a href="#{i}">{t}</a></li>' for t, i in toc)
        toc_btn = '<button class="rd-btn" type="button" aria-expanded="false" aria-controls="rd-toc" data-rd-toc>Contents</button>'
        toc_panel = f'<nav class="rd-toc" id="rd-toc" aria-label="Contents" hidden><p>In this article</p><ol>{items}</ol></nav>'
    return f'''<header class="rd-bar"><div class="rd-bar-in">
  <a class="rd-mark" href="{p}index.html" aria-label="Layer One, home">{LOGO}<span>LAYER ONE</span></a>
  <a class="rd-lib" href="{p}writing.html">Writing</a>
  <div class="rd-tools">{toc_btn}<button class="rd-btn rd-theme" type="button" data-rd-theme aria-label="Switch between light and dark reading">{SUN}{MOON}</button></div>
</div>{toc_panel}<div class="rd-progress" aria-hidden="true"><span></span></div></header>
'''


def reader_foot(p):
    return f'''<footer class="rd-foot"><div class="rd-foot-in">
  <a class="rd-mark" href="{p}index.html">{LOGO}<span>LAYER ONE</span></a>
  <p>A design systems studio in Bangalore, India. Led by Aniket Pandey.</p>
  <nav aria-label="Studio"><a href="{p}work.html">Work</a><a href="{p}pricing.html">Pricing</a><a href="{p}lab.html">Lab</a><a href="{p}contact.html">Contact</a><a href="{MEDIUM}" target="_blank" rel="noopener">Medium</a></nav>
</div></footer>
<script src="{p}assets/site.js?v={ver("assets/site.js")}" defer></script>
</body>
</html>
'''


NUDGE = {
    "audit": ("Working on this in your own product?", "Layer One helps product teams build and run design systems. Most teams start with a two-week audit: every style, component and token you have, checked and ranked. $1,500, fixed.", "See how an audit works", "pricing.html"),
    "lab": ("Want to try this on your own values?", "The Lab is a set of free tools we use ourselves: OKLCH palettes, contrast checks, type and spacing scales, a token name linter and an export kit.", "Open the Lab", "lab.html"),
    "call": ("Thinking about how your system is run?", "Layer One helps teams set up the people and process side of design systems. A thirty-minute call is a good place to start, with no pitch.", "Book a call", CAL),
    "next": ("When you're ready to look at your own product", "Layer One helps product teams build and run design systems. Most start with a two-week audit that ends in a ranked plan. $1,500, fixed.", "See how an audit works", "pricing.html"),
}


def build_article(a):
    p = "../"
    s = series_of(a["slug"])
    kicker = f'<a href="{p}writing/topics/{a["topic"]}.html">{TOPIC[a["topic"]][0]}</a>'
    nxt_html = ""
    if s:
        i = s[3].index(a["slug"])
        kicker += f'<span>Part {i + 1} of {len(s[3])} in <a href="{p}writing.html#{s[0]}">{s[1]}</a></span>'
        nxt = BY[s[3][i + 1]] if i + 1 < len(s[3]) else None
        if nxt:
            nxt_html = (f'<a class="rd-next" href="{nxt["slug"]}.html"><span>Next in {s[1]}</span><b>{short_title(nxt)}</b>'
                        f'<em>{nxt["minutes"]} min read</em></a>')
    if not nxt_html:
        r = BY[a["related"][0]]
        nxt_html = (f'<a class="rd-next" href="{r["slug"]}.html"><span>Read next</span><b>{short_title(r)}</b>'
                    f'<em>{r["minutes"]} min read</em></a>')
    more = "".join(f'<li><a href="{BY[r]["slug"]}.html"><b>{short_title(BY[r])}</b><span>{TOPIC[BY[r]["topic"]][0]} · {BY[r]["minutes"]} min</span></a></li>'
                   for r in a["related"][1:3])
    nh, nt, nl, nu = NUDGE[a["cta"]]
    ext = nu.startswith("http")
    nhref = nu if ext else p + nu
    nattr = ' target="_blank" rel="noopener"' if ext else ""
    upd = f' · Updated {nice_date(a["updated"])}' if a.get("updated") else ""
    content = f'''<main id="main" class="rd">
<article class="rd-article">
  <header class="rd-head rd-grid">
    <p class="rd-kicker">{kicker}</p>
    <h1 class="rd-title">{a["h1"]}</h1>
    <p class="rd-dek">{a["dek"]}</p>
    <p class="rd-meta"><img src="{p}assets/studio/aniket.jpg" alt="" width="32" height="32"><span>{AUTHOR}</span><span>{a["minutes"]} min read</span><span>{nice_date(a["date"])}{upd}</span></p>
    <figure class="rd-cover"><img src="{p}{a["cover"]}" alt="" width="1600" height="900"></figure>
  </header>
  <div class="rd-body rd-grid post-body">{a["body"]}</div>
  <footer class="rd-end rd-grid">
    <p class="rd-fin" aria-hidden="true">{LOGO}</p>
    <div class="rd-author"><img src="{p}assets/studio/aniket.jpg" alt="" width="48" height="48" loading="lazy"><p>Written by <b>{AUTHOR}</b>, founder of Layer One. He has built and run design systems as an employee at <a href="{p}experience.html">CARS24, IBM and JPMorgan Chase</a>.</p></div>
    {nxt_html}
    <ul class="rd-more">{more}</ul>
    <aside class="rd-nudge" aria-label="About Layer One"><p class="rd-nudge-k">From Layer One</p><h2>{nh}</h2><p>{nt}</p><a href="{nhref}"{nattr}>{nl} {ARROW}</a></aside>
  </footer>
</article>
</main>'''
    write(f"writing/{a['slug']}.html", article_head(a, 1) + content.join([reader_bar(p, a["toc"]), reader_foot(p)]))


def row(a, p, ext=None):
    """One entry in the article list: a small cover, the title, one line of summary, topic and length."""
    if ext:
        u, t, k, m, img = ext
        return (f'<li data-topic="{k}"><a href="{u}" target="_blank" rel="noopener"><span class="rd-thumb"><img src="{p}{img}" alt="" loading="lazy"></span>'
                f'<span class="rd-row-t"><b>{t}</b><span class="rd-row-m">{TOPIC[k][0]} · {m} min · on Medium ↗</span></span></a></li>')
    return (f'<li data-topic="{a["topic"]}"><a href="{p}writing/{a["slug"]}.html"><span class="rd-thumb"><img src="{p}{a["cover"]}" alt="" loading="lazy" width="1600" height="900"></span>'
            f'<span class="rd-row-t"><b>{short_title(a)}</b><span class="rd-row-d">{a["desc"]}</span>'
            f'<span class="rd-row-m">{TOPIC[a["topic"]][0]} · {a["minutes"]} min{" · Guide" if a.get("pillar") else ""}</span></span></a></li>')


def path_title(a):
    """The shortest honest name for an article, for compact lists: the H1 up to its first colon or question mark."""
    t = a["h1"]
    for sep in ("? ", ": ", " ("):
        if sep in t:
            t = t.split(sep)[0] + ("?" if sep == "? " else "")
    return t


def topic_links(p, active=None):
    allc = len(A) + len(MEDIUM_POSTS)
    out = f'<a href="{p}writing.html#articles"{" aria-current=" + chr(34) + "page" + chr(34) if active is None else ""}>All <span>{allc}</span></a>'
    for k, n, _ in TOPICS:
        c = sum(1 for a in A if a["topic"] == k) + sum(1 for m in MEDIUM_POSTS if m[2] == k)
        cur = ' aria-current="page"' if k == active else ""
        out += f'<a href="{p}writing/topics/{k}.html"{cur}>{n} <span>{c}</span></a>'
    return f'<nav class="rd-topics" aria-label="Topics">{out}</nav>'


def build_hub():
    p = ""
    start = BY["what-is-a-design-system"]
    paths = ""
    for i, (k, n, d, items) in enumerate(SERIES, 1):
        lis = "".join(f'<li><a href="writing/{s}.html">{path_title(BY[s])}</a></li>' for s in items)
        paths += f'<section class="rd-path" id="{k}"><p class="rd-path-n">{i:02d}</p><h3>{n}</h3><p>{d}</p><ol>{lis}</ol></section>'
    order = [a for a in NEW if a is not start] + [BY["librarian-vs-leader"]]
    rows = "".join(row(a, p) for a in order) + "".join(row(None, p, m) for m in MEDIUM_POSTS)
    content = f'''<main id="main" class="rd rd-hub">
  <header class="rd-hub-head">
    <p class="rd-kicker">Writing</p>
    <h1>Notes on building and running design systems</h1>
    <p class="rd-hub-dek">Practical, plain-English guides to design systems: what they are, tokens and colour, components, governance, the teams behind them and how to tell whether it's working. From systems built at CARS24, IBM and JPMorgan Chase.</p>
  </header>
  <a class="rd-feature" href="writing/{start["slug"]}.html">
    <span class="rd-feature-m"><img src="{start["cover"]}" alt="" width="1600" height="900"></span>
    <span class="rd-feature-t"><span class="rd-kicker">Start here · {start["minutes"]} min read</span><b>{start["h1"]}</b><span>{start["dek"]}</span></span>
  </a>
  <section class="rd-sec" id="series" aria-labelledby="paths-h">
    <h2 id="paths-h">Reading paths</h2>
    <p class="rd-sec-d">Short, ordered paths through the library. Every article stands on its own.</p>
    <div class="rd-paths">{paths}</div>
  </section>
  <section class="rd-sec" id="articles" aria-labelledby="all-h">
    <h2 id="all-h">All articles</h2>
    {topic_links(p)}
    <ul class="rd-list">{rows}</ul>
  </section>
</main>'''
    items = [{"@type": "ListItem", "position": i, "url": f"https://www.layerone.co.in/writing/{a['slug']}", "name": short_title(a)} for i, a in enumerate(NEW + [BY["librarian-vs-leader"]], 1)]
    ldj = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "Layer One: Writing", "url": "https://www.layerone.co.in/writing",
                      "description": "A practical library on building and running design systems.", "publisher": {"@type": "Organization", "name": "Layer One"},
                      "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False)
    h = reader_head("Writing: design systems guides | Layer One",
                    "Practical guides on design systems: what they are, tokens and colour, governance, team structure, operating models, metrics and ROI. From Layer One.",
                    0, extra=f'<script type="application/ld+json">{ldj}</script>')
    write("blog.html", h + reader_bar(p) + content + reader_foot(p))


def build_topics():
    p = "../../"
    for k, n, d in TOPICS:
        arts = [a for a in A if a["topic"] == k]
        arts.sort(key=lambda a: not a.get("pillar"))
        rows = "".join(row(a, p) for a in arts) + "".join(row(None, p, m) for m in MEDIUM_POSTS if m[2] == k)
        content = f'''<main id="main" class="rd rd-hub">
  <header class="rd-hub-head">
    <p class="rd-kicker"><a href="{p}writing.html">Writing</a> · Topic</p>
    <h1>{n}</h1>
    <p class="rd-hub-dek">{d}</p>
  </header>
  <section class="rd-sec" aria-label="Articles">
    {topic_links(p, k)}
    <ul class="rd-list">{rows}</ul>
  </section>
</main>'''
        write(f"writing/topics/{k}.html", reader_head(f"{n}: design systems articles | Layer One", d, 2) + reader_bar(p) + content + reader_foot(p))


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
