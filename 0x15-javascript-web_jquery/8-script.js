/* eslint-env jquery */ // => (we are using jQuery)
/* Fetching a list of items from a url and appending
to a html page */

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
  data.results.forEach((item) => {
    const li = $('<li></li>');
    const title = li.text(item.title);
    $('UL#list_movies').append(title);
  });
});
