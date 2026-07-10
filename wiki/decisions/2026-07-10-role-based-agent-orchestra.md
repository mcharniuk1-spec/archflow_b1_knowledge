# Decision: Role-Based Agent Orchestra

Date: 2026-07-10
Status: accepted.

## Decision

ArchFlow authority is defined by bounded roles, not permanently assigned runtime or agent names. Watchdog, executor, verifier, safety-reviewer, integrator, and external-action roles each carry explicit permissions, forbidden actions, evidence duties, and review gates. A compatible runtime may fulfil a role only under that role contract and may not approve its own high-risk output.

Current bindings remain useful operational facts: Codex is the local executor/integrator and Hermes is the planned watchdog label. Those bindings do not create permanent authority or activate providers, deployments, or writeback.

## Consequences

- The watchdog role remains non-executing.
- Substantial work retains maker-checker and independent safety review.
- External-action roles are disabled until action-specific owner approval, target/schema proof, secret isolation, budget/rollback evidence, and post-action verification pass.
- Historical run reports remain historical; current governing/configuration files carry the corrected rule.
