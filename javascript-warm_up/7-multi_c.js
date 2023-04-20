#!/usr/bin/node

// a script that prints x times “C is fun”

const x = process.argv[2];
const numOccurrences = parseInt(x);

if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
