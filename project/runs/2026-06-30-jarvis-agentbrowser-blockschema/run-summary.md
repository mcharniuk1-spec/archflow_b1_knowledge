# Jarvis Agentbrowser Voice And Block Schema Review

Date: 2026-06-30
Status: completed on review branch
Branch: `review-jarvis-agentbrowser-blockschema-20260630`

## Task

Improve the dashboard after the visible voice recognition `network` failure and make the block schema page operable for local review without enabling provider calls, writeback, raw transcript storage, or external publishing.

## Changes

- Added a manual transcript fallback path in the Jarvis view.
- Preserved fallback input during live/focus refresh so operator text is not cleared while editing.
- Added clearer browser speech-recognition error messages and a speaker-test control.
- Replaced the static block-schema explanation with a local editor:
  - draggable blocks;
  - visible movement controls;
  - node prompts, comments, owner/agent, status, requirements, files, questions, outputs, links, and config JSON;
  - validation and review queue export;
  - explicit LangGraph, CrewAI, LangSmith, and Codex trace-prep boundaries.
- Expanded the default schema with separate checker and safety review branches so the default graph validates cleanly.

## Verification

- `agent-browser` checked the local dashboard route.
- Manual fallback accepted a typed transcript, submitted it through the Jarvis chat path, and stored only session-local chat entries.
- Schema comments persisted in the local model.
- Selected schema nodes queued review-packet payloads.
- Pointer drag moved a node and persisted coordinates in local browser storage.
- Default schema validation returned a clean valid state after local reset.

## Checks

- `node --check project/dashboard/app.js`
- `git diff --check`
- `python3 -c 'import json; json.load(open("project/dashboard/data.json")); print("dashboard_json_ok")'`
- `python3 scripts/public_safety_scan.py`
- `project/local/venv/bin/python project/scripts/validate-workflows.py`
- `python3 project/scripts/pre-push-runtime-guard.py`
- Sensitive-string scan over changed dashboard files

All checks passed. The runtime guard required an approved rerun because it writes ignored generated summaries under `project/local`.

## Remaining Gates

- Physical microphone and speaker proof require owner-device browser permission.
- Live LangSmith tracing, provider-backed voice, backend writeback, background capture, deployment/merge, Telegram publishing, and external memory sync remain disabled until explicitly approved.
