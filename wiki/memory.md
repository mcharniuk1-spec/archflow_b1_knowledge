# Memory

## Stable Project Direction

ArchFlow Block 1 is the first public solution:

`dialogue/chat/meeting material -> structured context -> PRD -> responsibility plan -> agent-ready knowledge base`

## Current Runtime Decisions

- Codex is the primary operator, review, file-edit, and publication layer.
- Codex authentication is not exported as an API key.
- Ollama is the only model execution provider for now.
- Qwythos is the active local model after the latest smoke test generated text.
- `gemma4:e4b` remains the local fallback.
- LangSmith is tracing only, not a model provider.
- No cloud model provider is active in runtime. OpenRouter and Mistral keys exist only in ignored local env storage after the July 1 cleanup; browser/client code must not read or call them.
- LangGraph runtime is installed and the sanitized smoke workflow reached approved status.
- LlamaIndex runtime is installed and the approved public corpus retrieval proof returned source paths.
- CrewAI runtime is installed and config/import validation passes without LLM execution.

## Public Repo Rules

- All active project work goes under `project/`.
- Sanitized previous history goes under `history/`.
- Public WikiLLM memory goes under `wiki/`.
- Used/setup skills only go under `skills/` and `project/agents/`.
- Env files with real keys stay ignored.

## LangSmith Memory

- Project name: `ArchFlow`.
- Project ID: `masked_langsmith_project_id`.
- Endpoint: `https://eu.api.smith.langchain.com`.
- Local editable env: `project/.env.langsmith.local`.
- Public example env: `project/config/langsmith.env.example`.
- API key status: present only in ignored local env.
- Smoke trace status: submitted with sanitized Ollama-only metadata.

## Workflow Memory

- LangGraph controls path/state/review gates.
- CrewAI organizes named agents and expected outputs.
- LlamaIndex connects agents to bounded public-safe retrieval.
- LangSmith can trace sanitized workflow execution.
- The first complete proof should expand the LangGraph smoke path into E1.2 document generation.

## Safety Hook Memory

- Public pushes must run `.githooks/pre-push`.
- The hook runs `scripts/public_safety_scan.py`.
- The hook also runs `project/scripts/pre-push-runtime-guard.py`.
- The hook blocks publishable secrets, local paths, private links, tracked env files, tracked runtime files, and unsafe metadata.
- The local LangSmith key belongs only in ignored `project/.env.langsmith.local`.
- The runtime guard validates workflow YAML, LangGraph smoke, LlamaIndex approved-corpus retrieval, CrewAI config, and saved project skills.
- CrewAI guard checks must keep runtime storage inside ignored project-local storage and disable CrewAI telemetry/tracking.

## Task Handout Hook Memory

- `.codex/hooks.json` checks every submitted prompt for task handout triggers.
- The prompt hook runs `project/scripts/task-handout-hook.py` and does not store raw prompt text.
- `skills/task-handout/SKILL.md` is mandatory when the hook triggers, when one or more agent roles are used, or when one or more subtasks are solved or changed.
- The hook only marks that the handout skill is required; the executing agent must create or update `agent-handout.md` after outputs and checks exist.
- The ignored local marker is written under `project/local/task-handout-hook/`.

## Live Agent Communication Memory

- `project/live/communication/` is the shared active communication channel for parallel ArchFlow public project agents.
- Agents must read the current notice and latest communication log before work, append a starting update before edits, coordinate file claims, and append complete, blocked, or handoff updates after work.
- Run-specific `agent-handout.md` files remain the durable completion record for substantial work.
- Changes to the communication pattern must be recorded in `project/live/communication/pattern-change-log.md` and announced in `project/live/communication/agent-communication-log.md`.

## LangSmith Trace Memory

- LangSmith SDK is installed only inside ignored `project/local/venv`.
- A sanitized smoke trace was submitted with Ollama-only metadata.
- A sanitized LangGraph smoke trace was submitted.

## E1.2 Preparation Memory

- The June 24 next-steps source was reviewed as a private input and converted only into public-safe derived artifacts.
- The source supports starting E1.2 as a controlled dialogue-to-summary-to-PRD proof cycle.
- Speaker-specific ownership remains inferred; public outputs use role labels.
- Market research, web research, ICP validation, content tests, and customer-facing claims are downstream of the first E1.2 proof.

