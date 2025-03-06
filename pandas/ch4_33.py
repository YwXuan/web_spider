# ch4_33.py
import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
print(df)
print("-"*70)
x = df.isna()
print(x)
print("-"*70)
y = df.notna()
print(y)

















