# PRD/ICP Delivery Product Architecture

Date: 2026-07-10
Status: Branch B architecture and planning packet; no client delivery, provider call, deployment, publication, or Notion mutation occurred.

## Decision Summary

ArchFlow’s current client-facing proposition should remain a **service-first, productized delivery method**, not a claimed SaaS product: an approved source packet is converted into a reviewed evidence digest, ICP/problem frame, PRD, delivery backlog, Definition of Done, task packets, and a QA handoff. The artifact package is useful only when its source boundary, review gates, and unresolved decisions travel with it.

This document refreshes the planning architecture. It does **not** establish buyer demand, willingness to pay, delivery speed, ROI, paid-client results, current SaaS readiness, or a live Notion connection. The initial ICP is an operating hypothesis to be tested through the existing E2→E6→E7 evidence gates.

Supporting packets:

- [public source register](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/source-register.md)
- [delivery method packet](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/delivery-method-packet.md)
- [Notion-ready planning packet](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/notion-ready-planning-packet.md)

## Evidence Status

### FACT

- The existing public plan defines the first ICP as B2B SaaS product teams, particularly Series B-D companies with 50-500 employees and 2-5 PMs, with a Director or VP of Product accountable for PRD quality and speed. It marks the first paid entry offer as a **hypothesis**, not validated demand. See [project plan](../project-plan.md).
- The accepted E2.0A dry-run requires graded public source evidence and a two-independent-signal gate before outreach-facing account claims. See [ICP profile outline](../runs/2026-07-03-prd-icp-dry-run/icp-profile-outline.md) and [source-grade rubric](../runs/2026-07-03-prd-icp-dry-run/source-grade-rubric.md).
- Current first-party competitor category facts were checked on 2026-07-10 and are listed in the [source register](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/source-register.md).
- The previously prepared E1-E7 packet explicitly retains Notion, provider, deployment, outreach, analytics, and payment gates. See [prior E1-E7 packet](../runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/notion-e1-e7-update-packet.md).

### INTERPRETATION

- The proposed initial wedge is not “another PM tool.” It is a bounded, human-reviewed service intended to connect source discipline, decision traceability, requirements, delivery readiness, and explicit handoff.
- The alternative map points to a category boundary: suites optimize product systems; research platforms optimize customer intelligence; AI PM tools optimize drafting/coaching; connected-work platforms optimize organizational context; human alternatives optimize bespoke judgment. The proposed method is intended to supply accountable scope and review across those boundaries; client need for it remains unvalidated.

### HYPOTHESIS

- **Primary ICP:** B2B SaaS scaleups and other product-led companies, initially within the inherited Series B-D / 50-500 employee / 2-5 PM range, where a product team has an accountable discovery-to-delivery clarity problem. This remains an ICP hypothesis, not a validated segment.
- **Target buyers and leaders:** Director/VP Product, Head of Product, and senior PM leaders are hypothesized decision owners or sponsors. Product Operations leaders are hypothesized co-owners or operational sponsors. Individual senior PMs, product leads, founders, or delivery leads are hypothesized users/champions depending on company shape. None of these role/buying-path assignments is currently validated.
- **Triggers:** a new initiative, discovery material scattered across tools, PRD rework, unclear engineering handoffs, or decision-memory loss. These require account-specific evidence before they can be asserted.
- **Disqualifiers:** an unapproved source boundary, no accountable product/delivery owner, no review time, or data that cannot be safely included in the agreed delivery process.

### GAP

- There are no validated account cards, buyer interviews, paid diagnostics, prepayments, firm paid intent, or measured client outcomes in this branch.
- No Notion connector schema, target mapping, idempotency mechanism, rollback path, or owner approval was verified.
- The inherited ICP segment may need narrowing after E2 source evidence; it is not a market-size or conversion claim.

## Client-Facing Productized Service

### Job To Be Done