## E1.2 Full Test Memory

- E1.2 full-test graph ran with a sanitized source packet and reached approved status.
- The graph saved observable stream events and final state in `project/runs/E1.2/2026-06-26-full-test/`.
- E1.2 report PDFs were generated for the PRD, streaming report, and system report.
- Public streaming reports store node events, state summaries, and decisions; they do not store hidden chain-of-thought.
- Public files mask operational project identifiers; real values belong only in ignored local env or external systems.
- The approved LlamaIndex public corpus explicitly includes `project/`, `history/`, `skills/`, and `wiki/`.
- After Notion sync, E1.2 should remain in `Review` until owner acceptance even though E1.2.1 through E1.2.7 are evidence-backed `Done`.
- E1.3 should start with public-safe KB writeback and readback proof, not broad private ingestion, live Nexus writes, or CrewAI LLM execution.

## Dashboard Memory

- Phase 2 local dashboard exists under `project/dashboard/`.
- Dashboard data is generated by `project/scripts/generate-dashboard-data.py`.
- The dashboard is read-only and is a control panel, not the primary brain.
- WikiLLM remains the canonical durable memory layer.
- The dashboard monitors configured contracts, runtime package readiness, run files, and public-safe corpus status.

## Tool And Market Integration Memory - 2026-06-29

- Current MVP path remains E1 KB proof -> E2 research/ICP -> E3 website/positioning -> E4 content -> E5 analytics/ROI -> E6 outreach -> E7 payment verdict.
- Loop Engineering is adopted as an operating discipline for anti-looping, state, maker/checker separation, run logs, budgets, and human gates.
- Default loop level is L1 report-only. L3 unattended loops are blocked before payment verdict and explicit approval.
- Cognee is a candidate long-term memory/knowledge-graph layer after E1.3 readback proves public-safe KB writeback. It must not replace WikiLLM.
- turbovec is a candidate local vector store under LlamaIndex after vector embeddings, stable source IDs, and retrieval metadata are active.
- Mistral models are optional quality-pass models for sanitized PRDs, research synthesis, and final text after explicit credential, source-boundary, budget, and review approval.
- E2 first ICP hypothesis is one vertical: product teams inside B2B SaaS scaleups, especially Series B-D companies with 50-500 employees, 2-5 PMs, and Director/VP Product ownership of PRD quality and speed.
- Agencies, AI consultancies, founder-led B2B startups, market-research teams, operations teams, and enterprise product ops are later or adjacent lanes unless E2 evidence changes the hypothesis.
- First offer hypothesis is a Product Discovery-to-Production PRD Pack: product-team dialogues, customer research, interviews, notes, and docs become a reviewed context digest, production-ready PRD, backlog, acceptance criteria, decision log, and KB/update handoff in days, not weeks.
- E2 must use account evidence cards, source grades, role verification status, and at least two independent public signals before outreach.
- Directory counts, job counts, social posts, named sample accounts, internal proof, and content engagement are research signals only, not validated demand.

## Dashboard Voice Hosting Memory - 2026-06-30

- ArchFlow remains the workflow brain and canonical memory system.
- Onyx is a future optional portal/search/connector layer after readback and retrieval benchmark gates; it is not the primary control plane.
- The first live dashboard step should be static/read-only hosting, with Vercel as the preferred first target because the current dashboard is generated static UI.
- Railway is reserved for live API, background worker, queue, websocket/SSE, or voice-service needs.
- Voice starts local and read-only; write actions, deployments, external connector changes, outreach, and memory promotion require human approval and AF Review.
- GitHub stores source and public-safe examples only. Real credentials belong in provider secret stores or ignored local files.

## Outquestions Memory - 2026-06-30

- `skills/outquestions/SKILL.md` is the closeout skill for substantial execution.
- Use it after dashboard, voice, hosting, Onyx, Notion, GitHub, multi-agent, and public-reporting work.
- It must report what changed, artifacts, blocking questions, optional questions, next-stage gate, risks, and gaps.


## E1.3 Readback Memory - 2026-06-30

