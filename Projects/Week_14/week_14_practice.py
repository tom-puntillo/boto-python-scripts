import boto3

def stop_instances(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
            ],
        )
        
instance_id =[]   

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == 'running':
            instance_id.append(instance["InstanceId"]),
            stop_instances(ec2, instance_id)
            
            

      
      

    