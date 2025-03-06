from turtle import pen
import requests ,bs4
import os,re

url='https://www.taifex.com.tw/cht/3/dlFutPrevious30DaysSalesData'
csvDomainPrefix='https://www.taifex.com.tw/file/taifex/Dailydownload/DsilydownloadCSV/Daily_'

response=requests.get(url)
objsoup=bs4.BeautifulSoup(response.text,'lxml')

lastobj=objsoup.find('tr',class_='color')
lastUpdate=lastobj.find_all('td')[1].getText()

lastDownloadDate='lastDownloadDate.txt'
if os.path.exists(lastDownloadDate):
    with open(lastDownloadDate,'r') as f:
        lastDownload=f.read()
    print(lastDownload)
    if lastDownload==lastUpdate:
        print('downloaded')
    else:
        print('start to download')
        url=csvDomainPrefix+lastUpdate.replace('/','_')+'.zip'
        r=requests.get(url,allow_redirects=True)
        open(lastUpdate.replace('/','_'+'.zip','wb')).write(r.content)

        with open(lastDownloadDate,'w')as f :
            f.write(lastUpdate)
else:
    url = csvDomainPrefix + lastUpdate.replace('/','_')+'.zip'
    r=requests.get(url,allow_redirects=True)
    print(lastUpdate)
    open(lastUpdate.replace('/','_')+'.zip','wb').write(r.content)


    with open(lastDownloadDate,'w')as f :
        f.write(lastUpdate)