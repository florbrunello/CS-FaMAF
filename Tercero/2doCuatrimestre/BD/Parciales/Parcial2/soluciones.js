/* Parcial II: No-SQL - Brunello, Florencia */

// Ejercicio 1
db.sales.find(
    {
        "storeLocation" : { $in : ["London", "Austin", "San Diego"]},
        "customer.age" : { $gte: 18 }, 
        "items" : {
            $elemMatch : {
                "price" : { $gte : NumberDecimal(1000) },
                "tags" : { $in : ["school", "kids" ]}
            }
        }
    },
    {
        "_id" : 0,
        "sale" : "$_id", 
        "saleDate" : 1,
        "storeLocation" : 1, 
        "email" : "$customer.email"
    }
)

// Ejercicio 2
db.sales.aggregate([
    {
        $match : {
            "storeLocation" : "Seattle", 
            "purchaseMethod" : { $in : ["In store", "Phone"] }, 
            "saleDate" : { 
                $gte : ISODate("2014-02-01T00:00:00Z"), 
                $lte: ISODate("2015-01-31T00:00:00Z")
            }
        }
    },
    {
        $unwind: "$items"
    },
    {
        $project: {
            "_id" : 0,
            "email" : "$customer.email",
            "satisfaction" : "$customer.satisfaction",
            "montototal" : {
                $multiply: [ { $convert: {
                                    input: "$items.price", 
                                    to: "int", 
                                    onError: 0
                                }
                            }, "$items.quantity" ]
            }
        }
    },
    {
        $sort: {
            "satisfaction" : -1, 
            "email" : 1
        }
    }
])

// Ejercicio 3
db.createView("salesInvoiced", "sales", 
[
    {
        $unwind: "$items"
    },
    {
        $group: {
            "_id": {
                year: { $year: "$saleDate" },
                month: { $month: "$saleDate" }
            },
            "montominimo" : {
                $min: {
                    $multiply: [ { $convert: {
                                        input: "$items.price", 
                                        to: "int", 
                                        onError: 0
                                    }
                                }, "$items.quantity" ] }
            },
            "montomaximo" : { 
                $max: {
                    $multiply: [ { $convert: {
                                        input: "$items.price", 
                                        to: "int", 
                                        onError: 0
                                    }
                                }, "$items.quantity" ] }
            },
            "montototal" : {
                $sum: {
                    $multiply: [ { $convert: {
                                        input: "$items.price", 
                                        to: "int", 
                                        onError: 0
                                    }
                                }, "$items.quantity" ] }
            },
            "montopromedio" : {
                $avg: { 
                    $multiply: [ { $convert: {
                                        input: "$items.price", 
                                        to: "int", 
                                        onError: 0
                                    }
                                }, "$items.quantity" ] 
                }
            }
        }
    },
    {
        $project: {
            "_id" : 0,
            "year" : "$_id.year",
            "month" : "$_id.month",
            "montominimo" : 1,
            "montomaximo" : 1,
            "montototal" : 1,
            "montopromedio" : 1
        }
    },
    {
        $sort: {
            year: -1, 
            month: -1
        }
    }
])

// Ejercicio 4
db.sales.aggregate([
    {
        $unwind: "$items"
    },
    {
        $group: {
            "_id": "$storeLocation",
            "ventapromedio" : {
                $avg: { 
                    $multiply: [ { $convert: {
                                        input: "$items.price", 
                                        to: "int", 
                                        onError: 0
                                    }
                                 }, "$items.quantity" ] 
                }
            },
        }
    }, 
    {
        $lookup: {
            from: "storeObjectives", 
            localField: "_id",
            foreignField: "_id",
            as: "store"
        }
    },        
    {
        $project: {
            "_id" : 0,
            "storeLocation" : { $arrayElemAt : ["$store._id" , 0 ] },
            "ventapromedio" : 1, 
            "objetivo" : { $arrayElemAt : [ "$store.objective", 0 ] },
            "diferencia" : {
                $subtract: [ "$ventapromedio" , { $first : "$store.objective" }] }
            }
    }
])

// Ejercicio 5
db.runCommand({ 
    collMod: "sales", 
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: [ "saleDate", "storeLocation", "customer", "purchaseMethod" ],
            properties: {
                saleDate : {
                    bsonType : "date", 
                    description: "Fecha en que se hizo la venta, es requerido"
                },
                storeLocation : {
                    bsonType : "string", 
                    description: "Ubicacion de la tienda, es requerido"
                },
                purchaseMethod : {
                    bsonType : "string", 
                    description: "Forma de pago, es requerido"
                },
                customer : {
                    bsonType : "object", 
                    required : [ "gender", "age", "email", "satisfaction" ],
                    properties: { 
                        gender : {
                            bsonType: "string"
                        },
                        age : {
                            bsonType: "int", 
                        }, 
                        email : {
                            bsonType: "string"
                        }, 
                        satisfaction : {
                            bsonType: "int", 
                            minimum: 0,
                            maximum: 10
                        }
                    }
                }
            }
        }
    }
})

/* Caso de Éxito */ 
db.sales.insert({
    "saleDate": ISODate("2015-03-23T21:06:49.506Z"),
    "storeLocation" : "Denver",
    "customer" : {
		"gender" : "F",
		"age" : NumberInt(30),
		"email" : "fl.brunello@witwuta.sv",
		"satisfaction" : NumberInt(9),
	},
    "purchaseMethod" : "Online",
})

/* Caso de Falla */
db.sales.insert({
    "saleDate": ISODate("2015-03-23T21:06:49.506Z"),
    "customer" : {
		"gender" : "F",
		"age" : 30,
		"email" : "fl.brunello@witwuta.sv",
		"satisfaction" : 10,
	},
    "purchaseMethod" : "Online",
})
