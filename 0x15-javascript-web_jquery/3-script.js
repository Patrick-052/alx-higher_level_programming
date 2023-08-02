/* eslint-env jquery */ // => (we are using jQuery)
/* Adding a class attribute to a html element !($) => jQuery */

$('DIV#red_header').on('click', classFunc);
function classFunc () {
  $('header').addClass('red');
}
