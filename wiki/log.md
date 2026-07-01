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
