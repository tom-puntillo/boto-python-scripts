import boto3

def stop_instances(client, instance_id):
    response = client.stop_instances(
        InstanceIds=[instance_id],
    )

instance_id = 'i-0cd54c8eee80de55c'

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

def kill_all():
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == 'running':
                for tag in instance["Tags"]:
                    if tag["Key"] == 'Environment' and tag["Value"] == 'Dev':
                        if instance["InstanceId"] != instance_id:
                            stop_instances(ec2, instance["InstanceId"])
                            
def main():
    kill_all()
    
if __name__ == '__main__':
    main()


                    
