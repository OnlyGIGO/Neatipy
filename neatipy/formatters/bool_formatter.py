from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class BoolFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: bool) -> str:
        return f"Bool: {obj}"
