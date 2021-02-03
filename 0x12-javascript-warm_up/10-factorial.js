#!/usr/bin/node
// Write a script that computes and prints a factorial

const argPass = Number(process.argv[2]);
if (isNaN(argPass)) {
  console.log(1);
} else {
  console.log(factorial(argPass));
}
function factorial (number) {
  if (number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
