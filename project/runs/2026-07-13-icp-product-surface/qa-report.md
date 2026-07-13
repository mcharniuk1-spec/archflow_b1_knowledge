# QA Report - ICP Product Surface

Date: 2026-07-13
Result: pass for local/public implementation
Provider calls: 0
Writeback actions: 0

## Deterministic checks

| Check | Result |
|---|---|
| Dashboard data regeneration | Pass: `project/dashboard/data.json` regenerated after current audience, role, plan, run, and WikiLLM updates. |
| JSON/YAML parsing | Pass: dashboard data, Vercel configuration, agent roster, audience routing, market, RAG, and LangGraph files parse. |
| JavaScript syntax | Pass: website, Jarvis, and dashboard application. |
| Python compilation | Pass: serverless/FastAPI contracts, generators, retrieval, smoke, and safety scripts. |
| Workflow validation | Pass: LangGraph, LlamaIndex, CrewAI, knowledge integration, market research, and model routing. |
| Diff hygiene | Pass: `git diff --check`. |
| Public safety | Pass: publishable-file scan. The OpenAI-key rule still catches a token-shaped fixture and no longer mistakes `task-contract-index` for a key. |
| Current active-routing search | Pass: no old 50-500, Series B-D, PRD-Pack-first, PRD Rescue, Discovery Diagnostic, or E6/E7 market-gate phrase remains in the active CAG, audience, agent, workflow, content, dashboard-code, or routing scope. The dated collaborator brief retains its historical wording only under explicit `historical_superseded` metadata. |

## Browser and interaction QA

Tested at desktop 1440 x 1000 and mobile 390 x 844, plus a reduced-motion mobile context.

| Surface | Verified result |
|---|---|
| Website | Seven-layer direct selection works under reduced motion; selecting step 4 shows `Orchestrate & approve`. |
| ROI scenario | Default recovery is 0 and payback says `Set recovery`; entering 25% updates recovered value and payback. The label is `Modeled readiness index`. |
| Mobile dashboard | Content begins at y=160.6 in the first viewport; document width equals the 390px viewport. |
| Mobile workflow full screen | Shell width is 390px at x=0; exit control remains visible between y=48.2 and y=84.2. |
| Architecture hash routing | Changing from service to schema renders `(2) Reliable Agent Orchestra`. |
| Node dialog | Focus is trapped, Escape closes, and focus returns to the invoking Stage node. |
| Jarvis composer | A slash typed in the textarea remains in the request text. |
| API-base safety | A non-current, non-loopback API base is blocked before a request or owner token can be transported. |
| Essential Jarvis text | Tested runtime, approval, and model labels render at 10px or above. |
| Eight dashboard routes | Overview, Architecture, Knowledge, Agents, Runs, Reference, Workflow, and Plan render with no provider call or writeback. |

The broader desktop/mobile browser pass also found no horizontal overflow or console exceptions on the website/dashboard. The mobile ROI calculator remains contained in one 390 x 844 viewport.

## Jarvis API contract QA

FastAPI contract smoke:

```text
jarvis_api_contract_smoke=ok endpoints=18 owner_guard_cases=5 replay_blocked=1 cors_403=1 provider_calls=0 writeback=0
```

Serverless owner-guard smoke:

```text
jarvis_serverless_owner_guard_smoke=ok gates=owner,acknowledgement,allowlist,durable-controls replay_blocked=1 provider_calls=0
```

The tested replay blocker is `durable_nonce_and_spend_ledger_required`. This is a deliberate fail-closed state, not proof that durable controls are implemented.

## Retrieval QA

Lexical mode was requested explicitly. It loaded 589 approved documents and 4,388 chunks. Vector retrieval was not requested and is not claimed.

Query:

```text
enterprise onboarding product knowledge continuity RFP buyer
```

Result:

- The canonical audience node ranked first, second, fourth, and fifth.
- The current strategic plan ranked third.
- Dashboard authority metadata assigns `canonical_current` boost `3` to the audience node and `historical_superseded_icp` boost `-2` plus a canonical pointer to an old ICP report.

## External task-board readback

- Epic statuses and 25 relevant ICP-aligned rows were re-read independently.
- Four baseline rows remain Done / Proven.
- Twenty-one rows remain Planned.
- No required-field gap, duplicate current title, status inflation, or dependency cycle was found.

## Explicitly not tested or claimed

- Production deployment or freshness.
- Figma synchronization.
- Provider completion, provider cost, or live durable spend enforcement.
- External writeback, outreach, publication, buyer interview, paid intent, or payment.
- Vector-default retrieval, TurboVec, Cognee, or a new MCP/admin product runtime.

One non-blocking library deprecation warning appears in the FastAPI test harness. It does not change the passing contract result but should be addressed during the next dependency-maintenance lane.
