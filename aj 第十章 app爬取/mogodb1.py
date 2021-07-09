import pymongo

myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myClient['blued_users_info']
person_collection = db['stdent']

student = {
    'id':'239472342',
    'name':'ecdcece'
}

result = person_collection.insert_one(student)

print(result)