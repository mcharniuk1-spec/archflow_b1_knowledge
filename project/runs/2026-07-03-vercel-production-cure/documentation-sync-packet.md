# Documentation Sync Packet: Vercel Production Cure

Date: 2026-07-03
Status: complete after lead deployment facts
Scope: public-safe documentation and Notion synchronization for the Vercel/Railway deployment cure

## Role Boundary

This packet was prepared by the documentation/Notion synchronization worker and finalized after the lead recorded deployment evidence. It does not contain private deployment IDs, account IDs, secrets, or private URLs.

## Final Cure Facts

FACT:

- Public dashboard production freshness is current after the cure.
- The public dashboard URL points to the current Vercel production deployment.
- Vercel same-origin API and Railway Jarvis API both passed Architecture 1 and Architecture 2 review-packet checks.
- Vercel and Railway both report `MODEL_PROVIDER=openrouter`, provider calls `0`, and external writeback `0`.
- Provider-approved checks correctly stop at `openrouter_api_key_missing` because external OpenRouter key storage was not approved.
- No legacy Vercel project was deleted because safe deletion evidence was incomplete.

INTERPRETATION:

E1.7 can be marked Done for the production-current guarded review-flow baseline. It should remain Review for full product runtime.

GAP:

Live provider-backed Jarvis still requires explicit external credential-storage approval, budget ledgering, sanitized input policy, and one low-cost provider-call proof.

## Current Public-Safe Baseline

FACT:

- E1.7 is documented as working for the provider-disabled Railway hosted review-packet baseline.
- Railway checks previously covered health, CORS, chat, PRD/ICP, agent-orchestra, role config, voice-safe text, and approval-gated meeting-test behavior.
- Provider calls and external writeback were documented as `0`.
- Vercel production was reachable, but production dashboard data was stale relative to the current review preview.
- Full product runtime remained gated: auth, persistence, provider ledgering, provider-backed execution, durable writeback, raw voice handling, client workspaces, and buyer proof were not complete.

INTERPRETATION:

The documentation should not move E1.7 to Done merely because the public dashboard loads. It can only update the deployment status after the lead proves production freshness, API routing, and the intended backend authority.

GAP:

- The lead has not yet recorded final cure evidence in this run folder.
- No final proof is available here for production dashboard freshness, canonical Vercel project/domain mapping, OpenRouter-backed execution, live LangGraph/CrewAI runtime, durable configuration persistence, or autonomous KB/Notion/GitHub writeback.

## Documentation Updates Needed After Lead Cure

Update only after the lead supplies evidence:

| Target | Update condition | Required wording boundary |
|---|---|---|
| `project/reports/2026-07-03-cloud-kb-retrospective.md` | Production freshness is proven or remains stale after cure attempt | Say whether production is current; do not imply full product runtime unless all product gates pass |
| `project/reports/2026-07-03-e1-7-railway-jarvis-final-report.md` | E1.7 cloud flow evidence changes | Keep provider-disabled, provider-backed, and durable writeback states separate |
| `project/reports/2026-07-03-railway-dashboard-jarvis-cloud-setup-test-plan.md` | Railway/Vercel authority or API routing changes | Explain whether Vercel calls same-origin API, Railway API, or both |
| `project/reports/2026-07-03-epic-1-summary-and-final-test-plan.md` | Epic 1 final status changes | Move only proven parts to complete; keep product/runtime gates explicit |
| `project/runs/2026-07-03-vercel-production-cure/agent-handout.md` | Lead completes or blocks cure | Record final facts, changed files, checks, gaps, and next safe action |
| `project/runs/2026-07-03-vercel-production-cure/notion-update-packet.md` | Lead final facts are available | Prepare append-only Notion text with exact status and evidence |
| `project/dashboard/data.json` | Any source report or status text changes | Regenerate dashboard data and re-run public-safety checks |
| `wiki/log.md`, `wiki/memory.md`, `wiki/insights.md` | Cure changes durable operating facts | Add concise memory only for reusable future-run implications |

## Notion Pages And Tasks To Update

Use append-only updates and omit private page URLs/IDs from public files.

