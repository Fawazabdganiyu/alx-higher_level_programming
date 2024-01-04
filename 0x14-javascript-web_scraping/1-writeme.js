#!/usr/bin/node
// Write to a file
const fs = require('fs');
const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileName, content, 'utf8', (err) => {
  if (err) {
    return console.log(err);
  }
});
