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
     ["what-is-a-design-system", "design-system-vs-style-guide-vs-component-library", "do-you-need-a-design-system", "design-system-maturity-model"]),
    ("building-one", "Building one", "From the first audit to a documented system people can use.",
     ["how-to-build-a-design-system", "design-system-audit", "design-system-documentation"]),
    ("tokens-in-practice", "Tokens in practice", "Tokens, colour and themes, with real values you can check.",
     ["design-tokens", "design-token-naming-conventions", "oklch-color-palette", "dark-mode-design-tokens", "multi-brand-design-system"]),
    ("foundations-in-depth", "Foundations in depth", "Spacing, type, contrast and layout: the decisions every screen inherits.",
     ["spacing-system-4px-vs-8px", "type-scale-design-system", "color-contrast-design-system", "layout-grid-breakpoints"]),
    ("components-in-depth", "Components in depth", "Choosing, scoping and shaping the components teams build with.",
     ["which-components-to-build-first", "headless-component-library-build-vs-buy", "component-complexity", "component-props-best-practices"]),
    ("the-operating-model", "The operating model", "How design systems are run after launch: teams, decisions and requests.",
     ["design-system-operating-model", "design-system-team-structure", "design-system-governance", "design-system-contribution-model"]),
    ("running-it-day-to-day", "Running it day to day", "The rituals that keep a system trusted: help, releases, change and community.",
     ["design-system-office-hours", "design-system-release-notes", "design-system-versioning", "design-system-champions"]),
    ("patterns-and-content", "Patterns and content", "How components combine, what the words say, and getting ready for other languages.",
     ["design-system-patterns", "form-design-patterns", "ux-writing-design-system", "design-system-localization-rtl"]),
    ("tools-and-twins", "Tools and twins", "Keeping Figma and code identical, the toolchain behind them, and where AI helps.",
     ["figma-code-sync", "design-system-tooling", "ai-in-design-systems"]),
    ("growing-adoption", "Growing adoption", "Teaching the system, listening to the people who use it, and bringing older products along.",
     ["design-system-onboarding", "design-system-research", "design-system-migration"]),
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
    dict(slug="design-system-maturity-model", date="2026-11-11", topic="fundamentals",
         h1="The design system maturity model: five stages, and how to move up one",
         title="Design System Maturity Model: 5 Stages and How to Progress",
         desc="Five stages of design system maturity, how to tell which one you're at, what the next step takes, and why aiming for the top too early backfires.",
         dek="Design systems grow in stages, like a staircase. The most useful thing you can do is work out which step you're on and aim for the next one, not the top. Five stages, the signs of each, and what it takes to move up.",
         cta="audit", related=["do-you-need-a-design-system", "how-to-build-a-design-system", "design-system-metrics"]),
    dict(slug="design-system-versioning", date="2026-11-11", topic="governance",
         h1="Design system versioning: semantic versions, breaking changes and deprecation",
         title="Design System Versioning and Breaking Changes, Explained",
         desc="How to version a design system so updates don't break products: what counts as breaking, visual breaking changes, deprecation and migration.",
         dek="Nothing in the code broke, but three products did. Design system releases can break screens through a padding tweak as easily as a renamed prop. How to number versions, decide what's breaking, and retire things without surprising anyone.",
         cta="call", related=["design-system-release-notes", "design-system-governance", "component-props-best-practices"]),
    dict(slug="design-token-naming-conventions", date="2026-11-11", topic="foundations-and-tokens",
         h1="Design token naming conventions: a structure people can guess",
         title="Design Token Naming Conventions: Structure and Examples",
         desc="How to name design tokens so people can guess them: the parts of a name, primitive, semantic and component patterns, common mistakes and a checklist.",
         dek="Token names are an interface people type hundreds of times a day. A good naming structure lets someone guess the right name without looking it up. The parts of a name, patterns for each tier, and the mistakes that make tokens hard to use.",
         cta="lab", related=["design-tokens", "multi-brand-design-system", "component-props-best-practices"]),
    dict(slug="spacing-system-4px-vs-8px", date="2026-11-11", topic="foundations-and-tokens",
         h1="Spacing systems: 4px vs 8px, the scale, and how to use it",
         title="Spacing System Design: 4px vs 8px Grid and Scale",
         desc="How to build a spacing system: choosing a 4px or 8px base, a spacing scale, inset, stack and inline space, density modes and responsive spacing.",
         dek="Spacing is the foundation people notice least and feel most. Choose a base unit, build a short scale, and give space a few clear jobs, and screens stop feeling slightly off. How to choose between 4px and 8px, and how to use the scale.",
         cta="lab", related=["type-scale-design-system", "design-tokens", "color-contrast-design-system"]),
    dict(slug="type-scale-design-system", date="2026-11-11", topic="foundations-and-tokens",
         h1="How to build a type scale for a design system",
         title="Type Scale for Design Systems: How to Build One",
         desc="How to build a type scale: choosing a base and ratio, line height and letter spacing, naming text styles by role, fluid type and accessibility.",
         dek="If anyone can pick any text size, you end up with 13, 14, 14.5 and 15 pixels and nothing looks related. A type scale is a short list of sizes everyone chooses from. How to build one that suits product screens, name it, and keep it accessible.",
         cta="lab", related=["spacing-system-4px-vs-8px", "color-contrast-design-system", "design-tokens"]),
    dict(slug="color-contrast-design-system", date="2026-11-11", topic="foundations-and-tokens",
         h1="Colour contrast in design systems: WCAG ratios and pairing rules",
         title="Color Contrast for Design Systems: WCAG Rules That Scale",
         desc="How to build colour contrast into a design system: WCAG 2.2 ratios, checking pairs not colours, a contrast matrix, pairing rules by step, and APCA.",
         dek="Contrast is decided once in a design system and inherited everywhere, which makes it the cheapest place to get accessibility right. The WCAG ratios that matter, why you check pairs and not colours, and simple pairing rules that hold across a palette.",
         cta="lab", related=["oklch-color-palette", "dark-mode-design-tokens", "type-scale-design-system"]),
    dict(slug="multi-brand-design-system", date="2026-11-11", topic="foundations-and-tokens",
         h1="Multi-brand design systems: one core, many brands",
         title="Multi-Brand Design Systems: Share the Core, Vary the Brand",
         desc="How to support several brands, platforms and products from one design system: what to share, what to vary, brand tokens and families of systems.",
         dek="Three brands, three design teams, three date pickers. Scaling a design system means deciding what should be the same everywhere and what should be free to differ. What to share, what to vary, and when one system becomes a family.",
         cta="call", related=["dark-mode-design-tokens", "design-token-naming-conventions", "design-system-governance"]),
    dict(slug="which-components-to-build-first", date="2026-11-11", topic="building",
         h1="Which components to build first: a prioritisation method",
         title="Which Design System Components to Build First",
         desc="How to choose your first design system components: count frequency and trouble, plot a 2×2, pick a pilot, and the eight components most teams start with.",
         dek="Don't start with the component that's most fun to design, or the one that looks like the biggest problem. Start with the ones used everywhere and inconsistent today. A method for choosing, ranking and scheduling your first components.",
         cta="audit", related=["design-system-audit", "component-complexity", "headless-component-library-build-vs-buy"]),
    dict(slug="headless-component-library-build-vs-buy", date="2026-11-11", topic="building",
         h1="Build, borrow or buy: headless component libraries vs building your own",
         title="Headless UI Libraries vs Building Your Own Components",
         desc="Should you build design system components, use a headless library or theme a styled one? Trade-offs, a decision table and what we usually recommend.",
         dek="You don't have to build every component from scratch. Headless libraries handle the hard part, behaviour and accessibility, and leave the look to you. When to build, when to borrow, when to buy, and how to keep the choice reversible.",
         cta="audit", related=["which-components-to-build-first", "component-complexity", "component-props-best-practices"]),
    dict(slug="component-complexity", date="2026-11-11", topic="building",
         h1="Component complexity: how to estimate design system work",
         title="Component Complexity: Estimating Design System Work",
         desc="A scoring method for design system components: four levels of complexity, an eight-question rubric, and how complexity changes process and effort.",
         dek="A badge and a data table are both \"one component\", and planning them the same way guarantees missed dates. Four levels of complexity, an eight-question scoring method, and how to match the process to each level.",
         cta="audit", related=["which-components-to-build-first", "component-props-best-practices", "design-system-contribution-model"]),
    dict(slug="component-props-best-practices", date="2026-11-11", topic="building",
         h1="Component props best practices: designing APIs people can use",
         title="Component Props Best Practices for Design Systems",
         desc="How to design component props: the eight kinds of props, rules for good APIs, controlled vs uncontrolled, and keeping props in step between Figma and code.",
         dek="Props are a promise. They're the interface designers and engineers use every day, and once teams depend on one, changing it breaks their screens. The kinds of props, the rules we review them against, and how to keep Figma and code saying the same thing.",
         cta="audit", related=["component-complexity", "design-system-versioning", "design-token-naming-conventions"]),
    dict(slug="design-system-office-hours", date="2026-11-11", topic="operations",
         h1="How to run design system office hours people actually use",
         title="Design System Office Hours: How to Run Them Well",
         desc="How to run design system office hours: format, hosts, outputs, timing across time zones, and what to do when nobody turns up.",
         dek="Office hours are the single most effective routine a design system team can run: cheap, relationship-building and free research every week. Many teams start them, see three people arrive and quietly stop. The details that make the difference.",
         cta="call", related=["design-system-champions", "design-system-operating-model", "design-system-release-notes"]),
    dict(slug="design-system-release-notes", date="2026-11-11", topic="operations",
         h1="Design system release notes and announcements: templates you can copy",
         title="Design System Release Notes: Templates and Examples",
         desc="How to announce design system changes: channels, timing, and copyable templates for releases, breaking changes, deprecations, token updates and digests.",
         dek="Release notes are a design system's most-read documentation, and most are written for the people who built the change rather than the people who need it. Channels, timing and five templates you can copy.",
         cta="call", related=["design-system-versioning", "design-system-office-hours", "design-system-documentation"]),
    dict(slug="design-system-champions", date="2026-11-11", topic="operations",
         h1="Design system champions: building a community that multiplies the team",
         title="Design System Champions Programme and Community Guide",
         desc="How to run a design system champions programme and community: what champions do, time and recognition, community sessions and working groups.",
         dek="Five people can't serve two hundred. A community doesn't replace the system team, it multiplies it. How to set up a champions network, the community rituals worth running, and the two things that make or break it.",
         cta="call", related=["design-system-office-hours", "design-system-team-structure", "design-system-operating-model"]),
    dict(slug="ai-in-design-systems", date="2026-11-11", topic="building",
         h1="AI in design systems: where it helps, and where to keep a human",
         title="AI in Design Systems: Practical Uses and Cautions",
         desc="Where AI genuinely helps design system teams today (docs, release notes, checks, migrations) and the cautions that matter when mistakes spread to every product.",
         dek="AI tools are changing design system work quickly, and it's easy to overhype or dismiss them. A grounded view: where they help today, where a human must stay in the loop, and why a well-structured system is the best preparation for using AI well.",
         cta="call", related=["design-system-documentation", "design-system-release-notes", "design-token-naming-conventions"]),
    dict(slug="design-system-patterns", date="2026-11-12", topic="building",
         h1="Design system patterns: when components aren't enough",
         title="Design System Patterns: Beyond Components",
         desc="What design system patterns are, how they differ from components, the four pattern families to start with, and a template for documenting them.",
         dek="Every team uses the same button, field and table, and the product still feels like five products. Components are the words; patterns are the sentences. What patterns are, which ones to write down first, and how to document them.",
         cta="audit", related=["form-design-patterns", "ux-writing-design-system", "design-system-documentation"]),
    dict(slug="form-design-patterns", date="2026-11-12", topic="building",
         h1="Form design patterns: layout, validation and error messages",
         title="Form Design Patterns: Validation and Error Messages",
         desc="Seven form decisions a design system should make once: layout, required fields, when to validate, where errors go, what they say, long forms and buttons.",
         dek="Forms are where products make money and where people get most frustrated. Seven decisions every form shares, the validation timeline we start from, and how to write error messages people can act on.",
         cta="audit", related=["design-system-patterns", "ux-writing-design-system", "color-contrast-design-system"]),
    dict(slug="ux-writing-design-system", date="2026-11-12", topic="building",
         h1="Content design in a design system: voice, vocabulary and message formulas",
         title="UX Writing in Design Systems: Voice and Vocabulary",
         desc="How to put words into a design system: voice and tone, a shared vocabulary, formulas for buttons, errors and empty states, and writing for everyone.",
         dek="A product can have perfectly consistent buttons and still feel chaotic if one says \"Remove\", another \"Delete\" and a third \"Discard\" for the same action. Words are part of the interface, so they belong in the system too.",
         cta="call", related=["form-design-patterns", "design-system-localization-rtl", "design-system-patterns"]),
    dict(slug="layout-grid-breakpoints", date="2026-11-12", topic="foundations-and-tokens",
         h1="Layout grids and breakpoints for product UI",
         title="Layout Grid and Breakpoints for Design Systems",
         desc="How to set up a layout grid for product UI: columns, gutters and margins, choosing breakpoints, named content widths, dashboards and layout tokens.",
         dek="Columns, gutters, margins and the widths where layouts change, with real numbers from Material 3 and IBM Carbon. How to choose your own, lay out a dashboard, and store it all as tokens so design and code agree.",
         cta="lab", related=["spacing-system-4px-vs-8px", "design-tokens", "design-system-localization-rtl"]),
    dict(slug="design-system-localization-rtl", date="2026-11-12", topic="foundations-and-tokens",
         h1="Localisation and right-to-left in a design system",
         title="Design System Localization and RTL Support",
         desc="Getting a design system ready for other languages: logical CSS, right-to-left mirroring, text that grows, plurals, locale formats and testing.",
         dek="Translation breaks shared parts first: buttons that can't fit longer labels, icons that point the wrong way, dates written by hand. Six habits that make a system ready for other languages, even if you only support one today.",
         cta="audit", related=["layout-grid-breakpoints", "ux-writing-design-system", "multi-brand-design-system"]),
    dict(slug="figma-code-sync", date="2026-11-12", topic="building",
         h1="Keeping Figma and code in sync: five habits that stop drift",
         title="Keeping Figma and Code in Sync in a Design System",
         desc="How to stop Figma and code drifting apart: one vocabulary, one token source, a shared definition of done, a monthly twin check and links between them.",
         dek="Every component has two twins, one in Figma and one in code, and they drift unless someone works at keeping them identical. Five habits that do most of the work, and how to read the trail the twins leave.",
         cta="audit", related=["component-props-best-practices", "design-system-tooling", "design-tokens"]),
    dict(slug="design-system-tooling", date="2026-11-12", topic="building",
         h1="Design system tools by stage: what you need, and what to automate first",
         title="Design System Tools and Automation by Stage",
         desc="The design system toolchain mapped: design, tokens, code, docs, quality and insight. The minimum tools for each stage, and what to automate first.",
         dek="Tools don't make a design system, but the right ones make it much cheaper to run. The six areas of a toolchain, the minimum tool set for each stage, and the seven automations that pay for themselves.",
         cta="audit", related=["figma-code-sync", "ai-in-design-systems", "design-system-maturity-model"]),
    dict(slug="design-system-migration", date="2026-11-12", topic="governance",
         h1="Migrating legacy products onto a design system",
         title="Migrating Legacy Products to a Design System",
         desc="How to migrate legacy products onto a design system without a big-bang rewrite: tokens first, screens as they're touched, codemods and clear end states.",
         dek="Big-bang rewrites stall halfway and leave products with two systems. Migrate in layers instead: tokens first, then the most visible parts, then screen by screen, with codemods, warnings and an agreed end state for every product.",
         cta="audit", related=["design-system-versioning", "design-tokens", "multi-brand-design-system"]),
    dict(slug="design-system-onboarding", date="2026-11-12", topic="operations",
         h1="Design system onboarding and training that keeps adoption growing",
         title="Design System Onboarding, Training and Adoption",
         desc="How to teach a design system continuously: first-week onboarding, a starter task, learning paths by role, training formats and finding knowledge gaps.",
         dek="A launch event teaches the people in the room. Six months later, half the people building your product joined after it. How to make onboarding, training and learning content a permanent programme rather than a one-off.",
         cta="call", related=["design-system-champions", "design-system-office-hours", "design-system-documentation"]),
    dict(slug="design-system-research", date="2026-11-12", topic="operations",
         h1="Design system research: how to learn what teams actually need",
         title="Design System Research: Interviews, Surveys, Data",
         desc="How to research a design system's users: interviews, observation, a five-minute survey, testing components and docs, and turning findings into a roadmap.",
         dek="Design system teams research their customers' customers, then forget to research their own. The methods that work inside a company, a survey you can copy, and how to turn findings into a roadmap people believe in.",
         cta="call", related=["design-system-metrics", "design-system-onboarding", "design-system-audit"]),
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

