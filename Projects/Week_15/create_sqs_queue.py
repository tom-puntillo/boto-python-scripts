import boto3

sqs = boto3.client('sqs')

q_name = 'customer_orders'

response = sqs.create_queue(
    QueueName=q_name)
    
print(response)