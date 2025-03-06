# ch4_37.py
import pandas as pd
cities = {'Country':['China','China','Thailand','Japan','Singapore'],
          'Town':['Beijing','Shanghai','Bangkok', 'Tokyo','Singapore'],
          'Population':[2000, 2300, 900, 1600, 600]}
df = pd.DataFrame(cities, columns=["Town","Population"],
                  index=cities["Country"])
print(df)
print('-'*70)
total = df['Population'].sum()
print('人口總計 "', total)
print('-'*70)
print('累積人口總計')
cum_total = df['Population'].cumsum()
print(cum_total)








