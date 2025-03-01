import pandas
from pandas import DataFrame
from caching import LRUCache
from .base_formatter import BaseFormatter

class DataFrameFormatter(BaseFormatter):
    alignment="center"
    spacing=2

    @staticmethod
    @LRUCache.lru_cache(max_size=256)
    def format(obj: DataFrame) -> str:
        result = "DataFrame:\n"
        cols = obj.columns
        data = obj.values
        col_amnt = len(cols)
        format_chr = "^"
        if DataFrameFormatter.alignment == "right":
            format_chr = ">"
        elif DataFrameFormatter.alignment == "left":
            format_chr = "<"
        elif DataFrameFormatter.alignment != "center":
            raise Exception("Invalid alignment")
        longest_datas = {}
        for i, col in enumerate(cols):
            longest = -1
            for _, d in enumerate(data):
                data_length = len(str(d[i]))
                col_length = len(str(col))
                longest = max(longest, data_length, col_length)
            longest_datas[col] = longest
        width = (sum(longest_datas.values()) + (col_amnt * DataFrameFormatter.spacing) + 2 * col_amnt)
        def column_generator():
            yield "-" * width + "\n"
            for _, col in enumerate(cols):
                format_rule = "|{:" + format_chr + str(longest_datas[col] + DataFrameFormatter.spacing) + "}|"
                yield format_rule.format(col)
            yield "\n"
            yield "-" * width + "\n"
        def data_generator():
            for _, dlist in enumerate(data):
                for index, col in enumerate(cols):
                    format_rule = "|{:" + format_chr + str(longest_datas[col] + DataFrameFormatter.spacing) + "}|"
                    yield format_rule.format(dlist[index])
                yield "\n"
            yield "-" * width + "\n"
        result+="".join(column_generator())
        result+="".join(data_generator())
        return result

