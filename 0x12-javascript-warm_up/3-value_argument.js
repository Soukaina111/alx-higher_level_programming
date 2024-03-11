#!/usr/bin/node
// This Script displays the value of arg of the standard input

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
