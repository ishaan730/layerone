from cs import *

G = "assets/work/governance/"

msgs = [("SE", "Product designer · Seller", "10:14", "We need a custom card for car pricing on the seller flow. Can it go into the library? We launch in two weeks.", "No replies yet"),
        ("LO", "Frontend engineer · Loans", "11:02", "Can we add a heatmap chart? Our dashboard needs one and I'd rather not build it from scratch.", "👀 1"),
        ("BU", "Product designer · Buyer", "16:40", "Our flow needs a special carousel. Is there a way to do it with what we have?", ""),
        ("NC", "Product designer · New cars", "09:31", "Can I add this new filter pattern? Happy to do the Figma work myself.", "2 replies · last reply 9 days ago"),
        ("AE", "Mobile engineer · UAE", "12:05", "We built a checkout component. Can other teams use it? Where would I even put it?", ""),
        ("AU", "Product designer · Australia", "15:22", "How do I propose a new button variant? Is there a form somewhere?", "👍 4 · +1 same question")]
chat = '<div class="m-chat"><div class="mc-head"><b># design-system-help</b><span>6 new requests this week · 1 answered</span></div>' + "".join(
    f'<div class="mc-msg"><span class="av">{a}</span><div><p class="mc-who">{w}<span>{t}</span></p><p>{m}</p>{f"<p class=mc-meta>{r}</p>" if r else ""}</div></div>'
    for a, w, t, m, r in msgs) + '<p class="mc-foot">Recreated from real requests. Names removed.</p></div>'

steps = [("Ask", "Anyone", "Any time", "Post in #design-system-help or fill in the proposal form: what it's for, who needs it and how often it comes up.", "A request with context"),
         ("Review", "Design system team and the requester", "Weekly office hours", "New requests are reviewed together. Anything unclear goes back as a question.", "A complete request"),
         ("Score", "Design system team, in the open", "At review", "Four questions, out of 70. The score is shared, so the requester sees why it landed where it did.", "A priority"),
         ("Decide", "Design system team", "Same week", "Accept, defer or reject. Every decision goes back to the team with the reason attached.", "A decision and a reason"),
         ("Build", "Depends on the tier", "By priority", "Core work is built by the system team, extended work together, custom work stays with the product team.", "A tokenised, accessible component"),
         ("Release", "Design system team", "Every release", "Documented in Figma and Storybook, announced with a changelog and migration steps.", "A note in #design-system-releases"),
         ("Check", "Design system team", "Every quarter", "Live screens are audited. Anything that has drifted comes back in as a new request, so step 7 feeds step 1.", "New requests for step 1")]

questions = [
    ("where", "Where is it needed?", "Work in main products helps the most people.", [("20", "Main products"), ("15", "Smaller products"), ("5", "One small team"), ("x", "Nowhere")]),
    ("reuse", "How many can reuse it?", "A design system is for shared things.", [("20", "Many teams"), ("15", "A few teams"), ("5", "One team"), ("x", "Only one product")]),
    ("exists", "Do we already have it?", "Filling a real gap beats rebuilding what works.", [("15", "No"), ("10", "Partly"), ("5", "Mostly"), ("x", "Fully solved")]),
    ("effort", "How hard is it to build?", "Quick wins go first.", [("15", "Under a week"), ("10", "1–3 weeks"), ("5", "3+ weeks"), ("x", "Not worth it")]),
]
qs = "".join(
    f'<div class="scorer-q"><fieldset><legend>{q}</legend><p class="help">{h}</p><div class="seg">'
    + "".join(f'<label><input type="radio" name="{n}" value="{v}"><span>{"✕ " if v == "x" else "<b>" + v + "</b> "}{t}</span></label>' for v, t in o)
    + "</div></fieldset></div>" for n, q, h, o in questions)
scorer = f'''<form class="scorer" data-scorer onsubmit="return false" aria-label="Request scorecard">{qs}
  <div class="scorer-out" aria-live="polite"><div class="scorer-total"><span data-total>0</span> <small>/ 70</small></div><div class="scorer-verdict"><strong data-verdict></strong><span data-detail></span></div></div></form>'''

