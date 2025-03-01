from caching import LRUCache
from .base_formatter import BaseFormatter
class FloatFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj:float)->str:
        return f"Float: {obj}"
