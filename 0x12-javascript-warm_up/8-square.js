#!/usr/bin/node

// This script prints a square based on the arg

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const len = parseInt(process.argv[2]);
  for (let i = 0; i < len; i++) {
    let sd = '';
    for (let j = 0; j < len; j++) {
      sd += 'X';
    }
    console.log(sd);
  }
}
