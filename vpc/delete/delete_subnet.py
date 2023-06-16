import boto3

ec2 = boto3.client('ec2')

subnet_id = 'subnet-00b08fa9ce437b7e9'

ec2.delete_subnet(
    SubnetId=subnet_id,
)
