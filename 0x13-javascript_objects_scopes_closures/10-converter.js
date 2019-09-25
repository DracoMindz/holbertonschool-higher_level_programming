#!/usr/bin/node

exports.converter = function (base) {
	function mNum(num) {
		return num.toString(base);
	}
	return mNum;
};