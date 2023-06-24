import boto3

# Create an instance of the SQS client
sqs = boto3.client('sqs')

# Define the name of the queue
queue_name = 'customer_orders'

# Create the queue using the SQS client
response = sqs.create_queue(
    QueueName=queue_name
    )
    
# Print the response from the create_queue operation
print(response)
