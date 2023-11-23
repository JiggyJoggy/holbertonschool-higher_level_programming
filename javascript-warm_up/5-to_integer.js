#!/usr/bin/node
const argInt = parseInt(process.argv[2]);
if (Number(argInt)) {
  console.log(`My number: ${argInt}`);
} else {
  console.log('Not a number');
}
