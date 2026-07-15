# GAP: live runtime events, skill telemetry, and evidence ledger

Date: 2026-07-15

## FACT

The public dashboard has no proven sanitized runtime-event feed, durable skill-usage ledger, or authenticated database. Its stage animation, data catalog, and review bundle are browser-local/static features.

## IMPACT

The product must not claim live current-node execution, usage counts, production database access, or autonomous action.

## NEXT SAFE ACTION

Design a bounded event adapter conforming to `project/database/runtime-event.schema.json`, then test it against public-safe fixtures. Design a local evidence ledger only after its read-only, audit, recovery, and private-data separation controls are approved.
