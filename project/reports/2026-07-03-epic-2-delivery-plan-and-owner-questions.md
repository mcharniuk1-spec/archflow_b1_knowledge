# Epic 2 Delivery Plan And Owner Questions

Date: 2026-07-03
Status: Planning task prepared; execution not started
Scope: E2 Research Engine To ICP

## Executive Goal

Epic 2 converts the PRD Pack hypothesis into a source-graded market evidence engine before outreach, positioning upgrades, or demand claims.

The first goal is not to browse widely. The first goal is to define approved sources, data types, agent roles, scoring, competitor comparison, audience analysis, and owner decisions so real account research can proceed without contaminating the public repo or overstating evidence.

## Current Starting Point

FACT:

- E2.0A is accepted.
- Primary ICP hypothesis is B2B SaaS product teams, Series B-D, 50-500 employees, 2-5 PMs, Director/VP Product owner.
- First offer hypothesis is the Product Discovery-to-Production PRD Pack.
- Approved source types are public company websites, public jobs, public reviews, public directories/lists, authorized LinkedIn summaries, approved search queries, and the internal approved corpus.
- Gated tools remain gated: Tavily, Exa, SerpAPI, Firecrawl, Apify, Playwright/browserless, Clay, Apollo, Cognism, Clearbit, People Data Labs.

GAP:

- No account universe has been built.
- No account evidence cards have real public signals.
- ICP trigger, budget path, workaround, and role currentness are still hypotheses.
- No 10-15 verified E6 outreach target set exists.

## E2 Stage Plan

| Stage | Output | Owner agents | Data/source types | Review gate |
|---|---|---|---|---|
| E2.1 | Approved source list and segment data model | AF Tools, AF Research | Directories, company sites, job pages, internal corpus | Source boundary approval |
| E2.2 | Competitor map and public pain evidence cards | AF Research | Competitor sites, pricing pages, reviews, public jobs, public case studies | A-D source grade |
| E2.3 | One-page ICP card | AF Research, AF Review | Reviewed account cards and pain map | FACT/HYPOTHESIS/GAP split |
| E2.4 | Primary ICP plus later-lane split | AF Manager, AF Review | Segment scoring and exclusions | No ICP drift |
| E2.5 | 10-15 verified targets for E6 | AF Tools, AF Copy, AF Review | Company/domain/role-title records, no private personal data in public repo | Two B+ signals and role-currentness gate |

## Data Types To Collect

| Data type | Source | Public repo handling |
|---|---|---|
| Company domain and name | Public directory/company site | Allowed |
| Segment and size estimate | Public directory/company site/careers page | Allowed with source grade |
| Product org signal | Careers page, public job post | Allowed, dated |
| PRD/discovery/handoff pain | Public review, blog, case study, job text | Summary only |
| Current tools/workarounds | Public tech/integration pages, reviews | Summary only |
| Buyer role title | Public leadership/team/careers pages or authorized LinkedIn summary | Role title only; no personal lead data by default |
| Social language | Public social posts | HYPOTHESIS only |
| Contact details | Gated enrichment/manual owner-approved workflow | Do not store in public repo |

## Competitor Analysis Plan

Initial comparison set:

- Productboard, Aha!, Dovetail, Zeda, BuildBetter, Fibery, Cycle, ChatPRD, Notion AI, Glean, Dust.

Compare on:

| Field | Why it matters |
|---|---|
| Buyer and job | Shows whether they sell to the same owner |
| Artifact output | PRD, roadmap, insight repository, backlog, decision log |
| Evidence model | Whether claims are source-backed or AI-generated |
| Workflow integration | Jira, Linear, Notion, Productboard, Slack, docs |
| AI boundary | Where AI is used and what is reviewed |
| Pricing/CTA | Buying motion and budget proxy |
| Trust/privacy | Core objection for product-team source material |
| ArchFlow opportunity | The gap ArchFlow can own |

## Audience Analysis Plan

Analyze audience through four lenses:

| Lens | Evidence | Output |
|---|---|---|
| Account shape | size, stage, product team size, market | segment fit |
| Trigger | hiring, funding, launch, research/rework language | timing score |
| Pain | PRD rework, discovery overload, handoff loss, roadmap ambiguity | pain type |
| Buying path | role owner, budget proxy, current workflow | outreach readiness |

## Tools And Sources

Use now:

- repo-local E2.0A schema and rubric;
- public company sites;
- public career pages and job boards;
- public review sites summarized only;
- public directories/lists;
- authorized LinkedIn summaries;
- manual approved search queries;
- dashboard/run packets after Codex review.

Use later only with approval:

- search APIs, crawlers, browser automation, enrichment vendors, provider-backed synthesis, live Notion/GitHub/TG writeback, and any personal-contact dataset.

## Owner Questions Before Execution

1. Should E2.1 use live public web/search research now, or stay local-plan-only?
2. Which first source universe is approved: SaaS directories, funding lists, job boards, Product Hunt-style launch lists, or another list?
3. Is authorized LinkedIn summary allowed for role-title currentness in this run?
4. Should the first universe use 50-500 employees broadly or tighten to 100-300?
5. What is the minimum evidence threshold for E6 handoff: score, two B+ signals, owner judgment, or all three?
6. Should E3 diagnostic/analytics be finished before E4 social profile publication?
7. Are any regions, industries, or account types excluded for the first pass?
8. Is provider-backed summarization allowed after public-source collection, or must the first pass be deterministic/local only?

