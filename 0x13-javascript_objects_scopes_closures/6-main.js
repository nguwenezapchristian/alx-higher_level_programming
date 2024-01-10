#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
console.log('Before first charPrint');
s1.charPrint();
console.log('After first charPrint');
s1.charPrint('C');
