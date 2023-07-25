#!/usr/bin/node
/* Writing to a file */

const process = require('process');
const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[2], arg[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  } else {
    console.log('saved!');
  }
});
