#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, _res, body) {
 if (err) {
    console.log(err);
    return;
 }

 const done = {};
 const s = JSON.parse(body);
 let i = 0;

 while (i < s.length) {
    const userId = s[i].userId;
    const fin = s[i].completed;

    if (fin && !done[userId]) {
      done[userId] = 0;
    }

    if (fin) ++done[userId];

    i++;
 }

 console.log(done);
});

