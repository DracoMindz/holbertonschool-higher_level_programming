#!/usr/bin/node

// find the second largest number

const secondMax = function (myArray) {
  if (myArray.length === 0 || myArray.length === 1) {
    return 0;
  }
  let max = Math.max.apply(null, myArray);
  max = max.toString();
  const maxi = myArray.indexOf(max); // largest number
  myArray[maxi] = -Infinity;
  const secondMax = Math.max.apply(null, myArray); // second max
  myArray[maxi] = max;
  return secondMax;
};
console.log(secondMax(process.argv.slice(2)));
