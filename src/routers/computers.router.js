'use strict';

const Computers = require('./../controllers/computers.controller')
const validation = require('./../shared/schemaValidation');

exports.register = function(server, options, next) {
    server.route({
        method: 'POST',
        path: '/computers',
        config: {
            validate: {
                payload: {
                    stack: validation.schema.stack
                }
            },
            handler: Computers.newComputers,
            description: 'Create a new stack of Computers',
            tags: ['api', 'computers']
        }
    });

    server.route({
        method: 'PATCH',
        path: '/computers/{id}/stack/pointer',
        config: {
            validate: {
                params: {
                    id: validation.schema.lengthRequired
                },
                payload: {
                    addr: validation.schema.lengthRequired
                }
            },
            handler: Computers.stackPointer,
            description: 'Stack pointer to:',
            tags: ['api', 'computers']
        }
    });

    server.route({
        method: 'POST',
        path: '/computers/{id}/stack/insert/{option}',
        config: {
            validate: {
                params: {
                    id: validation.schema.lengthRequired,
                    option: validation.schema.options
                },
                payload: {
                    arg: validation.schema.lengthOptional
                }
            },
            handler: Computers.insertOptions,
            description: 'Adding a operation',
            tags: ['api', 'computers']
        }
    });

    server.route({
        method: 'POST',
        path: '/computers/{id}/exec',
        config: {
            validate: {
                params: {
                    id: validation.schema.lengthRequired
                }
            },
            handler: Computers.exec,
            description: 'Execute all stack script',
            tags: ['api', 'computers']
        }
    });

    return next();
};

exports.register.attributes = {
    name: 'routes-index'
};
