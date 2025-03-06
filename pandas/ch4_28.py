# ch4_28.py
import pandas as pd

data1 = [{'a':10, 'b':20}, {'a':30, 'b':40}]
df1 = pd.DataFrame(data1)
data2 = [{'a':1, 'b':2}, {'a':3, 'b':4}]
df2 = pd.DataFrame(data2)                            
x = df1.mul(df2)
print(x)

y = df1.div(df2)
print(y)












