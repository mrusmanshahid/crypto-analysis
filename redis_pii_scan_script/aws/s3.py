from logging import Filter
from aws.clients import Client
from configs import Config as conf


class S3:

    def put_object_to_object(self, filepath, filename):
        s3 = Client().get_resource("s3")
        s3.Bucket(conf.bucket).upload_file(filepath, f"{conf.bucket_folder}/{filename}")

    
    def put_object_from_io(self, csvio, filename):
        s3 = Client().get_client("s3")
        s3.put_object(Body=csvio.getvalue(), ContentType='application/vnd.ms-excel', Bucket=conf.bucket, Key=f"{conf.bucket_folder}/{filename}", ACL="bucket-owner-full-control") 
