sh.enableSharding("django_mongodb")
sh.shardCollection('django_mongodb.post',{owner:"hashed"})
sh.shardCollection('django_mongodb.user',{username:"hashed"})
sh.shardCollection('django_mongodb.liker',{liker:"hashed"})
sh.shardCollection('django_mongodb.comment',{author:"hashed"})
