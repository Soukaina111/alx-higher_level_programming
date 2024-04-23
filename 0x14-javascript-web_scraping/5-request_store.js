#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];

request(f1, function (_err, _res, body) {
  fs.writeFile(f2, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
