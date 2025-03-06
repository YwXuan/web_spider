# ch4_34.py
import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
z = df.fillna(0)
print(z)



















