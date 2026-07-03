#!/usr/bin/env python3
"""Run E1.2.8 provider comparison through OpenRouter using sanitized payload only."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


PUBLIC_ROOT = Path(__file__).resolve().parents[2]
PRIVATE_ROOT = PUBLIC_ROOT.parent
RUN_DIR = PUBLIC_ROOT / "project" / "runs" / "E1.2" / "2026-07-02-testmeeting-local"
CONTINUATION_DIR = PUBLIC_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture"
PAYLOAD_PATH = CONTINUATION_DIR / "openrouter-sanitized-provider-payload.json"
ROOT_ENV = PRIVATE_ROOT / ".env.local"
MODEL_LIST_URL = "https://openrouter.ai/api/v1/models"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
ROUTE_EXECUTION_MODELS = ["qwen/qwen3.6-plus", "qwen/qwen3-235b-a22b"]


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


def api_request(method: str, url: str, api_key: str | None = None, payload: dict | None = None, timeout: int = 60) -> dict:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=body, method=method)
    if api_key:
        request.add_header("Authorization", f"Bearer {api_key}")
    if body is not None:
        request.add_header("Content-Type", "application/json")
        request.add_header("HTTP-Referer", "https://archflow.local")
        request.add_header("X-Title", "ArchFlow E1.2.8 OpenRouter sanitized comparison")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def model_by_id(models_payload: dict) -> dict[str, dict]:
    return {item["id"]: item for item in models_payload.get("data", []) if isinstance(item, dict) and item.get("id")}


def choose_model(models_payload: dict, preferred: str | None) -> tuple[str, dict, str]:
    models = model_by_id(models_payload)
    if preferred and preferred in ROUTE_EXECUTION_MODELS and preferred in models:
        return preferred, models[preferred], "preferred_env_model_allowed_by_yushchenko_source_scope_gate"
    if preferred and preferred and preferred not in ROUTE_EXECUTION_MODELS:
        # Explicitly reject cross-role or frontier overrides for this execution node.
        preferred = None
    for candidate in ROUTE_EXECUTION_MODELS:
        if candidate in models:
            return candidate, models[candidate], "first_available_yushchenko_source_scope_execution_model"
    raise RuntimeError("no_yushchenko_source_scope_execution_model_available")


def estimated_cost(model_meta: dict, usage: dict) -> float | None:
    try:
        pricing = model_meta.get("pricing", {})
        prompt_price = float(pricing.get("prompt", "0"))
        completion_price = float(pricing.get("completion", "0"))
        prompt_tokens = float(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        completion_tokens = float(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
        return prompt_tokens * prompt_price + completion_tokens * completion_price
    except (TypeError, ValueError, AttributeError):
        return None


def extract_content(response: dict) -> str:
    choice = (response.get("choices") or [{}])[0]
    return str(((choice or {}).get("message") or {}).get("content") or "").strip()


def write_status(status: str, reason: str, extra: dict | None = None) -> None:
    extra = extra or {}
    (CONTINUATION_DIR / "openrouter-provider-status.md").write_text(
        "\n".join(
            [
                "# OpenRouter Provider Comparison Status",
                "",
                f"Date: {now_utc()}",
                f"Status: {status}",
                f"Reason: {reason}",
                "",
                "## Boundary",
                "",
                "- Provider path: OpenRouter.",
                "- Route: `yushchenko.source_scope_gate`.",
                "- Input kind: sanitized digest only.",
                "- Raw private source sent: false.",
                "- API keys are not written to public files.",
                "- Model selection is role/node-based, not Epic-based.",
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


def redacted_error(error: object) -> str:
    return re.sub(r"Bearer\s+[A-Za-z0-9._-]+", "Bearer <redacted>", str(error))[:1200]


def main() -> int:
    load_env(ROOT_ENV)
    if os.getenv("MODEL_PROVIDER", "none").strip().lower() != "openrouter":
        write_status("blocked", "MODEL_PROVIDER_not_openrouter")
        return 2
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        write_status("blocked", "OPENROUTER_API_KEY_missing")
        return 3
    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))

    try:
        models_payload = api_request("GET", MODEL_LIST_URL, None)
        model, model_meta, model_reason = choose_model(models_payload, os.getenv("OPENROUTER_MODEL", "").strip() or None)
        selection = {
            "checked_at": now_utc(),
            "provider": "openrouter",
            "task_role_and_langgraph_node": payload["model_route_profile"]["task_role_and_langgraph_node"],
            "query_shape": payload["model_route_profile"]["query_shape"],
            "allowed_execution_models": ROUTE_EXECUTION_MODELS,
            "selected_model": model,
            "selection_reason": model_reason,
            "context_length": model_meta.get("context_length"),
            "pricing": model_meta.get("pricing", {}),
            "epic_level_assignment": "prohibited",
        }
        (CONTINUATION_DIR / "openrouter-model-selection.json").write_text(json.dumps(selection, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        prompt = (
            "You are Yushchenko operating the ArchFlow source_scope_gate node. Use only the sanitized JSON payload below. "
            "Do not infer raw private source details. Do not claim customer validation, ROI, provider readiness, Railway readiness, "
            "Telegram delivery, or Notion writeback. Return Markdown with the expected sections and separate FACT, INTERPRETATION, HYPOTHESIS, and GAP.\n\n"
            f"{json.dumps(payload, indent=2, sort_keys=True)}"
        )
        request_payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You produce public-safe PRD comparison artifacts from sanitized product discovery digests. Preserve source boundaries."},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 1500,
            "temperature": 0.2,
        }
        response = api_request("POST", CHAT_URL, api_key, request_payload, timeout=90)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:1200]
        write_status("blocked", f"openrouter_http_error_{exc.code}", {"error_excerpt": body})
        return 4
    except Exception as exc:
        write_status("blocked", type(exc).__name__, {"error_excerpt": redacted_error(exc)})
        return 5

    output = extract_content(response)
    if not output:
        write_status("blocked", "empty_openrouter_response")
        return 6

    output_path = RUN_DIR / "E1.2.8_OpenRouter_Comparison.md"
    output_path.write_text(
        "\n".join(
            [
                "# E1.2.8 OpenRouter Provider Comparison",
                "",
                f"Date: {now_utc()}",
                "Provider: OpenRouter",
                f"Model: {model}",
                f"Model selection: {model_reason}",
                "Route: yushchenko.source_scope_gate",
                "Input kind: sanitized digest only",
                "Raw private source sent: false",
                "",
                output,
                "",
            ]
        ),
        encoding="utf-8",
    )
    usage = response.get("usage") or {}
    cost = estimated_cost(model_meta, usage)
    ledger = {
        "timestamp_utc": now_utc(),
        "run_id": payload["run_id"],
        "task_role_and_langgraph_node": payload["model_route_profile"]["task_role_and_langgraph_node"],
        "query_shape": payload["model_route_profile"]["query_shape"],
        "graph_node_path": payload["model_route_profile"]["graph_node_path"],
        "model_route_profile": "yushchenko_source_scope_gate_openrouter_execution",
        "provider": "openrouter",
        "model_id": model,
        "model_role": "execution_pool_structured_comparison",
        "prompt_version": "e1_2_8_openrouter_yushchenko_source_scope_v1",
        "source_ids_used": payload["source_boundary"]["source_ids_used"],
        "input_artifact": "project/runs/2026-07-02-e1-2-testmeeting-dashboard-architecture/openrouter-sanitized-provider-payload.json",
        "output_artifact": "project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_OpenRouter_Comparison.md",
        "prompt_tokens": usage.get("prompt_tokens"),
        "output_tokens": usage.get("completion_tokens"),
        "actual_or_estimated_cost": cost,
        "cost_currency": "USD",
        "pricing_source": "OpenRouter /api/v1/models",
        "budget_cap": float(os.getenv("OPENROUTER_RUN_BUDGET_USD", "1.99")),
        "daily_budget_cap": float(os.getenv("OPENROUTER_DAILY_BUDGET_USD", "5.00")),
        "decision": "provider_comparison_generated_for_review",
        "reviewer_model_id": "Codex operator",
        "human_gate_required": True,
        "runtime_source": "openrouter_chat_completions_sanitized_payload",
        "status": "completed",
        "raw_private_source_sent": False,
    }
    with (RUN_DIR / "openrouter-model-call-ledger.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(ledger, sort_keys=True) + "\n")
    (RUN_DIR / "openrouter-budget-guard.json").write_text(
        json.dumps(
            {
                "status": "ok" if cost is None or cost < float(os.getenv("OPENROUTER_RUN_HARD_STOP_USD", "1.99")) else "blocked_over_cap",
                "daily_budget_usd": float(os.getenv("OPENROUTER_DAILY_BUDGET_USD", "5.00")),
                "run_budget_usd": float(os.getenv("OPENROUTER_RUN_BUDGET_USD", "1.99")),
                "run_hard_stop_usd": float(os.getenv("OPENROUTER_RUN_HARD_STOP_USD", "1.99")),
                "actual_or_estimated_spend_usd": cost,
                "provider_calls": 1,
                "provider": "openrouter",
                "model": model,
                "input_kind": "sanitized_digest_only",
                "raw_private_source_sent": False,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    try:
        from e1_2_8_testmeeting_run import render_pdf

        render_pdf(output_path, output_path.with_suffix(".pdf"), "ArchFlow E1.2.8 OpenRouter comparison")
    except Exception as exc:  # PDF is useful but should not hide provider output success.
        (CONTINUATION_DIR / "openrouter-pdf-warning.md").write_text(f"# OpenRouter PDF Warning\n\nStatus: blocked\n\nReason: `{redacted_error(exc)}`\n", encoding="utf-8")

    write_status("completed", "openrouter_comparison_generated", {"model": model, "selection_reason": model_reason, "usage": usage, "estimated_cost_usd": cost})
    print(f"openrouter_comparison=completed model={model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