- E1.3 public-safe KB writeback/readback proof exists under `project/runs/E1.3/2026-06-30-kb-readback/`.
- E1.3 readback assertions cover current mission, next step, forbidden actions, existing outputs, open gaps, agent roles, graph route, ICP boundary, dashboard/voice gate, and public-reporting gate.
- E1.2 remains Review until owner acceptance; E1.3 can be in Review based on readback evidence without marking E1.2 Done.
- E1.5 has started only as a public-reporting gate under `project/runs/E1.5/2026-06-30-public-reporting-gate/`; no public posting is approved.
- GloomyLord is an internal visual/reporting sidecar by default, not public-facing branding unless separately approved.
- First hosted dashboard default remains static/read-only first. Vercel is preferred for that static step; Railway waits for live API, background worker, queue, websocket/SSE, or voice-service requirements.
- Voice commands start read-only/status only; write actions require human approval and AF Review.

## Dashboard Jarvis Vercel Memory - 2026-06-30

- The dashboard now has a Jarvis-first command shell under `project/dashboard/`.
- The first hosted dashboard target is hidden-link Vercel preview with public-safe static data only.
- Hidden link is not authentication; Google auth, server-side access control, and protected private state remain future gates.
- The dashboard can refresh deployed `data.json` without a page reload through manual refresh, focus/visibility refresh, command refresh, and timed polling.
- Static Jarvis can create browser-local packets from typed commands, authorized browser voice transcripts, and local text files, but cannot write to GitHub, Notion, WikiLLM, Obsidian, or local files.
- Railway remains deferred until the project needs API state, SSE/websocket events, voice execution, uploads, background workers, queues, model-provider calls, or durable writeback.
- The E1.5 content-template library now lives under `project/content/templates/` and turns reviewed executions into practical content plans; publication still requires AF Review and owner approval.

## Dashboard Reliability Sync Memory - 2026-06-30

- The current reliable web-view mode is protected static Vercel preview backed by committed public-safe source state.
- The dashboard README now records the verified preview URL and the reliability-sync procedure.
- Reliable dashboard updates require a run note, KB/log update, regenerated `project/dashboard/data.json`, safety/workflow/runtime checks, GitHub push, append-only Notion sync, and a web-view status check.
- Always-on execution is not active yet. Railway/API, OpenAI/Mistral runtime, live Codex bridge, persistent uploads, voice persistence, and browser writeback remain separate approval-gated work.

## June 30 Transfer And Provider Cleanup Memory - 2026-07-01

- The accepted June 30 static/browser-local review slice is `review-jarvis-agentbrowser-blockschema-20260630` at `d18fc55`.
- Main remains the reliable protected static dashboard baseline until owner-approved merge/deploy.
- JDB-8 is Done, JDB-7 is Review for merge/deploy, and E1.3.9 remains Review.
- Telegram publishing was not sent because the approval reviewer blocked external disclosure of protected/internal links and status data; exact owner-approved disclosure is required before sending.
- The dashboard now separates `(1) PRD/ICP Flow` from `(2) Agent Orchestra` and exposes node-level controls for prompts, comments, inputs, outputs, files, config, runs, and output links.
- OpenRouter and Mistral keys are available only in ignored local env storage for future approved local bridge or backend tests.
- The June 30 OpenAI local key file was removed; OpenAI is not an active ArchFlow runtime provider after cleanup.
- Static Vercel can preserve and display the last deployed dashboard state when the local agent is off, but cannot safely call providers, alter parameters, or write to GitHub, Notion, WikiLLM, Obsidian, or Telegram.
- Railway remains deferred until server-side auth, API state, queues/workers, SSE/websocket, provider calls, durable uploads, persistent run state, or writeback are explicitly approved.
- Review-branch Git durability for the July 1 dashboard/control-system stabilization was completed at `5efd281`; merge to `main`, deployment, backend/provider activation, and external writeback remain gated.
- When extending `project/config/model-routing.yaml`, preserve the validator-required `cloud_api`, `langsmith_observability`, and top-level `routing` keys. OpenRouter-specific planning can be richer, but it must not break the existing workflow validator or runtime guard.
- Dashboard voice UI must not claim browser microphone authorization until the browser actually starts speech recognition. Before that, describe the state as permission required or listening request pending.
- Dashboard/Jarvis UI changes should run `python3 project/scripts/dashboard-static-smoke.py` after regenerating data. This is the reusable rendered-route proof for `#jarvis`, `#history`, `#service`, `#schema`, `#config`, `#plan`, and the two node-panel deep links; it verifies static browser rendering only and does not prove mic/speaker, provider calls, Railway/local bridge, or writeback.

