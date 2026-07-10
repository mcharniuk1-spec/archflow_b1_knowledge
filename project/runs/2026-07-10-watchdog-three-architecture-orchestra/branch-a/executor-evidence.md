# Branch A Executor Evidence

Status: patch plan only; no shared architecture file was edited by this role.

## Scope And Execution Boundary

This executor reviewed the Branch A contract, current architecture/configuration, Jarvis API contract, dashboard manual, provider policy, historical Railway plan, and skills-governance policy. The review identifies a bounded implementation plan for the Branch A supervisor. It does not activate a provider, start a service, deploy, publish, push, mutate an external system, or make a network call.

GAP - Luna model selection unavailable

No external calls or external actions occurred.

## Evidence Observed

### FACT

- `project/agentic-stack.md` names Hermes as a planned non-executing watchdog, Codex as the local executor and approval boundary, and describes Level 1 as active, Level 2 as a target, and Level 3 only as deterministic fixture proof rather than the default runtime.
- `project/workflows/langgraph-controller.yaml` already separates a planned Hermes controller, worker execution, AF Review, merge, handoff, and an integrator decision; its current configuration still binds several nodes to agent-runtime names.
- `docs/dashboard-operating-manual.md` labels the dashboard as static/browser-local by default and says provider calls, Railway deployment, writeback, and publication require separate proof and approval.
- `services/jarvis-api/app.py` defaults `MODEL_PROVIDER` to `none`, blocks OpenRouter until both approvals, a server-side key, an explicit model, and budget configuration exist, but represents `actual_spend_usd` as `0.00` and has no durable provider-call ledger.
- `project/agents/model-efficiency-issues.md` independently records that an OpenRouter runtime and canonical provider ledger are not proven, and that model IDs and pricing can drift.
- `project/reports/2026-07-03-railway-dashboard-jarvis-cloud-setup-test-plan.md` is dated historical evidence. Its `production-current` wording cannot establish current hosted freshness for this run.
- `project/agents/skills-governance.md` requires a duplicate-skill and hook-governance audit before relevant edits; it prohibits auto-creating skills or hooks from a reminder alone.

### INTERPRETATION

The architecture should be expressed as role contracts fulfilled by compatible runtimes, not as a permanent one-name-to-one-runtime division. That correction must preserve the stricter invariant: a watchdog does not execute; a maker cannot approve its own high-risk output; external-action roles need explicit approval and current proof.

### GAP

- No current safe hosted health/CORS/endpoint evidence was collected in this executor pass.
- No current OpenRouter model-list or pricing evidence was collected; exact model and price claims must therefore remain activation-time checks.
- No current Railway project, service, environment, secret, deployment, or rollback proof was collected.
- A persistent provider-call ledger and readback check are absent from the reviewed contract.

## Concrete Patch Plan

