'use strict';

const Hapi = require('hapi');
const Inert = require('inert');
const Vision = require('vision');
const HapiSwagger = require('hapi-swagger');
const Pack = require('./package');
const BodyParser = require('hapi-bodyparser');

const ComputersRouter = require('./src/routers/computers.router');

const server = new Hapi.Server();

server.connection({
    host: process.env.IP || 'localhost',
    port: process.env.PORT || 3000
});

server.inject({
    url: 'localhost'
});


const options = {
    info: {
        title: 'Computers Simulator API Documentation',
        version: Pack.version
    }
};

server.register(
    [
        ComputersRouter,
        Inert,
        Vision,
        {
            register: HapiSwagger,
            options: options
        }
    ],
    err => {
        if (err) {
            throw err;
        }

        server.start(err => {
            console.log(`Server running at: ${server.info.uri}`);
        });
    }
);
