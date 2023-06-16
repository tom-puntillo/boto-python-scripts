import boto3

ec2 = boto3.client('ec2')

gateway_id = "igw-0be7d7b58f96ee682"
route_table_id = "rtb-03d77fb1bc1b3386c"

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=gateway_id,
    RouteTableId=route_table_id,
)
