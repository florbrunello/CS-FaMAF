// Parte 1 - Tareas

// Ejercicio 1
db.users.insertMany([
	{ "name" : "Flor", "email" : "flor@gameofthrdon.es", "password" : "aLongPassworsdrgdrgdHereWith50OrMoreCharactersresssss" },
	{ "name" : "Florencia", "email" : "florencia@gameofthron.es", "password" : "aLongPassworsdrgdrgdHereWith50OrMoreCharactersresssss" },
	{ "name" : "Juan", "email" : "juan@gameofthron.es", "password" : "aLongPassworsdrgdrgdHereWith50OrMoreCharactersresssss" },
	{ "name" : "JuanP", "email" : "juanp@gameofthron.es", "password" : "aLongPassworsdrgdrgdHereWith50OrMoreCharactersresssss" },
	{ "name" : "JuanC", "email" : "juanc@gameofthron.es", "password" : "aLongPassworsdrgdrgdHereWith50OrMoreCharactersresssss" },
])

db.comments.insertMany([
	{
		"name" : "Flor",
		"email" : "flor@gameofthron.es",
		"movie_id" : ObjectId("573a1390f29313caabcd418c"),
		"text" : "Muy buena pelicula!!Completar lengthhhhhhhhhhhhhhh",
		"date" : ISODate("2012-03-26T23:20:16Z")
	},
	{
		"name" : "Flor",
		"email" : "flor@gameofthron.es",
		"movie_id" : ObjectId("573a1390f29313caabcd418c"),
		"text" : "Muy linda pelicula!!Completar lengthhhhhhhhhhhhhhh",
		"date" : ISODate("2012-03-27T23:20:16Z")
	},
])

// Ejercicio 2
db.movies.find(   
    { 
		"year": {"$gte": 1990, "$lte": 1999 }, 
		"imdb.rating": { $type: "double" }
	},
    { "_id" : 0, "title": 1, "year": 1, "cast": 1, "directors": 1, "imdb.rating": 1} 
).sort(
	{ 
		"imdb.rating": -1
	}
).limit(10)

// Ejecicio 3
db.comments.find(
	{
		movie_id : ObjectId("573a1399f29313caabcee886"),
		date : { $gte : ISODate("2014-01-01T00:00:00Z"), $lte : ISODate("2016-12-31T00:00:00Z")}
	},
	{ "_id":0, "name": 1, "email":1, "text":1, "date":1 }
). sort(
	{ date : 1 }
)

db.comments.find(
	{
		movie_id : ObjectId("573a1399f29313caabcee886"),
		date : { $gte : ISODate("2014-00-00T00:00:00Z"), $lte : ISODate("2016-12-31T00:00:00Z"),
		"totalComentarios" : { $count : 1}
	}
	},
	{ "_id":0, "name": 1, "email":1, "text":1, "date":1 }
). count()

// Ejercicio 4
db.comments.find(
	{
		email: "patricia_good@fakegmail.com"
	},
	{ "_id":0, "name": 1, "movie_id":1, "text":1, "date":1  }
). sort (
	{ date : -1 }
). limit(3)

// Ejericio 5
db.movies.find(
	{
		"genres": { $all: ["Drama", "Action"]},
		"languages": { $size : 1},
		$or: [
			{ "imdb.rating": { $gt : 9 } },
			{ "runtime" : { $gte : 180 }}
		]
	},
	{ "_id" : 0, "title" : 1, "languages" : 1, "genres" : 1, "released" : 1, "imdb.votes" : 1 } 
). sort(
	{
		"released": -1, 
		"imdb.votes" :1
	}
)

// Ejercicio 6
db.theaters.find(
	{ 
		"location.address.state": { $in : ["CA", "NY", "TX"] },
		"location.address.city" : /^F/ 
	},
	{ "_id":0, "theaterId":1, "location.address.state": 1, "location.address.city":1, "location.geo.coordinates":1 }
). sort(
	{"location.address.state": 1, "location.address.city":1}
)

// Ejercicio 7
db.comments.updateMany(
	{
		"_id" : ObjectId("5b72236520a3277c015b3b73")
	},
	{
		$set: {
			text: "This is a great comment"
		},
		$currentDate: { 
			"date": true 
		}
	}
)

// Ejercicio 8
db.users.updateOne(
	{ email: "joel.macdonel@fakegmail.com" },
	{ $set: {
		password: "some password",
		name: "Joel MacDonel"
		}
	},
	{ upsert: true }
)

// Ejecutar por segunda vez -> se hace update
db.users.updateOne(
	{ email: "joel.macdonel@fakegmail.com" },
	{ $set: {
		password: "some password",
		name: "Joel MacDonel"
		}
	},
	{ upsert: true }
)
//{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 0 }

// Ejercicio 9
db.comments.deleteMany(
	{
		"email" : "victor_patel@fakegmail.com",
		"date" :  {"$gte" : ISODate("1980-01-01T00:00:00Z"), "$lte" : ISODate("1980-12-31T00:00:00Z")}
	}
)

db.comments.find(
	{ 
		$and: [ 
			{"email" : "victor_patel@fakegmail.com" }, 
			{ "date" :  { "$gte" : ISODate("1980-01-01T00:00:00Z"), "$lte" : ISODate("1980-12-31T00:00:00Z")} } 
		] 
	},
)

// Parte 2 - Tareas

// Ejercicio 10
db.restaurants.find(
	{
		grades : {
			$elemMatch : {
				date : {"$gte" : ISODate("2014-01-01T00:00:00Z"), "$lte" : ISODate("2015-12-31T00:00:00Z")},
				score: { "$gt" :70, "$lte" : 90}
			}
		}
	},
	{ "_id":0, "restaurant_id" : 1, "grades":1 }
)

// Ejercicio 11
db.restaurants.updateOne(
	{ "restaurant_id" : "50018608" },
	{ 
		$addToSet: { 
			"grades" : { 
				$each: [ 
					{	
						"date" : ISODate("2019-10-10T00:00:00Z"),
						"grade" : "A",
						"score" : 18
					}, 
					{
						"date" : ISODate("2020-02-25T00:00:00Z"),
						"grade" : "A",
						"score" : 21
					}
				]
			}
		}
	}
)
