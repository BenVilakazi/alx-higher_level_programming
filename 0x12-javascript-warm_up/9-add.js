#!/usr/bin/node

const first = process.argv[2];
const second = process.argv[3];
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(first, second);
