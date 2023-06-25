import boto3

sns = boto3.client('sns')

topic_name = 'customer_orders_notification'

response = sns.create_topic(
    Name=topic_name
    )
    
print(response)