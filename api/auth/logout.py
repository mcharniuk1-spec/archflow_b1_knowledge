from pathlib import Path
import sys


sys.path.insert(0, str(next(parent for parent in Path(__file__).resolve().parents if (parent / "_auth_contract.py").exists())))

from _auth_contract import QuietAuthHandler, handle_logout, method_not_allowed


class handler(QuietAuthHandler):
    def do_GET(self) -> None:
        method_not_allowed(self, "POST")

    def do_POST(self) -> None:
        handle_logout(self)
