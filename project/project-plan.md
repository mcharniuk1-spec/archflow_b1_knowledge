# Project Plan

Source: private project board reviewed on 2026-06-25.

This file is an English public-safe translation and synthesis. It does not include private page URLs, user IDs, owner names, or raw source content.

Latest detailed E1 breakdown: [`reports/2026-06-25-e1-block1-subtask-execution-plan.pdf`](reports/2026-06-25-e1-block1-subtask-execution-plan.pdf).

Latest tool and market integration plan: [`reports/2026-06-29-tool-and-market-integration-plan.md`](reports/2026-06-29-tool-and-market-integration-plan.md).

## Epic Timeline

| Epic | Public English Name | Status | Window |
|---|---|---|---|
| E1 | Build the knowledge base on ourselves | Active | 2026-06-24 to 2026-07-04 |
| E5 | Analytics and ROI method | Active | 2026-06-24 to 2026-07-07 |
| E4 | Content | Active | 2026-06-24 to 2026-08-01 |
| E3 | Website and positioning | Not started | 2026-07-01 to 2026-07-14 |
| E2 | Research engine to ICP | Planning | 2026-07-01 to 2026-07-11 |
| E6 | Outreach | Not started | 2026-07-14 to 2026-07-28 |
| E7 | Payment test to verdict | Not started | 2026-07-15 to 2026-08-01 |

## Current Execution Logic

1. Prove the knowledge-base and PRD workflow internally.
2. Turn internal proof into a repeatable method.
3. Use the method to research the first ICP.
4. Build positioning, a solution page, a diagnostic form, and analytics.
5. Publish content that documents the build and routes demand to the site.
6. Run direct outreach to a small target list.
7. Judge demand by payment or firm paid intent, not attention.

## June 29 Integration Update

The June 29 tool and market reports do not replace the E1-E7 path. They make it more explicit:

- Loop Engineering becomes the operating contract for state, attempt caps, budgets, maker/checker separation, stop conditions, and report-only loops.
- WikiLLM stays the canonical curated memory. Cognee is only a future recall and knowledge-graph sandbox after E1.3 readback passes.
- LlamaIndex stays the retrieval abstraction. turbovec is only a future local vector-store pilot after stable source IDs, chunk metadata, and embeddings exist.
- Ollama remains the current local model path for minor/background work with Qwythos and `gemma4:e4b` fallback.
- Mistral models are optional future quality-pass models for sanitized PRDs, research synthesis, and final text after credentials, budget, model metadata logging, and AF Review gates exist.
- E2 becomes a B2B evidence engine, not a loose browsing task: universe builder, signal collector, social-language miner, review miner, company parser, ICP scorer, and fact-check gate.

FACT: The first ICP hypothesis is one vertical: product teams inside B2B SaaS scaleups, especially Series B-D companies with 50-500 employees, 2-5 PMs, and a Director or VP of Product accountable for PRD quality and speed.

INTERPRETATION: The positioning should move from a general AI-native agency/service story to a specific product-team workflow: raw product material becomes a production-ready PRD through a connected knowledge-base and multi-agent execution/review loop.

HYPOTHESIS: The first paid entry offer should be a Product Discovery-to-Production PRD Pack: product-team dialogues, customer research, interviews, notes, and docs become a reviewed context digest, production-ready PRD, backlog, acceptance criteria, decision log, and KB/update handoff in days, not weeks.

GAP: Directory counts, job counts, social posts, named company samples, and internal proof are research signals only. Demand is not validated until a real buyer risks time, source material, authority, or money.

## E1 - Build The Knowledge Base On Ourselves

