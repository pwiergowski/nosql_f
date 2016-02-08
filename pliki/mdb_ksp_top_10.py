import pymongo
import json
from pymongo import MongoClient
from bson.son import SON
client = MongoClient('localhost', 27017)
db = client.mongo
pipeline = [
    { "$project": { "subreddit": 1, "author":1, "score": 1 } },
	{ "$match": { "subreddit": "KerbalSpaceProgram" }  },
	{ "$group": { "_id": "$author", "count": { "$sum": 1 }, "avgScore": { "$avg": "$score" } } },
	{ "$sort": { "count": -1, "avgScore": -1 } },
	{ "$limit": 11 },
	{ "$skip": 1 }
]
result = db.reddit.aggregate(pipeline)
for doc in result:
	print(doc)
