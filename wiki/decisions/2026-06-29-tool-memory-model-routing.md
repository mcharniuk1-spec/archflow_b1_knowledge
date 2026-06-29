# Decision - Tool Memory And Model Routing

Date: 2026-06-29

## Decision

Use Loop Engineering now as the operating contract. Keep WikiLLM as canonical memory. Keep LlamaIndex as the retrieval abstraction. Defer Cognee, turbovec, and Mistral until their gates pass.

## Rationale

FACT: The current public project already has Codex as operator, LangGraph as controller, CrewAI role contracts, LlamaIndex retrieval, WikiLLM memory, Ollama local model routing, and LangSmith tracing.

INTERPRETATION: Adding another active brain or vector layer before E1.3 readback would increase failure modes. The missing near-term layer is loop discipline: state, stop conditions, review, and memory promotion.

HYPOTHESIS: Cognee and turbovec will become valuable after E1.3/E2 create enough approved artifacts and source metadata to test recall and dense retrieval.

GAP: Mistral credentials, live model preflight, OCR model selection, Cognee sandbox, turbovec benchmark, and E7 demand verdict are not complete.

## Consequences

- Loop artifacts live under `project/loops/`.
- E2 market research uses `project/workflows/market-research-engine.yaml`.
- Mistral is disabled by default and only allowed on sanitized inputs after approval.
- Cognee must not replace WikiLLM.
- turbovec must stay behind LlamaIndex and use ignored local storage.
