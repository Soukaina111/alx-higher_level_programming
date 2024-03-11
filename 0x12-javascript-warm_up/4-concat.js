#!/usr/bin/node
// This script displays the standard inputin the givven format

if (process.argv.length > 3) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv.length === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
