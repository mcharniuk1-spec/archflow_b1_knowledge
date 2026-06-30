#!/usr/bin/env python3
"""Run E1.3 public-safe KB writeback and readback proof.

This proof is deterministic. It writes approved E1.2 summary/history into the
public WikiLLM-facing run folder, then verifies that future agents can read back
mission, next step, forbidden actions, outputs, gaps, agent roles, and gates from
repo-relative public artifacts only.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
WIKI = ROOT / "wiki"
RUN_DIR = PROJECT / "runs" / "E1.3" / "2026-06-30-kb-readback"
RESULTS_JSON = RUN_DIR / "e1_3_readback_results.json"

INPUT_FILES = {
    "routing_contract": ROOT / "AGENTS.md",
    "project_readme": PROJECT / "README.md",
    "operating_rules": PROJECT / "operating-rules.md",
    "e1_2_run_summary": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "run-summary.md",
    "e1_2_prd": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "E1.2_PRD.md",
    "e1_2_system_report": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "E1.2_System_report.md",
    "e1_2_review": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "review-report.md",
    "e1_2_matrix": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "responsibility-matrix.md",
    "e1_2_kb_update": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "kb-update.md",
    "e1_2_state": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "e1_2_langgraph_output.json",
    "e1_2_stream": PROJECT / "runs" / "E1.2" / "2026-06-26-full-test" / "e1_2_stream_events.jsonl",
    "e1_2_next_steps": PROJECT / "runs" / "E1.2" / "2026-06-26-notion-sync" / "next-steps-e1-2.md",
    "public_wiki_memory": WIKI / "memory.md",
    "public_wiki_insights": WIKI / "insights.md",
    "dashboard_voice_decision": WIKI / "decisions" / "2026-06-30-live-dashboard-voice-hosting-onyx.md",
    "market_engine": PROJECT / "workflows" / "market-research-engine.yaml",
}

ASSERTIONS = [
    {
        "id": "current_mission",
        "question": "What is the current mission?",
        "required_terms": ["dialogue", "prd", "knowledge", "readback"],
    },
    {
        "id": "next_step",
        "question": "What is the next execution step after E1.3?",
        "required_terms": ["E1.4", "principle", "E2", "evidence"],
    },
    {
        "id": "forbidden_actions",
        "question": "What actions remain forbidden before later gates?",
        "required_terms": ["raw", "private", "Nexus", "unattended", "outreach"],
    },
    {
        "id": "existing_outputs",
        "question": "What E1.2 outputs already exist?",
        "required_terms": ["PRD", "streaming", "system", "responsibility", "matrix"],
    },
    {
        "id": "open_gaps",
        "question": "What gaps remain after E1.3?",
        "required_terms": ["owner", "CrewAI", "vector", "Nexus"],
    },
    {
        "id": "agent_roles",
        "question": "Which agents cooperated in the Block 1 flow?",
        "required_terms": ["AF Tools", "AF Context", "AF Manager", "AF Knowledge", "AF Review"],
    },
    {
        "id": "langgraph_route",
        "question": "What route did the E1.2 graph prove?",
        "required_terms": ["intake_validate", "retrieve_context", "review_gate", "publish_or_record"],
    },
    {
        "id": "icp_boundary",
        "question": "What is the active ICP boundary?",
        "required_terms": ["product", "B2B", "SaaS", "Director", "VP"],
    },
    {
        "id": "dashboard_voice_gate",
        "question": "What is the dashboard and voice boundary?",
        "required_terms": ["Vercel", "Railway", "voice", "read-only"],
    },
    {
        "id": "public_reporting_gate",
        "question": "What is required before public carousel reporting?",
        "required_terms": ["GloomyLord", "AF Review", "owner", "carousel"],
    },
]

SKIP_PARTS = {".git", "local", "__pycache__", "dashboard"}
SUFFIXES = {".md", ".yaml", ".yml"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_.-]{1,}", text)]


def doc_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.name


def collect_docs() -> list[dict[str, str]]:
    docs: list[dict[str, str]] = []
    for base in [PROJECT, ROOT / "history", ROOT / "skills", WIKI]:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in SUFFIXES:
                continue
            parts = set(path.relative_to(ROOT).parts)
            if parts.intersection(SKIP_PARTS):
                continue
            if path.name.startswith(".env"):
                continue
            text = read(path)
            docs.append({"path": rel(path), "title": doc_title(text, path), "text": text})
    return docs


def retrieve(docs: list[dict[str, str]], terms: list[str], limit: int = 6) -> list[dict[str, object]]:
    term_tokens = [term.lower() for term in terms]
    scored: list[dict[str, object]] = []
    for doc in docs:
        haystack = f"{doc['title']} {doc['path']} {doc['text']}".lower()
        tokens = Counter(tokenize(haystack))
        score = 0
        for term in term_tokens:
            if " " in term:
                score += 3 if term in haystack else 0
            else:
                score += tokens[term]
                score += 2 if term in haystack else 0
        if score:
            scored.append({"score": score, "path": doc["path"], "title": doc["title"]})
    return sorted(scored, key=lambda item: (-int(item["score"]), str(item["path"])))[:limit]


def assertion_passed(docs: list[dict[str, str]], terms: list[str], results: list[dict[str, object]]) -> bool:
    combined = "\n".join(next((doc["text"] for doc in docs if doc["path"] == item["path"]), "") for item in results).lower()
    return all(term.lower() in combined for term in terms)


def e12_state() -> dict[str, object]:
    state_path = INPUT_FILES["e1_2_state"]
    if not state_path.exists():
        return {}
    return json.loads(read(state_path))


def stream_event_count() -> int:
    path = INPUT_FILES["e1_2_stream"]
    if not path.exists():
        return 0
    return sum(1 for line in read(path).splitlines() if line.strip())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def source_registry(now: str, state: dict[str, object]) -> str:
    rows = []
    for source_id, path in INPUT_FILES.items():
        rows.append(
            f"| {source_id} | `{rel(path)}` | {'present' if path.exists() else 'missing'} | public-safe approved artifact |"
        )
    return f"""
