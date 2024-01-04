#!/usr/bin/node
// Read the content of a file and print it content
const fs = require('fs');
const fileName = process.argv[2];
fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
