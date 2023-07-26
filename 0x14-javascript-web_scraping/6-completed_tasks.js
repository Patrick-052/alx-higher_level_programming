#!/usr/bin/node
/* Retrieving data from an API url =>arg[2] and
computeting tasks completed by userid */

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  const userCounts = {};

  data.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      userCounts[userId] = (userCounts[userId] || 0) + 1;
    }
  });
  console.log(userCounts);
});
