from configs import Config
from meta_data import ElasticCacheAnalysis


def main():
    Config().load_configs()
    ElasticCacheAnalysis().process_data()

def lambda_handler(event, context):
    Config().load_configs()
    ElasticCacheAnalysis().process_data()  
    
if __name__ == "__main__":
    main()
