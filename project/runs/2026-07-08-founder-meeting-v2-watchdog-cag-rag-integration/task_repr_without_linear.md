# Task Representation Without Linear

Status: active policy for this integration.

Linear is optional only and not required for ArchFlow execution.

## Default Artifacts

- `project/project-plan.md`
- `project/tasks/*.md` if task files are later added
- `project/tasks/*.json` if structured task packets are later added
- `project/runs/<run-id>/task-contracts.md`
- `project/runs/<run-id>/agent-handout.md`
- `project/runs/<run-id>/notion-e1-e7-update-packet.md`
- generated `project/dashboard/data.json`
- GitHub Issues only if owner approves
- Linear mirror only if owner approves and free limits are acceptable

## Required Task Fields

- ID.
- Title.
- Epic.
- Execution type.
- Role.
- Source boundary.
- Inputs.
- Outputs.
- Acceptance criteria.
- Evidence required.
- Review gate.
- Status.
- Blockers.
- Owner decisions.

## External Sync Rule

If Notion, GitHub Issues, Linear, or another task system is not explicitly approved, save update text as a repo artifact and stop.
