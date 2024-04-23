#!/usr/bin/node

const request = require('request');

const starWarsUri = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(starWarsUri, (error, response, body) => {
    if (error) {
        console.error('An error occurred:', error);
        process.exit(1);
    }

    const film = JSON.parse(body);

    console.log(`Title: ${film.title}`);
});

