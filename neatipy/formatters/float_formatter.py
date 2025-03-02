from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter
class FloatFormatter(BaseFormatter):
    @staticmethod
    def format(obj:float)->str:
        return f"Float: {obj}"
