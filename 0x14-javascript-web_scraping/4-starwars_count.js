#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const filmsData = JSON.parse(body).results;
    const filmsWithWedge = filmsData.filter((film) => {
      return film.characters.some((characterUrl) =>
        characterUrl.endsWith('18/'));
    });
    console.log(filmsWithWedge.length);
  }
});
