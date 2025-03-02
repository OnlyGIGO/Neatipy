from core import Neatipy
import pandas as pd
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
Neatipy.neatipy_print(df)
Neatipy.neatipy_print(car)
Neatipy.neatipy_print(lst)
Neatipy.neatipy_print(tpl)
Neatipy.neatipy_print(dct)
Neatipy.neatipy_print(st)