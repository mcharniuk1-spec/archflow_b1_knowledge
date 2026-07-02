# Log

## 2026-06-25

- Public project was created and published.
- Codex was set as primary operator layer.
- Ollama was connected as local model execution layer.
- Qwythos was verified as present and generating text.
- LangSmith tracing env was configured with project ID `masked_langsmith_project_id`.
- Public WikiLLM structure was created inside the repository.
- Educational setup summary and agent plan were added under `project/reports/`.
- Integrated knowledge-operation plan and Git pre-push public-safety hook were added.
- LangSmith SDK was installed locally in ignored runtime and a sanitized smoke trace was submitted.
- Phase 2 local dashboard was added for read-only monitoring of WikiLLM, LangGraph, CrewAI, LlamaIndex, LangSmith, env/config, and project activity.

## 2026-06-26

- LangGraph was installed in the project local runtime and a sanitized smoke workflow passed with approved status.
- Pydantic and PyYAML workflow validation was added for workflow and routing configuration.
- LlamaIndex was installed and an approved-public-corpus retrieval proof returned 58 documents and source-path results.
- CrewAI was installed and a config/import check was added without running LLM tasks.
- CrewAI guard execution was bounded to ignored project-local runtime storage with telemetry/tracking disabled.
- The saved `archflow-e1-runtime-guard` skill was added and connected to the Git pre-push hook.
- The pre-push runtime guard passed: workflow validation, LangGraph smoke, LlamaIndex corpus, and CrewAI config.
- A sanitized E1.2 preparation packet was created under `project/runs/2026-06-26-june24-next-steps-proof/`.
- A reusable `task-handout` skill was added, and the E1.1/E1.2 execution received an agent-readable handout with human summary, continuation prompt, decisions, validation, and next actions.
- The `task-handout` skill was connected to a prompt hook and workflow rule for prompts or executions that use one or more agents or solve one or more subtasks.
- E1.2 full-test graph ran and produced the PRD, streaming report, system report, task matrix, KB update, review report, and agent handout.
- Tracked public files now mask operational project identifiers.
- The approved LlamaIndex corpus now explicitly includes public WikiLLM files under `wiki/`.
- E1.2 Notion status sync prepared the owner next-steps document, report links, and evidence-backed state map: E1.2 parent in Review, E1.2.1 through E1.2.7 Done, and E1.3 ready after owner acceptance.
- The evening skill refresh corrected stale current-state proof-run wording in `project/agentic-stack.md`, confirmed the public skill registries already matched the configured skills, and recorded the automation pass under `project/runs/` and `wiki/runs/`.

## 2026-06-27

- The evening skill audit confirmed the public skill registries still matched the current saved skills and workflow setup.
- Lightweight validation found non-ASCII generated glyphs in `graphify-out/GRAPH_REPORT.md`; the report was normalized to ASCII-safe punctuation and the maintenance pass was recorded under `project/runs/` and `wiki/runs/`.

## 2026-06-28

- The evening status refresh confirmed the public skill registries still matched the current saved skills and workflow setup, so no registry edits were needed.
- The maintenance pass refreshed stale current-state wording in the June 25 setup and dashboard reports so they now match the saved runtime validation and proof artifacts.
- `project/dashboard/data.json` was regenerated after the report refresh, and lightweight YAML, public-safety, ASCII, and ignored-path checks passed on the public project scope.

## 2026-06-29

- The June 29 tool and market reports were integrated into the current E1-E7 plan.
- Loop Engineering was added as the L1 report-only operating contract under `project/loops/`.
- `project/workflows/market-research-engine.yaml` was added for E2 account evidence, signal extraction, ICP scoring, role verification, and reviewed outreach handoff.
- The agent roster now includes AF Research and AF Copy roles.
- Cognee, turbovec, and Mistral were documented as gated future layers, not activated runtime dependencies.
- The plan initially used a broader service-company hypothesis, then the partner answer corrected the current first ICP to product teams inside B2B SaaS scaleups and reframed the offer as a Product Discovery-to-Production PRD Pack.
- Product-team ICP correction was applied to the project plan, market engine, workflow YAML, dashboard data, and selected Notion E1/E2/E3/E6 rows.
- Targeted Notion E2 updates were applied after product-owner verification: E2 parent and related E2.1/E2.2/E2.3/E2.5 pages received append-only notes, and three Backlog research tasks were added.

## 2026-06-30

