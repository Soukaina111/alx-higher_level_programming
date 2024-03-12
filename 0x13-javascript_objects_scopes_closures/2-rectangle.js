#!/usr/bin/node
//This script defines the rectangle class wth condition in constructor

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
