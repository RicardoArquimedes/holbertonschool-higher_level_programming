#!/usr/bin/node
// Write a script that prints x times “C is fun”

const argPass = process.argv[2];
if (isNaN(argPass, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(argPass); i++) {
    console.log('C is fun');
  }
}
