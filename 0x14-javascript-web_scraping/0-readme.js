#!/usr/bin/node
/* Reading a file and printing its content */

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
