#!/usr/bin/node
$(document).ready(function () {
  const $listMovies = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (index, movie) {
        $listMovies.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
