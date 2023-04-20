#!/usr/bin/node

// a script that prints a message depending of the number of arguments passed

const numArgs = process.argv.length - 2;
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
