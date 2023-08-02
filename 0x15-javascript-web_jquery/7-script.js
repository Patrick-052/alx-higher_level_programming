/* eslint-env jquery */ // => (we are using jQuery)
/* Fething content from a url */

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, (response) => {
  if ('name' in response) {
    $('DIV#character').text(response.name);
  }
});
