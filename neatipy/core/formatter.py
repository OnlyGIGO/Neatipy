
from formatters import FloatFormatter
from formatters import StringFormatter
from formatters import IntFormatter
from formatters import DataFrameFormatter
from formatters import ClassFormatter
from formatters import ListFormatter
from formatters import TupleFormatter
from formatters import BoolFormatter
from formatters import SetFormatter
from formatters import DictFormatter
from formatters import FrozenSetFormatter
import pandas as pd
class NeatipyFormatter:
    @staticmethod
    def format(obj:any,_depth:int=0)->str:
        match obj:
            case float():
                return FloatFormatter.format(obj)
            case int():
                return IntFormatter.format(obj)
            case str():
                return StringFormatter.format(obj)
            case list():
                return ListFormatter.format(obj,_depth)
            case tuple():
                return TupleFormatter.format(obj,_depth)
            case dict():
                return DictFormatter.format(obj,_depth)
            case set():
                return SetFormatter.format(obj,_depth)
            case frozenset():
                return FrozenSetFormatter.format(obj,_depth)
            case bool():
                return BoolFormatter.format(obj)
            case pd.DataFrame():
                return DataFrameFormatter.format(obj)
            case _ if type(obj).__repr__ is not object.__repr__:#checking that the object's repr is not just the default one
                return repr(obj)
            case _ if type(obj).__module__ != "builtins":
                return ClassFormatter.format(obj,_depth=_depth)
            
