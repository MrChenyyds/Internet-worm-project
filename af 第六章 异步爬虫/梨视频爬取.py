import requests
from lxml import etree
import re
import os
from multiprocessing.dummy import Pool
import random
import json

if not os.path.exists('./热么视频'):
    os.mkdir('./热门视频')

url = 'https://www.pearvideo.com/category_9'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
response = requests.get(url=url,headers=header).text
tree = etree.HTML(response)
li_list = tree.xpath('//ul[@class="listvideo-list clearfix"]/li')
vedio = []
#src="https://video.pearvideo.com/mp4/third/20210517/cont-1729619-10436676-174211-hd.mp4"
#https://www.pearvideo.com/videoStatus.jsp?contId=1729619&mrd=0.5006994916984144
for li in li_list:
    ve_url = li.xpath('./div/a/@href')[0]
    id_num = str(ve_url).split('_')[1]
    detail_url = 'https://www.pearvideo.com/'+ve_url
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
#https://www.pearvideo.com/videoStatus.jsp?contId=1729619&mrd=0.17018806525553454
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    para = {
        'contId': id_num,
        'mrd': str(random.random())
    }
    header2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Referer': 'https://www.pearvideo.com/video_'+id_num
    }
    response2 = requests.get(url=ajax_url,headers=header2,params=para).json()
    vedio_url = response2["videoInfo"]["videos"]["srcUrl"]
    #https://video.pearvideo.com/mp4/third/20210517/1621611197406-10436676-174211-hd.mp4
    #https://video.pearvideo.com/mp4/third/20210517/cont-1729619-10436676-174211-hd.mp4
    ve_url = ''
    url_list = str(vedio_url).split('/')
    for i in range(0,len(url_list)):
            if i < len(url_list)-1:
                ve_url+=url_list[i]+'/'
            else:
                num_list = url_list[i].split('-')
                for j in range(0,len(num_list)):
                    if j ==0:
                        ve_url +='cont-'+id_num
                    else:
                        ve_url +='-'+num_list[j]

    dic = {
        'name': name,
        'new_url': ve_url
    }
    print(dic['name'],dic['new_url'])
    vedio.append(dic)

def get_content(dic):
    data = requests.get(url=dic['new_url'],headers=header).content
    filename = './热门视频/'+dic['name']
    with open(filename,'wb') as fp:
        fp.write(data)

pool = Pool(4)
pool.map(get_content,vedio)

pool.close()
pool.join()