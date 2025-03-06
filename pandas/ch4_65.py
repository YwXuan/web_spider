# ch4_65.py
import pandas as pd
from datetime import datetime, timedelta

ndays = 5
start = datetime(2021, 9, 15)   
dates = [start + timedelta(days=x) for x in range(0, ndays)]
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
print(type(ts))
print(ts)