## Dashboard Two-Layer Schema Memory - 2026-07-01

- The dashboard must keep `(1) PRD/ICP Flow` and `(2) Agent Orchestra` as separate screens because they answer different jobs: externally showable service-product workflow versus local reliable control-system workflow.

## Prompt 2.1 Local Jarvis Stack Memory - 2026-07-02

- `skills/arcagcom/SKILL.md` is the project-local communication skill for live-agent file claims, start/handoff/complete updates, Prompt 2.1/Prompt 3 coordination, and merge gates.
- `skills/archflow1/SKILL.md` is the project-local operating skill for Dashboard UI, `jarvis-api`, optional STT/TTS services, LangGraph, CrewAI role levels, OpenRouter budget gates, and later Railway migration.
- Prompt 2.1 resolves shorthand task drift by mapping `138`, `139`, `11310`, `41310`, `8`, `9`, and `10` to exact E1.3.x/JDB rows instead of deleting history.
- The four owner decisions remain explicit gates: full PRD/ICP test cycle; FastAPI dependency install/runtime proof; OpenRouter server-side activation and budget ledger; Railway, Telegram, production/Figma sync, and dashboard-driven writeback.
- Schema nodes should remain draggable and clickable, with the full node panel used for inputs, outputs, connection settings, dropdown configuration, interpreted run logs, operating prompt, system prompt, developer comments, safety, evidence, user job, pain, and business objective.
- Static dashboard actions remain browser-local review packets only. Provider calls, raw transcript storage, durable writeback, deployment, backend queues, and live traces require explicit approval and a server/local bridge.
- Claude-Mem and Impeccable are candidate memory/design tools, while NVIDIA garak and NeMo Guardrails are candidate safety-evaluation tools. Treat them as reviewed references only until hook scope, storage, worker behavior, install path, and public/private boundaries are approved.
- No current local Claude/Codex task-observer skill was found. Use the project chat registry, live communication log, dashboard session events, and run notes as the safe observer layer until a specific tool is selected.

## OpenRouter Model Routing Memory - 2026-07-01

- OpenRouter remains disabled as a runtime provider until explicit approval and an approved local bridge or backend exists.
- The model-routing contract is now recorded in `project/config/model-routing.yaml` and explained in `project/reports/2026-07-01-openrouter-model-routing-plan.md`.
- The strategic pattern is a frontier council: strongest available Claude, Gemini, and OpenAI models are reserved for planning, long reasoning, strategy, architecture, public-claim review, and payment verdicts.
- Cheaper execution models such as Kimi, Qwen, Mistral, DeepSeek, GLM, Llama, Perplexity, MiniMax, Mercury, Grok, and Gemma are assigned only to bounded extraction, classification, drafting, code variants, source discovery, and other intermediate work.
- Execution-pool outputs must not self-approve public claims, memory promotion, outreach, pricing, architecture changes, or payment verdicts.
- Future activation must refresh OpenRouter model IDs, keep secrets server-side or in ignored local env, log model ID and cost metadata, enforce budget caps, and require public-safety plus human approval before external or memory writes.

## Yushchenko Model Efficiency Observer Memory - 2026-07-01

- Codex app automation `yushchenko-model-efficiency-observer` is active on a five-hour cadence.
- The observer writes public-safe Markdown reports under `project/runs/yushchenko-model-efficiency/`.
- Durable model-efficiency advice lives in `project/agents/model-efficiency-advice.md`.
- Open model-efficiency issues live in `project/agents/model-efficiency-issues.md`.
- The observer must report actual model/token/cost evidence only and must say "No active OpenRouter runtime evidence found" when OpenRouter has not been used.
- Telegram delivery is conditional on an approved sender outside the public repo; chat destinations, IDs, links, and tokens must not be stored in public files.
- A separate zero-cost local deterministic CrewAI proof ledger now exists under `project/runs/2026-07-02-crewai-level-3-proof/model-call-ledger.jsonl`. It is valid runtime evidence for the local proof path, but it is not OpenRouter evidence and must stay labeled that way.

## Daily Skill/RAG Retrospective Maintenance Memory - 2026-07-01

- Recurring public lanes now include dedicated SKILL contracts for:
  - nightly registry/hook update,
  - daily skill + RAG + knowledgebase retrospective.
