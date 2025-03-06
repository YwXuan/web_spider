import bs4,requests
import json
data={
    "date":"2022.10.05",
    "new":[]
}
print(data)
resp=requests.get('https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw')
obj = bs4.BeautifulSoup(resp.text,'lxml')
itemobj=obj.find_all('div','mtitle')
textobj=obj.find_all('div',class_='mdetail')
title1=[]
content1=[]
date1=[]
for i in range(len(itemobj)):
    title1.append(str(itemobj[i].a.getText()).replace("\n","").replace('\t','')) #標題
    date1.append(str(itemobj[i].i.getText())) #時間
    content1.append(str(textobj[i].text).replace("\n","").replace('\t','')) #內容
    print((textobj[i].text).replace("\n","").replace('\t',''))
# print(title1)
# print(date1)
# print(content1)

for i in range(len(itemobj)):
    data["new"].append({"seq":i+1,"title":title1[i],"content":content1[i],"date":date1[i]})

# with open('data.json','w',encoding='utf8')as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)