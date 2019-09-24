#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        for (let m = 0; < this.height; m++) {
            console.log('X'.repeat(this.width));
        }
    }

    double() {
        this.width *= 2;
        this.height *= 2;
    }
}
module.exports = Rectangle;