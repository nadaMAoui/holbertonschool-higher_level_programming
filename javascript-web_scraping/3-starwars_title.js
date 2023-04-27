#!/usr/bin/node

// a script that prints the title of a Star Wars
// movie where the episode number matches a given integer

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request(url + process.argv[2], function (error, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
