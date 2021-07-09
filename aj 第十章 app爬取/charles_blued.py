import json
from mitmproxy import ctx
import pymongo

def response(flow):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client['blued_data']
    collection = db['person_info']

    infoList_url = 'https://argo.blued.cn/users?latitude='

    # 获取主页每个人的基本信息
    if infoList_url in flow.request.url:
            text = flow.response.text

            userData = json.loads(text)
            data_list = userData.get('data')

            for data in data_list:
                person_info = {
                    'name' : data.get('name'),
                    'height' : data.get('height'),
                    'weight' :data.get('weight'),
                    'role' : data.get('role'),
                    'age' :data.get('age'),
                    'distance' : data.get('distance'),
                    'des' :data.get('description'),
                    'pic' :data.get('avatar')
                }
                collection.insert_one(person_info)



