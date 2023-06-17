import boto3

ec2 = boto3.client('ec2')

group_name = 'boto3-security-group'
vpc_id = 'vpc-0c89411b70a35fac0'

response = ec2.create_security_group(
    Description='SG from boto3',
    GroupName=group_name,
    VpcId=vpc_id
)

print(response["GroupId"])