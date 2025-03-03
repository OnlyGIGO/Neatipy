from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class IntFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: int) -> str:
        return f"Int: {obj}"
