import json
import boto3

def lambda_handler(event, context):
   
    sqs = boto3.client('sqs')
    
    queue_url = 'https://sqs.us-east-1.amazonaws.com/582082071662/customer_orders'
    
    response = sqs.receive_message(
        QueueUrl=queue_url
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Messages')
    }