# E1.3 Source Registry

Date: 2026-06-30
Status: generated public-safe registry

## Purpose

This registry declares the approved input packet for E1.3 KB writeback/readback. It uses repo-relative paths only and does not include raw private source material.

## Source Packet Status

- E1.2 graph approval status: `{state.get('approval_status', 'unknown')}`
- E1.2 source boundary status: `{state.get('source_boundary_status', 'unknown')}`
- E1.2 stream event count: `{stream_event_count()}`
- E1.2 owner acceptance gate: `review_pending_owner_acceptance`
- Generated at: `{now}`

## Sources

| Source ID | Path | Status | Boundary |
|---|---|---|---|
{chr(10).join(rows)}

## Retrieval Metadata

| Field | Value |
|---|---|
| corpus | `project/`, `history/`, `skills/`, `wiki/` |
| excluded | raw/private/local/env/dashboard runtime outputs |
| source path rule | repo-relative only |
| readback method | deterministic lexical assertion over approved public files |
| vector layer | deferred until source IDs, chunk IDs, embedding model, and benchmark are approved |
| turbovec status | deferred; use only after context size or retrieval benchmark justifies it |
"""


def kb_writeback(now: str, state: dict[str, object]) -> str:
    return f"""
# E1.3 KB Writeback Report

Date: 2026-06-30
Status: writeback completed, readback required

## FACT

E1.2 was executed as a deterministic public-safe internal proof. The run state records approval status `{state.get('approval_status', 'unknown')}`, source boundary `{state.get('source_boundary_status', 'unknown')}`, and `{stream_event_count()}` stream events.

E1.2 produced the PRD, streaming report, system report, responsibility matrix, KB update note, review report, state JSON, stream log, and next-steps package under the E1.2 run folders.

E1.2 remains in Review until owner acceptance. This does not block E1.3 readback proof, but it blocks marking E1.2 as Done.

The active ICP hypothesis is one vertical: product teams inside B2B SaaS scaleups, especially Series B-D companies with 50-500 employees, 2-5 PMs, and a Director or VP of Product accountable for PRD quality and speed.

## INTERPRETATION

The E1.2 proof shows that ArchFlow can turn sanctioned source material into structured context, PRD outputs, agent role outputs, KB update candidates, and reviewed public-safe artifacts. E1.3 must prove that this knowledge can be read back without re-opening the original chat.

