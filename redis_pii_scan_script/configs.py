import logging
import yaml
from environment_variables import KEYWORDS_FILE_PATH, BUCKET, BUKCET_FOLDER, REDIS_CLUSTER

class Config:

    def load_configs(self):
        self.set_logging_config()
        self.get_keywords()
        Config.bucket = BUCKET
        Config.bucket_folder = BUKCET_FOLDER
        Config.cluster = REDIS_CLUSTER
        logging.info("Fetching Automation Configurations")

    @staticmethod
    def set_logging_config():
        root = logging.getLogger()
        if root.handlers:
            for handler in root.handlers:
                root.removeHandler(handler)
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s [%(module)s:%(funcName)s:%(lineno)d] %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def get_keywords(self):
        logging.info("Loading keywords from file")
        with open(KEYWORDS_FILE_PATH, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
            Config.keywords =  data_loaded['Keywords']
            