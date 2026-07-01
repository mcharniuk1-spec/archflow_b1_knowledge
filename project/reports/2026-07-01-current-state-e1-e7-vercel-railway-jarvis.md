# Current State: E1-E7, Vercel, Railway, Jarvis, And Knowledge System

Date: 2026-07-01
Status: current-state synthesis after June 30 transfer and provider cleanup

## Executive Answer

ArchFlow is in a two-paradigm state.

Paradigm 1 is the showable service product: a Product Discovery-to-Production PRD Pack for product teams. Its goal is to turn raw product-team material into a reviewed PRD, task/responsibility plan, ICP evidence, and a buyer-facing demo/landing path. This is not validated commercially yet. The product concept is coherent, but E2 evidence, E3 positioning, E4 content proof, E6 outreach, and E7 payment verdict still need execution.

Paradigm 2 is the reliable development and control system: the local agentic operating environment that makes Paradigm 1 repeatable. It contains Codex as operator, LangGraph-style state/control, WikiLLM memory, Graphify structure, public-safe run notes, dashboard/Jarvis UI, hooks, validations, and future provider/backend gates. This layer is stronger than the product layer today: E1 proof exists, E1.3 readback passed, and the accepted June 30 dashboard review branch works as a browser-local/static review slice.

Vercel is the current dashboard hosting path because the dashboard is static and source-generated. Railway is not configured as a live backend. Railway becomes relevant only when the project needs server-side auth, API state, queues/workers, SSE/websocket events, provider calls, durable uploads, or writeback. OpenRouter and Mistral keys now exist only in ignored local env storage; the June 30 OpenAI local key file was removed. The static dashboard must not call any provider directly.

## Situation And Complication

The project has enough internal proof to show a controlled PRD/KB workflow, but it does not yet have buyer evidence. The same work also created a local agentic operating system. That is useful, but it can become confusing if dashboard UI, provider keys, Railway, Vercel, Notion, WikiLLM, vaults, Graphify, and Jarvis are described as one finished system.

The correct current interpretation is staged:

- E1 proves internal KB/PRD/retrieval discipline.
- E2.0 should prove the research engine internally before production market research.
- E2 should validate ICP evidence.
- E3/E4/E5/E6/E7 should convert that evidence into positioning, content, metrics, outreach, and payment verdict.
- Dashboard/Jarvis should remain the internal control surface, not the product itself.

## Customer / Stakeholder Job

Situation: a product leader or founder has scattered product context across meetings, notes, customer research, docs, and chats.

Functional job: convert scattered context into a production-ready PRD, backlog, acceptance criteria, decision log, and knowledge-base update.

Social job: look organized, precise, and execution-ready in front of engineers, leadership, and stakeholders.

Emotional job: reduce anxiety that important context, decisions, or buyer evidence was missed.

Current alternatives: manual PRD writing, meeting summaries, Notion/Linear/Jira notes, consultants, generic AI assistants, product-ops templates.

Switching trigger: repeated PRD rework, missed context, long discovery cycles, unclear ownership, or pressure to ship faster.

Adoption barriers: private-source handling, trust in output quality, integration with existing tools, proof that the system understands the actual product context, and fear of over-automation.

## E1-E7 Current State

| Epic | Goal | State | Result | Next need |
|---|---|---|---|---|
| E1 | Build the knowledge base on ourselves | Active, strongest layer | E1.1 Done; E1.2 Review; E1.3 Review with readback proof passed; E1.5 reporting/dashboard gate in progress | Owner acceptance, E1.4 KB update principle, and clearer E1.5 reporting boundaries |
| E2 | Research engine to ICP | Not production-executed | E2 is defined as evidence engine; E2.0 internal dry run is the next safe step | Evidence-card schema, source grades, role verification, market reports, ICP profile |
| E3 | Website and positioning | Preliminary only | Current product-team ICP and PRD Pack hypothesis exist | E2 evidence must drive positioning before public claims |
| E4 | Content | Planning / gate only | Content-template direction exists; no public publishing approved | Content must separate attention from demand and link to proof |
| E5 | Analytics and ROI | Active but incomplete | Static dashboard exists; E5.1 done; ROI methodology not finished | Funnel metrics, qualification scoring, ROI formula, dashboard panels |
| E6 | Outreach | Not started | No autonomous or manual outreach wave is proven | 10-15 source-backed targets after E2/E3/E4 gates |
| E7 | Payment verdict | Not started | No demand verdict exists | Paid diagnostic, prepayment, approved paid start, or firm paid intent |

