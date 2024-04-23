#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.error('Please provide a movie ID as an argument.');
    process.exit(1);
}

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.error('An error occurred:', error);
        process.exit(1);
    }

    const film = JSON.parse(body);

    console.log(`Title: ${film.title}`);
});

