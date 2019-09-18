#!/usr/bin/node

// convert arguement to integer

const p = parseInt(process.argv[2]);

if (isNaN(p)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + p);
}
