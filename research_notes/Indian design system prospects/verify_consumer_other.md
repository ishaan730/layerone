# Verification pass: Indian consumer tech and other-sector prospects for Layer One

Date of pass: 2026-11-17. Scope: consumer (travel, commerce, subscriptions, on-demand, content) and other sectors (edtech, logistics, mobility, proptech, agritech, jobs, legaltech, B2B marketplaces).

## Method and source-quality notes (read first)

- URL checks: `curl -sL` against each homepage (Chrome user agent). "200" means the page loaded; "login/signup markers" means the homepage HTML contained login/sign-in/register strings. I did NOT complete any signup or OTP flow, so access category is "page reachable plus login UI present", not "booked/enrolled end to end". Everything flagged "app-only" had no usable web funnel in the HTML.
- Founded year, HQ, total funding, last-round date, employee count, valuation: taken from Inc42 company profile and funding pages, fetched directly (inc42.com now fetchable). Inc42 is a tracker (aggregator), not a primary source; it has visible errors (listed below). Employee counts are Inc42 figures as of 2026-11-17 (a tracker snapshot, likely LinkedIn-derived), not company-reported. Source tag "Inc42 profile" = https://inc42.com/company/{slug}/ and "Inc42 funding" = https://inc42.com/company/{slug}/funding/.
- Revenue figures: FY25 unless stated. "Entrackr/Inc42 headline" figures carry over from the earlier notes (RoC-based, secondary). Where Inc42 profile and earlier headline differ, both are given.
- Design-team evidence: Ashby public job-board API (jobs.ashbyhq.com/atlys, /Bounce) checked directly; the rest from aggregator listings surfaced by WebSearch (designproject.io, foundit, startup.jobs, Cutshort, Greenhouse). Careers pages on most company sites are JS/ATS rendered and returned no designer keywords to curl, which is NOT evidence of no designers. "None found in this pass" = not found, not absent.
- Design-system evidence: npm registry scope search for about 55 company-name scopes returned zero packages. GitHub (api and github.com) is blocked from this environment (403), so GitHub orgs, Storybook and public docs were not checked. "None found" below means only "no public npm scope found; GitHub/Storybook not checkable". Never read as "no design system".
- Budget: about 12 WebSearch calls used, plus direct fetches. Gaps are listed at the end.
- Access categories: A Freemium (free browse plus account), B Free trial, C Public demo, D Sales-led, E None.

## Changes to previous notes (headline)

