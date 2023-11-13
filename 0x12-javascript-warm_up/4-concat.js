#!/usr/bin/node
// prints two arguments passed putting "is" in the middle

const [first, last] = process.argv.slice(2);
console.log(`${first} is ${last}`);