Status vocabulary note: this report uses plain-language readiness states, not the exact task-board labels. E3 is still not started as a full website/positioning epic, even though E3.1 planning/material preparation can be in progress. E4 is active as a content-template/reporting gate, but no public publishing or demand proof is approved.

## Vercel And Railway State

Vercel:

- Current role: static dashboard hosting and protected/hidden-link preview.
- Working layer: source-generated dashboard under `project/dashboard/`.
- Strong point: can keep the last deployed state visible when local Codex/Jarvis is off.
- Limit: cannot execute Jarvis, call providers safely, access local files, update Notion/GitHub/WikiLLM, or change runtime parameters by itself.

Railway:

- Current role: planned, not configured.
- Needed only for: server-side auth, live API, queue/worker, SSE/websocket, provider calls, durable uploads, persistent run state, or writeback.
- Not safe to claim: live backend, active Jarvis runtime, Codex bridge, provider-backed voice, or automatic memory sync.

## Provider And Key State

FACT:

- `OPENROUTER_API_KEY` and `MISTRAL_API_KEY` are now stored only in ignored local env storage outside public Git.
- The Markdown secret source was deleted.
- The local OpenAI key file created on June 30 was deleted.
- Ignored env files were set to owner-only permissions.
- No provider key should appear in Git, dashboard JSON, Notion, WikiLLM, screenshots, or public run notes.

INTERPRETATION:

- OpenRouter can become the first hosted model-router option for Jarvis/orchestration only through an approved local bridge or backend.
- Mistral remains a gated quality/synthesis provider for sanitized PRD/research/copy passes.
- OpenAI is not configured for local runtime after cleanup.
- Static browser JavaScript cannot safely use any provider key.

GAP:

- No approved local bridge or Railway backend exists yet.
- No provider-call budget, model id, logging policy, or data-class approval is configured.

## Knowledge System State

WikiLLM:

- Active as durable public-safe memory inside `wiki/`.
- Updated by run notes, memory summaries, decisions, and issues.
- Needs the June 30 accepted `d18fc55` state added to memory/log, which this July 1 pass does.

Obsidian vault / second brain:

- Global and project vault contracts exist outside the public repo.
- A dedicated ArchFlow Obsidian vault is still not the active public source in this repo.
- Live Nexus is not proven here; file-based mirror was used in the LangGraph final handoff.

Graphify:

- Public project Graphify output exists under `graphify-out/`.
- It is generated structural reference, not final strategy.
- It should be regenerated after structural dashboard/code changes if graph accuracy matters.

Nexus:

- Live Nexus tool operation was not available/proven in this pass.
- Do not claim live vault writeback until schema discovery and tool-call verification pass.

Vault organization issue:

- The knowledge is not fully organized because several layers were created in parallel: ArchFlow public repo, LangGraph course-support, global agent-infra WikiLLM, Notion tasks, and Obsidian mirror packets.
- The practical fix is not to dump everything into one vault. The fix is to keep routing explicit: product proof in `project/runs/`, durable public memory in `wiki/`, strategic summaries in `project/reports/`, external/global agent-infra mirrors only for cross-project operating lessons, and private raw material outside public Git.

## Dashboard And Jarvis State

Working now on the review branch:

- Jarvis shell.
- Manual transcript fallback.
- Browser-local chat/history.
- Browser speech recognition/synthesis controls where the browser supports them.
- File metadata packets without reading document bodies.
- `(1) PRD/ICP Flow` block-schema screen.
- `(2) Agent Orchestra` block-schema screen.
- Node control panel for inputs, outputs, prompts, comments, run notes, config, and connections.
- Browser-local packet export.

