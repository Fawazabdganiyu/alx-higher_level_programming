#!/usr/bin/node
// prints the first argument passed
// - If no arguments are passed to the script, print "No argument"

// Get the command-line arguments
const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
