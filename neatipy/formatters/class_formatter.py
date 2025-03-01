from caching import LRUCache
from .base_formatter import BaseFormatter
class ClassFormatter(BaseFormatter):
    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj:any,_depth:int=0)->str:
        if _depth>0: #avoiding infinite recursion, but mainly to avoid going through potentially unwanted classes n their methods
            return f"User-defined class: {type(obj).__name__}"
        from core import NeatipyFormatter
        methods=(attr for attr in dir(obj) if callable(getattr(obj,attr)) and not attr.startswith("__"))
        attributes=(attr for attr in dir(obj) if not (attr.startswith("__") or callable(getattr(obj,attr))))
        def generate_class_header():
            yield f"User-defined class: {type(obj).__name__}{"\n|"*1}\n"

        def generate_attributes():
            yield f"{"-"*3}Attributes:\n"
            for attribute in attributes:
                yield f"| {attribute}: {NeatipyFormatter.format(getattr(obj,attribute),_depth=1)}\n" 
            yield "|\n"
        def generate_methods():
            yield f"{"-"*3}Methods:\n"
            for method in methods:
                yield f"| {method}\n"

        return f"{"".join(generate_class_header())}{"".join(generate_attributes())}{"".join(generate_methods())}"

