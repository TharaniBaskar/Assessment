import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.freshvoice
db = client['freshvoice']
"""getting a collection"""
collection = db.test_collection
collection = db['test-collection']
""""document"""
import datetime
post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()}
"""inserrting a document"""
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
db.list_collection_names()
[u'posts']
import pprint
pprint.pprint(posts.find_one())
{u'author': u'Mike',
  u'tags': [u'mongodb', u'python', u'pymongo'],
 u'text': u'My first blog post!'}
pprint.pprint(posts.find_one({"author": "Mike"}))
{u'author': u'Mike',
 u'tags': [u'mongodb', u'python', u'pymongo'],
 u'text': u'My first blog post!'}
posts.find_one({"author": "Eliot"})

