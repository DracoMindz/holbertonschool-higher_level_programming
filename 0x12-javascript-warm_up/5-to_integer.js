#!/usr/bin/node

// convert arguemtn to integer

const parsed = parseInt(process.argv[2]);

if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parsed);
}
