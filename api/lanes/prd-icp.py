from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, prd_icp_payload


class handler(JsonHandler):
    def handle(self, method, body):
        return prd_icp_payload(body)

