import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-0499fb7df20502b2e'

routeTable = ec2.create_route_table(VpcId=vpc_id)



print(routeTable["RouteTable"]["RouteTableId"])

