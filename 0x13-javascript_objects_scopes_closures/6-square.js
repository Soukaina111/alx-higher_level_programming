#!/usr/bin/node
// This script add a chart function to the previous code 

class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let ro = '';
      for (let j = 0; j < this.width; j++) {
        ro += c;
      }
      console.log(ro);
    }
  }
}

module.exports = Square;
