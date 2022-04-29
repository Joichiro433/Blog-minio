"""
Requirements
------------
$ pip install boto3
"""

import boto3


BUCKET_NAME = 'localbucket'

if __name__ == '__main__':
    s3 = boto3.resource(
        service_name='s3', 
        endpoint_url='http://localhost:9000',
        aws_access_key_id='localid',
        aws_secret_access_key='localpassword',
        region_name='')
    bucket = s3.Bucket(BUCKET_NAME)
    for obj in bucket.objects.all():
        print(obj.key)
