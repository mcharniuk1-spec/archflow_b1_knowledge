# Yushchenko Model Efficiency Observer

Status: active in Codex app automation.

Automation ID: `yushchenko-model-efficiency-observer`

Cadence: every five hours.

## Purpose

The Yushchenko observer watches model and token usage across the ArchFlow public project and produces recurring Markdown reports. It checks whether agents used the right model tier for the task, whether OpenRouter usage was logged, and whether cheaper execution models should replace frontier calls.

## Scope

Read:

- `project/config/model-routing.yaml`
- `project/reports/2026-07-01-openrouter-model-routing-plan.md`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- `project/live/communication/agent-communication-log.md`
- `project/runs/`
- `wiki/log.md`

Write:

- `project/runs/yushchenko-model-efficiency/YYYY-MM-DD-HHMM-model-efficiency-report.md`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- `wiki/log.md`
- `project/live/communication/agent-communication-log.md`

## Required Report Sections

Each report must include:

1. Run window and evidence files inspected.
2. Models used by provider and model ID.
3. Task and reason for each model use.
4. Token and cost fields when available.
5. Efficiency score from `project/agents/model-efficiency-advice.md`.
6. Waste or overuse risks.
7. Under-review risks.
8. Cheaper substitute recommendation where appropriate.
9. Frontier escalation recommendation where appropriate.
10. Missing logging fields.
11. Telegram delivery status.
12. Next actions.

## Telegram Rule

The observer should send a short summary to the approved private Telegram destination only when an approved Telegram sender, bot, or tool is available outside the public repo.

Never store chat URLs, chat IDs, bot tokens, private links, account IDs, or credentials in public project files.

If no approved sender exists, the report must say:

`Telegram send skipped - approved sender unavailable.`

## OpenRouter Rule

If no OpenRouter usage evidence exists, the observer must say:

`No active OpenRouter runtime evidence found.`

It must not invent model calls, token counts, costs, or efficiency numbers.

## Agent Notification Rule

At the start and end of each run, append a concise update to `project/live/communication/agent-communication-log.md`.

## Safety Checks

Run the smallest meaningful checks after writing:

- YAML parse for `project/agents/agent-roster.yaml` if edited.
- `python3 scripts/public_safety_scan.py`.

## Failure Handling

If a required source is missing, write a report with `GAP` entries instead of failing silently.

If public safety scan fails, do not send Telegram and record the failing file/pattern in the report.
