#!/usr/bin/node

// create square
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
}

for (let i = 0; i < x; i++) {
  for (let j = 0; j < x; j++) {
    console.log('X');
  }
  console.logln('');
}
