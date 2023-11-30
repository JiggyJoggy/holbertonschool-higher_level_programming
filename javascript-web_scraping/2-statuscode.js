#!/usr/bin/node
const args = process.argv;
const request = require('request');

request.get(`${args[2]}`, function(error, response, body) {
    console.log('code: ', response.statusCode);
})
