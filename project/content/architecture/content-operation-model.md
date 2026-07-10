# Content Operation Model

Status: preparation-only architecture
Date: 2026-07-10

## Positioning Anchor

The intended audience is B2B SaaS product leadership responsible for discovery quality, PRD clarity, and delivery handoff. The content must describe ArchFlow as a Product Discovery-to-Production PRD Pack: approved material becomes a labeled context digest, reviewed PRD/ICP evidence, acceptance criteria, task handoff, and decision-memory candidate. It must not promise autonomous delivery, generic AI transformation, live product access, customer outcomes, or ROI.

## Controlled Flow

| Stage and role | Bounded inputs | Required output | Stop condition | Human gate |
|---|---|---|---|---|
| 1. News and trend intake analyst | Official AI/product/company blogs, changelogs, docs, pricing pages, and a manually observed public format | Dated source record: URL, source category, theme, summary, evidence grade, and claim label | The source is private, non-public, untraceable, or the summary would retain personal/account data | Content owner accepts source record |
| 2. Competitor content analyzer | Public company positioning and official product material; category map | Alternative category, public URL, observed message, objection hypothesis, and evidence gap | The work needs account scraping, engagement graphs, or a demand/market-share claim | AF Review checks the comparison |
| 3. Planner bot | Accepted source records, run handouts, approved templates, and service positioning | Topic score, audience pain, format, evidence path, claim label, CTA, and review status | Topic score is below 8/12, evidence is missing, or risk is unsafe | Content owner selects candidates |
| 4. Writer/editor bot | Accepted planner item and evidence summary | LinkedIn-first company-voice draft, short X/Threads adaptation, claim table, and edit checklist | Draft adds an unsupported claim or a CTA that implies a live service or proof | AF Review approves draft readiness |
| 5. Design/mockup bot | Approved draft, visual specification, and artifact summary | Static post, carousel, cover, or script specification; no rendered private material | A visual needs a screenshot, customer logo, private text, fake dashboard, or personal/account data | Content owner approves mockup direction |
| 6. QA and publishing-preparation gate | Draft, claim table, source register, mockup spec, and checklist | Pass, revise, or blocked review packet with named gaps | Any safety, provenance, accessibility, claim, or platform-readiness check fails | AF Review plus owner approval |
| 7. Publishing-preparation queue | Only a passed review packet | A manual-ready package with caption, visual spec, CTA, and owner decision field | Any request would post, schedule, upload, or access an account | Owner performs any external action separately |
| 8. Feedback loop | Owner-provided aggregate outcome summary only | Report-only learning note and next-topic hypothesis | The data contains account-level, personal, private, or unapproved information | Content owner reviews learning note |

## Planner Scoring

Use the existing content-planner rubric. Admit an item only when it scores at least 8/12 across ICP fit, pain relevance, source strength, differentiation, CTA fit, and safety risk, with no unsafe flag. A candidate must identify a repo-relative evidence path and one of `FACT`, `INTERPRETATION`, `HYPOTHESIS`, or `GAP`.

## Drafting And Design Rules

- LinkedIn is the primary draft. X and Threads versions only shorten the approved core claim; they introduce no new claim.
- A short-video concept is a script and cover specification only. It always has a static companion and passes the same review gates.
- Use source-lineage, review-gate, acceptance-criteria, task-handoff, and decision-memory language. Avoid generic productivity, disruption, or AI-agency slogans.
- A CTA may invite a review of a source packet, readiness diagnostic, or scoped PRD Pack discussion. It cannot imply an active provider, automation, production integration, customer proof, or commercial result.

## Required QA Verdict

Every candidate must be marked `pass`, `revise`, or `blocked` against: source traceability, claim label, positioning fit, public safety, visual accessibility, CTA safety, and platform readiness. A missing source or gate is a `blocked` result, not a reason to improvise.
