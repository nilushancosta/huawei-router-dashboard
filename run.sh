#!/bin/bash

### Written by Nilushan Costa

### Purpose - Configure variables and start the router dashboard
### Input - None
### Output - None

DEFAULT_GATEWAY_IP=
MAX_DOWNLOAD_SPEED=
MAX_UPLOAD_SPEED=

if [ -z $DEFAULT_GATEWAY_IP ]; then
	echo "ERROR: DEFAULT_GATEWAY_IP not found! Please set the default gateway IP address"
	exit 1
fi

if [ -z $MAX_DOWNLOAD_SPEED ]; then
	echo "ERROR: MAX_DOWNLOAD_SPEED not found! Please set the maximum download speed"
	exit 1
fi

if [ -z $MAX_UPLOAD_SPEED ]; then
	echo "ERROR: MAX_UPLOAD_SPEED not found! Please set the maximum upload speed"
	exit 1
fi

if [ $MAX_DOWNLOAD_SPEED -gt $MAX_UPLOAD_SPEED ]; then
	yAxisMax=$MAX_DOWNLOAD_SPEED
else
	yAxisMax=$MAX_UPLOAD_SPEED
fi

`which node` ./getSpeeds.js $DEFAULT_GATEWAY_IP | `which python3` ./plotGraph.py $yAxisMax
