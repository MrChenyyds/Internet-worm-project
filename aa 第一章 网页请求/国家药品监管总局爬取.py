# http://scxk.nmpa.gov.cn:81/xk/
import  requests
import  json

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
first_list = []
all_list = []

for page in range(1,5):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': ''
    }
    response = requests.post(url=url,data=data,headers=header).json()
    for dic in response['list']:
        first_list.append(dic['ID'])

for id in first_list:
    data = {
        'id':id
    }

    response2 = requests.post(url=post_url,data=data,headers=header).json()
    all_list.append(response2)

filename = 'all_list.json'
fp = open(filename,'w',encoding='utf-8')
json.dump(all_list,fp=fp,ensure_ascii=False)

print('over!!!')
