#!/usr/bin/node
const args = process.argv;
const request = require('request');

request(`${args[2]}`, (response) => {
    console.log('code: ', response.statusCode);
})
