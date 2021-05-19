import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.mydb
db = client['mydb']
"""getting a collection"""
collection = db.user
collection = db['user']
post=[{"name":"tharani","email":"aaa.@gmail.com","phonenumber":"7685432101"},
      {"name":"thara", "email": "bbb.@gmail.com", "phonenumber": "7685432102"},
      {"name":"tharan","email":"ccc.@gmail.com","phonenumber":"7685432103"},
      {"name":"shiny","email":"ddd.@gmail.com","phonenumber":"7685432104"},
      {"name":"gayathri","email":"eee.@gmail.com","phonenumber":"7685432105"},
      {"name":"suba","email":"fff.@gmail.com","phonenumber":"7685432106"},
      {"name":"amirtha","email":"ggg.@gmail.com","phonenumber":"7685432107"},
      {"name":"nila","email":"hhh.@gmail.com","phonenumber":"7685432108"},
      {"name":"rani","email":"iii.@gmail.com","phonenumber":"7685432109"},
      {"name":"priya","email":"jjj.@gmail.com","phonenumber":"7685432110"}
      ]
collection.insert_many(post)
