import boto3

def stop_instances(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
            ],
        )
    
def kill_all():
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == 'running':
                if instance["InstanceId"] != ide_id:
                        stop_instances(ec2, instance["InstanceId"])

def main():
    kill_all()
ec2 = boto3.client('ec2')

ide_id = 'i-0655792865e66712d'

response = ec2.describe_instances()

if __name__ == '__main__':
    main()
    
            
    
            
            
            

      
      

    