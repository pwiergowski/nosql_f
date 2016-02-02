var mapFunction = function() {
                       emit(this.subreddit, 1);
                   };
                   
var reduceFunction = function(key, values) {
						var total = 0;
						for(var i = 0; i < values.length; i++) {
								total += values[i];
						}
						return total;
					};

db.reddit.mapReduce(mapFunction, reduceFunction, { out: "result" })