| Notion surface | Required update after cure | Suggested status logic |
|---|---|---|
| Epic 1 parent page | Add top summary explaining final deployment cure result and remaining gates | Do not mark Epic 1 fully Done unless product runtime gates are truly closed |
| E1.7 task | Add final Railway/Vercel proof, production freshness result, API authority, and endpoint matrix | Review if provider-disabled or partially provider-backed; Done only if acceptance criteria and owner approval are met |
| E1.6 task | Update only if KB role split or knowledge persistence changed | Keep Review unless private-vault/KB wiring is also proven |
| Daily Founder Notes | Add a founder-readable deployment cure addendum with business meaning and risks | State what changed, what still cannot be sold as SaaS, and next decision |
| Links page | Replace stale dashboard/deployment pointers with current public review links only | Keep links minimal; no private preview, private Notion, account, or deployment metadata |
| Epic 2 `Planning` task | Add dependency note only if Epic 1 runtime status affects E2 research execution | Keep E2 planning-gated until source/data/provider questions are answered |

## Post-Cure Notion Update Draft

Use this only after the lead fills the bracketed facts.

```text
2026-07-03 deployment cure addendum: the public dashboard production surface was rechecked after the Vercel/Railway cure. Production freshness: [current / still stale]. Canonical frontend authority: [production Vercel project/domain result]. Backend authority: [same-origin Vercel API / Railway Jarvis API / split]. Railway status: [health and endpoint result]. Jarvis architecture checks: Architecture 1 PRD/ICP [passed/failed], Architecture 2 agent-orchestra [passed/failed]. Provider mode: [provider-disabled / approved server-side OpenRouter route with budget ledger / not enabled]. Durable writeback: [disabled / approval-gated / implemented with audit].

Decision boundary: treat E1.7 as [Review / Done for provider-disabled cloud flow / Done for full product runtime] based only on the evidence above. Do not infer full SaaS readiness from site availability alone.
```

## Links Page Draft

Use only public links and repo-relative artifacts.

```text
Current ArchFlow review surfaces:
- Public dashboard: [public dashboard URL if production-current]
- Deployment cure report: project/reports/[final cure report filename]
- E1.7 final report: project/reports/2026-07-03-e1-7-railway-jarvis-final-report.md
- Cloud/KB retrospective: project/reports/2026-07-03-cloud-kb-retrospective.md
- Cure run handout: project/runs/2026-07-03-vercel-production-cure/agent-handout.md

Boundary: private deployment previews, private Notion pages, account IDs, deployment IDs, and service metadata are intentionally omitted.
```

## Evidence Required Before Stronger Claims

Before claiming production-current cloud delivery:

- production dashboard route HTTP `200`;
- production dashboard `data.json` generated from latest accepted source state;
- deployed commit or build source matches latest accepted Git state;
- production `/api/health` or configured Railway `/health` passes;
- Jarvis Architecture 1 route passes;
- Jarvis Architecture 2 route passes;
- browser QA shows no console or page errors;
- public safety scan passes after regenerated dashboard data;
- Notion update is append-only and status wording matches evidence.

Before claiming OpenRouter-backed Jarvis:

- provider key remains server-side only;
- provider model IDs/pricing are refreshed before activation;
- approval gate is recorded;
- budget ledger records model, input class, output class, token/cost estimate, and hard stop;
- sanitized input policy is enforced;
- provider call count and result are captured without logging secrets or raw private material;
- fallback to provider-disabled mode is tested.

Before claiming live LangGraph/CrewAI product runtime:

- LangGraph state transitions are executed by hosted backend code, not only represented in documentation;
- CrewAI roles produce or review an artifact in a controlled run;
- run state persists across requests or is explicitly stateless by design;
- audit log and rollback behavior exist for any durable write;
- KB updates pass the E1.4 promotion rule.

## Recommendation

Do not edit existing reports until the lead records final cure facts. Once facts exist, apply one coherent addendum across the E1.7 report, cloud retrospective, Epic 1 summary, cure handout, Notion packet, dashboard data, and WikiLLM memory. This prevents the old failure mode where backend health, production availability, and production freshness are merged into one overbroad claim.
