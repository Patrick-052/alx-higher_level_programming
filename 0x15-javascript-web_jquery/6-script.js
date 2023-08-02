/* eslint-env jquery */ // => (we are using jQuery)
/* Manipulating DOM by changing/setting text */

$('DIV#update_header').on('click', updateText);
function updateText () {
  $('header').text('New Header!!!');
}
