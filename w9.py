import hashlib
import json
import requests

# data=hashlib.md5()
# data.update(b'dof klkl pepo')
# print('hash value',data.digest())
# print('hash value(16)',data.hexdigest())
# print(type(data))
# print(type(data.hexdigest()))
# print(hashlib.algorithms_available)

url= "https://data.epa.gov.tw/api/v2/acidr_p_01?api_key=5a2b169c-50c4-42c1-a779-24c545fb40f9"
try:
    res=requests.get(url)
    print(type(res))
    print('下載成功')
except Exception as err:
    print('下載失敗')

aqi=res.json() ['records']
# print(f'aqi 資料型態：{type(aqi)}')
# print(aqi)
# for data in aqi:
#     print(data)

fn='aqi.json'
with open(fn,'w',encoding='utf8')as f:
    json.dump(aqi,f,ensure_ascii=False)