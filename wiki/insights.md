# Insights

## Public System Design

The safest current architecture separates three concerns:

- Codex supervises work and publication.
- Ollama runs local models.
- LangSmith observes traces after public-safety filtering.

This avoids mixing operator authentication, model credentials, and observability credentials.

## Block 1 Execution Insight

The project should prove one internal workflow before adding customer-facing claims:

1. Take a sanitized source summary.
2. Produce context digest.
3. Produce PRD.
4. Produce responsibility matrix.
5. Produce KB update.
6. Produce review report.
7. Publish only approved public-safe outputs.

## LangSmith Insight

LangSmith should receive structured run metadata and trace spans, not raw private material. The first useful trace should be a synthetic or sanitized proof run, not an unfiltered private transcript.

## Implementation Sequencing Insight

The lowest-risk order is: verify LangSmith trace with a sanitized run, install LangGraph runtime, add LlamaIndex retrieval, then add CrewAI execution. This keeps workflow control and public-safety gates stable before adding team automation.

## E1.2 Proof Insight

The first full proof should not start as a market research task. It should start as a controlled source-to-artifact workflow: source inventory, context digest, sole summary, PRD, responsibility matrix, KB update, retrieval log, and review report. Market and web research become useful after this proof defines explicit questions.

## CrewAI Boundary Insight

CrewAI imports can create app-data storage by default. In this project, CrewAI guard checks must override runtime storage to ignored project-local storage and disable telemetry/tracking. CrewAI should organize roles while LangGraph controls routing, revision loops, and approval gates.

## Dashboard Sequencing Insight

The dashboard should lag the proof workflow, not lead it. A read-only readiness dashboard is useful now because it exposes config health and memory activity without freezing early assumptions. A full control panel should wait until LangGraph, LlamaIndex, CrewAI, WikiLLM writes, and LangSmith traces have produced at least one complete proof run.

## E1.2 Streaming Insight

For public operational reports, streaming should mean observable graph state and progress: node names, state deltas, artifact paths, tool results, warnings, and review decisions. It should not mean saving hidden reasoning text. This keeps debugging useful without weakening the public-safety boundary.

## E1.2 Agent Configuration Insight

The first production-like agent setup should keep AF Tools, AF Review, and AF Publisher deterministic; allow only modest variance for AF Context, AF Manager, AF Knowledge, and technical trend analysis; and keep CrewAI LLM task execution behind LangGraph until one artifact-generating run passes review.

## E1.2 To E1.3 Handoff Insight

The correct transition gate is owner acceptance plus KB readback, not more artifact generation. E1.3 should prove that the approved PRD and agent history can be written into public-safe memory and retrieved by a future agent before Obsidian mirror expansion, Nexus live writes, or broader research layers are activated.

## Loop And Memory Architecture Insight

Loop Engineering should wrap the current LangGraph/CrewAI/LlamaIndex stack rather than replace it. The reliable pattern is state plus stop conditions: source boundary, attempt caps, maker/checker separation, budget, run log, review, handout, and memory promotion. WikiLLM remains the truth layer; Cognee and turbovec are useful only when they are fed approved artifacts and can be rebuilt or reset.

## Market Engine Insight

The first sellable market wedge is not generic AI productivity or "make a PRD." It is reducing ambiguity, PM/BA cleanup time, rework, weak handoffs, scope creep, and lost decision memory for B2B SaaS product teams that repeatedly convert product discovery and customer conversations into buildable work. E2 should therefore produce account-level evidence cards and ICP scores before content or outreach claims.

## Demand Validation Insight

Validated demand requires buyer risk: paid diagnostic, prepayment, approved paid start, source packet plus timeline/scope, budget-owner referral, or proposal request. Attention, compliments, category counts, social interest, and internal proof do not validate demand.

## Execution Report Insight

ArchFlow now needs decision-question closeouts because tasks span workflow design, Notion, GitHub, dashboard hosting, voice, Onyx, and public content. The failure risk is moving to the next stage while key owner decisions remain implicit. The `outquestions` skill solves this by turning every substantial run into a short report with blocking decisions, optional refinements, next-stage gates, and risks.


## Insight - E1.3 Readback Before Content And Live Services

