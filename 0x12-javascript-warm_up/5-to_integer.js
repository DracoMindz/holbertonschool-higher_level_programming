#!/usr/bin/node

const p = parseInt(process.argv[2]);

if (isNaN(p)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + p);
}
