# Agent Activity Progress Report Template

Use this template after any agentic execution, dashboard/Jarvis run, PRD generation, provider test, review pass, or multi-agent handoff. It is stricter than the general after-execution report because it records source boundaries, agent activity, provider state, checks, and Notion status candidates in one place.

## Required Structure

```md
# Agent Activity Progress Report - <run title>

## Run Metadata

| Field | Value |
|---|---|
| Date |  |
| Lane |  |
| Epic/task |  |
| Agent role |  |
| Status | complete / review / blocked / backlog |

## Source Boundary

- Approved inputs:
- Excluded raw inputs:
- Public-safe source IDs:
- Provider/input rule:

## Activity Ledger

| Time | Actor | Action | Artifact | Status |
|---|---|---|---|---|
|  |  |  |  |  |

## Artifact Table

| Output | Path | Purpose | Review state |
|---|---|---|---|
|  |  |  |  |

## Proof

FACT:

INTERPRETATION:

HYPOTHESIS:

GAP:

## Provider Ledger

| Field | Value |
|---|---|
| MODEL_PROVIDER |  |
| Provider calls |  |
| Model IDs |  |
| Input kind | raw / sanitized digest / public corpus / none |
| Cost |  |
| Budget guard |  |
| Blocker |  |

## Checks

| Check | Result | Notes |
|---|---|---|
| Public safety scan |  |  |
| Workflow validation |  |  |
| Runtime guard |  |  |
| Dashboard JSON parse |  |  |
| JS syntax check |  |  |
| API syntax check |  |  |
| PDF existence/size check |  |  |
| Evidence-label review |  |  |

## Notion Status Candidates

| Task | Status candidate | Evidence | Blocker |
|---|---|---|---|
|  |  |  |  |

## Next Safe Action

1.
2.
3.
```

## Rules

- Keep the report English-only and public-safe.
- Use repo-relative paths only.
- Do not include secrets, credentials, private URLs, account IDs, raw transcripts, screenshots with private UI, or personal identifiers.
- Separate local/Codex output from provider output.
- If an external provider call is blocked, record the exact blocker and do not retry through a workaround.
- A Notion task can move to Done only when the bounded output exists, checks passed, and no owner approval remains.
