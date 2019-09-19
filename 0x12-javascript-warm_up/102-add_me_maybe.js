#!/usr/bin/node

exports.callMeMaybe = function (number, theFunction) {
  return theFunction(number++);
};
