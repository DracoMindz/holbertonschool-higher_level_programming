#!/usr/bin/node
const mSquare = require('./5-square')
class Square extends mSquare{
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