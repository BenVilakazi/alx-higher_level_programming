#!/usr/bin/node

const args = parseInt(process.argv[2]);
let square = '';
let width = 0;
if (isNaN(args)) console.log('Missing size');
else {
  for (let height = 0; height < args; height++) {
    while (width < args) {
      square += 'X';
      width++;
    }
    console.log(square);
  }
}
