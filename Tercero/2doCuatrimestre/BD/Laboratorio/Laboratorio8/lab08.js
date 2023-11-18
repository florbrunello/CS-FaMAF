// Tareas
 
// Ejercicio 1
db.theaters.aggregate([
    {
        $group: {
            "_id" : "$location.address.state",
            "totalTheaters": { "$sum" : 1}
        }
    }, 
    {
        $project: { "_id" : 1, "totalTheaters": 1}
    }
])

// Ejercicio 2
db.theaters.aggregate([
    {
        $group: {
            "_id" : "$location.address.state", 
            "totalTheaters": { "$sum" : 1},
        }
    },
    { 
        $match: { "totalTheaters": { $gt: 2 }}
    }, 
    { 
        $sort: {  "_id": 1  }
    }
])

// Ejercicio 3
db.movies.aggregate([
    { 
        "$match": { "directors" :  "Louis Lumière" }
    }, 
    {
        $count: "totalMovies"
    }
])

// Ejercicio 4
db.movies.aggregate([
    { 
        $match: { "released" :  { $gte:  ISODate("1950-01-01T00:00:00Z"),"$lte" : ISODate("1959-12-31T00:00:00Z")}}
    }, 
    {
        $count: "totalMovies"
    }
])

// Ejercicio 5
db.movies.aggregate([
    {
        $unwind: "$genres"
    }, 
    {
        $group: {
            "_id": "$genres",
            "totalGenres": { $sum: 1 }
        }
    }, 
    {
        $sort: { "totalGenres" : -1 }
    },
    { 
        $limit: 10 
    },
    {
        $project: { "_id": 1, "totalGenres":1 }
    }
])

// Ejercicio 6
db.users.aggregate([
    {
        $lookup: {
            from: "comments",
            localField: "email", 
            foreignField: "email", 
            as: "cmts"
        }
    }, 
    {
        $project: {
            "_id":0,
            "name": 1,
            "email": 1,
            totalComments: { $size: "$cmts" }
        }
    },
    {
        $sort: { "totalComments" : -1 }
    },
    {
        $limit: 10
    }
])

// Ejercicio 7
db.movies.aggregate([

    {
      $match: {
        released: {
          $gte: ISODate("1980-01-01T00:00:00Z"),
          $lte: ISODate("1989-12-31T00:00:00Z"),
        },
        "imdb.rating": { $exists: true, $ne: null, $type: "number" }
      },
    },
    {
      $group: {
        "_id": {$year: "$released"},
        "promedio" : { $avg: "$imdb.rating" },
        "minimo" : { $min: "$imdb.rating" },
        "maximo" : { $max: "$imdb.rating" }
      }
    },
    {
      $sort: { promedio: -1}
    }
  ])

// Ejercicio 8
db.movies.aggregate([
    {
        $lookup: {
            from: "comments",
            localField: "_id", 
            foreignField: "movie_id",
            as: "movie_comts"
        }
    }, 
    {
        $project: {
            "_id" : 0, "title" : 1, "year" : 1, "totalcmts" : { $size: "$movie_comts" }
        }
    }, 
    {
        $sort : {"totalcmts" : -1},
    },
    {
        $limit : 10
    }
])

// Ejercicio 9
pipeline = [
    {
        $unwind: "$genres"
    },
    {
        $lookup: {
            from: "comments",
            localField: "_id", 
            foreignField: "movie_id",
            as: "movie_comts"
        }
    },
    {
        $group: 
        {
            "_id" : "$genres",
            "totalcmts" : { $sum : { $size: "$movie_comts" }}
        }
    }, 
    {
        $sort : { "totalcmts" : -1}
    }, 
    {
        $limit : 5
    }
]

db.createView("top5genres", "movies", pipeline)

// Ejercicio 10
db.movies.aggregate([
    {
        $match: {
            directors: "Jules Bass",
        }
    },
    {
        $unwind: "$cast"
    },
    {
        $group: {
            _id: "$cast",
            movies: {
                $addToSet: {
                    title: "$title",
                    year: "$year"
                }    
            }
        }
    },
    {
        $match: {
            $expr: {$gte: [{$size: "$movies"}, 2]}
        }
    },
    {
        $project: {
            "actor": "$_id",
            movies: 1,
            _id: 0
        }
    }
])

