#!/usr/bin/node
const process = require('process');
const argument = process.argv;
const num = parseInt(argument[2]);

if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
