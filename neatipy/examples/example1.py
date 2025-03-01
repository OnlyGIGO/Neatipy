from core import Neatipy
import pandas as pd
Neatipy.neatipy_print(3.141)
Neatipy.neatipy_print("Hello world")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
Neatipy.neatipy_print(df)
