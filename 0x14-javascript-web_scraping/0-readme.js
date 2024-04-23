#!/usr/bin/node

// this js script to read content of a file 

const fs = require('fs');
const filePath = process.argv[2];

if (process.argv.length < 3) {
    console.error('Please provide a file path as an argument.');
    process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
	    console.error('An error occurred:', err);
    } else {
	    console.log(data);
    }
});
