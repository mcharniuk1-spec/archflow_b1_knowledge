# ArchFlow Public Agent Contract

This repository is a generic public tool. Do not infer private workspace access, personal memory, credentials, provider authority, deployment authority, or permission to write externally.

## Read first

1. `README.md`
2. `project/README.md`
3. `project/operating-rules.md`
4. `project/context/cag-core.yaml`
5. `project/agents/agent-roster.yaml`
6. `project/agents/skills-governance.md`
7. `project/config/provider-registry.json`
8. the relevant workflow and portable `SKILL.md` contracts for the task

## Operating contract

- Keep tracked content English and public-safe.
- Never commit personal identifiers, customer material, private URLs, local absolute paths, raw transcripts, credentials, credential-presence state, browser profiles, recovery bundles, or unreviewed run archives.
- Start with a bounded objective, decision, source allowlist, exclusions, expected output, owner, independent reviewer, checks, retry cap, and stop conditions.
- Retrieve only from `project/dashboard/corpus-manifest.json` unless the caller explicitly supplies a different safe corpus. Return source paths and verify exact passages.
- Use the smallest functional role and skill set that owns the output, its checks, review, and integration. The roster is configuration, not proof that agents ran.
- Keep one writer per shared target. For parallel work, coordinate through an ignored caller-supplied packet under `project/local/communication/` or the browser Communication Center.
- Treat LangGraph as the state-owner contract, CrewAI as an optional reviewed role/task projection, and LlamaIndex as bounded retrieval rather than authority or durable memory.
- Keep `ARCHFLOW_PROVIDER_MODE=none` unless a separate task explicitly authorizes and proves an adapter. Never activate a provider or infer permission from a key name.
- Require a maker/checker split and independent verdict for substantial work. A model response or successful command is not a result receipt.
- Ask for explicit target-specific approval before Git mutation, deployment, publication, provider use on non-public material, dependency installation, messaging, database mutation, external writeback, or destructive/irreversible action.
- Promote only reviewed reusable meaning through the retained solution/action-memory schemas with provenance, owner, freshness, and supersession.

## Verify before handoff

Run the smallest relevant checks and record what was not run. For a full public-product change, use:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/benchmark-actionable-agents.py
python3 project/system/validate_system.py
python3 project/scripts/auth-contract-smoke.py
python3 project/scripts/browser-v3-smoke.py
python3 scripts/public_safety_scan.py
```

Provider calls and external writes must remain zero unless the task has a separately approved action packet and exact readback.
