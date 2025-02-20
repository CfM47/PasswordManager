account_schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["entryName", "siteurl", "username", "password"],
            "properties": {
                "entryName": {
                    "bsonType": "string",
                    "description": "Debe ser una cadena y es obligatorio"
                },
                "siteurl": {
                    "bsonType": "string",
                    "description": "Debe ser una cadena y es obligatorio"
                },
                "email": {
                    "bsonType": "string",
                    "description": "Debe ser una cadena"
                },
                "username": {
                    "bsonType": "string",
                    "description": "Debe ser una cadena"
                },
                "password": {
                    "bsonType": "string",
                    "description": "Debe ser una cadena y es obligatorio"
                }
            }
        }
    }

card_schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["entryName", "code", "password"],
            "properties": {
                "entryName" : {
                  "bsonType": "string",
                  "description": "Tipo de la tarjeta, obligatorio"
                },
                "code": {
                    "bsonType": "string",
                    "description": "Código que identifica la tarjeta, obligatorio"
                },
                "password": {
                    "bsonType": "string",
                    "description": "Pin, oligatorio"
                }
            }
        }
    }

user_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "Debe ser una cadena y es obligatorio"
            },
            "hash": {
                "bsonType": "string",
                "description": "Debe ser una cadena, obligatoria"
            }
        }
    }
}