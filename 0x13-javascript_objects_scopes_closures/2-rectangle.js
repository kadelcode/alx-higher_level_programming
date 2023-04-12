#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
