#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(
  {
    url: url
  },
  (err, response, body) => {
    if (err) {
      console.log(err);
    }
    if (response.statusCode === 200) {
      fs.writeFile(process.argv[3], body, 'utf8', err => {
        if (err) {
          console.log('error write the file');
        }
      });
    }
  }
);
