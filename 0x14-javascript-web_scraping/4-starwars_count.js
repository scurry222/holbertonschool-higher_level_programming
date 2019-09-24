#!/usr/bin/node
const request = require('request');
request.get('http://swapi.co/api/films/', function (err, res, body) {
  let count = 0;
  if (res.statusCode === 200) {
    const films = (JSON.parse(body).results);
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  } else if (err) {
    console.log(err);
  }
});