Goal: prove the internal knowledge-base and PRD operating method for the Product Discovery-to-Production PRD Pack before market validation. E1 turns approved product-team/project material into source inventory, context digest, PRD, task matrix, acceptance criteria, decision log, KB update, review gate, and agent handoff.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E1.1 Set up a separate KB project from scratch | Done | Docs | 2026-06-26 | Working KB workspace and structure. |
| E1.2 Run cycle: dialogue to summary to PRD | Review | Docs | 2026-06-28 | PRD, streaming report, system report, task matrix, KB update, review report, and PDFs from the first reproducible proof. |
| E1.2.8 Run testmeeting.md PRD/PDF comparison: Codex local vs OpenRouter | Review | Docs | 2026-07-04 | Local/Codex PRD/PDF package exists from private root `testmeeting.md` and discovery-methodology input; final local baseline rerun completed on 2026-07-03 with provider disabled; sanitized OpenRouter comparison exists as review-gated evidence. |
| E1.3 Record the PRD and agent history in the KB | Review | Docs | 2026-06-30 | Public-safe KB writeback, source registry, and readback proof. |
| E1.4 Write the KB update principle | Accepted | Docs | 2026-07-03 | Accepted KB update principle with promotion test, layer table, WikiLLM writing rules, provenance rules, dashboard-packet gate, and traceback procedure. |
| E1.5 Document the process for case study and content | Review | Docs | 2026-07-04 | Public-reporting gate, GloomyLord brief, content templates, and Jarvis dashboard shell documented; publication remains owner/AF Review gated. |
| E1.6 Set up role-split KB: primary operator + collaborator | Review | Docs | 2026-07-04 | Public-safe split exists under `project/knowledge/`; private vault/Obsidian wiring remains outside the public repo. |
| E1.7 Make hosted dashboard, Jarvis, API, and agentic system work without local runtime | Review / provider-disabled runtime verified | Runtime | After E1.5 owner acceptance and E1.6 KB split decision | Railway `jarvis-api` deployed from `services/jarvis-api`; hosted `/health`, CORS, chat, role config, PRD/ICP, agent-orchestra, and voice-safe text routes passed with provider calls and writeback at zero. |

E1.1 through E1.3 now have a finer staged sequence:

1. E1.1 setup order: Git safety, env/config, Ollama, LangSmith, LangGraph, Pydantic/YAML validation, LlamaIndex, CrewAI, observability/provenance.
2. E1.2 proof order: source packet, source inventory, context digest, PRD, responsibility matrix, provenance log, review gate.
3. E1.2.8 comparison rule: do not claim a testmeeting PRD/PDF run until the fixture exists and provider/local-run gates pass.
4. E1.3 KB order: approved PRD write, agent history, source registry, retrieval metadata, loop state, readback test, memory candidates, E1.4/E2 handoff.
5. E1.3 loop rule: keep the loop at L1 report-only until readback proves the KB can answer current mission, next step, forbidden actions, existing outputs, and open gaps from memory.
6. E1.7 runtime rule: hosted dashboard/Jarvis/API work must remain provider-disabled first. The first Railway baseline now passes hosted `/health`, CORS, budget-guarded review packets, and dashboard API-base routing controls. Provider activation, auth hardening, persistence, and writeback remain separate approvals.

E1.3 review update on 2026-06-30:

| Subtask | Status | Evidence |
|---|---|---|
| Approved PRD writeback | Review | `project/runs/E1.3/2026-06-30-kb-readback/kb-writeback-report.md` |
| Agent history writeback | Review | `project/runs/E1.3/2026-06-30-kb-readback/kb-writeback-report.md` |
| Source registry and retrieval metadata | Review | `project/runs/E1.3/2026-06-30-kb-readback/source-registry.md` |
| Readback assertions | Review | `project/runs/E1.3/2026-06-30-kb-readback/kb-readback-report.md` |
| Dashboard E1.3 status | Review | `project/dashboard/data.json` generated from run evidence |
| Dashboard/voice/hosting plan | Review | static Vercel dashboard first, Railway and voice writes gated |
| Jarvis dashboard shell | In Progress | `project/dashboard/` supports normal/interview mode, browser-local packets, and in-page refresh |
| GloomyLord reporting package | In Progress | starts under E1.5 public-reporting gate and `project/content/templates/` |
| Testmeeting/OpenRouter PRD comparison | Review / provider comparison review-gated | `project/runs/E1.2/2026-07-02-testmeeting-local/`; local PRD/PDF package exists, final provider-disabled baseline rerun completed on 2026-07-03, and the sanitized OpenRouter comparison remains separate review-gated evidence |
| Hosted Jarvis/API runtime without local machine | Review / provider-disabled runtime verified | E1.7 Railway hosted API deployed from `services/jarvis-api`; health, CORS, chat, role config, PRD/ICP, agent-orchestra, and voice-safe text routes passed; provider activation, auth, persistence, and writeback remain gated |

E1.3 review caveat: E1.2 remains in Review until owner acceptance. The E1.3 readback proof can pass without marking E1.2 Done.

## E5 - Analytics And ROI Method

