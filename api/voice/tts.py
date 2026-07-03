from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, packet


class handler(JsonHandler):
    def handle(self, method, body):
        return packet(
            "voice-tts",
            "browser_tts_only",
            {
                "text_excerpt": str(body.get("transcript") or body.get("request") or "")[:900],
                "tts_runtime": "browser_speech_synthesis_or_later_approved_provider",
            },
        )