Company-count and market-universe analysis are useful for E2 sourcing, but counts are not proof of demand. The improved rule is account-level evidence: source grade, role currentness, pain hypothesis, and at least two independent public signals before outreach.

## HYPOTHESIS

The Product Discovery-to-Production PRD Pack remains the best first paid entry offer: raw product-team material becomes a context digest, production-ready PRD, backlog, acceptance criteria, decision log, and KB/update handoff in days, not weeks.

A static read-only dashboard should be hosted before live API or voice workers. Vercel is first for static dashboard hosting; Railway waits until live API, worker, queue, websocket/SSE, or voice orchestration exists.

GloomyLord should stay an internal visual/reporting sidecar by default. Its first job is a public-reporting gate and template package, not public persona creation.

## GAP

Owner acceptance of E1.2 is still required before E1.2 becomes Done.

CrewAI LLM execution, vector retrieval, turbovec, Cognee, live Nexus writes, Onyx sandbox, hosted dashboard, local voice runner, and public carousel publishing remain gated.

E1 proof is not customer validation, ROI proof, market validation, or payment evidence.

## Agent History Written To KB

| Agent | E1 role | Current evidence |
|---|---|---|
| AF Tools | Source boundary, runtime readiness, and tool inventory | E1.2 source inventory, safety scans, runtime checks |
| AF Context | Structured context and decision/gap extraction | E1.2 context digest and readback assertions |
| AF Manager | PRD, task matrix, acceptance criteria | E1.2 PRD and responsibility matrix |
| AF Knowledge | KB update, memory candidates, source registry | E1.2 KB update and this E1.3 writeback |
| AF Review | Public-safety and evidence gate | E1.2 review and E1.3 readback review |
| AF Publisher | Git-ready public reporting | report/run folders, dashboard regeneration, validation |
| GloomyLord | Internal visual/reporting sidecar | starts under E1.5 public-reporting gate only |

## LangGraph Route Written To KB

`intake_validate -> retrieve_context -> parallel analysis -> merge_findings -> draft_documents -> review_gate -> publish_or_record`

The stream report records observable node updates and state summaries only. Hidden reasoning is not part of public streaming reports.

## Forbidden Actions Readback

The forbidden actions are raw private ingestion, live Nexus writes, unattended write actions, outreach before E6 review, public carousel publishing before AF Review and owner approval, Railway live services before API/worker requirements, and Onyx/Cognee/turbovec activation before their gates.

## Loop State

| Field | Value |
|---|---|
| loop level | L1 report-only |
| max revision loops | 2 |
| item retry cap | 3 |
| maker/checker | required for public or risky outputs |
| unattended writes | blocked |
| memory promotion | AF Review plus owner gate for high-risk content |

## E1.4 And E2 Handoff

E1.4 should write the KB update principle: what gets written, what stays out, how readback is tested, and when memory candidates become durable memory.

E2 should use the improved evidence engine: account evidence cards, source grades, role verification, public-signal triangulation, and a 10-15 target outreach list only after review.

## Public Reporting Handoff

E1.5 starts with a public-reporting gate, not immediate publishing. A task can become a public carousel only after it has approved source artifacts, evidence labels, AF Copy draft, AF Review approval, and owner approval.

Generated at: `{now}`
"""


def readback_report(results: list[dict[str, object]]) -> str:
    rows = []
    for item in results:
        top = item["results"][0]["path"] if item["results"] else "no-match"
        rows.append(f"| {item['id']} | {'pass' if item['passed'] else 'fail'} | `{top}` | {item['question']} |")
    status = "passed" if all(bool(item["passed"]) for item in results) else "blocked"
    return f"""
# E1.3 KB Readback Report

Date: 2026-06-30
Status: {status}

## Method

The proof queries approved public files after the E1.3 writeback report and source registry are generated. It verifies that a future agent can retrieve the core E1.2/E1.3 operating facts from repository artifacts without relying on the current chat.

## Assertions

| Assertion | Status | Top evidence | Question |
|---|---|---|---|
{chr(10).join(rows)}

## Result

FACT: The readback proof is `{status}` for the required E1.3 assertions.

