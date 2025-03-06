# ch4_15.py
import pandas as pd

fruits = ['Orange', 'Apple', 'Grape']
x = pd.Series([20, 30, 40], index=fruits)
print(f"{x['Apple']}")
print('-'*70)
print(f"{x[['Apple', 'Orange']]}")
print('-'*70)
print(f"{x[['Orange', 'Apple', 'Orange']]}")

      






















