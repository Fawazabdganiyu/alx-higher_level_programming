#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const films = JSON.parse(body).results;
      let count = 0;
      for (const film of films) {
	for (const character of film.characters) {
	  if (character === wedgeAntillesUrl) {
	    count++;
	  }
	}
      }
      console.log(count);
    } catch (err) {
      console.error(err);
    }
  }
});
