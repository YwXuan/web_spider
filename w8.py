import sqlite3
import bs4,requests 

conn=  sqlite3.connect("c110156225.db")
cursor = conn.cursor()
sql='''Create table news(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date text,
    title text,
    abstract text)'''
cursor.execute(sql)


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
    # print((textobj[i].text).replace("\n","").replace('\t',''))
    
for i in range(len(itemobj)):
    # data["new"].append({"seq":i+1,"title":title1[i],"content":content1[i],"date":date1[i]})
    x=(i+1,title1[i],content1[i],date1[i])
    print(x)
    sql='''insert into news values(?,?,?,?)'''
    conn.execute(sql,x)
    conn.commit()
cursor.close()
conn.close()