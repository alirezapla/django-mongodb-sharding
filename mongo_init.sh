#!/bin/bash

docker-compose exec config1 sh -c "mongo --port 27017 < /scripts/configserver.js"
sleep 5
docker-compose exec shard1a sh -c "mongo --port 27018 < /scripts/shard1.js"
docker-compose exec shard2a sh -c "mongo --port 27018 < /scripts/shard2.js"
sleep 30
docker-compose exec router sh -c "mongo < /scripts/router.js"
#sleep 5
#docker-compose exec router sh -c "mongo < /scripts/data.js"