# Card images: one size rule for every card, so the browser always picks a sensible file.
CARD_SIZES = "(max-width: 760px) calc(100vw - 32px), (max-width: 1100px) 45vw, 400px"
LEAD_SIZES = "(max-width: 760px) calc(100vw - 32px), 720px"
ROW_SIZES = "(max-width: 760px) calc(100vw - 32px), 300px"


def reader_head(title, desc, depth, og="assets/og/layer-one.jpg", extra=""):
    """The site's own <head> and body, plus the reading-theme switch."""
    h = head(title, desc, depth=depth, og=og)
    h = h.replace('<body class="theme-dark">', '<body class="theme-dark reader">')
    return h.replace("</head>", THEME_JS + extra + "\n</head>", 1)


def theme_toggle():
    return (f'<button class="ed-theme" type="button" data-rd-theme aria-label="Switch between dark and light reading" title="Light or dark reading">'
            f'{SUN}{MOON}</button>')


def ed_foot(p):
    return f'''<footer class="ed-foot"><div class="ed-foot-in">
  <a class="logo" href="{p}index.html" aria-label="Layer One, home">{LOGO}<span>LAYER ONE</span></a>
  <p>A design systems studio in Bangalore, India. Led by Aniket Pandey.</p>
  <nav aria-label="Studio"><a href="{p}work.html">Work</a><a href="{p}pricing.html">Pricing</a><a href="{p}lab.html">Lab</a><a href="{p}contact.html">Contact</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="{MEDIUM}" target="_blank" rel="noopener">Medium</a></nav>
</div></footer>'''


