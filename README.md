# ArchFlow Public Project

This folder is the clean public-safe project root for the ArchFlow reset.

All active work after the 2026-06-24 reset belongs under `project/`.
Prior work is represented only as sanitized English summaries under `history/`.

## Public Boundary

This folder is intended to be safe to push to a public Git repository.

Rules:

- Use English only.
- Use repo-relative paths only.
- Do not store personal names, private workspace links, local absolute paths, user IDs, account IDs, API keys, tokens, cookies, passwords, or raw credentials.
- Do not copy raw Notion exports, old PDFs, screenshots, Vercel metadata, API files, browser logs, or private source files into this folder.
- Store provider settings only as examples or non-secret configuration.
- Treat Codex as the operator runtime. Do not claim Codex auth is an API key for external frameworks.

## Folder Map

| Folder | Purpose |
|---|---|
| `project/` | Current post-reset project, operating rules, plan, agent stack, provider setup. |
| `history/` | Public-safe summaries and inventories of pre-reset ArchFlow work. |
| `skills/` | Skills and agent hooks used for this project. |
| `wiki/` | Public WikiLLM memory layer for project instructions, runs, decisions, issues, and insights. |

## Current Project Direction

ArchFlow is being reset around a first solution:

`dialogue/chat/meeting material -> structured context -> PRD -> task and responsibility plan -> agent-ready knowledge base`

The first public-safe implementation goal is to prove this workflow internally before positioning it externally.
