#!/usr/bin/node
// This function prints the addition of 2 integers

function add(a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  return num1 + num2;
}
console.log(add(process.argv[2], process.argv[3]));
