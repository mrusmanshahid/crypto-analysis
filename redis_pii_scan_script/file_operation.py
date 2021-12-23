from configs import Config as conf
from aws.s3 import S3
import logging
import os

class FileOperations:

    def __init__(self):
        pass

    def put_meta_data_files_to_bucket(self, csvio ,filename):
        logging.info(f"Uploading {filename} to S3")
        S3().put_object_from_io(csvio, filename)
