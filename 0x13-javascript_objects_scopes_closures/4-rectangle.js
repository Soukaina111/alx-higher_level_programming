#!/usr/bin/node
// This script adds a rotate and double method to the previous code

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.height = h;
      this.width = w;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let ro = "";
      for (let j = 0; j < this.width; j++) {
        ro += "X";
      }
      console.log(ro);
    }
  }

  rotate() {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
