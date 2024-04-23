#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const url2 = url.concat(process.argv[2]);

request(url2, function (_err, _res, body) {
  mov = JSON.parse(body);
  console.log(mov.title);
});
