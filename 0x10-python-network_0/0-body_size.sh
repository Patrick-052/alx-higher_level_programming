#!/usr/bin/env bash
# Sending a request to a URL and
#+displaying the size of the body of the response

curl -w '%{size_request}'
