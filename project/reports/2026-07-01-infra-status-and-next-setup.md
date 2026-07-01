# Infra Status And Next Setup

Date: 2026-07-01
Status: local MVP implemented; hosted runtime remains gated

## Executive Answer

The current MVP is a static public ArchFlow services website plus the existing internal dashboard route.

Vercel is configured and externally verified as the static hosting layer with prior ready deployments. It keeps the last deployed website/dashboard available when local Codex/Jarvis is off, but it does not execute Jarvis, agents, provider calls, memory writes, or Notion/GitHub writeback.

Railway is not linked or configured for this repo. The Railway connector returned no linked project, and no local Railway service files were found. Railway remains the future backend option for server-side auth, provider calls, queues, SSE/websocket, durable uploads, and writeback.

OpenRouter and Mistral are present only as ignored owner-local environment variables outside public Git. The public browser code must not read or call those providers. OpenAI local key material from the June 30 lane remains removed.

## FACT

- `.vercel/project.json` exists locally and links this repo to a Vercel project, with sensitive IDs kept out of public artifacts.
- Vercel project/deployment connector checks showed ready static deployments from `main`.
- `vercel.json` now keeps `/dashboard` and `/dashboard/` routed to the internal static dashboard while `/` serves the public MVP landing.
- No `railway.json`, `nixpacks.toml`, `Procfile`, or `Dockerfile` exists in the public repo.
- Railway MCP status checks returned no linked project.
- Static browser code uses local assets and dashboard data only; it does not call OpenRouter, Mistral, OpenAI, or Ollama.
- `garak`, `nemoguardrails`, and `nvidia-smi` are not installed in this environment, so no NVIDIA safety checker was run.

## INTERPRETATION

The safe current architecture is:

1. Vercel/static for the last-known public site and internal dashboard view.
2. Codex/local operator for edits, review, Git, and public-safe knowledge updates.
3. OpenRouter/Mistral only behind a future approved server-side bridge.
4. Railway only after the backend contract, auth, budget, secret storage, and data policy are explicit.

## GAP

- No deployed current MVP URL has been produced in this pass.
- No Railway project or service has been created.
- No `/api/jarvis` or equivalent backend bridge exists.
- No provider-call budget, model list refresh, logging policy, or data-class approval is active.
- No live Nexus/Obsidian writeback, Figma sync, or Notion deployed-URL update was performed.

## Recommended Next Bridge Contract

The first server-side bridge should be minimal:

- endpoint: `/api/jarvis` or `/api/agent-command`;
- input: sanitized dashboard packet only;
- secrets: `OPENROUTER_API_KEY` read only from server env or provider secret store;
- response: reviewed draft packet with model ID, cost estimate, source labels, and confidence;
- writes: zero automatic Git, Notion, WikiLLM, Telegram, or Obsidian writeback;
- gates: budget limit, public-safety screen, timeout/retry policy, and human approval before external or durable writes.

## Decision

Do not connect OpenRouter from static browser JavaScript. Build a local bridge or Railway backend first, then attach the dashboard to that bridge only after approval and validation.
