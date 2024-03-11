#!/usr/bin/node

// This Script Write a script that prints x times “C is fun” 
// Or it prints “Missing number of occurrences” in case the arg isNan
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
