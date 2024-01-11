#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    });
    console.log(completedTasksByUser);
  }
});
