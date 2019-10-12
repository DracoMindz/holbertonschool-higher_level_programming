#!/usr/bin/node
const request = require('request');
let movieUrl = 'https://swapi.co/api/films' + process.argv[2];

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(response.body).characters;
    for (let index = 0; index < characters.length; index++) {
      request.get(characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(response.body).name);
        }
      });
    }
  }
});
