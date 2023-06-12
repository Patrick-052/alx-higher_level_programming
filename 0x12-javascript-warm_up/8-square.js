#!/usr/bin/node
const argument = process.argv;
const num = parseInt(argument[2]);

if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    const row = [];
    for (let j = 0; j < num; j++) {
      row.push('X');
    }
    console.log(row.join(''));
  }
} else {
  console.log('Missing size');
}
