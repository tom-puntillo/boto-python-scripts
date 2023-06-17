import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-0749a6e6eab1b0edc',
    Name='Dynamo DB Movie AMI')

print(response["ImageId"])