Goal: create operational discipline, lead funnel metrics, qualification, and ROI logic.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E5.1 Daily operational log template and habit | Done | Ops | 2026-06-27 | Daily log template and habit from day one. |
| E5.2 Lead funnel with metrics | Backlog | Ops | 2026-07-04 | Funnel from visit to form to lead to conversation to payment. |
| E5.3 Inbound project qualification scoring | Backlog | Ops | 2026-07-06 | Qualification checklist for real demand versus audience interest. |
| E5.4 ROI calculation method | Backlog | Ops | 2026-07-07 | ROI template based on saved time, labor cost, current tool cost, and service cost. |

E5 demand-quality update:

1. Track source-packet willingness, paid diagnostic interest, price/scope/privacy questions, proposal requests, budget-owner referrals, and existing-tool integration questions.
2. ROI should estimate PM/BA hours saved, meetings avoided, rework reduced, proposal approval speed, and sprint-readiness improvement.

## E4 - Content

Goal: document the build in a way that creates demand and separates attention from buying intent.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| Package social profiles for LinkedIn, X, and Threads | In Progress | Ops | 2026-06-28 | Profiles prepared for content launch. |
| Package social profiles for LinkedIn, X, and Threads, operator-side | To Do | Ops | 2026-06-28 | Operator-specific profile setup tasks completed. |
| E4.1 Five-week content plan | In Progress | Ops | 2026-07-01 | Content calendar by week and platform. |
| E4.5 Weekly review of what worked | To Do | Ops | 2026-07-03 and weekly | Weekly note separating attention from demand. |

E4 content update:

1. Prioritize category education and proof over founder-build narration.
2. Content angles: messy-source transformations, product discovery cleanup, PRD quality checklist, job-post signal breakdowns, why meeting assistants stop too early, and how review gates protect AI-assisted work.
3. Weekly review must separate content attention from demand signals such as source-packet willingness, paid diagnostic interest, proposal requests, and budget-owner referrals.

## E2 - Research Engine To ICP

Goal: convert the KB method into market research and define a specific first ICP.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E2.0 Reset research engine for integrated API/tool approach | Backlog | Research | 2026-07-02 | Tool/API plan, source boundaries, extraction schema, and loop-readiness gate for market research. |
| E2.1 Define sources, APIs, and connectable data | Backlog | Research | 2026-07-04 | Source list, allowed acquisition methods, corpus boundaries, and segment data model. |
| E2.2 Competitor, job-signal, company, social-language, and pain research for PRD segment | Backlog | Research | 2026-07-06 | Competitor positioning, public pain summary, account evidence-card schema, and dashboard plan for monitoring research/workflow evidence. |
| E2.3 Synthesize customer profile and ICP | To Do | Research | 2026-07-08 | One-page product-team ICP card for B2B SaaS Series B-D outreach, with later-lane notes kept separate. |
| E2.4 Split solution by sub-audiences | Backlog | Research | 2026-07-09 | Main ICP plus future audience notes. |
| E2.5 Build 10 to 15 verified targets for outreach | Backlog | Research | 2026-07-11 | Outreach target table with source grade, role verification status, pain hypothesis, and message angle handed to E6. |

E2.0 adds the required reset to a full integrated research/tool approach:

1. Start with a single ICP hypothesis and exclusion rules: product teams inside B2B SaaS scaleups first; agencies, AI consultancies, founder-led B2B startups, market-research teams, and enterprise product ops are later lanes unless a warm proof opportunity appears.
2. Define allowed acquisition methods before collection: public directories, company websites, job pages, authorized LinkedIn/company views, reviews, product launches, and approved search APIs.
3. Treat Tavily, Exa, SerpAPI, Google Custom Search, Firecrawl, Apify, Playwright, Browserless, Clay, Apollo, Cognism, Clearbit, and People Data Labs as gated tools. Use them only when legal, source boundaries, storage rules, and rate limits are clear.
4. Use public social signals for language and hypotheses only. Do not treat LinkedIn/X/Reddit/Product Hunt posts as proof without triangulation.
5. Create account-level evidence cards before outreach. Every card needs source URLs/dates, source grade, pain type, offer fit, role map status, risk, and next action.

E2.2 now includes dashboard planning and market-evidence workflow as supporting operating tasks:

