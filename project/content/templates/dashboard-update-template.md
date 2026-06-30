# Dashboard Update Template

Use when dashboard status, read-only monitoring, hosted-view readiness, or dashboard-adjacent reporting changes. This template must not modify dashboard code or imply live control when the dashboard is read-only.

## Template Metadata

- Working title:
- Dashboard surface:
- Source run folder:
- Related epic/task:
- Status: draft / AF Review / owner approval / ready / blocked
- Public state: local read-only / hosted read-only / hidden-link / auth-gated / blocked

## Eligible Subtopics

- E1.3 dashboard status generated from run evidence.
- Read-only operator dashboard as proof surface.
- Dashboard/voice/hosting gate status.
- What dashboard cards can show publicly.
- Why dashboards should not create live-state claims before runtime proof.

## Proof Required

| Claim | Required proof | Evidence label |
|---|---|---|
| Dashboard data changed | Generated data artifact or run summary | FACT |
| Dashboard is read-only | Dashboard documentation or gate report | FACT |
| Hosted dashboard is available | Hosting proof and approved visibility setting | FACT |
| Dashboard proves workflow reliability | Review report plus repeatable run evidence | INTERPRETATION |
| Dashboard proves customer demand | E6/E7 evidence only | FACT when verified, otherwise blocked |

## Allowed Screenshots And Data

Allowed:

- Public-safe dashboard status card.
- Run-count or artifact-count summaries from public files.
- Read-only badges and gate-status chips.
- Cropped views that reveal no private paths, IDs, credentials, logs, or hidden config.

Blocked:

- Raw env status values, tokens, private project IDs, local paths, private source names, fake live metrics, customer data, named target accounts, or unpublished internal decisions.

## Copy Blocks

### Opening

```text
ArchFlow uses the dashboard as a read-only proof surface, not the project brain.
```

### What Changed

```text
FACT: [dashboard-related artifact or status changed]
FACT: The source evidence is stored at [repo-relative path].
```

### What It Means

```text
INTERPRETATION: This helps future operators see which proof runs, review gates, and knowledge-base outputs exist before they act.
```

### What It Does Not Mean

```text
GAP: This does not prove customer demand, ROI, or production buyer value. Those remain blocked until E6/E7 evidence exists.
```

### CTA

```text
For product leaders, the useful dashboard question is simple: can your team see which PRD claims are facts, hypotheses, or unresolved gaps before engineering starts?
```

## Approval Checklist

- The update does not require dashboard code edits.
- All screenshots are sanitized and approved.
- The dashboard is described as read-only unless a separate runtime gate proves otherwise.
- No private config, hidden env state, local path, or private identifier appears.
- AF Review approved safety and claim status.
- Owner approved publication or sharing mode.

## Save After Execution

- Draft update: `project/runs/<epic>/<date-run-name>/dashboard-update.md`
- Screenshot checklist: `project/runs/<epic>/<date-run-name>/dashboard-screenshot-checklist.md`
- Review gate: `project/runs/<epic>/<date-run-name>/review-gate.md`
- Approved update, if approved: `project/runs/<epic>/<date-run-name>/approved-dashboard-update.md`
