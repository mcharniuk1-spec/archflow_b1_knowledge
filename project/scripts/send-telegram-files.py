#!/usr/bin/env python3
"""Send sanitized ArchFlow files through Telegram Bot API.

This script reads Telegram credentials only from ignored local environment or
process environment. It stores delivery status, but never stores tokens, chat
IDs, private destinations, or Telegram response bodies.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHFLOW_ROOT = REPO_ROOT.parent
DEFAULT_ENV = ARCHFLOW_ROOT / ".env.local"


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


def safe_repo_path(raw: str) -> Path:
    path = (REPO_ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    try:
        path.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise RuntimeError(f"file_outside_public_repo:{raw}") from exc
    if not path.exists() or not path.is_file():
        raise RuntimeError(f"file_missing:{raw}")
    if path.name.startswith(".env") or "/.env" in path.as_posix():
        raise RuntimeError(f"refusing_env_file:{raw}")
    return path


def post_form(token: str, method: str, fields: dict[str, str], timeout: int) -> None:
    url = f"https://api.telegram.org/bot{token}/{method}"
    body = urllib.parse.urlencode(fields).encode("utf-8")
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - explicit approved Telegram API endpoint.
        payload = json.loads(response.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError(f"telegram_{method}_not_ok")


def post_document(token: str, chat_id: str, path: Path, caption: str, timeout: int) -> None:
    boundary = f"----archflow-{secrets.token_hex(12)}"
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    chunks: list[bytes] = []

    def add_field(name: str, value: str) -> None:
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode("utf-8"),
                b"\r\n",
            ]
        )

    add_field("chat_id", chat_id)
    add_field("caption", caption[:1024])
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="document"; filename="{path.name}"\r\n'.encode(),
            f"Content-Type: {mime}\r\n\r\n".encode(),
            path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    body = b"".join(chunks)
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendDocument",
        data=body,
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - explicit approved Telegram API endpoint.
        payload = json.loads(response.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError("telegram_sendDocument_not_ok")


def write_status(path: Path, md_path: Path, status: dict[str, object]) -> None:
    path.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Telegram File Delivery Status",
        "",
        f"Date: {status['timestamp_utc']}",
        f"Status: {status['status']}",
        f"Reason: {status.get('reason', 'none')}",
        "",
        "Files:",
    ]
    for item in status.get("files", []):
        if isinstance(item, dict):
            lines.append(f"- {item.get('path')}: {item.get('status')}")
    lines.extend(
        [
            "",
            "Boundary:",
            "- Message and files are sanitized project status artifacts only.",
            "- Bot token, chat ID, private destination, and Telegram response body are not stored in public files.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send sanitized Telegram files.")
    parser.add_argument("--env", default=str(DEFAULT_ENV), help="Ignored env file with TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID.")
    parser.add_argument("--message", required=True, help="Sanitized message file to send before documents.")
    parser.add_argument("--file", action="append", required=True, help="Repo-relative file to send. Repeat for multiple files.")
    parser.add_argument("--status", required=True, help="Sanitized JSON status output.")
    parser.add_argument("--status-md", required=True, help="Sanitized Markdown status output.")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    env = {**load_env(Path(args.env)), **os.environ}
    token = env.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = env.get("TELEGRAM_CHAT_ID", "").strip()
    status_path = Path(args.status)
    status_md_path = Path(args.status_md)
    status: dict[str, object] = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": "blocked",
        "reason": "not_sent",
        "files": [],
    }
    try:
        if not token or not chat_id:
            raise RuntimeError("telegram_env_missing")
        message_path = safe_repo_path(args.message)
        files = [safe_repo_path(raw) for raw in args.file]
        message = message_path.read_text(encoding="utf-8")
        post_form(token, "sendMessage", {"chat_id": chat_id, "text": message, "disable_web_page_preview": "false"}, args.timeout)
        for path in files:
            rel = path.relative_to(REPO_ROOT).as_posix()
            post_document(token, chat_id, path, f"ArchFlow artifact: {rel}", args.timeout)
            status["files"].append({"path": rel, "status": "sent"})
        status.update({"status": "sent", "reason": "telegram_api_ok"})
    except urllib.error.URLError as error:
        status.update({"status": "blocked", "reason": f"url_error:{error.reason}"})
    except Exception as error:  # noqa: BLE001
        status.update({"status": "blocked", "reason": str(error)})
    write_status(status_path, status_md_path, status)
    print(f"telegram_file_delivery_status={status['status']} reason={status['reason']}")
    return 0 if status["status"] == "sent" else 1


if __name__ == "__main__":
    sys.exit(main())
