'use strict';

/**
 * Create row stack
 */
module.exports.create = function() {
    this.row = [];
};

/**
 * Add computer to stack
 *
 * @param {Object} computer
 */
module.exports.add = function(computer) {
    const nextIndex = this.row.length + 1;

    this.row[nextIndex] = computer;
};

/**
 * Get row
 *
 * @param {Number} id
 */
module.exports.getRow = function(id) {
    return this.row[id];
};
