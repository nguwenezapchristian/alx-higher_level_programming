#!/usr/bin/node
// a script that display the status code of a GET request.

const request = require('request');

function statusCode () {
  const requestURL = process.argv[2];
  request.get(requestURL, (error, response) => {
    if (error) {
      console.log(error);
    }
    console.log(`code: ${response.statusCode}`);
  });
}
statusCode();
