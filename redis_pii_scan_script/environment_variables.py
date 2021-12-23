import os

ACCOUNT = os.environ.get('ACCOUNT', 'RH-PROD')

KEYWORDS_FILE_PATH = os.environ.get('KEYWORDS_FILE_PATH', 'resources/keywords.yaml') 

BUCKET = os.environ.get('BUCKET', 'careem-storage-team')

BUKCET_FOLDER = os.environ.get('BUKCET_FOLDER', 'redis-data')

REDIS_CLUSTER = os.environ.get('CLUSTER')