#!/bin/bash
#Displaying all HTTP methods the server will accept.
curl -sX OPTIONS "$1"
