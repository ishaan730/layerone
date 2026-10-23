from cs import *

G = "assets/work/governance/"

requests = [
    ("Seller", "Product designer", "We need a custom card for car pricing on the seller flow. Can it go into the library? We launch in two weeks."),
    ("Loans", "Frontend engineer", "Can we add a heatmap chart? Our dashboard needs one and I'd rather not build it from scratch."),
    ("Buyer", "Product designer", "Our flow needs a special carousel. Is there a way to do it with what we have?"),
    ("New cars", "Product designer", "Can I add this new filter pattern? Happy to do the Figma work myself."),
    ("UAE", "Mobile engineer", "We built a checkout component. Can other teams use it? Where would I even put it?"),
    ("Australia", "Product designer", "How do I propose a new button variant? Is there a form somewhere?"),
]
req_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in requests)

flow = [
    ("Ask", "Post in the help channel or fill in the proposal form: what it's for, who needs it and how often it comes up.", "Anyone, any time"),
    ("Review", "New requests are reviewed together at weekly office hours. Anything unclear goes back as a question.", "DS team and requester, weekly"),
    ("Score", "Four questions, out of 70. The score is shared, so the requester sees why it landed where it did.", "DS team, in the open"),
    ("Decide", "Accept, defer or reject. Every decision goes back to the team with the reason attached.", "DS team, same week"),
    ("Build", "Core work is built by the DS team, extended work together, and custom work stays with the product team.", "Depends on the tier"),
    ("Release", "Documented in Figma and Storybook, announced with a changelog and migration steps.", "DS team, every release"),
    ("Check", "Live screens are audited every quarter. Anything that has drifted comes back in as a new request.", "DS team, quarterly"),
]
flow_html = '<ol class="flow">' + "".join(f'<li><div><h3>{a}</h3><p>{b}</p></div><span class="who">{c}</span></li>' for a, b, c in flow) + "</ol>"

questions = [
    ("where", "Where is it needed?", "Work in main products helps the most people.", [("20", "Main products"), ("15", "Smaller products"), ("5", "One small team"), ("x", "Nowhere")]),
    ("reuse", "How many can reuse it?", "A design system is for shared things.", [("20", "Many teams"), ("15", "A few teams"), ("5", "One team"), ("x", "Only one product")]),
    ("exists", "Do we already have it?", "Filling a real gap beats rebuilding what works.", [("15", "No"), ("10", "Partly"), ("5", "Mostly"), ("x", "Fully solved")]),
    ("effort", "How hard is it to build?", "Quick wins go first, so teams aren't stuck waiting.", [("15", "Under a week"), ("10", "1–3 weeks"), ("5", "3+ weeks"), ("x", "Not worth it")]),
]
qs = ""
for name, q, help_, opts in questions:
    radios = "".join(
        f'<label><input type="radio" name="{name}" value="{v}"><span>{("✕ " if v == "x" else "<b>" + v + "</b> ")}{t}</span></label>' for v, t in opts)
    qs += f'<div class="scorer-q"><fieldset><legend class="label">{q}</legend><p class="help">{help_}</p><div class="seg">{radios}</div></fieldset></div>'
scorer = f'''<form class="scorer" data-scorer onsubmit="return false" aria-label="Request scorecard">{qs}
  <div class="scorer-out" aria-live="polite"><div class="scorer-total"><span data-total>0</span> <small>/ 70</small></div>
  <div class="scorer-verdict"><strong data-verdict></strong><span data-detail></span></div></div>
</form>'''

bands = '''<div class="table-wrap"><table class="data"><thead><tr><th>Score</th><th>Priority</th><th>What happens</th></tr></thead><tbody>
<tr><td class="num">55–70</td><td>High</td><td>Accepted and picked up first. The design system team builds it.</td></tr>
<tr><td class="num">40–54</td><td>Medium</td><td>Accepted, after high-priority work. The requesting team can contribute to speed it up.</td></tr>
<tr><td class="num">20–39</td><td>Low</td><td>Deferred. The team can build it as a custom or extended component.</td></tr>
<tr><td class="num">Any ✕</td><td>Won't fix</td><td>Rejected, whatever the total. The team builds it outside the system using the design language.</td></tr>
</tbody></table></div>'''

