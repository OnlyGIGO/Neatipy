from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class IntFormatter(BaseFormatter):
    @staticmethod
    def format(obj: int) -> str:
        return f"Int: {obj}"
