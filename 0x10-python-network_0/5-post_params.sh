#!/bin/bash
# A post request with variables and values
curl -sX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
