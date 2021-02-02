#!/usr/bin/node
// script that prints a message depending of the number o= arguments passed
const ArgsPassed = process.argv.length;
if (ArgsPassed === 2) {
  console.log('No argument');
} else if (ArgsPassed === 3)  {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