// Ejercicio 11
db.comments.aggregate([
    {
      $lookup: {
        from: "movies",
        localField: "movie_id",
        foreignField: "_id",
        let: {
          comment_year: {
            $year: "$date"
          },
          comment_month: {
            $month: "$date"
          }
        },
        pipeline: [
          {
            $set: {
              released_year: {
                $year: "$released"
              },
              released_month: {
                $month: "$released"
              }
            }
          },
          {
            $match: {
              released: {
                $exists: true
              },
              $expr: {
                $and: [
                  {
                    $eq: ["$released_year", "$$comment_year"]
                  },
                  {
                    $eq: ["$released_month", "$$comment_month"]
                  }
                ]
              }
            }
          }
        ],
        as: "movie"
      }
    },
    {
      $unwind: {
        path: "$movie",
        preserveNullAndEmptyArrays: false
      }
    },
    {
      $lookup: {
        from: "users",
        localField: "email",
        foreignField: "email",
        as: "user"
      }
    },
    {
      $unwind: {
        path: "$user",
        preserveNullAndEmptyArrays: false
      }
    },
    {
      $project: {
        name: "$user.name",
        email: "$user.email",
        date: "$date",
        title: "$movie.title",
        released: "$movie.released",
        text: "$text"
      }
    },
    {
      $match: {
        email: "edward_barrett@fakegmail.com"
      }
    }
])

// Ejercicio 12
// a)
db.restaurants.aggregate([
    {
        $unwind: "$grades"
    },
    {
        $group: {
            "_id" : "$restaurant_id",
            "name" : { $first: "$name" },
            "max_puntuacion" : { $max : "$grades.score" },
            "min_puntuacion" : { $min : "$grades.score" },
            "suma_total" : { $sum : "$grades.score" }
        }
    }, 
    {
        $sort : { _id : 1 }
    }
])

// b)
db.restaurants.aggregate([
    {
        $project: {
            "_id" : 0,
            "restaurant_id" : 1,
            "name" : 1,
            "max_puntuacion" : { $max : "$grades.score" },
            "min_puntuacion" : { $min : "$grades.score" },
            "suma_total" : { $sum : "$grades.score" }
        }
    },
    {
        $sort : { restaurant_id : 1 }
    }
])

// c)
db.restaurants.aggregate([
    {
        $project: {
            "_id" : 0,
            "restaurant_id" : 1,
            "name" : 1,
            "max_puntuacion" : { $max : "$grades.score" },
            "min_puntuacion" : { $min : "$grades.score" },
            "suma_total" : { $reduce : {
                                input: "$grades.score", 
                                initialValue: 0,
                                in: { $add : ["$$value", "$$this"] } 
                            }
                           }
        }
    },
    {
        $sort : { restaurant_id : 1 }
    }
])

// d)
db.restaurants.find(
    { },
    {
        restaurant_id: 1,
        name: 1,
        max_score: { $max: "$grades.score" },
        min_score: { $min: "$grades.score" },
        total_score: {    
            $reduce: {
                input: "$grades.score",
                initialValue: 0,
                in: { $add : ["$$value", "$$this"] }
            }
        },
        _id: 0
    }
).sort({ "restaurant_id" :1 })

//Ejercicio 13
db.restaurants.aggregate([
    {
        $addFields: { average_score: { $avg: "$grades.score" } }
    },
    {
        $addFields: { grade: {
                        $switch: {
                            branches: [
                                { case: { $and: [ { $gte: ["$average_score", 0] }, { $lte: ["$average_score", 13] } ] }, then: "A" },
                                { case: { $and: [ { $gte: ["$average_score", 14] }, { $lte: ["$average_score", 27] } ] }, then: "B" },
                                { case: { $gte: ["$average_score", 28] }, then: "C" },
                            ],
                            default: "Unknown"
                        }
                       }
                    }  
    }
])