1. Rentomojo: listed on NSE/BSE on 2026-09-17 (IPO Rs 1,255.57 Cr, issue price Rs 404, subscribed about 72x) — [Business Standard IPO page](https://www.business-standard.com/markets/ipo/rentomojo-ltd-ipo-68302), [5paisa](https://www.5paisa.com/blog/rentomojo-ipo-listing), [Inc42 profile shows "Listed"](https://inc42.com/company/rentomojo/). Founded 2014 per Inc42 (2012 in earlier note). Moved to SECONDARY (listed, pre-2015/borderline, large).
2. Cashify: Inc42 lists founded 2009 for legal entity (Manak Waste Management Pvt Ltd), earlier note said 2013; both pre-2015. Total funding Inc42 $313.5M vs earlier note about $130M (conflict, unresolved). Moved to SECONDARY (pre-2015).
3. Shadowfax: listed on NSE/BSE 2026-01-28 at Rs 124 issue price — [Entrackr](https://entrackr.com/news/shadowfax-lists-at-9-discount-on-market-debut-11035898). Moved to SECONDARY.
4. Stage: Inc42 profile lists founded 2014, Noida HQ, 47 employees; earlier note said about 2019, Gurugram/Jaipur. Employee count of 47 is implausible against Rs 112.7 Cr revenue and 132 jobs on a Greenhouse board named "stage" (board ownership unconfirmed). Founded year and HQ unresolved; flagged.
5. Snabbit: Inc42 profile says HQ Mumbai, earlier note Bengaluru (unresolved; Snabbit job posts found were for Bengaluru). Series D 2026-04-27/28 ($113.2M total per Inc42; valuation $179.5M per Inc42 funding page, which conflicts with $350M-$400M in earlier press-based note). Not resolved.
6. Pronto: real site is withpronto.com (pronto.in is a parked frames page). Inc42 reported HQ moved from Gurugram to Bengaluru ([Inc42](https://inc42.com/?p=538767)). Inc42 valuation $82.9M conflicts with earlier $200M (May 2026) press figure. Promoted from SECONDARY to PRIMARY (verified Play/App Store app; app-only).
7. Supertails: Inc42 FY25 revenue Rs 33.0 Cr vs earlier Indian Retailer Rs 108.26 Cr; likely different bases (consolidated vs entity) — unresolved.
8. Atlys: Inc42 total funding $84.25M (earlier arithmetic $72M); Series C date 2026-03-16.
9. StayVista: Inc42 founded 2015, HQ Mumbai, total funding $11.39M (Series B Jun 2025); earlier note said ~2018, Gurugram. Elivaas total $17.5M.
10. Headout: Inc42 founded 2015 (earlier 2014), total $64.2M, last round Series B 2022-02-02, employees 789; Inc42 HQ text "New York" (global company with Bengaluru product org; HQ conflict). Site returns 403 to curl (CloudFront bot block); not a lack of a product.
11. Seekho: Inc42 founded 2021 (earlier ~2019-20), Series B, total $39.47M, last round 2025-09-03, 48 employees (implausibly low vs 100M downloads; likely partial LinkedIn count).
12. Pratilipi: Inc42 founded 2015, Series E Apr 2025, total $101.68M, 788 employees; earlier note said ~2014.

## Section A. Consumer tech, PRIMARY (20 companies)

Format per record: Website | Subcategory | Founded | HQ | Total funding | Latest round | Valuation | Revenue | Employees | Product | Product URL | Signup URL | Access | Free access | Testable | Design team | DS | DS opportunity | Sources | Notes.

### C1. Atlys (UPDATED)
- Website: atlys.com | Subcategory: visa processing, B2C plus agent product | Founded: 2020 (Inc42 profile) | HQ: Delhi per job posts ("Delhi HQ" role page); Inc42 text says San Francisco (conflict) | Total funding: $84.25M+ (Inc42; earlier note about $72M by sum) | Latest round: Series C $36M, March 2026 (Susquehanna Asia; MakeMyTrip joined) | Valuation: Not publicly disclosed | Revenue: Rs 31.8 Cr FY25 (Inc42), up about 231% | Employees: 381 (Inc42, Nov 2026).
- Product: Atlys web app, visas for 120+ destinations | Product URL: https://www.atlys.com/en-US (200; title "Get Visas On Time to 120+ Destinations") | Signup URL: account created inside application flow (login UI not isolated in HTML; unverified) | Access: A | Free access: Yes (requirements, pricing, application start) | Testable: destination search, visa requirements, application and document-upload funnel, tracking.
- Design team: Ashby board lists Product Designer (published 2026-07-31) and Graphic Design Intern (2026-11-06) — [Ashby Product Designer](https://jobs.ashbyhq.com/atlys/9b25615c-572a-4fc0-975c-9745e412911d). Aggregator summaries of Atlys listings mention contributing to a design system (unverified on primary page).
- DS: none found publicly. Opportunity: multi-country flows, agent product, rapid hiring after Series C; strongest evidence of an active design hire in this set.
- Sources: [Inc42 profile](https://inc42.com/company/atlys/), [Entrepreneur India](https://india.entrepreneur.com/news-and-trends/atlys-raises-usd-36-mn-in-series-c-round/503468).

### C2. Scapia (UPDATED)
- Website: scapia.cards | Subcategory: travel credit card plus travel booking | Founded: 2022 | HQ: Bengaluru | Total funding: $134.82M+ (Inc42) | Latest round: $63M Series C, May 2026 (General Catalyst) | Valuation: $500M (Inc42 funding page; Entrackr figure about $539M) | Revenue: Rs 40.4 Cr total income FY25 (Inc42); about Rs 28.7-29 Cr operating, net loss about Rs 83 Cr (Entrackr) | Employees: 321 (Inc42).
- Product: Scapia app and card | URL: https://www.scapia.cards/ (200; "A credit card for the traveller in you") | Signup: app-based card onboarding with KYC (not exercised) | Access: A/E borderline (browse free; card issuance needs KYC) | Free access: Limited | Testable: marketing site, app download, onboarding to the KYC gate.
- Design team: Senior Product Designer and Lead Product Designer postings (B2C travel and cards experience) on [designproject.io](https://designproject.io/jobs/senior-product-designer-at-scapia-y4d3j6) and [foundit](https://www.foundit.in/job/senior-product-designer-scapia-bengaluru-bangalore-39611061) (aggregators). DS: none found. Opportunity: fintech plus travel in one app, post-round hiring.

### C3. Headout (UPDATED)
- Website: headout.com (curl returns 403; reachable in browser) | Subcategory: tours and experiences marketplace | Founded: 2015 (Inc42; earlier 2014) | HQ: conflict (Inc42 New York; Bengaluru product org per earlier note) | Total funding: $64.2M+ (Inc42; other trackers $30M-$75.8M) | Latest round: Series B, 2022-02-02 (Inc42) | Valuation: Not publicly disclosed | Revenue: self-reported $130M calendar 2024 (company newsroom, not FY) | Employees: 789 (Inc42, Nov 2026; earlier 405-772).
- Product: web, iOS, Android booking | URL: https://www.headout.com | Signup: account at checkout/login on site (not curl-verifiable) | Access: A | Free access: Yes | Testable: city and attraction search, PDPs, multi-currency booking funnel.
- Design team: Lead Product Designer and Product Designer on [Greenhouse](https://job-boards.greenhouse.io/headoutlinkedin/jobs/4690944006) and [second post](https://job-boards.greenhouse.io/headoutlinkedin/jobs/4672973006); Ashby board (22 jobs) showed only a Frontend Developer in design/frontend titles on 2026-11-17. DS: junior role mentions maintaining design system and component docs (earlier note); public docs none found. Opportunity: audit/scale, not greenfield.
- Sources: [Inc42 profile](https://inc42.com/company/headout/), [Headout newsroom](https://newsroom.headout.com/news/headout-revenue-surges-to-130m/).

### C4. Zingbus (UPDATED)
- zingbus.com | intercity bus | Founded 2019 | HQ Gurugram | Total $15.13M+ (Inc42) | Latest: Series A, 2024-12-17 | Valuation: $9.98M listed by Inc42 (low-confidence tracker figure) | Revenue: Rs 161 Cr FY25 (Entrackr; Inc42 Rs 161.1 Cr) | Employees 447 (Inc42).
- Product URL: https://www.zingbus.com (200; "Bus Ticket Booking Online") | Signup: login at booking | Access: A | Free: Yes | Testable: route search, seat map, booking funnel, account.
- Design team: none found. DS: none found. Opportunity: web plus app, operator/driver tooling.

### C5. StayVista (UPDATED)
- stayvista.com | villa rentals | Founded 2015 (Inc42; earlier ~2018) | HQ Mumbai (Inc42; earlier Gurugram — conflict) | Total $11.39M+ | Latest: Series B, June 2025 | Valuation: Not publicly disclosed | Revenue Rs 181-183 Cr FY25 (profit about Rs 3.6 Cr per Pulse/Entrackr summary) | Employees 533.
- URL: https://www.stayvista.com/ (200) | Access A | Free Yes | Testable: villa search, PDP, booking; host side not public.
- Design team: Associate Visual Designer (Cutshort) only; no product designer found. DS none found. Opportunity: guest plus host/owner products, multiple brands.

### C6. Elivaas (UPDATED)
- elivaas.com | luxury villas | Founded 2022 | HQ Gurugram | Total $17.5M+ | Latest: Series B, Aug 2025 | Valuation: Not publicly disclosed | Revenue Rs 40.1 Cr FY25 (Inc42; up about 403%) | Employees 441.
- URL: https://www.elivaas.com/ (200) | Access A | Free Yes | Testable: villa search, PDP, booking.
- Design team: none found; DS none found. Opportunity: rapid growth, young product.

### C7. Snabbit (UPDATED)
- snabbit.com | 10-minute home services | Founded 2024 | HQ Mumbai (Inc42) vs Bengaluru (earlier; unresolved) | Total $113.2M+ (Inc42) | Latest: Series D, April 2026 (Rs 528 Cr / $56M reported) | Valuation: $179.5M (Inc42) vs $350M-$400M (press) — conflict | Revenue: Rs 1.1 Cr FY25 (Inc42, entity FY25 tiny) | Employees 618.
- URL: https://www.snabbit.com/ (200; "House Help & Home Cleaning in 10 Min"); Play Store package com.snabbit.customer returned 200 | Access: A, geo-limited to served cities | Free: Yes to browse; booking in serviceable areas only | Testable: service selection and booking, partner app (separate).
- Design team: Graphic Designer roles on [foundit](https://www.foundit.in/job/graphic-designer-snabbit-bengaluru-bangalore-41709967); a Lead Product Designer (Supply Operations) post on weekday.works is attributed to another employer name, so unconfirmed. DS none found. Opportunity: customer plus worker app, city expansion.

### C8. Pronto (NEW TO PRIMARY)
- withpronto.com | quick home services | Founded 2024 (one source says 2025) | HQ moved Gurugram to Bengaluru ([Inc42](https://inc42.com/?p=538767)) | Total $58M+ (Inc42; earlier $45M) | Latest: Series B extension May 2026 | Valuation: $82.9M (Inc42) vs about $200M (press) conflict | Revenue: Not publicly disclosed | Employees 752 (Inc42).
- URL: https://www.withpronto.com/ (200; "Pronto - Trusted house help in minutes"), app-only: iOS https://apps.apple.com/in/app/id6743402816; Android "Pronto: House Help in Minutes" (package com.company.pronto per AppGoblin mirror) | Access: A, app-only, geo-limited | Free: Yes to browse | Testable: app booking flow in served cities; separate Pronto Professional partner app.
- Design team: none found (Greenhouse board slug "pronto" showed 33 jobs, none design; ownership unconfirmed). DS none found.

### C9. Supertails (UPDATED)
- supertails.com | pet care e-commerce, vet, grooming | Founded 2021 | HQ Bengaluru (Inc42; earlier Mumbai) | Total $58.44M+ | Latest: Series C, Feb 2026 | Valuation $130M | Revenue: Rs 108.26 Cr FY25 (Indian Retailer) vs Rs 33.0 Cr (Inc42) — conflict | Employees 338.
- URL: https://supertails.com/ (200; login/register markers heavy) | Access A | Free Yes | Testable: shop, PDP, cart, vet booking.
- Design team none found; DS none found.

### C10. Kuku FM (UPDATED)
- kukufm.com | audio content, audiobooks | Founded 2018 | HQ Mumbai | Total $156.8M+ | Latest: 2026-03-30 (Inc42; earlier note $85M Nov 2025 — dates differ, unresolved) | Valuation $489.97M (Inc42) | Revenue Rs 242 Cr FY25 (Angel One/SiliconIndia; Inc42 profile Rs 258.4 Cr) | Employees 1,620.
- URL: https://kukufm.com/ (200) | Access A (free content, paid subscription) | Free Limited | Testable: audio player, library, paywall.
- Design team: "Design Lead, AI-Driven Visual Design" listing on [foundit](https://www.foundit.in/job/design-lead-ai-driven-visual-design-kuku-fm-bengaluru-bangalore-38095788). DS none found.

### C11. STAGE (UPDATED, conflicts)
- stage.in | regional OTT | Founded: 2014 per Inc42 (earlier ~2019) unresolved | HQ Noida (Inc42; earlier Gurugram/Jaipur) | Total $21.46M+ | Latest: Series B $12.5M, March 2025 | Valuation $13.3M per Inc42 (low confidence) | Revenue Rs 111-112.7 Cr FY25 (Entrackr RoC; company claims Rs 135 Cr) | Employees: 47 per Inc42 (implausible; treat as unreliable).
- URL: https://www.stage.in/ (200; Play package in.stage) | Access A/B | Free Limited | Testable: browse, free content, subscription.
- Design team: none found. DS none found. Opportunity: multi-language, mobile plus web plus TV.

### C12. Seekho (UPDATED; edtech overlap)
- seekho.in | short-video learning subscription | Founded 2021 (Inc42) | HQ Gurugram | Total $39.47M+ | Latest Series B, 2025-09-03 | Valuation Not publicly disclosed | Revenue Rs 141.5 Cr FY25 operating (Pulse/Entrackr) | Employees 48 (Inc42, unreliable).
- URL: https://seekho.in/ (200; login/sign up markers; Play com.seekho.android) | Access A/B | Free Limited | Testable: course/video browse, subscription paywall.
- Design team none found; DS none found.

### C13. Pratilipi (UPDATED)
- pratilipi.com | stories and audio | Founded 2015 | HQ Bengaluru | Total $101.68M+ | Latest Series E Apr 2025 | Valuation Not publicly disclosed | Revenue Rs 82.6 Cr FY25; claims over Rs 185 Cr FY26 (self-reported) | Employees 788.
- URL: https://www.pratilipi.com/ (200) | Access A | Free Yes | Testable: reading, writer tools, subscription.
- Design team/DS none found.

### C14. CityMall (UPDATED)
- citymall.live | community commerce, small towns | Founded 2019 | HQ Gurugram | Total $158.8M+ | Latest Series D, Sept 2025 | Valuation $297.2M (Inc42) | Revenue Rs 534-551 Cr FY25 (Entrackr / Inc42) | Employees 1,760.
- URL: https://citymall.live/ (200; Play live.citymall.customer.prod) | Access A (serviceable-area gated) | Free Yes | Testable: catalog, cart, vernacular UI.
- Design team/DS none found.

### C15. Park+ (UPDATED)
- parkplus.io | parking, FASTag, car services | Founded 2019 | HQ Gurugram | Total $53.15M+ | Latest Series C, Jan 2023 | Valuation $20.7M (Inc42, low confidence) | Revenue Rs 175-179 Cr FY25 | Employees 878.
- URL: https://parkplus.io/ (200; Play com.ovunque.parkwheels) | Access A | Free Yes | Testable: app flows. Possible mobility overlap.
- Design team/DS none found.

### C16. Kapiva (NEW)
- kapiva.in | D2C Ayurveda wellness | Founded 2016 | HQ Bengaluru | Total $83.5M+ | Latest Series D, Sept 2025 | Valuation $238M (Inc42) | Revenue Rs 347.5 Cr FY25 (Inc42) | Employees 537.
- URL: https://kapiva.in/ (200; login markers) | Access A | Free Yes | Testable: shop, subscriptions, account.
- Design team/DS none found. Note: D2C storefront (less complex journey than travel/on-demand); lower priority.

### C17. IntrCity SmartBus (NEW)
- intrcity.com | intercity bus | Founded: Inc42 lists 2002 (parent group); SmartBus launch year not verified | HQ Noida | Total $46.99M+ | Latest Series D, Oct 2025 | Valuation Not publicly disclosed | Revenue Rs 33.8 Cr FY25 (Inc42, entity-level) | Employees 572.
- URL: https://www.intrcity.com/ (200; Play bus.tickets.intrcity) | Access A | Free Yes | Testable: route search, seat booking.
- Design team/DS none found. Tier-2 angle: Noida HQ.

### C18. Eloelo (NEW)
- eloelo.in (corporate page only, 3 KB; "Eloelo Group") | live social/gaming | Founded 2020 | HQ Bengaluru | Total $130.75M+ | Latest Series C, Nov 2026 (Inc42 2026-11-03/04) | Valuation $120.3M (Inc42; verify) | Revenue Rs 75.8 Cr FY25 | Employees 309.
- Product is app-only; Play package not extracted | Access A (app) | Free Yes | Design team/DS none found.

### C19. Frnd (NEW)
- frnd.app | social audio / matching | Founded 2019 | HQ Bengaluru | Total $8.5M+ | Latest Series A, Dec 2021 | Valuation $25.1M (Inc42) | Revenue Rs 197.8 Cr FY25 (Inc42) | Employees 327.
- URL: https://frnd.app/ (200; Play com.dating.for.all); careers link redirected to interact.global (possible parent/rebrand; not verified) | Access A, app-only | Design team/DS none found.

### C20. Pickyourtrail (UPDATED; borderline founding)
- pickyourtrail.com | holiday packages | Founded 2014 (Inc42; earlier ~2014) borderline pre-2015 | HQ Chennai | Total $3.0M+ | Latest Venture round, March 2022 | Valuation Not publicly disclosed | Revenue Rs 215.6 Cr FY25 (Inc42; net loss Rs 8.6 Cr per Indian Startup Times) | Employees 716.
- URL: https://pickyourtrail.com/ (200) | Access A (itinerary builder; booking consultant-assisted) | Free Yes | Design team/DS none found. Tier-2 angle: Chennai.

## Section B. Consumer, moved to SECONDARY (with reasons)

- Zostel (pre-2015): founded 2013 (Inc42), HQ Gurugram, $1M+ funding, last round 2018, 394 employees; Inc42 FY25 Rs 1.7 Cr vs group gross about Rs 200 Cr (conflict). Site 200. Reason: pre-2015.
- Furlenco (pre-2015): founded 2012 (Inc42), Bengaluru, $291.5M+, last 2025-12-02, 605 employees; revenue Rs 229-240 Cr FY25. Site 200. Reason: pre-2015.
- RentoMojo: listed 2026-09-17; founded 2014. Reason: listed, large, borderline pre-2015.
- The Souled Store (pre-2015): founded 2013, Mumbai, $29.4M+, Series C 2023, Rs 500.3 Cr FY25, 1,017 employees. Reason: pre-2015, D2C apparel.
- Bewakoof (pre-2015): founded 2012, Bengaluru (Inc42; earlier Mumbai), $49.4M+, Rs 174.7 Cr FY25. Site returned 403 to curl.
- Cashify (pre-2015): see change 2. 2,369 employees; Rs 1,120 Cr FY25 (Inc42).
- FabHotels: founded 2014, Gurugram, $67.65M+, Rs 725 Cr FY25 (Inc42), 701 employees. Reason: borderline pre-2015, overlap with other stays; DRHP filed per earlier note (IPO status not rechecked).
- Treebo: Inc42 page returned no data in my parse; site 200 (Play com.treebo.starscream). Reason: stale funding (Jun 2021 per earlier note), unverified.
- Country Delight: founded 2015, Gurugram, $210.4M+, Series E Mar 2025, 2,168 employees; revenue only FY23 Rs 800.8 Cr on Inc42. Reason: geo-gated subscription delivery, near household scale.
- DealShare: founded 2018, Bengaluru, $398.6M+, last round Feb 2022, valuation $1.71B (Inc42), Rs 523.5 Cr FY25, 1,667 employees. Site returned 403 to curl; app access not verified. Reason: unverified access, stale funding.
- GoMechanic: founded 2016, Gurugram, $68.9M+, last round Nov 2023, last revenue FY23 Rs 309.8 Cr (Inc42), 830 employees; site 200 (Play gomechanic.retail). Reason: stale financials; current status not verified.
- Servify: founded 2015, Mumbai, $137.9M+, Series D Mar 2025, Rs 360.4 Cr FY25, 525 employees; servify.com is B2B2C product-lifecycle platform. Reason: sales-led (D).
- Aisle: founded 2014 (Inc42), Bengaluru, $0.3M+ seed 2021, 56 employees, no revenue figure; Play com.aisle.app. Reason: small, pre-2015 borderline.
- Sleepy Owl: site returned 429 bot-check; Inc42 page returned no data. Not verified.
- Zolo: Inc42 page stale (seed 2016, 1,520 employee figure duplicates Zolostays); not verified.

## Section C. Other sectors, PRIMARY (22 companies)

Same field format, shortened where evidence is identical ("none found" for design team and DS means none found in this pass; see method notes).

### Edtech
**O1. Masai** — masaischool.com | coding bootcamp, income-share/outcome-based | Founded 2019 | Bengaluru | Total $22.16M+ | Series B (last round 2022-11-08) | Valuation $52.6M (Inc42) | Rs 63.8 Cr FY25 | Employees not on Inc42 | URL https://www.masaischool.com/ (200; signup/login markers) | Access A/B (free application/assessment; paid program) | Testable: program browse, application, learner portal gated | Design/DS none found.
**O2. Newton School** — newtonschool.co | coding education | 2019 | Bengaluru | $30.82M+ | Series B 2022-04-12 | valuation $135.6M (Inc42) | Rs 43.6 Cr FY25 | URL https://www.newtonschool.co/ (200) | Access A/B | Design/DS none found.
**O3. SpeakX** — speakx.ai | AI English speaking app | 2020 | Gurugram | $23.3M+ | latest round 2026-09-01 (Inc42) | Employees 67 | Play yellowclass.kids.live visible (older Yellow Class package) | Access A (app) | Design/DS none found.
**O4. PlanetSpark** — planetspark.in | live 1:1 English/public-speaking classes | 2017 | Gurugram | $31.3M+ | Series B 2024-03-10 | Rs 81.2 Cr FY25 (Inc42) | Employees 5,882 (likely includes tutors) | URL https://www.planetspark.in/ (200; "free trial" appears 14 times) | Access B (free trial class) | Testable: trial booking funnel | Design/DS none found.
**O5. Suraasa** — suraasa.com | teacher professional development | 2017 | Gurugram | $7.2M+ | Series A | Rs 15.3 Cr FY25 | Employees 136 | URL https://www.suraasa.com/ (200) | Access A | Design/DS none found.
**O6. Leverage Edu** — leverageedu.com | study abroad | 2017 | New Delhi | $73.27M+ (Inc42) | Series C $40M Jul 2023 (valuation reported about $150M, [Medial](https://medial.app/news/leverage-edu-raises-dollar40-million-at-dollar150-million-valuation-reports-e02a45ded502f)) | Revenue conflict: Rs 173 Cr (Entrackr) vs Rs 114.8 Cr (Inc42) vs >Rs 180 Cr (Entrackr other item) | Employees 1,254 | URL https://leverageedu.com/ (200; Play com.leverageedu.leverageedu) | Access A (free profile/counselling booking) | Design/DS none found.
**O7. Leap (LeapScholar, Leap Finance, GeeBee)** — joinleap.com (4.7 KB landing; Play id found in HTML belonged to an unrelated app, ignore) | study abroad group | 2019 | Bengaluru | $317.9M+ incl. debt (Inc42) | Series E $65M Jan 2025 | Rs 175.3 Cr FY24 | Employees 1,315 | Ashby board shows 20 jobs, none design/frontend titles on 2026-11-17 | Access A (app) | Multi-brand DS angle (inference).
**O8. Adda247** — adda247.com | test prep | 2016 | Gurugram | $67M+ | Series B | Rs 217.1 Cr FY25 (Inc42 article); Inc42 profile Rs 165.3 Cr FY24 (basis differs) | Employees 2,340 | URL https://www.adda247.com/ (200) | Access A (free classes/content) | Design/DS none found.

### Logistics
**O9. LetsTransport** — letstransport.in | B2B logistics | 2015 | Bengaluru | $82.64M+ | Series E, last round 2024-04-24 | valuation $45.8M (Inc42) | Rs 530 Cr FY25 (Inc42) | Employees 626 | URL https://letstransport.in/ (200; login markers) | Access D/E (customer and driver apps; web login only) | Design/DS none found.
**O10. Vahak** — vahak.in | truck/LCV booking marketplace | 2017 | Bengaluru | $19M+ | Series A | Rs 41.3 Cr FY24 | Employees 168 | URL https://www.vahak.in/ (200; login and signup markers) | Access A (free account) | Design/DS none found.

### Mobility and EV
**O11. Yulu** — yulu.bike (4 KB page, app-led) | EV bike rental | 2017 | Bengaluru | $228.15M+ | Series C, last round 2026-08-12 | valuation $222.1M (Inc42) | Rs 228.6 Cr FY25 (Inc42; Entrackr Rs 237.4 Cr) | Employees 1,157 | Access A (app: browse and unlock needs KYC/payment; verify) | Design/DS none found.
**O12. Zypp Electric** — zypp.app (Play com.zyppdelivery) | EV rental for delivery partners | 2017 | Gurugram | $62.5M+ | Series C | Rs 438-455 Cr FY25 (Entrackr / Inc42 Rs 448.6 Cr / ThePrint; bases differ) | Employees 1,190 | Access B/D (rider onboarding) | Design/DS none found.
**O13. Statiq** — statiq.in | EV charging network | 2020 | Gurugram | $43.7M+ | last round 2026-02-18 | valuation $83.6M (Inc42) | Rs 79.5 Cr FY25 | Employees 328 | URL https://www.statiq.in/ (200; Play com.statiq) | Access A (map and charger search free; charging needs payment) | careers site career.statiq.in exists; roles seen were PM/engineering plus a marketing "Designer" role; no product designer found.
**O14. ChargeZone** — chargezone.co (curl failed, 000; unresolved, retry in browser) | EV charging | 2018 | Vadodara (tier-2) | $86.11M+ | Venture round | Rs 54.8 Cr FY24 | Employees 215 | Access A (app; unverified) | Design/DS none found. Tier-2 city candidate.
**O15. Bounce (Bounce Infinity)** — bounceinfinity.com (www.bounceshare.com redirects here) | EV scooters and battery swap | 2014 (Inc42; borderline pre-2015) | Bengaluru | $238.06M+ | last round 2026-03-02 | Employees 637 | Revenue not disclosed (Inc42 FY21 Rs 7 Lakh is a tracker artefact) | Design team: Ashby lists Product Designer (published 2026-09-15) and Senior Product Designer (2026-11-12) — [Ashby Senior Product Designer](https://jobs.ashbyhq.com/Bounce/a787155b-7784-41df-9e5f-a845615a6aa7) | DS none found | Access: app/product page (Category not exercised; likely D for purchase, A for app).

### Proptech and housing
**O16. Zolostays** — zolostays.com | co-living | 2015 | Bengaluru | $98M+ | latest round (Inc42 stage Series A, stale) | Rs 342-346 Cr FY25 | Employees 1,520 | URL https://zolostays.com/ (200; Play com.zelo.customer) | Access A | Design/DS none found.
**O17. Stanza Living** — stanzaliving.com | managed student/professional housing | 2017 | New Delhi | $228.3M+ | debt financing | Rs 545.5 Cr FY25 (Ascendants summary) vs Inc42 Rs 729.8 Cr (conflict, bases differ) | Employees 1,719 | URL https://www.stanzaliving.com/ (200; Play com.stanzaliving.app) | Access A (browse and booking) | Design/DS none found.
**O18. HomeLane** — homelane.com | home interiors, design-led funnel | 2014 (Inc42; borderline) | Bengaluru | $156.86M+ | Rs 683.4 Cr (Inc42) vs Rs 748 Cr (headline in earlier note) | Employees 3,807 | URL https://www.homelane.com/ (200) | Access A (free design consultation) | Design/DS none found.

### Jobs
**O19. Apna** — apna.co | blue/grey-collar jobs | 2019 | Bengaluru | $193.45M+ | Series C Sept 2021 at $1.1B valuation | Rs 144.1 Cr FY25 | Employees 1,728 | URL https://apna.co/ (200; login and "search jobs" markers) | Access A | Design team: Senior Product Designer listing that includes architecting a design system on [startup.jobs](https://startup.jobs/senior-product-designer-apna-9957709) (aggregator; strongest DS-hire signal among other sectors) | Caveat: well known in India; coordinator to judge "household name".
**O20. WorkIndia** — workindia.in | blue-collar jobs | 2015 | Bengaluru | $34.16M+ | latest round 2025-12-18 | valuation $76.9M (Inc42) | Rs 80 Cr FY25 | Employees 1,096 | URL https://www.workindia.in/ (200; register/login markers) | Access A | Design/DS none found.

### Agritech and B2B marketplace
**O21. BigHaat** — bighaat.com | agri inputs marketplace | 2015 | Bengaluru | $23.78M+ (Inc42) | Series C | Revenue conflict: Rs 27.1 Cr (Inc42 entity) vs >Rs 1,100 Cr (Entrackr exclusive, likely GMV/consolidated) | Employees 287 | URL https://www.bighaat.com/ (200; Play com.BigHaat) | Access A | Design/DS none found. DeHaat parent is pre-2015 (see secondary).
**O22. Moglix** — moglix.com | industrial B2B marketplace | 2015 | Noida | $481.5M+ | Rs 4,232 Cr FY24 (Inc42) | Employees 1,459 | URL https://www.moglix.com/ (200; Play com.moglix.online; login markers) | Access A (public catalogue browse; business account) | Design/DS none found.

Tier-2 coverage: ChargeZone (Vadodara) only. No Jaipur, Indore, Kochi, Bhubaneswar or Lucknow company was verified in this pass; Noida (IntrCity, Stage per Inc42) and Chennai (Pickyourtrail) are secondary metros.

## Section D. Other sectors, moved to SECONDARY (with reasons)

- Testbook (2013, Mumbai): pre-2015; owned by Classplus (overlap with SaaS researcher). Rs 136.7 Cr FY24, 3,803 employees. Site 200.
- Oliveboard (founded 2012, Bengaluru): pre-2015; $3.09M, Rs 22.7 Cr FY25, 182 employees; Play in.oliveboard.prep.
- Cuemath (2013, Bengaluru): pre-2015; $121.5M+, Rs 155.4 Cr FY25, 2,760 employees.
- Shadowfax: listed 2026-01-28 (see change 3).
- Square Yards (Inc42 2014, Gurugram): pre-2015/borderline, 9,625 employees, Rs 300.7 Cr FY24 (Inc42) vs Rs 1,400 Cr FY25 (Entrackr; basis differs); large, partly sales-led.
- AgroStar (2013, Pune): pre-2015; Rs 865.5 Cr FY25 (Inc42), 3,082 employees. DeHaat (2012, Gurugram): pre-2015; Series (pre) Aug 2026, $251.2M+, Rs 2,647.6 Cr FY24 (Inc42); profit/loss conflict from earlier note remains unresolved.
- Vakilsearch (2010, Chennai) and IndiaFilings (2013, Chennai): pre-2015; Inc42 revenue data unusable (Vakilsearch Rs 24 Lakh FY24 artefact); both sites live with register/login markers; legaltech candidates remain thin.
- OfBusiness (2015, Gurugram): Category D sales-led; $890M+, Rs 14,735 Cr FY25 (Inc42), 1,178 employees on tracker.
- Jumbotail (2015, Bengaluru): B2B grocery marketplace, $287.8M+, Series D, Rs 103.8 Cr FY25 (Inc42; earlier note Rs 914 Cr FY24 secondary, conflict); public site is a 54 KB marketing page, app access unverified; Category D/E.
- Zypp/Bounce/Yulu stay primary despite tier-D purchase flows because the rider apps are free to install.

## Inferences

- Highest-confidence active design-hiring signals: Atlys, Bounce (Ashby boards read directly, dates in 2026), Scapia, Headout, Apna (aggregator listings). These are the best first-wave outreach.
- Pronto and Snabbit are app-only and geo-gated; testing requires being in a served city, so they rank lower for hands-on audit.
- Inc42 employee counts conflict with revenue or traffic for Stage, Seekho and Snabbit revenue; treat those as unreliable.

## Gaps

- Not done: signup/OTP completion for any company; GitHub org and Storybook checks (GitHub blocked, 403); Dribbble/Medium design blogs; Keka/Darwinbox/Instahyre scans; official careers pages (JS rendered); entrackr.com company pages (entrackr.com/companies/* returned 404; article URLs unchecked in this pass).
- Unresolved conflicts: Headout HQ and founding year; Stage founding year/HQ/employees; Snabbit HQ and valuation; Pronto valuation; Supertails revenue basis; Leverage Edu revenue; Cashify total funding; BigHaat revenue; DeHaat profit/loss; Kuku FM latest round date.
- Not found: tier-2 city companies (Jaipur, Indore, Kochi, Bhubaneswar, Lucknow); working domain for ChargeZone (curl 000); Eloelo product URL beyond corporate page; Sleepy Owl data (bot-block); Treebo Inc42 data.
- Search snippets from WebSearch summaries were used only as pointers to listings; one summary incorrectly called Scapia bootstrapped, contradicted by Inc42 funding $134.8M+.
