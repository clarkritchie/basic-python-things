#!/usr/bin/env bash

while true; do
	echo "Checking if the queue has anything to process"
	/app/index.py
	sleep 5
done