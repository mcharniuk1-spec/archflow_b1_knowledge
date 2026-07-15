# Issue: Runtime, Authentication, And Writeback Remain Gated

Date: 2026-07-15

Status: open

## GAP

The public dashboard now has browser-local Admin/Guest previews and local report downloads, but it has no authentication, individual durable memory, live agent runtime, runtime event feed, provider execution ledger, production database, or external writeback.

## Required closure evidence

- Authentication/tenancy/RBAC/retention design and tests before describing users or member memory.
- Sanitized runtime event schema and fresh evidence feed before showing a live execution state.
- Durable owner/replay/spend ledger and provider readback before provider activation.
- Target/schema/idempotency/rollback/approval/readback proof before any external writeback.

## Safe interim behavior

Keep the Admin/Guest switch and downloads explicitly browser-local. Do not infer a runtime action from a dashboard animation or local report ID.
