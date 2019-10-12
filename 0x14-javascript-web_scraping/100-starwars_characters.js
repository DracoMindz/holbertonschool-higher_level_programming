#!/usr/bin/node
const request = require('request');
const movurl = 'http://swapi.co/api/films' + process.argv[2];
request.get(movurl, (err, response, body) => {
  if (err) throw err;
  else {
    const char = JSON.parse(body);
    for (const index of char.characters) {
      request(index, function (err, response, body) {
        if (err) throw err;
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
