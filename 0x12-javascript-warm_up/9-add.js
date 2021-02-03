#!/usr/bin/node
// Write a script that prints the addition of 2 integers

const firstNumber = Number(process.argv[2]);
const secondNumber = Number(process.argv[3]);
if (isNaN(firstNumber) || isNaN(secondNumber)) {
  console.log('NaN');
} else {
  console.log(add(firstNumber, secondNumber));
}

function add (a, b) {
  return a + b;
}
