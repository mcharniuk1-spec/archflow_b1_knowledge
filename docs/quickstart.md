# Quickstart

ArchFlow's first proof is local, synthetic, provider-disabled, and standard-library only.

## Requirements

- Git
- Python 3.11+
- Node.js for the JavaScript syntax check
- Chrome/Chromium only for full route rendering

## Clone and prove the core

```bash
git clone <your-repository-url> archflow
cd archflow
python3 project/system/validate_system.py
```

Expected:

- seven layers, twenty-one roles, ten packs, and a 12,000-token capsule validate;
- one bounded synthetic proposal is eligible;
- stale, authority-spoof, target-escape, and reviewer-spoof proposals are blocked;
- malformed proposals are rejected;
- every proposal reports `executed: false`.

## Start the Crew Desk

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/project/dashboard/#today`.

Use Today for orientation, Work for a mission, Knowledge for architecture/methods, Team for roles, Review for trace/gates, and Set up for local proposals.

## Verify the public surface

```bash
python3 project/system/validate_system.py
python3 project/scripts/generate-dashboard-data.py
python3 -m json.tool project/dashboard/data.json >/dev/null
node --check project/dashboard/app.js
python3 project/scripts/dashboard-static-smoke.py --skip-browser
python3 project/scripts/pre-push-runtime-guard.py
python3 scripts/public_safety_scan.py
```

Full route render:

```bash
python3 project/scripts/dashboard-static-smoke.py
```

Optional YAML workflow validation needs the development dependencies:

```bash
python3 -m pip install -r project/requirements-dev.txt
python3 project/scripts/validate-workflows.py
```

## Optional framework-runtime proof

The public core does not require LangGraph, LlamaIndex, or CrewAI to display and validate the contracts. If you intentionally install those frameworks in `project/local/venv`, request their deeper provider-disabled probes explicitly:

```bash
ARCHFLOW_VERIFY_OPTIONAL_RUNTIME=1 python3 project/scripts/pre-push-runtime-guard.py
```

This check is bounded by timeouts, submits no trace, calls no model, and performs no writeback. A missing, stale, or timed-out optional environment is a runtime GAP; it does not change the passing status of the standard-library public core.

## Adapt safely

Start with one employee role, one decision, one current source set, one approved requirement, one reversible output, and one different reviewer. Do not ingest a whole device or vault.

Keep private knowledge in an approved local/private system and secrets in app-native auth or an OS keychain. The browser dashboard is never a secret store.

Read [the complete architecture](responsive-knowledge-crew-architecture.md), [adaptation guide](adapting-archflow.md), and [security boundary](security-and-data-boundaries.md) before adding a provider, persistence, private retrieval, or write adapter.
