
from datastructures import LRUCache 

class NeatipyFormatter:
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj):
        match obj:
            case float():
                return f"Float: {obj:.2f}"
            case _:
                return str(obj)
