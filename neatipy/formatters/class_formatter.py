from neatipy.caching import LRUCache
from .base_formatter import BaseFormatter
import inspect


class ClassFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: any, _depth: int = 0) -> str:
        if (
            _depth > 0
        ):  # avoiding infinite recursion, but mainly to avoid going through potentially unwanted classes n their methods
            return f"User-defined class: {type(obj).__name__}"
        from neatipy.core import NeatipyFormatter

        methods = (
            attr
            for attr in dir(obj)
            if callable(getattr(obj, attr)) and not attr.startswith("__")
        )
        attributes = (
            attr
            for attr in dir(obj)
            if not (attr.startswith("__") or callable(getattr(obj, attr)))
        )

        def generate_class_header():
            yield f"User-defined class: {type(obj).__name__}{"\n"}\n"

        def generate_attributes():
            yield f"{"-"*3}Attributes:\n"
            for attribute in attributes:
                yield f"{attribute}: {NeatipyFormatter.format(getattr(obj,attribute),_depth=1)}\n"
            yield "\n"

        def generate_methods():
            yield f"{"-"*3}Methods:\n"
            for method in methods:
                fullArgs = inspect.getfullargspec(getattr(obj, method))
                argsString = ", ".join(fullArgs.args)
                kwargsString = ", ".join(
                    [f"{key}={value}" for key, value in fullArgs.kwonlyargs]
                )
                yield f"{method}({argsString}{f', {kwargsString}' if kwargsString else ''})\n"

        return f"{"".join(generate_class_header())}{"".join(generate_attributes())}{"".join(generate_methods())}"
