#!/usr/bin/node
// This script shows the second biggest integer in the givven list

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  let max = parseInt(args[0]);
  let secondMax = parseInt(args[1]);

  if (secondMax > max) {
    [max, secondMax] = [secondMax, max];
  }

  for (let i = 2; i < args.length; i++) {
    const num1 = parseInt(args[i]);

    if (num1 > max) {
      secondMax = max;
      max = num1;
    } else if (num1 > secondMax && num1 < max) {
      secondMax = num1;
    }
  }

  console.log(secondMax);
}
