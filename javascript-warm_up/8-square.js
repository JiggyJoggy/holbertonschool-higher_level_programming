#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number(size)) {
  for (let row = 0; row < size; row++) {
    for (let col = 0; col < size; col++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
