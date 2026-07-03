from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, packet


class handler(JsonHandler):
    def handle(self, method, body):
        return packet("whole-block-report", "ok", {"template": "docs/reporting-daily-weekly-template.md", "scope": "E1-E7 whole block"})

