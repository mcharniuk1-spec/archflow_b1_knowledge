from pathlib import Path
import sys

sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / '_jarvis_contract.py').exists())))

from _jarvis_contract import JsonHandler, health_payload


class handler(JsonHandler):
    def route(self, method, body):
        return health_payload()
