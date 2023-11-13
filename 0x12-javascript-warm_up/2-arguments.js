#!/usr/bin/node
// prints a message depending of the number of arguments passed
// - If no arguments are passed, print "No argument"
// - If only one argument is passed, print "Argumnet found"
// - Otherwise, print "Arguments found"

const { argv } = require('node:process');
// Deduct the execPath and the script path (-2)
switch (argv.length - 2) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
