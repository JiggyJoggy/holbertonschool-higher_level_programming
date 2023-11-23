#!/usr/bin/node
let args = process.argv;
if (args.length < 4) {
  console.log('0');
} else {
  args = args.sort((a, b) => a - b).reverse();
  console.log(args[1]);
}
