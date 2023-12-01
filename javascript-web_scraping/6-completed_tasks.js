#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');

request.get(`${arg}`, function (error, response, body){
    if (error) {
        throw error;
    }
    const listBody = JSON.parse(body);
    const taskDone = {};

    for (const task of listBody) {
        if (task.completed) {
            const userId = task.userId;
            if (!taskDone[userId]) {
                taskDone[userId] = 1;
            } else {
                taskDone[userId]++;
            }
        }
    }
    console.log(taskDone)
})