- Observation: E1.3 only becomes useful when a future agent can recover the mission, gates, outputs, gaps, and next actions from artifacts rather than from chat context.
- Interpretation: readback proof is the real transition from document generation to an agent-ready operating KB.
- Why it matters: this prevents dashboard, voice, Onyx, vector retrieval, and public reporting from becoming competing systems before the core memory loop is reliable.
- Where applicable: E1.4 KB principle, E1.5 reporting gate, E2 evidence engine, hosted dashboard planning, and future turbovec benchmark.
- Limitations: the current proof is deterministic lexical readback; vector retrieval still needs source IDs, chunk IDs, embeddings, and a benchmark.

## Insight - Static Jarvis Shell Versus Durable Execution

- Observation: A static Vercel dashboard can make the operating system easier to use before the backend exists, but it cannot safely own durable writes or private state.
- Interpretation: the reliable split is browser-local preparation first, then Codex or Railway-backed writeback after explicit approval.
- Why it matters: this lets Jarvis accept typed, voice, and file inputs now without pretending that static JavaScript can update the KB, Notion, GitHub, or local files.
- Where applicable: dashboard hosting, voice mode, file checks, E1.5 content templates, E2 research packets, and future Railway API design.
- Limitation: true live state, Google auth, SSE/websocket events, background jobs, provider model calls, and durable memory writes require a backend.

## Insight - Economical Frontier Council

- Observation: ArchFlow benefits from strong Claude, Gemini, and OpenAI models for strategy, long reasoning, and review, but using them for every transformation would waste budget and create slow feedback loops.
- Interpretation: the reliable model architecture is a tiered maker/checker system: cheap execution models produce structured intermediate artifacts, deterministic checks validate shape and source IDs, and frontier models review only when the output affects strategy, public claims, memory, outreach, architecture, or payment verdicts.
- Why it matters: this keeps the system economically viable while still using the strongest models where mistakes would be expensive.
- Where applicable: E1 PRD/KB review, E2 account evidence cards, E3 positioning, E4 content, E5 ROI logic, E6 outreach, E7 payment verdicts, and future Railway/provider bridge design.
- Limitation: model names and pricing change quickly, so exact OpenRouter IDs must be refreshed before runtime activation.

## Insight - Model Efficiency Needs A Ledger

- Observation: A model-routing plan can prevent obvious misuse, but it cannot measure efficiency without recorded model IDs, task roles, token counts, costs, reviewers, and outcomes.
- Interpretation: the Yushchenko observer is useful as a recurring reviewer, but real optimization requires a canonical model-call ledger before OpenRouter activation.
- Why it matters: without a ledger, agents can only give qualitative advice and cannot prove which model choices saved money or improved output quality.
- Where applicable: OpenRouter activation, E2 account research, E3 content and website drafts, E6 outreach variants, E7 payment verdict review, and future provider bridge design.
- Limitation: Telegram delivery and cost accounting remain partial until an approved sender and model-call logging source exist.

## Insight - Context-Overhead Measurement Is Blocked

- Observation: No local public-safe evidence records provider context-window settings or runtime configuration overhead from VLLM 0.5, instruction packs, or extra libraries.
- Interpretation: context-load overhead cannot be measured on this run; only proof of endpoint and token-window logging would make comparisons valid.
- Why it matters: claims of efficiency gains from model-library instructions are currently speculative without measured `context_window_tokens` and per-call metadata.
- Where applicable: model routing drift checks, benchmark planning for `VLLM 0.5` or local bridge activation, and future frontier escalation thresholds.
- Limitation: endpoint-level telemetry must become part of the model-call ledger before any hard efficiency statement can be made.

## Insight - Website Sells The Service, Dashboard Proves The Control Layer

- Observation: The strongest July 1 combined state separates the blue/ivory public website from the internal operator dashboard instead of trying to make one surface do both jobs.
- Interpretation: the website should stay focused on the buyer-facing PRD/ICP service wedge, while the dashboard should prove source state, routes, generated data, and blocked gates.
- Why it matters: this prevents overclaiming live Jarvis/provider/Railway/writeback execution while still giving the owner a working public page and a reliable test dashboard.
- Where applicable: E3 website promotion, JDB dashboard review, Notion task descriptions, future Figma baseline sync, and any backend/provider activation decision.
- Limitation: owner-device voice acceptance and provider-backed runtime proof remain separate from static visual and route proof.

## Insight - Tags Make Multi-Agent Delivery Auditable

