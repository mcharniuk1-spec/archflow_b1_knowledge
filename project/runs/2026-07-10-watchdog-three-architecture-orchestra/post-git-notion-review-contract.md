# Post-Git Notion Review Contract

Status: execute only after the integrated `main` commit is pushed.

## Planning Lanes

1. **E1-E7 / Tasks / Subtasks** - review Branch B's manual Notion packet, the prior Founder Meeting v2 E1-E7 packet, and the pushed Git evidence. Return exact proposed changes and conflicts; do not mutate.
2. **Links Page** - review public links and repo-relative artifacts proposed for the Links page. Return the minimum safe set; do not include private URLs or IDs and do not mutate.
3. **July 4-10 Daily Founder Notes** - compare the existing daily-notes packet with the pushed completion evidence. Return append/update recommendations without copying raw private notes and without mutation.

## Required Report

Each planning agent returns: target concept, proposed entries, source artifacts, schema assumptions, conflicts, idempotency concerns, private-data risks, and one recommendation: approve, revise, or block.

## Watchdog Mutation Gate

The watchdog may mutate Notion only after pushed Git evidence and only if connector search/fetch proves the exact target pages/databases and property schema. The action also needs an unambiguous update set, idempotency/duplicate check, rollback or correction path, and public-safety approval. If any gate fails, preserve the manual packet and stop.