- Recurring reviews must explicitly score:
  - used vs unused skills,
  - RAG source-boundary stability,
  - knowledgebase update impact,
  - and repeated inefficiency or drift patterns.
- For recurring maintenance and daily review, tools that repeatedly add no value are now blacklisted by default until an explicit override is approved.
- This lane should emit a low-friction no-op record when no useful state change exists, rather than forcing false-positive churn.
- The two scheduled lanes are now explicit in `agent-roster.yaml`:
  - `archflow_evening_skill_and_hook_update` for the 21:00 maintenance scope,
  - `daily_skill_rag_retrospective` for the 22:30 review scope.
- Repeating inefficient tool patterns are first captured in run summaries and moved to durable memory only if they persist across multiple cycles.

## Final Static Website And Dashboard Goal Memory - 2026-07-01

- Current public service goal: ArchFlow Automate should be presented as a source-backed PRD/ICP operating service for B2B SaaS product teams, not as a generic AI chatbot or unproven autonomous platform.
- The public website's job is to explain the offer clearly: approved sources become context digest, PRD, ICP evidence, task matrix, approval gates, and an agent-ready operating handoff.
- The public diagnostic and calculator are planning tools only. They can estimate rework/readiness and recommend the first package, but must not claim guaranteed ROI or validated demand.
- The dashboard's job is the operator/control layer: Jarvis command center, PRD/ICP service flow, reliable agent orchestra, proof/backlog visibility, generated data, and blocked runtime gates.
- Static delivery is allowed to be merge-ready when website, diagnostic, dashboard, generated data, run notes, Notion Links, and task states are aligned and public-safe.
- Future runtime layers remain separate gates: owner-device visual/voice acceptance, main promotion, Figma final baseline sync if promoted, Railway/backend, provider activation, live Nexus, durable writeback, autonomous writeback, and model-call cost logging.

## Dashboard Website Strategy QA Memory - 2026-07-01

- The latest QA/PM audit confirms the stable public site and dashboard routes return HTTP 200 for the static review scope.
- Notion task management now has `Agent Tags` for active agent and specialization tracking; use tags to distinguish QA, senior dev, PM, strategy review, frontend, dashboard, LangGraph, RAG KB, Notion, GitHub, Telegram, API runtime, and reviewer work.
- The Notion Links page should stay minimal: current public site, diagnostic, dashboard, dashboard data, review branch, PR create link, and gated-state notes only.
- Maxibook Telegram delivery remains To Do until TG-1/TG-2/TG-3 prove sender contract, redacted outbound template, dry-run/health check, and public-safe send audit.
- GitHub review branch matched local branch at `73c41ea` before the audit's local report artifacts; new audit files require a separate approved commit/push before GitHub again reflects every local artifact.

## Jarvis Dashboard ICP Task Consolidation Memory - 2026-07-02

- Current English goal: ArchFlow is an AI-native service that turns raw product-team material, including conversations, research, documents, decisions, notes, and backlog fragments, into production-ready PRDs in days rather than weeks through a connected knowledge-base engine and supervised multi-agent execution workflow.
- Current ICP: product teams in B2B SaaS companies, usually Series B-D, roughly 50-500 employees, often with 2-5 PMs, where the Director or VP of Product owns PRD quality, discovery-to-delivery speed, and cross-functional alignment.
- Current first offer: Product Discovery-to-Production PRD Pack. Expected outputs are source inventory, context digest, PRD, ICP/evidence cards where relevant, task matrix, acceptance criteria, decision log, risk/gap list, KB update packet, and approval-gated agent handoff.
- Jarvis dashboard MVP concept: Lane A is direct Jarvis chat/config/local packet control; Lane B is coordinator/executor supervision for PRD/ICP Flow, Agent Orchestra, QA, docs, reporting, and deployment sequencing.
- Current proof supports static/browser-local dashboard and website review only. Provider-backed Jarvis, Railway/backend, live Nexus/writeback, owner-device voice proof, Telegram delivery, model-call telemetry, vector retrieval, and production/Figma promotion remain gated.
- Task consolidation outcome: keep E1 active, E1.2 Review, E1.3 Review, E1.3.8 Review, dashboard E1.3.9 Review, access/security E1.3.10 Review, and JDB-8/JDB-9/JDB-10 Done only for static/browser-local scope.
- GloomyLord remains an internal visual/reporting sidecar. GloomyLord audience-pain, method-log, and planning-package rows should move or rename under E1.5/reporting to avoid collision with E1.3.9/E1.3.10 dashboard/security rows.
- Prompt 2 readiness: ready only for static/browser-local dashboard MVP implementation and proof. It is not approval for provider/backend/voice/writeback runtime activation.