**Hypothesis:** when product evidence and decisions are fragmented, a product leader may value a reviewable path from approved source material to a delivery-ready PRD and task handoff. The proposition is intended to start cross-functional delivery with traceable scope, clear acceptance criteria, and visible gaps rather than a polished but ungrounded draft; buyer need and outcome remain unvalidated.

### Delivery Flow

The complete method is specified in the [delivery method packet](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/delivery-method-packet.md):

1. Agree scope, consent, source boundary, exclusions, and decision owner.
2. Inventory sources and create a discovery record covering JTBD, current alternative, 90-day trigger where evidenced, customer forces, risks, and open questions.
3. Build a FACT / INTERPRETATION / HYPOTHESIS / GAP evidence digest and contradiction log.
4. Produce the ICP/problem card and PRD with source or assumption traceability.
5. Translate approved scope into a prioritized backlog, measurable acceptance criteria, Definition of Done, and role-owned task packets.
6. Run evidence, completeness, safety, traceability, and readiness QA; issue a ready / revise / blocked verdict.
7. Deliver the final artifact bundle and propose a knowledge-base promotion candidate only after a verified client destination and approval.

### Standard Artifact Package

| Artifact | Client purpose | QA gate |
|---|---|---|
| Intake brief and source boundary | Defines authorized inputs, exclusions, decision, and recipients. | Consent/scope check. |
| Source inventory and discovery summary | Makes coverage, provenance, JTBD, alternatives, triggers, and unknowns visible. | Source sampling and private-material exclusion. |
| Evidence digest and decision/risk log | Separates fact, interpretation, hypothesis, and gap. | Contradiction and assumption review. |
| ICP card and PRD | Defines who/what problem is in scope and the proposed requirements. | Traceability, non-goals, and acceptance-criteria review. |
| Prioritized backlog and Definition of Done | Makes delivery sequencing and completion testable. | Owner, dependency, measurable outcome, and test-evidence check. |
| Task packets | Gives implementers bounded work, inputs, outputs, constraints, and handoffs. | Role, dependency, acceptance, and QA evidence present. |
| QA verdict and handoff note | States what is ready, what needs revision, and what remains unknown. | AF Review / client reviewer sign-off; no silent gap closure. |

## Alternative Map

All vendor facts below are first-party positioning, checked on 2026-07-10. They support category comparison only; they do not prove product quality, pricing, adoption, implementation effort, security suitability, or client outcomes.

Market-level demand, category size, pricing, and willingness-to-pay evidence were not collected in this branch. The matrix must not be read as a market-demand conclusion.

