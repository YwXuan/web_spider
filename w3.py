import requests
p={'http':'http://149.28.72.118:20002'}
r=requests.get('https://mp3cut.net/',proxies=p)
if r.status_code==200:
    print('代理成功')

print('\n\n\n\n\n HEADERS',r.headers)
print('\n\n\n\n\n BODY',r.content)
for i in r.content:
    print('\n\n\n\n\n',i)
