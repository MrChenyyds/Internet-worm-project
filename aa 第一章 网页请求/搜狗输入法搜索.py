import requests

url = 'http://www.baidu.com/s'
word = input('enter a word:')
param = {
    'wd':word
}
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
response = requests.get(url=url,params=param,headers=header)

data_text = response.text

filename = word+'.html'

with open(filename,'w',encoding='utf-8') as fp:
    fp.write(data_text)

print('over!!!!')
