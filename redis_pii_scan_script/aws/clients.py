from boto3 import client, resource
import logging
from configs import Config as conf

class Client:
    
    def __init__(self):
        pass
        
    def get_sts_session_info(self):
        sts_connection = client('sts')
        sts_session = sts_connection.assume_role(
            RoleArn=F"arn:aws:iam::{self.account_arn}:role/{self.role}",
            RoleSessionName="cross_acct_lambda"
        )
        return  sts_session['Credentials']['AccessKeyId'], sts_session['Credentials']['SecretAccessKey'], sts_session['Credentials']['SessionToken']

    def get_session_client(self,client_type):
        ACCESS_KEY,SECRET_KEY,SESSION_TOKEN = self.get_sts_session_info()
        return client(
            client_type,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN,
        )

    def get_default_client(self,client_type):
        return client(client_type)

    def get_client(self, client_type):
        return self.get_default_client(client_type)

    def get_resource(self, resource_type):
        return resource(resource_type)