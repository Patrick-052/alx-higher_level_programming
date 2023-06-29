#!/usr/bin/env bash
# Sending a request to a URL and
#+displaying the size of the body of the response

curl -L -s http://www.youtube.com/ | wc -c
