from flask import Flask, request
import os
from datetime import datetime
from dotenv import load_dotenv
import boto3
import json
import logging as logger


app = Flask(__name__)

# Load env vars
load_dotenv()

# Grab secrets from environment variables
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')

# Create SQS client
sqs = boto3.client('sqs')

sqs_client = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

@app.route('/')
def base_route():
    return 'Base Notification Route'

# Service to post a notification to the queue, accepts json to be posted
@app.route('/notify/', methods=['POST'])
def notify():

    # Take the JSON that was posted and use as message for Queue
    notify_message = request.json

    # Post message to SQS queue
    response = sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        DelaySeconds=10,
        MessageBody=json.dumps(notify_message)
    ) 
    
    return response


if __name__ == '__main__':
    # Force to run on specific ports set in env vars
    app.run(host=os.environ.get('HTTP_HOST'),
        port=int(os.environ.get('HTTP_PORT')))