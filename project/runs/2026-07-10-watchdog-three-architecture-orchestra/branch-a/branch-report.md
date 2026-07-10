# Branch A Report - Company Development Agent Architecture

Status: review complete; documentation and configuration hardening only. No provider call, deployment, hosted-endpoint check, external writeback, commit, or push occurred.

GAP - Luna model selection unavailable

## Merge Recommendation

`revise`

The Branch A changes are public-safe and retain the required role, maker-checker, approval, provider, deployment, and writeback gates. The recommendation remains conservative because current hosted/provider freshness, a canonical provider-call ledger, and dependency-backed workflow/API checks are not proven in this run. This is not authorization to perform those actions.

## Files Changed Or Proposed

Branch A-owned architecture/configuration changes in the current diff:

- `AGENTS.md`
- `project/operating-rules.md`
- `project/agentic-stack.md`
- `project/context/cag-core.yaml`
- `project/agents/agent-roster.yaml`
- `project/agents/skills-by-agent.md`
- `project/agents/skills-governance.md`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `services/jarvis-api/README.md`

Branch A evidence and planning artifacts:

- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/planner-evidence.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/executor-evidence.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/verifier-evidence.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/safety-review-evidence.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/official-source-evidence.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/railway-prerequisite-packet.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/consistency-scan.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/branch-report.md`

No unowned inherited or concurrent worktree changes are attributed to Branch A.

## Diff Summary

- Replaces hard runtime-name authority wording with bounded role contracts. Compatible runtimes may fulfil a role only under that role's task contract, evidence requirements, forbidden actions, and maker-checker separation.
- Retains the planned watchdog as non-executing and prohibits high-risk self-approval; retains Codex as the current local execution and final-integration binding without treating that binding as provider, deployment, or writeback authority.
- Adds an architecture-stage reliability matrix that separates static/browser-local packets, provider-disabled Jarvis contracts, future Railway preparation, and activation-gated OpenRouter routing from current hosted or always-online proof.
- Clarifies dashboard and Jarvis connection labels, historical Railway baseline language, disabled voice mode, and deployment-time healthchecks as distinct from continuous monitoring.
- Adds activation-time OpenRouter model-selection, cost/usage capture, ledger, observer-review, independent safety-review, and owner-approval requirements. No model, price, credential, budget balance, or provider call is asserted.
- Records a duplicate-skill and hook-governance audit result without adding, removing, or editing a skill or hook.

## Checks And Results

| Check | Result | Boundary |
|---|---|---|
| `git diff --check` | Pass | No whitespace errors in the current diff. |
| Ruby YAML parse of `cag-core.yaml`, `agent-roster.yaml`, `langgraph-controller.yaml`, and `crewai-crew.yaml` | Pass | Syntax only; no workflow runtime executed. |
| `python3 scripts/public_safety_scan.py` | Pass | Current repository public-safety scan. |
| Python syntax compilation of Jarvis/API modules | Pass (verifier evidence) | Syntax only; no server or provider call. |
| Railway JSON parse | Pass (verifier evidence) | JSON syntax only. |
| Dependency-backed workflow validation | Blocked | Active interpreter lacks the YAML dependency; no installation was authorized. |
| Jarvis API contract smoke | Blocked | Active interpreter lacks FastAPI and no approved environment was available. |

## Evidence Sources

Role evidence: `planner-evidence.md`, `executor-evidence.md`, `verifier-evidence.md`, and `safety-review-evidence.md` in this folder; the governing scope and stop conditions are in `../branch-task-contracts.md`, `../discovery-and-integration-plan.md`, and `../context-capsule.json`.

The source-review packet records official documentation checked on 2026-07-10: [OpenRouter Models API](https://openrouter.ai/docs/guides/overview/models), [OpenRouter API overview](https://openrouter.ai/docs/api/reference/overview), [OpenRouter limits](https://openrouter.ai/docs/api/reference/limits), [Railway healthchecks](https://docs.railway.com/deployments/healthchecks), [Railway variables](https://docs.railway.com/variables), and [Railway build and deploy](https://docs.railway.com/build-deploy). These sources support activation and verification gates only; they do not establish an ArchFlow account, deployment, selected model, remaining budget, or service availability.

## Consistency-Scan Status

Complete. The scan covered `AGENTS.md`, `project/operating-rules.md`, `project/agentic-stack.md`, `project/context/cag-core.yaml`, `project/agents/agent-roster.yaml`, `project/agents/skills-by-agent.md`, `project/workflows/langgraph-controller.yaml`, and `project/workflows/crewai-crew.yaml`. It found that existing prohibitions were retained and added role/runtime wording where a current named binding could otherwise be read as permanent authority. See `consistency-scan.md` for FACT, INTERPRETATION, and GAP statements.

## Blockers And Next Safe Action

- No current hosted Jarvis/Railway health, CORS, auth, logs, persistence, recovery, or continuous-monitoring evidence exists in this run.
- No OpenRouter model selection, provider call, current price/availability proof, budget consumption, or canonical provider-backed ledger/readback exists in this run.
- Dependency-backed workflow and API smoke checks remain unavailable without an approved dependency environment.
- The next safe action is integrator review of this documentation/configuration diff, preserving the stated gaps and separately authorizing any future runtime validation only with a bounded, owner-approved evidence packet.
