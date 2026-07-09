# Package To Repo Mapping

Run: `2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration`

This file records how the owner-approved package was integrated without blindly copying it.

## Package Summary

Source package: `archflow_8_07/`

Package files inspected:

- `README.md`
- `reports/ArchFlow_00_Source_Register_and_Founder_Meeting_Delta_v2.*`
- `reports/ArchFlow_01_Current_Architecture_and_Setup_v2.*`
- `reports/ArchFlow_02_Service_Company_and_Operations_Model_v2.*`
- `reports/ArchFlow_03_Market_ICP_Positioning_Content_and_Sales_v2.*`
- `reports/ArchFlow_04_Tools_Automation_Agent_Strategy_and_Roadmap_v2.*`
- `reports/ArchFlow_05_Hermes_Watchdog_CAG_RAG_Integration_Plan_v2.*`
- `prompts/01_codex_global_agent_loop_prompt_v2.md`
- `prompts/02_archflow_codex_project_configuration_prompt_v2.md`
- `prompts/03_hermes_watchdog_controller_prompt_v2.md`
- `prompts/04_cag_rag_context_capsule_prompt_v2.md`
- `prompts/05_subagent_task_contract_prompt_v2.md`
- `prompts/06_skill_registry_hook_governance_prompt_v2.md`
- `prompts/07_market_content_sales_execution_prompt_v2.md`
- `prompts/08_e1_e7_notion_task_update_prompt_v2.md`
- `prompts/09_final_git_website_dashboard_kb_publish_prompt_v2.md`
- `implementation_files/AGENTS.md.draft`
- `implementation_files/CODEX_EXECUTION_PLAN.md`
- `implementation_files/architecture-finalization-checklist.md`
- `implementation_files/content-template-system.md.draft`
- `implementation_files/hermes-watchdog.yaml.draft`
- `implementation_files/notion-e1-e7-update-plan.md.draft`
- `implementation_files/skills-governance.md.draft`
- the implementation draft for task representation without Linear
- `schemas/context-capsule.schema.json`

## Mapping Table

| Package item | Repo integration target | Integration action |
|---|---|---|
| Report 00 source register and founder delta | `project/reports/2026-07-08-founder-meeting-v2-watchdog-cag-rag-architecture.md`, run handout | Summarized as accepted package inputs, deltas, and gated claims. Raw report files are not copied. |
| Report 01 current architecture | `project/agentic-stack.md`, `project/workflows/langgraph-controller.yaml`, architecture report | Added Hermes/CAG/RAG overlay while preserving current LangGraph/CrewAI/LlamaIndex/Codex boundaries. |
| Report 02 service operations | `project/runs/.../service-operations-model.md`, `project/project-plan.md`, content/sales templates | Added service-company operating model, QA gates, artifact packages, and offer ladder. |
| Report 03 market/ICP/content/sales | `project/content/templates/`, `project/project-plan.md`, run market/content packet | Added ICP, competitor positioning, discovery-call flow, sales offer, and corrected 70/20/10 content rule. |
| Report 04 tools/automation/agent strategy | `project/context/`, `project/agents/skills-governance.md`, workflows | Added CAG context layer and governance boundaries without activating paid tools or broad ingestion. |
| Report 05 Hermes/CAG/RAG plan | `project/workflows/langgraph-controller.yaml`, `project/agents/agent-roster.yaml`, prompts | Added planned Hermes watchdog/controller role and subagent task-contract method. |
| Prompt 01 Codex global loop | `project/runs/.../prompts/01_codex_system_prompt_v2.md` | Adapted into a repo-safe Codex system prompt complement. |
| Prompt 02 ArchFlow Codex config | `AGENTS.md`, `project/operating-rules.md`, run prompt pack | Integrated as short routing rules and detailed run prompt. |
| Prompt 03 Hermes watchdog | `project/runs/.../prompts/03_hermes_watchdog_controller_prompt_v2.md` | Adapted as final Hermes prompt. |
| Prompt 04 CAG/RAG capsule | `project/context/context-capsule.schema.json`, `project/context/cag-core.yaml`, run capsule | Implemented schema, core, retrieval policy, and sample run capsule. |
| Prompt 05 subagent task contract | `project/runs/.../task-contracts.md`, `project/workflows/langgraph-controller.yaml` | Added standard bounded task contract and used it for this run's subagents. |
| Prompt 06 skill governance | `project/agents/skills-governance.md`, `project/agents/skills-by-agent.md`, hook scripts | Added skill visibility policy, add-skill checklist, and reminder routing. |
| Prompt 07 market/content/sales | `project/content/templates/`, `project/project-plan.md` | Integrated with latest owner correction: 70% static, 20% carousel/checklist/template, 10% short video. |
| Prompt 08 E1-E7 update | `project/runs/.../notion-e1-e7-update-packet.md`, `project/project-plan.md` | Added Notion-ready Markdown task blocks without mutating Notion. |
| Prompt 09 final publish | `project/runs/.../final-publish-plan.md`, agent handout | Prepared approval-gated Git/website/dashboard/KB/Notion sequence only. |
| `AGENTS.md.draft` | `AGENTS.md` | Integrated as short routing addendum, not a long global prompt copy. |
| `hermes-watchdog.yaml.draft` | `project/workflows/langgraph-controller.yaml`, `project/agents/agent-roster.yaml` | Merged planned nodes and role metadata; no runtime claim. |
| `skills-governance.md.draft` | `project/agents/skills-governance.md` | Expanded with current project skill audit and role-specific visibility. |
| `content-template-system.md.draft` | `project/content/templates/README.md` and new templates | Integrated with corrected 70/20/10 distribution. |
| `notion-e1-e7-update-plan.md.draft` | `project/runs/.../notion-e1-e7-update-packet.md` | Converted to Notion-ready blocks, no external writeback. |
| Task representation without Linear draft | `project/runs/.../task_repr_without_linear.md` | Adopted repo-native task packet policy; Linear remains optional. |
| Context capsule schema | `project/context/context-capsule.schema.json` | Adapted and extended for provenance, validation, provider policy, and side-effect policy. |

## Conflicts And Corrections

- Package content rule says 90% static/text/template and 10% video. Latest owner instruction says 70% static educational/analytical, 20% carousel/checklist/template, and 10% short video. Repo integration uses the latest owner instruction.
- Package material is planning-approved, but not all public claims are evidence-approved. Runtime, provider, customer demand, ROI, paid client, writeback, Railway, Linear, voice, and SaaS readiness claims remain downgraded unless supported by current repo evidence.
- Linear is not required. Repo-native Markdown/YAML/JSON packets remain default.
- Hermes is watchdog/controller/reviewer only. Codex remains executor/integrator and final file-edit boundary.

## Files Not Touched

- Package source files under `archflow_8_07/`.
- Secret or local runtime files.
- Private source exports.
- Notion, Linear, Telegram, Railway, provider, Figma, Git remote, or deployment state.

## Validation Recommendations

- YAML parse for changed workflow and roster files.
- JSON parse for context schema, run capsule, and dashboard data.
- Python compile for changed scripts/API code.
- Dashboard data regeneration when public text changes.
- Public safety scan.
- `git diff --check`.
- Final QA reviewer after implementation.
