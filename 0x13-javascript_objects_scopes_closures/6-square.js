#!/usr/bin/node
const mSquare = require('./5-square');
module.exports = class Square extends mSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
