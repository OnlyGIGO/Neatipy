from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter
import numpy as np


class NumpyArrayFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: list, _depth: int = 0) -> str:
        from neatipy.core import (
            NeatipyFormatter,
        )  # lazy import to avoid circular imports

        indent_str = " " * len("Numpy array: [")
        current_indent = indent_str * _depth
        next_indent = indent_str * (_depth + 1)
        result = "Numpy array: [\n"
        formatted_elements = (
            NeatipyFormatter.format(element, _depth=_depth + 1) for element in obj
        )
        result += f",\n".join(
            (f"{next_indent}{element}" for element in formatted_elements)
        )
        result += f"\n{current_indent}]"
        return result
