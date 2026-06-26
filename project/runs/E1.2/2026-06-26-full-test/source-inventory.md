# Source Inventory

Date: 2026-06-26
Run: E1.2 full public-safe proof test
Status: approved public-safe source packet

## Approved Inputs

| Source | Role | Boundary |
|---|---|---|
| `project/workflows/langgraph-controller.yaml` | LangGraph state, nodes, edges, and review gate contract. | Public repo file. |
| `project/workflows/crewai-crew.yaml` | CrewAI agent roles, tasks, process, and limitations. | Public repo file. |
| `project/workflows/llamaindex-rag.yaml` | Approved corpus and retrieval parameters. | Public repo file. |
| `project/workflows/knowledge-integration.yaml` | WikiLLM, Graphify, Obsidian mirror, Nexus, and runtime-layer responsibilities. | Public repo file. |
| `project/runs/2026-06-26-june24-next-steps-proof/` | E1.1 completion and E1.2 preparation artifacts. | Public-safe derived artifacts only. |
| `wiki/memory.md` | Stable public memory and current runtime decisions. | Public WikiLLM file. |
| `wiki/insights.md` | Reusable design insights. | Public WikiLLM file. |
| `graphify-out/GRAPH_REPORT.md` | Generated public repo graph summary. | Generated structural reference. |
| Official docs checked on 2026-06-26 | Current tendencies for LangGraph, CrewAI, LlamaIndex, and LangSmith. | Technical reference only; no private data. |

## Blocked Inputs

- Raw private dialogue, transcripts, Notion pages, credentials, private workspace links, screenshots, PDFs, deployment metadata, and local absolute paths.
- Live Obsidian/Nexus write operations.
- Customer-facing claims about validated demand, ROI, or paying users.

## Source Conclusion

FACT: The E1.2 proof can proceed from the public setup state and sanitized E1.2 preparation artifacts.

INTERPRETATION: The source set is enough to test the workflow mechanics, document generation, agent division, runtime review, and system review.

GAP: A real client or customer dialogue source is not approved for public ingestion yet. This proof therefore validates the internal machinery, not market demand.
