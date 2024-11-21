#!/usr/bin/node
const givenUrl = process.argv[2];
const request = new Request(givenUrl, { method: 'GET' });

fetch(request)
  .then((response) => {
    console.log('code: ' + response.status);
  });
