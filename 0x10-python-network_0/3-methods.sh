#!/bin/bash
#Displaying all HTTP methods the server will accept.
curl -sXI OPTIONS "$1" | grep "Allow:" | cut -d" " -f2-
