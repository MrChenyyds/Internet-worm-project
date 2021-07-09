import requests
from bs4 import BeautifulSoup

import time

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
header = {
'Connection': 'close',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
wb_text = requests.get(url=url,headers=header)

wb_text.encoding = 'utf-8'
wb_text = wb_text.text

soup = BeautifulSoup(wb_text, 'lxml')

li_list = soup.select('.book-mulu > ul > li')
fp = open('./三国演义.text','w',encoding='utf-8')
for li in li_list:
    title = li.a.string

    a_link = li.a['href']
    full_link = 'https://www.shicimingju.com'+a_link
    detail_text = requests.get(url=full_link, headers=header)

    detail_text.encoding = 'utf-8'
    detail_text = detail_text.text

    de_soup = BeautifulSoup(detail_text, 'lxml')
    detail_content = de_soup.find('div', class_='chapter_content').text
    fp.write(title+':'+'\n'+detail_content+'\n')
    print(title,'over!!!!')
    time.sleep(1)
