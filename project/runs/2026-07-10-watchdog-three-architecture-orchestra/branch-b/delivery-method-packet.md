# PRD/ICP Delivery Method Packet

Status: proposed internal delivery method. No client delivery, source ingestion, provider call, or external writeback was performed.

## Delivery Boundary

The service begins only after an authorized client source packet is defined. It does not promise automated decisions, a finished software product, a guaranteed time saving, ROI, funding outcome, or implementation completion.

## Method And Gates

| Stage | Operator action | Required artifact | Gate to proceed |
|---|---|---|---|
| 0. Scope and consent | Confirm business question, source classes, recipient roles, exclusions, confidentiality, and the desired decision. | Intake brief and source boundary | Named owner approves scope; sensitive or prohibited material is excluded. |
| 1. Source inventory | Inventory approved documents, notes, calls, research, and existing tickets without treating model output as a source. | Source register with provenance and coverage gaps | Every assertion can point to an approved source or is labeled as a gap/hypothesis. |
| 2. Evidence review | Extract and classify facts, interpretations, hypotheses, risks, assumptions, and open questions. | Evidence digest and decision log | Reviewer samples source links and resolves contradictions or records them as gaps. |
| 3. ICP and problem frame | Define user, buyer, job, trigger, current workaround, disqualifiers, and evidence confidence. | ICP card and problem statement | No buyer or demand assertion without source support; uncertain rows remain hypotheses. |
| 4. PRD | Convert the reviewed problem into goal, non-goals, scope, flows, requirements, measures, risks, and acceptance criteria. | Review-ready PRD | Every requirement has an evidence link, owner decision, or explicit assumption label. |
| 5. Backlog and Definition of Done | Break approved scope into epics, stories/tasks, dependencies, acceptance criteria, and test evidence. | Prioritized backlog and Definition of Done | Delivery owner confirms sequencing and unresolved decisions. |
| 6. Task packet | Prepare implementation-ready work packets with responsibility, inputs, outputs, constraints, handoff, and QA evidence. | Task packets | Each task has an owner role, dependency state, and testable completion condition. |
| 7. QA and handoff | Run evidence, completeness, traceability, contradiction, safety, and formatting checks. | QA checklist, exception list, and handoff note | Client-facing pack is marked ready, revise, or blocked; no silent gap closure. |

## Standard Artifact Package

1. Intake brief and source boundary.
2. Source register and evidence digest.
3. FACT / INTERPRETATION / HYPOTHESIS / GAP decision log.
4. ICP card and problem frame.
5. PRD with scope, non-goals, requirements, risks, and acceptance criteria.
6. Backlog, Definition of Done, and responsibility map.
7. Task packets and QA/exception report.
8. Optional knowledge-base handoff only after client approval and a verified destination/mutation policy.

## QA Checklist

- Traceability: sampled PRD claims point to a source, owner decision, or labeled hypothesis.
- Scope: non-goals and exclusions are explicit.
- Evidence: contradictions, missing evidence, and unvalidated demand are retained as gaps.
- Delivery readiness: backlog tasks have owners, dependencies, acceptance criteria, and test evidence.
- Safety: private source material, credentials, personal data, and private URLs are absent from public-facing artifacts.
- Handoff: no external task-board or knowledge-base write occurs unless the target, schema, idempotency, rollback, and approval are verified.
