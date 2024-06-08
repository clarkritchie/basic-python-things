#!/usr/local/bin/python

import json

import os
from pystalk import BeanstalkClient

queue = os.getenv("JOB_QUEUE_NAME")
port = os.getenv("JOB_QUEUE_PORT")
tube = os.getenv("JOB_QUEUE_TUBE")

client = BeanstalkClient(queue, port)
# client.use(tube)
print(f"Sending a message to {queue}:{port} on tube {tube}")
client.put_job(json.dumps({"foo": "bar"}), delay=30)