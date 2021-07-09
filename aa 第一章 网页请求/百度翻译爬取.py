import requests
import json

url = 'https://dict.youdao.com/word/wordarticle'
word = input('enter a word:')
data = {
    'query': word
}
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
response = requests.post(url=url,data=data,headers=header)

obj = response.json()

filename = word +'.json'
file = open(filename,'w',encoding='utf-8')
json.dump(obj ,fp=file,ensure_ascii=False)
print('over!!!')