# ch4_51.py
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
x = pd.read_csv("pandas\out4_50a.csv",index_col=0)
y = pd.read_csv("pandas\out4_50a.csv",names=course)
print(x)
print(y)







