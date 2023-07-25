#!/usr/bin/node
/* Retrieving data from an API url =>arg[2] and
saving the data in a file =>arg[3] */

const request = require('request');
const fs = require('fs');
const arg = process.argv;

request(arg[2]).pipe(fs.createWriteStream(arg[3]));
