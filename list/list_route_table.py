import boto3


ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routeTable in response["RouteTables"]:
    print(routeTable["VpcId"], routeTable["RouteTableId"])
    
    for association in routeTable['Associations']:
        print(association["RouteTableAssociationId"])
        if "SubnetId" in association:
            print(association["SubnetId"])
    
    for route in routeTable["Routes"]:
        if "DestinationCidrBlock" in route:
            print(route["DestinationCidrBlock"])
        else:
            pass
        
    for route in routeTable["Routes"]:
        if "GatewayId" in route:
            print(route["GatewayId"])
        else:
            pass

        