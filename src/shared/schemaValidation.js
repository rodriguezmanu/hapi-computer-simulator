'use strict';

const Joi = require('joi');

const options = ['MULT', 'CALL', 'RET', 'STOP', 'PRINT', 'PUSH'];

module.exports.schema = {
    stack: Joi
                .number()
                .min(1)
                .positive()
                .integer()
                .required(),
    lengthRequired: Joi
                        .number()
                        .min(0)
                        .integer()
                        .required(),
    lengthOptional: Joi
                        .number()
                        .min(0)
                        .positive()
                        .integer(),

    options: Joi
                .valid(options)
}
