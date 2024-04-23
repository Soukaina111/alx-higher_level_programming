#!/usr/bin/node

// this one writes the second arg
const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

if (process.argv.length < 4) {
  console.error('Please provide a file path and a string to write as arguments.');
  process.exit(1);
}

fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error('An error occurred:', err);
  } else {
    console.log('File written successfully.');
  }
});
