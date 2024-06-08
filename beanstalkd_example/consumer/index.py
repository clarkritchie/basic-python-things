#!/usr/local/bin/python

import os
from pystalk import BeanstalkClient

queue = os.getenv("JOB_QUEUE_NAME")
port = os.getenv("JOB_QUEUE_PORT")
tube = os.getenv("JOB_QUEUE_TUBE")

client = BeanstalkClient(queue, port)
client.use(tube)

print(f"Checking for messages on {queue}:{port} using tube {tube}")

for job in client.reserve_iter():
    print("Received job")
    try:
        print(job)
    except Exception:
        client.release_job(job.job_id)
        raise
    client.delete_job(job.job_id)