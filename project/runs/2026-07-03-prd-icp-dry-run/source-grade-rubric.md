# E2.0A Source Grade Rubric

Date: 2026-07-03
Status: accepted dry-run rubric on 2026-07-03

## Grades

| Grade | Definition | Examples | Allowed use |
|---|---|---|---|
| A | Direct, current, first-party public statement | Company website product/pricing page, official careers page posting, official announcement | FACT with citation; can support outreach and ICP claims |
| B | Independent third-party public evidence, dated and attributable | Public review text, public directory entry, public conference talk, funding announcement | FACT with citation when corroborating; needs one more independent signal for outreach |
| C | Indirect or aging public evidence | Job posting older than 90 days, secondhand blog commentary, aggregated market lists | INTERPRETATION support only; never sole basis for a claim |
| D | Unverifiable, social-only, or anonymous | Social posts, forum comments, uncited claims | HYPOTHESIS only; monitor, never assert |

## Grading Rules

- Every signal on an account evidence card gets exactly one grade.
- Two independent signals of grade B or better are required before any outreach-facing claim (inherited from evidence_rules).
- A social-only account is capped at grade D overall regardless of volume.
- Evidence older than 180 days decays one grade unless re-verified.
- Provider/model output has no grade; it is not a source.
- Conflicting signals: record both, grade both, and mark the conflict as GAP; never silently pick one.

## Scoring Interaction

Grades feed the scoring model in `project/workflows/market-research-engine.yaml` (pain 25, budget proxy 15, trigger 15, strategic fit 15, reachability 10, differentiation gap 10, risk -20). A score computed from grade C/D signals is flagged provisional and cannot pass the fact_check_gate.
