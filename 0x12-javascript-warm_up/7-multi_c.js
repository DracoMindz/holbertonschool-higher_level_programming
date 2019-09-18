#!/usr/bin/node

// print multiple times
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
