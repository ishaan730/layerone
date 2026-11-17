# Verification pass: Indian insurtech and healthtech prospects for Layer One (design-systems consulting)

Research date: 2026-11-17. Method: public pages read via curl/HTML (title, CTA button text, store links), Inc42 company/financials pages (read via curl), npm registry search, GitHub-hosted job boards, ~14 WebSearch calls. No accounts, logins, forms, OTPs or quotes were used. WebFetch could not resolve hosts in this session (ENOTFOUND), so curl was the fetch method.

Conventions. Access: A Freemium / B Free trial / C Public demo / D Sales-led / E none. "Limited" = free public tools or a consumer app exist but the real product needs enrolment, a phone number/OTP (not tested), or an advisor call. "Inc42" figures come from inc42.com/company/<slug>/ and /financials/ pages (aggregator; "Founded" is often incorporation year; "employees" is a 2026 snapshot, probably LinkedIn-derived and sometimes inflated). "ND" = not publicly disclosed / not found. Design-system evidence: no company showed a public Storybook, docs site or design-system npm package in my checks; "none found" means not found in the limited checks (npm registry search, job text, web search), never a claim they lack one.

## Insurtech: verified records (14 qualified primary)

### Takeaway
Only about half of the earlier insurtech list has a genuinely free public entry. Truly public (consumer calculators, compare tools, or free app): Ditto, InsuranceDekho, Coverfox, OneAssure, Turtlemint, SecureNow, Insurance Samadhan, Beshak, BimaKavach, Nova Benefits. The four employer-benefit platforms (Plum, Onsurity, Pazcare, Loop) are kept as "primary-conditional" (D-lean): they have public employee apps/tools but the real product needs employer enrolment or a demo. Strongest design signals: Loop Health (Product Designer and Senior Product Designer roles posted Jul 2026, mentions Loop App + B2B + ops tools), Zopper (named Head of Product Design and Behance design team page), Ditto (UI/UX designer roles), Plum (Product Designer on careers page).

### Cited Findings

