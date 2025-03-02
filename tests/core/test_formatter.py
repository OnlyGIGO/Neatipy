from neatipy import NeatipyFormatter
import numpy as np
import pandas as pd
from dataclasses import dataclass


def test_list_formatter():
    assert NeatipyFormatter.format([1, 2, 3]) != str([1, 2, 3])


def test_tuple_formatter():
    assert NeatipyFormatter.format(
        (
            1,
            2,
            3,
        )
    ) != str(
        (
            1,
            2,
            3,
        )
    )


def test_dict_formatter():
    assert NeatipyFormatter.format({1: 2, 3: 4}) != str({1: 2, 3: 4})


def test_set_formatter():
    assert NeatipyFormatter.format({1, 2, 3}) != str({1, 2, 3})


def test_frozenset_formatter():
    assert NeatipyFormatter.format(frozenset({1, 2, 3})) != str(frozenset({1, 2, 3}))


def test_numpy_array_formatter():
    assert NeatipyFormatter.format(np.array([1, 2, 3])) != str(np.array([1, 2, 3]))


def test_pandas_dataframe_formatter():
    assert NeatipyFormatter.format(
        pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    ) != str(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))


def test_class_formatter_non_default_repr():
    class A:
        def __repr__(self):
            return "A"

    assert NeatipyFormatter.format(A()) == str(A())


def test_class_formatter_default_repr():
    class A:
        pass

    assert NeatipyFormatter.format(A()) != str(A())


def test_float_formatter():
    assert NeatipyFormatter.format(3.141) != str(3.141)


def test_string_formatter():
    assert NeatipyFormatter.format("Hello world") != str("Hello world")


def test_bool_formatter():
    assert NeatipyFormatter.format(True) != str(True)


def test_dataclass_formatter():
    @dataclass
    class DataClass:
        a: int
        b: int

    assert NeatipyFormatter.format(DataClass(1, 2)) != str(DataClass(1, 2))


def test_int_formatter():
    assert NeatipyFormatter.format(1) != str(1)
