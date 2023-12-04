#!/usr/bin/node
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json').then((data) => {
    const charName = data.name;
    $('DIV#character').append(charName);
  });
});
