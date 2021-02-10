#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(
  {
    url: url,
    json: true
  },
  (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      if (response.statusCode === 200) {
        const store = {};
        body.forEach(element => {
          const { userId, completed } = element;
          if (completed) {
            if (store[userId]) {
              store[userId]++;
            } else {
              store[userId] = 1;
            }
          }
        });
        console.log(store);
      }
    }
  }
);
