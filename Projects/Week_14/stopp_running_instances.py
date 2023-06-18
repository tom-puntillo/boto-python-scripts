import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

ide_id = 'i-0655792865e66712d'

for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == 'running':
                if instance["InstanceId"] != ide_id:
                        stop_instances(ec2, instance["InstanceId"])


