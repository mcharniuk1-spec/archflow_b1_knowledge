# Quickstart

This repository is a local-first reference implementation. It starts a static public site and generated dashboard data; it does not start providers, background agents, external writeback, or a production database.

## Prerequisites

- Git
- Python 3.11 or later
- Node.js only for the optional JavaScript syntax check

The generator and static server use the Python standard library. A clean clone does not depend on an ignored virtual environment.

## Run the public console

```bash
git clone <your-fork-or-repository-url> archflow
cd archflow
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open these local routes:

- `http://127.0.0.1:8765/` — public product surface
- `http://127.0.0.1:8765/project/dashboard/` — architecture and operating console
- `http://127.0.0.1:8765/jarvis` — guarded review-packet interface

## Try the workflow safely

1. In the dashboard, open **Operations**.
2. Choose **Knowledge Service** or **Agent Control**.
3. Read the input and authority boundaries.
4. Select **Prepare review bundle**.
5. Download the browser-local bundle and have an approved operator decide whether any repository change is appropriate.

The visible stage sequence is a local preparation preview. It does not run a model, create a file, invoke a subagent, write a database record, commit code, or push Git.

## Verify a checkout

The first three checks use the standard library plus Node for syntax. Workflow validation needs the optional development dependency:

```bash
python3 -m pip install -r project/requirements-dev.txt
```

```bash
python3 project/scripts/generate-dashboard-data.py
python3 scripts/public_safety_scan.py
node --check project/dashboard/app.js
python3 project/scripts/validate-workflows.py
python3 project/scripts/dashboard-static-smoke.py --timeout 20 --retries 2
```

Run the Jarvis contract checks only when their documented local dependencies are installed:

```bash
python3 -m pip install -r services/jarvis-api/requirements.txt
python3 project/scripts/jarvis-api-contract-smoke.py
python3 project/scripts/jarvis-serverless-owner-guard-smoke.py
```

## Before enabling anything beyond the demo

Read [security and data boundaries](security-and-data-boundaries.md), [operations](operations.md), and the repository operating rules. Provider use, private corpus processing, external writeback, deployment, and Git push each need their own explicit approval and verification path.