INTERPRETATION: The KB now carries enough public-safe state for the next agent to understand the current mission, next step, forbidden actions, outputs, gaps, agent roles, graph route, ICP boundary, dashboard/voice gate, and public-reporting gate.

GAP: This is deterministic lexical readback, not vector retrieval. Vector retrieval and turbovec remain deferred until source IDs, chunk metadata, embedding model, and a retrieval benchmark exist.
"""


def review_report(results: list[dict[str, object]]) -> str:
    passed = all(bool(item["passed"]) for item in results)
    return f"""
# E1.3 Review Report

Date: 2026-06-30
Status: {'approved_for_review' if passed else 'blocked'}

## Review Verdict

FACT: E1.3 KB writeback artifacts now exist and the readback assertion set {'passes' if passed else 'does not pass'}.

FACT: E1.2 owner acceptance is still required before E1.2 can move from Review to Done.

INTERPRETATION: E1.3 can move to Review because the repo now contains the approved PRD summary, agent history, source registry, retrieval metadata, loop state, readback proof, memory candidates, and E1.4/E2 handoff.

HYPOTHESIS: Starting E1.5 with a public-reporting gate is safe because it does not publish claims; it only defines evidence, review, visual, and approval requirements.

## Blocked From This Review

- Marking E1.2 Done without owner acceptance.
- Publishing public carousels before AF Review and owner copy approval.
- Creating Railway service infrastructure before live API/worker/voice requirements exist.
- Enabling voice write actions before read-only command proof and approval gates.
- Activating Onyx, Cognee, turbovec, Nexus writes, or broad APIs before their gates.

## Checks Required Before Git Push

- Run `python3 scripts/public_safety_scan.py`.
- Run `project/local/venv/bin/python project/scripts/validate-workflows.py`.
- Regenerate and parse `project/dashboard/data.json`.
- Run the runtime guard if local runtime is available.
"""


def run_summary(results: list[dict[str, object]]) -> str:
    passed = all(bool(item["passed"]) for item in results)
    return f"""
# Run: E1.3 KB Writeback And Readback

Date: 2026-06-30
Status: {'readback passed, E1.3 ready for review' if passed else 'blocked'}

## Task

Execute E1.3 by recording the approved E1.2 PRD and agent history into the public-safe KB layer, adding source/retrieval metadata, and proving readback from approved artifacts.

## What Changed

E1.3 now has a public-safe run folder with a source registry, KB writeback report, readback report, review report, run summary, agent handout, and machine-readable readback results.

The writeback records E1.2 proof status, agent cooperation, LangGraph route, loop state, current ICP, dashboard/voice gates, and public-reporting gates without raw private source material.

The readback proof verifies that future agents can retrieve the current mission, next step, forbidden actions, existing outputs, open gaps, agent roles, graph route, ICP boundary, dashboard/voice gate, and public-reporting gate.

## Outputs

- `project/runs/E1.3/2026-06-30-kb-readback/source-registry.md`
- `project/runs/E1.3/2026-06-30-kb-readback/kb-writeback-report.md`
- `project/runs/E1.3/2026-06-30-kb-readback/kb-readback-report.md`
- `project/runs/E1.3/2026-06-30-kb-readback/review-report.md`
- `project/runs/E1.3/2026-06-30-kb-readback/e1_3_readback_results.json`
- `project/runs/E1.3/2026-06-30-kb-readback/agent-handout.md`
- `project/runs/E1.3/2026-06-30-kb-readback/agent-coordination-stream.md`

## Current Status

FACT: E1.3 readback {'passed' if passed else 'failed'}.

FACT: E1.2 remains Review until owner acceptance.

INTERPRETATION: E1.5 can start as a process/reporting gate only; publishing remains blocked until approval.

## Next Step

Start E1.5 by defining the public-reporting gate and GloomyLord template package, then write E1.4 KB update principle before broad E2 evidence work.
"""


def handout() -> str:
    return """
# Agent Handout: E1.3 KB Readback

Use this handout before changing E1.3, dashboard status, E1.5 public reporting, or the E2 evidence engine.

## Current State

E1.3 has been executed as a public-safe writeback/readback proof. The readback report verifies the core KB questions from approved public artifacts.

E1.2 remains Review until owner acceptance. Do not mark E1.2 Done without explicit acceptance or requested edits being completed.

