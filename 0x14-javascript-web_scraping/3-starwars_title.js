#!/usr/bin/node
const request = require('request');
const swurl = 'http://swapi.co/api/films/' + process.argv[2];
request(swurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
