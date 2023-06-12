#!/usr/bin/node
const process = require('process');
const argument = process.argv;

if (argument.length === 2) {
  console.log('No argument');
} else if (argument.length === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
