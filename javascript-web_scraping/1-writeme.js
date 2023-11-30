#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

const filename = args[2];
const data = args[3];

fs.writeFile(filename, data, 'utf-8', (err) => {
  if (err) throw err;
});
