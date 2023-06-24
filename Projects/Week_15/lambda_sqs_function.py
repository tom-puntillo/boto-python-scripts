import json
import boto3
import random

sqs= boto3.client('sqs')

def lambda_handler(event, context):
    queue_url = 'https://sqs.us-east-1.amazonaws.com/582082071662/customer_orders'
    message = str(random.randint(1,100))
    
    response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message,
    DelaySeconds=1
)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
    