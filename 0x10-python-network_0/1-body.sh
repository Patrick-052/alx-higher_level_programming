#!/bin/bash
#displaying the body of the response obtained by (GET)
curl -sL -w "%{http_code}\n" -o /dev/null | grep -q "200" && curl -sL
