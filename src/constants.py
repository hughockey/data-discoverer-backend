import pymongo

client = pymongo.MongoClient("mongodb://root:root@mongo:27017/")
mydb = client[""]
mycol = mydb[""]