- Observation: Notion had task type and status fields, but no way to record which agent specialization actively contributed to each row.
- Interpretation: `Agent Tags` are the right lightweight mechanism for PM review because they preserve Type as the work category while recording QA, senior-dev, frontend, dashboard, LangGraph, RAG/KB, Telegram, API, Notion, GitHub, and reviewer responsibility signals.
- Why it matters: future agents can route work to the right workflow without reading long chat history or confusing Done static work with gated runtime work.
- Where applicable: JDB dashboard tasks, E3 website tasks, E2 research tasks, Telegram delivery tasks, scheduled skill/RAG retrospectives, and merge/promotion reviews.
- Limitation: tags are useful only if future updates keep them evidence-backed and avoid tagging every row with every role.

## Insight - Static Control Surface With API Contract

- Observation: Prompt 2 can make the dashboard operationally useful before a live backend exists by combining browser-local packets, visible role configuration, provider-disabled API contracts, and explicit budget/runtime gates.
- Interpretation: the reliable next layer is not a hidden provider call; it is a reviewable packet path plus a server-side contract that can later be activated under auth, secrets, budget, ledger, and owner approval.
- Why it matters: this preserves momentum on PRD/ICP workflow design while preventing the dashboard from implying Railway, OpenRouter, Telegram, Notion, or default CrewAI runtime readiness.
- Where applicable: Jarvis API activation, Screen 1 PRD/ICP tests, Screen 2 Agent Orchestra, OpenRouter budget guard, and future Railway deployment planning.
- Limitation: until FastAPI dependencies are installed and a backend is run, the service remains an implementation contract rather than runtime proof.

## Insight - Cloud Freshness Is A Separate Reliability Gate

- Observation: Railway can be healthy and Vercel production can load while production dashboard data remains older than the current review preview.
- Interpretation: hosted reliability has at least three layers: backend health, frontend availability, and deployed evidence freshness. All three must pass before claiming an always-current cloud surface.
- Why it matters: this prevents the project from treating a 200 response as proof that users see the latest verified state.
- Where applicable: E1.7 closeout, future Vercel production promotion, dashboard data generation, Notion/GitHub links, Telegram reporting, and any client review surface.
- Limitation: production freshness can only be closed by a post-push check or an explicit production deployment/promotion step.

## Insight - Guarded Provider Routing Is Not Provider Execution

- Observation: Vercel and Railway can both be configured for `MODEL_PROVIDER=openrouter` while still making zero provider calls if the server-side key is absent.
- Interpretation: this is a useful intermediate state: route shape, approval fields, budget guards, and architecture-specific packets can be verified without moving secrets or spending money.
- Why it matters: it prevents the project from confusing "OpenRouter route wired" with "OpenRouter output generated" and keeps credential-storage risk explicit.
- Where applicable: E1.7 cloud closeout, Epic 2 research planning, model-call ledger setup, and future Jarvis provider activation.
- Limitation: the next proof must be an explicitly approved, ledgered, low-cost provider call with sanitized input and no durable writeback.

## Insight - Watchdog Control Is Separate From Execution

- Observation: The Founder Meeting v2 package is strongest when Hermes controls classification, context capsules, task contracts, evidence review, and stop decisions while Codex remains the executor and integration boundary.
- Interpretation: a watchdog can improve reliability without becoming an autonomous executor. This preserves safety gates and avoids confusing planning authority with file/runtime authority.
- Why it matters: provider calls, writeback, Notion mutation, deployment, and production promotion remain explicit owner decisions instead of hidden side effects.
- Where applicable: LangGraph controller updates, subagent task contracts, CAG/RAG capsules, E1-E7 task packets, skills governance, and future Jarvis provider activation.
- Limitation: Hermes is currently a documented architecture and prompt contract, not a running controller service.

## Insight - CAG Prevents RAG From Becoming Unbounded Memory

- Observation: The integration separates CAG stable context from RAG task-specific evidence retrieval.
- Interpretation: CAG gives every subagent the current operating rules, architecture boundaries, E1-E7 state, and gated claims before retrieval adds only the evidence needed for the task.
- Why it matters: this prevents broad source ingestion, stale assumptions, and evidence-free completion claims.
- Where applicable: all broad ArchFlow architecture, content, task-board, provider, and KB work.
- Limitation: capsules must be regenerated when core project rules or task state changes.
## Role Authority And External-Action Sequencing - 2026-07-10

- Separating role authority from runtime identity lets Codex, Hermes, or another compatible agent participate without weakening maker-checker separation or turning a named tool into automatic execution authority.
- Git-first external sequencing makes the public repository the reviewed evidence boundary: branch work is merged and validated before task-board or production mutation is considered.