def page(p, depth, content, active="writing"):
    """Writing pages use the site's top bar and its outer grid: the same container, edges and gutters
    as the navigation, so every section lines up with the logo on the left and the button on the right."""
    bar = topbar(active, depth).replace('<a class="pill book"', theme_toggle() + '<a class="pill book"', 1)
    return bar + f'<main id="main" class="ed-wrap">{content}</main>' + ed_foot(p) + close(depth)


def meta_line(a):
    return f'{TOPIC[a["topic"]][0]}', f'{a["minutes"]} min read' + (" · Guide" if a.get("pillar") else "")


def ecard(a, p, size="", ext=None, eager=False):
    """The one article card used everywhere: cover, topic, title, summary, reading time."""
    load = (' fetchpriority="high"' if size == "ec--lead" else "") if eager else ' loading="lazy"'
    sizes = {"ec--lead": LEAD_SIZES, "ec--row": ROW_SIZES}.get(size, CARD_SIZES)
    if ext:
        u, t, k, m, img = ext
        return (f'<a class="ec {size}" href="{u}" target="_blank" rel="noopener" data-topic="{k}">'
                f'<span class="ec-m"><img src="{p}{img}" alt="" width="1600" height="900" sizes="{sizes}" decoding="async"{load}></span>'
                f'<span class="ec-k">{TOPIC[k][0]}</span><b class="ec-t">{t}</b>'
                f'<span class="ec-f">{m} min read · on Medium ↗</span></a>')
    topic, mins = meta_line(a)
    title = a["h1"] if size == "ec--lead" else short_title(a)
    desc = a["dek"] if size == "ec--lead" else a["desc"]
    go = f'<span class="ec-go">Read the guide {ARROW}</span>' if size == "ec--lead" else ""
    return (f'<a class="ec {size}" href="{p}writing/{a["slug"]}.html" data-topic="{a["topic"]}">'
            f'<span class="ec-m"><img src="{p}{a["cover"]}" alt="" width="1600" height="900" sizes="{sizes}" decoding="async"{load}></span>'
            f'<span class="ec-k">{topic}</span><b class="ec-t">{title}</b>'
            f'<span class="ec-d">{desc}</span><span class="ec-f">{mins}</span>{go}</a>')