Not working / gated:

- Physical microphone/speaker proof requires owner-device permission.
- Provider-backed voice is not active.
- Real Jarvis comprehension through OpenRouter/Mistral is not active.
- Local Codex/Jarvis bridge is not active.
- Railway backend is not active.
- Durable writeback to GitHub, Notion, WikiLLM, Obsidian, or Telegram is not active from the web UI.

## External Repos And NVIDIA Safety

Reviewed references:

- `claude-mem`: useful as a memory-system reference because it uses hooks, a worker service, database, and search tools. It is not installed here and should not be adopted without a separate hook/privacy review.
- `impeccable`: useful as a dashboard/UI design guidance reference because it provides design setup, commands, live browser iteration, and deterministic frontend detectors. It is not installed here.
- NVIDIA `garak` / NeMo Guardrails: useful future safety-evaluation references for LLM apps and guardrail configurations. No NVIDIA safety CLI or skill is installed in this environment.

Implementation state:

- None of those repos are implemented in ArchFlow.
- None are connected to turbovec.
- turbovec remains a future retrieval/vector-store gate after E1.3, stable source IDs, chunk metadata, embeddings, and retrieval benchmark exist.

## Telegram Result

The Telegram message was not sent because the approval reviewer blocked external disclosure of protected/internal links and status data. The correct state is: final message body prepared in the LangGraph support workspace, but external Telegram publishing requires explicit owner approval for the exact disclosure after the warning.

## Recommendation

Keep the next execution in two tracks:

1. Paradigm 1, service product: run E2.0 dry run, then E2 evidence cards, then update E3/E4/E5 assets from real evidence.
2. Paradigm 2, development system: finish dashboard UI verification, keep provider calls disabled, define the local bridge/Railway contract, and regenerate dashboard data after each knowledge change.

## Requirements And Acceptance Criteria

Functional requirements:

- Dashboard must distinguish static, local bridge, hosted backend, provider-ready, and blocked states.
- Agent schemas must show inputs, outputs, prompts, comments, run notes, config, and approvals.
- Provider keys must stay out of client JavaScript and public files.
- Every durable write needs a run note and safety scan.

UX requirements:

- Main page starts with Jarvis as the operating center.
- `(1)` and `(2)` must be visible as separate schema screens.
- Node control panel must make agent state understandable without opening raw files.

Analytics requirements:

- E5 needs funnel stages, qualification scoring, and ROI formula before demand claims.

Operational requirements:

- Use Codex for source changes.
- Use Vercel for static last-known state.
- Use Railway only after backend need, auth, secrets, and data policy are explicit.

Acceptance criteria:

- JS syntax passes.
- Dashboard route renders.
- Public safety scan passes.
- Workflow validation passes.
- Runtime guard passes or records exact blocked reason.
- Dashboard `data.json` is regenerated after source/knowledge edits.

## Risks And Counterarguments

- Risk: OpenRouter connection is misunderstood as live. Counter: document it as local-env-only and backend/local-bridge gated.
- Risk: dashboard becomes a fake control plane. Counter: show static/local/backend state explicitly.
- Risk: vaults stay fragmented. Counter: each layer gets a purpose and links back to run notes.
- Risk: E2 is skipped and product claims become ungrounded. Counter: keep E2.0 and evidence cards as the next required gate.
- Risk: third-party memory/hook tools capture private data. Counter: no install until safety and privacy review.

## Confidence Level

Reliable data confidence: 0.86 for branch state, E1-E7 status, provider cleanup, and dashboard static/backend boundaries because these are backed by local files, branch checks, and run notes.

Probable confidence: 0.65 for external repo applicability because source pages were reviewed, but no local install/sandbox audit was run.

Unreliable below 0.5: any claim that live Jarvis, Railway backend, provider-backed voice, live Nexus, or payment demand is complete.
