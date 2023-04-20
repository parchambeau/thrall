from flask import Flask, request, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv
import boto3
import json

load_dotenv()


app = Flask(__name__)

# Load env vars
load_dotenv()

# Grab secrets from environment variables
QUEUE_URL = os.environ.get('QUEUE_URL')

# Create SQS client
sqs = boto3.client('sqs')

@app.route('/')
def base_route():
    return 'Base Notification Route'

# Service to post a notification to the queue, accepts json to be posted
@app.route('/notify/', methods=['POST'])
def notify(notification_type, message):

    print (request.json)
    # Take the JSON that was posted and use as message for Queue
    notify_message = request.json

    # Post message to SQS queue
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=10,
        MessageBody=json.dumps(notify_message)
    ) 
    
    return response


if __name__ == '__main__':
    # Force to run on specific ports set in env vars
    app.run(host=os.environ.get('HTTP_HOST'),
        port=int(os.environ.get('HTTP_PORT')))