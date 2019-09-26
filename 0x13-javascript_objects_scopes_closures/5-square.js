#!/usr/bin/node
const mSquare = require('4-rectangle.js:');
module.exports = class Square extends mSquare {
  constructor (size) {
    super(size, size);
  }
};
