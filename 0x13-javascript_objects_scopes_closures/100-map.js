#!/usr/bin/node

const dict = require('./100-data.js').dict;

const mpDict = dict.map(function (current, index) { return (current * index); });
console.log(dict);
console.log(mpDict);
