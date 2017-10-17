# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Computer(models.Model):

    stack_pointer = models.IntegerField(default=0)
    program_counter = models.IntegerField(default=0)
    computation_ended = models.BooleanField(default=False)

    @staticmethod
    def create(size):
        computer = Computer.objects.create()
        for x in range(size):
            Register.objects.create(address=x, computer=computer)
        return computer

    def insert(self, value, param=None):
        register = self.register_set.get(address=self.stack_pointer)
        register.value1 = value
        register.value2 = param
        register.save()
        self.stack_pointer += 1

    def pop(self):
        self.stack_pointer -= 1
        return self.register_set.get(address=self.stack_pointer)

    def _set_stack_pointer(self):
        """
        Before execute, we set the stack pointer to the top of the stack
        """
        last_value_pos = 0
        for r in self.register_set.order_by('address'):
            if r.value1:
                last_value_pos = r.address
        self.stack_pointer = last_value_pos + 1

    def execute(self):
        self._set_stack_pointer()
        print_buffer = []
        while not self.computation_ended:
            register = self.register_set.get(address=self.program_counter)
            instruction, param = register.value1, register.value2
            self.program_counter += 1
            output = self._process(instruction, param)
            if output:
                print_buffer.append(output)
        return print_buffer

    def _process(self, ins, param):
        if ins == 'MULT':
            a = self.pop().value1
            b = self.pop().value1
            self.insert(int(a) * int(b))
        elif ins == 'CALL':
            self.program_counter = param
        elif ins == 'RET':
            self.program_counter = int(self.pop().value1)
        elif ins == 'STOP':
            self.computation_ended = True
        elif ins == 'PRINT':
            return self.pop().value1
        elif ins == 'PUSH':
            self.insert(param)


class Register(models.Model):

    address = models.IntegerField()
    value1 = models.CharField(max_length=50, null=True)
    value2 = models.IntegerField(null=True)
    computer = models.ForeignKey(Computer)
