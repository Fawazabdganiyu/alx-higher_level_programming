#!/usr/bin/node

const argNum = process.argv.slice(2).map(Number);

if (argNum.length <= 1) {
  console.log(0);
} else {
  const sortedNum = argNum.sort((a, b) => b - a);
  console.log(sortedNum[1]);
}
