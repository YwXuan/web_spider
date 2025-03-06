# ch4_32.py
import pandas as pd
import numpy as np

s1 = pd.Series([1, np.nan, 5])
s2 = pd.Series([np.nan, 6, 8])
x = s1.add(s2)
print(x)















