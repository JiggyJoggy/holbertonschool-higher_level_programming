#!/usr/bin/node
const argInt = parseInt(process.argv[2]);
if (Number(argInt)) {
  for (let index = 0; index < argInt; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
