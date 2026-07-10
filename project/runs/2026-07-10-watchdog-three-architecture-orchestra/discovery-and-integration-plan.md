# Discovery And Integration Plan

Status: execution authorized; external side effects remain gated.

## Current State

The public repo contains a pushed Founder Meeting v2/CAG-RAG architecture baseline and a later conservative integration review. The current worktree also contains uncommitted owner-directed corrections to the watchdog continuation packet. Those corrections are treated as existing input and must be preserved.

The broader planning package was inspected read-only. Its durable ideas are already largely present in the public repo, while its older 90/10 content ratio and hard runtime-name division are superseded by the current 70/20/10 ratio and role-based orchestration instruction.

## Branch Plan

1. Branch A owns internal company-development architecture, runtime claims, model routing, deployment gates, role/skill governance, and branch-review mechanics.
2. Branch B owns the client-facing PRD/ICP delivery product, current market/competitor evidence, delivery methodology, E1-E7 updates, and Notion planning packet.
3. Branch C owns the content-agent architecture, public-source policy, planning/writing/design/QA roles, feedback loop, 70/20/10 plan, and public-safe visual specifications.

The branch scopes are intentionally disjoint. Shared integration files such as `wiki/log.md`, dashboard data, and the final run report remain owned by the watchdog supervisor. Each branch may append only its required start/update/complete entries to the live communication log; the supervisor will reconcile those append-only entries during integration.

## Integration Sequence

1. Launch three separate worktree chats from the current working-tree state.
2. Require each chat to run Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter roles.
3. Read branch summaries and inspect worktree diffs.
4. Request one repair pass if a report lacks evidence or violates scope.
5. Integrate only approved branch changes into `main` while preserving pre-existing worktree edits.
6. Regenerate generated data and run the full required validation set.
7. Commit and push once if checks pass.
8. After pushed Git evidence, launch bounded Notion-planning reviews for E1-E7/tasks, Links, and July 4-10 Daily Founder Notes.
9. Mutate Notion only if connector schema, target mapping, idempotency, safety, and approval gates are proven; otherwise preserve a manual packet and record the blocker.

## Files Not To Touch In Specialist Branches

- `project/dashboard/data.json`
- `wiki/log.md`
- `project/live/communication/agent-communication-log.md`, except for required append-only branch status entries
- existing master continuation handoff corrections
- ignored local runtime or secret files

## Verification Plan

- Branch-specific Markdown, JSON, YAML, JS, or Python checks as relevant.
- Dashboard regeneration and JSON parse after integration.
- Workflow validation and pre-push runtime guard.
- Python syntax checks named in the owner instruction.
- Public safety scan.
- `git diff --check`.
- Focused review of unsupported claims and external-action gates.
