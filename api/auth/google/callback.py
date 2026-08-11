from pathlib import Path
import sys


sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / "_auth_contract.py").exists())))

from _auth_contract import QuietAuthHandler, handle_google_callback, method_not_allowed


class handler(QuietAuthHandler):
    def do_GET(self) -> None:
        handle_google_callback(self)

    def do_POST(self) -> None:
        method_not_allowed(self, "GET")
