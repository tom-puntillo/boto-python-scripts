import boto3

ec2 = boto3.client('ec2')

def stop_instances():
    instance_ids = ['i-02516c5514102ac58', 'i-0875dee5d93ccc110', 'i-049a202a7b420fc01', 'i-0ded5b6703918c653']
    response = ec2.stop_instances(
    InstanceIds=instance_ids)
    print(response)

def main():
    stop_instances()

if __name__ == '__main__':
    main()