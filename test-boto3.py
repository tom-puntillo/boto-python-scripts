import boto3

session = boto3.Session()

s3 = boto.client('s3')
s3 = session.client('s3')

s3 = boto3.resource('s3')