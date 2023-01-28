# django-mongodb-sharding
mongodb with django(sharding)

![alt text](https://github.com/minhhungit/mongodb-cluster-docker-compose/blob/master/images/sharding-and-replica-sets.png)

first run services by

```python
docker-compose up -d
```
then run `mongo_init.sh`

```bash
sh mongo_init.sh
```
Enable sharding 

```bash
sh enable_sharding.sh
```
ready to use
