# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from computer.models import Computer
from computer.serializers import ComputerSerializer, PointerSerializer


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
