from neatipy.formatters import FloatFormatter
from neatipy.formatters import StringFormatter
from neatipy.formatters import IntFormatter
from neatipy.formatters import DataFrameFormatter
from neatipy.formatters import ClassFormatter
from neatipy.formatters import ListFormatter
from neatipy.formatters import TupleFormatter
from neatipy.formatters import BoolFormatter
from neatipy.formatters import SetFormatter
from neatipy.formatters import DictFormatter
from neatipy.formatters import FrozenSetFormatter
from neatipy.formatters import NumpyArrayFormatter
from neatipy.formatters import DataClassFormatter
from neatipy.formatters import DataFrameFormatterC
from dataclasses import is_dataclass
import pandas as pd
import numpy as np


class NeatipyFormatter:
    @staticmethod
    def format(obj: any, _depth: int = 0) -> str:
        match obj:
            case bool():  # ordered bool to first bc otherwise int will catch it
                return BoolFormatter.format(obj)
            case float():
                return FloatFormatter.format(obj)
            case int():
                return IntFormatter.format(obj)
            case str():
                return StringFormatter.format(obj)
            case list():
                return ListFormatter.format(obj, _depth)
            case tuple():
                return TupleFormatter.format(obj, _depth)
            case dict():
                return DictFormatter.format(obj, _depth)
            case set():
                return SetFormatter.format(obj, _depth)
            case frozenset():
                return FrozenSetFormatter.format(obj, _depth)
            case np.ndarray():
                return NumpyArrayFormatter.format(obj, _depth)
            case pd.DataFrame():
                return DataFrameFormatterC.format(obj)
            case _ if is_dataclass(obj):
                return DataClassFormatter.format(obj, _depth)
            case _ if (
                type(obj).__repr__ is not object.__repr__
            ):  # checking that the object's repr is not just the default one
                return repr(obj)
            case _ if type(obj).__module__ != "builtins":
                return ClassFormatter.format(obj, _depth=_depth)
