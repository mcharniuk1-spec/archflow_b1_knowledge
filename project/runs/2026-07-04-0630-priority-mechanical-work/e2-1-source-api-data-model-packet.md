# E2.1 Source/API/Data Model Packet

Date: 2026-07-04
Status: prepared for review
Basis: accepted E2.0A dry-run packet and `project/workflows/market-research-engine.yaml`

## Purpose

This packet turns the accepted E2.0A source boundary into an E2.1-ready operating artifact. It defines the approved public source classes, the gated API/tool classes, the segment data model, and the fact-check route for the first ICP research pass.

No live research, provider call, crawler, lead-enrichment tool, external write, Notion update, outreach, or profile publication happened in this run.

## Selected Source Classes

| Source class | Status | Allowed use | Required fields | Notes |
|---|---|---|---|---|
| Company website | allowed now | First-party product, pricing, use-case, integration, blog, and security evidence | domain, URL, observed date, page type, short summary, grade | Grade A when current and directly attributable. |
| Company careers page | allowed now | Hiring signal and team-growth proxy | domain, URL, role title, function, observed date, summary, grade | Grade A when official and current. |
| Public job board posting | allowed now | Hiring signal when company source is absent or corroborated | source, company, URL, role title, observed date, summary, grade | Grade B or C depending currentness and attribution. |
| Public review site | allowed now | Pain-language and workflow-friction evidence | source, product/category, URL, observed date, summary, grade | Summaries only; no raw review dumps. |
| Public directory or market list | allowed now | Account-universe seed only | source, URL, observed date, segment label, inclusion reason, grade | Does not validate pain by itself. |
| Authorized LinkedIn view | allowed with summary only | Role-map and company/currentness hypothesis | role title, company, observed date, summary, verification status | No raw profile text or private identifiers in public repo. |
| Public social signal | hypothesis only | Language mining and monitoring | source type, observed date, summary, hypothesis, grade | Capped at D unless independently corroborated. |
| Internal approved corpus | allowed now | Method, template, and project-state reference | repo-relative path, summary, rule inherited | Does not create external market proof. |

## Gated Tool/API Classes

| Tool/API class | Gate | Safe current action |
|---|---|---|
| Search APIs such as Tavily, Exa, SerpAPI, and Google Custom Search | Requires legal, storage, rate-limit, source-boundary, budget, and AF Review approval | Prepare query templates only. |
| Crawlers and browser automation such as Firecrawl, Apify, Playwright, and Browserless | Requires approval before collection and storage | Prepare page-type rules only. |
| Enrichment vendors such as Clay, Apollo, Cognism, Clearbit, and People Data Labs | Requires explicit approval and private-data handling plan | Exclude from public run artifacts. |
| Provider model calls | Requires approved runtime, budget ledger, sanitized input, and review gate | Keep model output out of evidence grading. |
| Notion/GitHub/external writeback | Requires approved connector/write path and owner-safe payload | Prepare payload text only. |

## Segment Data Model

| Field | Type | Rule |
|---|---|---|
| segment_id | enum | `b2b_saas_product_teams` for the first lane. |
| account_shape | string | Series B-D B2B SaaS, 50-500 employees, 2-5 PMs remains the working hypothesis. |
| company_domain | string | Stable domain, public website only. |
| company_name | string | Public company name only. |
| employee_band | enum | `50_100`, `101_300`, `301_500`, `unknown`; mark `unknown` when not first-party or current. |
| product_team_signal | enum | `explicit_product_roles`, `product_ops`, `pm_hiring`, `unclear`. |
| trigger_event | enum | `funding`, `pm_team_growth`, `launch`, `reorg`, `migration`, `unknown`. |
| pain_signal | enum | `customer_research_overload`, `prd_rework`, `roadmap_ambiguity`, `handoff_loss`, `decision_memory_gap`, `unknown`. |
| source_count | integer | Number of independent signals. |
| best_grade | enum | Highest source grade among evidence signals. |
| evidence_status | enum | `hypothesis`, `candidate`, `review_ready`, `blocked`. |
| next_action | enum | `exclude`, `monitor`, `enrich`, `verify_people`, `draft_outreach`, `interview`. |

## Evidence Promotion Rules

FACT:
- E2.1 can define source rules and data shape without collecting accounts.
- E2.2 must create evidence cards before market claims, outreach claims, or ICP confidence upgrades.

INTERPRETATION:
- The first useful E2.1 output is not a scraped list. It is a reproducible source and field contract that prevents later account cards from mixing evidence, hypotheses, and private data.

GAP:
- Real account cards, live role verification, search API use, crawler use, enrichment use, outreach drafts, and demand claims remain blocked until separately approved or explicitly started in a safe public-source run.

## E2.2 Readiness Checklist

- Confirm E2.1 packet acceptance.
- Choose one or two public directory seeds.
- Define query templates without executing gated APIs.
- Create a blank account-card table using the accepted schema.
- Require at least two independent source signals before `draft_outreach`.
- Route any scored shortlist through AF Review before E6 handoff.
