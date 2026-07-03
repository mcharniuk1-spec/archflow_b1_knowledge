from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, packet


class handler(JsonHandler):
    def route(self, method, body):
        return packet(
            "voice-chat",
            "review_packet_created",
            {
                "reply": "Voice transcript received as text only. Raw audio is not stored and provider calls remain disabled.",
                "transcript_excerpt": str(body.get("transcript") or body.get("request") or "")[:900],
            },
        )
