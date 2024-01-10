#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// a class Square that defines a square and
// inherits from class Rectangle
class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.height));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
