from caching import LRUCache
from .base_formatter import BaseFormatter
class StringFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj:str)->str:
        return f"String: {obj}"
