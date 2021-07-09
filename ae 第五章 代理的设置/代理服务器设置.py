import  requests

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
proxy_list = [
'177.225.253.178:8080',
'195.162.71.112:8080',
'118.96.226.251:8080',
'36.89.144.157:8080',
'193.34.95.110:8080',
'200.16.208.187:8080',
'113.161.186.101:8080',
'103.47.66.150:8080',
'181.39.48.2:8080',
'80.245.117.134:8080'
]
responce = requests.get(url=url,headers=headers,proxies={"https":proxy_list[1]}).text
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(responce)