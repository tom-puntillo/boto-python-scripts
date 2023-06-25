import boto3

sns = boto3.client('sns')

topic_arn = 'arn:aws:sns:us-east-1:582082071662:customer_orders_notifications'
protocol = 'email'
endpoint = 'tom.puntillo@gmail.com'

response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol=protocol,
    Endpoint=endpoint
    )
    
print(response)
    