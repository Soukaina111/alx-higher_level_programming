#!/usr/bin/node

// this one writes the second arg

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error('An error occurred:', err);
  } else {
    console.log('File written successfully.');
  }
});
