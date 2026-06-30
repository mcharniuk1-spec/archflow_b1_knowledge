#!/usr/bin/env python3
"""Generate public-safe dashboard data from the ArchFlow repository.

This script intentionally uses only the Python standard library. It reads
tracked public project files plus ignored local env/runtime file presence, but
never emits secret values or raw local paths.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
WIKI = ROOT / "wiki"
DASHBOARD = PROJECT / "dashboard"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path, limit: int | None = None) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    return text if limit is None else text[:limit]


def public_excerpt(text: str, limit: int = 1200) -> str:
    sanitized_lines = []
    secret_line = re.compile(r"^(\s*[A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD)[A-Z0-9_]*\s*=\s*)(.+)$")
    for line in text.splitlines():
        sanitized_lines.append(secret_line.sub(r"\1<not-shown>", line))
    return " ".join(sanitized_lines)[:limit]


def title_for(path: Path) -> str:
    if not path.exists():
        return path.name
    for line in read(path, 1200).splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return path.name


def first_match(text: str, pattern: str, default: str = "") -> str:
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else default


def list_files(base: Path, suffixes: tuple[str, ...] = (".md", ".yaml", ".yml")) -> list[Path]:
    if not base.exists():
        return []
    skip_parts = {".git", "local", "__pycache__"}
    result: list[Path] = []
    for path in sorted(base.rglob("*")):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        if skip_parts.intersection(path.relative_to(ROOT).parts):
            continue
        if path.name.startswith(".env"):
            continue
        result.append(path)
    return result


def parse_section_items(text: str, section_name: str) -> list[str]:
    lines = text.splitlines()
    capture = False
    items: list[str] = []
    for line in lines:
        if re.match(rf"^{section_name}:\s*$", line):
            capture = True
            continue
        if capture and re.match(r"^[a-zA-Z0-9_]+:\s*", line) and not line.startswith((" ", "-")):
            break
        if capture:
            m = re.match(r"^\s{2}([a-zA-Z0-9_]+):\s*$", line)
            if m:
                items.append(m.group(1))
    return items


def parse_mapping_block(text: str, section_name: str) -> dict[str, dict[str, str | list[str]]]:
    lines = text.splitlines()
    capture = False
    current: str | None = None
    block: dict[str, dict[str, str | list[str]]] = {}
    current_list_key: str | None = None
    for line in lines:
        if re.match(rf"^{section_name}:\s*$", line):
            capture = True
            continue
        if capture and re.match(r"^[a-zA-Z0-9_]+:\s*", line) and not line.startswith((" ", "-")):
            break
        if not capture:
            continue
        m_current = re.match(r"^\s{2}([a-zA-Z0-9_]+):\s*$", line)
        if m_current:
            current = m_current.group(1)
            block[current] = {}
            current_list_key = None
            continue
        if current is None:
            continue
        m_key = re.match(r"^\s{4}([a-zA-Z0-9_]+):\s*(.*)$", line)
        if m_key:
            key, value = m_key.groups()
            value = value.strip().strip('"')
            if value:
                block[current][key] = value
                current_list_key = None
            else:
                block[current][key] = []
                current_list_key = key
            continue
        m_list = re.match(r"^\s{6}-\s*(.*)$", line)
        if m_list and current_list_key:
            value = m_list.group(1).strip()
            target = block[current].setdefault(current_list_key, [])
            if isinstance(target, list):
                target.append(value)
    return block


def parse_langgraph() -> dict:
    path = PROJECT / "workflows" / "langgraph-controller.yaml"
    text = read(path) if path.exists() else ""
    nodes = []
    node_blocks = parse_mapping_block(text, "nodes")
    for node_id, data in node_blocks.items():
        nodes.append(
            {
                "id": node_id,
                "owner": str(data.get("owner_agent", "")),
                "purpose": str(data.get("purpose", "")),
                "output": data.get("output", ""),
            }
        )
    edges = []
    edge: dict[str, str] = {}
    in_edges = False
    for line in text.splitlines():
        if line.startswith("edges:"):
            in_edges = True
            continue
        if in_edges and re.match(r"^[a-zA-Z0-9_]+:", line):
            break
        if not in_edges:
            continue
        m_start = re.match(r"^\s{2}-\s+from:\s*(.*)$", line)
        if m_start:
            if edge:
                edges.append(edge)
            edge = {"from": m_start.group(1).strip()}
            continue
        m_key = re.match(r"^\s{4}(to|condition):\s*(.*)$", line)
        if m_key:
            edge[m_key.group(1)] = m_key.group(2).strip()
    if edge:
        edges.append(edge)
    return {
        "path": rel(path),
        "status": first_match(text, r"^status:\s*(.*)$", "missing"),
        "runtime": first_match(text, r"^runtime:\s*(.*)$", "unknown"),
        "purpose": first_match(text, r"purpose:\s*>\n\s*(.*)$", ""),
        "nodes": nodes,
        "edges": edges,
        "params": {
            "checkpointer": first_match(text, r"^\s{2}checkpointer:\s*(.*)$"),
            "observability": first_match(text, r"^\s{2}observability:\s*(.*)$"),
            "max_revision_loops": first_match(text, r"^\s{2}max_revision_loops:\s*(.*)$"),
            "human_approval_required_before_publication": first_match(
                text, r"^\s{2}human_approval_required_before_publication:\s*(.*)$"
            ),
        },
    }


def parse_crewai() -> dict:
    path = PROJECT / "workflows" / "crewai-crew.yaml"
    text = read(path) if path.exists() else ""
    agents = []
    for agent_id, data in parse_mapping_block(text, "agents").items():
        agents.append(
            {
                "id": agent_id,
                "role": str(data.get("role", "")),
                "goal": str(data.get("goal", "")),
                "skills": data.get("skills", []),
            }
        )
    tasks = []
    task: dict[str, str] = {}
    in_tasks = False
    for line in text.splitlines():
        if line.startswith("tasks:"):
            in_tasks = True
            continue
        if in_tasks and re.match(r"^[a-zA-Z0-9_]+:", line):
            break
        if not in_tasks:
            continue
        m_start = re.match(r"^\s{2}-\s+id:\s*(.*)$", line)
        if m_start:
            if task:
                tasks.append(task)
            task = {"id": m_start.group(1).strip()}
            continue
        m_key = re.match(r"^\s{4}(agent|expected_output):\s*(.*)$", line)
        if m_key:
            task[m_key.group(1)] = m_key.group(2).strip()
    if task:
        tasks.append(task)
    return {
        "path": rel(path),
        "status": first_match(text, r"^status:\s*(.*)$", "missing"),
        "runtime": first_match(text, r"^runtime:\s*(.*)$", "unknown"),
        "process": first_match(text, r"^process:\s*(.*)$", "unknown"),
        "memory": first_match(text, r"^memory:\s*(.*)$", "unknown"),
        "cache": first_match(text, r"^cache:\s*(.*)$", "unknown"),
        "planning": first_match(text, r"^planning:\s*(.*)$", "unknown"),
        "agents": agents,
        "tasks": tasks,
        "limitations": re.findall(r"^\s{2}-\s*(.*)$", text.split("current_limitations:", 1)[-1], re.MULTILINE)
        if "current_limitations:" in text
        else [],
    }


def parse_llamaindex() -> dict:
    path = PROJECT / "workflows" / "llamaindex-rag.yaml"
    text = read(path) if path.exists() else ""
    include = re.findall(r"^\s{4}-\s*(.*)$", text.split("include:", 1)[-1].split("exclude:", 1)[0], re.MULTILINE) if "include:" in text else []
    exclude = re.findall(r"^\s{4}-\s*(.*)$", text.split("exclude:", 1)[-1].split("indexing_parameters:", 1)[0], re.MULTILINE) if "exclude:" in text else []
    return {
        "path": rel(path),
        "status": first_match(text, r"^status:\s*(.*)$", "missing"),
        "runtime": first_match(text, r"^runtime:\s*(.*)$", "unknown"),
        "include": include,
        "exclude": exclude,
        "chunk_size": first_match(text, r"^\s{2}chunk_size:\s*(.*)$"),
        "chunk_overlap": first_match(text, r"^\s{2}chunk_overlap:\s*(.*)$"),
        "similarity_top_k": first_match(text, r"^\s{2}similarity_top_k:\s*(.*)$"),
        "persist_dir": first_match(text, r"^\s{2}persist_dir:\s*(.*)$"),
        "limitations": re.findall(r"^\s{2}-\s*(.*)$", text.split("current_limitations:", 1)[-1], re.MULTILINE)
        if "current_limitations:" in text
        else [],
    }


def env_status() -> list[dict]:
    local_env = PROJECT / ".env.local"
    local_langsmith = PROJECT / ".env.langsmith.local"
    langsmith_key_present = False
    if local_langsmith.exists():
        for line in read(local_langsmith).splitlines():
            if line.startswith("LANGSMITH_API_KEY=") and line.split("=", 1)[1].strip():
                langsmith_key_present = True
    return [
        {"name": "Provider example", "path": "project/config/providers.env.example", "status": "tracked_example"},
        {"name": "LangSmith example", "path": "project/config/langsmith.env.example", "status": "tracked_example"},
        {"name": "Local provider env", "path": "project/.env.local", "status": "present_ignored" if local_env.exists() else "missing"},
        {
            "name": "Local LangSmith env",
            "path": "project/.env.langsmith.local",
            "status": "key_present_ignored" if langsmith_key_present else ("present_key_missing" if local_langsmith.exists() else "missing"),
        },
        {
            "name": "Runtime package project",
            "path": "project/pyproject.toml",
            "status": "missing_not_installed" if not (PROJECT / "pyproject.toml").exists() else "present",
        },
        {
            "name": "Local RAG index",
            "path": "project/local/rag_index",
            "status": "present_ignored" if (PROJECT / "local" / "rag_index").exists() else "not_generated",
        },
    ]


def package_status() -> list[dict]:
    runtime_python = PROJECT / "local" / "venv" / "bin" / "python"
    python_bin = runtime_python if runtime_python.exists() else Path(sys.executable)
    checks = {
        "langgraph": "LangGraph runtime",
        "crewai": "CrewAI runtime",
        "llama_index": "LlamaIndex runtime",
        "langsmith": "LangSmith SDK",
        "streamlit": "Streamlit dashboard runtime",
        "fastapi": "FastAPI dashboard runtime",
    }
    results = []
    for module, label in checks.items():
        probe = subprocess.run(
            [str(python_bin), "-c", f"import {module}"],
            text=True,
            capture_output=True,
            cwd=ROOT,
        )
        status = "installed" if probe.returncode == 0 else "not_installed"
        results.append(
            {
                "module": module,
                "label": label,
                "status": status,
                "runtime": "project_local_venv" if runtime_python.exists() else "current_python",
            }
        )
    return results


def activity_items() -> list[dict]:
    files = []
    for base, kind in [
        (PROJECT / "runs", "project_run"),
        (PROJECT / "reports", "project_report"),
        (WIKI / "runs", "wiki_run"),
        (WIKI / "decisions", "wiki_decision"),
        (WIKI / "issues", "wiki_issue"),
    ]:
        for path in list_files(base, (".md", ".pdf")):
            files.append(
                {
                    "kind": kind,
                    "path": rel(path),
                    "title": title_for(path) if path.suffix == ".md" else path.name,
                    "modified": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                    "size": path.stat().st_size,
                }
            )
    return sorted(files, key=lambda x: x["modified"], reverse=True)


def wiki_summary() -> dict:
    files = []
    for path in list_files(WIKI, (".md",)):
            files.append(
                {
                    "path": rel(path),
                    "title": title_for(path),
                    "excerpt": public_excerpt(read(path, 900), 420),
                }
            )
    return {
        "index_path": "wiki/index.md",
        "memory_path": "wiki/memory.md",
        "insights_path": "wiki/insights.md",
        "file_count": len(files),
        "files": files,
    }


def graphify_status() -> dict:
    candidates = [
        ROOT / "reference" / "graphify",
        ROOT / "graphify-out",
        PROJECT / "reference" / "graphify",
    ]
    existing = [rel(p) for p in candidates if p.exists()]
    return {
        "status": "available" if existing else "planned_not_generated",
        "paths": existing,
        "recommended_next": "Regenerate Graphify after code or workflow changes."
        if existing
        else "Generate Graphify after runtime code exists, then link the graph report here.",
    }


def corpus() -> list[dict]:
    docs = []
    for base in [PROJECT, ROOT / "history", ROOT / "skills", WIKI]:
        for path in list_files(base, (".md", ".yaml", ".yml")):
            text = read(path, 1600)
            docs.append(
                {
                    "path": rel(path),
                    "title": title_for(path),
                    "text": public_excerpt(text, 1200),
                }
            )
    return docs



def e13_gate_status() -> dict:
    run_dir = PROJECT / "runs" / "E1.3" / "2026-06-30-kb-readback"
    required = [
        run_dir / "source-registry.md",
        run_dir / "kb-writeback-report.md",
        run_dir / "kb-readback-report.md",
        run_dir / "review-report.md",
        run_dir / "run-summary.md",
        run_dir / "agent-handout.md",
        run_dir / "e1_3_readback_results.json",
        WIKI / "runs" / "2026-06-30-e1-3-kb-readback.md",
    ]
    evidence = [{"path": rel(path), "status": "present" if path.exists() else "missing"} for path in required]
    results_path = run_dir / "e1_3_readback_results.json"
    result_status = "missing"
    passed_count = 0
    assertion_count = 0
    if results_path.exists():
        try:
            loaded = json.loads(read(results_path))
            result_status = str(loaded.get("status", "unknown"))
            passed_count = int(loaded.get("passed_count", 0))
            assertion_count = int(loaded.get("assertion_count", 0))
        except (json.JSONDecodeError, ValueError):
            result_status = "invalid_json"
    if all(item["status"] == "present" for item in evidence) and result_status == "passed":
        derived = "readback_passed"
    elif any(item["status"] == "present" for item in evidence):
        derived = "in_progress"
    else:
        derived = "not_started"
    return {
        "label": "E1.3 KB writeback/readback",
        "source": "project/project-plan.md",
        "planned_status": "Review" if derived == "readback_passed" else "To Do",
        "derived_status": derived,
        "readback_status": result_status,
        "passed_count": passed_count,
        "assertion_count": assertion_count,
        "required_evidence": evidence,
        "readback_assertions": [
            "current mission",
            "next step",
            "forbidden actions",
            "existing outputs",
            "open gaps",
            "agent roles",
            "LangGraph route",
            "ICP boundary",
            "dashboard and voice gate",
            "public reporting gate",
        ],
    }


def main() -> None:
    langgraph = parse_langgraph()
    crewai = parse_crewai()
    llamaindex = parse_llamaindex()
    e13_gate = e13_gate_status()
    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": {
            "name": "ArchFlow Block 1 Knowledge",
            "mode": "phase_2_local_dashboard",
            "operator": "Codex",
            "memory_layer": "WikiLLM files",
            "dashboard_rule": "control panel, not primary brain",
        },
        "status_cards": [
            {"label": "LangGraph", "value": langgraph["status"], "tone": "ok"},
            {"label": "CrewAI", "value": crewai["status"], "tone": "ok"},
            {"label": "LlamaIndex", "value": llamaindex["status"], "tone": "ok"},
            {"label": "WikiLLM files", "value": f"{wiki_summary()['file_count']} files", "tone": "ok"},
            {"label": "Activity files", "value": str(len(activity_items())), "tone": "ok"},
            {"label": "Local dashboard", "value": "static_read_only", "tone": "ok"},
            {"label": "E1.3 readback", "value": e13_gate["derived_status"], "tone": "ok" if e13_gate["derived_status"] == "readback_passed" else "warn"},
        ],
        "langgraph": langgraph,
        "crewai": crewai,
        "llamaindex": llamaindex,
        "env": env_status(),
        "packages": package_status(),
        "activity": activity_items(),
        "wiki": wiki_summary(),
        "graphify": graphify_status(),
        "gates": {"e1_3": e13_gate},
        "corpus": corpus(),
        "sources": [
            {"label": "LangGraph overview", "url": "https://docs.langchain.com/oss/python/langgraph/overview"},
            {"label": "LangGraph Studio / LangSmith Studio", "url": "https://docs.langchain.com/langsmith/studio"},
            {"label": "LangSmith observability", "url": "https://docs.langchain.com/langsmith/observability"},
            {"label": "CrewAI crews", "url": "https://docs.crewai.com/en/concepts/crews"},
            {"label": "LlamaIndex concepts", "url": "https://developers.llamaindex.ai/python/framework/getting_started/concepts/"},
            {"label": "Ollama API", "url": "https://docs.ollama.com/api/introduction"},
            {"label": "NVIDIA NeMo Agent Toolkit", "url": "https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html"},
        ],
    }
    DASHBOARD.mkdir(parents=True, exist_ok=True)
    (DASHBOARD / "data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"wrote {rel(DASHBOARD / 'data.json')}")


if __name__ == "__main__":
    main()
