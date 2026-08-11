# Portable Skill Set

The public release allowlist contains exactly ten project-local skill packages. `project/database/skill-catalog.json` is the machine-readable catalog and the dashboard projection. Catalog hashes must be regenerated after any `SKILL.md` change; documentation mentions are not execution counts.

These packages provide reusable operating contracts. They do not activate a provider, grant administrator authority, read credentials, start a service, edit an external system, deploy, publish, or push Git.

## Packages

| Package | Purpose |
|---|---|
| [`arcagcom`](arcagcom/SKILL.md) | Coordinate parallel work with public-safe Communication Center or local packets, file claims, conflict stops, and evidence-backed handoffs. |
| [`archflow-agent-control`](archflow-agent-control/SKILL.md) | Convert a reviewed knowledge report into a bounded role, task, skill, file, review, and stop contract without launching agents. |
| [`archflow-architecture-operator`](archflow-architecture-operator/SKILL.md) | Design or audit goal, state, role, retrieval, loop, review, receipt, memory, and external-action boundaries. |
| [`archflow-e1-runtime-guard`](archflow-e1-runtime-guard/SKILL.md) | Run provider-disabled safety, schema, workflow, import, fixture, dashboard-data, and Git-diff checks before integration. |
| [`archflow-knowledge-service`](archflow-knowledge-service/SKILL.md) | Prepare source-bounded FACT / INTERPRETATION / HYPOTHESIS / GAP knowledge packets and reviewed solution-memory candidates. |
| [`archflow-task-breakdown`](archflow-task-breakdown/SKILL.md) | Turn a bounded objective into staged subtasks, dependencies, acceptance criteria, gates, and stop conditions. |
| [`humanize-writing`](humanize-writing/SKILL.md) | Improve user-facing prose while preserving facts, links, metrics, protected blocks, uncertainty, and evidence limits. |
| [`outquestions`](outquestions/SKILL.md) | Convert a completed pass into clear decisions, open questions, risks, and the next-stage gate. |
| [`priority-task-operator`](priority-task-operator/SKILL.md) | Rank actionable tasks from a caller-supplied plan and prepare one reproducible next-task handoff. |
| [`task-handout`](task-handout/SKILL.md) | Produce a human summary and copy-ready continuation prompt from verified work, artifacts, checks, and gaps. |

## Shared contracts

- `project/context/context-capsule.schema.json` defines source-bounded context.
- `project/database/run-envelope.schema.json` defines provider-neutral execution state.
- `project/database/review-bundle.schema.json` defines a browser-local review export; it is not authority.
- `project/database/action-receipt.schema.json` records an action only after verified execution and review.
- `project/database/solution-memory-record.schema.json` defines reusable reviewed meaning and supersession.
- `project/config/provider-registry.json` is the canonical provider inventory; the default remains `none` and observability remains off.

## Integration rules

1. Give each role only the minimum packages named by its task contract.
2. Keep maker and independent reviewer separate for high-risk output.
3. Use the dashboard Communication Center or caller-supplied Git-ignored local output; do not depend on tracked live logs, run archives, wiki folders, dated plans, or automations.
4. Treat a configured workflow, valid packet, or installed dependency as readiness evidence only, not execution proof.
5. Require action-specific approval, rollback, and readback for provider calls, credential use, deployment, Git push, publication, destructive actions, and external writeback.
6. Regenerate `project/database/skill-catalog.json` and dashboard data, then run the runtime guard and independent review before release.

Additional packages may enter the allowlist only after provenance and license review, public-safety checks, a sanitized fixture, permission analysis, rollback proof, catalog registration, and independent approval.
