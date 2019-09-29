#!/usr/bin/node

const list = require('./100-data.js').list;

const mpDict = list.map(function (current, index) { return (current * index); });
console.log(list);
console.log(mpDict);
