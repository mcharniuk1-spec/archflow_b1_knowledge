# Review Gate Template

Use whenever AF Review, owner approval, or another gate decides whether an executed task, carousel, post, dashboard update, or research check can move forward.

## Template Metadata

- Review target:
- Source run folder:
- Reviewer role: AF Review / owner / implementation reviewer / research reviewer
- Status: approved / approved with edits / blocked / needs owner decision
- Date:

## Review Inputs

- Draft artifact:
- Evidence artifact:
- Source registry or inventory:
- Validation result:
- Screenshot/data checklist:
- Prior gate, if any:

## Review Checks

| Check | Pass/Fail | Required evidence or edit |
|---|---|---|
| English-only content |  |  |
| Public-safe text |  |  |
| No private links, local paths, personal identifiers, IDs, or secrets |  |  |
| No raw transcripts or private source material |  |  |
| Evidence labels are present |  |  |
| Claims match evidence strength |  |  |
| No demand, ROI, customer, revenue, or market-validation overclaim |  |  |
| Allowed screenshots/data only |  |  |
| ICP fit: B2B SaaS product leaders |  |  |
| ArchFlow company voice |  |  |
| Owner approval required before publication |  |  |

## Verdict Blocks

### Approved

```text
Status: approved
Reason: The artifact is public-safe, evidence-labeled, ICP-relevant, and contains no unsupported demand or ROI claims.
Required next action: record owner approval before publication.
```

### Approved With Edits

```text
Status: approved with edits
Required edits:
- [edit 1]
- [edit 2]
Required next action: apply edits, rerun AF Review, then request owner approval.
```

### Blocked

```text
Status: blocked
Blocking issues:
- [issue 1]
- [issue 2]
Required next action: fix source boundary, downgrade claims, remove unsafe material, or wait for missing proof.
```

### Needs Owner Decision

```text
Status: needs owner decision
Decision needed:
- [visibility, CTA, public/persona lane, screenshot approval, or publishing timing]
Required next action: do not publish until owner decision is recorded.
```

## Approval Checklist

- Review target is named and linked with a repo-relative path.
- Verdict is one of the four allowed states.
- Every fail has a required edit or blocker.
- Owner-only decisions are not resolved by the reviewer.
- Publication remains blocked until owner approval is recorded.

## Save After Execution

- Review gate: `project/runs/<epic>/<date-run-name>/review-gate.md`
- Owner approval record, if received: `project/runs/<epic>/<date-run-name>/owner-approval.md`
- Blocker note, if blocked: `project/runs/<epic>/<date-run-name>/blocked-issues.md`
- Revised artifact: keep beside the original draft with `approved-` prefix only after approval.
