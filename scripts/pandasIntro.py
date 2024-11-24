import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

list = [1, 3, 5, 7, 9]
s = pd.Series(list)
print(s)


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
print(df)

print(df.iloc[:2])

data = {
    "Department": ["HR", "HR", "IT", "IT", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Salary": [50000, 52000, 60000, 62000, 58000],
}
df = pd.DataFrame(data)

fileName = "test.xlsx"
df.to_excel(fileName)

rd = pd.read_excel("./test.xlsx")
print(rd)
