# After-Execution Report Template

Use after any executed task, review state, content draft, research check, dashboard update, or implementation proof. This is the durable report that future agents and reviewers can read without chat history.

## Template Metadata

- Run title:
- Date:
- Epic/task:
- Agent role:
- Source run folder:
- Status: completed / review / blocked / deferred
- Publication status: not drafted / drafted / AF Review / owner approval / published / blocked

## Required Report Structure

```md
# Run: <title>

Date:
Status:
Epic/task:
Agent role:

## Task

What was executed, reviewed, or created?

## Inputs

- Public-safe input 1:
- Public-safe input 2:
- Source boundary:

## Outputs

| Output | Path | Purpose | Status |
|---|---|---|---|
|  |  |  |  |

## Proof

FACT:
INTERPRETATION:
HYPOTHESIS:
GAP:

## Allowed Screenshots/Data

- Approved:
- Blocked:
- Needs owner approval:

## Review And Approval

- AF Review:
- Owner approval:
- Publication state:

## Checks

| Check | Result | Notes |
|---|---|---|
| Public safety scan |  |  |
| English-only/ASCII review |  |  |
| Link/path review |  |  |
| Evidence-label review |  |  |

## Next Actions

1. 
2. 
3. 

## Save Locations

- Run artifacts:
- Content draft:
- Review gate:
- Owner approval:
- Final approved output:
```

## Proof Required

- At least one concrete output path.
- Explicit claim status using FACT, INTERPRETATION, HYPOTHESIS, and GAP when meaningful.
- Check result or reason skipped.
- Review status and owner-approval status.
- Clear next action.

## Approval Checklist

- Report is English-only and public-safe.
- Paths are repo-relative.
- No private material, secrets, private links, personal identifiers, local paths, or raw transcripts are included.
- Any content draft is marked draft until AF Review and owner approval pass.
- Publication state is explicit.

## Save After Execution

- Default: `project/runs/<epic>/<date-run-name>/run-summary.md`
- For content-specific runs: `project/runs/E1.5/<date-run-name>/after-execution-report.md`
- Agent handout when agent roles or subtasks are involved: `project/runs/<epic>/<date-run-name>/agent-handout.md`
- Wiki run note only when the work changes future operating behavior.