| File | Section or symbol | Old wording/problem | Replacement intent |
|---|---|---|---|
| `project/agentic-stack.md` | Layer Decision and Tool Responsibilities | The diagram and table imply named products/agents are the only holders of a role; the separate Hermes prohibition can be misread as a hard runtime split. | Add a role-contract layer before runtime selection: watchdog, executor, verifier, safety reviewer, integrator, and external-action preparer. State that a compatible runtime may fulfil one role for a bounded task, while the role's allowed actions, evidence, independence, and approval gates remain controlling. Retain Hermes's non-executing limitation when Hermes fulfils the watchdog role. |
| `project/agentic-stack.md` | Runtime Levels | The table distinguishes levels but does not state stage-by-stage proof requirements or clearly distinguish historical hosted proof from live freshness. | Replace or extend the table with a reliability matrix: configured role contract; local/static review packets; deterministic fixture; hosted provider-disabled API; server-side provider call; external writeback. For each stage record status, allowed side effects, minimum evidence, and promotion gate. Label hosted evidence `historical unless checked in the current run`. |
| `project/agentic-stack.md` | Screen (2): Agent Orchestra and Stop Rules | Named roles exist, but runtime compatibility and maker/checker independence are not shown beside the route. | Add a role-to-runtime compatibility and separation table. Require an executor artifact, independent verifier evidence, independent safety-review evidence, integrator decision, and owner approval for external-action preparation. Clarify that the dashboard records packets and gates; it is neither evidence of an always-online controller nor authority to alter source/external state. |
| `project/workflows/langgraph-controller.yaml` | State schema, nodes, `screen_contracts` | `owner_agent` values mix roles and runtime identities, and existing status labels can be read as current runtime availability. | Introduce typed fields such as `role`, `compatible_runtime`, `runtime_status`, `evidence_refs`, `independent_reviewer_required`, and `external_action_gate`. Keep the current controller as a contract where not runtime-proven. Require every role assignment to resolve to one compatible runtime only at execution time, with evidence captured in the run packet. |
| `project/workflows/langgraph-controller.yaml` | `agent_orchestra` route and `optionally_prepare_git_notion_deploy_actions` | The route reaches preparation for external actions without an explicit merge-readiness packet in the same route. | Add a pre-merge node that checks allowed-file scope, inherited-diff preservation, role evidence completeness, public safety, and `git diff --check`; add explicit stop states for missing current hosted proof, missing provider ledger, ambiguous target/schema, or absent owner approval. Keep external actions as preparation-only. |
| `project/context/cag-core.yaml` | Roles, gated claims, and runtime inputs | CAG context should provide current gates to every compatible runtime, not just named runtime identities. | Add the role contract and reliability-matrix references, plus required claims labels: `configured`, `historical_evidence`, `current_run_verified`, `blocked`, and `approval_gated`. Require source-path evidence for every promoted runtime claim. |
| `project/provider-setup.md` | OpenRouter / Mistral Status | The future route lists high-level gates but does not assign the Yushchenko observer a non-executing policy or distinguish configuration from spend evidence. | Add an OpenRouter activation packet: fresh official model/pricing check, selected model rationale, sanitized input class, server-side secret confirmation, run/daily caps, hard stop, retry/timeout behavior, ledger write/readback, AF Review, and owner approval. State Yushchenko is an observer that audits selection and ledger evidence, cannot activate a provider, and must report unknown cost as unknown. |
| `project/config/model-routing.yaml` | `openrouter_cloud`, `cloud_api`, and `routing` | The file has activation requirements but lacks an explicit observer decision record and a canonical cost/usage contract. | Add a model-selection record schema with official source URL, observed-at time, model ID, pricing snapshot reference, task class, fallback, and approval status. Add a ledger schema reference containing request ID, runtime, model, input class, token fields when returned, cost estimate, hard-stop result, and review status. Do not set a static model ID or price. |
| `project/agents/agent-roster.yaml` | Yushchenko entry and role registry | `provider: codex_automation`, `schedule`, and output targets can be misread as an independent always-online provider/model controller. | Describe Yushchenko as a scheduled-or-manual observer role only when its configured runtime is available; require a run artifact and report `not run` otherwise. Add explicit prohibited actions: provider activation, budget override, secret access, deployment, and writeback. Preserve its current reporting role. |
| `project/agents/model-efficiency-advice.md` and `project/agents/model-efficiency-issues.md` | Model-routing advice and open gaps | The issue list correctly identifies gaps but needs a single activation acceptance set aligned with the API. | Add one canonical activation checklist and map existing issues to it: fresh official model/pricing evidence, approved secret boundary, ledger persistence/readback, cap enforcement, output review, and owner approval. Keep local deterministic proof ledgers separate from provider-backed ledgers. |
| `services/jarvis-api/app.py` | `budget_state`, `provider_ready`, `provider_packet`, `runtime_packet` | `actual_spend_usd` is always zero and `default_runtime` can read as an active guarded OpenRouter default even when the provider is disabled. | Preserve `MODEL_PROVIDER=none` as default. Replace simulated spend language with `ledger_unavailable` until a guarded server-side ledger implementation and readback test exist; make the runtime label `provider_disabled_review_packet` unless a call is actually executed and logged. Require a ledger write/readback before returning a provider-success packet. Do not implement activation without an approved deployment/secret environment. |
| `services/jarvis-api/README.md` | Current state and Railway deploy section | The historical `Railway E1.7 baseline passed` statement is close to a current-hosted claim, and the deploy command could be mistaken for authorization. | Change to `historical 2026-07-03 evidence; current availability unverified in this run`. Add a Railway prerequisite packet: approved target, build/start/health proof, CORS proof, provider-disabled default proof, secret boundary, observability, rollback plan, owner approval, and public-safe result record. Mark the command as documentation only. |
| `docs/dashboard-operating-manual.md` | Purpose, Jarvis modes, and hosted-runtime wording | The manual mixes local/static browser behavior with historical hosted API behavior, which risks an always-online implication. | Define dashboard states explicitly: static/local packet UI; provider-disabled API reachable only when current health evidence exists; provider-enabled route approval-gated; external actions disabled. Require the UI to render the evidence timestamp/status and use `unknown` when no current check exists. |
| `project/agents/skills-governance.md` | Hook Governance and Add-Skill Checklist | Governance is strong but does not prescribe a recorded audit result for a no-change review. | Add a `governance audit record` requirement before skill/hook edits: candidate, duplicate check, existing-skill coverage, hook authority check, file scope, reviewer, and outcome. Specify `NO_UPDATE` when no reusable gap is demonstrated; hooks remain reminders only. |
| `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/` | Branch evidence and handout | Branch review needs an integration-ready, evidence-complete merge record. | Add planner, verifier, safety-review, and branch-report evidence beside the final `agent-handout.md`; the supervisor should link all role evidence, annotate current versus historical claims, list exact diffs/checks, preserve inherited edits, and issue `approve`, `revise`, or `block`. |

