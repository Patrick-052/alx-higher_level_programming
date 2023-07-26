#!/usr/bin/node
/* Printing all characters of a movie using the filmId =>[2]
from an API url */

const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) console.log(error);
        const char = JSON.parse(body);
        console.log(char.name);
      });
    });
  }
});
