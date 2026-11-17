# Verification pass: Indian B2B SaaS (horizontal + vertical/commerce/devtools) prospects for Layer One

Run date: 2026-11-17. Network was open. Method: direct `curl` of pricing/signup/home/careers pages (HTML grepped), live ATS JSON endpoints (Keka embedjobs, Lever, Ashby), npm registry, GitHub repo-search API and raw.githubusercontent.com (GitHub contents API was blocked for this session), and Inc42 company pages (https://inc42.com/company/<slug>/ ). Entrackr was not usable for lookups.

Legend. Access: A Freemium, B Free Trial, C Public/interactive demo, D Sales-led only, E none. "ND" = Not publicly disclosed / not found in fetched sources. R = reported by press/filing-sourced outlet (Inc42 Datalabs, Entrackr). E = estimate (aggregator). Inc42 "employee count" = Inc42 Datalabs profile snapshot (Nov 2026, E, LinkedIn-style, India-entity or global unclear). Inc42's "based in" often shows the registered holding-company city (US) rather than where the product org sits; flagged per record.
Caveat on "DS evidence: none found": means not found by the checks listed (careers page, GitHub org repo search, npm @scope guess, README/package.json). It never means the company lacks a design system.
Caveat on search tools: only fetches/APIs were used (zero WebSearch calls). Several sites returned 403/429 (sprinto.com, verloop.io, hiverhq.com, wigzo.com, devrev.ai); those are marked unverified rather than guessed.

---

## 1. Horizontal B2B SaaS: verified PRIMARY list (19 companies, target was >=16)

### Takeaway
19 horizontal companies have a confirmed free plan, free trial, or interactive demo, checked by fetching the page. Two earlier primaries (Kissflow, Qandle) and several others were demoted because their "sign up / free trial" buttons turn out to be demo-request forms. Strongest design-system signals: Keka (live design-team hiring), Hevo (Senior Product Designer on Lever), Chatwoot (public UI/design/styleguide repos), Signeasy and Leegality (public interactive demos).

### Cited Findings (one record per company)

#### H1. Keka (UPDATED: access downgraded, design evidence upgraded)
- Name/Website: Keka (Keka Technologies Pvt Ltd), keka.com | Subcategory: HRMS / payroll / talent / PSA
- Founded: 2015 (R, Inc42 - was unverified before) | HQ: Hyderabad (careers listings Hyderabad + Bengaluru; Inc42 snapshot)
- Total funding: $58.60M (R) | Latest round: Series A, 08 Nov 2022 (Inc42); RBF $1.6M Apr 2026 per earlier note (not re-verified) | Valuation: ND (third-party $115.6M Jun 2023 is E, from earlier note)
- Revenue: Rs 133.9 Cr FY25, +54.5% from Rs 86.6 Cr FY24; net loss Rs 71.8-71.9 Cr (R, Inc42). Earlier Entrackr FY24 figure Rs 78 Cr conflicts with Inc42 Rs 86.6 Cr; unresolved, use Inc42.
- Employees: 1,315 (Inc42, Nov 2026, E)
- Product: Keka HR / People OS | URL: https://www.keka.com | Pricing: https://www.keka.com/pricing
- Signup URL: https://www.keka.com/signup (pricing-page "Free Trial" buttons go to /signup?plan=foundation, /strength, /hire-pro). CORRECTION: the page title is "Sign Up for a Free HR Software Demo" and renders a request form, so the trial is form-gated, not instant self-serve. Trial length not stated on fetched pages (earlier "14-day" claim unconfirmed).
- Access category: B (form-gated; borderline D) + video demos: https://www.keka.com/product-demos ("short, self-paced demos"; YouTube embeds, not interactive)
- Free access: Limited | Testable: module demos (payroll, hiring, performance, attendance) as video; trial only after form.
- Design team evidence (STRONG, live Nov 2026): Keka ATS JSON (https://hr.keka.com/careers/api/embedjobs/default/active/24040a7e-a7c5-47a5-9cd5-019962c66385) lists Lead Product Designer (Hyderabad), Senior Product Designer (Bengaluru), Design Manager (Bengaluru), Senior Visual Designer, Visual/UI Designer, Visual/Motion Designer. Earlier notes: 2024 posts for "Lead Designer, Design Systems"/"Senior Product Designer, Design System" (https://hr.keka.com/careers/jobdetails/75543).
- DS evidence: internal Keka design system implied by those posts (accessibility/VPAT). Public docs/Storybook/npm: none found (npm @keka/ui 404).
- DS opportunity: multi-suite (Payroll, HR, Talent, Project Services/PSA, PeopleOS/AI) + GCC/US expansion; pitch is audit/scale/accessibility/multi-product consistency, not greenfield.
- Sources: https://inc42.com/company/keka-hr/financials/ ; https://www.keka.com/pricing ; https://www.keka.com/signup ; Keka ATS URL above.
- Notes: Confidence high on firmographics/design hiring; medium on access.

#### H2. SuperOps (UPDATED: signup verified)
- Website: superops.com | Subcategory: IT management, MSP PSA + RMM | Founded: 2020 (Inc42) | HQ: US-registered (Inc42: Claymont, Delaware; earlier note Dallas) with India product/engineering org (Chennai/Bengaluru) - US-HQ with India team; verify India share before outreach
- Funding: $54.37M total (R); latest Series C, 29 Jan 2025 (Inc42; earlier channele2e $25M, led by March Capital); Series B $12.4M Oct 2023 | Valuation: ND
- Revenue: only Rs 11.0 Cr FY22 on Inc42 (stale; +194.7%); later years ND | Employees: 173 (Inc42, E); ~200-220 earlier
- Product: SuperOps PSA/RMM | URL: https://superops.com | Signup: https://superops.com/signup (fetched, 200): "14-DAY FREE TRIAL | NO CREDIT CARD"
- Access: B (14 days, no card, confirmed on vendor page) | Free access: Yes (trial) | Testable: PSA, RMM, ticketing, documentation, client portal.
- Design team: careers page fetched, no design role found; none found. DS: none found.
- DS opportunity: technician console + client portal + mobile, multiple product lines. Sources: https://superops.com/signup ; https://inc42.com/company/superops/

#### H3. Rocketlane (UPDATED: funding conflict resolved, signup verified)
- Website: rocketlane.com | Subcategory: customer onboarding / PSA | Founded: 2020 (Inc42) | HQ: Chennai + US (Inc42 registered city Walnut, California; earlier note Lehi, Utah)
- Funding: $105.0M total across 5 rounds: Series C $60M, 24 Mar 2026 (Insight Partners); Atlassian Ventures undisclosed, 06 Jul 2026; Series B $24M Jun 2024; Series A $18M Jan 2022; Seed $3M Jun 2021 (R, Inc42 funding page https://inc42.com/company/rocketlane/funding/). This resolves the earlier "doubtful July 2026 round" flag: it is real per Inc42. Valuation ND.
- Revenue: Rs 43.0 Cr FY25, +50.8% (Inc42) | Employees: 333 (Inc42, E)
- Product: Rocketlane | Signup URL: https://www.rocketlane.com/signup (fetched): "Start your free trial", work email, activation email; pricing page text: "14-day trial" (also "21-day portfolio course" is unrelated).
- Access: B (14 days; verified) | Free access: Yes | Testable: project/onboarding workspace, customer portal, AI features.
- Design team: careers URL guesses 404; none found. DS: none found (npm @rocketlane/ui 404).
- DS opportunity: two audiences (internal PSA workspace + customer portal) and new AI modules after a $60M round.
- Sources: https://inc42.com/company/rocketlane/funding/ ; https://www.rocketlane.com/signup

#### H4. Wati (UPDATED)
- Website: wati.io | Subcategory: WhatsApp business platform | Founded: 2020 (single source, unchanged) | HQ: ND (not on Inc42; unresolved)
- Funding: $32.3M over 4 rounds, Series B $23M Oct 2022 (CB Insights, from earlier note; not re-verified) | Revenue ND | Employees: ND
- Product: Wati | Signup: https://www.wati.io/signup/?language=en and https://auth.wati.io/register (fetched 200). Pricing page: "7 days free trial, zero setup fees" (earlier "no card" claim from Capterra not on page).
- Access: B (7 days) | Free: Yes | Testable: shared inbox, broadcasts, chatbot builder.
- Design team/DS: careers URL 404; none found. India HQ status still uncertain - confirm.
- Sources: https://www.wati.io/pricing/

#### H5. Interakt (Jio Haptik) (UPDATED)
- Website: interakt.shop | Founded: 2020 (Inc42 profile exists; no funding data) | HQ: Mumbai group (Haptik); parent Haptik founded 2013, FY24 revenue Rs 156.6 Cr (R, https://inc42.com/company/haptik/), 307 employees.
- Signup: https://www.interakt.shop/signup and https://www.interakt.shop/marketing-automation/signup/ (fetched 200); homepage "Start Free Trial - 14 day free trial | No credit card required". App: https://app.interakt.ai
- Access: B (14 days, verified) | Testable: WhatsApp inbox, marketing hub, SOLO AI agents.
- Design/DS: careers 404; none found. Valuation/revenue for Interakt alone ND.

#### H6. AiSensy (UPDATED: free plan verified)
- Website: aisensy.com | Founded/HQ: ND (careers site careers.aisensy.com exists) | Funding: ND firm (Latka $100K seed, E) | Revenue: Latka $8.9M 2025 (E)
- Signup: https://app.aisensy.com/signup (fetched 200). Pricing page: "WhatsApp API FREE for life", Free Forever plan, broadcasting not available on free.
- Access: A | Free: Yes | Testable: dashboard, inbox, API, Meta-ads connection (1,000 free conversation credits mention).
- Design/DS: none found. Sources: https://aisensy.com/pricing

#### H7. Gallabox (UPDATED)
- Website: gallabox.com | Founded 2020 (Inc42) | HQ Chennai (Inc42) | Funding: Seed 28 Jan 2025; total $8.26M per Inc42 (earlier ~$5M; conflict, Inc42 incl. earlier rounds) | Revenue Rs 4.8 Cr FY25 (R) | Employees 95 (Inc42, E)
- Signup: https://app.gallabox.com/signup (fetched 200). FAQ: "There's no free forever plan"; 7-day trial with 500 AI credits.
- Access: B (7 days) | Design/DS: none found (careers on Wellfound). Smaller company, lower fit.

#### H8. Kylas (UPDATED)
- Website: kylas.io | Founded 2019/2020 (conflict, unresolved) | HQ Pune (page address Mahalunge, Pune) | Bootstrapped (earlier note) | Revenue: Latka $7.6M 2025 (E)
- Signup: https://app.kylas.io (200). Homepage: "Start Free Trial (No Card Required)"; page meta: "Try free for 7 days".
- Access: B (7 days per page meta) | Design: careers on kylastechnologies.keka.com list 7 roles, none design (earlier "product designer" mention was an unrelated page string). DS: none found.

#### H9. Mailmodo (UPDATED)
- Website: mailmodo.com | Founded 2020 (Inc42) | HQ: India team; Inc42 registered San Francisco | Funding: Seed $2.27M, 23 Jul 2021 | Employees 45 (Inc42, E) | Revenue ND
- Signup: https://manage.mailmodo.com/auth/signup (200); nav: "Get started - it's free".
- Access: A/B (free sign-up; plan limits not verified) | Testable: AMP interactive-email builder, flows. Design/DS: careers 404; none found. Interest: email-builder UI.

#### H10. Pabbly (UPDATED)
- Website: pabbly.com | Bhopal | Founded 2017-2019 (conflict) | Bootstrapped | founders Pankaj and Neeraj Agarwal (about page)
- Signup: https://accounts.pabbly.com/signup; site nav "Sign Up Free"; 9 products under one bundle (Pabbly Plus). Free-tier limits not verified.
- Access: A/B | Careers via pabbly.zohorecruit.in. Design/DS: none found. Multi-product consistency case.

#### H11. Chatwoot (UPDATED: DS evidence found)
- Website: chatwoot.com | Founded: 2020 per Inc42 (earlier note 2017; GitHub repos date from 2017-2019, unresolved) | HQ: Bengaluru / San Francisco (conflict) | Funding: Seed $1.6M, 08 Aug 2021 (Inc42) | Revenue Rs 2.2 Cr FY25 (Inc42) | Employees 13 (Inc42, E; India entity likely)
- Signup: https://app.chatwoot.com/app/auth/signup (200). Pricing page: "Sign up for your 15-day free trial"; open-source self-host free.
- Access: A/B (OSS free + 15-day cloud trial) | Free: Yes
- DS evidence: public GitHub repos chatwoot/ui (pushed 2023-03), chatwoot/chatwoot-ui-monorepo (2024-01), chatwoot/ui-components ("Vue.js UI components", 2019), chatwoot/design, chatwoot/styleguide (via GitHub repo search); main repo package.json has Histoire story scripts (story:dev). Design hiring: careers is a Notion page; none found.
- DS opportunity: small team, Vue app with fragmented UI repos; code-level audit possible in public.
- Sources: https://api.github.com/search/repositories?q=org:chatwoot ; https://raw.githubusercontent.com/chatwoot/chatwoot/develop/package.json

#### H12. Hevo Data (UPDATED)
- Website: hevodata.com | Subcategory: data integration/ELT | Founded 2017 (Inc42) | HQ: Inc42 registered San Francisco, Bengaluru ops - US-HQ with India team
- Funding: $43.0M (Inc42), Series B 16 Dec 2021 ($30M Sequoia India, Qualgro) | Revenue Rs 80.5 Cr FY25 (Inc42; down from Rs 97.6 Cr per earlier note) | Employees 250 (Inc42, E)
- Signup: https://hevodata.com/signup/?step=email (200). Pricing: "14 day free trial ... No credit card required"; "Start for Free". Free-plan existence not shown on fetched page.
- Access: B (14 days) | Testable: pipelines/connectors.
- Design team: Lever postings API (https://api.lever.co/v0/postings/hevodata?mode=json, 39 postings) lists "Senior Product Designer, Bengaluru". DS: none found.
- DS opportunity: connector/pipeline console, transformation + activation modules.

#### H13. Signeasy (NEW to this list)
- Website: signeasy.com | Subcategory: e-signature / contract management | Founded: ND confirmed (about page contains "2011"; unverified context; older than window - flag) | HQ: Bengaluru (Koramangala address on about page) | Funding/revenue/employees: ND in fetched sources (Inc42 slug not found)
- Signup: https://app.signeasy.com/signup (200). Pricing page: 14-day free trial (3 mentions), "Start free". Public interactive demo on Storylane: https://demo.storylane.com/demo/2vczedx16qod (Intelligent Contract Management) plus "Interactive Demos" nav.
- Access: B + C (strongest testability in set) | Free: Yes (trial)
- Design team: careers uses Teamtailor (not parsed); none found. DS: npm/GitHub none found (only signeasy/GPUImage2 repo).
- DS opportunity: web + mobile + API + ICM product line expansion. Sources: https://signeasy.com/pricing ; home page

#### H14. Synup (NEW)
- Website: synup.com | Subcategory: local listings / reputation marketing | Founded 2014 (Inc42; older - flag) | HQ: Inc42 New York registered; Bengaluru product org (verify)
- Funding: Series A 23 Sep 2017, total $6.5M | Revenue Rs 17.6 Cr FY24 (Inc42) | Employees 67 (Inc42, E)
- Signup: https://ai.synup.com/signup (200); pricing FAQ "What's included in the 14-day free trial?"
- Access: B (14 days) | Design/DS: careers mention in fetched page was a design-system-flavoured blog excerpt about a widget (not evidence of a team); none confirmed. Lower fit (US-oriented, small).

#### H15. Leegality (NEW)
- Website: leegality.com | Subcategory: e-sign / stamping / legal workflow | Founded 2016 | HQ: Gurugram (Inc42) | Funding: Series A $5.0M, 17 Oct 2022 | Revenue Rs 86.6 Cr FY25, +30.4% (Inc42) | Employees 223 (Inc42, E)
- Public demo: nav "Experience a Leegality flow in just 2 minutes" and "Interactive demo" for Deal Collaboration (https://www.leegality.com/demos). Sign-up: https://dashboard.leegality.com/sign-up (200) and free "PDF Tools" (free sign-up; plan limits not verified).
- Access: C (+ free tools sign-up, A limited) | Design/DS: careers 404; none found.
- DS opportunity: multiple products (BharatSign, BharatStamp, Deal Collaboration, consent) with profitable revenue base. Sources: https://inc42.com/company/leegality/

#### H16. Zimyo (MOVED UP from secondary)
- Website: zimyo.com | Founded 2018 (Inc42) | HQ Gurugram (Inc42; earlier note Noida) | Funding $3.74M total, last 02 Mar 2022 | Revenue Rs 9.4 Cr FY25 (Inc42) | Employees 107 (Inc42, E)
- Pricing page FAQ: "How does the 14 days free trial work? ... limited features for 14 days ... no credit card". Dedicated signup URL not isolated (pricing page has "sign up" CTAs; also "request a demo").
- Access: B (14 days, limited features) | Design/DS: careers at zimyo.com/about/career/; none found. Small; lower fit.

#### H17. Zluri (MOVED UP from secondary)
- Website: zluri.com | Subcategory: SaaS management / IGA | Founded 2020 | HQ: Inc42 registered San Francisco, Bengaluru ops (US-HQ flag) | Funding: Series B $32M, 12 Jul 2023 (Lightspeed) | Revenue Rs 12.5 Cr FY25 | Employees 244 (Inc42, E)
- Public demo: https://www.zluri.com/product-tours ("quick, self-guided walkthroughs"; vendor not identified). No self-serve trial found.
- Access: C | Design/DS: none found.

#### H18. Scrut Automation (MOVED UP from gaps)
- Website: scrut.io | Subcategory: GRC / compliance automation | Founded 2022 (Inc42) | HQ: Inc42 registered Palo Alto; Bengaluru ops | Funding $29.53M total, last 01 Apr 2024 | Revenue Rs 47.1 Cr FY25, +82% | Employees 239 (Inc42, E)
- Public demo: homepage CTA "Try Scrut without the pitch. Take a tour" (tour vendor/URL not extracted; /product-tours 404). 
- Access: C (probable; click-test before outreach) | Design/DS: none found.

#### H19. Whatfix (UPDATED; borderline)
- Website: whatfix.com | Founded 2013 per Inc42 (earlier note 2014; older - flag) | HQ Bengaluru / US | Funding $264.4M (Inc42) vs $201M (CB Insights E); Series E $125M, 24 Sep 2024 (Warburg Pincus, SoftBank); valuation ~$900M (R, Business Standard per earlier note)
- Revenue CONFLICT: Inc42 shows standalone Rs 467.3 Cr FY25 (+65.7%), consolidated Rs 580.5 Cr FY25 (+29.5% from Rs 448.2 Cr), net loss Rs 227.2 Cr consolidated; earlier note Rs 556.7 Cr from other source. Not resolved. Employees 1,095 (Inc42, E).
- Access: B/D borderline: https://whatfix.com/start-free-trial/ serves a JS flow-editor shell ("create, share and execute flows"), https://whatfix.com/request-demo/ is the main CTA; homepage mentions "sandbox" 10x. Confirm in browser.
- Design/DS: careers page fetched, no design mention (JS-rendered); none found. Opportunity: DAP, Mirror, analytics, authoring editor + embedded end-user widgets needing themeable components.

### Inferences
- Best "can-test-it-today" targets: Signeasy (trial + Storylane demo), Rocketlane, SuperOps, Chatwoot, Hevo, AiSensy.
- Highest design-system pitch quality (proof of design investment): Keka, Hevo, Chatwoot (public UI repos), Whatfix/Rocketlane/SuperOps by product complexity.
- Several US-registered, India-founded companies (SuperOps, Hevo, Zluri, Scrut, Synup, Mailmodo) should be framed as "India product org" companies; confirm before outreach.

### Gaps
- No Entrackr cross-check of conflicting revenue (Keka FY24, Whatfix FY25).
- Founded year / HQ for AiSensy, Wati, Interakt, Kylas, Pabbly, Signeasy not confirmed from authoritative sources.
- Careers-based design evidence only checkable where ATS had open API (Keka, Hevo Lever, Sarvam Ashby, SpotDraft Ashby); other companies' careers pages are JS-rendered or 404.

---

## 2. Vertical / commerce-enablement / devtools / AI: verified PRIMARY list (16 companies, target >=16)

### Takeaway
16 companies with verified self-serve free plan, trial or public playground. Open-source devtools give direct DS evidence: Appsmith (two design systems already in the monorepo), SigNoz (public components + design-tokens + npm), Hoppscotch (@hoppscotch/ui), Chatwoot-like public UI. Commerce/creator tools (Dukaan, Exly, TagMango, Cosmofeed, Graphy) are free-to-start with take-rates.

### Cited Findings

#### V1. Appsmith (UPDATED; DS evidence is major finding)
- Website: appsmith.com | Subcategory: open-source low-code internal tools | Founded 2019 (Inc42) | HQ: Inc42 registered San Francisco; Bengaluru office (Insight Partners page) - US-HQ with India team
- Funding: $49.0M (Inc42); CB $51.5M / Caplight $56.5M (conflict); Series B $41M, 21-22 Jun 2022 (Insight Partners, Accel) | Valuation ND | Revenue Rs 33.9 Cr FY25 (Inc42, India entity) | Employees 48 (Inc42, E, India entity)
- Product: Appsmith | Signup: https://login.appsmith.com/ ; pricing modal: "Appsmith Free is free forever" + "All new signups receive a 15-day free trial of Appsmith Business, no credit card" (https://www.appsmith.com/pricing); self-host free.
- Access: A + B | Free: Yes | Testable: full builder, widgets, datasources.
- Design team: careers page fetched, no design role seen. 
- DS evidence (STRONG): npm @appsmith/wds 1.0.0 (MIT, maintained by appsmithinc); monorepo package.json depends on @appsmith/ads, @appsmith/ads-old, @appsmith/wds, @appsmith/wds-headless, @appsmith/wds-theming, @design-system/widgets-old, and a Storybook workspace (@design-system/storybook); github.com/appsmithorg/design-system ("repository for the Appsmith design system components", 32 stars, last pushed 2024-07-11).
- DS opportunity: they have an old and a new DS side by side (ads-old/widgets-old vs wds) = migration/consolidation, theming for end-user widgets. Not greenfield.
- Sources: https://registry.npmjs.org/@appsmith/wds ; https://raw.githubusercontent.com/appsmithorg/appsmith/release/app/client/package.json ; https://inc42.com/company/appsmith/

#### V2. ToolJet (UPDATED)
- Website: tooljet.com | Founded 2021 (Inc42; earlier bg 2020/21) | HQ: Inc42 registered San Francisco; India engineering (verify) | Funding $7.65M, last 16 Jul 2023 (CB $6.81M earlier) | Employees 67 (Inc42, E) | Revenue ND
- Signup: https://app.tooljet.ai/ (200). Pricing page: Free plan (incl. AI credits, GPT-6 Luna); FAQ: "Start with the Free plan to evaluate ToolJet. Contact our team to arrange a trial of paid features." So A (not B); paid-feature trial is sales-arranged.
- DS evidence: ToolJet/ToolJet frontend package.json uses Radix UI primitives (@radix-ui/react-*, colors); no Storybook script seen on develop; other repos ToolJet/ActionRail, tooljet-embed-app. Design hiring: Wellfound page links only (no listings parsed); none found.
- DS opportunity: Radix-based in-house components + embeddable app UI; no visible DS docs. Sources: https://raw.githubusercontent.com/ToolJet/ToolJet/develop/frontend/package.json

#### V3. Hasura (UPDATED; rebrand flag)
- Website: hasura.io | Founded 2017 (Inc42) | HQ: Inc42 registered San Francisco; Bengaluru ops | Funding $136.5M, Series C 21 Feb 2022 | Employees 120 (Inc42, E) | Revenue ND
- Signup/console: https://console.hasura.io/ . Pricing: DDN Free ("Start building"), Base and Advanced "Start free trial" (https://hasura.io/pricing).
- Access: A + B | Testable: DDN projects. FLAG: hasura.io/careers now redirects to promptql.io/careers (Gem job board), homepage content is PromptQL ("Try PromptQL", request demo) - the company appears to be pivoting to PromptQL; confirm which product is the target.
- DS evidence: github hasura/auth-ui-kit; Console lives in graphql-engine monorepo (no Storybook confirmed). Design team: none found.

#### V4. SigNoz (NEW)
- Website: signoz.io | Subcategory: open-source observability | Founded 2020 (Inc42) | HQ: Inc42 registered San Francisco; Bengaluru team (verify) | Funding: Seed $5.4M, 27 Sep 2023 | Employees 46 (Inc42, E)
- Signup: signoz.io "Get Started - Free", 30-day free trial, no credit card; self-hosted OSS. Pricing starts at $49/month.
- Access: A/B | DS evidence (STRONG): GitHub SigNoz/components, SigNoz/design-tokens, SigNoz/signoz-core-ui; npm @signozhq/design-tokens (1.1.4), @signozhq/button; frontend still uses antd 5.11. => DS exists and is mid-migration from Ant Design (inference). Design hiring not checked.

#### V5. Middleware (NEW; tier-2)
- Website: middleware.io | Subcategory: observability | Founded 2022 | Offices: San Francisco and Ahmedabad (about page) - tier-2 India (Ahmedabad) | Funding/employees: ND (no Inc42 page)
- Pricing: "Free Forever $0 ... Free access to all features with monthly limits" (100GB data), Sign Up Now; pages mention product tour/interactive demo.
- Access: A (+C mentions) | DS: npm @middleware/ui 404; none found.

#### V6. Keploy (NEW)
- Website: keploy.io | Subcategory: API/test generation, open source | Founded 2021 (Inc42) | Latest round 27 Sep 2026 (undisclosed; Inc42) | Employees 27 (Inc42, E) | HQ: ND
- Pricing: "Playground ... Free forever", no credit card, open-source. Access A.
- DS evidence: github keploy/ui repo exists (contents not browsed). Design hiring not checked.

#### V7. Hoppscotch (NEW)
- Website: hoppscotch.io | Subcategory: open-source API client | Founded 2019 (Inc42) | Seed $3.0M, 12 Dec 2021 | Employees 10 (Inc42, E) | HQ ND
- Access: A (open-source web app; pricing page renders minimal text - confirm plan limits) 
- DS evidence: npm @hoppscotch/ui (published) and github hoppscotch/ui. Very small team; high DS-in-public evidence.

#### V8. Testsigma (NEW)
- Website: testsigma.com | Subcategory: test automation | Founded 2019 | HQ Bengaluru (Inc42) | Series A $12.8M, 04 Jun 2024 | Revenue Rs 42.1 Cr FY25 (+38.2%) | Employees 235 (Inc42, E)
- Homepage FAQ: "offers a free trial to start"; app: https://app.testsigma.com/ (duration not stated). Access B.
- Design/DS: none found. 

#### V9. Dukaan (UPDATED)
- Website: mydukaan.io | Founded 2020 (Inc42) | HQ Bengaluru | Funding: $17.0M total, last 31 Dec 2023 (Inc42; earlier valueforstartups $29.4M, conflict) | Revenue Rs 10.0 Cr FY23 (Inc42; stale) | Employees 523 (Inc42, E)
- Pricing/home: "Free plan - no card", "Start free", "Free forever plan"; paid plans have no trial. Site pitches "a 1-person e-commerce stack" (AI pivot).
- Access: A | Design/DS: careers 404; none found.

#### V10. Graphy (NEW)
- Website: graphy.com | Subcategory: creator/course business platform | Founded/HQ/funding: ND in fetched sources (Inc42 slug not found; earlier note "Vedantu-owned" unverified)
- Signup: https://graphy.com/us/signup/ : "Start free in 2 minutes, no credit card". Pricing FAQ: "every plan comes with a 14-day free trial". Access B.
- Design/DS: none found (careers 404).

#### V11. Exly (NEW)
- Website: exlyapp.com | Subcategory: creator/coach commerce | Pricing: Starter FREE annual fee with 10% commission; Pro Rs 30,000, Premium Rs 1,08,000 annual (commission 6%/3%). Access A. Founded/HQ/funding ND (careers 404). Design/DS none found.

#### V12. TagMango (NEW)
- Website: tagmango.com | Founded 2019 | Mumbai (Inc42) | Seed $0.75M, 14 Dec 2021 | Revenue Rs 20.9 Cr FY25, +162.9% | Employees 79 (Inc42, E)
- Signup: https://tagmango.com/web/sign-up . Basic plan "Zero Fixed Fee, 10% commissions"; custom-domain "Freedom Setup" Rs 24,999 + GST/yr. Access A (take-rate). Careers page exists; no design role parsed. DS none found.

#### V13. Cosmofeed / SuperProfile (NEW)
- Website: cosmofeed.com (product SuperProfile, superprofile.bio) | Founded Sep 2021, Gurugram (about page) | Seed $1.5M, 15 Mar 2022 | Revenue Rs 11.7 Cr FY25 | Employees 153 (Inc42, E)
- Homepage: "Sign up for Free / Get started for free". Access A. Design/DS: none found.

#### V14. InVideo (UPDATED)
- Website: invideo.io | Founded 2017 (Inc42) | HQ: Inc42 San Francisco registered; Mumbai ops (earlier note) | Funding: Inc42 Series A $17.5M, Oct 2020; CB Insights $52.5M (conflict, stale) | Employees 253 (Inc42, E) | Revenue ND (earlier ~$70M ARR is an aggregator E)
- Signup: https://invideo.io/signup (200); pricing mentions Free plan and downgrade-to-free. Access A. Design: careers 404; none found.

#### V15. Sarvam AI (UPDATED)
- Website: sarvam.ai | Founded 2023 | Bengaluru (Inc42) | Series B, 14 Jun 2026; total $275M (Inc42); earlier reports: $234M (HCLTech-led) vs $350M at $1.55B valuation - conflict | Revenue Rs 29.1 Cr FY25 (+162%) | Employees 477 (Inc42, E)
- Signup via homepage "Sign up"; dashboard sign-in at indus.sarvam.ai (403 to bot fetch); homepage: "Playground - Test in browser, no setup"; products Indus Cowork, Voice Agents, STT/TTS. Access A/C (free credits not verified).
- Design team (STRONG, live): Ashby job board https://api.ashbyhq.com/posting-api/job-board/sarvam (48 postings) lists Product Designer, Motion Designer, Frontend Engineer (Chanakya), all Bengaluru. DS: none found.

#### V16. Shiprocket (UPDATED; flag)
- Website: shiprocket.in | Founded 2012 per Inc42 (Kartrocket lineage; earlier note 2017; older - flag) | HQ Gurugram/New Delhi | Funding $426.16M, Series E 25 Dec 2024 | Revenue FY25 ~Rs 1,632 Cr (Entrackr/Inc42 per earlier note) | Employees 2,006 (Inc42, E)
- Signup: https://app.shiprocket.in/newlogin ; pricing page: "No fees. No minimum sign up period. No credit card required." Access A (free account, pay per shipment). Careers: https://careers.shiprocket.in/ (not parsed for design). DS none found.
- Note: large, IPO-bound, near household in D2C circles; keep as stretch primary.

### Inferences
- Strongest DS-signal vertical/devtools targets: Appsmith, SigNoz, Hoppscotch, Chatwoot (horizontal), Sarvam (live designer hiring). For SigNoz/Appsmith the pitch is migration/consolidation since they already ship systems.
- Tier-2 coverage: Middleware (Ahmedabad), Kylas (Pune), Pabbly (Bhopal), Petpooja (Ahmedabad, secondary).

### Gaps
- Hoppscotch, Keploy, Exly, Graphy, Cosmofeed, Middleware: no funding/HQ confirmation in fetched sources.
- Teachmint/Classplus self-serve not verified (sites are demo/app-store led).
- Hasura vs PromptQL product status unresolved.
- No Indore, Coimbatore, Kochi, Jaipur companies vetted in this pass (Bik.ai and Wigzo checked: see secondary).

---

## 3. Companies moved to SECONDARY (or excluded), with reasons

### Takeaway
Moved because the fetched "signup/free trial" page is a demo/lead form, the site blocked verification, or the India link is weak. Revenue conflicts noted where Inc42 data changed earlier figures.

### Cited Findings
- Kissflow (was primary): DEMOTED to D. https://kissflow.com/get-started/ is a HubSpot form ("our solution experts will get in touch within one business day"); pricing page has no trial text (1 "book a demo"). About page: 350+ employees and a 2003 history (OrangeScape) vs product ~2012 - older. DS evidence: github kissflow/lcnc-component-example, kissflow/app-builder-plugin; blog on reusable components/design systems (earlier note). Still a strong DS-fit secondary (builder + runtime UI).
- Qandle (was primary): DEMOTED to D. Homepage CTA "Book a Free Trial" opens a form; now "part of MYND". Inc42: 2016, Gurugram, Seed $1.2M Feb 2018, Rs 5.7 Cr FY25, 47 employees.
- HROne: "Get Free Trial" links to https://hrone.cloud/demo/ (form); D. Inc42: 2016, Noida, Series B $7.93M Sep 2024, Rs 46.7 Cr FY25, 453 employees. Page copy lists "UI designer" tooling pages only (not a job).
- Smartlead: trial confirmed (app.smartlead.ai/sign-up; "All plans come with a free trial and no credit card") but India product org not verified (earlier note: Mumbai address only). Keep as optional primary only after India link is confirmed.
- Hiver (hiverhq.com HTTP 429), Verloop (403), Sprinto (403), Wigzo (403), DevRev (429): could not be verified; earlier claims (Hiver trial, Verloop free tier) stay UNVERIFIED. Inc42: Hiver founded 2011, $30M total, Series B 06 Mar 2022, Rs 71.6 Cr FY25 (+1.2%), 281 employees, Inc42 registered San Jose; Verloop 2016, $8M, Rs 37.6 Cr FY25 (+31%), 100 employees, Bengaluru; Sprinto 2020, $31.5M, Series B 08 Apr 2024, Rs 64.4 Cr FY25 (+134%), 445 employees; Wigzo 2015 New Delhi, 15 employees, Rs 9.4 Cr FY23.
- Kapture CX: https://www.kapture.cx/signup/ is "Sign up to AgentOS - Create your account" (a real account form, but enterprise-positioned; free access not stated); pricing page "request a demo". Inc42: 2014, Pre-Series B 29 Jun 2026, total $18.0M, Rs 40.9 Cr FY24 (earlier note Rs 52.1 Cr FY25), 665 employees. Could be promoted after click-test.
- SpotDraft: sales-led (request demo); Ashby board 18 postings, no design role. Inc42: 2017, total $88.55M, last round 26 Jan 2026, Rs 54.7 Cr FY25 (+16%) - conflicts with earlier note's ~Rs 121 Cr (earlier figure likely wrong or a different metric), 344 employees.
- Easyecom: FAQ says "We don't offer a self-serve free trial" - D. Inc42: 2015, Bengaluru, $1.8M, Rs 19.1 Cr FY25 (+72%), 202 employees.
- Pepper Content (2017, $18.66M, Rs 52.4 Cr FY25, 900 employees; book-a-demo), Atlan (2019, $201.5M, Rs 121.2 Cr FY24; sales-led), Bik.ai (book-a-demo only), Instasafe (2012; book-a-demo; Inc42 SF), Springworks (2014; no data), Locus (2015, $78.75M, Rs 66 Cr FY24; Inc42 Milpitas), LogiNext (2014, $49.6M, Mumbai; book-a-demo), Fleetx (2017, Gurugram, Series C 26 May 2025, total $38.5M, Rs 79.7 Cr FY25, 603 employees; request demo), ClickPost (2015, Gurugram, Series A $6M Apr 2024, Rs 19.6 Cr FY23, 208 employees; book-a-demo), Powerplay (2020, Bengaluru, $12.34M, Rs 34.0 Cr FY25; homepage empty to curl), UrbanPiper (2016, Bengaluru, Series B $36.5M Apr 2022, Rs 29.9 Cr FY25, 196 employees; pricing 404), DotPe (2019, Gurugram, $93.5M, Rs 82.8 Cr FY25 +47.7%, 550 employees; no trial found).
- GoKwik (2020, Gurugram; $68.45M, Rs 117.5 Cr FY25 +24%, 626 employees; 42 "book a demo" on home), Shopflo (2021, Bengaluru, Seed $2.6M May 2022, 83 employees: "sign up" is a qualification form with company/platform fields = D), Petpooja (2011, Ahmedabad, $21.9M, Rs 77.2 Cr FY24, 1,789 employees; book-a-demo), Teachmint (2020 per Inc42, Bengaluru, $118M, Rs 99.4 Cr FY25 vs Entrackr Rs 74 Cr operating, 661 employees; book-a-demo; careers on Keka ATS), Classplus (2018, Noida, $158.3M, Series D Mar 2022, Rs 142.8 Cr FY24 per Inc42 - earlier notes conflict at Rs 213-265 Cr; unresolved), Shopflo/GoKwik/Petpooja/Teachmint/Classplus all D-or-unverified. Large earlier secondaries (Darwinbox, Yellow.ai, MoEngage, LeadSquared) unchanged: not re-fetched.
- Excluded for age/household: Wingify/VWO (2009), Plivo (US), LambdaTest/TestMu (2017, free plan exists, large and widely known; optional).

### Inferences
- Roughly one-third of earlier "primary" SaaS claims did not survive fetching: a "free trial" button often opens a demo form (Keka partly, Kissflow, Qandle, HROne, Shopflo).

### Gaps
- Unverifiable due to blocks: Hiver, Verloop, Sprinto, Wigzo, DevRev.
- Revenue conflicts unresolved: Whatfix, Classplus, Teachmint, Keka FY24.
