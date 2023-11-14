#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  // Iterate the list from last element then push to the `reversesList`
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
