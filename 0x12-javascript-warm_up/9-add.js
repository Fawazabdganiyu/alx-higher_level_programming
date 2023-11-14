#!/usr/bin/node

const [x, y] = process.argv.slice(2);

function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(x, 10), parseInt(y, 10)));
