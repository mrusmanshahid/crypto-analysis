from logging import Filter
from aws.clients import Client
from configs import Config as conf

class ElasticCache:

    def get_all_replication_clusters(self):
        client = Client().get_client("elasticache")
        if conf.cluster:
            clusters = client.describe_replication_groups(
                MaxRecords=100,
                ReplicationGroupId = conf.cluster
            )
            return clusters['ReplicationGroups']
        clusters = client.describe_replication_groups(
                MaxRecords=100
            )
        return clusters['ReplicationGroups']
    
    def get_all_independent_clusters(self):
        client = Client().get_client("elasticache")
        clusters = client.describe_cache_clusters(
            ShowCacheNodeInfo=True
        )
        return clusters['CacheClusters']

    