#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
    return this;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