## Jarvis Dashboard MVP Implementation Memory - 2026-07-02

- Screen 1 now exposes a PRD/ICP request surface, required output blocks, local packet fallback, and test-cycle gate references.
- Screen 2 now exposes task stages and editable browser-local role configuration panels for the named ArchFlow roles plus CrewAI role workers.
- Dashboard voice controls are explicit: mic, stop, cancel, timer, editable transcript preview, send transcript, browser playback, stop playback, and auto-speak. Raw audio and raw transcript persistence remain off by default.
- `services/jarvis-api/` is a provider-disabled FastAPI service contract with required endpoints, not a deployed or provider-backed runtime.
- `.env.example` and `services/jarvis-api/.env.example` are tracked placeholder examples; real env files remain blocked.
- `docs/tgapi.md` was removed after a Telegram-token-shaped value was detected outside env flow.
- OpenRouter remains disabled with a `5.00` USD daily cap and `1.99` USD run hard stop. Provider activation still requires owner approval, backend/local bridge, server-side secrets, fresh pricing, provider ledger proof, live budget guard, and expanded AF Review.
- CrewAI Level 3 remains `proof_passed_not_default_runtime`; it is not default runtime and not provider runtime.

## Hybrid RAG And Jarvis Readiness Memory - 2026-07-03

- LlamaIndex is now the bounded hybrid retrieval layer for the approved public corpus, with stable `doc_id`/`chunk_id`, source-path enforcement, lexical fallback, and local embedding adapter probing.
- The 20-query benchmark is the gate before full vector defaulting. A pass without vector availability proves fallback reliability, not vector readiness.
- Turbovec remains deferred until benchmark, stable chunk metadata, embedding dimensions, source filters, ignored local persistence, and lexical rollback are proven.
- Jarvis currently works for local and hosted provider-disabled review packets. Architecture 1 routes PRD/ICP service-output requests; Architecture 2 routes agent-control and workflow/knowledge-system requests.
- Provider-backed Jarvis, Railway always-on workers, live Nexus/writeback, raw audio storage, autonomous Notion/GitHub updates, and production promotion remain separate approval-gated lanes.
- NVIDIA RAG/NeMo skills are future evaluation candidates for guardrails, retriever evaluation, performance, and speech. They are not active in the current public RAG runtime.

## Cloud And KB Retrospective Memory - 2026-07-03

- Railway Jarvis is verified for the provider-disabled hosted review-packet baseline, including health, CORS, chat, PRD/ICP, agent-orchestra, role config, role-update candidate packets, voice text packets, and the meeting-test approval gate.
- Vercel production availability is a separate fact from Vercel production freshness. On this continuation, production loaded without browser errors but served older dashboard data than the current E1.7 review preview.
- Future agents must not claim "always-current cloud product" from API availability alone; production `data.json` freshness must be checked after pushes.
- E1.6 role-split KB should not be called substantive until each role lane contains actual reviewed notes. The collaborator lane now has a founder-note-derived brief; before this continuation it was mostly routing scaffolding.

## Vercel Production Cure Memory - 2026-07-03

- The public dashboard URL now points to the current Vercel production deployment and served regenerated July 3 dashboard data during the cure.
- Vercel and Railway Jarvis APIs are now guarded OpenRouter review-packet runtimes: `MODEL_PROVIDER=openrouter`, provider calls `0`, writeback `0`, and approved provider-route tests stop at `openrouter_api_key_missing`.
- Do not describe this as live provider-backed Jarvis until external OpenRouter key storage is explicitly approved, a budget ledger is active, and a low-cost provider call is recorded.
- Future Railway deploys for `services/jarvis-api` should use the service directory as the archive root; deploying from the wrong root can make Railway infer a static/Caddy app and crash because `uvicorn` is missing.
- Legacy Vercel cleanup is destructive and requires a separate owner-approved inventory before deleting old projects.
