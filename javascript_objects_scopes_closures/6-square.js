#!/usr/bin/node
const squareV1 = require('./5-square.js');

class Square extends squareV1 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
