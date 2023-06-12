#!/usr/bin/node
const process = require('process');
const argument = process.argv;

if (argument[2] != null) {
  console.log(argument[2]);
} else {
  console.log('No argument');
}
