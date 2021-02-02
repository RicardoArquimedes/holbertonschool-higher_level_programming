#!/usr/bin/node
// script that prints a message depending of the number o= arguments passed
const args_passed = process.argv.length;
if (args_passed === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
