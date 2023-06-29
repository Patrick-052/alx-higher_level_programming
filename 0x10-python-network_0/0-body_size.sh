#!/bin/bash
# displaying the size of the response in bytes
curl -sL "$1" | wc -c