queue = [("Filter pattern", "New cars", 55), ("Checkout component", "UAE", 50), ("Button variant", "Australia", 45), ("Carousel variant", "Buyer", 35), ("Pricing card", "Seller", 25), ("Heatmap chart", "Loans", 0)]
qbars = '<figure class="m-fig"><div class="m-queue" data-inview>' + "".join(
    f'<div class="q"><span class="q-l">{n}<small>{t}</small></span><div class="q-t"><i style="--w:{s / 70 * 100:.0f}%" class="{"hi" if s >= 55 else "md" if s >= 40 else "lo" if s else "no"}"></i></div><b>{"Won’t fix" if s == 0 else s}</b></div>'
    for n, t, s in queue) + '</div><figcaption>The six requests from the channel, scored and put in order. Scores are illustrative.</figcaption></figure>'

tiers = [("core", "Core", "Used everywhere: buttons, inputs, tokens.", ["Designs: system team", "Builds: system team", "Reviews: system team", "Maintains: system team"]),
         ("extended", "Extended", "Used by a few teams: advanced filters, pricing cards.", ["Designs: together", "Builds: product team", "Reviews: system team", "Maintains: together"]),
         ("custom", "Custom", "One product, one use: a seasonal campaign card.", ["Designs: product team", "Builds: product team", "Reviews: product team", "Maintains: product team"])]
rings = '''<div class="m-rings" data-tabs><svg viewBox="0 0 300 300" aria-hidden="true">
  <circle cx="150" cy="150" r="140" class="r-custom"/><circle cx="150" cy="150" r="96" class="r-extended"/><circle cx="150" cy="150" r="52" class="r-core"/>
  <text x="150" y="155" text-anchor="middle">Core</text><text x="150" y="80" text-anchor="middle">Extended</text><text x="150" y="30" text-anchor="middle">Custom</text></svg>
  <div><div role="tablist" aria-label="Ownership tiers" class="rt">''' + "".join(
    f'<button role="tab" type="button" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}" data-ring="{k}">{n}</button>' for i, (k, n, *_r) in enumerate(tiers)) + "</div>" + "".join(
    f'<div role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if i == 0 else " hidden"}><p>{d}</p><ul>{"".join("<li>" + x + "</li>" for x in xs)}</ul></div>' for i, (k, n, d, xs) in enumerate(tiers)) + "</div></div>"

weeks = "".join(
    f'<div class="w"><span>W{i + 1}</span><i class="d"></i><i class="{"wk" if i % 1 == 0 else ""}"></i>{"<i class=qt></i>" if i == 12 else ""}</div>' for i in range(13))
quarter = f'''<figure class="m-fig"><div class="m-quarter"><div class="qg">{weeks}</div>
  <p class="br-key"><span class="kd">Daily: Slack help and release channels</span><span class="kw">Weekly: office hours</span><span class="kq">Quarterly: system audit</span></p></div>
  <figcaption>One quarter of listening: every day, every week, every quarter.</figcaption></figure>'''

