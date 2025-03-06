# ch4_14.py
import pandas as pd

fruits1 = ['Orange', 'Apple', 'Grape']
fruits2 = ['Orange', 'Banana', 'Grape']
x1 = pd.Series([20, 30, 40], index=fruits1)
x2 = pd.Series([25, 38, 55], index=fruits2)
y = x1 + x2
print(f"{y}")




      






















