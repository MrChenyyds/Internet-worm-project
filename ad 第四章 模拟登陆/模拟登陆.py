import requests
data= {
    'name':'asda',
    'password':'asfewvev',
}
url = 'http://www.baidu.com'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

session = requests.Session()
response =session.post(url=url,headers=header,data=data).text