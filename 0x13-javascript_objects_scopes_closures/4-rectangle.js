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
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
    return this;
  }

  double () {
    const wid = this.width * 2;
    const hit = this.height * 2;
    return [wid, hit];
  }
}

module.exports = Rectangle;
