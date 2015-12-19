var randomPoint = { "type" : "Point", "coordinates" : [ 19.701680, 53.232336 ] };
var citiesPointsArray = db.cities.find({loc: {$near: {$geometry: randomPoint} } }).limit(4).toArray();
printjson(citiesPointsArray);
