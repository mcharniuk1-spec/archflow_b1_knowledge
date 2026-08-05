# ArchFlow Crew Desk

The Crew Desk is the primary non-technical, browser-local projection of the responsive knowledge crew.

Routes:

- `#today` — mission and Taras onboarding guidance;
- `#work` — one case/mission and materialized per-role task/handoff contracts;
- `#knowledge` — layers, systems, parameters, diagrams, research, and skill lifecycle;
- `#team` — twenty-one canonical role contracts and ten adaptive packs;
- `#review` — trace, gates, receipts, and promotion;
- `#setup` — bounded local configuration proposals.

The dashboard loads:

- `project/system/contracts/knowledge-crew-config.json`
- `project/system/contracts/role-catalog.json`
- `project/system/contracts/role-workflows.json`
- `project/system/contracts/operating-model.json`
- `project/dashboard/data.json`

It stores mission/setup/example drafts in browser local storage and can export JSON review packets containing schema-backed role-task bindings. Role authority fields remain read-only, and missing sources/requirements/targets stay visible. It does not run agents, contact a model, checkpoint a graph, write a database, mutate Git, deploy, send, or promote knowledge.

## Run

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/project/dashboard/#today`.

## Verify

```bash
node --check project/dashboard/app.js
python3 project/scripts/dashboard-static-smoke.py --skip-browser
python3 project/scripts/dashboard-static-smoke.py
```

`/dashboard` redirects here. `/jarvis` redirects to `#today`; there is no separate Jarvis source of truth.

See [Crew Desk Operating Manual](../../docs/dashboard-operating-manual.md).
