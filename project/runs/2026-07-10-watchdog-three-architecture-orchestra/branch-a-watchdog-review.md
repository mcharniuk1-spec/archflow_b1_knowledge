# Branch A Watchdog Review

Decision: **approve documentation/configuration integration; block runtime and external actions**.

## Evidence Reviewed

- Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter evidence.
- Role/runtime consistency scan across governing, CAG, roster, skills, LangGraph, and CrewAI contracts.
- Official OpenRouter and Railway source packet plus Railway prerequisite packet.
- Branch report, handout, changed-file diff, and branch checks.

## Acceptance Findings

- Current governing/configuration files now make authority derive from bounded roles rather than permanent runtime names.
- Watchdog non-execution, maker-checker separation, independent safety review, and high-risk self-approval prohibition remain intact.
- Jarvis/dashboard, Railway, and OpenRouter text clearly separates historical/configuration evidence from current hosted, provider, budget, deployment, or always-online proof.
- OpenRouter selection remains activation-time and requires current model/capability/pricing evidence, cost/usage ledger, observer review, independent safety review, and owner approval.
- Railway healthcheck evidence is correctly separated from continuous monitoring and availability proof.
- No new or duplicate skill/hook was introduced.

## Branch Recommendation Handling

Branch A returned `revise` because current runtime/provider evidence and dependency-backed checks were unavailable in its isolated worktree. The owner contract allows external actions to remain explicitly blocked with evidence. The watchdog therefore accepts the safe documentation/configuration slice, preserves the runtime blockers, and requires the main project environment to run dependency-backed checks after merge.

## Merge Boundary

Integrate only the twelve changed governing/configuration files listed in the Branch A report plus the `branch-a/` evidence folder. Exclude the branch-local communication-log copy, generated dashboard data, inherited handoff changes, `.codex/`, and common supervisor-owned run files.
