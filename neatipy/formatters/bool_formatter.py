from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class BoolFormatter(BaseFormatter):
    @staticmethod
    def format(obj: bool) -> str:
        return f"Bool: {obj}"
