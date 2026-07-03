# Agent Handout: E1.4 KB Update Principle

Date: 2026-07-03
Run: 2026-07-03-kb-update-principle
Owner agent: Claude (Cowork)
Status: accepted by owner on 2026-07-03

## Human Summary

E1.4 is written. The report `project/reports/2026-07-03-kb-update-principle.md` defines the single durable rule for the knowledge system: WikiLLM is the only durable memory; LlamaIndex is retrieval only; Graphify is generated reference; dashboard packets, Notion, Obsidian/Nexus, and Telegram are surfaces whose content becomes knowledge only after agent review and a WikiLLM write. The report includes a promotion test, a per-file WikiLLM decision table, provenance rules, retrieval rules, error/traceback procedure (including credential-boundary incidents), the agent closeout workflow, and validation bundles.

## Decisions Made

- One promotion test governs all durable writes: the content must change future agent behavior, be public-safe English, and carry repo-relative provenance.
- Errors are corrected in place in durable memory, never left standing; incidents get masked issue records.
- No new architecture was invented; the report codifies the existing layer contract.

## Files Changed

- `project/reports/2026-07-03-kb-update-principle.md` (new)
- `project/runs/2026-07-03-kb-update-principle/agent-handout.md` (new, this file)
- `wiki/runs/2026-07-03-kb-update-principle.md` (new)
- `wiki/log.md` (pointer appended)
- `project/dashboard/data.json` (regenerated)
- `project/live/communication/agent-communication-log.md` (starting + closeout entries)

## Checks

- `python3 scripts/public_safety_scan.py`
- `python3 project/scripts/generate-dashboard-data.py` + JSON parse
- `git diff --check`
- venv-dependent checks: see closeout log entry for pass/GAP status.

## Gaps

- Owner acceptance recorded on 2026-07-03 (E1.4 gate closed for documentation/method scope).
- Provider-backed Jarvis, Railway, live Nexus writeback, vector defaulting, dashboard writeback, raw voice storage, autonomous external updates remain gated and unproven.

## Continuation Prompt

You are continuing ArchFlow. E1.4 was accepted by the owner on 2026-07-03. Read `project/reports/2026-07-03-kb-update-principle.md` and apply it to all KB writes. Next task: use the accepted E2.0A packet to plan E2.1 source-list and segment-model execution with approved public-safe sources only. Follow the live communication log discipline and the documentation validation bundle before closeout.
