import boto3

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
    if 'Contents' in response:
        keys = []
        for content in response['Contents']:
            keys.append(content['Key'])
        
        
    objects = [{'Key': content['Key']} for content in response['Contents']]
    
    response = client.delete_objects(
       Bucket=bucket,
       Delete={
           'Objects':objects
           
      },
    )
    
    while response.get('NextContinuationToken'):
        response = client.list_objects_v2(Bucket=bucket, 
                        ContinuationToken=response['NextContinuationToken'])
        
        objects = [{'Key': content['Key']} for content in response['Contents']]
        
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
           '    Objects':objects
           } 
    )


s3 = boto3.client('s3')

bucket = 'tpuntillo-boto3-06122023'

empty_bucket(s3, bucket)

response = s3.delete_bucket(
    Bucket=bucket
)