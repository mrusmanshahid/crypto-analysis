import logging
import redis
from redis import BlockingConnectionPool

class RedisOps:

    def get_connection(self, cluster):
        try:
            redis_client = redis.StrictRedis(host=cluster.get("Endpoint"), port=cluster.get("Port"),socket_timeout=10)
            redis_client.ping()
            return redis_client
        except Exception as e:
            logging.info(e)

    def get_value_from_key(self, redis_client, key):
        try:
            return redis_client.get(key)
        except:
            return "failed to retrieve sample"

    def get_keyword_result(self, cluster, redis_client, keyword):
        logging.info(f"Scanning data for -> {keyword}")
        _keyword = f"*{keyword}*"
        data = []
        cur, keys = redis_client.scan(cursor=0, match=_keyword, count=100)
        for key in keys:
            data.append({
                'Cluster': cluster.get("ClusterId"),
                'Key': key, 
                'SampleValue': self.get_value_from_key(redis_client,key),
                'Keyword': keyword
            })
        return data