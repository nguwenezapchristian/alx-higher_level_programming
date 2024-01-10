#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// a class Square that defines a square and
// inherits from class Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let b = 0; b < this.width; b++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
