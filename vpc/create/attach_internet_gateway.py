import boto3

ec2 = boto3.client('ec2')

attachment = ec2.attach_internet_gateway(
    InternetGatewayId='igw-c0a643a9',
    VpcId='vpc-a01106c2',
)

print(response)