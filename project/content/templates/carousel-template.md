# Carousel Template

Use after a task or review state has public-safe artifacts and can teach the product-team ICP something concrete about knowledge continuity, source boundaries, generated output packs, or review gates.

## Template Metadata

- Working title:
- Epic/task:
- Source run folder:
- Intended channel: LinkedIn carousel first
- ICP lane: 30-75-person product-led B2B SaaS product leaders under a verified knowledge-continuity forcing moment
- Content identity: ArchFlow company content
- Visual style: product-system and research-lab
- Status: draft / AF Review / owner approval / ready / blocked

## Eligible Subtopics

- A forcing moment exposing scattered product knowledge.
- Messy product source material becoming a reviewed knowledge spine.
- Knowledge spine to PRD, questionnaire, onboarding, or handoff pack.
- Generated-output quality and acceptance-criteria proof.
- KB writeback/readback proof from E1.3.
- Source registry and evidence-label discipline.
- Review gate workflow: AF Review, owner approval, claim downgrade.
- Dashboard as read-only proof surface.
- Why search and meeting assistants stop before maintained knowledge continuity and reviewed execution handoff.

## Proof Required

| Proof item | Required evidence | Evidence label |
|---|---|---|
| Task executed | Run summary or report path | FACT |
| Artifact exists | Repo-relative artifact path | FACT |
| Claim about usefulness | Review report, readback result, or acceptance check | INTERPRETATION |
| Claim about market or buyer pain | Public research card or owner-approved research summary | HYPOTHESIS unless validated |
| Claim about demand, ROI, customers, revenue | E5/E7 payment or firm-intent evidence | FACT only when verified |

## Allowed Screenshots And Data

Allowed:

- Cropped, sanitized artifact screenshots with private content redacted.
- Public-safe snippets from generated reports.
- Source-status chips such as `approved artifact`, `reviewed`, `blocked`, `hypothesis`.
- Process diagrams built from public-safe task names.
- Dashboard screenshots only when they show public-safe read-only state.

Blocked:

- Raw transcripts, private notes, private tool screenshots, private links, local paths, credentials, operational IDs, named targets, customer logos, or fake live dashboard state.

## Slide Structure

### Slide 1: Hook

Copy block:

```text
Most product teams do not need another AI summary.
They need a reviewed path from scattered sources to an answerable company brain and reliable execution handoff.
```

Visual:

- Before/after split: scattered inputs -> reviewed knowledge spine -> generated output pack.
- Evidence chip: `HYPOTHESIS` unless backed by public research.

### Slide 2: Source Boundary

Copy block:

```text
The first gate is not generation.
It is deciding what can be used, what must be redacted, and what cannot leave the private workspace.
```

Visual:

- Three columns: allowed summary, redacted private source, blocked source.
- Evidence chip: `FACT` if tied to the run's source registry.

### Slide 3: Execution Path

Copy block:

```text
ArchFlow turns approved inputs into four execution assets:
source map, reviewed knowledge spine, task-specific output pack, and governed handoff.
```

Visual:

- Linear workflow with four artifact cards.
- Each card links internally to a repo-relative artifact path in the working plan, not in the public graphic unless approved.

### Slide 4: Review Gate

Copy block:

```text
Every output gets reviewed for evidence level, safety, and whether the claim is still only a hypothesis.
```

Visual:

- AF Review checklist with `approved`, `requires edit`, `blocked`.

### Slide 5: Proof Artifact

Copy block:

```text
The proof is not that AI wrote text.
The proof is that the system can preserve context, cite its boundaries, and survive readback.
```

Visual:

- Sanitized artifact card with evidence labels.
- Use E1.3 readback proof only if the run folder has review output.

### Slide 6: Question / CTA

Copy block:

```text
Where does your product knowledge lose the most signal: source ownership, retrieval, synthesis, review, or handoff?
```

Visual:

- Four selectable bottleneck chips.
- CTA stays educational until diagnostic page readiness is approved.

## Approval Checklist

- All slide claims have evidence labels.
- Each artifact reference exists in the source run folder.
- Any screenshot is sanitized and approved.
- No demand, customer, revenue, or ROI claim is made unless E5/E7 evidence exists.
- AF Review approved the carousel plan.
- Owner approved final slide text and images before publishing.

## Save After Execution

- Draft plan: `project/runs/<epic>/<date-run-name>/carousel-plan.md`
- Slide source copy: `project/runs/<epic>/<date-run-name>/carousel-copy.md`
- Visual checklist: `project/runs/<epic>/<date-run-name>/visual-approval-checklist.md`
- Review gate: `project/runs/<epic>/<date-run-name>/review-gate.md`
- Final approved copy, if approved: `project/runs/<epic>/<date-run-name>/approved-carousel-copy.md`
