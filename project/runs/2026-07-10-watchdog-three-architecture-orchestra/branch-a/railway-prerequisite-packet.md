# Railway Prerequisite Packet

Status: planning only. No Railway action or hosted freshness check occurred in this Branch A run.

## Required Before a Deployment Proposal

1. Identify one scoped service and its non-secret build/start contract.
2. Bind the service to the platform-provided port and expose a readiness endpoint.
3. Configure a deployment healthcheck and preserve the response evidence.
4. Keep secrets in Railway variables or another approved server-side secret store; do not copy values into this repository or client code.
5. Define provider-disabled-first behavior, CORS/auth policy, input boundary, request timeout, and retry limit.
6. Define logs, request/model-cost ledger, alert/observability ownership, rollback path, and recovery test.
7. Obtain owner approval before provider activation, external writeback, production promotion, or any deployment action.

## Required Before an Always-Online Claim

- Current endpoint and deployment evidence.
- Deployment-time health evidence plus separate continuous monitoring evidence.
- Auth, persistence, backup/recovery, incident ownership, and capacity expectations.
- A dated availability window and explicit scope of the claim.

## Stop Conditions

- Missing owner approval, target/service mapping, secret isolation, health evidence, or rollback plan.
- Any request to use browser-held provider credentials or to treat a deployment healthcheck as continuous monitoring.
