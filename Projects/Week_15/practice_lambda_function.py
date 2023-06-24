import json
import boto3
import random

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    q_url = 'https://sqs.us-east-1.amazonaws.com/582082071662/customer_orders'
    message = str(random.randint(1,100))
    
    sqs = boto3.client('sqs')
    
    response = sqs.send_message(
        QueueUrl=q_url,
        MessageBody=message,
        DelaySeconds=1
        )
    
    return {
        'body':json.dumps(message),
        'details':json.dumps(response['MessageId'])
    }
    