const Joi = require('Joi');

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
                        .positive()
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
