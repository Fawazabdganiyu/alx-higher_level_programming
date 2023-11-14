#!/usr/bin/node

const num = parseInt(process.argv[2]);

const factorial = num =>
  isNaN(num) || (num === 1)
    ? 1
    : num * factorial(num - 1);

console.log(factorial(num));
