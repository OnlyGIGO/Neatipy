
from formatters import FloatFormatter
from formatters import StringFormatter
from formatters import IntFormatter
from formatters import DataFrameFormatter
import pandas as pd
class NeatipyFormatter:
    @staticmethod
    def format(obj:any)->str:
        match obj:
            case float():
                return FloatFormatter.format(obj)
            case int():
                return IntFormatter.format(obj)
            case str():
                return StringFormatter.format(obj)
            case pd.DataFrame():
                return DataFrameFormatter.format(obj)
            case _:
                return repr(obj)