SHORT_TOPIC = {"building": "Building", "foundations-and-tokens": "Foundations & tokens", "operations": "Operations & teams", "business-case": "Value & metrics"}


def topic_count(k):
    return sum(1 for a in A if a["topic"] == k) + sum(1 for m in MEDIUM_POSTS if m[2] == k)


def filter_bar(p, active=None, filt=False):
    """Topic chips that sit with the article list they control. On the library page they filter in place;
    on topic pages they link between topics."""
    def chip(href, label, count, key, cur):
        attrs = ' aria-current="page"' if cur else ""
        f = f' data-filter="{key}"' if filt else ""
        return f'<a href="{href}"{attrs}{f}><span>{label}</span><em>{count}</em></a>'
    out = chip(f"{p}writing.html#articles", "All", len(A) + len(MEDIUM_POSTS), "all", active is None)
    out += "".join(chip(f"{p}writing/topics/{k}.html", SHORT_TOPIC.get(k, n), topic_count(k), k, k == active) for k, n, _ in TOPICS)
    return f'<nav class="ed-chips" aria-label="Filter by topic">{out}</nav>'


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
    series_line = ""
    nxt = None
    if s:
        i = s[3].index(a["slug"])
        series_line = f'<span class="ed-crumb-s">Part {i + 1} of {len(s[3])} in <a href="{p}writing.html#{s[0]}">{s[1]}</a></span>'
        nxt = BY[s[3][i + 1]] if i + 1 < len(s[3]) else None
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for t, i in a["toc"])
    nh, nt, nl, nu = NUDGE[a["cta"]]
    ext = nu.startswith("http")
    nattr = ' target="_blank" rel="noopener"' if ext else ""
    nhref = nu if ext else p + nu
    nexts = ([nxt] if nxt else []) + [BY[r] for r in a["related"] if not nxt or r != nxt["slug"]]
    nexts = nexts[:3]
    lead = "Next in " + s[1] if nxt else "Keep reading"
    cards = "".join(ecard(x, p) for x in nexts)
    upd = f' · Updated {nice_date(a["updated"])}' if a.get("updated") else ""
    mtoc = (f'<details class="ed-mtoc"><summary><span>On this page</span><b data-mtoc-current>{a["toc"][0][0] if a["toc"] else ""}</b></summary>'
            f'<ol>{toc}</ol></details>')
    steps = ""
    if s:
        steps = "".join(f'<li{" aria-current=" + chr(34) + "step" + chr(34) if x == a["slug"] else ""}><a href="{x}.html">{path_title(BY[x])}</a></li>' for x in s[3])
        steps = f'<div class="ed-meta-sec"><p class="ed-meta-h">{s[1]}</p><ol class="ed-steps">{steps}</ol></div>'
    url = f"https://www.layerone.co.in/writing/{a['slug']}"
    share = (f'<div class="ed-meta-sec"><p class="ed-meta-h">Share</p><p class="ed-share">'
             f'<button type="button" data-copy="{url}">Copy link</button>'
             f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener">LinkedIn</a>'
             f'<a href="https://x.com/intent/post?url={url}" target="_blank" rel="noopener">X</a></p></div>')
    content = f'''<article class="ed-article">
  <div class="ed-layout">
    <aside class="ed-meta" aria-label="About this article"><div class="ed-meta-in">
      <div class="ed-meta-who"><img src="{p}assets/studio/aniket.jpg" alt="" width="40" height="40"><p><b>{AUTHOR}</b><span>Founder, Layer One</span></p></div>
      <dl class="ed-meta-dl"><div><dt>Published</dt><dd>{nice_date(a["date"])}{upd}</dd></div><div><dt>Reading time</dt><dd>{a["minutes"]} minutes</dd></div><div><dt>Topic</dt><dd><a href="{p}writing/topics/{a["topic"]}.html">{topic}</a></dd></div></dl>
      {steps}{share}
    </div></aside>
    <header class="ed-head">
      <p class="ed-crumb"><a href="{p}writing.html">Writing</a><span aria-hidden="true">/</span><a href="{p}writing/topics/{a["topic"]}.html">{topic}</a>{series_line}</p>
      <h1 class="ed-title">{a["h1"]}</h1>
      <p class="ed-dek">{a["dek"]}</p>
      <p class="ed-byline"><img src="{p}assets/studio/aniket.jpg" alt="" width="36" height="36"><span><b>{AUTHOR}</b><span>{a["minutes"]} min read · {nice_date(a["date"])}{upd}</span></span></p>
    </header>
    <figure class="ed-cover"><img src="{p}{a["cover"]}" alt="" width="1600" height="900" sizes="(max-width: 1024px) calc(100vw - 32px), 760px" fetchpriority="high"></figure>
    {mtoc}
    <div class="ed-body post-body">{a["body"]}</div>
    <aside class="ed-aside" aria-label="On this page"><nav class="ed-toc"><p>On this page</p><ol>{toc}</ol><a class="ed-top" href="#main">Back to top ↑</a></nav></aside>
  </div>
  <footer class="ed-end">
    <section class="ed-more" aria-labelledby="more-h"><h2 class="ed-sec-h" id="more-h">{lead.lower()}:</h2><div class="ec-grid">{cards}</div></section>
    <aside class="ed-note" aria-label="From Layer One"><div><p class="ed-note-k">From Layer One</p><h2>{nh}</h2><p>{nt}</p></div><a href="{nhref}"{nattr}>{nl} {ARROW}</a></aside>
  </footer>
</article>
<div class="ed-progress" aria-hidden="true"><span></span></div>'''
    write(f"writing/{a['slug']}.html", article_head(a, 1) + page(p, 1, content))


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
        out += (f'<section class="ep" id="{k}"><header class="ep-h"><span class="ep-no">Path {i:02d} · {len(items)} articles · {mins} min</span><h3>{n}</h3><p>{d}</p></header>'
                f'<ol class="ep-steps">{steps}</ol><a class="ep-start" href="{p}writing/{items[0]}.html">Start the path {ARROW}</a></section>')
    return out


