import requests
import re
import os
#<img src="//pic.qiushibaike.com/system/pictures/12431/124317196/medium/ZQZC0FOCMI4ZPI6S.jpg" alt="糗事#124317196" class="illustration" width="100%" height="auto">
if not os.path.exists('qiutulabs'):
    os.mkdir('qiutulabs')

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

urls = 'https://www.qiushibaike.com/imgrank/page/%d'
for pagenum in range(1, 3):
    new_url = format(urls%pagenum)

    wb_text = requests.get(url=new_url, headers=header).text

    new_urllist = re.findall('<div class="thumb">.*?<img src="(.*?)" alt.*?</div>', wb_text, re.S)

    for url in new_urllist:
        full_url = 'https:' + url

        img_content = requests.get(url=full_url, headers=header).content

        filename = url.split('/')[-1]
        filepath = './qiutulabs/'+filename

        with open(filepath,'wb') as fp:
            fp.write(img_content)
            print(filename,'over!!!!')