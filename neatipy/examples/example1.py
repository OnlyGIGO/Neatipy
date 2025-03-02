from core import Neatipy
import pandas as pd
import numpy as np


Neatipy.neatipy_print(3.141)
Neatipy.neatipy_print("Hello world")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

class Driver():
    def __init__(self):
        self.name="John Smith"
        self.age=18

class Car():
    def __init__(self,driver):
        self.speed=10
        self.type="vehicle"
        self.diver=driver
    def drive(self):
        print(f"{self.driver.name} is driving, vroom vroom")


driver=Driver()
car=Car(driver=driver)
df = pd.DataFrame(data)
lst=[[car,driver,car,[driver,car,driver]] for _ in range(2)]
tpl=(1,2,3,(),567,)
dct={"test":1,"test2":2,"test3":[1,2,3]}
st={"apple","banana"
    }
frozenst=frozenset([1,2,3,4])

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
