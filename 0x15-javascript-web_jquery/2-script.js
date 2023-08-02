/* eslint-env jquery */ // => (we are using jQuery)
/* Adding an event listener/handler that changes
   the color !($) => jQuery */

$('DIV#red_header').on('click', colorFunc);
function colorFunc () {
  $('DIV#red_header').css('color', '#FF0000');
}
