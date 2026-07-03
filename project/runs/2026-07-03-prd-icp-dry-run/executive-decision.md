# E2.0A Executive Decision

Date: 2026-07-03
Status: accepted by owner on 2026-07-03

## One-Sentence Decision

ArchFlow will run its first market-facing research loop as a bounded PRD-to-ICP evidence pipeline over public sources only, using the account evidence card schema and source grade rubric from this packet, before any outreach, provider spend, or paid-test claims.

## Why Now

- E1.1-E1.3 proved the infrastructure spine; E1.4 defined the KB update principle. The system is ready for disciplined research proof, not wider architecture.
- Positioning (E3.1) and content (E4.1) need graded evidence to avoid overclaiming.

## Owner Of The Decision

Project owner. AF Review gates fact-checking; agents execute bounded stages per `project/workflows/market-research-engine.yaml`.

## What This Decision Enables

- E2.1: approved source list and segment data model.
- First real account universe pass with deduplicated card table.
- Honest ICP confidence upgrades from graded signals.

## What This Decision Explicitly Does Not Do

- No outreach, no payment-test claims, no demand validation claims.
- No gated tools (search APIs, crawlers, enrichment vendors) without separate approval.
- No provider calls; no autonomous external sync.

## If Unresolved

Research proceeds ad hoc without evidence discipline, positioning claims risk overreach, and the fact_check_gate has nothing enforceable to check against.

## Acceptance

Owner acceptance of this packet was recorded on 2026-07-03. E2.0A is closed for method scope and E2.1 planning is unlocked.
