#!/usr/bin/node
/* Retrieving information from an API using an id =>[2] */

const request = require('request');
const arg = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[2];

request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error.message);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
