from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, approval_block, packet


class handler(JsonHandler):
    def handle(self, method, body):
        if not body.get("owner_approval"):
            return approval_block("voice_transcription_requires_owner_approval_and_storage_policy")
        return packet("voice-transcribe", "review_packet_created", {"transcript_excerpt": str(body.get("transcript") or "")[:900]})

