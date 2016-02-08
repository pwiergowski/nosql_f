var pipeline = [ 
	{ $match: { "subreddit":"KerbalSpaceProgram"}  },
    { $group: { _id: "$subreddit", count: { $sum: 1 } } }
];
db.reddit.aggregate(pipeline);
