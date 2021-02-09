#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(
  {
    url: url,
    json: true
  },
  (error, response, body) => {
    if (error) {
      console.log(error);
    }
    if (response.statusCode === 200) {
      console.log(body.title);
    }
  }
);
