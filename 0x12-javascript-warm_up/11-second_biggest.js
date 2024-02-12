#!/usr/bin/node
const args = process.argv;
let i = 2;
let res = 0;
let maxIndex = 0;
let temp = 0;
const list = [];
const len = args.length;

for (i = 2; i < len; i++) {
  list.push(parseInt(args[i]));
}
for (i = 2; i < len; i++) {
  if (parseInt(args[i]) > parseInt(temp)) {
    temp = parseInt(args[i]);
    maxIndex = i;
  }
}

temp = 0;
i = 2;

if (!args[2] || !args[3]) console.log(0);
else {
  while (i < len) {
    if (args[i] < args[maxIndex] && args[i] > temp && i !== maxIndex) {
      temp = args[i];
      res = args[i];
    }
    i++;
  }
  console.log(res);
}
