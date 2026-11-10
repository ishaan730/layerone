"""Data-driven figures for the writing library. Every number comes from the playbook's computed data
(content/writing/data/*.json, generated with culori in OKLCH by the Design Systems Playbook build).
Used in article bodies as <!--fig:name-->."""
import json
import os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "writing", "data")


def _j(name):
    with open(os.path.join(D, name + ".json")) as f:
        return json.load(f)


def _ink(hexv):
    """Black or white text for a swatch, whichever contrasts more."""
    r, g, b = (int(hexv[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    return "#0b0d12" if (y + 0.05) / 0.05 > 1.05 / (y + 0.05) else "#ffffff"


def fig(body, cap, cls=""):
    return f'<figure class="w-fig {cls}">{body}<figcaption>{cap}</figcaption></figure>'


def palette():
    p = _j("palette")
    rows = ""
    for r in p["ramps"]:
        cells = "".join(f'<div class="sw" style="background:{s["hex"]};color:{_ink(s["hex"])}"><b>{s["step"]}</b><span>{s["hex"]}</span><em>{s["onWhite"]:.1f}</em></div>' for s in r["steps"])
        rows += f'<div class="w-ramp"><p>{r["label"]}<span>hue {r["hue"]}°</span></p><div class="w-ramp-row">{cells}</div></div>'
    return fig(f'<div class="w-ramps">{rows}</div>',
               "Six ramps built in OKLCH with one lightness curve and one chroma envelope. Each swatch shows its step, hex value and contrast ratio against white. "
               "Step 700 passes 4.5:1 on white in every ramp; step 600 passes in all but green (4.16:1). Source: the Layer One design systems playbook, computed with culori.", "w-fig--wide")


def lightness():
    p = _j("palette")
    steps = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
    bars = "".join(f'<div class="lc"><i style="height:{l * 100:.0f}%"></i><b>{l:.3f}</b><span>{s}</span></div>' for s, l in zip(steps, p["lightnessCurve"]))
    return fig(f'<div class="lcurve">{bars}</div>',
               "The shared lightness curve: OKLCH lightness for each step, from 0.975 (step 50) to 0.255 (step 950). Every ramp uses the same curve, which is why "
               "step 600 in blue and step 600 in green have nearly the same contrast against white.")


def hsl_vs_oklch():
    h = _j("hsl-vs-oklch")

    def row(items, label):
        cells = "".join(f'<div class="sw" style="background:{x["hex"]};color:{_ink(x["hex"])}"><b>{x["label"].replace("hsl(", "").replace("oklch(", "").rstrip(")")}</b><span>L {x["perceivedL"]:.2f}</span><em>{x["onWhite"]:.2f}:1</em></div>' for x in items)
        return f'<div class="w-ramp"><p>{label}</p><div class="w-ramp-row w-ramp-row--6">{cells}</div></div>'

    return fig(f'<div class="w-ramps">{row(h["hsl"], "HSL, all at 50% lightness")}{row(h["oklch"], "OKLCH, all at lightness 0.65")}</div>',
               "Same promise, different results. The six HSL colours all claim 50% lightness, but their perceived lightness runs from 0.45 (blue) to 0.97 (yellow), "
               "and their contrast on white runs from 1.07:1 to 8.59:1. The six OKLCH colours sit at 0.65 and their contrast stays between 2.93:1 and 3.46:1.", "w-fig--wide")


def semantic():
    s = _j("semantic-colors")
    rows = "".join(
        f'<tr><td><code>{t["token"]}</code></td><td><span class="chip" style="background:{t["lightHex"]}"></span><code>{t["light"]}</code></td>'
        f'<td><span class="chip" style="background:{t["darkHex"]}"></span><code>{t["dark"]}</code></td></tr>' for t in s["tokens"])
    return fig(f'<div class="w-tbl"><table><thead><tr><th>Semantic token</th><th>Light mode</th><th>Dark mode</th></tr></thead><tbody>{rows}</tbody></table></div>',
               "Seventeen semantic colour tokens and the primitive each one points to in light and dark mode. Components only ever use the left column.")


def pairs():
    s = _j("semantic-colors")
    rows = ""
    for x in s["pairs"]:
        req = f'{x["min"]}:1' if x["min"] else "exempt"
        def cell(v, ok):
            mark = "" if ok is None else ('<span class="ok">Pass</span>' if ok else '<span class="no">Fail</span>')
            return f"<td class=\"r\">{v:.2f}:1 {mark}</td>"
        rows += f'<tr><td>{x["use"]}</td><td><code>{x["fg"]}</code> on <code>{x["bg"]}</code></td><td class="r">{req}</td>{cell(x["light"], x["lightPass"])}{cell(x["dark"], x["darkPass"])}</tr>'
    return fig(f'<div class="w-tbl"><table><thead><tr><th>Use</th><th>Pair</th><th class="r">Needs</th><th class="r">Light</th><th class="r">Dark</th></tr></thead><tbody>{rows}</tbody></table></div>',
               "Every pairing that matters, checked in both modes against WCAG 2.2: 4.5:1 for text (1.4.3) and 3:1 for borders and focus rings (1.4.11). "
               "Disabled text is exempt under WCAG, but we still keep it readable.")


def preview():
    s = {t["token"]: t for t in _j("semantic-colors")["tokens"]}

    def card(mode):
        g = lambda k: s[k][mode + "Hex"]
        return (f'<div class="tm" style="background:{g("bg.canvas")};color:{g("text.primary")};border-color:{g("border.default")}">'
                f'<p class="tm-k" style="color:{g("text.secondary")}">{mode} mode</p>'
                f'<p class="tm-h">Invoice #2041</p><p style="color:{g("text.secondary")}">Due 12 March · 3 items</p>'
                f'<div class="tm-alert" style="background:{g("feedback.danger.bg")};color:{g("feedback.danger.text")}">Payment overdue by 4 days</div>'
                f'<div class="tm-row"><span class="tm-btn" style="background:{g("action.primary.bg")};color:{g("action.primary.text")}">Pay now</span>'
                f'<span style="color:{g("text.link")};text-decoration:underline">View details</span></div></div>')
    return fig(f'<div class="tm-pair">{card("light")}{card("dark")}</div>',
               "The same card, the same component code, two sets of answers. Only the semantic tokens change between the two.")


def roi_years():
    e = _j("economics")
    mx = max(max(y["usd"], y["cost"]) for y in e["years"])
    rows = ""
    for y in e["years"]:
        rows += (f'<div class="roi-y"><p><b>Year {y["year"]}</b><span>{int(y["adoption"] * 100)}% adoption · {int(y["gain"] * 100)}% faster on system work</span></p>'
                 f'<div class="roi-b"><i class="v" style="width:{y["usd"] / mx * 100:.1f}%"></i><span>Value ${y["usd"]:,}</span></div>'
                 f'<div class="roi-b"><i class="c" style="width:{y["cost"] / mx * 100:.1f}%"></i><span>Cost ${y["cost"]:,}</span></div>'
                 f'<p class="roi-n {"pos" if y["net"] >= 0 else "neg"}">Net {"+" if y["net"] >= 0 else "−"}${abs(y["net"]):,}</p></div>')
    return fig(f'<div class="roi">{rows}</div>',
               "Ledgerly, an illustrative SaaS company with 40 engineers and 6 designers, funds two full-time people at $12,000 a month each ($288,000 a year). "
               "Value is hours saved on UI work × $90 an hour. It doesn't pay back until year three, and only because adoption keeps climbing.")


def break_even():
    e = _j("economics")
    rows = ""
    for b in e["breakEvens"]:
        note = ""
        if b["gain"] != 0.2:
            note = " (34% speed-up)"
        elif b["adoption"] != 0.7:
            note = " (50% adoption)"
        rows += f'<tr><td>{b["fte"]:g} FTE{note}</td><td class="r">${b["cost"]:,}</td><td class="r"><b>{b["engineers"]}</b></td></tr>'
    return fig(f'<div class="w-tbl"><table><thead><tr><th>System team</th><th class="r">Cost a year</th><th class="r">Engineers needed to break even</th></tr></thead><tbody>{rows}</tbody></table></div>',
               "Break-even at 70% adoption and a 20% speed-up on system work, with one designer for every seven engineers. Roughly 22–23 engineers for every full-time system person. "
               "Change the speed-up or the adoption and the answer moves a lot, which is the point.")


def sensitivity():
    e = _j("economics")
    head = "".join(f'<th class="r">{int(c["adoption"] * 100)}% adoption</th>' for c in e["sensitivity"][0]["cells"])
    rows = ""
    for r in e["sensitivity"]:
        cells = "".join(f'<td class="r heat {"pos" if c["net"] >= 0 else "neg"}">{"+" if c["net"] >= 0 else "−"}${abs(c["net"]) // 1000:,}k</td>' for c in r["cells"])
        rows += f'<tr><th>{int(r["gain"] * 100)}% faster</th>{cells}</tr>'
    return fig(f'<div class="w-tbl"><table class="heat-t"><thead><tr><th>Speed-up on system work</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>',
               "Net value in one year for Ledgerly's $288,000 system team, across nine combinations of speed-up and adoption. Adoption matters as much as how good the components are.")


def budgets():
    e = _j("economics")
    out = ""
    for s in e["scenarios"]:
        roles = "".join(f"<li><span>{n}</span><b>{f:g} × {m} mo</b></li>" for n, f, m in s["build"])
        lo, hi = s["totalFteMonths"] * 6000, s["totalFteMonths"] * 20000
        out += (f'<div class="bud"><p class="bud-k">{s["name"]}</p><p class="bud-p">{s["profile"]}</p><ul>{roles}</ul>'
                f'<p class="bud-t"><b>{s["totalFteMonths"]:g} FTE-months</b><span>${lo / 1000:,.0f}k–${hi / 1000:,.0f}k at $6k–$20k a month per person</span></p></div>')
    return fig(f'<div class="buds">{out}</div>',
               "Three realistic first-year budgets from the playbook, counted in FTE-months (one person, full-time, for one month) so they work in any country. "
               "The startup and mid-sized totals include the first months of running the system, not just the build.", "w-fig--wide")


def scoring():
    rows = [("Dialog focus bug (accessibility)", 3, 3, 3, 3, 1), ("Filter pattern for lists", 3, 2, 3, 2, 2),
            ("Month-range date picker", 1, 2, 2, 2, 2), ("Spreadsheet-style editable grid", 1, 3, 1, 2, 3)]
    body = "".join(f'<tr><td>{n}</td><td class="r">{a}</td><td class="r">{b}</td><td class="r">{c}</td><td class="r">{d}</td><td class="r">{e}</td><td class="r"><b>{(a + b + c + d) / e:.1f}</b></td></tr>' for n, a, b, c, d, e in rows)
    return fig(f'<div class="w-tbl"><table><thead><tr><th>Request</th><th class="r">Reach</th><th class="r">Impact</th><th class="r">Reuse</th><th class="r">Value</th><th class="r">Effort</th><th class="r">Score</th></tr></thead><tbody>{body}</tbody></table></div>',
               "Priority = (Reach + Impact + Reuse + Business value) ÷ Effort, each scored 1–3. An accessibility bug used everywhere scores 12; a complex grid for one team scores 2.3.")


def type_ratios():
    t = _j("type-scales")
    rows = ""
    for sc in t["scales"]:
        sizes = [z for z in sc["sizes"] if z["step"] >= -1][:6]
        cells = "".join(f'<span class="tr-s" style="font-size:{min(z["rounded"], 56)}px">Aa<em>{z["rounded"]}</em></span>' for z in sizes)
        rows += f'<div class="tr-row"><p><b>{sc["name"]}</b><span>× {sc["ratio"]}</span></p><div class="tr-sizes">{cells}</div></div>'
    return fig(f'<div class="tr">{rows}</div>',
               "Four type scales from the same 16px base. A small ratio (1.125) gives many sizes close together, which suits dense product screens; "
               "the golden ratio (1.618) jumps so fast it leaves few useful sizes for an app. Sizes are rounded to whole pixels.", "w-fig--wide")


def type_styles():
    t = _j("type-scales")
    rows = "".join(
        f'<tr><td><code>{x["token"]}</code></td><td class="r">{x["px"]}px</td><td class="r">{x["lineHeight"]}px</td><td class="r">{x["ratio"]:.2f}</td>'
        f'<td class="r">{x["weight"]}</td><td class="r">{x["tracking"]:+.3f}em</td></tr>' for x in t["productScale"])
    return fig(f'<div class="w-tbl"><table><thead><tr><th>Text style</th><th class="r">Size</th><th class="r">Line height</th><th class="r">Ratio</th><th class="r">Weight</th><th class="r">Tracking</th></tr></thead><tbody>{rows}</tbody></table></div>',
               "Twelve text styles in five families, from the Layer One playbook. Every line height is a multiple of 4px, and the line-height ratio tightens as text gets bigger: "
               "1.5 for body text, about 1.2 for display sizes. Large sizes get slightly tighter letter spacing; small labels slightly looser.")


def contrast_matrix():
    c = _j("contrast-matrix")
    steps = c["steps"]
    head = "".join(f'<th class="r">{x}</th>' for x in steps)
    body = ""
    for i, row in enumerate(c["neutral"]):
        cells = ""
        for j, v in enumerate(row):
            cls = "aa" if v >= 4.5 else ("lg" if v >= 3 else "no")
            cells += f'<td class="cm-{cls}">{v:.1f}</td>' if i != j else '<td class="cm-x">–</td>'
        body += f"<tr><th>{steps[i]}</th>{cells}</tr>"
    return fig(f'<div class="w-tbl cm"><table><thead><tr><th>Text ↓ · Bg →</th>{head}</tr></thead><tbody>{body}</tbody></table></div>'
               '<p class="cm-key"><span class="cm-aa">4.5:1 or more · any text</span><span class="cm-lg">3:1 to 4.5:1 · large text, borders, icons</span><span class="cm-no">below 3:1 · decoration only</span></p>',
               "Every pairing of the eleven neutral steps, computed. Read across from a text colour to a background. Because the lightness curve is shared, "
               "the pattern carries over to every hue: steps six or more apart pass 4.5:1 for body text (except next to step 50, which needs 700), and steps five or more apart always pass 3:1 for large text and borders.", "w-fig--wide")


def spacing_scale():
    vals = [(0.5, 2), (1, 4), (2, 8), (3, 12), (4, 16), (5, 20), (6, 24), (8, 32), (10, 40), (12, 48), (16, 64), (20, 80), (24, 96)]
    rows = "".join(f'<div class="ss-r"><code>space-{n:g}</code><i style="width:{px}px"></i><span>{px}px</span></div>' for n, px in vals)
    return fig(f'<div class="ss">{rows}</div>',
               "A spacing scale on a 4px base: thirteen values from 2 to 96px, drawn at actual size. Each name is the number of 4px units it contains, "
               "so space-6 is 24px. Plenty of choice at the small end, where 4px is visible; only a few steps at the large end.")


FIGS = {"palette": palette, "lightness": lightness, "hsl-vs-oklch": hsl_vs_oklch, "semantic": semantic, "pairs": pairs,
        "theme-preview": preview, "roi-years": roi_years, "break-even": break_even, "sensitivity": sensitivity,
        "budgets": budgets, "scoring": scoring, "type-ratios": type_ratios, "type-styles": type_styles,
        "contrast-matrix": contrast_matrix, "spacing-scale": spacing_scale}