def build_hub():
    p = ""
    lead = BY["what-is-a-design-system"]
    second = [BY["design-system-operating-model"], BY["design-tokens"]]
    shown = {lead["slug"]} | {x["slug"] for x in second}
    rest = sorted([a for a in NEW if a["slug"] not in shown], key=lambda a: a["date"], reverse=True) + [BY["librarian-vs-leader"]]
    cards = "".join(ecard(a, p) for a in rest) + "".join(ecard(None, p, ext=m) for m in MEDIUM_POSTS)
    topics = "".join(f'<a class="et" href="writing/topics/{k}.html"><b>{n}</b><span>{d}</span><em>{topic_count(k)} articles</em></a>' for k, n, d in TOPICS)
    content = f'''<header class="ed-intro">
  <div>
    <p class="ed-crumb"><span>Writing</span></p>
    <h1>Field notes on design systems</h1>
  </div>
  <div class="ed-intro-r">
    <p>How design systems are built, run and measured: tokens and components, governance and teams, and what actually changes once a system is in use. From work at CARS24, IBM and JPMorgan Chase.</p>
    <p class="ed-intro-n"><span>{len(A) + len(MEDIUM_POSTS)} articles</span><span>{len(SERIES)} reading paths</span><span>{len(TOPICS)} topics</span></p>
  </div>
</header>

<section class="ed-sec ed-sec--first" aria-labelledby="featured-h">
  <h2 class="ed-sec-h" id="featured-h">featured:</h2>
  <div class="ed-featured">
    {ecard(lead, p, "ec--lead", eager=True)}
    <div class="ed-featured-row">{"".join(ecard(x, p, "ec--row") for x in second)}</div>
  </div>
</section>

<section class="ed-sec" id="articles" aria-labelledby="latest-h">
  <div class="ed-sec-bar">
    <h2 class="ed-sec-h" id="latest-h">latest articles:</h2>
    {filter_bar(p, filt=True)}
  </div>
  <p class="ed-filter-state" data-filter-state aria-live="polite"></p>
  <div class="ec-grid" data-filter-list>{cards}</div>
</section>

<section class="ed-sec" id="series" aria-labelledby="paths-h">
  <div class="ed-sec-bar"><h2 class="ed-sec-h" id="paths-h">reading paths:</h2><p class="ed-sec-d">Curated sequences for learning a subject from the start. Each article still stands on its own.</p></div>
  <div class="ep-list">{paths_html(p)}</div>
</section>

<section class="ed-sec" id="topics" aria-labelledby="topics-h">
  <div class="ed-sec-bar"><h2 class="ed-sec-h" id="topics-h">explore by topic:</h2><p class="ed-sec-d">Older essays are on <a href="{MEDIUM}" target="_blank" rel="noopener">Medium</a>.</p></div>
  <div class="et-grid">{topics}</div>
</section>'''
    items = [{"@type": "ListItem", "position": i, "url": f"https://www.layerone.co.in/writing/{a['slug']}", "name": short_title(a)} for i, a in enumerate(NEW + [BY["librarian-vs-leader"]], 1)]
    ldj = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "Layer One: Writing", "url": "https://www.layerone.co.in/writing",
                      "description": "A practical library on building and running design systems.", "publisher": {"@type": "Organization", "name": "Layer One"},
                      "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False)
    h = reader_head("Writing: design systems guides | Layer One",
                    "Practical guides on design systems: what they are, tokens and colour, governance, team structure, operating models, metrics and ROI. From Layer One.",
                    0, extra=f'<script type="application/ld+json">{ldj}</script>')
    write("blog.html", h + page(p, 0, content))


