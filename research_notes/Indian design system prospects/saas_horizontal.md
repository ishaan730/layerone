# Indian Horizontal B2B SaaS - Design-System Prospects for Layer One (researched 2026-11-17)

## METHOD CAVEATS (read first)
- In this session every direct fetch of company sites, Inc42, Entrackr failed (host not in allowed network: keka.com, interakt.shop, aisensy.com, wati.io, inc42.com, entrackr.com). Only web search was usable. So: (1) NO signup/trial link was fetched and verified by loading it; "Signup URL" values are URLs that appeared in search results, or are marked "UNVERIFIED (not fetched)". (2) Access category = best evidence from search snippets of company pages + review sites; confirm by clicking before outreach. (3) Design-system evidence = job posts / search hits only; "none found in search" does NOT mean the company lacks one. Company repos/Storybook/npm/Dribbble were not browsable.
- Figures: R = reported by press/filing-sourced outlet; E = aggregator estimate (Latka, Bitscale, CB Insights etc.). Conflicts are noted. "ND" = Not publicly disclosed / not found.
- Verdict on goal: ~18 primary + 8 secondary listed, but primary access claims are search-derived (see per-record "Confidence").

## PRIMARY - self-serve access (Categories A/B/C)

### 1. Keka (Keka Technologies)
- Website: keka.com | Subcategory: HRTech / HRMS + payroll + talent | Founded: 2015 (ND in sources fetched; from prior knowledge, UNVERIFIED) | HQ: Hyderabad
- Funding: ~USD 57M Series A (WestBridge, Nov 2022) + USD 1.6M revenue-based (Recur Club) = ~USD 58.6M (R) - https://inc42.com/buzz/keka-raises-57-mn-funding-help-smes-automate-hr-functions/ ; https://inc42.com/company/keka-hr/captable/
- Latest round: Series A 2022 (+ RBF Apr 2026 per https://telanganatoday.com/hyderabad-based-keka-hr-raises-1-6-million-through-recur-club). Valuation: not official; third-party 115.59M USD (Jun 2023, E) - https://www.thecompanycheck.com/company/b/keka/f0l1fn0bhpbgncrjg
- Revenue: Rs 133.9 Cr FY25, up 54.5% from Rs 86.6 Cr FY24; net loss Rs 71.8 Cr (Inc42, R) - https://inc42.com/company/keka-hr/financials/ (Entrackr earlier put FY24 at Rs 78 Cr: conflict)
- Employees: 1,275 (Inc42 profile); 888 (Jan 2025, thecompanycheck); LeadIQ ~1.2K Apr 2026 (E)
- Product: Keka HR | Product URL: https://www.keka.com | Signup/trial: https://www.keka.com/signup-v2 (appeared in search; UNVERIFIED by fetch) - pricing page https://keka.com/pricing shows "Free Trial" on Foundation/Growth/Enterprise plans
- Access: B (Free Trial). Trial length not confirmed (14-day claim unverified). Explorable: self-serve trial of core HR, payroll, leave, attendance per pricing-page listing. Source: https://www.keka.com/signup-v2 ; https://subscribed.fyi/?p=110453
- Design team: STRONG. Multiple Product Designer / Lead Designer roles incl. "Lead Designer, Design Systems" and "Senior Product Designer, Design System" - https://hr.keka.com/careers/jobdetails/75543 ; https://jobs.weekday.works/keka-lead-designer---design-systems ; https://overseasjobs.com/job/details/27983596/lead-product-designer (posted Nov 2024)
- Design system: internal "Keka Design System" being built/maintained (job posts mention accessibility audits, VPAT docs). Public docs/Storybook/npm: none found. NOTE: they already hire for it -> pitch is scale/audit/accessibility/multi-product, not greenfield.
- Why need: HRMS + payroll + hiring + performance + expense + employee app, admin vs employee vs manager roles, web + mobile, expanding to US/GCC (localisation, VPAT). Confidence: high on funding/revenue, medium on access.

### 2. SuperOps
- Website: superops.com | Subcategory: IT management - MSP/PSA/RMM (horizontal IT mgmt) | Founded: 2020 (R) | HQ: Dallas TX (US) with India product/engineering org (Chennai/Bengaluru) - US-HQ w/ India-founded team; verify
- Funding: USD 54.4M total after Series C (R) - https://channele2e.com/news/superops-earmarks-25m-series-c-for-endpoint-ai-tools ; Series B USD 12.4M Oct 2023 (Addition, March Capital, Matrix) https://techcrunch.com/2023/10/10/superopsai/
- Latest round: USD 25M Series C (led by March Capital; year ND in snippet, after Oct 2023) | Valuation: ND
- Revenue: ND (founder target USD 50M in 2-3 yrs, a goal not actual) | Employees: ~200 (2025 article), ~220 (E)
- Product: SuperOps (PSA+RMM) | URL: https://superops.com | Signup: https://superops.com/signup ("Why commit before you get a chance to try us out?" - 14-day trial, full suite)
- Access: B (14-day free trial, reportedly no card; one aggregator Krowdbase disagrees, vendor page preferred). Explorable: full PSA, RMM, ticketing, documentation.
- Design team/DS: not verified; none found in search.
- Why need: PSA + RMM + Documentation + Service Desk modules, technician console + client portal + mobile, multiple product lines (SuperOps, endpoint, AI). Confidence: medium.

### 3. Whatfix
- Website: whatfix.com | Subcategory: Digital adoption platform (workflow/productivity) | Founded: 2014 | HQ: Bengaluru (US ops in San Jose)
- Funding: ~USD 201M (CB Insights, E); 139.5M (Latka) / 265.5M (thecompanycheck): conflict. Latest: USD 125M Series E Sep 2024 (Warburg Pincus, SoftBank), valuation ~USD 900M (R) - https://business-standard.com/companies/start-ups/startup-firm-whatfix-raises-125-mn-in-series-e-round-led-by-warbug-pincus-124092501167_1.html ; https://multiples.vc/private-comps/whatfix
- Revenue: Rs 556.7 Cr (~USD 66M) FY25, +31% from Rs 424.6 Cr (R); Latka USD 138.8M is E
- Employees: 1,107 (Jun 2026, TipRanks), 1,190 (Inc42)
- Product: Whatfix DAP | URL: https://whatfix.com/dap/ | Trial: https://whatfix.com/request-trial (form; may be sales-gated) 
- Access: B/D borderline - "request trial"/"test drive" free; GetApp/subscribed.fyi mention limited free plan (conflict). Confirm if self-serve. Explorable: Editor/authoring + flows on a sandbox.
- Design team/DS: not verified; none found.
- Why need: multiple products (DAP, Mirror, Product Analytics, Enterprise Content), a browser extension/authoring editor + end-user widgets embedded on third-party apps (needs themeable components). Confidence: medium.

### 4. Kissflow
- Website: kissflow.com | Subcategory: Workflow automation / low-code | Founded: ~2012 (outside preferred window; prior knowledge UNVERIFIED) | HQ: Chennai (TIDEL Park) - https://thefederal.com/category/business/significant-threat-to-saas-products-today-firms-must-innovate-refine-offerings-suresh-sambandam-148868
- Funding: ~USD 1M early then largely bootstrapped; sources conflict (1M-40M) (pitchbook/Latka); latest round ND; valuation ND
- Revenue: ND reported; estimates 9M (Latka), 27M (Sacra), 90.3M (aggregator) - wildly inconsistent, do not use
- Employees: 340 (PitchBook), 470 (AppsRunTheWorld), 568 (BuiltIn); 45-50 laid off earlier (Inc42) https://inc42.com/buzz/kissflow-cuts-45-50-jobs-as-part-of-annual-performance-review
- Product: Kissflow (Work Platform / Process / Project / Case / Low-code) | URL: https://kissflow.com
- Signup: UNVERIFIED (not fetched) - commonly kissflow.com signup flow
- Access: B (14-day free trial per aggregator; freemium discontinued) 
- Design: blog on reusable components & design systems in low-code https://kissflow.com/low-code/reusable-components-and-design-systems-in-enterprise-lowcode-development/ ; no public Storybook found. 
- Why need: 5+ modules, builder (low-code) UI + runtime apps for end users, white-label/customer-built apps => themeable component library is core product. Confidence: medium.

### 5. Hevo Data
- Website: hevodata.com | Subcategory: Data integration/ELT (horizontal data tooling - borderline vs devtools researcher; flag) | Founded: 2017 | HQ: San Francisco with Bengaluru ops (India entity Hevo Technologies India Pvt Ltd) - US-HQ/India-founded
- Funding: USD 43M (Latka) - 44.5M (CB Insights); latest USD 30M Series B Dec 2021 (Sequoia India, Qualgro) https://inc42.com/buzz/hevo-data-grabs-30-mn-funding-from-sequoia-capital-qualgro/ ; valuation ND
- Revenue: Rs 80.5 Cr FY25 (down 17.5% from Rs 97.6 Cr FY24), PAT Rs 9.2 Cr (Inc42/IST estimate) https://inc42.com/company/hevo-data/financials ; Latka USD 46.9M (E, conflicts)
- Employees: ND in search | Product: Hevo Pipeline | URL: https://hevodata.com | Signup: UNVERIFIED
- Access: A/B (free plan + 14-day trial from prior knowledge, NOT confirmed by search) 
- Design/DS: none found. 
- Why need: console with many connectors/ pipelines/ destinations, transformation & activation modules. Confidence: low on access.

### 6. Rocketlane
- Website: rocketlane.com | Subcategory: Customer onboarding / PSA / project mgmt | Founded: 2019 (prior knowledge, UNVERIFIED) | HQ: Chennai + Lehi, Utah (dual)
- Funding: USD 45M total; USD 24M Series B June 2024 (8VC, Matrix India, Nexus) https://techcrunch.com/2024/06/25/rocketlane-snags-24m-to-bring-ai-led-experiences-for-professional-services-teams ; valuation ND
- Revenue: ND (company said 3x growth, 500+ customers 2023) | Employees: ~120 (2024 report)
- Product: Rocketlane | URL: https://rocketlane.com | Signup: UNVERIFIED
- Access: B (self-serve free trial per one aggregator of doubtful reliability - it cited a July 2026 round not seen elsewhere). Verify.
- Design/DS: none found. Why need: customer-facing portal + internal PSA workspace (two audiences), growing AI modules. Confidence: low.

### 7. Wati
- Website: wati.io | Subcategory: WhatsApp business platform / conversational | Founded: 2020 (Extruct, single source) | HQ: ND consistently (reported as Hong Kong-registered with India eng; UNVERIFIED) 
- Funding: USD 32.3M over 4 rounds; Series B USD 23M Oct 2022 (Tiger, Sequoia, DST, Shopify) https://www.cbinsights.com/company/wati/financials ; valuation ND
- Revenue: ND | Employees: 201-500 (Extruct)
- Product: Wati | URL: https://www.wati.io | Pricing/trial: https://www.wati.io/pricing/ ; Signup UNVERIFIED
- Access: B (7-day free trial, no card per Capterra) https://www.capterra.com/p/204314/WATI/pricing/ 
- Design/DS: none found. Why need: shared inbox, broadcast, chatbot builder, Shopify/CRM integrations, agent + admin. Confidence: medium (India-HQ status uncertain - confirm).

### 8. Interakt (Jio Haptik)
- Website: interakt.shop | Subcategory: WhatsApp commerce / CRM for SMBs | Founded: ND | HQ: Mumbai (Haptik group, verify)
- Funding: ND for Interakt; parent Haptik ~USD 12.2M (E). Revenue: parent Haptik Rs 156.6 Cr FY24 (Inc42) https://inc42.com/company/haptik/financials ; Interakt Latka USD 4.5M 2025 (E, low confidence)
- Product: Interakt | URL: https://www.interakt.shop | Signup: UNVERIFIED
- Access: B (14-day free trial per one profile). Note: Haptik SOLO (new SMB platform) reported with free plans https://yourstory.com/2025/09/jios-haptik-rs-10000-whatsapp-ai-agents-small-businesses
- Design/DS: none found. Why need: two products under one group (Interakt, SOLO, Haptik). Confidence: low.

### 9. AiSensy
- Website: aisensy.com | Subcategory: WhatsApp marketing/API platform | Founded: ND | HQ: ND (India)
- Funding: Latka USD 100K seed 2022 (E, low); CB Insights lists one investor, no amount. Valuation ND.
- Revenue: Latka USD 8.9M for 2025 (E) https://getlatka.com/companies/aisensy | Employees: ND
- Product: AiSensy | URL: https://aisensy.com | Pricing: https://aisensy.com/pricing ; free plan FAQ https://faq.aisensy.com/aisensy-forever-free-plan-everything-you-need-to-know
- Access: A (Forever Free plan, no time limit; no broadcast/template API on free). Explorable: dashboard, inbox, API access.
- Design/DS: none found. Why need: marketing + inbox + chatbot + campaigns; fast-growing. Confidence: medium on access, low on numbers.

### 10. Gallabox
- Website: gallabox.com | Subcategory: WhatsApp/ conversational commerce | Founded: ND | HQ: ND (India; teams in ME, LatAm, US)
- Funding: USD 3.5M seed Jan 2025 (FUSE, Prime Venture, Neon); total ~USD 5M https://yourstory.com/2025/01/conversational-commerce-platform-gallabox-seed-funding-fuse
- Revenue: Rs 4.8 Cr FY25, loss Rs 2.3 Cr (Indian Startup Times, R) https://www.indianstartuptimes.com/startup-deep-dive/gallabox-deep-dive/ | Employees: 30-95 (conflicting E)
- Product: Gallabox | URL: https://gallabox.com | Signup UNVERIFIED
- Access: B (free trial reported by Software Advice/Softwarefinder). Design/DS: none found. Smaller; lower fit but good trial access. Confidence: medium.

### 11. Kylas
- Website: kylas.io | Subcategory: Sales CRM | Founded: 2019/2020 (conflict) | HQ: Pune
- Funding: none disclosed (bootstrapped per Latka/IST) https://www.indianstartuptimes.com/?p=26758 | Revenue: USD 7.6M 2025 (Latka, E) https://getlatka.com/companies/kylas.io
- Product: Kylas CRM (parent Sell.Do) | URL: https://kylas.io | Signup UNVERIFIED | Access: B (free trial; Gappsy also tags free plan, unverified) 
- Design/DS: none found. Why need: CRM + marketing + telephony modules, web+mobile. Confidence: low-medium.

### 12. Qandle
- Website: qandle.com | Subcategory: HRMS / payroll | Founded/HQ/funding/revenue: ND in searches
- Access: B - own page advertises "14-day free trial" https://www.qandle.com/keka-alternative.html (Keka-alternative landing page)
- Product: Qandle | URL: https://www.qandle.com | Signup UNVERIFIED | Design/DS: none found. Gap: no firmographics found. Confidence: low.

### 13. Hiver
- Website: hiver.com | Subcategory: Customer support helpdesk inside Gmail | Founded: 2011 (outside window, selective) | HQ: Bengaluru
- Funding: USD 22M Series B (K1 Capital, 2021) https://inc42.com/buzz/hiver-bags-22-mn-in-funding-to-help-companies-streamline-customer-service ; valuation ND
- Revenue: last reported USD 9.6M (2022); Latka USD ~25M (Oct 2024 E) | Employees: 164-288 (conflicting)
- Access: trial UNVERIFIED in search (free trial believed from prior knowledge). Design/DS: none found. 70% revenue from North America. Why need: helpdesk + knowledge base + CSAT + analytics + AI. Confidence: low on access.

### 14. Verloop.io
- Website: verloop.io | Subcategory: Conversational AI / support | Founded: 2016 (prior knowledge) | HQ: Bengaluru
- Funding: USD 8M over 4 rounds; USD 5M Series A-II Aug 2020 https://www.cbinsights.com/company/verloop/financials | Revenue: Rs 28.6 Cr FY24 (loss Rs 9.3 Cr) one source vs Rs 42.8 Cr unverified https://voice.lapaas.com/startup/verloop-io/financials/
- Access: A (free starter tier per site claim in search). Design/DS none found. Confidence: low-medium.

### 15. Mailmodo
- Website: mailmodo.com | Subcategory: Marketing automation (interactive email) | HQ/founded: ND here (YC-backed, 2019-20) | Funding: USD ~2.27M total, USD 2M seed Jul 2021 (Surge, YC) https://entrepreneur.com/en-in/finance/mailmodo-raises-2-mn-seed-funding/378086
- Revenue: ND; estimates USD 1.6M vs 15.1M (conflict, unusable) | Access: B (free trial per G2); free plan disputed https://www.g2.com/products/mailmodo/pricing
- Design/DS: none found; interesting due to email builder/editor UI. Confidence: low.

### 16. Pabbly
- Website: pabbly.com | Subcategory: Workflow automation / SaaS suite (Connect, Subscription Billing, Email Marketing) | HQ: Bhopal | Founded: 2017-2019 (conflict) | Funding: bootstrapped | Revenue: Latka USD 3.1M (E)
- Access: A/B ("free tier" per review; one-time plans); confirm. Source: https://www.pabbly.com/connect/about ; https://getlatka.com/companies/countries/india/cities/bhopal?cap=mid
- Multiple products under one brand -> consistency case. Design/DS none found. Confidence: low.

### 17. Chatwoot
- Website: chatwoot.com | Subcategory: Open-source customer support/omnichannel | Founded: 2017 | HQ: Bengaluru/SF (conflict) 
- Funding: USD 1.6M (Inc42) vs ~130K (CB Insights) https://inc42.com/company/chatwoot/funding/ | Revenue: Rs 2.2 Cr FY25, down 11.7% (Inc42) https://inc42.com/company/chatwoot/
- Access: A (open-source self-host free; cloud trial UNVERIFIED). Public GitHub => design/UI code publicly inspectable (not browsed). Small but ideal for code-level audit. Confidence: low-medium.

### 18. Smartlead
- Website: smartlead.ai | Subcategory: Sales engagement / cold email | India link: Capterra India lists Mumbai address only - weak; Latka USD 14M rev (E) | Trial: 14-day (Notion/Capterra India) | Funding ND. Include only if India product org confirmed. Confidence: low.

## SECONDARY - sales-led / no confirmed self-serve (Category D/E)
1. Darwinbox (Hyderabad; 2015): FY25 total revenue ~Rs 534 Cr (+ ~60% vs Rs 334 Cr) https://entrackr.com/news/darwinboxs-revenue-rises-to-rs-534-cr-in-fy25-narrows-adjusted-losses-10572733 ; funding USD ~296-307M; USD 40M TVG Aug 2025. Excluded from primary: enterprise HCM, demo-led; no trial found. Huge design-system need (HCM + mobile + modules). 
2. Yellow.ai (Bengaluru/SF; 2016): FY25 India entity Rs 235.9 Cr (Inc42), PAT Rs 0.79 Cr; Series C USD 78.15M Aug 2021, total USD 102M https://inc42.com/company/yellow-ai/financials/ ; ~863 employees. Exclusion: self-serve not confirmed; trial status unchecked (G2 mentions a free tier historically - verify).
3. MoEngage (Bengaluru; 2014): USD 100M (Nov 2025) + USD 180M Series F ext (Dec 2025) https://www.moengage.com/in-the-news/moengage-gets-100m-to-scale-marketing-ai-agents-and-accelerate-expansion-in-north-america/ ; revenue Rs 311.5 Cr FY24 (Inc42, R). Exclusion: demo-led; no trial found. Multi-module (Analytics, Inform, Cards, Inbox, AI agents).
4. LeadSquared (Bengaluru; founded 2011): FY25 operating revenue Rs 326 Cr, net loss Rs 89 Cr https://entrackr.com/fintrackr/leadsquared-trims-losses-by-45-in-fy25-growth-remains-modest-10561373 ; USD 153M Series C Jun 2022; total ~USD 188-189M; ~1,060 employees. Exclusion: trial status not found (book-a-demo); outside founding window.
5. Sprinto (Bengaluru; 2020): USD 20M Series B Apr 2024 (Accel), total ~USD 31.5M https://sprinto.com/blog/sprinto-series-b/ ; FY25 Rs 64.4 Cr (Inc42; another source 110.8 Cr - conflict); ~433 employees. Exclusion: no self-serve trial found (compliance automation is typically demo-led).
6. SpotDraft (NY/Bengaluru; 2017): USD 54M Series B Feb 2025 + 8M ext Jan 2026 (total ~USD 90M, CB Insights); FY25 ~Rs 121 Cr, loss Rs 121 Cr https://india.entrepreneur.com/news-and-trends/spotdraft-raises-usd-8-mn-in-series-b-extension-from/502230 . Exclusion: sales-led CLM; legal-tech vertical-leaning; no trial.
7. Kapture CX (Bengaluru; 2014): USD 10M pre-Series B Jul 2026 (Bajaj Finserv Ventures) https://www.kapture.cx/press-releases/kapture-raises-10-million-pre-series-b-funding/ ; FY25 Rs 52.1 Cr (Inc42) / ~48 Cr (VI); headcount 296-627 conflicting. Exclusion: no free trial (G2/Capterra); BFSI-heavy.
8. Zimyo (Noida; 2020): FY25 revenue Rs 9.4 Cr (Inc42) - much smaller than hype; funding ~USD 3.7M https://inc42.com/company/zimyo/financials/ ; no free trial found. Exclusion: no trial evidence, small.
- Also surfaced: Zluri (Bengaluru/ US; USD 20M Series B Jul 2023 Lightspeed, total ~USD 32M; FY22 operating revenue Rs 5.83 lakh; no trial found; sales-led), Leena AI (USD 30M Series B Oct 2025 per Salestools, valuation USD 250M unverified; no trial; enterprise).

## GAPS (no usable data in this session)
- Springworks, Salesken, Scrut Automation, Unstop, HROne, WebEngage: no funding/revenue/trial data returned by searches; not assessed. Superset: FY25 revenue Rs 10.8 Cr and PAT Rs 13.5 Cr (Inc42; odd, verify) https://inc42.com/company/superset/financials/ - student/talent platform, not clearly horizontal B2B SaaS.
- No Storylane/Navattic (Category C) demo pages were found for any target company (one search returned only vendor-landscape articles). No company confirmed as Category C.
- Founded year / HQ for AiSensy, Gallabox, Interakt, Qandle, Mailmodo not confirmed from sources.
- All design-team/design-system claims beyond Keka are unverified; recommend a follow-up pass with open network access: company /careers pages, Dribbble, GitHub org, npm scope, Storybook subdomains, then click-test each signup URL.
