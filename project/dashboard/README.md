# Local Operator Dashboard

This is the Phase 2 dashboard for ArchFlow Block 1.

It is a static source-state control panel and Jarvis command shell generated from public project files. It can hold browser-local draft graph edits and review packets, but it cannot write back to source files by itself. It is not the project brain and it does not replace WikiLLM, Obsidian, LangSmith, GitHub, or Codex.

Protected review route format:

```text
https://<protected-preview-host>/project/dashboard/
```

Review-branch local deep links:

```text
http://127.0.0.1:8765/project/dashboard/#jarvis
http://127.0.0.1:8765/project/dashboard/#history
http://127.0.0.1:8765/project/dashboard/#service
http://127.0.0.1:8765/project/dashboard/#schema
http://127.0.0.1:8765/project/dashboard/#config
http://127.0.0.1:8765/project/dashboard/#plan
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

## Static Smoke Test

For dashboard/Jarvis UI changes, run the rendered-route smoke test from the repository root:

```bash
python3 project/scripts/dashboard-static-smoke.py
```

What it proves:

- `#jarvis`, `#history`, `#service`, `#schema`, `#config`, and `#plan` render in headless Chrome.
- `?panel=svc-intake#service` and `?panel=architecture-review#schema` open the large node control panel on initial render for the two required modes.
- `(1) PRD/ICP Flow` and `(2) Agent Orchestra` expose their required source, node, provider-boundary, and approval-gate markers.
- The node control panel exposes Inputs, Outputs, Configuration, Prompts, Safety, and provider/writeback boundary text.
- Rendered HTML does not expose obvious provider secret patterns.
- The static UI performs no provider calls and no writeback.

What it does not prove:

- real microphone permission or speaker output on the owner's browser;
- node-modal click-through quality on mobile;
- Railway/local bridge, provider, Nexus, Notion, GitHub, or WikiLLM writeback.

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
- Current-session Jarvis chat history with export/clear controls.
- Browser-local voice input through Web Speech recognition where supported.
- Browser-local speech output through Web Speech synthesis where supported.
- `(1) PRD/ICP Flow` block-schema page for the externally showable service product path.
- `(2) Agent Orchestra` block-schema page for the local Codex/LangGraph/WikiLLM/Graphify control system.
- Full node control panels with inputs, outputs, run notes, system prompts, comments, config dropdowns, and connection summaries.
- Config/subprompting page for browser-local prompt candidates and exportable review packets.
- Project Plan page for the E1-E7 spine and current source links.
- Browser-local file metadata packet creation.
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
4. Run the public safety, workflow, dashboard JSON, JavaScript, rendered-route smoke, and runtime guard checks.
5. Commit and push the tracked source update.
6. Update Notion append-only with the protected preview URL, GitHub commit, verification status, and remaining gated work.

The web view is reliable only for deployed public-safe source state. It does not provide always-on execution, writeback, model calls, or local Codex availability until a backend/local bridge is explicitly approved and implemented.

## Jarvis Boundary

Allowed in the static preview:

- status/readback answers from deployed `data.json`;
- manual refresh and polling without page reload;
- current-session Jarvis chat history in browser session storage;
- browser-local voice transcript command during the current browser session when the user authorizes voice and the browser supports recognition;
- browser-local speech output when the user enables spoken replies and the browser exposes speech synthesis voices;
- browser-local file metadata packet creation without reading document bodies;
- downloadable local packets for later Codex/Railway writeback.

Voice verification boundary:

- Headless checks can verify that the voice controls render and JavaScript syntax passes.
- A real microphone/speaker test requires the owner's interactive browser permission on the local device.
- Browser speech voices are device/browser dependent. The dashboard can request a natural English voice when one is installed, but it cannot guarantee a specific human voice without an approved voice provider or local TTS runtime.

Deferred to Vercel server/auth or Railway backend:

- Google account auth;
- durable file uploads;
- raw transcript storage;
- Notion/GitHub/WikiLLM writes;
- SSE/websocket live events;
- background workers and queues;
- OpenRouter/Mistral/OpenAI/Ollama provider calls;
- any private dashboard state.

Provider state as of 2026-07-01:

- `OPENROUTER_API_KEY` and `MISTRAL_API_KEY` are stored only in the root ignored local `.env.local`.
- the June 30 OpenAI local key file was removed;
- static Vercel/client JavaScript must not read provider env vars or call providers directly;
- provider use requires an approved local bridge or backend with server-side secret access, budget limits, source labels, and review before any writeback.

## Boundary

The dashboard reads public-safe files and ignored local env presence only. It must not display real API keys, raw private transcripts, private workspace links, or local absolute paths.
