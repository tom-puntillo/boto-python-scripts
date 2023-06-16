import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-0499fb7df20502b2e'

ec2.delete_vpc(
    VpcId=vpc_id,
)
