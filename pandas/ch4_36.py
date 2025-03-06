# ch4_36.py
import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
x = df.dropna(axis='columns')
print(x)



















