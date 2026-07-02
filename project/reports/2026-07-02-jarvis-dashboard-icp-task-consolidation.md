# Jarvis Dashboard ICP Task Consolidation

Date: 2026-07-02
Status: Prompt 1 consolidation complete; implementation not started
Lead integrator: Jesus/Codex

## Executive Decision

ArchFlow should enter Prompt 2 only as a bounded static/dashboard MVP implementation lane. Prompt 2 is allowed to begin after this consolidation if it stays inside the documented boundaries: static or browser-local dashboard work, clear runtime-state labels, generated public-safe data, local packet export, and review-gated implementation artifacts.

Prompt 2 is not allowed to activate provider-backed Jarvis, Railway/backend services, durable writeback, live Nexus actions, autonomous Notion/GitHub/WikiLLM writes, Telegram delivery, raw voice persistence, or production promotion without separate approval and proof.

## Product Concept

ArchFlow is an AI-native service that turns raw product-team material into production-ready PRD output in days rather than weeks. The raw material can include product conversations, meeting notes, customer research, interview summaries, internal documents, decision records, backlog fragments, and execution context.

The service is not positioned as another generic AI chatbot or a replacement for a product-management platform. It is a source-to-artifact operating service. It takes approved material, organizes the source boundary, produces a context digest, builds a source-backed PRD, extracts tasks and acceptance criteria, records decision history, and hands the result to a governed multi-agent execution workflow.

The connected knowledge-base engine matters because a PRD is only trustworthy when the team can see where the claims came from, what was inferred, what remains unknown, who owns the next step, and which actions are blocked until review. The dashboard is therefore a supervision layer for the owner, not the brain itself.

## ICP

The current ICP is one vertical: product teams in B2B SaaS companies, usually Series B-D, roughly 50-500 employees, often with 2-5 PMs, where the Director or VP of Product owns PRD quality, discovery-to-delivery speed, and cross-functional alignment.

Adjacent audiences such as agencies, founder-led startups, market-research teams, enterprise product-ops groups, and general operations teams remain later-lane hypotheses unless E2 evidence changes the plan.

## Pain Being Solved

The buyer pain is not just "write a PRD." The recurring pain is scattered context, repeated synthesis work, lost customer evidence, weak decision memory, unclear ownership, repeated engineering handoff questions, and anxiety that AI-generated output is not governed enough for real delivery.

The first wedge is the Product Discovery-to-Production PRD Pack. It should produce:

- a source inventory and source-boundary note;
- a context digest;
- a production-ready PRD;
- ICP or account evidence cards where relevant;
- task matrix and ownership map;
- acceptance criteria;
- decision log;
- risk and gap list;
- knowledge-base update packet;
- approval-gated agent handoff.

This is what "production-ready PRD in days, not weeks" means in the current phase: a reviewed artifact bundle that a product leader can use for engineering handoff and follow-up execution, not an unreviewed draft or autonomous platform claim.

## Evidence Reviewed

This consolidation used public-safe project evidence and sanitized live task-board metadata. The main evidence surfaces were:

- `project/project-plan.md`
- `project/reports/2026-07-01-messi-coordination-review.md`
- `project/reports/2026-07-01-messi-task-architecture-review.md`
- `project/reports/2026-07-01-current-state-e1-e7-vercel-railway-jarvis.md`
- `project/reports/2026-07-01-openrouter-model-routing-plan.md`
- `project/reports/2026-07-01-dashboard-website-strategy-qa.md`
- `project/runs/E1.3/2026-06-30-kb-readback/`
- `project/runs/E1.5/2026-06-30-public-reporting-gate/`
- `project/runs/yushchenko-model-efficiency/2026-07-02-1112-model-efficiency-report.md`
- `project/config/model-routing.yaml`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- live task-board status rows for E1, E1.3, E1.3.8, E1.3.9, E1.3.10, E1.3.11, and JDB tasks, summarized without private URLs or IDs.

Five read-only audit lanes also contributed findings: Notion/E1 task audit, GloomyLord document review, ICP/competitor positioning, technical state, and dashboard two-lane UX.

## GloomyLord Document Conclusions

GloomyLord should stay an internal visual/reporting sidecar. Its role is to turn approved execution evidence into public-safe report templates, proof cards, carousel structures, dashboard status cards, and visual reporting systems. It is not a public brand, not a runtime, and not a writer with publication authority.

The GloomyLord review packet around the June 29 documents should be interpreted as E1/E1.5 support, not E2 execution. The useful conclusions are:

- the tool-stack document should inform source boundaries and workflow design;
- the market-analysis theory document should act as default analysis context;
- the PRD market analysis should be read through the single B2B SaaS product-team ICP;
- the ICP market analysis should preserve the current single vertical and downgrade broader audiences to later-lane hypotheses;
- public reporting can explain method and proof only after AF Review plus owner approval.

No public-safe evidence proved that shorthand `138`, `139`, `11310`, or `41310` are standalone GloomyLord execution tasks. Live and local evidence resolve the real issue as task naming drift around E1.3.8, duplicate-looking E1.3.9 rows, and duplicate-looking E1.3.10 rows.

