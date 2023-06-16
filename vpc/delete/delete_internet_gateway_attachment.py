import boto3

ec2 = boto3.client('ec2')

internet_gateway_id = 'igw-0be7d7b58f96ee682'
vpc_ic = 'vpc-0499fb7df20502b2e'


ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_ic,
)
