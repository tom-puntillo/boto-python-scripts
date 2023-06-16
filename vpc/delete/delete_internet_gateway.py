import boto3

ec2 = boto3.client('ec2')

internet_gateway_id = 'igw-0be7d7b58f96ee682'

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
