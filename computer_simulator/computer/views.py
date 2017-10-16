# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from computer.serializers import ComputerSerializer


@api_view(['POST'])
def computer_create(request):
    """
    Create a new computer with a stack of size 'size'.
    """
    serializer = ComputerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(ComputerSerializer(instance).data, status=status.HTTP_201_CREATED)