example = '''<div class="table-wrap"><table class="data"><thead><tr><th>Question</th><th>Answer</th><th>Points</th></tr></thead><tbody>
<tr><td>Where is it needed?</td><td>Search and filters sit in the main Buy funnel.</td><td class="num">20</td></tr>
<tr><td>How many can reuse it?</td><td>Buyer and New cars both filter listings. Seller doesn't.</td><td class="num">15</td></tr>
<tr><td>Do we already have it?</td><td>There were chips, but no way to pick several filters.</td><td class="num">10</td></tr>
<tr><td>How hard is it to build?</td><td>About two weeks, starting from the existing chip.</td><td class="num">10</td></tr>
<tr><td><strong>Total</strong></td><td>Accepted. Built by the design system team with the requester.</td><td class="num">55 / 70</td></tr>
</tbody></table></div>'''

rings = '''<div class="rings">
  <svg viewBox="0 0 280 280" role="img" aria-label="Three nested rings: core inside extended inside custom">
    <circle cx="140" cy="140" r="130" stroke-width="1" stroke-dasharray="4 5"/>
    <circle cx="140" cy="140" r="88" stroke-width="1"/>
    <circle cx="140" cy="140" r="46" stroke-width="2"/>
    <text x="140" y="144" text-anchor="middle">Core</text>
    <text x="140" y="74" text-anchor="middle">Extended</text>
    <text x="140" y="30" text-anchor="middle">Custom</text>
  </svg>
  <div class="table-wrap" style="margin-top:0"><table class="data"><thead><tr><th>Tier</th><th>Designs</th><th>Builds</th><th>Reviews</th><th>Maintains</th></tr></thead><tbody>
    <tr><td><strong>Core</strong></td><td>DS team</td><td>DS team</td><td>DS team</td><td>DS team</td></tr>
    <tr><td><strong>Extended</strong></td><td>Together</td><td>Product team</td><td>DS team</td><td>Together</td></tr>
    <tr><td><strong>Custom</strong></td><td>Product team</td><td>Product team</td><td>Product team</td><td>Product team</td></tr>
  </tbody></table></div>
</div>'''

shift_items = [("Teams worked in silos", "A shared language and shared habits"), ("Forked styles and duplicate work", "Consistency through tokens and the system"),
               ("Rules handed down from the top", "Contributions led by the community"), ("The design system was a blocker", "The design system was an enabler"),
               ("Fear of change", "Trust and collaboration")]
shift = '<ul class="shift">' + "".join(f'<li><span>{a}</span>{ARROW_SHIFT}<span>{b}</span></li>' for a, b in shift_items) + "</ul>"