## Recommended Implementation Sequence

1. Run the duplicate-skill and hook-governance audit before changing `project/agents/skills-governance.md`, skill mappings, or hooks; do not add a skill unless the audit demonstrates a reusable uncovered method.
2. Establish the role-contract and reliability-matrix language in `project/agentic-stack.md`, `project/workflows/langgraph-controller.yaml`, and `project/context/cag-core.yaml` first.
3. Align provider, observer, and API labels without changing the default-disabled runtime or activating a service.
4. Correct dashboard and Railway documentation to distinguish historical evidence from current-run verification and add a prerequisite packet rather than a deploy action.
5. Run parses and focused safety checks, then use independent verifier and safety-review evidence before the integrator makes a merge recommendation.

## Validation Plan For The Supervisor

- Parse each changed YAML file with a safe YAML parser.
- Run `python3 -m py_compile services/jarvis-api/app.py` if that file changes.
- Run `python3 -m py_compile project/scripts/public_safety_scan.py` and `python3 project/scripts/public_safety_scan.py` after all edits.
- Run `git diff --check` and a focused search for unsupported `always online`, `production-current`, `active OpenRouter`, and unmasked secret patterns.
- If API labels change, execute only an in-process/provider-disabled smoke that proves no outbound provider call; do not start a network-facing service.
- Treat any current hosted check as separate, owner-approved work. Without it, preserve `historical` or `unverified` labels.

## Evidence Sources

- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-task-contracts.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/discovery-and-integration-plan.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/context-capsule.json`
- `project/agentic-stack.md`
- `project/workflows/langgraph-controller.yaml`
- `project/provider-setup.md`
- `project/config/model-routing.yaml`
- `project/agents/skills-governance.md`
- `project/agents/agent-roster.yaml`
- `project/agents/model-efficiency-issues.md`
- `docs/dashboard-operating-manual.md`
- `services/jarvis-api/app.py`
- `services/jarvis-api/README.md`
- `project/reports/2026-07-03-railway-dashboard-jarvis-cloud-setup-test-plan.md`

## Executor Conclusion

The proposed patch is safe to implement within Branch A only if it maintains provider-disabled defaults, separates historical from current hosted evidence, makes runtime compatibility subordinate to role safety, and leaves all external side effects gated. No production-freshness, provider-spend, always-online, or deployment claim should be promoted without a separate current safe check.
