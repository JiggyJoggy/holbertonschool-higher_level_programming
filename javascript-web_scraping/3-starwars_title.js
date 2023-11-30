#!/usr/bin/node
const request = require('request');
const args = process.argv;

request.get(`https://swapi-api.hbtn.io/api/films/${args[2]}`, function (error, response, body) {
  if (error) {
    throw error;
  }
  console.log(JSON.parse(body).title);
});
