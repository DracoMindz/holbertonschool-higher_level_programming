#!/usr/bin/node
const Square = require('./5-square.js');
class Square extends Rectangle {
  contructor (size) {
    super(size, size);
	}

	charPrint(c) {
		if (c === undefined) {
			this.print();
		} else {
			for (let m = 0; m < this.height; m++) {
				console.log(c.repeat(this.width));
			}
	 }
	

}
module.exports = Square;