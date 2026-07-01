# Dashboard And Website Improvement Issues

Date: 2026-07-01
Status: open planning backlog

## Dashboard Issues

| ID | Priority | Issue | Required Fix | Acceptance |
|---|---:|---|---|---|
| D-1 | P0 | Jarvis is not yet dominant enough as the first-screen operating area. | Redesign first viewport around Jarvis chat, voice sphere, command state, and packet queue. | A new user can identify where to start without reading docs. |
| D-2 | P0 | Two orchestras can still feel like tabs rather than operating modes. | Add explicit mode switch and lane descriptions for PRD/ICP Flow and Agent Orchestra. | Each lane explains purpose, inputs, outputs, and blocked actions. |
| D-3 | P0 | Static/local/backend/provider/writeback state can be misunderstood. | Add persistent state badges and proof drawer. | No page implies provider-backed or durable writeback execution unless implemented. |
| D-4 | P1 | Node panel is rich but can feel dense. | Group controls into task tabs: Overview, Inputs, Outputs, Config, Prompt, Runs, Comments. | Operators find prompts/config/logs in one click. |
| D-5 | P1 | Long graph navigation is hard on small screens. | Add mini-map, stage rail, and mobile stage cards. | Mobile review does not require horizontal precision dragging first. |
| D-6 | P1 | Proof and blocker status are not visible enough. | Add issue queue, latest check results, and blocker drawer. | Operator can see current blockers without opening run notes. |
| D-7 | P2 | Brand expression is functional but not memorable. | Add stroke-only arch motif, depth hover buttons, and purposeful transitions. | Dashboard feels like ArchFlow without sacrificing density. |
| D-8 | P2 | Public-safe sample outputs are missing. | Add sanitized sample packets for PRD, evidence, task matrix, and agent run. | Buyer/service lane can be demonstrated without private data. |

## Website Issues

| ID | Priority | Issue | Required Fix | Acceptance |
|---|---:|---|---|---|
| W-1 | P0 | Public positioning must move away from outdated real-estate/short-term-rental framing. | Reframe ArchFlow as source-backed PRD/report/task and governed agent-system services. | Homepage never suggests the old vertical is current. |
| W-2 | P0 | Offer is not yet packaged for a buyer. | Define service packages: diagnostic, PRD packet, evidence/ICP review, dashboard/control setup, optional backend/provider. | Visitor can understand what they can buy first. |
| W-3 | P0 | First ICP must stay product-team-first. | Write homepage and solution page for B2B SaaS product leaders first. | Secondary audiences are not allowed to dilute the first lane. |
| W-4 | P1 | No high-conversion diagnostic path exists. | Create diagnostic page with questions for tools, source readiness, privacy, budget owner, and urgency trigger. | Lead form captures qualification signals, not just contact info. |
| W-5 | P1 | Website needs artifact proof without private screenshots. | Create public-safe examples of source packet, PRD, evidence card, task matrix, and agent config. | Proof section is credible without exposing private material. |
| W-6 | P1 | Differentiation from PRD generators is not explicit enough. | Show two-orchestra architecture and approval gates. | Visitor sees why ArchFlow is not only a prompt or template tool. |
| W-7 | P2 | Visual identity needs modernization. | Reuse arch motif, editorial type, warm/dark palette, and 3D hover motion while dropping old vertical. | Site feels premium and specific to agentic product operations. |
| W-8 | P2 | Metrics and claims need guardrails. | Add claim policy: no fake ROI, fake customers, live backend, autonomous execution, or demand validation. | Public copy passes safety review. |
| W-9 | P0 | Legacy visual interaction reference is not yet encoded into implementation priorities. | Reuse layered arch assets, scroll drift, ambient sheen, dark command panels, and depth-hover patterns from the legacy site while dropping rental positioning. | New page feels visually continuous with legacy ArchFlow but never implies property-manager or short-term-rental positioning. |
| W-10 | P0 | Calculator needs to become the first proof interaction for the new offer. | Rebuild the legacy calculator as `PRD/ICP ROI` and `Knowledgebase Readiness` modes. | Calculator shows planning estimates, readiness scores, recommended first package/action, and explicit no-guaranteed-ROI disclaimer. |

## Gated Dependencies

- Jesus has appended `complete` for the dashboard smoke-test/setup lane. Future dashboard or website implementation edits still require a fresh starting claim, current `git status`, and no overlap with any newer active lane.
- Provider-backed Jarvis requires approved backend or local bridge.
- Railway claims require actual config/runtime proof.
- Public demand claims require E2/E5/E6/E7 evidence.
- Website examples must be public-safe and sanitized.

## Confidence Level

Confidence: 0.78 for issue prioritization; 0.6 for conversion impact until E2/E6/E7 evidence exists.

## Ronaldo Priority Pass

Date: 2026-07-01
Status: planning refinement

### Implementation Order

1. P0 dashboard clarity: D-1, D-2, D-3.
2. P0 website buyer clarity and proof interaction: W-1, W-2, W-3, W-9, W-10.
3. P1 dashboard operability: D-4, D-5, D-6.
4. P1 website conversion/proof: W-4, W-5, W-6.
5. P2 brand and samples: D-7, D-8, W-7, W-8.

### Shared Acceptance Criteria

- No dashboard or website copy implies provider-backed Jarvis, Railway runtime, browser-side provider calls, durable writeback, autonomous execution, validated demand, or ROI proof before implementation and verification.
- Every public-facing claim is either source-labeled, framed as a service offer, or marked as a gated/planned capability.
- The first ICP remains B2B SaaS product teams led by Director/VP Product owners.
- Outdated real-estate and short-term-rental positioning is absent from the active website narrative.
- Public-safe artifact examples use sanitized examples only, not private screenshots, transcripts, documents, account identifiers, or raw source material.
- Legacy design mechanics are reused as interaction mechanics only: layered arch assets, scroll drift, CSS perspective/translate3d, ambient sheen, depth-hover pointer lighting, dark command panels, and calculator-first proof.
- Calculator outputs are planning estimates only and cannot be presented as guaranteed ROI, financial advice, validated savings, or market demand proof.

### Coordination Gate

The prior Jesus smoke-test/setup handoff gate is complete. Dashboard implementation edits remain coordination-gated: append a fresh starting entry, check current `git status`, and verify no active sidecar lane has claimed the target files.
