import requests

url = r'http://epub.cnki.net/kns/brief/result.aspx?dbPrefix=CIPD'
res = requests.session().get(url)

with open('C:\\Users\\ch\\Desktop\\xxx.html','wb') as file:
    file.write(res.text.encode('utf-8'))
