#!/usr/bin/node
/* Writing to a file */

const fs = require('fs');
const arg = process.argv;

fs.writeFile(arg[2], arg[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
