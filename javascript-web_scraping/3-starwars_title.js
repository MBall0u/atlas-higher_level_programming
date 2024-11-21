#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + arg, (err, response, body) => {
  if (err) throw err;
  else {
    console.log(JSON.parse(body).title);
  }
});
