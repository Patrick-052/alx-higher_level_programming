/* eslint-env jquery */ // => (we are using jQuery)
/* Fetching from api and displaying a value of variable from
the response */

$(document).ready(() => {
  $.ajax({
    url:'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'jsonp',
    success:function (response) {
        if ('hello' in response) {
            $('DIV#hello').text(response.hello);
        }
    }
  });
});
