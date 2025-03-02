from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class StringFormatter(BaseFormatter):
    @staticmethod
    def format(obj: str) -> str:
        return f"String: {obj}"
