#!/usr/bin/env python3
"""Send a sanitized ArchFlow status message through Telegram Bot API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHFLOW_ROOT = REPO_ROOT.parent
DEFAULT_ENV = ARCHFLOW_ROOT / ".env.local"
DEFAULT_MESSAGE = REPO_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture" / "telegram-summary.txt"
DEFAULT_STATUS = REPO_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture" / "telegram-delivery-status.json"
DEFAULT_STATUS_MD = REPO_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture" / "telegram-delivery-status.md"


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def write_status(path: Path, md_path: Path, status: dict[str, object]) -> None:
    path.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Telegram Delivery Status",
        "",
        f"Date: {status['timestamp_utc']}",
        f"Status: {status['status']}",
        f"Reason: {status.get('reason', 'none')}",
        "",
        "Boundary:",
        "- Message file is sanitized project status only.",
        "- Bot token, chat ID, and Telegram response body are not stored in public files.",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def send(token: str, chat_id: str, text: str, timeout: int) -> dict[str, object]:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    body = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - approved explicit API endpoint.
        payload = json.loads(response.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError("telegram_api_returned_not_ok")
    return {"status": "sent"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Send sanitized Telegram status.")
    parser.add_argument("--env", default=str(DEFAULT_ENV), help="Ignored env file with TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID.")
    parser.add_argument("--message", default=str(DEFAULT_MESSAGE), help="Sanitized message file.")
    parser.add_argument("--status", default=str(DEFAULT_STATUS), help="Sanitized JSON status output.")
    parser.add_argument("--status-md", default=str(DEFAULT_STATUS_MD), help="Sanitized Markdown status output.")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    env = {**load_env(Path(args.env)), **os.environ}
    token = env.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = env.get("TELEGRAM_CHAT_ID", "").strip()
    status_path = Path(args.status)
    status_md_path = Path(args.status_md)
    status = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": "blocked",
        "reason": "not_sent",
    }
    try:
        if not token or not chat_id:
            raise RuntimeError("telegram_env_missing")
        text = Path(args.message).read_text(encoding="utf-8")
        send(token, chat_id, text, args.timeout)
        status.update({"status": "sent", "reason": "telegram_api_ok"})
    except urllib.error.URLError as error:
        status.update({"status": "blocked", "reason": f"url_error:{error.reason}"})
    except Exception as error:  # noqa: BLE001
        status.update({"status": "blocked", "reason": str(error)})
    write_status(status_path, status_md_path, status)
    print(f"telegram_delivery_status={status['status']} reason={status['reason']}")
    return 0 if status["status"] == "sent" else 1


if __name__ == "__main__":
    raise SystemExit(main())
