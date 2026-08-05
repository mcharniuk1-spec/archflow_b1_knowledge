# Dashboard Integration Plan — Not Executed

Status: plan only
Implementation authority: not granted in the 2026-08-05 architecture run
Last verified: 2026-08-05

The dashboard must eventually become a read-only projection of the unified Knowledge Case Controller. No dashboard code, data generator, API route, screen, or deployment was changed by this work.

## Planned information architecture

Replace the top-level numbered architecture selector with one case entry point:

`Cases | Evidence | Requirements & Decisions | Roles & Work | Proposed Actions | Reviews & Approvals | Receipts | Knowledge`

`Knowledge Service` and `Agent Control` may remain temporary stage/view aliases, but not separate stores or product architectures.

## Required packet migration

- Use one `case_id` and one versioned case packet from intake through promotion.
- Map legacy PRD/ICP reports to requirements projections.
- Map legacy Agent Orchestra handoffs to role, task, and proposal projections.
- Preserve original legacy evidence states and attach deprecation metadata.
- Display requirements with source, owner, version, freshness, contradictions, supersession, and acceptance checks.
- Display proposals with requirement coverage, permission, exact change, side effects, rollback, verification, verdict, and approval interrupt.
- Display private evidence only as source class plus sanitized opaque receipt.

## Truth rules

The public/dashboard profile remains report-only. Suggested files stay `created: false`; actions stay `not_executed`; knowledge stays `not_promoted`; adapter readiness is shown separately from configuration. The dashboard never receives raw private paths, corpus text, credentials, Orbit database rows, or action tokens.

## Execution gates for a future run

1. Canonical schemas and compatibility fixtures independently approved.
2. Provider-disabled controller and action validator pass positive and adversarial cases.
3. Legacy packet parity and deprecation inventory complete.
4. Browser-local privacy, accessibility, mobile, and frozen-output review pass.
5. API/report contracts updated without inventing runtime proof.
6. Owner separately authorizes dashboard edits and any deployment/promotion.

The numbered labels are retired only after all six gates and a rollback plan pass.
