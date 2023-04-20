#!/usr/bin/node

// a script finds the second biggest number

function findSecondBiggest (args) {
  const numbers = Array.from(args, Number);
  if (numbers.length <= 1) {
    return 0;
  }
  numbers.sort((a, b) => b - a);

  const secondBiggest = numbers[1];

  return secondBiggest;
}
const args = process.argv.slice(2);
const result = findSecondBiggest(args);

console.log(result);
