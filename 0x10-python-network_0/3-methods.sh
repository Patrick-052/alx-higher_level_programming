#!/bin/bash
#Displaying all HTTP methods the server will accept.
curl -sXLI OPTIONS "$1"
