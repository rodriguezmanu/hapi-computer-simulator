# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from computer.models import Computer, Register


class SearchLibrosTestCase(TestCase):
    client_class = APIClient

    def test_create(self):
        url = reverse('computer_create')

        self.assertEqual(Computer.objects.count(), 0)
        self.assertEqual(Register.objects.count(), 0)

        response = self.client.post(url, {'stack': 100})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(data['computer_id'], 1)

        self.assertEqual(Computer.objects.count(), 1)
        self.assertEqual(Register.objects.count(), 100)
