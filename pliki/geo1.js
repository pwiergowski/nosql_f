var randomPoint = { "type" : "Point", "coordinates" : [ 19.701680, 53.232336 ] };
var citiesPointsArray = db.cities.find({loc: {$near: {$geometry: randomPoint} } }, {_id: 0, country:0 }).limit(4).toArray();
printjson(citiesPointsArray);
