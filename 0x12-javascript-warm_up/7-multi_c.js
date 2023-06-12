#!/usr/bin/node
const argument = process.argv;
const num = parseInt(argument[2]);

if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
