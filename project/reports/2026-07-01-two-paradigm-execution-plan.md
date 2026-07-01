# Two-Paradigm Execution Plan

Date: 2026-07-01
Status: testable operating plan

## Executive Answer

Execute ArchFlow through two explicitly separated lanes:

1. Product lane: PRD/ICP service product, externally showable after evidence gates.
2. Control-system lane: local agentic development system, operated by Codex and later optionally by an approved local bridge or backend.

The two lanes can share dashboard visibility, but they must not share authority. The product lane creates buyer-facing output. The control-system lane edits code, routes agents, verifies checks, writes memory, and decides when output is safe.

## Lane 1: PRD/ICP Service Product

Goal: show the buyer a clear productized service outcome.

Input:

- sanitized dialogue or meeting summary;
- product-team docs or approved public examples;
- customer/research notes;
- current ICP hypothesis;
- constraints and privacy boundaries.

Flow:

1. Intake source packet.
2. Build PRD.
3. Split market evidence research.
4. Synthesize one ICP.
5. Build landing/demo package.
6. Approve external-safe output.
7. Publish PRD/ICP packet or buyer-facing demo.

Required artifacts:

- source packet;
- PRD draft;
- evidence cards;
- ICP profile;
- demo/landing outline;
- task list;
- confidence level.

Checks:

- source labels present;
- facts, interpretations, hypotheses, and gaps separated;
- no private raw material in public files;
- no demand claim before E7.

## Lane 2: Reliable Development / Control System

Goal: make agentic project execution repeatable, inspectable, and safe.

Input:

- owner command;
- dashboard packet;
- run note or issue;
- branch diff;
- agent handoff;
- validation output.

Flow:

1. Jarvis intake and classification.
2. Codex implementation or review.
3. LangGraph-style state tracking.
4. Parallel agent/reviewer split when needed.
5. Safety/source review.
6. Integrator merge.
7. Owner approval for durable/external actions.
8. Run note, decision, issue, dashboard data, and memory update.

Required artifacts:

- branch diff;
- run note;
- agent handout if multi-agent;
- check results;
- safety scan result;
- dashboard data regeneration;
- memory/log update.

Checks:

- `node --check project/dashboard/app.js`;
- `git diff --check`;
- dashboard JSON parse;
- `python3 project/scripts/dashboard-static-smoke.py`;
- `python3 scripts/public_safety_scan.py`;
- workflow validation;
- runtime guard;
- browser route check for UI changes.

## Codex Local Implementation Route

Use this route for the current project.

1. Codex reads contracts, run notes, dashboard files, and memory.
2. Codex edits the review branch.
3. Codex runs checks locally.
4. Codex writes public-safe run/memory records.
5. Codex updates Notion append-only when current task state needs it.
6. Codex pushes only after checks and owner/merge approval.

Strength:

- safest current executor;
- real filesystem and Git visibility;
- can run project validations.

Limit:

- not always-on when the local device/session is off.

## Web / OpenRouter Route

Use this only after a backend or local bridge exists.

1. Dashboard creates a browser-local command packet.
2. Backend/local bridge receives packet after auth.
3. Backend/local bridge reads `OPENROUTER_API_KEY` from secret/env storage.
4. Provider receives sanitized input only.
5. Result returns as a review packet.
6. Codex/integrator approves memory/writeback.

Strength:

- can support always-on chat/orchestration.

Limit:

- cannot safely run from static client JavaScript;
- requires auth, secrets, budget, model logging, and data policy.

## Branch And Merge Pattern

Use separate branches when both routes exist:

- `product/prd-icp-e2-dry-run` for Lane 1 product artifacts;
- `control/dashboard-jarvis-openrouter-bridge` for Lane 2 runtime/control work.

Merge order:

1. Control-system safety/review branch first.
2. Product artifacts second.
3. Dashboard data regenerated after both.
4. WikiLLM/log/Notion sync last.

## Test Comparison

| Capability | Codex local route | Web/OpenRouter route |
|---|---|---|
| File edits | Yes, with local approval | No until bridge/backend authority exists |
| Provider calls | Not needed by default | Possible only server-side |
| Secrets | Local ignored env | Secret store or ignored local bridge env |
| Dashboard state | Regenerated `data.json` | Live API/SSE after backend |
| Memory write | Codex-reviewed files | Approval packet only until writeback exists |
| Best current use | Implementation and verification | Future chat/orchestration UX |

## Done Criteria

- The route used is explicit.
- The output file exists.
- The dashboard state is regenerated or the reason is recorded.
- Checks pass or exact blockers are recorded.
- Memory/log/report surfaces are updated.
- Notion receives append-only status only after verification.
