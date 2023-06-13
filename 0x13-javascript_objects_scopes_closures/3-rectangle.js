#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { str += 'X'; }
      str += '\n';
    }
    return str;
  }
}

module.exports = Rectangle;
