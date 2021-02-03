#!/usr/bin/node
const argPass = process.argv[2];
if (isNaN(Number(argPass))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argPass); i++) {
    let y = '';
    for (let j = 0; j < Number(argPass); j++) {
      y += 'X';
    }
    console.log(y);
  }
}
