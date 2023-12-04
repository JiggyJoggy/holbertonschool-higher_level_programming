#!/usr/bin/node
$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (data) => {
      $('DIV#hello').text(data.hello);
    }
  });
});
