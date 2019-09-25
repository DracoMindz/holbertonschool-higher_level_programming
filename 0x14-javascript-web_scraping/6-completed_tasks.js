#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const bobj = {};
  const binfo = JSON.parse(body);
  for (const num of binfo) {
    if (num.completed === true) {
	    if (bobj[num.userId] === undefined) {
        bobj[num.userId] = 0;
	    }
	    bobj[num.userId]++;
    }
  }
  console.log(bobj);
});
