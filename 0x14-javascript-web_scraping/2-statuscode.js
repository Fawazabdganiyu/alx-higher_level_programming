#!/usr/bin/node
// Display the status code of a GET request.
const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (error) {
    console.error('error:', err);
  }
  console.log('code:', response.statusCode);
});
