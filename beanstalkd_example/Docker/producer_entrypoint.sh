#!/usr/bin/env bash

while true; do
    echo "Sending something into the queue"
	/app/index.py
	sleep 5
done
