# Agent Handout: Live Communication Channel

## Title And Purpose

This handout records the creation of the ArchFlow public project live communication channel for parallel agent work.

## Human Summary

ArchFlow now has a single public-safe live communication folder at `project/live/communication/`. Agents should use it before and during active work so parallel changes do not contradict each other.

The folder contains the working log, the current notice, a message template, a pattern-change log, and a copy-ready system prompt append. Run-specific handouts remain the durable completion record after substantial work.

## Current State

Status: complete.

Main artifacts:

- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- `project/live/communication/agent-communication-log.md`
- `project/live/communication/message-template.md`
- `project/live/communication/pattern-change-log.md`
- `project/live/communication/system-prompt-append.md`

## Agent Continuation Prompt

```text
You are continuing ArchFlow public project work. Before editing files, read project/operating-rules.md and project/live/communication/current-agent-notice.md. Then read the latest entries in project/live/communication/agent-communication-log.md and append a starting update naming your task, likely files, claimed files, expected output, blockers, and next step. Coordinate with any existing claims before editing. Keep all updates public-safe and use repo-relative paths only.
```

## Execution Trace

FACT: Created the live communication folder and routing files.

FACT: Updated operating rules, agent README, and agent roster to point agents to the new channel.

INTERPRETATION: The live channel is the correct place for active coordination; `project/runs/` remains the correct place for final handouts.

GAP: This repository cannot directly interrupt agents already running in other chats. The durable notification is now available for agents that follow the project routing contract.

## Decisions

- Use `project/live/communication/` for active communication.
- Keep run handouts under `project/runs/` for durable completion summaries.
- Require pattern changes to be logged and announced.

## Validation

- Pass: `python3 scripts/public_safety_scan.py`
- Pass: targeted safety text scan found only existing safe/masked references and the new safety-boundary warnings.
- Pass: `ruby -e "require 'yaml'; YAML.load_file('project/agents/agent-roster.yaml'); puts 'agent-roster yaml ok'"`
- Pass: targeted ASCII scan on the new communication files and updated routing files.
- Note: base `python3` does not have PyYAML installed, so Ruby was used for the YAML parse check.
- Note: the public worktree already had unrelated changed files before this run; they were left untouched.

## Safety Boundary

Do not store secrets, private URLs, account IDs, local absolute paths, raw private source text, screenshots, credentials, or personal identifiers in the live communication folder.
