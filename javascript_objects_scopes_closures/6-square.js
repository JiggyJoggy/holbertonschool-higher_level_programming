#!/usr/bin/node
const SquareV2 = require('./5-square');

module.exports = class Square extends SquareV2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.width; row++) {
      for (let col = 0; col < this.height; col++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
