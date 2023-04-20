#!/usr/bin/node

// a script that prints the addition of 2 integers

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

add(num1, num2);
