import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0bf8b923aeef31da7',
)

print(response)