# ch4_13.py
import pandas as pd

fruits = ['Orange', 'Apple', 'Grape']
x1 = pd.Series([20, 30, 40], index=fruits)
x2 = pd.Series([25, 38, 55], index=fruits)
y = x1 + x2
print(f"{y}")




      






