- Executed the Onyx/live-dashboard/voice/hosting planning baseline by creating private Notion tasks, adding the public `outquestions` skill, updating the public skill registries, and recording a public run and decision note.
- The plan keeps ArchFlow as the workflow brain, starts dashboard hosting with a static Vercel path, reserves Railway for live API/worker/voice services, and requires decision-question closeouts after substantial runs.
- 2026-06-30: Executed E1.3 public-safe KB writeback/readback proof, added dashboard-derived E1.3 gate status, and started E1.5 as a public-reporting gate with GloomyLord kept internal by default.
- 2026-06-30: Added the Jarvis-first dashboard shell for hidden-link Vercel preview, added E1.5 content templates, and recorded the Vercel/Railway/static-write boundary.
- The updated evening skill-and-hook audit confirmed no public registry drift, proved the prompt hook still triggers for subtask maintenance, normalized tracked non-ASCII punctuation in `graphify-out/GRAPH_REPORT.md` and `graphify-out/graph.html`, and the final combined-tree public-safety scan passed after the dashboard/Jarvis handoff was finalized.
- The June 30 integrator review approved the combined dashboard/Jarvis, content-template, graphify normalization, and hook-audit file set for Git review while keeping production deployment cleanup as a separate owner-approved Vercel task.
- The dashboard reliability sync recorded the verified protected preview, updated dashboard operating instructions, refreshed the public KB/log, regenerated dashboard data, and kept Railway, OpenAI/Mistral runtime, live Codex bridge, uploads, voice persistence, and writeback behind explicit approval gates.

## 2026-07-01

- Added `project/live/communication/` as the shared active communication channel for ArchFlow public project agents, including the current notice, message template, pattern-change log, live communication log, and copy-ready system prompt append.
- Updated operating rules, agent routing, and the agent roster so parallel agents announce intent, claim files, coordinate conflicts, and report completion before relying on run handouts.
- Transferred the final June 30 LangGraph handoff into the ArchFlow public knowledge layer: `d18fc55` is the accepted static/browser-local dashboard review slice, JDB-8 is Done, JDB-7 is Review, E1.3.9 remains Review, Telegram was not sent, and Railway/provider-backed writeback remains gated.
- Cleaned provider-key state by moving OpenRouter and Mistral into ignored local env storage, removing the Markdown secret source, removing the June 30 OpenAI local key file, and documenting that static browser code must not call providers directly.
- Updated the dashboard branch with separate `(1) PRD/ICP Flow` and `(2) Agent Orchestra` schema screens plus node-level controls for prompts, comments, inputs, outputs, config, run history, and output links.
- Added the July 1 current-state report, two-paradigm execution plan, analytical-writing framework prompt, project run note, and WikiLLM run note.
- Integrated parallel subagent review findings by fixing model-routing schema drift, correcting dashboard voice permission wording, adding keyboard/modal accessibility for schema nodes, tightening the writing framework, clarifying E3/E4 status vocabulary, and recording that Git commit/push/merge/deploy remain pending.
- Hardened the two-layer dashboard schema with draggable/clickable blocks, large node control panels, connection editors, dropdown configuration for every node, explicit static/offline boundaries, and a public-safe third-party tool review.
- Added the OpenRouter model-routing contract: frontier Claude/Gemini/OpenAI models are reserved for planning, long reasoning, strategy, and review, while cheaper models handle bounded execution under maker/checker, budget, reliability, and public-safety gates.
- Added the Yushchenko model-efficiency observer automation on a five-hour cadence, with public-safe Markdown reports, separate advice and issue registers, live-agent notifications, and a guarded Telegram-summary rule that requires an approved sender outside the public repo.
- Added the Messi coordination review: the July 1 dashboard/model-routing/Notion work is directionally correct but should freeze before more implementation; open blockers are active file claims, missing screenshot evidence referenced by a run note, and pending modal/mobile QA. A reported duplicate top-level YAML key was rechecked and is not present in the current shared workspace.
- Added `project/scripts/dashboard-static-smoke.py` as the reusable rendered-route smoke test for dashboard/Jarvis UI changes; it verifies `#jarvis`, `#history`, `#service`, `#schema`, `#config`, `#plan`, and the two node-panel deep links without provider calls or writeback.
- Pushed review branch `review-jarvis-agentbrowser-blockschema-20260630` at `5efd281` for July 1 dashboard orchestration, model-routing, live-agent communication, planning, and smoke-test stabilization; merge/deploy/runtime activation remain gated.

## 2026-07-02

- The Yushchenko observer published a new public-safe model-efficiency report from local evidence only. No active OpenRouter runtime evidence was found, token and cost logs are still absent, and Telegram delivery was skipped because an approved sender was unavailable.
- The CrewAI direct runtime proof also added a zero-cost local deterministic model-call ledger. That ledger is useful for bounded local runtime verification, but it must not be confused with provider-backed OpenRouter evidence.
- Hardened recurring public execution contracts for the two scheduled maintenance lanes:
  - ArchFlow public evening skill and hook update,
  - Daily Skill Retrospective and RAG Knowledge Review.
  Added dedicated SKILL contracts, explicit no-op-safe lane scope, and recurring inefficiency blacklists so each run reviews not only functional output but also tool relevance and waste.
