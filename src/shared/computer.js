'use strict'

/**
 * Create a new computer
 *
 * @param {Number} addr
 */
module.exports.createComputer = function(addr) {
    this.stack = new Array(addr);
    this.resultPrint = [];
};

/**
 * Set pointer
 *
 * @param {number} pointer
 */
module.exports.setPointer = function(pointer) {
    this.pointer = pointer;
};

/**
 * Insert option into stack
 *
 * @param {String} option
 * @param {Number} arg
 */
module.exports.insertOptions = function(option, arg) {
    this.stack[this.pointer] = (arg) ? `${option}:${arg}` : option;

    this.pointer++;
};

/**
 * Execute all options
 */
module.exports.exec = function() {
    let result = [];

    for (let index = 0; index < this.stack.length; index++) {
        const element = this.stack[index];

        if (element === undefined) {
            break;
        }

        const option = element.split(':');

        if (option[0] === 'MULT') {
            const mult = result.pop() * result.pop();

            result.push(mult);
        } else if (option[0] === 'CALL') {
            index = option[1] - 1;
        } else if (option[0] === 'RET') {
            index = result.pop();
        } else if (option[0] === 'STOP') {
            return this.resultPrint;
        } else if (option[0] === 'PRINT') {
            this.resultPrint.push(result.pop());
        } else if (option[0] === 'PUSH') {
            result.push(option[1]);
        }
    }
    return this.resultPrint;
}
