#!/usr/bin/node
const request = require(Request);
const givenUrl = process.argv[2];

request(givenUrl, (err, response) => {
  if (err) throw err;
  else console.log('code: ' + response.statusCode);
});
