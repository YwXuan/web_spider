# ch4_69.py
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('3/11/2022', '3/15/2022')
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
ts.plot(title='Data in Time Series')
plt.xlabel("Date")
plt.ylabel("Data")
plt.show()








