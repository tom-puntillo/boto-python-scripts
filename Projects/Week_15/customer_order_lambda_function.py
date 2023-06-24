import json
import boto3
import random

# Create an instance of the SQS client
sqs = boto3.client('sqs')

# Specify the URL of the queue
queue_url = 'https://sqs.us-east-1.amazonaws.com/582082071662/customer_orders'

# Define the Lambda handler function
def lambda_handler(event, context):
    # Generate a random message
    message = str(random.randint(1,50))
    
    # Send the message to the queue using the SQS client
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message,
        DelaySeconds=1
    )
    
    # Return a response indicating the success of the operation
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
