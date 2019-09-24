#!/usr/bin/node
class Square extends require('./5-square.js') {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let m = 0; m < this.height; m++) {
			 console.log(c.repeat(this.width));
			}
	 }
}
module.exports = Square;