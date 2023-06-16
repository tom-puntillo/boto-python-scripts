import boto3

ec2 = boto3.client('ec2')

def stop_instances():
    instance_ids = ['i-0cfe5e7b5e12f7a46', 'i-0e82c0c19c45db77f', 'i-0749a6e6eab1b0edc']
    response = ec2.stop_instances(
    InstanceIds=instance_ids)
    print(response)

def main():
    stop_instances()

if __name__ == '__main__':
    main()