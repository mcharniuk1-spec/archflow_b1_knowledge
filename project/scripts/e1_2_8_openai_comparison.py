#!/usr/bin/env python3
"""Run E1.2.8 provider comparison with OpenAI using sanitized payload only."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


PUBLIC_ROOT = Path(__file__).resolve().parents[2]
PRIVATE_ROOT = PUBLIC_ROOT.parent
RUN_DIR = PUBLIC_ROOT / "project" / "runs" / "E1.2" / "2026-07-02-testmeeting-local"
CONTINUATION_DIR = PUBLIC_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture"
PAYLOAD_PATH = CONTINUATION_DIR / "openai-sanitized-provider-payload.json"
ROOT_ENV = PRIVATE_ROOT / ".env.local"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def api_request(method: str, url: str, api_key: str, payload: dict | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=body, method=method)
    request.add_header("Authorization", f"Bearer {api_key}")
    if body is not None:
        request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def choose_model(models_payload: dict, preferred: str | None) -> tuple[str, str]:
    ids = sorted(item.get("id", "") for item in models_payload.get("data", []) if item.get("id"))
    if preferred and preferred in ids:
        return preferred, "preferred_env_model_available"
    priority = [
        "gpt-4.1-mini",
        "gpt-4o-mini",
        "gpt-5.4-mini",
        "gpt-5-mini",
    ]
    for model in priority:
        if model in ids:
            return model, "low_cost_structured_comparison_model"
    for model in ids:
        if "mini" in model.lower() and model.startswith("gpt"):
            return model, "first_available_gpt_mini_model"
    for model in ids:
        if model.startswith("gpt"):
            return model, "first_available_gpt_model"
    raise RuntimeError("no_openai_gpt_model_available")


def extract_output_text(response: dict) -> str:
    if response.get("output_text"):
        return str(response["output_text"])
    chunks: list[str] = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                chunks.append(str(content["text"]))
    return "\n".join(chunks).strip()


def write_status(status: str, reason: str, extra: dict | None = None) -> None:
    extra = extra or {}
    status_md = CONTINUATION_DIR / "openai-provider-status.md"
    status_md.write_text(
        "\n".join(
            [
                "# OpenAI Provider Comparison Status",
                "",
                f"Date: {now_utc()}",
                f"Status: {status}",
                f"Reason: {reason}",
                "",
                "## Boundary",
                "",
                "- Input kind: sanitized digest only.",
                "- Raw private source sent: false.",
                "- API keys are not written to public files.",
                "- Cost is not estimated without current pricing proof.",
                "",
                "## Details",
                "",
                "```json",
                json.dumps(extra, indent=2, sort_keys=True),
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    load_env(ROOT_ENV)
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        write_status("blocked", "OPENAI_API_KEY_missing")
        return 2

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    prompt = (
        "You are AF Review for ArchFlow. Use only the sanitized JSON payload below. "
        "Do not infer raw private source details. Do not claim customer validation, ROI, "
        "provider readiness, Railway readiness, Telegram delivery, or Notion writeback. "
        "Return Markdown with the expected sections.\n\n"
        f"{json.dumps(payload, indent=2, sort_keys=True)}"
    )

    try:
        models_payload = api_request("GET", "https://api.openai.com/v1/models", api_key)
        model, model_reason = choose_model(models_payload, os.getenv("OPENAI_MODEL", "").strip() or None)
        request_payload = {
            "model": model,
            "input": prompt,
            "max_output_tokens": 1400,
            "store": False,
        }
        response = api_request("POST", "https://api.openai.com/v1/responses", api_key, request_payload)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:1200]
        write_status("blocked", f"openai_http_error_{exc.code}", {"error_excerpt": body})
        return 3
    except Exception as exc:
        write_status("blocked", type(exc).__name__, {"error_excerpt": str(exc)[:1200]})
        return 4

    output = extract_output_text(response)
    if not output:
        write_status("blocked", "empty_openai_response", {"response_id": response.get("id")})
        return 5

    output_path = RUN_DIR / "E1.2.8_OpenAI_Comparison.md"
    output_path.write_text(
        "\n".join(
            [
                "# E1.2.8 OpenAI Provider Comparison",
                "",
                f"Date: {now_utc()}",
                f"Provider: OpenAI",
                f"Model: {model}",
                f"Model selection: {model_reason}",
                "Input kind: sanitized digest only",
                "Raw private source sent: false",
                "",
                output.strip(),
                "",
            ]
        ),
        encoding="utf-8",
    )

    usage = response.get("usage", {})
    ledger = {
        "timestamp_utc": now_utc(),
        "run_id": "2026-07-02-e1-2-testmeeting-dashboard-architecture",
        "task_role_and_langgraph_node": payload["model_route_profile"]["task_role_and_langgraph_node"],
        "query_shape": payload["model_route_profile"]["query_shape"],
        "graph_node_path": payload["model_route_profile"]["graph_node_path"],
        "model_route_profile": "openai_low_cost_structured_comparison",
        "provider": "openai",
        "model_id": model,
        "model_role": "execution_pool_structured_comparison",
        "prompt_version": "e1_2_8_openai_comparison_v1",
        "source_ids_used": payload["source_boundary"]["source_ids_used"],
        "input_artifact": "project/runs/2026-07-02-e1-2-testmeeting-dashboard-architecture/openai-sanitized-provider-payload.json",
        "output_artifact": "project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_OpenAI_Comparison.md",
        "context_window_tokens": "not_reported",
        "prompt_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "actual_or_estimated_cost": "not_estimated_without_current_pricing_proof",
        "cost_currency": "USD",
        "pricing_source": "not_fetched_in_run",
        "budget_cap": "under_1.99_usd_run_cap_required",
        "budget_remaining": "not_estimated",
        "decision": "provider_comparison_generated_for_review",
        "reviewer_model_id": "Codex operator",
        "human_gate_required": True,
        "runtime_source": "openai_responses_api_sanitized_payload",
        "status": "completed",
        "error_type": None,
        "response_id_recorded": bool(response.get("id")),
        "raw_private_source_sent": False,
    }
    ledger_path = RUN_DIR / "openai-model-call-ledger.jsonl"
    with ledger_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(ledger, sort_keys=True) + "\n")

    budget_path = RUN_DIR / "openai-budget-guard.json"
    budget_path.write_text(
        json.dumps(
            {
                "status": "completed_without_cost_estimate",
                "daily_budget_usd": 5.0,
                "run_hard_stop_usd": 1.99,
                "provider_calls": 1,
                "input_kind": "sanitized_digest_only",
                "raw_private_source_sent": False,
                "cost_note": "No cost estimate stored because current pricing was not fetched in this run.",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    write_status("completed", "openai_comparison_generated", {"model": model, "usage": usage})
    print(f"openai_comparison=completed model={model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
