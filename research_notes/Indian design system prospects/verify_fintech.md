# Indian Fintech verification pass (lending + wealth/payments/fin-SaaS) - Layer One prospects

Date: 2026-11-17. Method: public pages read with curl/WebFetch (titles, link and button text), plus ~13 web searches. entrackr.com and inc42.com are NOT fetchable in this sandbox (host does not resolve for WebFetch); their figures appear only via search-result summaries, labelled "(via search)". GitHub org pages/API are blocked (403) and npm scope search returned nothing, so "DS evidence: none found" means "not searchable here", NOT "company lacks one". Design-team evidence is mostly not visible because careers pages are JS/ATS-rendered; only static hits are recorded. No accounts created, no forms submitted.

Access categories: A Freemium, B Free trial, C Public demo, D Sales-led, E none (marketing only). Many consumer lenders are app-first: signup is by phone OTP in the app (not tested, by rule); I record the public entry URL.

# PART 1 - LENDING / CONSUMER CREDIT

## Takeaway
16 qualified primaries (15 + Fi flagged low-priority). Newly checked: mPokket, TrueBalance, CreditMantri (primaries); Refyne, Kaleidofin moved to secondary. Founded-year flag: Moneyview (2014) older than preferred window.

## PRIMARY records

### 1. KreditBee - website https://www.kreditbee.in/ ; subcategory: instant personal loans
- Founded 2018 (most sources; two say 2017); HQ Bengaluru. Funding: Series D ~$200M+ (Dec 2022-early 2023, Advent $100M). Valuation: ~$680-700M then (reported); $1.5B figure from one aggregator unconfirmed (earlier notes). Revenue FY25 Rs 2,185 Cr, PAT Rs 221 Cr (Angel One, from earlier notes). Employees: estimates conflict 1,083 / 1,261 (Mar 2024) / ~1,839 (Inc42) / ~1.6K (LeadIQ, Dec 2025) - aggregators only.
- Product: KreditBee app. Entry: Play Store/App Store app + https://www.kreditbee.in/ (marketing site, "Get started"/register CTAs). Access: app-only phone-OTP onboarding; Category A-ish (free signup, real product reachable only after KYC) - Limited. Explorable: loan flow up to offer in app (not tested).
- Design team: careers on Darwinbox https://kreditbee.darwinbox.in/ms/candidatev2/main/careers/home (JS; roles not readable). DS evidence: none found.
- Source: [kreditbee.in](https://www.kreditbee.in/), [thekredible](https://thekredible.com/company/kreditbee/overview). Changed: confirmed site live, founded/HQ/headcount added; access verified as app-first.

### 2. Moneyview - https://moneyview.in/ ; personal loans + credit score + cards + gold
- Founded Aug 2014 (PrivateCircle) - OLDER than window, flag; HQ Bengaluru. FY25 revenue ~Rs 2,339 Cr, profit Rs 240 Cr ([Entrackr via search](https://entrackr.com/fintrackr/moneyview-profit-grows-to-rs-240-cr-in-fy25-revenue-surges-74-10621058)). Funding/valuation/employees: Not publicly disclosed in sources found.
- Entry: web logins per product (e.g. https://moneyview.in/check-credit-score-free/login, /credit-cards/login, /digital-gold-investment/login, /home-loan/login) plus app; free credit-score check = freemium. Access: A (free account reaches real credit-score product). Multi-product (loans, cards, UPI, gold, insurance) = real surface variety.
- Design team: https://moneyview.in/careers static code references a "Design pod" / "UIDesigner" / "UX writer" section (job-category anchors) - evidence of in-house design function. DS: none found.
- Changed: access now verified A; design hiring evidence found; flagged 2014 founding.

### 3. Fibe (ex-EarlySalary) - https://www.fibe.in/ ; salary/personal loans
- Founded 2015, HQ Pune (CB Insights). FY25 revenue conflict: >Rs 1,200 Cr ([Entrackr via search](https://entrackr.com/fintrackr/fibe-crosses-rs-1200-cr-revenue-in-fy25-profit-spikes-13-11121260)) vs Rs 1,033 Cr operating (Angel One). Employees: not found.
- Entry: Play Store https://play.google.com/store/apps/details?id=com.earlysalary.android ; App Store id1094602630. Access: app-only, A/limited. Design/DS: none found. Changed: founded/HQ confirmed; app links verified.

### 4. Kissht (OnEMi Technology) - https://kissht.com/ (returns 403 to scripted fetch; site exists) ; instalment loans + credit line
- Founded 2015 (Bouncewatch) / 2016 (Dealroom); HQ Mumbai. FY25 revenue Rs 1,337 Cr, profit ~Rs 161 Cr ([Inc42](https://inc42.com/buzz/kissht-parents-fy25-profit-declines-18-to-inr-161-cr)); IPO-bound. Employees ~2,053 (Bouncewatch, aggregator, year unspecified).
- Access: app-only/unverified (site blocked); Limited. Design/DS: none found. Changed: founded/HQ/headcount added; access still unverified (403).

### 5. Stashfin - https://www.stashfin.com/ (Cloudflare 403 to script) ; credit line / personal loans
- Delhi-based (background, unverified); funding ~$424M+ (Inc42) / $458M (CB Insights), conflicting; FY24 revenue figures conflict (see earlier notes). Access unverified (blocked); likely app-first Limited. Design/DS: none found. Changed: no new facts; site blocked.

### 6. Uni Cards - https://www.uni.cards/ (Cloudflare challenge) ; pay-later card
- Founded 2019, Bengaluru (background). $70M Series A Dec 2021 (~$350M); FY25 rev ~Rs 95-106 Cr, loss ~Rs 151 Cr (aggregator); reported down-round talks. Access: app/card application, unverified. Priority: lower (cash-strapped).

### 7. OneCard (FPL Technologies) - https://www.getonecard.app/ ; metal credit card + app
- FY25 operating revenue Rs 1,878 Cr, loss Rs 297.5 Cr ([Entrackr](https://entrackr.com/fintrackr/onecard-posts-rs-1878-cr-revenue-in-fy25-cuts-losses-by-26-10954999)). Site live (verified title). Founded 2019 / Pune (background). Access: card application via app; Limited. Design/DS: none found.

### 8. Jupiter - https://jupiter.money/ ; neobank app (UPI, cards, loans)
- Site live ("1-app For Everything Money"). Financials per earlier notes (FY24 rev Rs 35.85 Cr, loss Rs 275.9 Cr; Rs 115 Cr raised 2025). Access: free app signup (OTP) - A (app-only). Design/DS: none found.

### 9. Freo (ex-MoneyTap) - https://freo.money/ ; loans, UPI, digital gold, insurance app
- Site live (Framer-built site; careers page https://freo.money/careers exists). Funding conflicting $46-90M; profitable since Dec 2023 (aggregator). Access: app, A/limited. Design/DS: none found.

### 10. Rupeek - https://rupeek.com/ (403 to script) ; gold loans, Bengaluru; funding $143-216M conflicting; peak valuation ~$634M (Jan 2022) then ~60% cut; seeking ~$50M (Feb 2026, via search). Headcount ~1,600 (aggregator). Access unverified (home-service model; Limited).

### 11. Indiagold - https://indiagold.co/ ; gold loan (home service); site live. Series A ext ~$22M. Access: application form/app; Limited. Small revenue; lower priority.

### 12. Snapmint - https://snapmint.com/ ; no-cost EMI/BNPL; Play Store com.snapmint.customerapp; ~$125M round 2025 (General Atlantic), FY25 rev >Rs 150 Cr profitable. Access: app A/limited.

### 13. mPokket (NEW verified) - https://www.mpokket.in/ ; student/young-adult instant loans
- Product entry: web app https://web.mpokket.in/ ("Get Instant Personal Loans up to Rs 2,00,000") + Play Store com.mpokket.app. A browser web app exists - good for review. Access: A/Limited (OTP sign-in, not tested). FY24: revenue ~Rs 1,355 Cr, PAT Rs 171 Cr (Inc42 via search; verify - unusually high vs earlier years). Founded ~2016 / HQ Kolkata-Bengaluru: Not verified. Careers page /careers present, no design roles readable. DS: none found.

### 14. TrueBalance (Balance Hero) - https://www.truebalance.io/ ; instant personal loans
- Entry: web onboarding https://app.truebalance.io/onboarding/landing + Play Store com.balancehero.truebalance + App Store id6752374449 (new app listing). FY24 profit ~Rs 138 Cr (Entrackr headline via search; body not read). Founded/HQ: Not verified (Balance Hero is Korean-founded; India operations). Careers /careers exists. Access: A/Limited.

### 15. CreditMantri - https://www.creditmantri.com/ ; credit score + loan marketplace
- Entry: https://www.creditmantri.com/getstarted/?act=register ("Check Free Credit Score") + Play Store com.creditmantri. Access: A (free account reaches real credit report/score product). FY25 revenue ~Rs 43.5 Cr, loss ~Rs 3.7 Cr (Inc42 via search). Founded 2013/Chennai (background; OLDER than window - flag). Smaller; mid priority.

### 16. Fi Money - https://fi.money/ - CAUTION: cash-strapped, B2B pivot (earlier notes). Keep as low-priority primary.

## SECONDARY / excluded (lending)
- Refyne (https://www.refyne.co.in/): B2B employer-led earned-wage-access infrastructure; homepage is a ~3 KB shell "Financial Infrastructure for Working India"; funding $82M Series B Jan 2022 (Tiger) total ~$106M; no public self-serve. Category D.
- Kaleidofin: B2B2C / partner-led inclusive finance; no public signup. D.
- Progcap, FlexiLoans, Indifi, Lendingkart, Oxyzo: MSME assisted/B2B (earlier notes). Simpl (halted), ZestMoney (shut): excluded.
- FlexSalary: not checked (no data found).

# PART 2 - WEALTH / PAYMENTS / FINANCIAL SAAS

## Takeaway
23 qualified primaries. Acquired/moved to secondary: Fyle, Kuvera, Happay, Setu. Strongest explorable-without-sales: Cashfree and Easebuzz (self-serve gateway dashboards), PayGlocal (documented sandbox), Decentro (signup), Refrens/Vyapar/myBillBook/OkCredit (free tiers), Dhan/Sensibull/INDmoney/Stable Money (free signup).

## PRIMARY records

### 1. Cashfree Payments - https://www.cashfree.com ; payments infra. Founded 2015, Bengaluru (background). FY25 rev ~Rs 640 Cr, loss Rs 154 Cr; Series C $53M Feb 2025 (Krafton, Apis); valuation ~$700M (secondary); employees ~943 (Inc42, year unspecified). Entry: https://merchant.cashfree.com/merchants/signup ("Sign up with Cashfree"); sandbox docs https://www.cashfree.com/docs/payments/online/resources/sandbox-environment.md (test before activation). Access A (test-mode dashboard). Careers: https://www.cashfree.com/careers/. DS: none found. Changed: signup URL verified.

### 2. Easebuzz - https://easebuzz.in ; payments. FY25 rev ~Rs 656 Cr, PAT ~Rs 19 Cr; $30M Series A Apr 2025 (Bessemer). Entry: https://dashboard.easebuzz.in/register (title "Payment Gateway Dashboard", live). Access A/B (self-serve merchant signup; test-mode not confirmed). Founded ~2016 / Pune unverified.

### 3. INDmoney - https://www.indmoney.com ; wealth super-app. FY25 operating rev ~Rs 164 Cr, loss ~Rs 76 Cr. Site live with Login/register CTAs; free app signup A. Founded ~2019 unverified.

### 4. Smallcase - https://www.smallcase.com ; FY25 rev ~Rs 106 Cr; $50M Series D Mar 2025. Site live. Free signup via broker login A. 

### 5. Stable Money - https://stablemoney.in/ ; FD/bond/MF; site live with register/login; A (app+web). Funding $25M Peak XV at $175M (Entrackr). FY25 revenue conflicting (see earlier notes).

### 6. Wint Wealth - https://www.wintwealth.com/ ; bonds ("Start with Rs 1000"); live; A. FY25 rev Rs 44.5 Cr; Series B ~Rs 250 Cr at ~Rs 700 Cr valuation (conflict with Rs 120 Cr).

### 7. Vyapar - https://vyaparapp.in/ ; GST billing. "Free Plan Available" and "free trial" text on homepage; desktop + mobile. Access A/B. FY25 rev Rs 69-77 Cr, loss ~Rs 63 Cr; funding ~$35M, last Jan 2022.

### 8. Dhan (Raise Financial Services) - https://dhan.co/ ; broking/trading. Founded: Not verified here (Raise started ~2021; background). Series B $120M Oct 2025 at $1.2B valuation (Hornbill, MUFG, Beenext) - [Entrackr](https://entrackr.com/news/dhan-turns-unicorn-after-120-mn-fundraise-led-by-hornbill-capital-10532947); total funding $142M (Inc42, via search); FY25 revenue Rs 877-904 Cr, profit Rs ~408 Cr (Inc42 via search). Employees conflict 572 (Inc42) vs ~100 (TrueUp). Entry: web trading app https://web.dhan.co/ ("Dhan Web") and https://login.dhan.co/ ; also DhanHQ API. Access A (free demat account; login required). Strong prospect: unicorn, profitable, web+mobile+API+TradingView. Mumbai HQ (background, unverified). DS: none found (check madefortrade.in / developer docs). Careers: not readable.

### 9. Grip Invest - https://grip.in/ (root returns directory index/odd page via script; app/web exists) ; alternative investments. Founded ~2020, Gurugram? unverified. $10M Series B Jan 2024 (Stride); total ~$14M; FY25 revenue Rs 12.1 Cr (Inc42) vs Rs 17.7 Cr, loss ~Rs 28 Cr. Small; mid-low priority. Access: A (app/web signup, unverified).

### 10. Jiraaf - https://www.jiraaf.com/ ; fixed-income marketplace; Sign Up/Login on site. FY25 revenue ~Rs 20 Cr, loss Rs 25.75 Cr (Indian Startup Times); funding $16.2M (CB) to ~$22M (Venture Intelligence). Small. A.

### 11. Dezerv - https://dezerv.in (403 to script) ; wealth management (HNI), Bengaluru, founded 2021. FY25 rev Rs 66 Cr, loss Rs 112 Cr ([Entrackr](https://entrackr.com/fintrackr/dezerv-reports-rs-66-cr-revenue-in-fy25-employee-costs-climb-to-rs-111-cr-11066163)); Series C ~Rs 350 Cr/$40M Oct 2025; total ~$99M; valuation ~$298M (Inc42). Employees ~624 (Inc42) vs 51-200 (Parsers) conflict. Access: effectively D/E (HNI onboarding, min ticket; no free product) - borderline; kept primary only because app exists; downgrade to secondary if strict.

### 12. Sensibull - https://sensibull.com/ ; options analytics. Web app https://web.sensibull.com/login (broker-linked login; many features free per homepage); also /app.html. Rainmatter seed 2018 (Rs 2.5 Cr). FY24 revenue ~Rs 39.8 Cr (database, low confidence); employees ~38-42 (stale). A (broker login required). Founded 2016-17 / Bengaluru (background).

### 13. Liquide - https://liquide.life/ ; trading ideas/research app, careers page /careers; Play Store life.liquide.app. No financials found. A/app-only.

### 14. Univest - https://univest.in/ ; founded 2022 (Pranit Arora et al.); FY25 revenue Rs 44.1 Cr, loss Rs 30 Cr ([Inc42 via search](https://inc42.com/buzz/univest-on-track-to-achieve-profitability-in-fy26-ceo-pranit-arora/)). Apps on Play/App Store. A/app-only.

### 15. Jar - https://jar.app/ (did not respond to curl) ; digital gold savings. Founded 2021; FY25 operating revenue Rs 208 Cr per Entrackr ([link](https://entrackr.com/news/jar-clocks-rs-208-cr-operating-revenue-in-fy25-turns-profitable-in-h2-10478229)) vs Rs 2,448 Cr after accounting change (Inc42) - conflict explained by gross vs net gold revenue; FY25 loss Rs 50.5 Cr; 35M+ users claimed; funding >$111M, $22M Series B at $300M (Inc42). A (app-only).

### 16. myBillBook (FloBiz) - https://mybillbook.in/ ; billing. "Sign up for free" + free demo (https://freetrial.mybillbook.in/book-free-demo-ctr.html), /free/invoicing-software/, free invoice generator; Play Store com.valorem.flobooks; careers on Keka https://valorem.keka.com/careers/. Access A/B. Funding $31M Series B Sep 2021 (Sequoia, Think), total ~$44M; FY24 revenue conflict Rs 38.9 Cr vs "Rs 4.1 Cr profit"; FY25 not found. Founded 2018? unverified; Bengaluru.

### 17. Khatabook - https://khatabook.com/ ; ledger app. Site is JS-only shell via curl. Series C $100M (2021, older note); FY24 revenue ~Rs 102.7 Cr ([YourStory](https://cwv.yourstory.com/2024/11/ms-dhoni-backed-khatabook-clocks-rs-1027-cr-revenue-cuts-losses-7-in-fy24)); 40+ layoffs reported (date unverified). FY25: not found. Founded 2018 Bengaluru (background). Access A (free app).

### 18. OkCredit - https://okcredit.in/ ; ledger. Web app https://web.okcredit.in/ + Android/iOS/Web ("Free digital bahi khata"). FY25 loss Rs 23.2 Cr (Inc42 via search). Founded 2017 Bengaluru (background). A.

### 19. Refrens - https://www.refrens.com/ ; accounting/invoicing. Entry https://www.refrens.com/register (Continue with Google); free plan, "no credit card" (https://www.refrens.com/free-accounting-software). FY25 revenue Rs 5.5 Cr, loss Rs 2.6 Cr (Indian Startup Times). Small but excellent self-serve access: A. Founded 2018-19 / Bhopal? unverified.

### 20. Open (Open Financial Technologies) - https://open.money/ ; business banking/spend SaaS. Entry https://open.money/signup + https://app.open.money/login; "Get started" and "Book a demo". Careers https://open.money/company/careers: "hiring across engineering, design, product, GTM and operations" (15+ departments, Bengaluru HQ) - design hiring evidence. Funding conflict $187M (CB) vs $437M; employees ~438 (Bouncewatch). Revenue FY25 not found. Access: Limited/B (signup real, business KYC likely gates features - not tested). Founded 2017.

### 21. PayGlocal - https://payglocal.in/ ; cross-border payments. Dev docs https://payglocal.in/developers; homepage advertises "Full sandbox environment". Round: Rs 36.38 Cr (~$3.84M) led by Beenext at Rs 1,140 Cr (~$120M) valuation (Dealroom/Newsbytes, via search); $12M Series B 2022; FY25 revenue ~Rs 25 Cr (~$3.4M), loss ~Rs 14 Cr. Bengaluru. Access: sandbox documented, signup via Get Started - A/B (not tested). Founded ~2019 (background).

### 22. Decentro - https://decentro.tech/ ; payments/KYC/lending APIs. Entry https://decentro.tech/signup. ~$3.6M Series B (flip back to India); FY24 revenue Rs 17.7 Cr (+47%) (TheKredible via search). Access: B/A (developer signup; sandbox not seen in homepage text). Small.

### 23. Fello - https://fello.in/ ; digital gold + savings/games app; Play Store in.fello.felloapp. No financials found. A (app-only). Small; low priority.

## Not qualified / unverified
- Fisdom (https://fisdom.com/): site live (mutual funds), login at app.fisdom.com/login returned 404 to script; PayU-led $7M round noted on site; current ownership/entity status not verified; founded 2015 Bengaluru (background). Keep as "to verify"; careers at /careers/.

## SECONDARY / acquired (wealth/payments/SaaS)
- Fyle: acquired by Sage, announced 28 Jul 2025 ([Sage](https://www.sage.com/investors/investor-downloads/press-releases/2025/07/sage-acquires-fyle-to-simplify-and-automate-expense-management-workflows-for-smbs)); now Sage Expense Management; founded 2016 Bengaluru; deal value $90-94M (unconfirmed).
- Kuvera: CRED announced acquisition Feb 2024 ([TechCrunch](https://techcrunch.com/2024/02/06/cred-acquires-mutual-fund-startup-kuvera-in-wealth-management-push/)); continues as stand-alone app; CRED is excluded household -> subsidiary.
- Happay: CRED acquired (announced ~$180M valuation, [Inc42](https://inc42.com/?p=270037)); search also reports MakeMyTrip business-transfer agreement for Happay - dates unconfirmed. Subsidiary -> secondary.
- Setu: Pine Labs acquired for ~$70M, June 2022 -> subsidiary, secondary.
- EnKash: sales-led corporate payments/spend; revenue fell 77% to Rs 71 Cr in FY25 ([Entrackr](https://entrackr.com/fintrackr/enkashs-revenue-nosedives-77-in-fy25-halves-losses-10590754)); funding ~$23.5M; enkash.com did not return a readable page here; access unverified. Secondary.
- From earlier notes (unchanged): Zeta, M2P, Signzy, IDfy, Hyperface (sales-led); Recur Club, Mintifi (lending-adjacent).

## Gaps
- Design-team and DS evidence: not found for nearly all (JS careers pages; GitHub/npm blocked or empty). Only static hits: Moneyview careers (Design pod / UI designer), Open careers (design among departments). Recommend manual LinkedIn/Dribbble/Medium sweep.
- Founded/HQ marked "background" are not sourced here.
- Access for consumer lenders is app-first and phone-OTP gated; not tested per rules.
- Unreachable to scripts (403): kissht.com, stashfin.com, uni.cards, rupeek.com, dezerv.in; jar.app and enkash.com timed out.
- Revenue conflicts retained (Fibe, Jar, Grip, Stable Money, Vyapar, Wint size); mPokket FY24 figure should be double-checked.
