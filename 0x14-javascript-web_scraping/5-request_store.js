#!/usr/bin/node
/* Retrieving data from an API url =>arg[2] and
saving the data in a file =>arg[3] */

const request = require('request');
const fs = require('fs');
const arg = process.argv;

request(arg[2], (error, response, body) => {
  if (error) {
    console.log('Error:', error.message);
  } else {
    fs.writeFile(arg[3], body, 'utf-8', (error) => {
      if (error) throw error;
      console.log('saved!');
    });
  }
});
