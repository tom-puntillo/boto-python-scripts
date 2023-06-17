import boto3

def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    response = client.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_group_id
        ],
        UserData=user_data
    )
    
    print(response["Instances"][0]["InstanceId"])

ami_id = "ami-09e67e426f25ce0d7"
key_pair_name = "boto3_key_pair"
security_group_id = "sg-0bf8b923aeef31da7"

user_data='''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)
