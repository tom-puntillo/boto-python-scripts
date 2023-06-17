import boto3

def stop_instances(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
            ],
        )
        
    print(instance_id, "stopped")

def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    print(instance_id, "started")
    
def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    print(instance_id, "terminated")

#def main():
 #   stop_instances()

if __name__ == '__main__':
  #  main()
  instance_id = [
        'i-0a5573d119db11f1f',
        'i-0cfe5e7b5e12f7a46',
        'i-0e82c0c19c45db77f',
        'i-0749a6e6eab1b0edc',
        'i-0aa4653cea8b0ddee'
    ]
  
  ec2 = boto3.client('ec2')
start_instance(ec2, instance_id)