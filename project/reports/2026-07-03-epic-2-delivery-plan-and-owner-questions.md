# Epic 2 Delivery Plan And Owner Questions

Date: 2026-07-03
Status: plan complete, execution not started
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

## Acceptance Criteria

- E2.1 source list and segment model are approved before collection.
- E2.2 evidence cards include provenance, grade, signal count, pain type, risk note, and next action.
- Shortlisted accounts have at least two independent B-or-better signals.
- E2.3 ICP card separates FACT, HYPOTHESIS, and GAP.
- E2.4 keeps later audiences separate.
- E2.5 hands E6 a reviewed 10-15 target set with no public overclaiming.
- Public safety scan passes before any repo-stored research packet is complete.

## Notion Task Packet

Create or update the E2 Notion task page with this plan, then add the owner questions as the first execution checklist. Do not flip E2 tasks to Done. E2 should move from Backlog/To Do to Review/In Progress only after the owner answers the source and execution questions.
