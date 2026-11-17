# -*- coding: utf-8 -*-
"""Build and validate the Layer One prospect CSVs.

Run:  python3 -I build_prospects.py   (from /home/user/layerone/reports)

Prospect Priority Score (0-100) = Fin + Org + Access + DS
  Fin    (0-25) Financial strength & funding. Guide: revenue >= Rs 1,000 Cr or funding >= $200M
                or unicorn 22-25; Rs 300-1,000 Cr or $100-200M 19-21; Rs 100-300 Cr or $50-100M 16-18;
                Rs 30-100 Cr or $20-50M 12-15; Rs 10-30 Cr or $5-20M 8-11; smaller 4-7; no data 3-5.
                -1/-2 for heavy losses or cash strain, +1 for profitability.
  Org    (0-20) Employee count & organisational scale. >=1,500: 18-20; 1,000-1,500: 16-17;
                500-1,000: 13-15; 250-500: 10-12; 100-250: 7-9; 50-100: 5-6; <50: 3-4;
                unknown or unreliable: 3-6 (conservative).
  Access (0-30) Product accessibility & testability. Freemium full web product 26-30;
                Free Trial self-serve 22-26; Freemium-limited (app-only/OTP/KYC gate, tools only) 18-24;
                Public Demo 15-21; site blocked / unverified -3 to -5; gated or D-lean 8-12.
  DS     (0-25) Product complexity & DS opportunity. Public/internal DS evidence + design hiring 21-25;
                design hiring + multi-surface 17-20; multi-surface/multi-role/multi-brand 12-16;
                single simple surface 8-11.
Tier: High >= 70, Medium 55-69, Low < 55.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prospects_primary_data import PRIMARY  # noqa: E402
from prospects_secondary_data import SECONDARY, SL  # noqa: E402

OUT = os.path.dirname(os.path.abspath(__file__))
PRIMARY_CSV = os.path.join(OUT, "layer_one_primary_prospects.csv")
SECONDARY_CSV = os.path.join(OUT, "layer_one_secondary_prospects.csv")
N_PRIMARY = 100

P_COLS = ["Company Name", "Website", "Industry", "Subcategory", "Founded Year", "Headquarters", "Total Funding",
          "Latest Funding Round", "Annual Revenue", "Revenue Year", "Employee Count", "Employee Data Year",
          "Product Name", "Product URL", "Signup URL", "Product Access Type", "Free Access Available",
          "Product Testability", "Design Team Evidence", "Design System Evidence", "Potential DS Opportunity",
          "Prospect Priority Score", "Priority Tier", "Research Sources", "Additional Notes"]
S_COLS = ["Company Name", "Website", "Industry", "Subcategory", "Founded Year", "Headquarters", "Total Funding",
          "Latest Funding Round", "Annual Revenue", "Revenue Year", "Employee Count", "Product Access Type",
          "Reason Excluded From Primary", "Potential DS Opportunity", "Research Sources", "Additional Notes"]

LIMITS = dict(fin=25, org=20, acc=30, ds=25)
ACCESS_OK = {"Freemium", "Free Trial", "Public Demo"}
SEC_ACCESS_OK = {"Enterprise / Sales-led", "No Accessible Product", "Listed/Acquired/Pre-2015"}


def tier(score):
    return "High" if score >= 70 else ("Medium" if score >= 55 else "Low")


def score(r):
    for k, lim in LIMITS.items():
        assert 0 <= r[k] <= lim, (r["name"], k, r[k])
    return r["fin"] + r["org"] + r["acc"] + r["ds"]


def notes_for(r):
    parts = []
    if r["notes"]:
        parts.append(r["notes"].rstrip("."))
    if r["missing"] and "score limited by missing data" not in r["notes"].lower():
        parts.append("Score limited by missing data")
    if r["dlean"] and "d-lean" not in r["notes"].lower():
        parts.append("D-lean access: scored as gated")
    parts.append("Score: Fin %d/25, Org %d/20, Access %d/30, DS %d/25" % (r["fin"], r["org"], r["acc"], r["ds"]))
    return ". ".join(parts)


def src(lst):
    return " | ".join(lst) if lst else "No source URL captured in research notes (background lead)"


def build():
    names = [r["name"] for r in PRIMARY]
    assert len(names) == len(set(names)), "duplicate primary candidate"
    for r in PRIMARY:
        assert r["access"] in ACCESS_OK, r["name"]
        r["score"] = score(r)
    ranked = sorted(PRIMARY, key=lambda r: (-r["score"], -r["acc"], -r["ds"], r["name"]))
    primary = ranked[:N_PRIMARY]
    cut = ranked[N_PRIMARY:]

    with open(PRIMARY_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
        w.writerow(P_COLS)
        for r in primary:
            w.writerow([r["name"], r["website"], r["industry"], r["sub"], r["founded"], r["hq"], r["funding"],
                        r["latest"], r["rev"], r["revyr"], r["emp"], r["empyr"], r["product"], r["purl"], r["surl"],
                        r["access"], r["free"], r["test"], r["dteam"], r["dsev"], r["dsopp"], r["score"],
                        tier(r["score"]), src(r["sources"]), notes_for(r)])

    # D-lean candidates that fell below the cut are sales-led in practice -> secondary.
    sec = list(SECONDARY)
    watch = []
    for r in cut:
        if r["dlean"]:
            sec.append(dict(name=r["name"], website=r["website"], industry=r["industry"], sub=r["sub"],
                            founded=r["founded"], hq=r["hq"], funding=r["funding"], latest=r["latest"], rev=r["rev"],
                            revyr=r["revyr"], emp=r["emp"], access=SL,
                            reason="Employer-led (D-lean): public surface limited to tools/employee app; scored %d, below the primary cut." % r["score"],
                            dsopp=r["dsopp"], sources=r["sources"], notes=r["notes"]))
        else:
            watch.append(r)
    snames = [s["name"] for s in sec]
    assert len(snames) == len(set(snames)), "duplicate secondary"
    assert not set(snames) & {r["name"] for r in primary}, "overlap primary/secondary"
    for s in sec:
        assert s["access"] in SEC_ACCESS_OK, s["name"]

    with open(SECONDARY_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
        w.writerow(S_COLS)
        for s in sorted(sec, key=lambda s: (s["access"], s["industry"], s["name"])):
            w.writerow([s["name"], s["website"], s["industry"], s["sub"], s["founded"], s["hq"], s["funding"],
                        s["latest"], s["rev"], s["revyr"], s["emp"], s["access"], s["reason"], s["dsopp"],
                        src(s["sources"]), s["notes"] or "No additional notes"])
    return primary, cut, watch, sec


def validate(path, cols, expect_rows=None):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0] == cols, "header mismatch in " + path
    body = rows[1:]
    bad = [i for i, r in enumerate(body) if len(r) != len(cols)]
    assert not bad, ("ragged rows", bad)
    names = [r[0].strip().lower() for r in body]
    assert len(names) == len(set(names)), "duplicate names in " + path
    if expect_rows is not None:
        assert len(body) == expect_rows, (path, len(body))
    raw = open(path, encoding="utf-8").read()
    assert raw.startswith('"Company Name"'), "not fully quoted"
    return len(body)


if __name__ == "__main__":
    primary, cut, watch, sec = build()
    n1 = validate(PRIMARY_CSV, P_COLS, N_PRIMARY)
    n2 = validate(SECONDARY_CSV, S_COLS)
    print("primary rows", n1, "secondary rows", n2)
    tiers = {}
    for r in primary:
        tiers[tier(r["score"])] = tiers.get(tier(r["score"]), 0) + 1
    print("tiers", tiers)
    print("cut line score", primary[-1]["score"], "| first excluded", cut[0]["name"], cut[0]["score"] if cut else None)
    print("WATCHLIST (A/B/C access, below cut):")
    for r in watch:
        print("  %s %d (%s)" % (r["name"], r["score"], r["access"]))
    print("D-lean moved to secondary:", [r["name"] for r in cut if r["dlean"]])
    print("TOP 25:")
    for i, r in enumerate(primary[:25], 1):
        print("  %2d %-40s %3d  F%d O%d A%d D%d  %s" % (i, r["name"], r["score"], r["fin"], r["org"], r["acc"], r["ds"], r["industry"]))
    ind = {}
    for r in primary:
        ind.setdefault(r["industry"], []).append(r["score"])
    for k, v in sorted(ind.items(), key=lambda kv: -len(kv[1])):
        print("  %-14s n=%2d avg=%.1f high=%d" % (k, len(v), sum(v) / len(v), sum(1 for x in v if x >= 70)))
    acc = {}
    for r in primary:
        acc[r["access"]] = acc.get(r["access"], 0) + 1
    print("access", acc)
