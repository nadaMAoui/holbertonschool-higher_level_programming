#!/usr/bin/node

// a class Square that defines a square and inherits from Rectangle of 4-rectangle.js

class Square extends require('./4-rectangle') {
    constructor (length) {
      super(length, length);
    }
  }
  module.exports = Square;
