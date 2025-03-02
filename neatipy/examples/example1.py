from core import Neatipy
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict,Tuple, Any
from collections.abc import Mapping
import time

# Basic examples
Neatipy.neatipy_print(3.141)
Neatipy.neatipy_print("Hello world")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

class Driver():
    def __init__(self):
        self.name = "John Smith"
        self.age = 18

class Car():
    def __init__(self, driver):
        self.speed = 10
        self.type = "vehicle"
        self.driver = driver  # corrected from 'diver' to 'driver'
    def drive(self):
        print(f"{self.driver.name} is driving, vroom vroom")

driver = Driver()
car = Car(driver=driver)
df = pd.DataFrame(data)
lst = [[car, driver, car, [driver, car, driver]] for _ in range(2)]
tpl = (1, 2, 3, (), 567,)
dct = {"test": 1, "test2": 2, "test3": [1, 2, 3]}
st = {"apple", "banana"}
frozenst = frozenset([1, 2, 3, 4])

nested_array = np.array([
    np.array([1, 2, 3], dtype=np.int32),
    np.array([1.5, 2.5, 3.5], dtype=np.float64),
    np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128),
    np.array([True, False, True], dtype=np.bool_),
    np.array([b'hello', b'world'], dtype=np.bytes_),
    np.array(['a', 'b', 'c'], dtype=np.str_),
    np.array([None, object(), lambda x: x**2], dtype=np.object_),
    np.array([np.datetime64('2025-03-02'), np.datetime64('1999-12-31')], dtype=np.datetime64),
    np.array([np.timedelta64(5, 'D'), np.timedelta64(100, 'h')], dtype=np.timedelta64),
    np.array([(1, 2.5, 'x'), (3, 4.5, 'y')], dtype=[('int', np.int32), ('float', np.float64), ('char', 'U1')])
], dtype=object)

Neatipy.neatipy_print(df)
Neatipy.neatipy_print(car)
Neatipy.neatipy_print(lst)
Neatipy.neatipy_print(tpl)
Neatipy.neatipy_print(dct)
Neatipy.neatipy_print(st)
Neatipy.neatipy_print(frozenst)
Neatipy.neatipy_print(True)
Neatipy.neatipy_print(nested_array)

@dataclass(frozen=True)
class NestedDetail:
    name: str
    attributes: Tuple[Tuple[str, int], ...]

@dataclass(frozen=True)
class SubComponent:
    id: int
    info: str
    detail: NestedDetail

@dataclass(frozen=True)
class ComplexNested:
    value: int
    description: str
    details: Tuple[NestedDetail, ...]
    components: Tuple[SubComponent, ...]
    metadata: Tuple[Tuple[str, str], ...] = field(default_factory=lambda: (("default", "info"),))
    tags: Tuple[str, ...] = ()

detail1 = NestedDetail(name="Detail1", attributes=(("a", 1), ("b", 2)))
detail2 = NestedDetail(name="Detail2", attributes=(("c", 3), ("d", 4)))
component1 = SubComponent(id=1, info="Component One", detail=detail1)
component2 = SubComponent(id=2, info="Component Two", detail=detail2)
complex_instance = ComplexNested(
    value=42,
    description="A more complex instance with nested structures",
    details=(detail1, detail2),
    components=(component1, component2),
    metadata=(("created", "2025-03-02"), ("status", "active")),
    tags=("python", "dataclass", "complex")
)
#timing the prints of the frozen dataclasses to see the effects of our LRU cache properly
start = time.time()
Neatipy.neatipy_print(complex_instance)
print("First print took", time.time() - start, "seconds")
start = time.time()
Neatipy.neatipy_print(complex_instance)
print("Second print took", time.time() - start, "seconds")