## E1 Task Conclusions

E1 is active, not fully done. E1.1 is complete. E1.2 remains Review until owner acceptance. E1.3 is Review-ready because KB writeback/readback proof exists, but it should not be marked Done while E1.2 acceptance, hosted/shared dashboard access, live API/Railway, write actions, vector benchmark, and GloomyLord publication package remain incomplete.

E1.3.1 through E1.3.7 are Done as KB/readback subtasks. E1.3.8 remains Review for the June 29 market/tool context review and ICP correction. E1.3.11 remains Review for KB readback delta and E2 handoff gate.

The dashboard/security rows should remain distinct from the GloomyLord/reporting rows. The clearest canonical split is:

- E1.3.9 dashboard/Jarvis/hosting umbrella: Review.
- E1.3.10 access/security/runtime gate: Review.
- GloomyLord audience-pain sample: move or rename under E1.5/reporting or E2 preflight, currently Blocked/Needs Review.
- GloomyLord method log and planning package: move or rename under E1.5/reporting, currently Blocked/Needs Review.

## Duplicate Task Merge Decisions

Do not delete information. Consolidate meaning:

- Keep dashboard/Jarvis hosting under E1.3.9.
- Keep access/security/runtime gate under E1.3.10.
- Move or rename GloomyLord planning/method/reporting rows under E1.5 so they stop colliding with security/runtime numbering.
- Treat shorthand `8` and `9` as ambiguous unless prefixed with E1.3 or JDB.
- Treat `138`, `139`, `11310`, and `41310` as unverified aliases; do not create new tasks from them without live sanitized owner confirmation.

## Already Done

FACT:

- Static public website and diagnostic route have prior review evidence.
- Static/browser-local dashboard evidence exists.
- Dashboard data generation exists.
- Dashboard smoke evidence has previously shown static routes, zero provider calls, and zero writeback.
- E1.3 KB readback proof exists and passed its recorded assertions.
- JDB-8, JDB-9, and JDB-10 are Done only for the static/browser-local scope.
- OpenRouter routing is documented as a future specification.
- Yushchenko observer reports no active OpenRouter runtime evidence and no token/cost ledger.

## Still Gated

GAP:

- provider-backed Jarvis;
- Railway/backend or local bridge;
- live Nexus writeback;
- durable GitHub/Notion/WikiLLM/Obsidian writeback from the web UI;
- owner-device microphone/speaker proof;
- raw voice/file persistence;
- model-call ledger and cost logging;
- vector retrieval benchmark;
- production promotion and Figma sync;
- Telegram delivery;
- E2 evidence cards;
- E5 ROI method completion;
- E6 outreach;
- E7 payment or firm-intent verdict.

## Dashboard Service Model

The Jarvis dashboard MVP has two coherent lanes.

Lane A is direct Jarvis chat and configuration control. It should support typed command intake, normal and interview modes, manual transcript fallback, local packet staging, file metadata intake only, local export, configuration/subprompt editing, and explicit runtime-state labels. It must never imply it can write to Git, Notion, WikiLLM, Obsidian, providers, Telegram, or production without an approved bridge.

Lane B is coordinator/executor supervision. It should show the PRD/ICP Flow and Agent Orchestra as separate workflows. It should display node inputs, outputs, prompts, config, logs, comments, safety state, approval state, validation checks, report generation steps, and deployment sequencing. It should help the owner see what is ready, what is blocked, and what needs review.

The MVP should control review packets and proof. It should not yet control live autonomous execution.

## Safe Customer-Facing Claims

Safe now:

- ArchFlow turns scattered product context into source-backed PRD and execution packets.
- The current offer is designed for B2B SaaS product teams with Director/VP Product ownership.
- The system uses source boundaries, evidence labels, task extraction, acceptance criteria, decision logs, review gates, and knowledge-base handoff.
- Current dashboard proof is static/browser-local and public-safe.

Gated:

- validated demand;
- paying customers;
- guaranteed ROI or cycle-time savings;
- autonomous execution;
- live provider-backed Jarvis;
- Railway/backend runtime;
- live Nexus/writeback;
- Telegram delivery;
- production-grade voice.

## Implementation Should Do Next

Prompt 2 should start with a static MVP implementation scope:

1. Read the live communication log and current Git state.
2. Preserve existing dirty work and active file claims.
3. Define the Lane A command/packet schema.
4. Define the Lane B supervision/state schema.
5. Keep runtime states visible: static snapshot, browser-local, provider disabled, backend absent, writeback gated.
6. Add or verify dashboard smoke markers for both lanes.
7. Add mobile/modal acceptance proof.
8. Regenerate `project/dashboard/data.json` after source/report changes.
9. Run public safety, JavaScript syntax, JSON parse, workflow validation, runtime guard, dashboard smoke, and diff hygiene checks.

Backend/provider/voice bridge design should be a separate later prompt after approval.

## Implementation Readiness

Ready for Prompt 2 with constraints.

Prompt 2 may begin only as a static/browser-local dashboard MVP implementation and proof pass. It must not begin provider/backend/voice/writeback implementation unless the owner explicitly authorizes that separate lane.
