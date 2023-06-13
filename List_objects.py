import boto3

def list_object_keys(client, bucket, filter=None):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Filter=filter)
    for content in response['Contents']:
        keys.append(content['Key'])
    
    return keys

s3 = boto3.client('s3')



response = filter_objects_extension(s3, 'tpuntillo-boto3-06122023', '/')
print(response)