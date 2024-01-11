#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, { json: true }, (err, response, body) => {
  if (!err) {
    body.characters.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (err, response, body) => {
        if (!err) { console.log(body.name); }
      });
    });
  }
});
