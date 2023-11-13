#!/usr/bin/node
// prints a message depending of the number of arguments passed
// - If no arguments are passed, print "No argument"
// - If only one argument is passed, print "Argumnet found"
// - Otherwise, print "Arguments found"

// Remove the execPath and the script path by
// slicing from the third element
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
