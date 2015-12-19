var result = db.reddit.aggregate(
[ 
    { $group: { _id: "$subreddit"}  },
    { $group: { _id: 1, count: { $sum: 1 } } }
]).pretty();
printjson(result);