## Planning Task Question Analysis

The E2 Notion task named `Planning` should contain both the questions and the analysis below. The default is conservative: do only public-source, public-safe, source-graded research until the owner explicitly approves live search, enrichment, provider-backed synthesis, or personal-contact handling.

| Question | Why it matters | Default if unanswered | Risk if skipped |
|---|---|---|---|
| Live public web/search now or local-plan-only? | Decides whether E2 starts evidence collection or stays a method package | Local-plan-only plus approved source list | Accidental unbounded browsing or weak provenance |
| First source universe | Determines where accounts come from and what bias the sample has | SaaS directories plus public careers pages | Random account list with inconsistent fit |
| LinkedIn role-title currentness | Helps confirm buyer role without storing personal lead data | Authorized summaries only, role/title only | Stale or unverifiable buyer-owner assumptions |
| 50-500 vs 100-300 employees | Controls segment breadth and product-team maturity | Keep 50-500, tag sub-segments | Overfitting too early or noisy ICP |
| Evidence threshold for E6 | Prevents outreach based on weak signals | Require two independent B-or-better signals plus owner judgment | Low-quality outreach list |
| E3 before E4 publication | Decides whether positioning and diagnostic should precede content | Finish E3 diagnostic/analytics before heavy publication | Content drives attention without conversion path |
| Exclusions | Prevents wasted research in bad-fit markets | Exclude regulated/high-security accounts until trust model matures | Privacy/security objections dominate too early |
| Provider summarization | Controls cost, privacy, and traceability | Deterministic/local first, provider only on sanitized digests after approval | Unlogged model use or contaminated source boundaries |

## Agent Distribution For Epic 2

| Agent role | Responsibility | Required output |
|---|---|---|
| Source Boundary Agent | Define allowed public sources, forbidden data, and source-grade rubric | E2.1 source boundary packet |
| Universe Builder | Build the first company universe from approved public lists | Account universe table with source dates |
| Competitor Analyst | Compare alternatives and positioning gaps | Competitor comparison matrix |
| Audience Analyst | Score account shape, trigger, pain, and buying path | ICP signal cards |
| Evidence QA Agent | Grade provenance and separate fact/hypothesis/gap | Evidence-card audit notes |
| Offer Strategist | Translate evidence into PRD Pack offer, objections, and CTA | ICP card and offer hypothesis |
| Outreach Gatekeeper | Prepare E6 handoff only after evidence threshold passes | 10-15 reviewed target candidates, no personal-contact dump |

## Competitor And Market Analysis Method

Use direct, dated public evidence first. Each competitor row should include the buyer, artifact workflow, AI/review boundary, integrations, pricing/CTA, proof assets, privacy/trust posture, and ArchFlow gap.

Compare competitors in three groups:

| Group | Examples | What to learn |
|---|---|---|
| Product management suites | Productboard, Aha!, Zeda, Cycle | Existing budget category and integration expectations |
| Research/insight tools | Dovetail, BuildBetter, Notion AI, Glean | Evidence handling, synthesis claims, trust posture |
| AI artifact/workflow tools | ChatPRD, Dust, Fibery, internal AI assistants | Speed expectations and AI-review objections |

## Market And Audience Analysis Sources

| Source type | Use | Handling rule |
|---|---|---|
| Company sites | Segment, product category, positioning, workflow hints | Summaries with dated URLs |
| Careers pages and public jobs | Product-team maturity, tooling, pain language | Job text summarized, no raw dumps |
| Review sites | Pain/workaround language | Short summaries only |
| Public pricing/CTA pages | Budget and buying motion proxy | Dated capture and interpretation |
| Public directories/lists | Universe construction | Keep list provenance and inclusion rule |
| Authorized LinkedIn summaries | Role-title currentness | Role/title only by default |
| Internal approved corpus | Offer and method alignment | Public-safe derived summaries |

## Epic 2 Execution Gate

E2 execution should start only after the `Planning` task records:

- approved source universe;
- allowed/disallowed data types;
- first segment boundaries;
- evidence threshold for E6 handoff;
- provider/use-of-search decision;
- excluded account classes;
- reviewer who can approve source cards.

## Acceptance Criteria

- E2.1 source list and segment model are approved before collection.
- E2.2 evidence cards include provenance, grade, signal count, pain type, risk note, and next action.
- Shortlisted accounts have at least two independent B-or-better signals.
- E2.3 ICP card separates FACT, HYPOTHESIS, and GAP.
- E2.4 keeps later audiences separate.
- E2.5 hands E6 a reviewed 10-15 target set with no public overclaiming.
- Public safety scan passes before any repo-stored research packet is complete.

## Notion Task Packet

Create or update the E2 Notion task page named `Planning` with this plan, then add the owner questions as the first execution checklist. Do not flip E2 tasks to Done. E2 should move from Backlog/To Do to Review/In Progress only after the owner answers the source and execution questions.
