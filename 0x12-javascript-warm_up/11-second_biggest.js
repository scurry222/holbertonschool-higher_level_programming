#!/usr/bin/node
let arr = 0;
if (process.argv.length <= 3) {
  console.log(arr);
} else {
  arr = process.argv.slice(2);
  arr.sort();
  arr.reverse();
  const second = arr[1];
  console.log(second);
}
