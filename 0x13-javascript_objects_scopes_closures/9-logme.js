#!/usr/bin/node
// This script for task 9

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
