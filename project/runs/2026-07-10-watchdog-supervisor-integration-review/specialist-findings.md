# Specialist Findings

Status: integrated review
Date: 2026-07-10

## Scope

The watchdog supervisor reviewed the July 10 continuation handoff and coordinated bounded specialist reviews for:

- Architecture reliability and Jarvis runtime.
- Yushchenko/OpenRouter/model routing.
- Railway and production deployment.
- Market, ICP, competitor, and content-agent architecture.
- Content operations, writing bots, competitor analyzer, and post mockups.
- Notion and Linear external-sync readiness.
- Daily Founder Notes evidence review.

Previously requested specialist outputs were recorded as dispatched in the public handout, but no discoverable output artifacts were available in this run. Replacement specialist reviews were used for evidence gathering. No specialist IDs or private thread details are stored here.

## Decisions By Lane

| Lane | Decision | Accepted Now | Blocked Or Revised |
|---|---|---|---|
| Architecture and Jarvis runtime | Revise | Static/browser-local dashboard plus guarded review-packet API contracts are accepted. | Do not claim autonomous Jarvis, provider runtime, durable writeback, or production-current July 7 contract without fresh hosted proof. |
| OpenRouter and model routing | Revise / block activation | One prior sanitized OpenRouter test artifact is accepted as historical review-gated evidence. | No active provider runtime. Activation requires fresh model/pricing check, explicit model, budget, ledger, and AF Review. |
| Railway and deployment | Block deploy execution | July 3 provider-disabled Railway baseline is accepted as historical proof only. | No current live Railway/Vercel verification or deployment was performed. |
| Market and ICP | Revise | Core ICP remains B2B SaaS product teams and product leaders with PRD/source-lineage pain. | No account-level evidence cards, target table, live buyer proof, paid diagnostic, or ROI/customer proof. |
| Content operations and mockups | Revise | Existing template library and E4/E5 evidence are accepted as foundation. | Missing role contracts, social source policy, and static mockup specs were added in this integration. Publication remains blocked. |
| Notion and Linear | Block automated writeback | Existing Notion-ready packet is accepted as a manual mutation packet. Linear remains optional mirror only. | No verified external target/schema/idempotency map, so no connector mutation. |
| Daily Founder Notes | Accept with gap | July 4-10 notes are accepted as repo-visible evidence summary. | Specialist lane outputs and external mutations were still pending until this review. |

## Main Safety Corrections

- Static dashboard text no longer infers provider approval from phrases such as "use provider" or "OpenRouter."
- OpenRouter execution now requires explicit `OPENROUTER_MODEL`; no `openrouter/auto` fallback is accepted for governed runs.
- The dashboard operating manual now says voice mode is disabled and `/api/voice/chat` returns a disabled-mode packet.
- Content operations now have public-safe role contracts, source policy, competitor-analyzer contract, planner workflow, writing workflow, static post design specs, and a five-week planning draft.

## Remaining Gaps

- No Notion or Linear mutation.
- No Railway/Vercel deployment or hosted smoke proof.
- No provider/model call or model activation.
- No canonical provider-call ledger write path.
- No live buyer proof, account-level outreach table, or paid diagnostic.
- No social posting, social scraping, private profile collection, or external send.
