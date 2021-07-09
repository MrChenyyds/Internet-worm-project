import requests
from lxml import etree

url = 'https://sc.chinaz.com/jianli/fengmian.html'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
wb_text = requests.get(url=url, headers=header).text
tree = etree.HTML(wb_text)

div_list = tree.xpath('//div[@id="container"]/div')
for div in div_list:
    new_url ='https:'+div.xpath('./a[1]/@href')[0]
    new_data = requests.get(url=new_url, headers=header).text
    tree2 = etree.HTML(new_data)
    data = tree2.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
    print(data)