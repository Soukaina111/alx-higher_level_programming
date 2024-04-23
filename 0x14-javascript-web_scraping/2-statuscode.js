#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.error('Please provide a URL as an argument.');
    process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response, body) => {
    if (error) {
        console.error('An error occurred:', error);
        process.exit(1);
    }
   console.log(`code: ${response.statusCode}`);
});

