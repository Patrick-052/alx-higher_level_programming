/* eslint-env jquery */ // => (we are using jQuery)
/* Swithing the value of a class attribute of an element !($) => jQuery */

$('DIV#toggle_header').on('click', toggle);
function toggle () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').addClass('green');
  }
}
