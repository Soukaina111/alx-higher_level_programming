#!/usr/bin/node

// This script adds a print method to the previous code

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
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
}
module.exports = Rectangle;
