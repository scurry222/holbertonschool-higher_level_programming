#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[3], process.argv[2], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
