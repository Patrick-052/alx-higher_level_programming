/* eslint-env jquery */ // => (we are using jQuery)
/* adding list items to an unorded list element !($) => jQuery */

$('DIV#add_item').on('click', listAddition);
function listAddition () {
  $('UL.my_list').append('<li>Item</li>');
}
