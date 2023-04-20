#!/usr/bin/node

// a script that computes and prints a factorial

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
const input = isNaN(num) ? 1 : num;

const result = factorial(input);

console.log(result);
