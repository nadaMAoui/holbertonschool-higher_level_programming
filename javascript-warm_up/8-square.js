#!/usr/bin/node

// a script that prints a square

const size = process.argv[2];
const squareSize = parseInt(size);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  if (squareSize <= 0) {
    console.log('Invalid size');
  } else {
    for (let i = 0; i < squareSize; i++) {
      console.log('X'.repeat(squareSize));
    }
  }
}