sections = [
("setting", "The setting", "The setting", "10+ products, three countries, one library",
 prose("CARS24 runs buying, selling, loans and new cars across India, the UAE and Australia, on web, iOS and Android. Every one of those products used the same design system, looked after by one small team.",
       "As the company grew, product teams needed changes faster than that team could make them. There was no clear way to ask for something, no fair way to decide what came first, and no way for teams to help. So everything waited.")
 + cards([("Slower launches", "Product work waited on library changes that had no date."),
          ("Paying twice", "The same card, chip or carousel got built again by different teams."),
          ("Less trust", "People buying a car worth lakhs saw screens that didn't match.")], cols=3)),

("problem", "The problem", "The problem", "Six requests a week, one answered",
 prose("Requests arrived through DMs, Slack threads, meetings and hallway chats. Nobody could see the full list, including the design system team. Whether the answer was yes depended on who asked and how loudly, so teams stopped trusting it and built their own versions.",
       "Here's a typical week in the help channel, recreated from real requests with names removed.")
 + f'<div class="table-wrap"><table class="data"><thead><tr><th>Team</th><th>Role</th><th>Request</th></tr></thead><tbody>{req_rows}</tbody></table></div>'
 + cards([("No front door", "Requests came in everywhere, so nobody could see them all."),
          ("No shared rules", "Answers depended on who asked, so teams couldn't predict them."),
          ("No way to help", "Teams that had already built something had nowhere to put it.")], cols=3)),

("research", "Research", "Research", "First, we listened",
 prose("Before designing any process, we looked at where things actually broke, from seven angles: interviews with designers, engineers and PMs; a workflow audit of where requests got stuck; usage data on unused and stalled requests; benchmarking against Base, Shopify Polaris and Agoda; surveys on trust in the process; shadowing to watch delays happen live; and experiments with existing frameworks.",
       "The hardest part was deciding what to work on first. We scored a batch of real requests with RICE and MoSCoW. With RICE, people argued about the numbers, because reach and confidence are guesses for a shared component. With MoSCoW, every team's request came back as a Must.",
       "For a shared component, it came down to four things: where it's used, who can reuse it, whether it already exists, and how hard it is to build.")),

("front-door", "One front door", "Intake", "Every request takes the same path",
 prose("A bug, a new variant or a whole new component: it doesn't matter. Everything goes through the same seven steps, so anyone can tell where a request is and what happens next.")
 + flow_html
 + prose("Step seven feeds step one, so the system keeps improving without anyone having to remember to ask.")),

("score", "The score", "Prioritisation", "A score instead of an argument",
 prose("Four plain questions that any product designer can answer without the design system team. Each answer is worth points, the points add up to a priority, and the priority decides what happens next. It works the same way for every team. Try it.")
 + scorer + bands
 + prose("Here's the filter request from the help channel, as it was scored in office hours.") + example
 + prose("It held up because the questions were ones requesters could answer themselves. Once requesters and the design system team kept landing on the same score, it became the default.")),

("ownership", "Who owns what", "Ownership", "Not everything belongs in the core",
 prose("Components are split into three rings. The closer to the centre, the more widely a component is used and the more the design system team looks after it.")
 + rings),

("contributing", "Contributing", "Contribution", "Building with us, not waiting on us",
 prose("Once people saw the system working, many of them wanted to add to it. Without a clear path that meant uneven quality, long reviews and confusion about ownership. So we wrote a four-step playbook, with a template for every step.")
 + '<ol class="flow">'
   '<li><div><h3>Propose</h3><p>Start with context, not just a component: use cases, how often it comes up, the problem it solves, screenshots and suggested tokens.</p></div><span class="who">Requesting team</span></li>'
   '<li><div><h3>Review and score</h3><p>Data, not debate. The proposal is scored with the same four questions as every other request.</p></div><span class="who">DS team, with the requester</span></li>'
   '<li><div><h3>Build together</h3><p>Design system and product designers refine the spec together; engineers pair on reusable, tokenised code, checked for accessibility on web, iOS and Android.</p></div><span class="who">Both teams</span></li>'
   '<li><div><h3>Document and release</h3><p>A component without documentation doesn\'t exist. It ships with docs, a version number and a release note.</p></div><span class="who">DS team</span></li>'
   '</ol>'
 + prose("Around the playbook, we built listening into the routine at four speeds.")
 + cards([("Every day", "Slack channels for help, releases and changelogs. Fast answers, so nobody stays blocked."),
          ("Every week", "Office hours where any designer brings real use cases, friction and ideas."),
          ("Every quarter", "A system audit of live screens for token use, forked components and accessibility gaps."),
          ("Every release", "Changelogs with migration steps, so platforms stop drifting apart.")])),

("changed", "What changed", "Outcome", "From gatekeeper to partner",
 shift
 + prose("Designers trusted the tools and patterns. Engineers started suggesting improvements themselves. Product managers saw the system as a way to ship faster, and planned around releases. The design system team stopped being a bottleneck and became a facilitator.")),

("learnings", "Learnings", "Learnings", "What we'd do again",
 cards([("Agree on the goal first", "Every later argument is easier when everyone signed up to the same outcome."),
        ("Governance is what lets you scale", "Without it, more demand just means a longer queue."),
        ("Docs and templates are lifelines", "Templates made the right thing the easy thing."),
        ("Culture matters as much as code", "The process only worked once people trusted it.")])),
]

page("governance",
     "How the design system team stopped being the bottleneck",
     "As CARS24 grew, every team needed something from the design system, and one small team couldn't keep up. We changed how work came in, got decided and got built, so teams moved fast without going around the system.",
     [("Client", "CARS24"), ("Focus", "Governance, prioritisation, contribution"), ("Platforms", "Web, iOS and Android"), ("Markets", "India, UAE, Australia")],
     [("70 pts", "scorecard any team can apply to its own request"), ("7 steps", "one path for every bug, variant and component"),
      ("3 tiers", "core, extended and custom ownership"), ("4 rhythms", "daily, weekly, quarterly and per-release listening")],
     G + "cover.jpg", "Diagram of requests from six teams flowing through one front door, a score, and three ownership tiers to release", sections, "cars24-governance.html")
