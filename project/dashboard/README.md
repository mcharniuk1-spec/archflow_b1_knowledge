# Local Operator Dashboard

This is the Phase 2 dashboard for ArchFlow Block 1.

It is a read-only control panel and Jarvis command shell generated from public project files. It is not the project brain and it does not replace WikiLLM, Obsidian, LangSmith, GitHub, or Codex.

Current stable protected review route:

```text
https://public-mcharniuk1-4994-mcharniuk1-4994s-projects.vercel.app/project/dashboard/
```

Current deployment target: hidden-link Vercel preview first. Hidden link is convenience, not security. Use Vercel platform protection or a server-side auth gate before exposing private state, commands, uploads, voice execution, memory controls, or non-public data.

## Run

From the repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open:

```text
http://127.0.0.1:8765/project/dashboard/
```

## Vercel Preview

Deploy from the public repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
npx vercel --yes --target preview
```

The preview should be opened at:

```text
https://<deployment>/project/dashboard/
```

The root `vercel.json` sets `noindex` headers and disables cache for dashboard files and `data.json`. This does not authenticate the page.

## What It Shows

- Overview and recent activity.
- WikiLLM memory, decisions, issues, and runs.
- Graphify status and future graph links.
- LangGraph nodes, routing, review gates, and stop logic.
- LlamaIndex-style local query test over approved public files.
- CrewAI agents, roles, tasks, and expected outputs.
- LangSmith tracing readiness and safe trace rules.
- Env/config and runtime package status.
- E1.3 KB writeback/readback derived gate status and evidence links.
- Jarvis normal/interview mode shell.
- Browser-local voice command placeholder and local file metadata packet creation.
- In-page refresh: manual button, Jarvis refresh command, focus refresh, and timed polling of `data.json`.

## Change Config

- LangGraph nodes and routing: `project/workflows/langgraph-controller.yaml`
- CrewAI roles and task outputs: `project/workflows/crewai-crew.yaml`
- LlamaIndex corpus and retrieval parameters: `project/workflows/llamaindex-rag.yaml`
- Model routing: `project/config/model-routing.yaml`
- Dashboard data extraction: `project/scripts/generate-dashboard-data.py`
- Dashboard UI: `project/dashboard/app.js` and `project/dashboard/styles.css`

Regenerate `project/dashboard/data.json` after changing any workflow, config, WikiLLM, report, or run file.

On Vercel, the dashboard can update in-page without reloading the page after a new `data.json` has been deployed. It cannot observe local file changes, write to GitHub/Notion/WikiLLM, process private uploads, or run live voice execution without a backend.

## Reliability Sync

After each substantial dashboard/Jarvis execution:

1. Write a public-safe run note under `project/runs/`.
2. Append the durable memory summary under `wiki/runs/`, `wiki/memory.md`, and `wiki/log.md`.
3. Regenerate `project/dashboard/data.json`.
4. Run the public safety, workflow, dashboard JSON, JavaScript, and runtime guard checks.
5. Commit and push the tracked source update.
6. Update Notion append-only with the protected preview URL, GitHub commit, verification status, and remaining gated work.

The web view is reliable only for deployed public-safe source state. It does not provide always-on execution, writeback, model calls, or local Codex availability until a backend/local bridge is explicitly approved and implemented.

## Jarvis Boundary

Allowed in the static preview:

- status/readback answers from deployed `data.json`;
- manual refresh and polling without page reload;
- browser-local voice transcript command during the current browser session when the user authorizes voice;
- browser-local file metadata packet creation without reading document bodies;
- downloadable local packets for later Codex/Railway writeback.

Deferred to Vercel server/auth or Railway backend:

- Google account auth;
- durable file uploads;
- raw transcript storage;
- Notion/GitHub/WikiLLM writes;
- SSE/websocket live events;
- background workers and queues;
- OpenAI/Mistral/Ollama provider calls;
- any private dashboard state.

## Boundary

The dashboard reads public-safe files and ignored local env presence only. It must not display real API keys, raw private transcripts, private workspace links, or local absolute paths.
