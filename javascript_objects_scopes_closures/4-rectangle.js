#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    this.temp = this.width;
    this.width = this.height;
    this.height = this.temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
