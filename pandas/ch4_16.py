# ch4_16.py
import pandas as pd
import numpy as np

fruits = ['Orange', 'Apple', 'Grape']
x = pd.Series([20, 30, 40], index=fruits)
print((x + 10) * 2)
print('-'*70)
print(np.sin(x))


      






















