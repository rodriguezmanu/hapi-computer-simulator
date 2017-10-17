# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from computer.models import Computer
from computer.serializers import ComputerSerializer, PointerSerializer, InsertSerializer


@api_view(['POST'])
def computer_create(request):
    """
    Create a new computer with a stack of size 'size'.
    """
    serializer = ComputerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(ComputerSerializer(instance).data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def set_pointer(request, computer_id):
    """
    Set pointers to the give address.
    """
    computer = get_object_or_404(Computer, id=computer_id)
    serializer = PointerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        address = serializer.validated_data['addr']
        computer.stack_pointer = address
        computer.program_counter = address
        computer.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def insert(request, computer_id, operation):
    """
    Insert operation and (if available) argument.
    """
    computer = get_object_or_404(Computer, id=computer_id)
    serializer = InsertSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        if operation == 'CALL':
            argument = serializer.validated_data['addr']
        elif operation == 'PUSH':
            argument = serializer.validated_data['arg']
        elif operation in ['MULT', 'RET', 'STOP', 'PRINT']:
            argument = None
        else:
            raise ValidationError('Invalid operation')

        register = computer.register_set.get(address=computer.stack_pointer)
        register.value1 = operation
        register.value2 = argument
        register.save()
        computer.stack_pointer += 1
        computer.save()

        return Response(status=status.HTTP_200_OK)
