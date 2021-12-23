import logging
import csv
import io
from aws.elastic_cache import ElasticCache
from configs import Config as conf
from environment_variables import ACCOUNT
from redis_ops import RedisOps
from file_operation import FileOperations

class ElasticCacheAnalysis:

    def __init__(self):
        pass
    
    def save_csv(self,cluster,records):
        if len(records) == 0:
            logging.info("Nothing to write")
            return
        logging.info("Storing data locally")
        cluster_id = cluster.get("ClusterId")
        filename = f"redis_{ACCOUNT.lower()}_{cluster_id}.csv"
        csvio = io.StringIO()
        dict_writer = csv.DictWriter(csvio, fieldnames=records[0].keys(),delimiter='|')
        dict_writer.writeheader()
        dict_writer.writerows(records)
        FileOperations().put_meta_data_files_to_bucket(csvio,filename)
    
    def get_all_endpoints(self):
        logging.info(f"Fetching all endpoints for {ACCOUNT}")
        endpoints = []
        elastic_cache = ElasticCache()
        dependent_clusters = elastic_cache.get_all_replication_clusters()
        for cluster in dependent_clusters:
            if "ConfigurationEndpoint" in cluster:
                endpoints.append({
                    'ClusterId': cluster.get("ReplicationGroupId"),
                    'Endpoint': cluster.get("ConfigurationEndpoint").get("Address"), 
                    'Port': cluster.get("ConfigurationEndpoint").get("Port")
                })
            else:
                endpoints.append({
                    'ClusterId': cluster.get("ReplicationGroupId"),
                    'Endpoint': cluster.get("NodeGroups")[0].get("PrimaryEndpoint").get("Address"), 
                    'Port': cluster.get("NodeGroups")[0].get("PrimaryEndpoint").get("Port")
                })
        logging.info(f"Total {len(endpoints)} nodes(s) fetched.")
        return endpoints

    def fetch_pii_fields(self, cluster):
        redis = RedisOps()
        data = []
        redis_client = redis.get_connection(cluster)
        if not redis_client:
            return []
        for keyword in conf.keywords:
            data.extend(redis.get_keyword_result(cluster,redis_client,keyword))
        return data
    
    def process_data(self):
        clusters = [{
            'ClusterId': 'cac105dwt7ei69fh',
            'Endpoint':'cac105dwt7ei69fh-ro.4j0ura.ng.0001.euw1.cache.amazonaws.com',
            'Port':'6379'
        },{
            'ClusterId': 'prc1xhmmagnsm9nr',
            'Endpoint':'prc1xhmmagnsm9nr-ro.6h6csz.ng.0001.euw1.cache.amazonaws.com',
            'Port':'6379'
        },{
            'ClusterId': 'prc29thwdnqb2c7',
            'Endpoint':'prc29thwdnqb2c7-ro.6h6csz.ng.0001.euw1.cache.amazonaws.com',
            'Port':'6379'
        }] #self.get_all_endpoints()
        logging.info(f"Clusters -> {clusters}")
        logging.info("Starting gathering data from Redis tables")
        for cluster in clusters:
            endpoint = cluster.get("Endpoint")
            logging.info(f"Fetching data for the cluster -> {endpoint}")
            data = self.fetch_pii_fields(cluster)
            self.save_csv(cluster,data)
 