- Split the two scheduled maintenance lane contracts in `agent-roster.yaml` into separate scheduled blocks (`21:00` and `22:30`) and added explicit long-term inefficiency carry-forward to wiki memory surfaces for durable global-knowledge governance.
- Completed the final Jesus integration and Notion closeout for the static website/dashboard lane: Messi handoff reviewed, mobile homepage readability fixed, Notion Links and task rows refreshed to branch-head evidence, dashboard route/static data verified, and runtime/provider/Railway/Nexus/writeback claims kept gated.
- Completed the dashboard/website/strategy QA audit: stable public site and dashboard routes returned HTTP 200, Notion task rows received `Agent Tags`, the Links page was reduced to current essential public/GitHub/dashboard pointers, Maxibook Telegram follow-up tasks TG-1 through TG-3 were created, and the public-safe PDF/handout were saved under `project/runs/2026-07-01-dashboard-website-strategy-qa/`.
- Completed the 22:30 daily skill/RAG retrospective: the 21:00 registry lane stayed separate, `task-handout` and daily review skills were useful, and open proof gaps were consolidated for priority-task runtime, model-call ledger, Telegram sender, Nexus/writeback, and backend/provider claims.
- Rerun the Yushchenko model-efficiency observer at 11:12 EEST; no active runtime, tokens, cost, or context-window data were logged for VLLM/remote provider calls, while two short local smoke checks each failed twice due `127.0.0.1:11434` being unreachable.
- Completed the Jarvis dashboard ICP task consolidation block without implementation. The run created the strategic report, E1 task consolidation table, Notion update package, and run handout. It saved the current English goal, ICP, two-lane dashboard concept, and task consolidation outcome into public WikiLLM memory. Prompt 2 is ready only for static/browser-local dashboard MVP implementation; backend/provider/voice/writeback activation remains gated.
- Completed Prompt 1.2 dashboard execution architecture. The run defined the PRD/ICP Flow and Agent Orchestra execution contracts, mapped Level 1 configured roles, Level 2 LangGraph-wrapped target execution, and blocked Level 3 direct CrewAI runtime, then added OpenRouter disabled-state behavior and a required model-call ledger gate before any future provider activation.
- Updated the Prompt 1.2 execution contract with the owner OpenRouter budget rule: 5.00 USD per day and always under 2.00 USD per run. Clarified that Level 3 direct CrewAI runtime is blocked only because direct runtime proof is missing, and documented the proof ladder needed to unblock it safely.
- Completed the CrewAI Level 3 proof pass. A tiny public-safe PRD/ICP fixture ran through direct CrewAI with a deterministic local LLM adapter, wrote a model-call ledger and budget guard, spent 0.00 USD, made zero provider calls and zero writeback calls, passed AF Review and validation, and promoted Level 3 only to `proof_passed_not_default_runtime`.
## 2026-07-01

- The Yushchenko model-efficiency observer completed a new public-safe report and again found no active OpenRouter runtime evidence.
- The project still needs a canonical model-call ledger before true token and cost efficiency can be measured.
## 2026-07-02 - Jarvis dashboard MVP implementation

FACT:
- Prompt 2 implementation updated the static dashboard with Screen 1 PRD/ICP request/output blocks, Screen 2 role configuration panels, explicit voice controls, block-schema zoom, and fixed bottom composer behavior.
- A provider-disabled FastAPI service contract was added under `services/jarvis-api/`.
- Env examples now provide placeholders only.
- `docs/tgapi.md` was removed after a Telegram-token-shaped value was detected outside env flow.
- OpenRouter remains disabled with a `5.00` USD daily cap and `1.99` USD run hard stop.
- CrewAI Level 3 remains `proof_passed_not_default_runtime`.

INTERPRETATION:
- The dashboard is now a stronger static/browser-local control surface, not a live provider/backend/writeback runtime.

GAP:
- FastAPI dependencies are not installed in the current local runtime.
- Full PRD/ICP test cycle, dashboard-driven Notion writeback, Telegram send, Railway deployment, provider activation, and default CrewAI promotion remain approval-gated.

Outputs:
- `project/reports/2026-07-02-jarvis-dashboard-mvp-layer-report.md`
- `project/runs/2026-07-02-jarvis-dashboard-mvp-implementation/agent-handout.md`
- `wiki/runs/2026-07-02-jarvis-dashboard-mvp-implementation.md`
