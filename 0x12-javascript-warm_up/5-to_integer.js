#!/usr/bin/node
// prints `My number: <first argument converted in integer>`
// if the first argument can be converted to an integer
// Otherwise print "Not a number"

const argNum = parseInt(process.argv[2], 10);

if (isNaN(argNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argNum}`);
}
