/* a JavaScript script that fetches and lists the title for all movies
by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movies in data.results) {
    $('ul#list_movies').append('<li>' + data.results[movies].title + '</li>');
  }
});
