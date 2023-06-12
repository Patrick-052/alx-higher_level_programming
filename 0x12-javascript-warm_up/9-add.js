#!/usr/bin/node
const argument = process.argv;
const a = parseInt(argument[2]);
const b = parseInt(argument[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(a, b);
