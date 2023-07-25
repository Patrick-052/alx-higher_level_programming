#!/usr/bin/node
/* Retrieving data on a specific condition
from an API =>arg[2] */

const request = require('request');
const arg = process.argv;

let counter = 0;
const characterId = '18';
request(arg[2], (error, response, body) => {
  if (error) {
    console.log('Error:', error.message);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          counter += 1;
        }
      });
    });
    console.log(counter);
  }
});
