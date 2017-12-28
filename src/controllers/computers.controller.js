'use strict';

const Computer = require('./../shared/computer');
const Stack = require('./../shared/stack');
const exec = require('child_process').exec;

Stack.create();

/**
 * Getting started new computers
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.newComputers = function(request, reply) {
    const { stack } = request.payload;

    Computer.createComputer(stack);
    Stack.add(Computer);

    return reply({
        result: `Computer created: stack ${stack}`
    });
};

/**
 * Stack pointer handler
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.stackPointer = function(request, reply) {
    const { id } = request.params;
    const { addr } = request.payload;

    const computer = Stack.getRow(id);

    computer.setPointer(addr);

    return reply({
        result: `Pointer created to: ${addr} computer ${id}`
    });
};

/**
 * Insert options operator
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.insertOptions = function(request, reply) {
    const { id } = request.params;
    const { option } = request.params;
    const { arg } = request.payload;

    if ((option === 'CALL' || option === 'PUSH') && arg === undefined) {
        return reply({
            result: 'PUSH and CALL need arg'
        });
    }

    if ((option !== 'CALL' && option !== 'PUSH') && arg !== undefined) {
        return reply({
            result: 'STOP, RET, MULT or PRINT does not need arg'
        });
    }

    const computer = Stack.getRow(id);

    computer.insertOptions(option, arg);

    const replyText = (arg) ? `${option}:${arg}` : option;

    return reply({
        result: `Insert ops added ${replyText}`
    });
};

/**
 * Execute main script
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.exec = function(request, reply) {
    const { id } = request.params;
    const computer = Stack.getRow(id);
    const results = computer.exec();

    return reply({
        result: `Exec results: ${results}`
    });
};

/**
 * Execute main script curls for ui
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.execCurls = function(request, reply) {
    const script = exec('./script.bash', (error, stdout, stderr) => {
        if (error !== null) {
            console.log(`exec error: ${error}`);
        }

        // parse result script in json
        let results = stdout.replace(/}{/g, '},{');
        results = '[' + results + ']';

        return reply(JSON.parse(results));
    });
};
