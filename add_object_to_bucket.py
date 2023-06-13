import boto3

s3 = boto3.client('s3')

S3.put_object(Bucket = 'tpuntillo-boto3-06122023', Key = 'test_text.txt', )