import pymongo
import json
from pymongo import MongoClient
from bson.son import SON
from bson.code import Code

client = MongoClient('localhost', 27017)
db = client.mongo

mapper = Code("""
				function () {
						emit(this.subreddit, 1);
				}
				""")
reducer = Code("""
				function (key, values) {
					var total = 0;
					for (var i = 0; i < values.length; i++) {
						total += values[i];
					}
					return total;
				}
				""")
result = db.reddit.map_reduce(mapper, reducer, "result",full_response=True)
#for doc in result.find():
#print result
print(result)
print(list(result))
