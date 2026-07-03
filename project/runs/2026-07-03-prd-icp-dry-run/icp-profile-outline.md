# E2.0A ICP Profile Outline

Date: 2026-07-03
Status: accepted dry-run baseline on 2026-07-03
Basis: `project/workflows/market-research-engine.yaml` segment model; `docs/prd-icp-output-template.md` ICP block.

## Primary ICP (dry-run baseline)

| Field | Answer | Evidence | Confidence |
|---|---|---|---|
| Account shape | Series B-D B2B SaaS, 50-500 employees, 2-5 PMs | Workflow segment model (internal, approved) | Medium |
| Buyer role | Director or VP of Product accountable for PRD quality and speed | Workflow segment model | Medium |
| Trigger | New funding, PM team growth, discovery-to-delivery handoff failures, PRD rework complaints | HYPOTHESIS until account evidence exists | Low |
| Pain | Customer research overload, PRD rework, roadmap ambiguity, handoff loss, decision memory gap | pain_type enum; needs per-account evidence | Low-Medium |
| Current workaround | Docs/Notion templates, ad hoc AI chats, manual synthesis by senior PM | HYPOTHESIS | Low |
| Disqualifier | No dedicated product function; single-founder pre-seed; agencies without recurring product work; regulated data that cannot be sanitized | Boundary decision, this run | Medium |
| Budget path | Product org tooling/services budget owned by the buyer role | HYPOTHESIS | Low |

## Offer Mapping

- First offer: Product Discovery-to-Production PRD Pack (source inventory, context digest, PRD, ICP logic, backlog, decision log, review handoff, KB update).
- Fit rule: the account must show at least one graded-B pain signal matching the pain_type enum before offer-fit is asserted.

## Confidence Discipline

Every row above marked Low or HYPOTHESIS must be upgraded only by graded evidence on account cards, never by narrative. The dry run deliberately ships with honest low confidence; E2.1+ fills evidence.

## Open Questions

- Which public directories give the cleanest Series B-D B2B SaaS universe without gated tools?
- Is 50-500 employees the right band, or does PRD pain concentrate at 100-300?
- Does the buyer sit in Product or Product Ops at the upper band?
