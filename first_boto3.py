import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='tpuntillo-boto3-06122023'
  ) 
  
print(response)

print(response)