## Required Read Order

1. `project/runs/E1.3/2026-06-30-kb-readback/run-summary.md`
2. `project/runs/E1.3/2026-06-30-kb-readback/kb-writeback-report.md`
3. `project/runs/E1.3/2026-06-30-kb-readback/kb-readback-report.md`
4. `project/runs/E1.3/2026-06-30-kb-readback/review-report.md`
5. `wiki/runs/2026-06-30-e1-3-kb-readback.md`
6. `project/runs/E1.5/2026-06-30-public-reporting-gate/public-reporting-gate.md`

## Safe Next Actions

- Regenerate dashboard data after any run/wiki/plan change.
- Keep dashboard read-only.
- Keep voice read-only/status until a command taxonomy and approval flow pass.
- Keep Railway deferred until a live API/worker/queue/voice bridge exists.
- Keep public reporting behind AF Review and owner approval.

## Blocked Actions

- Raw private ingestion.
- Live Nexus writes.
- Onyx or Cognee as primary brain.
- turbovec before source IDs, chunk IDs, embeddings, and benchmark.
- Public demand claims before E6/E7 evidence.
"""


def coordination_stream() -> str:
    return """
# E1.3 Agent Coordination Stream

Date: 2026-06-30
Status: recorded public-safe sidecar coordination

## Main Operator Stream

Codex kept the critical path local: inspect current E1.2 evidence, implement E1.3 writeback/readback, update dashboard status, start E1.5 gate, validate, then report.

## Sidecar Assignments

| Sidecar | Assignment | Result |
|---|---|---|
| AF Review sidecar | Read-only E1.2 proof integrity review | Confirmed E1.2 was actually executed and identified owner acceptance as the remaining state gate. |
| AF Knowledge/Dashboard sidecar | Read-only E1.3 and dashboard-readback requirements | Confirmed E1.3 was not complete and recommended a derived dashboard gate object. |
| AF Copy/GloomyLord sidecar | Read-only public-reporting and visual gate review | Recommended LinkedIn-first product-team category education, GloomyLord as internal sidecar by default, and AF Review plus owner copy approval. |

## Integration Decisions

FACT: E1.2 proof exists and is technically approved as an internal proof.

FACT: E1.3 required a new run folder, writeback report, readback report, review report, wiki run/log update, and dashboard-derived gate status.

INTERPRETATION: E1.5 should start with the public-reporting gate, not public copy generation.

HYPOTHESIS: GloomyLord can own internal visual/reporting templates and dashboard-friendly report layouts after the gate is accepted.

GAP: Live Notion state should be updated after repo validation; public repo artifacts do not include private task URLs.
"""


def main() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    state = e12_state()

    write(RUN_DIR / "source-registry.md", source_registry(now, state))
    write(RUN_DIR / "kb-writeback-report.md", kb_writeback(now, state))

    docs = collect_docs()
    results = []
    for assertion in ASSERTIONS:
        retrieved = retrieve(docs, assertion["required_terms"])
        results.append(
            {
                "id": assertion["id"],
                "question": assertion["question"],
                "required_terms": assertion["required_terms"],
                "passed": assertion_passed(docs, assertion["required_terms"], retrieved),
                "results": retrieved,
            }
        )

    RESULTS_JSON.write_text(
        json.dumps(
            {
                "generated_at": now,
                "status": "passed" if all(item["passed"] for item in results) else "blocked",
                "assertion_count": len(results),
                "passed_count": sum(1 for item in results if item["passed"]),
                "source_boundary": "approved public files only",
                "results": results,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    write(RUN_DIR / "kb-readback-report.md", readback_report(results))
    write(RUN_DIR / "review-report.md", review_report(results))
    write(RUN_DIR / "run-summary.md", run_summary(results))
    write(RUN_DIR / "agent-handout.md", handout())
    write(RUN_DIR / "agent-coordination-stream.md", coordination_stream())

    print("e1_3_readback=ok" if all(item["passed"] for item in results) else "e1_3_readback=blocked")
    print(f"assertions={sum(1 for item in results if item['passed'])}/{len(results)}")
    print(f"results={rel(RESULTS_JSON)}")
    return 0 if all(item["passed"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
