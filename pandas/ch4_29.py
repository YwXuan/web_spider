# ch4_29.py
import pandas as pd

s1 = pd.Series([1, 5, 9])
s2 = pd.Series([2, 4, 8])
x = s1.gt(s2)
print(x)

y = s1.eq(s2)
print(y)















