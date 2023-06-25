import boto3

sns = boto3.client('sns')

topic_arn = 'arn:aws:sns:us-east-1:582082071662:customer_orders_notifications'
message = 'You have received a new customer order'

response = sns.publish(
    TopicArn=topic_arn,
    Message=message
    )
    
print(response)