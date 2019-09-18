#!/usr/bin/node

// factorial

function factorial (m) {
  if (isNaN(m) || m < 0 || m === 1) {
    return 1;
  }
  return (m * factorial(m - 1));
}

console.log(factorial(Number(process.argv[2])));