#### 1. Ditto Insurance (Finshots-linked, Zerodha-backed) - UPDATED
- Website https://joinditto.in | Subcategory: consumer insurance advisory and distribution | Founded: 2018 per [Inc42](https://inc42.com/company/ditto-insurance/) (earlier note had none) | HQ: Bengaluru (J.P. Nagar office per job listings, [Y-Axis job post](https://jobs.y-axis.com/jobs/ui-ux-designer-ditto-by-finshots))
- Funding: total not on Inc42 profile; earlier notes: Rs 4 Cr Zerodha Dec 2021, Series A ~2023, TheKredible total Rs 34.01 Cr (unreconciled) | Latest round: Seed/Series A, 31 Mar 2023 per Inc42 | Valuation: ND
- Revenue: Rs 97.1 Cr FY25 (+85.7% from Rs 52.3 Cr), PAT Rs 31.6 Cr, per [Inc42 financials](https://inc42.com/company/ditto-insurance/financials/) (reported; RoC-based figure not independently found; Entrackr has no FY25 Ditto article in search)
- Employees: Inc42 shows 1,488 (2026; likely LinkedIn count including advisors, treat as unreliable); true headcount ND
- Product: Ditto advice-to-purchase journey | Product URLs: https://joinditto.in/term-insurance/cover-calculator/ , https://joinditto.in/health-insurance/compare-plans/ , https://joinditto.in/health-insurance/buy-health-insurance/ | Entry: calculator page says it works "without asking for your phone number or email"; purchase goes via "Book a free call" with an advisor
- Access: A (Limited). Free: yes for tools; buying is advisor-led. Explorable: cover calculator, premium calculator, plan comparison pages, checklists
- Design team: UI/UX Designer (Bengaluru, in-office, listing dated 24 Dec 2025) and "Senior UI/UX Designer, Figma-based tech team" (Ditto's Freshteam application page) via third-party boards ([jobr.pro](https://jobr.pro/job/35936726/uiux-designer)); careers hub https://ditto.zappyhire.com/ (JS page, roles not readable). Status of listings may be stale
- DS evidence: none found
- DS opportunity: consumer web + content + calculators across health and term lines, profitable and growing, small design team hiring (inference)
- Notes: Ditto's Inc42 profile is thin; the earlier FY25 revenue figure is now confirmed on Inc42 financials page.

#### 2. InsuranceDekho (Girnar Insurance Brokers) - UPDATED
- Website https://www.insurancedekho.com | Subcategory: B2C + agent (POSP) marketplace | Founded: 2016 (Inc42; Girnar group origin earlier) | HQ: Gurugram (not verified this pass)
- Funding: $430M+ per [Inc42](https://inc42.com/company/insurancedekho/) (earlier trackers $300-362M; unresolved) | Latest round: Mar 2025, undisclosed (earlier note $70M Series C) | Valuation: ND (third-party estimates $650-775M)
- Revenue: Rs 1,311.5 Cr FY25 (+67.1%), net loss Rs 47.5 Cr per [Inc42 financials](https://inc42.com/company/insurancedekho/financials/); earlier note ~Rs 1,290 Cr; Inc42 article gave Rs 47.49 Cr loss
- Employees: 2,479 (Inc42, 2026)
- Product URLs: https://www.insurancedekho.com/health-insurance/premium-calculator , /car-insurance/quotes-page , /life-insurance/quotes-page , /dashboard (Download Policy) | Entry: public calculators and quote pages; Login link
- Access: A (Limited: quote pages public; whether a quote needs phone entry not tested). Careers: https://careers.insurancedekho.com/ (no design role text readable). Design evidence: a Behance profile of a Senior UI Designer at InsuranceDekho since 2014 (candidate profile, not a posting)
- DS evidence: none found | DS opportunity: many lines (motor, health, life, travel), B2C + agent apps, post-RenewBuy merger consolidation (merger reported earlier, unverified) | Notes: larger and near-household in tier-2/3; IPO DRHP reported planned.

#### 3. Coverfox - NEW (gap-fill)
- Website https://www.coverfox.com | Subcategory: B2C retail + enterprise insurance | Founded: 2013 per [Inc42](https://inc42.com/company/coverfox/) (outside 2015+ window; flag) | HQ: Bengaluru/Mumbai region (Inc42 snippet; about page says Bangalore tech team; not confirmed)
- Funding $56.8M+ (Inc42); latest Series C 23 Jul 2019 | Valuation ND | Revenue Rs 61.6 Cr FY25 (+325%), PAT Rs 71.4 lakh per [Inc42 financials](https://inc42.com/company/coverfox/financials/) | Employees 519 (Inc42, 2026)
- Product: Coverfox website and app | URLs: https://www.coverfox.com/term-insurance/buy-term-insurance/ , https://www.coverfox.com/car-insurance/car-insurance-premium-calculator/ , login /user-login/ , Android https://play.google.com/store/apps/details?id=com.coverfox.app , iOS https://apps.apple.com/in/app/coverfox-insurance/id1616646614
- Access: A. Explorable: premium/IDV/term calculators, compare and buy pages, free app
- Design: careers page lists Software Developer (Frontend Engineer) "UI/UX and development", React, "build reusable components and front-end libraries" ([careers](https://www.coverfox.com/careers/)); a design role not found | DS: none found; frontend component-library language only
- DS opportunity: React frontend already building reusable components; rebranding to "Retail and Enterprise Insurance Solutions" suggests a dual-surface product (inference)

#### 4. OneAssure - UPDATED
- Website https://www.oneassure.in | Health and term distribution | Founded 2019 per [Inc42](https://inc42.com/company/oneassure/) | HQ Bengaluru (earlier note) | Funding $657K+ pre-seed Dec 2021 (Inc42) | Valuation ND | Revenue Rs 1.0 Cr+ FY25 (Inc42 header; earlier note Rs 3.7 Cr; unresolved) | Employees 48 (Inc42, 2026)
- URLs: https://www.oneassure.in/compare-health-insurance-plans ("Get a Free Quote", "Book a Free Call", "Talk to PolicyPal" AI chat https://www.oneassure.in/ask-me-anything), plus many free health calculators
- Access: A (Limited). Design: UI/UX Designer opening on Wellfound ([listing](https://wellfound.com/jobs/1168568-ui-ux-designer), via search; date not read); careers page lists engineering roles | DS: none found
- Notes: very small; budget risk. Borderline qualified.

#### 5. Nova Benefits - NEW (gap-fill; was flagged unverified)
- Website https://www.novabenefits.com | Employee benefits broker platform | Founded 2020 per [Inc42](https://inc42.com/company/nova-benefits/) | HQ: ND (not verified) | Funding $11.0M+, latest 9 May 2022 (Inc42) | Valuation ND | Revenue Rs 7.8 Cr FY25 (down 10.5%), loss Rs 4.6 Cr per [Inc42 financials](https://inc42.com/company/nova-benefits/financials/) | Employees 128 (Inc42, 2026)
- Entry points: "Get an estimated quote" https://app.novabenefits.com/policy-calculator/get-started (returns a page shell titled "Nova - Health and Wellness Benefits for teams"; content is JS-rendered so fields unverified), "Sign in" https://portal.novabenefits.com/ , employee app https://play.google.com/store/apps/details?id=com.novabenefits and iOS id1561333321
- Access: A/D Limited (self-serve estimate calculator for HR buyers; sign-in portal; Request flow unverified). Design: careers page shows AI Automation Engineer only; no designer found | DS: none found
- DS opportunity: HR portal + employee app + calculator across web/mobile (inference)

#### 6. Turtlemint - MOVED FROM SECONDARY (note: consumer site exists)
- Website https://www.turtlemint.com | Distribution; consumer storefront https://www.turtlemintinsurance.com/ (Compare Plans, premium calculators, "Download Turtlemint App", free advice) and agent product TurtlemintPro | Founded 2015 (Inc42), listed company (Turtlemint Fintech Solutions Ltd; Inc42 page shows Listed) | HQ Mumbai (not verified this pass) | Revenue: FY25 Rs 662.7-674.5 Cr, FY26 Rs 1,098.3 Cr (+57%) per earlier notes (see [Inc42](https://inc42.com/company/turtlemint/)); employees ND this pass
- Access: A (Limited). Design/DS: not checked this pass | Notes: listed, large, so less typical for a small consultancy; keep as stretch account. Earlier agent-login exclusion is softened because a consumer compare flow exists.

#### 7. BimaKavach - NEW (gap-fill)
- Website https://www.bimakavach.com | SME/business insurance, AI risk assessment | Founded 2021 per [Inc42](https://inc42.com/company/bimakavach/) | HQ ND | Funding $2.0M seed (Oct 2022, Inc42); investment by Beyond Capital Ventures announced Jul 2026 (amount not read) per [Pulse 2.0](https://pulse2.com/beyond-capital-ventures-invests-in-bimakavach-to-advance-ai-native-commercial-insurance-in-india/) | Revenue Rs 54.6 lakh FY25 (Inc42 header; very small, may be partial) | Employees 89 (Inc42, 2026)
- Entry: "Get Insured in Minutes", "Start Your Assessment" (cyber-risk assessment), Dashboard Login https://www.bimakavach.com/dashboard/login/ ; careers https://bimakavach.keka.com/careers
- Access: A (Limited; assessment flow not clicked, likely collects business details). Design/DS: none found | Notes: small; early-stage.

#### 8. SecureNow - NEW (gap-fill; older)
- Website https://securenow.in | Consumer + SME insurance (quotes, buy, renew; app at /download-app) | Founded 2011 per [Inc42](https://inc42.com/company/securenow/) (older than window; flag) | Funding $6.0M+ Series B (Dec 2021; another source says >$13.3M total, unresolved) | Revenue Rs 3.6 Cr FY25 (Inc42) | Employees ND
- Access: A (Limited, unverified flow). Design/DS: not checked | Notes: small; weak candidate.

#### 9. Insurance Samadhan - NEW (gap-fill)
- Website https://insurancesamadhan.com | Insurance complaint/claims resolution; app "Polifyx" | Founded 2018 per [Inc42](https://inc42.com/company/insurance-samadhan/) | Funding $4.71M+, latest May 2025 (Inc42; earlier note Rs 8.5 Cr raise) | Revenue Rs 6.2 Cr FY25 (+24%) (Inc42) | Employees 160 (Inc42, 2026)
- Entry: "Apply Now"/"Contact us" -> register.html; Login login.html; Polifyx apps https://play.google.com/store/apps/details?id=com.insurancesamadhan.polifyx and iOS id1623606564
- Access: A (Limited; free app, case registration form - not submitted). Design/DS: none found | Notes: niche (claims help); web + app + case-management back office.

#### 10. Beshak - NEW (gap-fill; bootstrapped)
- Website https://www.beshak.org (beshak.com 301-redirects) | Unbiased insurance advice | Founded 2020, Mumbai per [Inc42](https://inc42.com/company/beshak/) | Bootstrapped; revenue Rs 1.8 Cr FY25; employees 31 (Inc42)
- Entry: free expert content, "Ask the Community", free consultation booking | Access: A (Limited; content + consult, no interactive product) | Design/DS: none found | Notes: very small; weak.

#### 11. Plum (Plum Benefits) - UPDATED (primary-conditional, D-lean)
- Website https://www.plumhq.com | Employee health benefits, expanding to personal and business insurance | Founded: 2019 per [Inc42](https://inc42.com/company/plum-1/); but CIN on site (U66000KA2022PTC160458) indicates a 2022 incorporation (conflict) | HQ: Bengaluru (Primeco, ITPL Main Rd 560067 per site footer)
- Funding $56.87M+ across 5 rounds (Inc42); latest Series B ~Rs 193 Cr (~$20M), Peak XV, 25-26 Mar 2026 ([Inc42](https://inc42.com/buzz/insurtech-startup-plum-nets-%E2%82%B9193-cr-to-expand-employee-health-benefits-platform/)) | Valuation: ~Rs 1,181 Cr reported earlier (single source, unverified)
- Revenue: CONFLICT RESOLVED PARTLY. Inc42 header says Rs 13.9 Cr (FY25) but the same page's financials text says Rs 69.9 Cr FY25 (+54.3% from Rs 45.3 Cr) and net loss Rs 14.0 Cr ([Inc42 financials](https://inc42.com/company/plum-1/financials/)). Entrackr FY24 operating revenue Rs 41.3 Cr, loss Rs 25.5 Cr ([Entrackr](https://entrackr.com/fintrackr/plum-insurance-revenue-surges-25x-in-fy24-cuts-losses-by-half-7782487)); Rs 45.3 Cr on Inc42 is probably total income. Best reading: FY25 ~Rs 69.9 Cr (total revenue, Inc42), Rs 13.9 Cr header is a mis-parsed number. No Entrackr FY25 article found (do not confuse with beauty brand Plum). Company says first full year of EBITDA/cash profitability (Series B coverage; company claim)
- Employees: Inc42 shows 898 (2026, LinkedIn-style); earlier note: ND
- Entry points: https://www.plumhq.com/get-quote ("Get a Group Insurance Quote": form; "Book a demo with Plum" / "Build your plan"; consultative quote, not an instant price), log-in https://app.plumhq.com/ , employee app https://play.google.com/store/apps/details?id=com.plumhq.employee.production and iOS https://apps.apple.com/in/app/plum-health-benefits/id1616851078
- Access: D-lean (Limited: public employee app needs employer enrolment) | Free: Limited
- Design team: careers page https://www.plumhq.com/careers lists "Product Designer" (Design dept, mid-level; location label not clear) | DS: none found | Product lines: Admin Experience, Employee Experience, Plum Care, Claims Experience, Personal and Business insurance (nav)
- DS opportunity: admin + employee + claims experiences plus new personal and business lines, fresh Series B (inference)

#### 12. Onsurity - UPDATED (primary-conditional, D-lean)
- Website https://www.onsurity.com | SME healthcare membership/employee benefits | Founded 2020 per [Inc42](https://inc42.com/company/onsurity/) | HQ ND this pass (earlier unverified) | Funding $61.0M+ per Inc42; latest Series B Sep 2024 ($24M IFC-led Oct 2023 per [Entrackr](https://entrackr.com/2023/10/onsurity-raises-24-mn-in-series-b-led-by-ifc/), extended; "$45M Creaegis-led" headline is Entrackr's update, see [Entrackr](https://entrackr.com/2024/09/exclusive-onsurity-raises-over-26-mn-in-new-round-led-by-creaegis/)) | Valuation ND
- Revenue: CONFLICT RESOLVED PARTLY. Inc42 financials text: FY25 revenue Rs 168.3 Cr (+25%), net loss Rs 68.9 Cr ([Inc42 financials](https://inc42.com/company/onsurity/financials/)); Inc42 header says Rs 114.1 Cr and YourStory reported FY24 operating revenue Rs 131.66 Cr. Use Rs 168.3 Cr (total revenue, Inc42) as reported FY25; operating revenue figure not independently found
- Employees 418 (Inc42, 2026)
- Entry: nav "Request Demo" https://www.onsurity.com/request-a-demo ; "Get a quote" also routes to request-a-demo ; public https://www.onsurity.com/tools (HR salary, gratuity, premium calculators) ; "Explore TeamSure"
- Access: D with public tools (Limited). Design: design intern and graphic designer postings ([career.io](https://career.io/job/graphic-designer-bengaluru-onsurity-eaa0f6d5e6980df4d80cf60c1d75233f), [Weekday](https://jobs.weekday.works/intern-design-at-onsurity-4393513541)); no product designer found | DS: none found

#### 13. Pazcare - UPDATED (primary-conditional, D-lean)
- Website https://www.pazcare.com | Employee benefits + insurtech | Founded 2020 per [Inc42](https://inc42.com/company/pazcare/) (Inc42 description mentions therapy; likely auto-text, check) | HQ Bengaluru | Funding $11.43M+, latest Series A Jun 2022 | Valuation ND (aggregator est. $48M, unverified)
- Revenue: Rs 15.4 Cr FY25 (+29%), loss Rs 15.5 Cr ([Inc42 financials](https://inc42.com/company/pazcare/financials/)); Inc42 header Rs 6.9 Cr; earlier Latka $22.9M claim is unreliable | Employees 279 (Inc42, 2026; earlier ~208 estimates)
- Entry: "Get Quote" -> https://www.pazcare.com/lp/group-health-insurance (lead form, free teleconsult features listed); https://www.pazcare.com/get-a-quote ; client login https://app.pazcare.com/login ; app https://play.google.com/store/apps/details?id=com.getpaz.pazcare ; free HR calculators (salary hike, HRA, gratuity, full-and-final) on site
- Access: D-lean (Limited). Design/DS: not found on careers page (JS); none found

#### 14. Loop Health - UPDATED (primary-conditional, D-lean; best design evidence)
- Website https://www.loophealth.com | Group health insurance + preventive care ("health assurance") | Founded 2018 (Inc42 and job post) | HQ Bengaluru | Funding $39.3M+ per Inc42 (earlier $25M Series B Apr 2022 led by General Catalyst, Elevation) | Valuation ND | Revenue Rs 8.9 Cr FY24, loss Rs 30.1 Cr ([Inc42 financials](https://inc42.com/company/loop-health/financials/)); FY25 ND (note: Rs 8.9 Cr looks small for the scale; may reflect brokerage entity) | Employees 834 (Inc42, 2026; likely LinkedIn-derived)
- Entry: "Request a Demo", "Get Started", app download page https://www.loophealth.com/download ("Schedule unlimited free consults" for covered members), careers https://www.loophealth.com/careers ("60+ open roles")
- Access: D-lean (Limited)
- Design team: Product Designer and Senior Product Designer jobs (posted Jul 2026) - "Work on a variety of mobile and web products in the Loop ecosystem - Loop App, onboarding modules, B2B interfaces as well as tools for efficient ops" ([General Catalyst job board](https://jobs.generalcatalyst.com/companies/loop-health/jobs/86370717-product-designer), [Keka](https://loop.keka.com/careers/jobdetails/151291)) ; mentions Figma, Origami, SwiftUI, ProtoPie, heads of design and product | DS: none found; strongest case of multi-surface design growth

### Inferences
- Pattern fit for DS work: employer-benefit platforms (Plum, Onsurity, Pazcare, Loop, Nova) run HR admin + employee app + claims surfaces; consumer funnels (Ditto, InsuranceDekho, Coverfox) run calculators + comparison + checkout. Both are DS-friendly, but only Loop, Ditto, Zopper and Plum show named design hiring.
- Inc42 financial headers often disagree with its own financials text. Prefer the FAQ/financials text (total revenue), and Entrackr operating revenue where it exists, and say which.

### Gaps
- Not clickable-verified: whether quote flows need phone numbers (not tested by design). SPA pages (Nova calculator, many careers pages) returned only shells. Valuations mostly ND. Headcounts are Inc42 2026 snapshots, not company-disclosed. Turtlemint, SecureNow, BimaKavach design evidence not checked. PolicyX, Mintpro, RenewBuy sites did not load or were not checked (renewbuy.com failed).

## Healthtech: verified records (17 qualified primary, 3 conditional)

### Takeaway
Product entry points: HealthPlix has a public interactive sandbox EMR (class C) that was previously mis-sorted as sales-led. Eka Care (patient app, doctor app, free tier for solo doctors per Aug 2025 company post) and Wysa/Amaha/Sugar.fit/Clinikk have real free app entry. Diagnostics, surgery-care and clinic firms have public booking sites. Healthians, Truemeds (403 to curl), MediBuddy (site did not resolve) and Even Healthcare could not be verified hands-on and are conditional. Strongest design evidence: Eka Care (design system mentioned in job post; npm UI packages), Even Healthcare (Product Designer UI opening); design evidence for Sugar.fit and others was not checked.

### Cited Findings

#### 1. Eka Care (Orbi Health Pvt Ltd) - UPDATED
- Website https://www.eka.care | PHR/ABHA app + clinic EMR + AI scribe | Founded: Inc42 says 2020 (incorporation; earlier note ~2016, unverified) | HQ Bengaluru | Funding $19.5M+, Series A $15M Jul 2022 (Hummingbird) per [Inc42](https://inc42.com/company/eka-software-solutions/) | Valuation ND
- Revenue: FY25 Rs 28.7 Cr (down 17.6%), net loss Rs 12.0 Cr per [Inc42 financials](https://inc42.com/company/eka-software-solutions/financials/) (header: Rs 26.4 Cr; earlier note Rs 26.4 Cr, so refined) | Employees 180 (Inc42, 2026; earlier 117-205 range)
- Product: Eka Care patient app; Eka for doctors (EMR, scribe, mac/Windows/Android downloads) | URLs: https://www.eka.care ; patient Android https://play.google.com/store/apps/details?id=eka.care ; doctor Android https://play.google.com/store/apps/details?id=eka.care.doctor ; iOS https://apps.apple.com/bt/app/eka-health-ai-abha-records/id1561621558 ; EMR page https://www.eka.care/eka-for-doctors/emr-ehr-medical-software ; homepage buttons: "Request a Demo", "Download for Mac/Windows/Android", "Get started"
- Access: A. Free: Yes (patient app); doctors: Limited. Company post "Important update to Eka.Care's free tier - same mission, clearer limits" (14 Aug 2025) says it keeps a free plan with limits for independent doctors ([post](https://curiocdn.eka.care/services/important-update-to-eka-cares-free-tier-same-mission-clearer-limits)); TrustRadius lists paid Plus Rs 9,999/yr and Pro Rs 14,999/yr and no free version (conflict, listing may be outdated)
- Design team: Product Designer jobs (https://ekacare.keka.com/careers/jobdetails/151150 , joinsaarthi listing) | DS evidence: job post (jobdetails/135452) says role contributes to a design system used across EMR, PHR and AI flows (earlier finding; text not re-extracted this pass). npm: @eka-care/medical-records-ui, @eka-care/medassist-widget, @eka-care/ekascribe-ts-sdk exist ([npm search](https://registry.npmjs.org/-/v1/search?text=%40eka-care)); no public Storybook or docs found. GitHub org lookup returned 403 (unchecked)
- DS opportunity: PHR + EMR + scribe + embeddable widgets = multiple surfaces; DS exists internally, being stretched across AI flows

#### 2. HealthPlix - MOVED SECONDARY TO PRIMARY (class C)
- Website https://www.healthplix.com | Clinic EMR, AI | Founded 2014 (Inc42; outside window, flag) | HQ Bengaluru | Funding $44.68M+, Series C 14 Mar 2023 (earlier note ~$22M round) | Valuation ND | Revenue Rs 38.4 Cr FY25 (+24%) (Inc42 header; financials page not checked) | Employees 264 (Inc42, 2026)
- Entry: "Schedule a Demo" -> https://demo.healthplix.com/sandboxSpecialities.php ("Experience the EMR for your speciality", pick from ~25 specialities); public page loads without login; sandbox registration CSS references mobile fields (not filled) ; Login https://md.healthplix.com/ ; Patient App https://www.healthplix.com/healthplix-for-patients
- Access: C (Public Demo). Free: Limited (a web search snippet says HealthPlix markets its EMR as free for doctors; unverified). Explorable: speciality sandbox EMR
- Design/DS: not checked (not enough budget) | Notes: previous "no free trial" note from Capterra is superseded by the sandbox demo.

#### 3. Wysa (Touchkin eServices) - UPDATED
- Website https://www.wysa.com (returned HTTP 520 error in my fetch; transient) | Mental health AI chatbot | Founded 2015 (Inc42; [Spanish startup registry](https://startups.one.gob.es/companies/touchkin)) | HQ Bengaluru | Funding $34.7M+ per [Inc42](https://inc42.com/company/wysa/) (earlier CB Insights $40.1M) | Latest: grant 21 May 2023 per Inc42; earlier Series B $20M 2022 | Valuation ND | Revenue ND (earlier conflicting $4.68M vs Rs 40.12 Cr FY24) | Employees 177 (Inc42, 2026)
- Product: Wysa app | Android https://play.google.com/store/apps/details?id=bot.touchkin (verified live) | Access: A. App free to download with free AI chat and paid premium (App Store: annual plan about $74.99 and 7-day trial per third-party price aggregators; verify on store)
- Design/DS: none found

#### 4. Amaha (MindCrescent Wellness Ventures) - UPDATED
- Website https://www.amahahealth.com | Mental health (app + clinics) | Founded 2016 (Inc42) | HQ Bengaluru | Funding $11.67M+, Series A 8 Jan 2024 | Valuation ND (Entrackr est. ~Rs 300 Cr, not official)
- Revenue FY25: Rs 31.0 Cr (Inc42 financials text; header Rs 23.1 Cr; Entrackr Rs 27.57 Cr via earlier note) - three figures conflict; use "Rs 23-31 Cr range" | Employees 352 (Inc42, 2026)
- Entry: "GET STARTED", "Download App" ; iOS https://apps.apple.com/in/app/innerhour-self-care-therapy/id1323264990 | Access: A (self-care app free; therapy paid) | Design/DS: none found

#### 5. Clinikk (Ohealer Healthcare Services) - NEW (gap-fill)
- Website https://clinikk.com | Bangalore neighbourhood GP clinics, unlimited visits plans | Founded 2016 (Inc42) | HQ Bengaluru | Funding $9.42M+, Series A 3 Dec 2024 | Valuation ND | Revenue Rs 8.5 Cr FY25 (+44%), loss Rs 7.4 Cr ([Inc42 financials](https://inc42.com/company/clinikk/financials/)) | Employees 211 (Inc42, 2026)
- Entry: patient web app https://patient.clinikk.com/en ; Android https://play.google.com/store/apps/details?id=com.clinikk.clinikkV0 ; iOS id6621223667 ; "Get Treatment" clinic finder | Access: A (Limited; plans paid, signup likely OTP, not tested)
- Design/DS: not checked | DS opportunity: patient app + clinic ops + insurance add-on (inference)

#### 6. Even Healthcare - UPDATED (conditional)
- Website https://evenhealthcare.com | Managed-care/insurance-linked care in Bengaluru | Founded ~2020 (earlier note, unverified) | Funding: >$120M after $50M Series B Oct 2026 Khosla-led ([YourStory](https://yourstory.com/2026/10/even-healthcare-raises-50m-in-series-b-round-led-by-khosla-ventures)) | Valuation: $300M third-party estimate (Multiples.vc), not confirmed | Revenue/employees ND (Inc42 has no profile slug tried)
- Entry: homepage "Get Started", "Talk with us", "Sign In"; plans from Rs 300/month; careers https://careers.even.in/ | Access: D-lean (advisor-led; Get Started likely collects phone, not tested) | Design: Product Designer (UI) opening https://jobs.8vc.com/companies/even-healthcare-2-8cdc62f1-1283-4210-9bac-40246a25fd88/jobs/89826128-product-designer-ui | DS: none found

#### 7. Sugar.fit - UPDATED
- Website https://home.sugarfit.com | Diabetes/metabolic app + CGM + coaching | Founded 2021 per [Inc42](https://inc42.com/company/sugar-fit/) (earlier ~2020 unverified) | HQ Bengaluru | Funding $15.92M+ per Inc42 (earlier $26M sum of rounds; conflict) | Latest Series A ext. 12 Mar 2024 | Revenue Rs 75.1 Cr FY25 (+79%), loss Rs 41.9 Cr (Inc42; Entrackr Rs 66.5 Cr per earlier note) | Employees 441 (Inc42)
- Entry: "Book FREE session" https://app.sugarfit.com/book-free-session (form with Phone field; not submitted); Android https://play.google.com/store/apps/details?id=fit.sugar.android ; iOS id1568271882 | Access: A/B (free session then paid program) | Design/DS: not checked

#### 8. Redcliffe Labs - UPDATED
- Website https://redcliffelabs.com | Diagnostics | Founded: ND this pass (earlier ~2016) | HQ Gurugram/Noida | Funding $113-116M; Series C $42M Sep 2024 | Revenue: FY25 Rs 419 Cr (company, [BioVoice](https://biovoicenews.com/redcliffe-labs-reports-20-growth-with-rs-419-crore-revenue-in-fy25/)) vs Inc42 Rs 436.3 Cr (conflict) | Employees ND
- Entry: public test search https://redcliffelabs.com/search , My Bookings dashboard ; Android https://play.google.com/store/apps/details?id=com.redcliffelabs (live) ; iOS id1602990503 | Access: A (Limited; booking needs account) | Design/DS: not checked

#### 9. Orange Health Labs - UPDATED
- Website https://www.orangehealth.in | Diagnostics | Founded 2020 (Inc42) | HQ Bengaluru | Funding $76.81M+, Series C 15 May 2026 per [Inc42](https://inc42.com/company/orange-health/) (earlier $48.1M CB Insights; update) | Revenue Rs 87.7 Cr FY25 (+77%), loss Rs 81.2 Cr (Inc42 financials); earlier FY26 Rs 138.6 Cr headline (Ascendants) | Employees 728 (Inc42, 2026)
- Entry: public package/test catalog pages (e.g. /health-checkups-bangalore) ; app ID not verified | Access: A (Limited) | Design/DS: not checked

#### 10. Healthians - UPDATED (conditional)
- Website https://www.healthians.com (HTTP 403 to curl) | Founded 2014 per Inc42 (outside window; earlier ~2015) | HQ Gurugram | Funding $15.18M+ per Inc42 (CB Insights $70.3M; conflict) | Revenue Rs 270.5 Cr FY25 per Inc42 financials; Entrackr Rs 263 Cr ([Entrackr](https://entrackr.com/fintrackr/healthians-posts-rs-263-cr-revenue-in-fy25-nears-breakeven-10806865)) | Employees 1,573 (Inc42, 2026)
- Access: A unverified (site blocked, Play ID guess failed) | Design/DS: not checked

#### 11. Truemeds - UPDATED (conditional)
- Website https://www.truemeds.in (403 to curl) | Online pharmacy | Founded 2019 (Inc42) | HQ Mumbai | Funding $176.47M+ (Inc42), Series C Aug 2025 | Valuation >$400M per [CXO Digital Pulse](https://www.cxodigitalpulse.com/healthtech-startup-truemeds-raises-20-million-in-series-c-round-led-by-peak-xv-valuation-crosses-400-million/) | Revenue: CONFLICT. Inc42 financials Rs 8.3 Cr FY25 (down 97%) is evidently a parse/entity error; earlier secondary report ~Rs 510 Cr net revenue; not resolved | Employees 1,441 (Inc42, 2026)
- Access: A unverified | Notes: near-household; low priority.

#### 12. Pristyn Care - UPDATED
- Website https://www.pristyncare.com | Surgery care | Founded 2018 (Inc42) | HQ Gurugram | Funding $181M+, last 22 Jul 2025; valuation $1.17B (Inc42 profile) | Revenue Rs 388.4 Cr FY24 (Inc42) | Employees 1,604 (Inc42, 2026)
- Entry: "Book FREE Appointment", free consultation, hospital pages | Access: A (Limited) | Design/DS: not checked | Notes: unicorn-scale.

#### 13. HexaHealth - UPDATED
- Website https://www.hexahealth.com | Surgery discovery | Founded 2021 per Inc42 (earlier ~2019) | HQ Gurugram | Funding $23.48M+, Series A 29 Apr 2025 | Revenue Rs 39.9 Cr FY25 (+96%) | Employees 375 (Inc42, 2026)
- Entry: "Get Second Opinion" /services/second-opinion, "Get The App" https://m.hexahealth.com/qLo3, BMI calculator tool | Access: A (Limited) | Design/DS: not checked

#### 14. CureBay - UPDATED
- Website https://curebay.com | Tech-enabled primary care | Founded 2021 per Inc42 (earlier ~2018) | HQ Hyderabad | Funding $45.18M+, latest 21 Oct 2026 (Pre-Series C) per [Inc42](https://inc42.com/company/curebay/) | Revenue Rs 70.4 Cr FY25 (+467%), loss Rs 58.1 Cr (Inc42 financials; header Rs 13.2 Cr is FY24-style number) | Employees 384 (Inc42, 2026)
- Entry: "Get Kavach - Rs 499/year" membership, "Book Lab Test", partner pages | Access: A (Limited) | Design/DS: not checked

#### 15. Allo Health - UPDATED
- Website https://www.allohealth.com (allohealth.care redirects) | Sexual health clinics | Founded 2022 (Inc42; earlier ~2021) | HQ Bengaluru | Funding $1.83M+ pre-Series A Mar 2025 | Revenue Rs 3.6 Cr FY24 (Inc42) | Employees 177 (Inc42, 2026; high for revenue)
- Entry: "Book appointment", "Start Chat", free tools | Access: A (Limited) | Design/DS: not checked | Notes: small.

#### 16. Lybrate - MOVED IN (gap-fill; flag)
- Website https://lybrate.com | Doctor discovery/online consults | Founded 2014 per Inc42 (outside window; flag); Inc42 marks "Acquired"; last funding 2017 ($14.43M); revenue Rs 11 lakh FY25 (Inc42; operations look minimal) ; employees 159 (Inc42)
- Entry: "Book Free Appointment" | Access: A (Limited) | Notes: likely stale; weak prospect.

#### 17. MediBuddy (Phasorz Technologies) - UPDATED (conditional)
- Website https://www.medibuddy.in (did not resolve) | Founded 2013 (flag) | HQ Bengaluru | Funding $206.65M+ (Inc42; "Acquired" tag on Inc42 profile, details not read) | Revenue FY25 Rs 743.0 Cr, loss Rs 137.1 Cr per Inc42 financials (earlier Entrackr Rs 724.6 Cr) | Employees 1,966 (Inc42, 2026)
- Access: A unverified | Design/DS: not checked | Notes: large; possible ownership change - check before outreach.

### Conditional / other healthtech notes
- Ultrahuman: https://www.ultrahuman.com (D/E-lean: ring is paid hardware; "no membership" on US ring page). FY25 Rs 580.8 Cr, PAT Rs 73.0 Cr (Inc42 financials); funding $141.3M+ (latest 2 Sep 2026); employees 508. Keep out of primary.
- Eka, Wysa, HealthPlix etc. design-system hunts were limited to job text and npm; no public design-system site found for any healthtech company.

### Inferences
- HealthPlix sandbox gives Layer One a way to see a real EMR UI without sales contact; Eka Care is the best-evidenced prospect (stated internal DS, multiple surfaces, free entry).
- Several earlier "founded ~20xx [K]" values were wrong or incorporation-based on Inc42; use "approx." until company pages confirm.

### Gaps
- Phone-OTP flows deliberately not tested, so what lies beyond booking/signup screens is unknown for diagnostics, clinics and mental-health apps. Healthians, Truemeds, MediBuddy not loadable; Zeno not loadable. Design-team evidence not checked for most healthtech firms beyond Eka and Even. Even Healthcare financials ND.

## Companies moved to SECONDARY (sales-led or unusable) with reasons

### Takeaway
Seven insurtech and several healthtech names are demo-led, enterprise-API, defunct or unverifiable.

### Cited Findings
- Zopper (https://www.zopper.com): homepage CTAs only "Contact Us", "API-driven platform, 2500+ brands" - D (sales/API). Inc42: founded 2011 (flag), Series D $25M Nov 2024, $125M+ total, FY25 revenue Rs 363.3 Cr (down 18.8%), loss Rs 203.4 Cr, employees 922 ([Inc42 financials](https://inc42.com/company/zopper/financials/)); the Inc42 header Rs 133 Cr is inconsistent, prefer Rs 363.3 Cr (Entrackr FY23 Rs 187.28 Cr, loss Rs 13.95 Cr). Design: Head of Product Design named on Zopper's career page and a Behance team page (https://www.behance.net/ZopperDesignTeam) - strong design signal despite D access.
- Riskcovry (https://www.riskcovry.com): "Schedule Demo", "Let's talk" - D. Founded 2018, FY25 revenue Rs 46.0 Cr (+115.6%), loss Rs 19.4 Cr, $9.52M funding, employees 131 (Inc42). Earlier "Rs 30 Cr target" superseded.
- Bharatsure (https://bharatsure.com): "Book a Demo", "Schedule a demo" - D. Founded 2021, $2.89M, FY25 revenue Rs 22.8 lakh, employees 57 (Inc42).
- Ensuredit (https://ensuredit.com): "Request Demo" -> contact - D. Founded 2019, $4.83M, FY25 revenue Rs 3.1 Cr, employees 45 (Inc42).
- Toffee Insurance (https://toffeeinsurance.com): domain did not respond to curl; Inc42: founded 2017, $7.0M, last round Dec 2019, FY24 revenue Rs 4.6 Cr, employees 34 - E/unverified, possibly stale; not primary.
- Bimaplan (bimaplan.com): domain shows "for sale" page - defunct; excluded.
- Probus Insurance: founded 2002 (Inc42), $6.7M - too old, broker; not checked further. RenewBuy: site did not load, agent-led (earlier note). Kenko Health: shut down 2024 (earlier note).
- Healthcare: Mykare (https://mykare.ai): "Book A Demo" for hospital AI agents - D. Ekincare (https://www.ekincare.com): "Book a demo", employee/DataVue logins - D; Inc42: founded 2015, $20.73M, Series C 28 Apr 2025, FY25 revenue Rs 93.0 Cr (+71%), employees 253. Visit Health: employer-sponsored, page returned no title to curl; Inc42 founded 2016, $37.5M, FY25 Rs 225.2 Cr, employees 1,105 - D. Elevate Now: program-led; note elevatenow.com is an unrelated coaching site, the weight-loss company is on elevatenow.in (consult/program, not free product) - D/E; Inc42 founded 2022, $1.99M seed Feb 2026, FY25 Rs 4.2 Cr, employees 410. Docon (https://docon.co.in, 403 to curl): a directory lists 15-day trial at Rs 6,000/year ([Techjockey summary via search](https://techjockey.com/blog/list-ten-best-clinic-management-software-market/amp)) - unverified, Inc42 has no profile. Medcords: site did not load; no profile. Zeno Health: site did not load; no Inc42 profile; earlier data weak.
- Clinic-software firms with trials (from one search, vendor/listicle claims, not verified on vendor sites): MedPrax OPD (14-day Pro trial, free Starter plan), ClinicAdmin (MDM Solutions, 14-day trial), Zoho for Healthcare (15-day trial), Medixcel (30-day), KareXpert (30-day), Clinic Manager (Vayuzon, 90-day). None checked for funding or design team; none counted as primary.

### Inferences
- Zopper stays a high-value D account because of named design leadership.

### Gaps
- Docon and Medcords not verified; free-trial clinic software firms need individual follow-up if Layer One wants class B accounts.
