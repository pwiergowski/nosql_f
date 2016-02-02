import pymongo
import json
from pymongo import MongoClient
from bson.son import SON
client = MongoClient('localhost', 27017)
db = client.mongo
pipeline = [
    { "$group": { "_id": "$subreddit"}  },
    { "$group": { "_id": 1, "count": { "$sum": 1 } } }
]
result = db.reddit.aggregate(pipeline)
##result = db.reddit.find_one()
print(list(result))
