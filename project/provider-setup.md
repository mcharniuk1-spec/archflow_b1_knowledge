# Provider and local setup

ArchFlow’s useful core is deliberately boring to start: it needs no model key. You can validate the contracts, regenerate the dashboard, retrieve source-linked context, compose a Jarvis work packet, and run the fixed engineering fixtures without sending material to a provider.

The setup is split into four local profiles so an individual or team installs only what they need.

| Profile | What it adds | Default |
|---|---|---|
| `core` | Standard-library schemas, generator, dashboard, and benchmark | Ready without installation |
| `validation` | Pydantic and YAML contract validation | Optional pinned environment |
| `agentic` | LangGraph smoke, CrewAI contract check, LlamaIndex import check | Optional and provider-disabled |
| `jarvis` | FastAPI compatibility-service tests | Optional and provider-disabled |

Inspect the plan first:

```bash
python3 project/scripts/setup-local.py --profile all
```

Install into the ignored project-local environment only when required:

```bash
python3.12 project/scripts/setup-local.py --profile validation --locked --install --verify
python3.12 project/scripts/setup-local.py --profile agentic --locked --install --verify
python3.12 project/scripts/setup-local.py --profile jarvis --locked --install --verify
```

`--install` may download packages. The helper never inserts credentials, starts a service, calls a provider, deploys, or writes to an external system.

## Credential boundary

The root `.env.example` and `project/config/providers.env.example` contain empty server-side names for possible platforms. Put a real value only in an ignored local file, OS keychain, hosting-platform secret, or approved secret manager. Never paste it into Jarvis, the dashboard, a screenshot, a report, Git, or a client-side variable.

`project/config/provider-registry.json` is the public adapter truth. The only implemented provider state is `none`. Ollama, OpenRouter, OpenAI, Anthropic, Gemini, and Mistral are documented extension points; LangSmith is an observability extension. None has a provider-execution route in this release.

## What an adapter must prove

A future adapter is a separate implementation task. Before activation it must have:

1. a server-side or loopback-only boundary with no browser credential access;
2. an explicit approved input and forbidden-data contract;
3. current model and pricing verification at activation time, without committing a snapshot;
4. timeout, retry, budget, and hard-stop behavior;
5. fixed success and abuse fixtures plus an independent reviewer;
6. a provider-disabled fallback;
7. exact authority for any downstream action, with rollback or idempotency and readback.

A key’s presence, a model name, an import, or a health response proves none of those things by itself.

## Optional observability

LangSmith stays off. If an approved runtime needs tracing, use `project/config/langsmith.env.example` as a name-only template, enable tracing explicitly for that run, and send only sanitized state admitted by its source contract. Never publish a trace link or credential-presence signal as proof of product behavior.

## Optional local service

The Jarvis compatibility profile can be tested on loopback after its environment is installed. It returns review packets only; it has no model adapter or writeback authority.

```bash
cd services/jarvis-api
../../project/local/venv-setup/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8787
```

Stop the service after the test. Binding it publicly or deploying it changes the boundary and requires a separate deployment contract.
