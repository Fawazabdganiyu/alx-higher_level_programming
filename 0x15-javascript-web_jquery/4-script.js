#!/usr/bin/node
$('DIV#toggle_header').click(() => {
  $('HEADER').toggleClass('red green');
});
