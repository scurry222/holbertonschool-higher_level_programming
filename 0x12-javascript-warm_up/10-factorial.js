#!/usr/bin/node

let fact = 1;
if (process.argv[2] === undefined) {
  console.log(fact);
} else {
  for (let x = Number(process.argv[2]); x !== 0; x--) {
    fact = fact * x;
  }
  console.log(fact);
}
