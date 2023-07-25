#!/usr/bin/node
/* Displaying status code of a get request from a url=>arg[2] */

const request = require('request');
const arg = process.argv;

request(arg[2], (error, response) => {
  if (error) {
    console.log('Error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
