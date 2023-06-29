#!/bin/bash
#Displaying all HTTP methods the server will accept.
curl -sXL OPTIONS "$1"
