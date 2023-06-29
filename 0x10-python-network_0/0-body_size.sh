#!/bin/bash
# displaying the size of the response
curl -L -s -w '%{size_download}\n'
