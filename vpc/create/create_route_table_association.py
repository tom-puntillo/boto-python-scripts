import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-03d77fb1bc1b3386c'
subnet_id = 'subnet-00b08fa9ce437b7e9'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(association["AssociationId"])