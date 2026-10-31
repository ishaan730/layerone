from common import *


def choices(name, label, opts, kind="seg", required=False, hint=""):
    """Radio group. kind: list (stacked rows in one box), tile (even grid), seg (joined segmented buttons).
    opts = [(value, title, desc)]"""
    req = " required" if required else ""
    items = ""
    for i, (v, t, d) in enumerate(opts):
        desc = f"<small>{d}</small>" if d else ""
        items += f'<label class="opt opt--{kind}"><input type="radio" name="{name}" value="{v}"{req if i == 0 else ""}><span><b>{t}</b>{desc}</span></label>'
    h = f'<span class="f-hint">{hint}</span>' if hint else ""
    return f'<fieldset class="f-group"><legend>{label}{h}</legend><div class="opts opts--{kind}">{items}</div></fieldset>'


def section(n, title, body):
    return f'<section class="f-sec"><header class="f-sec-head"><span>{n:02d}</span><h2>{title}</h2></header><div class="f-sec-body">{body}</div></section>'


stage = choices("stage", "Where is your design system today?", [
    ("We don't have one yet", "We don't have one yet", "Styles live in each team's files"),
    ("It doesn't scale", "It doesn't scale", "Works for one product, breaks across several"),
    ("The system team is a bottleneck", "The team is a bottleneck", "Requests pile up, teams build around it"),
    ("Teams aren't using it", "Teams aren't using it", "It exists, but adoption is low"),
], kind="list", required=True)

offer = choices("offer", "What are you interested in?", [
    ("System Audit", "Audit", "$1,500"), ("Foundations", "Foundations", "$5,900"), ("Partner", "Partner", "$2,900/mo"),
    ("Workshop", "Workshop", "$450"), ("Founding partner slot", "Founding partner", "−20%"), ("Not sure yet", "Not sure yet", "We'll suggest one"),
], kind="tile", required=True)

when = choices("when", "When would you like to start?", [
    ("As soon as possible", "As soon as possible", ""), ("In 1–3 months", "In 1–3 months", ""), ("Just exploring", "Just exploring", "")], hint="Optional")

size = choices("size", "How many designers are on the team?", [
    ("1–5", "1–5", ""), ("6–20", "6–20", ""), ("20+", "20+", "")], hint="Optional")

about = f'''<div class="f-row">
      <label class="field"><span>Your name</span><input name="name" autocomplete="name" required placeholder="Priya Sharma"></label>
      <label class="field"><span>Work email</span><input name="email" type="email" autocomplete="email" required placeholder="priya@company.com"></label>
    </div>
    <div class="f-row">
      <label class="field"><span>Company</span><input name="company" autocomplete="organization" required placeholder="Company name"></label>
      <label class="field"><span>Your role <em>Optional</em></span><input name="role" autocomplete="organization-title" placeholder="Design lead, CTO…"></label>
    </div>'''

details = f'''{when}{size}
    <label class="field"><span>Anything else we should know? <em>Optional</em></span>
      <textarea name="message" rows="3" placeholder="Products, platforms, deadlines, or a link to your Figma library or Storybook"></textarea></label>'''

content = f'''
<h1 class="statement">Start a project</h1>
<p class="sub muted">Tell us where your system is today. You'll hear back from Aniket within one working day.</p>

<div class="contact">
  <form class="cform" data-contact novalidate>
    {section(1, "About you", about)}
    {section(2, "Your system", stage + offer)}
    {section(3, "Timing and details", details)}
    <p class="f-error" data-f-error role="alert" hidden></p>
    <div class="f-submit">
      <button class="pill pill--accent pill--lg" type="submit">Send enquiry {ARROW}</button>
      <p class="small muted">Opens an email to {EMAIL} with your answers filled in. Nothing is stored on this site.</p>
    </div>
  </form>

  <aside class="c-side" aria-label="Other ways to reach us">
    <div class="c-card">
      <div class="c-person"><img src="assets/studio/aniket.jpg" alt="" width="56" height="56"><div><strong>You'll talk to Aniket</strong><span>Founder. Design systems at CARS24, IBM and JPMorgan Chase.</span></div></div>
      <div class="c-mail"><a href="mailto:{EMAIL}">{EMAIL}</a><button type="button" class="btn-line" data-copy-email="{EMAIL}">Copy</button></div>
      <a class="pill c-book" href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call {ARROW}</a>
      <p class="small muted">Mon–Fri, 10:00–19:00 IST. Calls can be early or late for US and European teams.</p>
    </div>
    <div class="c-card">
      <h2>What happens next</h2>
      <ol class="c-steps">
        <li><b>Within a day</b><span>We reply with a few questions or a time to talk.</span></li>
        <li><b>A 30-minute call</b><span>Where your system is, what's in the way, and whether we're the right fit. If we're not, we'll say so.</span></li>
        <li><b>A fixed proposal in 48 hours</b><span>Scope, timeline and a fixed price. No hourly billing.</span></li>
      </ol>
    </div>
  </aside>
</div>
'''
write("contact.html", head("Contact — Layer One", "Start a design system project with Layer One.")
      + shell("contact", [("Start a project", "#main")], content))
