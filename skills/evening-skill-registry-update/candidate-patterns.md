# Candidate Patterns

This file stores candidate post-execution lessons when the evidence points to a possible skill update but the target skill or final rule still needs review.

Candidate entries are not active controlling rules. Promote them only after repeated evidence or explicit review.

## Entry Template

- Candidate title:
- Proposed target skill or prompt:
- Proposed update mode:
- Evidence:
- Why this might improve future runs:
- Why this is not yet active:

## 20260706_run_daily_skill_retrospective

- Date recorded: 2026-07-08T14:56:04+00:00
- Candidate target: `priority-task-operator`
- Proposed mode: `PATCH_EXISTING_SKILL`
- Required human review: confirm this belongs in an existing support file or `SKILL.md` before promotion.
- Evidence from execution:
- No new skill is justified. The concrete improvement belongs inside the existing `priority-task-operator` workflow.
- Priority mechanical runs repeatedly ranked an owner-gated profile task even after earlier packets already prepared profile drafts and decision artifacts.
- Checks passed in the source run note, including Markdown path existence, dashboard data regeneration, dashboard JSON parse, public safety scan, and diff check.
- Stop rule: do not patch a controlling prompt unless this pattern repeats or the evidence proves a fundamental rule change.
- Update reason: run identified a concrete improvement for an existing skill
