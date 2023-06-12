#!/usr/bin/node
const argument = process.argv;
const num = parseInt(argument[2]);

function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
