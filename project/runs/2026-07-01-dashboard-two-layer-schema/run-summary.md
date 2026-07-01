# Run Summary: Two-Layer Dashboard Schema Control Panel

Date: 2026-07-01
Status: implemented, architecture reviewer approved

## Task

Make the dashboard comprehensible and operable for two separate jobs:

1. `(1) PRD/ICP Flow`: the externally showable service-product path from source context to PRD, evidence, ICP, demo package, and approved output.
2. `(2) Agent Orchestra`: the local reliable development/control system for Codex, LangGraph-style routing, WikiLLM, Graphify, safety review, run logs, approvals, and gated provider/backend actions.

## Answer First

The dashboard now has two separate block-schema screens, draggable/clickable nodes, and a large n8n-style node control panel covering inputs, outputs, connections, dropdown configuration, run history, prompts, comments, safety fields, and business-fit fields. It remains a static browser-local review surface: no provider calls, secrets, raw transcripts, deployment, or writeback are enabled.

## Outputs

- Updated `project/dashboard/app.js`.
- Updated `project/dashboard/styles.css`.
- Updated `project/dashboard/index.html`.
- Updated `project/dashboard/README.md`.
- Added this run record and the handout beside it.

## Dashboard Behavior

FACT: `#service` renders `(1) PRD/ICP Flow`.

FACT: `#schema` renders `(2) Agent Orchestra`.

FACT: Each graph has draggable nodes, connect mode, auto-layout, validation, queue/export packet actions, and node duplication/deletion.

FACT: Clicking a node opens a large control panel with:

- input ports and incoming connection summaries;
- final output, output ports, possible outputs, and output links;
- editable connection label/mode/condition settings;
- dropdowns for layer, provider, provider mode, execution mode, approval gate, memory target, retrieval scope, trace target, safety review, persistence, input connector, output connector, and run recorder;
- interpreted last-run log;
- operating prompt, system prompt, and requirements;
- description, developer comments, owned files, and covered questions;
- Jobs To Be Done, pain/risk, evidence, and business objective fields.

INTERPRETATION: The UI now makes the two paradigms explicit enough for operator use and review without mixing external product output with internal agent-control mechanics.

HYPOTHESIS: A future backend can convert exported node packets into LangGraph or queue jobs, but the static dashboard should keep that as a gated next step.

GAP: Runtime execution, durable writeback, provider calls, live traces, real browser/device voice proof, and deployment are still not implemented by this pass.

## Third-Party Tool Review

PUBLIC SOURCE REVIEW: Claude-Mem's public README describes persistent context across sessions through captured tool observations, semantic summaries, future context injection, lifecycle hooks, a worker service, SQLite storage, and vector search.

INTERPRETATION: Claude-Mem is potentially useful for Codex-style memory continuity, but it is not safe as a default ArchFlow runtime layer until privacy exclusions, hook scope, worker behavior, storage location, and public/private boundaries are reviewed.

PUBLIC SOURCE REVIEW: Impeccable's public README describes design guidance for AI coding agents, a Codex-compatible skill/hook path, and deterministic design detector rules.

INTERPRETATION: Impeccable is applicable as a UI critique/polish method for the dashboard, but its hook installation must stay explicit and approved. This pass used the already available local skill guidance only; it did not install or activate the GitHub package.

PUBLIC SOURCE REVIEW: NVIDIA garak is documented as an LLM vulnerability scanner, and NeMo Guardrails documents guardrail mechanisms plus garak-based vulnerability scanning examples.

INTERPRETATION: These are the right future safety-evaluation references for model/provider and guardrail work. They were not installed or run here because this dashboard pass does not activate an LLM endpoint and network/runtime installation was not approved.

GAP: No clearly applicable local Claude/Codex "task observer" skill was found. The current safe observer is the project chat registry, live communication log, dashboard session events, and run notes until a specific observer tool is selected and reviewed.

Sources reviewed:

- `https://github.com/thedotmack/claude-mem`
- `https://github.com/pbakaus/impeccable`
- `https://github.com/NVIDIA/garak`
- `https://docs.nvidia.com/nemo/guardrails/latest/evaluation/llm-vulnerability-scanning`
- `https://github.com/NVIDIA-NeMo/Guardrails`

## Checks

- Pass: `node --check project/dashboard/app.js`
- Pass: `git diff --check -- project/dashboard/app.js project/dashboard/styles.css project/dashboard/index.html project/dashboard/README.md`
- Pass: schema static smoke over both default graphs.
- Pass: `python3 project/scripts/generate-dashboard-data.py`
- Pass: dashboard JSON parse.
- Pass: `python3 scripts/public_safety_scan.py`
- Pass: `project/local/venv/bin/python project/scripts/validate-workflows.py`
- Pass: `python3 project/scripts/pre-push-runtime-guard.py`
- Pass with fixes: implementation reviewer found queue/save, schema storage, connect-mode, URL, and panel-tab issues; fixes were applied.
- Pass with fixes: UX reviewer found mobile graph, local-edit labeling, nav-label, public-label, and node-summary issues; fixes were applied or bounded.
- Fail then resolved for dashboard scope: safety reviewer found repo-wide validation drift from the active model-routing lane, screenshot artifacts, generated deployment URLs, live-log labels, and under-sourced third-party claims. Validation now passes, screenshot artifacts were removed, dashboard generated data redacts deployment URLs and excludes the live communication log, and public third-party sources are listed above.

## Reviewer Gate

FACT: The parallel architecture reviewer approved this dashboard/UI pass through the project chat-file workflow on 2026-07-01.

INTERPRETATION: No more dashboard design help is needed for this pass. Remaining gates are merge/deploy/runtime/provider/writeback decisions, not UI-review blockers.

Confidence: medium-high for static UI implementation; medium for full operating-system readiness because runtime/writeback/provider gates remain future work.
