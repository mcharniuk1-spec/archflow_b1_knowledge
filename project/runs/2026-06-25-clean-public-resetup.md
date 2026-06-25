# Run - Clean Public Resetup

Date: 2026-06-25
Scope: public project folder

## Task

Create a clean public-safe project folder for the ArchFlow reset. Translate the private project board into English. Keep prior work as sanitized history. Prepare provider setup templates for Ollama local mode and Codex operator mode without storing secrets.

## Inputs Reviewed

- Existing resetup package from 2026-06-24.
- Private project board epics and tasks.
- Existing local provider state.
- Current public-safety requirements.

## Outputs Created

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `project/README.md`
- `project/operating-rules.md`
- `project/project-plan.md`
- `project/agentic-stack.md`
- `project/provider-setup.md`
- `project/config/providers.env.example`
- `project/config/model-routing.yaml`
- `project/scripts/check-ollama.sh`
- `project/scripts/smoke-test-ollama-qwythos.sh`
- `project/prompts/af-graph.md`
- `project/prompts/af-review.md`
- `history/previous-work-summary.md`
- `history/legacy-file-inventory.md`
- `history/resetup-summary-2026-06-24.md`
- `history/notion-plan-ingest-2026-06-25.md`
- `skills/skills-used.md`
- `PUBLICATION_REVIEW.md`
- `CHANGELOG.md`

## Checks

- Public files are ASCII-only.
- No local absolute paths found in public files.
- No private Notion URLs found in public files.
- No raw user IDs found in public files.
- No personal owner names from the private task board copied into public files.
- Provider files contain env var names only, not secret values.
- `project/config/model-routing.yaml` parses as YAML.
- Clean Git repository initialized inside `public/`.
- Branch renamed to `main`.
- Files intentionally left uncommitted pending public author identity approval.

## Provider State

FACT: Ollama CLI is installed.

FACT: The local Ollama server was not running during the check.

FACT: Local Ollama manifests include a Qwythos model with Q4_K_M quantization.

FACT: Codex auth is available as operator runtime auth, not as an API key for external frameworks.

GAP: Ollama has not been started or smoke-tested in this run.

## Next Approval Needed

Approve these before activation:

1. Start `ollama serve`.
2. Run `project/scripts/check-ollama.sh`.
3. Run `project/scripts/smoke-test-ollama-qwythos.sh`.
4. Create `.env.local` from `project/config/providers.env.example`.
5. Approve Git author identity and create the first commit.
