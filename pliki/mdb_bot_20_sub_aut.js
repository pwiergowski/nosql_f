var pipeline = [ 
	{ $project: { subreddit: 1, score: 1, author: 1 } },
	{ $match: { score: { $lt: 0 }, author: { $ne: "[deleted]" } } },
	{ $group: { _id: { subreddit: "$subreddit", author: "$author" }, count: { $sum: 1 }, minScore: { $min: "$score" } } },
	{ $sort: { minScore: 1 } },
	{ $limit: 20 }
];
db.reddit.aggregate( pipeline, { allowDiskUse: true } );
