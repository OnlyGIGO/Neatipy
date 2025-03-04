import pandas
from pandas import DataFrame
from .base_formatter import BaseFormatter
import neatipy_c

class DataFrameFormatterC(BaseFormatter):
    @staticmethod
    def format(obj: DataFrame) -> str:
       return f"Dataframe:\n{neatipy_c.format_dataframe(obj.columns.tolist(), obj.values.tolist())}\n"