spec = dict(
    h1="How the design system team stopped being the bottleneck",
    lede="As CARS24 grew, every team needed something from the design system, and one small team couldn't keep up. Requests piled up, nobody could see what was happening, and teams built around us. We changed how work came in, got decided and got built.",
    meta=[("Role", "Design Systems Lead"), ("Focus", "Governance, prioritisation, contribution"), ("Platforms", "Web, iOS, Android"), ("Markets", "India, UAE, Australia")],
    cover=(G + "cover.jpg", "Requests from six teams flowing through one front door, a score and three ownership tiers to release"),
    tldr=[("The problem", "Every request from every team ran through one small team. No front door, no shared rules, no way to help. Most requests just waited."),
          ("What we did", "One front door, a 70-point scorecard anyone can apply, three ownership tiers, a contribution playbook and a steady listening rhythm."),
          ("What changed", "Every decision came with a reason. Teams planned around releases, and more people built with the system instead of around it.")],
    kpis=[("70", " pts", "", "scorecard any team can apply"), ("7", " steps", "", "one path for every request"), ("3", " tiers", "", "core, extended and custom ownership"), ("4", "", "", "listening rhythms: daily to quarterly")],
    chapters=[
        ("problem", "Problem", "Six requests a week, one answered",
         "Requests arrived by DM, Slack, meetings and hallway chats. Yes or no depended on who asked loudest, so teams stopped trusting the answer.",
         chat + tiles([("No front door", "Requests came in everywhere, so nobody could see them all, including us."),
                       ("No shared rules", "Answers depended on who asked, so teams couldn't predict them."),
                       ("No way to help", "Teams that had already built something had nowhere to put it.")], cols=3)),
        ("research", "Research", "We tried the usual frameworks first",
         "Seven angles of research, from shadowing to surveys. Then we scored real requests with RICE and MoSCoW. With RICE, people argued about the numbers; with MoSCoW, everything was a Must.",
         tiles([("RICE: tried", "Weighs value against effort, but reach and confidence are guesses for a shared component. The score became the argument."),
                ("MoSCoW: tried", "Quick and familiar, but every team's request was a Must, and the label never explained why."),
                ("Our scorecard: used", "Four questions a product designer can answer without us: where, who reuses, do we have it, how hard."),
                ("Tested in the open", "Requesters scored their own asks next to ours. Where it felt wrong, we adjusted it.")])
         + more("We interviewed designers, engineers and PMs; mapped where requests got stuck; looked at unused and stalled requests; benchmarked Base, Shopify Polaris and Agoda; surveyed how much teams trusted the process; ran experiments; and shadowed teams to watch delays happen live.")),
        ("front-door", "Front door", "Every request takes the same path",
         "A bug, a new variant or a whole new component: everything goes through the same seven steps, so anyone can tell where a request is and what happens next.",
         stepper("flow", steps)),
        ("score", "Scorecard", "A score instead of an argument",
         "Four plain questions, each worth points. Any ✕ stops a request. 55+ is accepted and built first, 40–54 accepted, under 40 deferred. Try it on a request of your own.",
         scorer + qbars),
        ("ownership", "Ownership", "Not everything belongs in the core",
         "Three rings. The closer to the centre, the more widely a component is used and the more the system team looks after it. Select a ring.",
         rings),
        ("listening", "Listening", "A system you set and forget falls apart",
         "Listening was built into the routine at every speed, and a four-step playbook let teams contribute: propose, review and score, build together, document and release.",
         quarter),
        ("changed", "Outcome", "From gatekeeper to partner",
         "Flip between before and after.",
         shift([("Teams worked in silos", "A shared language and shared habits"), ("Forked styles and duplicate work", "Consistency through tokens and the system"),
                ("Rules handed down from the top", "Contributions led by the community"), ("The design system was a blocker", "The design system was an enabler"),
                ("Fear of change", "Trust and collaboration")])
         + tiles([("Designers", "Trusted the tools and patterns."), ("Engineers", "Started suggesting improvements themselves."),
                  ("Product managers", "Saw the system as a way to ship faster, and planned around releases."), ("The system team", "Stopped being a bottleneck and became a facilitator.")])),
        ("learnings", "Learnings", "What we'd do again", "Agree on the goal first, and treat governance as the thing that lets you scale.",
         tiles([("Agree on the goal first", "Every later argument is easier when everyone signed up to the same outcome."),
                ("Governance is what lets you scale", "Without it, more demand just means a longer queue."),
                ("Templates are lifelines", "They made the right thing the easy thing."),
                ("Culture matters as much as code", "The process only worked once people trusted it.")])),
    ],
    gallery=[(G + "cover.jpg", "The new flow: one front door, a score, three tiers"),
             ("assets/work/tokens/workshop-2.jpg", "Office hours and working sessions"),
             ("assets/work/patterns/request-template.jpg", "The request template teams use to propose new work")],
    credits="Led by Aniket Pandey as Design Systems Lead at CARS24, with CARS24's design, engineering and product teams. Images belong to CARS24 and are shown for portfolio purposes.",
)
page("governance", spec)
