#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const request = require('request');

request.get(`${args[2]}`, function (error, response, body) {
  if (error) {
    throw error;
  }
  fs.writeFile(`${args[3]}`, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
