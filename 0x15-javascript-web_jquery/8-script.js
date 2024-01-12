#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
  $.each(data.results, (index, movie) => {
    $('UL#list_movies').append('<LI>' + movie.title + '</LI>');
  });
});
