import os
import logging

class Config:

    def __init__(self):
        pass

    def load_configurations(self):
        self.set_logging_config()
        
    @staticmethod
    def set_logging_config():
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )