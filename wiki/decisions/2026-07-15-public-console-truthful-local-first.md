# Decision: public console remains truthful and local-first

Date: 2026-07-15

## Decision

Package ArchFlow publicly as a local-first Knowledge Reliability Setup and reference implementation. The console may demonstrate contracts, generated public data, browser-local drafts, and review-bundle export. It must not simulate or market live autonomous execution, a production database, all private skills, or external actions without current evidence.

## Rationale

The verified public surface supports explainability and controlled handoff. A live event feed, durable database, skill-usage ledger, and action-specific approvals are distinct capabilities with different security and operational requirements.

## Consequences

- Stage animation is labelled browser-local preparation until a sanitized event feed exists.
- The public skills catalog contains only the reviewed repository allowlist; no private inventory bulk copy.
- The Data Lab remains read-only generated JSON preview.
- Review-bundle download remains separate from files, commits, push, deployment, provider use, and writeback.
