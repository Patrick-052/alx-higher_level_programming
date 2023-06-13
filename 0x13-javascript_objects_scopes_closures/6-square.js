#!/usr/bin/node
const Square = require('./5-square');

class Square1 extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    this.print(c);
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += c;
      }
      console.log(rec);
    }
  }
}

module.exports = Square1;
