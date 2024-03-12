#!/usr/bin/node
// this script defines a subclass square of Rectnagle class

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
};