| Alternative | Current public category fact | Relevant boundary for the service |
|---|---|---|
| Productboard | Product-management platform spanning customer signals, priorities, roadmaps, and delivery-ready specs. [Source](https://www.productboard.com/) | A system of record and planning layer may exist; the service focuses on a reviewed source-to-artifact engagement. |
| Aha! | Product-development suite covering discovery, feedback, prioritization, roadmaps, prototypes, applications, and AI assistance. [Source](https://www.aha.io/) | Broad suite capabilities do not remove the need to agree evidence, scope, owners, and delivery criteria for a specific decision. |
| Dovetail | Customer-intelligence platform that centralizes/analyzes signals and supports research-oriented search, analysis, and documentation. [Source](https://dovetail.com/) | Strong source intelligence can precede the explicit PRD/backlog/DoD handoff that this method makes reviewable. |
| BuildBetter | AI signal analysis for customer feedback, feature requests, bugs, action items, and related signals. [Source](https://docs.buildbetter.ai/pages/Signals/overview) | Generated or classified signals still require scoped interpretation and a client-approved delivery artifact. |
| Cycle | Feedback-to-product-delivery workflow positioning. [Source](https://docs.cycle.app/introduction/about-cycle) | The service can specify the evidence/PRD/DoD boundary before feedback is routed into a delivery workflow. |
| ChatPRD | AI documentation, coaching, planning, templates, and product-tool integration for PM work. [Source](https://www.chatprd.ai/product/features) | Fast drafting/coaching does not replace authorized sources, accountable decisions, or reviewer acceptance. |
| Notion AI | Workspace AI with search, writing, agents, enterprise search, and meeting-note capabilities. [Source](https://www.notion.com/help/category/notion-ai) | It can be a destination or context layer only after the destination, permissions, and write policy are verified. |
| Glean | Enterprise generative AI/search connected to company knowledge, with agents for multi-step work. [Source](https://docs.glean.com/user-guide/about/end-user-quick-start-guide) | Connected enterprise context does not itself define a product decision, PRD quality bar, or client handoff. |
| Dust | Platform for customizable, secure AI agents over team knowledge. [Source](https://docs.dust.tt/docs/intro) | Agent configuration is a separate concern from source authority, review accountability, and delivery criteria. |
| Status quo | Manual documents, spreadsheets, tickets, and ad hoc AI conversations. | A comparison category, not a claim about a particular team; the proposed method supplies a repeatable traceability/review layer. |
| Junior PM / BA | Internal role that may collect requirements and draft documentation. | A human alternative; capability depends on context, supervision, source access, and quality bar, so no performance comparison is asserted. |
| Fractional product consultant | External human practitioner who may provide discovery, product strategy, or documentation support. | A human alternative; engagement scope, expertise, and outcome are variable, so no cost or outcome comparison is asserted. |

## Refreshed E1-E7 Planning Spine

The import-ready details, task rows, properties, and mutation gate are in the [Notion-ready planning packet](../runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/notion-ready-planning-packet.md). This refresh preserves the inherited state: it proposes work and gates; it does not mark any new execution complete.

| Epic | Branch B purpose and status | Retain / revise / add | Acceptance evidence, blocker, and owner decision |
|---|---|---|---|
| E1 | Internal source-to-PRD proof; active/review. | Retain proof and KB governance; add delivery-method QA. | Traceability and public-safety proof; provider/writeback remain gated; owner decides whether a sample may be used. |
| E2 | Evidence-led ICP research; planning/backlog. | Retain source-grade/account-card work; add current alternative map and explicit two-signal gate. | Approved source universe, graded cards, and review; owner decides source scope and segmentation. |
| E3 | Service-first positioning; in progress/backlog. | Retain positioning; revise any SaaS/autonomous/ROI phrasing; add artifact-package proof. | Reviewed copy and source-packet CTA; owner decides publication/CTA. |
| E4 | Educational content; active/in-progress. | Retain content plan; add alternatives, Definition of Done, and source-lineage education. | Source labels and claim QA; owner decides publication. |
| E5 | Demand-quality and ROI method; mixed done/backlog. | Retain measurement architecture; add diagnostic-field mapping and an ROI-hypothesis label. | Approved event/qualification/privacy approach; owner decides analytics/storage. |
| E6 | Evidence-led outreach; not started/backlog. | Retain outreach later; add readiness gate and discovery script. | E2 cards, contact-data policy, owner/reviewer approval; owner decides channel and first wave. |
| E7 | Payment-to-verdict; not started/backlog. | Retain payment/firm-intent standard; add a paid-diagnostic and verdict rubric. | Payment or firm-intent packet with scope, timeline, and budget path; owner decides offer and threshold. |

## Notion Planning Boundary

The prepared packet defines **Epics**, **Tasks**, **Subtasks**, and a **Links** page with minimum properties, seed task rows, and public source references. It is deliberately manual-entry ready only. No target workspace, database, page ID, URL, schema, or field mapping is guessed. Any future mutation must first prove connector schema, target mapping, property types, idempotency, rollback, and explicit owner approval.

## Branch Acceptance And Recommendation

The Branch B deliverables are ready for supervisor review: the report, three supporting packets, and handout remain within the Branch B contract; official source links are present; no external write occurred; and Markdown local-link, diff, and public-safety checks passed. The independent safety review required claim-language corrections, now applied. Branch recommendation: **approve**.
