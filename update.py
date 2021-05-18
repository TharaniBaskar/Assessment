import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.mydb
db = client['mydb']
"""getting a collection"""
collection = db.user
collection = db['user']
x=collection.update_one({"name":"suba"},{"$set":{"name":"elsi"}})
print(x)