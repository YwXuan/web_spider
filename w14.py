# import pandas as pd
# import matplotlib.pyplot as plt

# colName = ['國文','英文','數學','自然','社會']
# iris = pd.read_csv('pandas\out4_50b.csv',names=colName)
# print(iris)

# plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
# # # 繪製直條圖
# iris.plot(kind='bar')
# # # # 刻度處理
# # # plt.yticks(iris_mean.index, iris_mean['國文'],rotation=0)

# plt.show()


import pandas as pd
import csv
url = 'http://www.stockq.org/market/cryptocurrency.php'
currencys = pd.read_html(url)                               # 讀取全球匯率行情表

currency = currencys[7]                                     
currency = currency.drop(currency.index[[0,1]])
currency=currency.drop(columns=[0,1])
currency.columns = ['貨幣', '代碼', '價格', '一日','七日','總市值','成交量'] # 建立column標題
currency.index = range(len(currency.index))                 # 建立row標題
print(currency)
print(type(currency))
currency.to_csv('data.csv',encoding="utf_8_sig")
