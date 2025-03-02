from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter


class DictFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: dict, _depth: int = 0) -> str:
        from neatipy.core import (
            NeatipyFormatter,
        )  # lazy import to avoid circular imports

        indent_str = " " * len("Dict: {")
        current_indent = indent_str * _depth
        next_indent = indent_str * (_depth + 1)
        result = "Dict: {\n"
        formatted_elements = (
            f"Key: ({NeatipyFormatter.format(key, _depth=_depth + 1)}) : Val: ({NeatipyFormatter.format(val, _depth=_depth + 1)})"
            for key, val in obj.items()
        )
        result += f",\n".join(
            (f"{next_indent}{element}" for element in formatted_elements)
        )
        result += f"\n{current_indent}{"}"}"
        return result
