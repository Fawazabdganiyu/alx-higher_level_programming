#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((result, item) => {
  const [usrId, occur] = item;
  if (!result[occur]) {
    result[occur] = [];
  }

  result[occur].push(usrId);

  return result;
}, {});

console.log(newDict);
