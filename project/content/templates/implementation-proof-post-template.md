# Implementation Proof Post Template

Use when an executed task produced a working artifact, validation result, review decision, or process proof. The post must show implementation evidence, not a generic progress summary.

## Template Metadata

- Working title:
- Epic/task:
- Source run folder:
- Primary artifact:
- Validation artifact:
- Review status:
- Intended channel: LinkedIn post first
- ICP lane: B2B SaaS product leaders for Product Discovery-to-Production PRD Pack

## Eligible Subtopics

- E1.3 KB writeback/readback proof.
- E1.5 public-reporting gate and content approval system.
- Source registry, retrieval metadata, and readback assertions.
- Review gate blocking unsupported claims.
- Dashboard read-only status as operator proof.
- Implementation of reusable templates, PRD assets, or source-boundary rules.

## Proof Required

- `FACT`: exact repo-relative artifact paths, run summary, check output, review verdict.
- `INTERPRETATION`: why the proof matters for PRD quality or agent reliability.
- `HYPOTHESIS`: how the same method may help the product-team ICP.
- `GAP`: what is still blocked, unapproved, or awaiting E6/E7 demand proof.

## Copy Blocks

### Opening

```text
ArchFlow implemented a new proof gate for turning messy product-team source material into execution assets.
```

Alternative for E1.3:

```text
ArchFlow tested whether the knowledge base can read back the current mission, outputs, forbidden actions, and next steps from approved artifacts.
```

Alternative for E1.5:

```text
ArchFlow added a content gate so internal proof does not become public overclaiming.
```

### What Was Implemented

```text
The task produced:
- [artifact 1]
- [artifact 2]
- [review or validation artifact]
```

### What The Proof Shows

```text
FACT: [artifact exists or check passed]
INTERPRETATION: [why this improves handoff quality]
HYPOTHESIS: [how this maps to product teams]
GAP: [what still needs review, owner approval, or buyer evidence]
```

### Why Product Leaders Should Care

```text
The bottleneck is not only writing a PRD.
It is preserving source context, separating fact from hypothesis, and handing a reviewed artifact to the next operator without losing decisions.
```

### Close / CTA

```text
Question for product teams: where does your current PRD process lose the most context before engineering starts?
```

## Allowed Screenshots And Data

Allowed:

- Sanitized artifact cards from `project/runs/`.
- Review verdict snippets without private source content.
- Checklist screenshots made from public-safe text.
- Dashboard screenshot only if it contains public-safe read-only status.

Blocked:

- Private source screenshots, raw transcripts, private URLs, local paths, credentials, customer names, named target accounts, or unapproved dashboard state.

## Approval Checklist

- The post names the implementation artifact, not just the activity.
- Evidence labels appear for proof, interpretation, hypothesis, and gap.
- The ICP link is framed as hypothesis unless market evidence exists.
- No customer, revenue, ROI, or market-validation claim appears before E6/E7 proof.
- AF Review approved public safety and claim status.
- Owner approved final text before publication.

## Save After Execution

- Draft post: `project/runs/<epic>/<date-run-name>/implementation-proof-post.md`
- Evidence checklist: `project/runs/<epic>/<date-run-name>/post-evidence-checklist.md`
- Review gate: `project/runs/<epic>/<date-run-name>/review-gate.md`
- Final approved post, if approved: `project/runs/<epic>/<date-run-name>/approved-implementation-post.md`
