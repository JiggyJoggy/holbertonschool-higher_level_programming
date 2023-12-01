#!/usr/bin/node
const request = require('request');
const arg = process.argv;

request.get(`${arg[2]}`, function (error, response, body) {
  if (error) {
    throw error;
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film in films) {
    const char = films[film].characters;
    for (const person in char) {
      if (char[person].match(/.\/18\//g)) {
				count++;
      }
    }
  }
  console.log(count);
});
