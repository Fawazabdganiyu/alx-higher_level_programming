#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const filmsData = JSON.parse(body).results;
      const filmsWithWedge = filmsData.filter((film) => {
	return film.characters.includes(wedgeAntillesUrl);
      });
      console.log(filmsWithWedge.length)
    } catch (err) {
      console.error(err);
    }
  }
});
