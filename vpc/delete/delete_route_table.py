import boto3

ec2 = boto3.client('ec2')

route_table_id ='rtb-03d77fb1bc1b3386c'

ec2.delete_route_table(
    RouteTableId=route_table_id,
)
