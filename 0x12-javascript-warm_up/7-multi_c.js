#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurence');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
