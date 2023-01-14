sh.enableSharding("DB_NAME")

db.adminCommand( { shardCollection: "DB_NAME.MyCollection", key: { oemNumber: "hashed", zipCode: 1, supplierId: 1 } } )
