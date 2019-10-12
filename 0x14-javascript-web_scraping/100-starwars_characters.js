#!/usr/bin/node
const request = require('request');
const movurl = 'https://swapi.co/api/films' + process.argv[2];
request.get(movurl, (err, response, body) => {
  if (err) throw err;
  else {
    const characters = JSON.parse(response.body).characters;
    for (let index = 0; index < characters.length; index++) {
      request.get(characters[index], (err, response, body) => {
        if (err) throw err;
        else {
          console.log(JSON.parse(response.body).name);
        }
      });
    }
  }
});
