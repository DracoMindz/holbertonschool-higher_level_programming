#!/usr/bin/node

const dict = require('./101-data.js').dict;
const uDict = {};

for (const m in dict) {
  if (uDict[dict[m]] === undefined) {
    uDict[dict[m]] = [];
  }
  uDict[dict[m]].push(m);
}
console.log(uDict);
