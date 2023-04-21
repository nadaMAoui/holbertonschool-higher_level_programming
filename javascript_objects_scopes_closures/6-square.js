#!/usr/bin/node

//  a class Square that defines a square and inherits from Square of 5-square.js

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let count = 0; count < this.height; count++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
