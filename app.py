from flask import Flask
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# Load env vars
load_dotenv()

# Grab secrets from environment variables
QUEUE_URL = os.environ.get('QUEUE_URL')


@app.route('/')
def base_route():
    return 'Base Notification Route'

# Service to post a notification to the queue
@app.route('/notify/<base>/<quote>')
def notify(base, quote):

    # TODO Figure out what data needs to go for notification
    
    

    return 1


if __name__ == '__main__':
    # Force to run on specific ports set in env vars
    app.run(host=os.environ.get('HTTP_HOST'),
        port=int(os.environ.get('HTTP_PORT')))