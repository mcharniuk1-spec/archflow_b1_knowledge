# Branch C Agent Handout: Content Agent Architecture

Date: 2026-07-10
Status: complete; review repairs applied
Branch recommendation: approve

## Purpose

This handout records the Branch C preparation-only content architecture for a future integrator. It covers public news/trend intake, competitor-category analysis, planning, writing/editing, visual specifications, QA/publishing preparation, and report-only learning for the Product Discovery-to-Production PRD Pack.

## Human Summary

Branch C adds a bounded content operation rather than an autonomous social system. It turns public repo evidence and official public platform guidance into reviewed candidate content for B2B SaaS product teams that need source lineage, PRD clarity, acceptance criteria, and task handoff. It does not frame ArchFlow as a generic AI agency and it makes no customer, revenue, ROI, demand, runtime, or platform-integration claim.

The new calendar fixes a pre-existing arithmetic conflict: it explicitly counts ten candidates as seven static posts, two carousel/checklist posts, and one short-video script. The short-video script uses an included static companion, preserving 70/20/10 without silently counting extra deliverables.

The visual specification follows the current blue/ivory website system: ivory editorial field, teal architecture, controlled blue process rails, dark operational panels, and evidence-first labels. It specifies public-safe artifact concepts rather than screenshots or rendered social assets.

## Current State

- Content operation architecture: drafted in `project/content/architecture/`.
- Initial calendar and visual specifications: drafted and review-gated.
- Platform status: no API access, credentials, social account access, scheduling, upload, publishing, scraping, or external writeback is configured or authorized.
- GAP - Luna model selection unavailable: the collaboration API did not expose a model selector. Required Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter roles were nevertheless requested as bounded real subagents.

## Execution Trace

FACT:

- The branch contract limits Branch C to content architecture, initial calendar, visual specs, the branch handout, and append-only live-log entries.
- Existing content operations already prohibit private-account collection and unapproved social automation.
- The prior five-week calendar labeled as 70/20/10 actually contained five static, five carousel, and five video entries. This new plan makes the arithmetic explicit.
- The current site stylesheet contains the blue/ivory style tokens used by the new visual spec.

INTERPRETATION:

- Product-operations content can explain the source-to-PRD-to-task-handoff method more credibly than generic automation positioning when every claim is evidence-labeled and review-gated.

HYPOTHESIS:

- A static-first mix with one short scripted explanation will make the method understandable while leaving publication and buyer validation to later owner-approved work.

GAP:

- Current Meta/Threads/Instagram guidance was not retrievable during review and must be checked again before any implementation.
- Current platform access, account authorization, API terms, budget/rate limits, owner approval, and buyer-demand evidence are unproven.

## Decisions

- Keep the entire architecture preparation-only; the owner performs any future external action separately.
- Treat manual observation of public formats as a hypothesis source only; no scraped or account-level data may enter the operation.
- Use primary official platform documentation for drift-prone API/access statements and record Meta retrieval as a GAP rather than infer capabilities.
- Use ten counted candidates to enforce the 70/20/10 mix exactly.
- Use the actual website stylesheet's blue/ivory tokens rather than the older gray/red post-design system.

## Artifacts

- `project/content/architecture/README.md` — scope, positioning, mix, and artifact map.
- `project/content/architecture/content-operation-model.md` — eight-role/stage controlled flow with inputs, outputs, stop conditions, and human gates.
- `project/content/architecture/public-source-and-platform-method.md` — source-record schema, public-platform readiness matrix, and prohibitions.
- `project/content/architecture/feedback-and-measurement-specification.md` — aggregate, report-only learning rules.
- `project/content/calendar/2026-07-watchdog-initial-content-plan.md` — exact ten-item, 7/2/1 candidate plan.
- `project/content/mockups/2026-07-watchdog-visual-specs.md` — current blue/ivory visual requirements and item mappings.

## Validation

- Required artifact existence check: pass.
- Exact 7 static / 2 carousel / 1 short mix check: pass.
- Current stylesheet-token check: pass.
- `git diff --check`: pass for the current worktree diff.
- Safety Reviewer: pass after repair. It required C02 to change from `FACT` to `INTERPRETATION` and C05 from `FACT` to `HYPOTHESIS`; both corrections are applied.
- Branch Reporter: approve after this handout and the required complete live-log entry exist. It confirmed the artifacts are additive, allowed-scope files.
- Public safety scan: pass after the complete live-log entry.

## Agent Continuation Prompt

Continue the Branch C review in the ArchFlow Public repository. Read `project/operating-rules.md`, the latest live communication log, `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-task-contracts.md`, and this handout. Inspect only Branch C artifacts and append-only live-log entries. Verify the exact 7/2/1 mix, public-source boundaries, official platform URLs, blue/ivory token alignment, and absence of scraping, posting, external writeback, unsupported runtime claims, or private material. Re-run the public-safety and diff checks after any late edit. Do not deploy, activate providers, access social accounts, publish, mutate external systems, commit, or push. Update this handout with the independent reviewer verdict and return one recommendation: approve, revise, or block.

## Next Actions

1. Give the watchdog integrator the Branch C file list, validation evidence, gaps, and recommendation.
2. Let the integrator decide whether to merge; this branch must not commit or push.

## Safety Boundary

Never copy private material, credentials, social account data, raw posts/comments/messages, screenshots, personal identifiers, local absolute paths, provider values, or private URLs into these artifacts. Do not post, schedule, scrape, call APIs, or write externally from Branch C.
