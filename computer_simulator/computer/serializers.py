# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from computer.models import Computer, Register


class ComputerSerializer(serializers.Serializer):

    computer_id = serializers.IntegerField(read_only=True, source='id')
    stack = serializers.IntegerField(write_only=True)

    def save(self):
        size = self.validated_data['stack']
        return Computer.create(size)