1. E2.2.1 dashboard plan and local operator UI review: keep Phase 1 surfaces as Codex, GitHub, LangSmith, Obsidian, and WikiLLM; use the Phase 2 local dashboard for read-only monitoring; defer a full control panel until one full proof workflow exists.
2. Monitor LangGraph nodes, CrewAI roles, LlamaIndex corpus boundaries, LangSmith readiness, env/config status, and WikiLLM run history without making the dashboard the project brain.
3. Use `project/dashboard/` and `project/reports/2026-06-25-dashboard-setup-and-operation-report.md` as the public-safe implementation and operation reference.
4. E2.2.2 research engine stages: hypothesis -> account universe -> parallel public signal extraction -> pain scoring -> live role verification -> message synthesis -> learning loop.
5. E2.2.3 parallel work rule: universe building, website parsing, job-signal capture, review mining, and social-language mining can run in parallel; synthesis, role verification, message approval, memory promotion, and outreach handoff remain sequential and reviewed.
6. E2.2.4 evidence rule: account qualification should use at least two independent public signals before outreach, such as website/service page plus job post, review theme plus case study, or founder/company post plus careers signal.
7. E2.2.5 fact-check gate: every ICP, offer, or outreach claim must be downgraded to HYPOTHESIS if it lacks source support or current role verification.

## E3 - Website And Positioning

Goal: build a site path from message to solution page to diagnostic form.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E3.1 Fix positioning and message | In Progress | Website | 2026-07-04 | Hero text and five-screen message structure. |
| E3.2 Homepage interactive block and tools block | Backlog | Website | 2026-07-07 | Working homepage interaction. |
| E3.3 Solution page for KB/PRD with ROI and CTA | Backlog | Website | 2026-07-10 | Solution page with clear action point. |
| E3.4 Diagnostic page and analytics-ready form | Backlog | Website | 2026-07-12 | Form page that captures leads and events. |
| E3.5 Blog, navigation, and final site assembly | Backlog | Website | 2026-07-14 | Connected site ready for traffic. |

E3 positioning update:

1. Primary message should narrow around `raw product-team material -> reviewed production-ready PRD/backlog/KB pack`.
2. The product-team solution page should show before/after artifact proof, redaction/source-boundary rules, review gates, and existing-tool handoff.
3. The diagnostic form should ask for segment, trigger event, current tools, source-packet willingness, privacy concerns, budget-owner path, and preferred output destination.

## E6 - Outreach

Goal: test the offer against real people and conversations.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E6.1 Write short offers for each ICP target | Backlog | Sales | 2026-07-14 | 10 to 15 personalized offer drafts. |
| E6.2 First outreach wave | Backlog | Sales | 2026-07-18 | 10 to 15 contacts initiated and responses logged. |
| E6.3 Conversations and diagnostics | Backlog | Sales | 2026-07-21 | Pain and reaction log from real conversations. |
| E6.4 Process inbound leads by qualification checklist | Backlog | Sales | 2026-07-24 | Qualified inbound leads moved toward the same offer. |
| E6.5 Second wave and follow-up | Backlog | Sales | 2026-07-28 | Follow-up completed and message angles compared. |

E6 first-wave targeting update:

1. Start with 10 to 15 people in the same ICP: Directors or VPs of Product, Heads of Product, Product Ops leads, or senior PM leaders inside B2B SaaS companies with roughly 50-500 employees and 2-5 PMs.
2. Every message must cite one public signal, name one pain hypothesis, offer one concrete artifact, and use one low-friction CTA.
3. Do not send generic AI automation pitches.

## E7 - Payment Test To Verdict

Goal: decide whether the first solution has real demand.

Tasks:

| Task | Status | Type | Due | Public Output |
|---|---|---|---|---|
| E7.1 Move warm contacts to payment or prepayment decision | Backlog | Sales | 2026-07-28 | Clear yes/no status for each warm contact. |
| E7.2 Demand verdict: money versus attention | Backlog | Ops | 2026-07-31 | Count of paying or firm-intent prospects. |
| E7.3 Decision on next step | Backlog | Ops | 2026-08-01 | Team decision for the next month. |

Validated demand means one of:

- paid diagnostic
- prepayment
- signed or approved paid start
- firm paid intent with source packet, timeline, scope, and budget-owner path

Not validated demand: directory universe size, market-size math, job counts, social posts, named sample accounts, competitor features, internal E1 proof, content engagement, ICP ranking, compliments, replies, or "interesting" feedback.

## Acceptance Criteria For The Current Public Project

- The KB project is clean and reproducible.
- One internal dialogue-to-PRD run is completed.
- The output is safe enough to explain publicly without raw private material.
- The agent stack can read back the KB and produce a useful follow-up answer.
- The website and content do not claim validated customer demand before the payment test.
- The August 1 verdict separates payment or firm intent from likes, comments, and vague interest.
