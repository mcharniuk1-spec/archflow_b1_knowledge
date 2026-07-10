# Agent Handout

Run: `2026-07-10-watchdog-supervisor-external-execution-lanes`

Status: supervisor delegation prepared.

## Goal

Create bounded specialist execution lanes for the next stage after the Founder Meeting v2 / Hermes watchdog / CAG-RAG integration.

The supervisor role is initiator/watchdog only. Specialist agents perform discovery, implementation, verification, and handoff inside separate Codex threads/worktrees.

## Baseline

Current pushed baseline before this supervisor run:

- Commit: `135dc6f`
- Summary: Founder Meeting v2 / Hermes watchdog / CAG-RAG architecture update is committed and pushed on `main`.

Important current boundaries:

- Codex remains executor, reviewer, file editor, validator, and final integration boundary.
- Hermes remains planned watchdog/controller/reviewer only.
- Dashboard/Jarvis are operator/control surfaces, not the primary brain.
- OpenRouter is spec-ready but disabled by default.
- Railway and production deployment require fresh proof before claims.
- Notion and Linear are optional external surfaces, not required project control planes.
- Content strategy is service-first, not SaaS-first.

## Supervisor Dispatch Lanes

1. Architecture Reliability and Jarvis Runtime Review.
2. Yushchenko OpenRouter and model-routing review.
3. Railway and production deployment review/execution lane.
4. Market, ICP, competitor, and content-agent architecture research.
5. Content operations, writing-bot plan, competitor-analyzer role, and post-design mockups.
6. Notion and Linear external-sync review.

## Shared Safety Rules

Every specialist thread must:

- Read `AGENTS.md`, `project/operating-rules.md`, `project/live/communication/README.md`, `project/live/communication/current-agent-notice.md`, and the latest live communication log before editing.
- Append a public-safe `starting` update before editing.
- Create or update its own run folder under `project/runs/`.
- Keep public files English-only and public-safe.
- Avoid local absolute paths, secrets, private URLs, account IDs, deployment IDs, raw private source text, screenshots, credentials, and personal identifiers.
- Separate `FACT`, `INTERPRETATION`, `HYPOTHESIS`, and `GAP` for claims that affect architecture, runtime, provider, deployment, or market decisions.
- Run the smallest meaningful checks for touched files.
- Stop if the same error appears twice.
- Use at most 3 repair attempts per task.

## External Action Gates

External actions may proceed only when the assigned specialist can prove all required prerequisites without exposing private values:

- Production deployment: public-safety checks pass, deployment target is unambiguous, and rollback/verification path exists.
- Railway action: official Railway CLI/MCP path is used, project/service linkage is verified, no IDs or private URLs are written to public files, and `/health` proof is recorded safely.
- OpenRouter/provider calls: server-side secret access only, fresh model availability check, explicit budget caps, sanitized public-safe payload, model/cost logging, and no raw private material.
- Notion mutation: connector access and target scope are discovered, public-safe mutation packet is reviewed, and no IDs/private URLs are stored in tracked files.
- Linear mirror: optional and lightweight; no overload, no paid-level dependency, no required control-plane migration.

## Expected Specialist Outputs

Each specialist must produce:

- Run handout.
- Files inspected.
- Changes made or explicit no-change decision.
- Evidence.
- Checks run or skipped with reason.
- Remaining risks.
- Exact next safe action.

## Integration Rule

Specialist outputs must be reviewed by a final integrator before merging to `main`, pushing, deploying, mutating Notion/Linear, activating providers, or promoting production.
