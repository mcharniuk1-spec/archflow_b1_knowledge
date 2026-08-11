# Deterministic public system core

This directory is the machine-checkable center of the generic ArchFlow tool. It contains one state model, one canonical 21-role catalog, a seven-layer knowledge-crew configuration, strict case and action schemas, synthetic fixtures, and a provider-disabled validator.

Run:

```bash
python3 project/system/validate_system.py
```

The validator checks state ordering and gates, exact role/catalog projection, skill and tool ceilings, reviewer-route closure, four smallest-responsible role packs, exact-manifest retrieval settings, the synthetic knowledge case, action eligibility, adversarial fixtures, and zero provider or external writes.

The system is a contract and fixture set. It does not prove that a model, CrewAI crew, LangGraph process, provider, hosted service, shared database, deployment, or external action is running.