def build_topics():
    p = "../../"
    for k, n, d in TOPICS:
        arts = [a for a in A if a["topic"] == k]
        arts.sort(key=lambda a: not a.get("pillar"))
        cards = "".join(ecard(a, p, eager=i < 3) for i, a in enumerate(arts)) + "".join(ecard(None, p, ext=m) for m in MEDIUM_POSTS if m[2] == k)
        content = f'''<header class="ed-intro">
  <div>
    <p class="ed-crumb"><a href="{p}writing.html">Writing</a><span aria-hidden="true">/</span><span>Topic</span></p>
    <h1>{n}</h1>
  </div>
  <div class="ed-intro-r"><p>{d}</p><p class="ed-intro-n"><span>{topic_count(k)} articles</span></p></div>
</header>
<section class="ed-sec ed-sec--first" aria-labelledby="t-h">
  <div class="ed-sec-bar"><h2 class="ed-sec-h" id="t-h">articles:</h2>{filter_bar(p, k)}</div>
  <div class="ec-grid">{cards}</div>
</section>'''
        write(f"writing/topics/{k}.html", reader_head(f"{n}: design systems articles | Layer One", d, 2) + page(p, 2, content))


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
    # Writing pages load a stylesheet with only the rules they use (about a quarter of site.css).
    from purge_css import purge
    pages = [os.path.join(OUT, f) for f in WRITTEN if f == "writing.html" or f.startswith("writing/")]
    full, lean = purge(pages, "assets/writing.css")
    v = ver("assets/writing.css")
    for f in pages:
        h = open(f).read()
        h = re.sub(r'(href="(?:\.\./)*)assets/site\.css\?v=\w+"', lambda m: f'{m.group(1)}assets/writing.css?v={v}"', h)
        open(f, "w").write(h)
    print(f"writing.css: {lean // 1024} KB (site.css {full // 1024} KB without comments), used by {len(pages)} pages")
