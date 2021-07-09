import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
para = {
    'type': 5,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
response = requests.get(url=url,params=para,headers=header)

result = response.json()

filename = '排行榜.json'
file = open(filename,'w',encoding='utf-8')
json.dump(result,fp=file,ensure_ascii=False)
print('over!!!!!')