#!/usr/bin/node
// Print a Star Wars movie title where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
