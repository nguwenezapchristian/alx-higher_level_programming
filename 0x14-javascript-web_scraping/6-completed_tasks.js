#!/usr/bin/node
// a script that computes the number of tasks completed by user id
const request = require('request');

async function tasksCompleted() {
    const requestURL = process.argv[2];
    await new Promise((resolve, reject) => {
        request.get(requestURL, (error, response, body) => {
            if (error) {
                console.log(error);
                reject(error);
            }
            if (response.statusCode !== 200) {
                console.log(response.statusCode);
                reject(response.statusCode);
            }
            const todos = JSON.parse(body);
            let todosDone = {};
            for (let id = 1; id <= 10; id++) {
                let taskDone = 0;
                for (let index = 0; index < todos.length; index++) {
                    const user = todos[index];
                    if (user.userId === id && user.completed) {
                        taskDone += 1;
                    }
                }
                todosDone[id] = taskDone;
                
                // console.log(`${id}: ${taskDone}`);
                taskDone = 0; 
            }
            console.log(todosDone);
            resolve();
        });
    });
}
tasksCompleted();