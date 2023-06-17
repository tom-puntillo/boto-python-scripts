import boto3

def stop_instances(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
            ],
        )
    

ec2 = boto3.client('ec2')

ide_id = 'i-0655792865e66712d'

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == 'running':
            print(instance["InstanceId"])
            
    if "InstanceId" == ide_id:
        pass        
    else ec2.stop_instances(
        InstanceIds=[instance["InstanceId"]])
    
            
    
            
            
            

      
      

    