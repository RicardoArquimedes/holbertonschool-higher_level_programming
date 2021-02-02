#!/usr/bin/node
// script that prints a message depending of the number o= arguments passed
const args_passed = process.argv.length;
if (args_passed === 2) {
  console.log('No argument');
} else if (args_passed === 3)  {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
