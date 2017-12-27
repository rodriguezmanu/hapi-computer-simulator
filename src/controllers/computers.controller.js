'use strict';

const Computer = require('./../shared/computer');
const Stack = require('./../shared/stack');

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
        result: 'Computer created'
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
        result: 'Pointer created'
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

    return reply({
        result: 'Insert ops added'
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

    console.log(computer);
    const results = computer.exec();
    console.log(results);

    return reply({
        result: `Exec results: ${results}`
    });
};
