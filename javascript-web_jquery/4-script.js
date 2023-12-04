#!/usr/bin/node
$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});

// Look up toggleClass in doc of jquery