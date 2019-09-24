#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  contructor (size) {
    super(size, size);
	}

	charPrint(c) {
		if (c === undefined) {
			this.print();
		} else {
			for (let m = 0; m < this.height; m++) {
				console.log(c.repeat(this.height));
			}
	 }
	

}
module.exports = Square;