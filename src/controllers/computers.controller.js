/**
 * Getting started new computers
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.newComputers = function(request, reply) {
    const { stack } = request.payload;

    return reply(stack);
};

/**
 * Stack pointer handler
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.stackPointer = function(request, reply) {
    const { id } = request.params;
    const { addr } = request.payload;

    return reply({ id, addr });
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

    return reply({ id, option, arg });
};

/**
 * Execute main script
 * @param {Object} request
 * @param {Object} reply
 */
module.exports.exec = function(request, reply) {
    const { id } = request.params;

    return reply(id);
};
