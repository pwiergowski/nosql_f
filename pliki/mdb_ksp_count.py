import pymongo
import json
from pymongo import MongoClient
from bson.son import SON
client = MongoClient('localhost', 27017)
db = client.mongo
pipeline = [
    { "$match": { "subreddit": "KerbalSpaceProgram"}  },
    { "$group": { "_id": "$subreddit", "count": { "$sum": 1 } } }
]
result = db.reddit.aggregate(pipeline)
print(list(result))
