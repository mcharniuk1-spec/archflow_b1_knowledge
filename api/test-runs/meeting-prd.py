from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, approval_block, packet


class handler(JsonHandler):
    def handle(self, method, body):
        if not body.get("owner_approval"):
            return approval_block("meeting_prd_test_cycle_requires_owner_approval")
        return packet(
            "meeting-prd-test",
            "review_packet_created",
            {
                "input_ref": "approved private fixture, filename redacted",
                "note": "Full execution still requires approved runtime and public/private source boundary review.",
            },
        )

