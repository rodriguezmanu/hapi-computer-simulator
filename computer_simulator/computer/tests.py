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

    def test_set_pointer(self):
        computer = Computer.create(100)
        url = reverse('set_pointer', kwargs={'computer_id': computer.id})
        response = self.client.patch(url, {'addr': 50})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        computer.refresh_from_db()
        self.assertEqual(computer.stack_pointer, 50)
        self.assertEqual(computer.program_counter, 50)

    def test_set_pointer_invalid_computer(self):
        url = reverse('set_pointer', kwargs={'computer_id': 1})
        response = self.client.patch(url, {'addr': 50})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_insert(self):
        computer = Computer.create(100)
        computer.stack_pointer = computer.program_counter = 50
        computer.save()

        # insert MULT
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'MULT'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        computer.refresh_from_db()
        register = computer.register_set.get(address=50)
        self.assertEqual(register.value1, 'MULT')
        self.assertIsNone(register.value2)
        self.assertEqual(computer.stack_pointer, 51)

        # insert PRINT
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'PRINT'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        computer.refresh_from_db()
        register = computer.register_set.get(address=51)
        self.assertEqual(register.value1, 'PRINT')
        self.assertIsNone(register.value2)
        self.assertEqual(computer.stack_pointer, 52)

        # insert RET
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'RET'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        computer.refresh_from_db()
        register = computer.register_set.get(address=52)
        self.assertEqual(register.value1, 'RET')
        self.assertIsNone(register.value2)
        self.assertEqual(computer.stack_pointer, 53)

    def test_insert_push(self):
        computer = Computer.create(100)
        computer.save()

        # insert PUSH with argument in arg
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'PUSH'})
        response = self.client.post(url, {'arg': 1009})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        computer.refresh_from_db()
        register = computer.register_set.get(address=0)
        self.assertEqual(register.value1, 'PUSH')
        self.assertEqual(register.value2, 1009)

    def test_insert_call(self):
        computer = Computer.create(100)
        computer.save()

        # insert CALL with argument in addr
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'CALL'})
        response = self.client.post(url, {'addr': 50})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        computer.refresh_from_db()
        register = computer.register_set.get(address=0)
        self.assertEqual(register.value1, 'CALL')
        self.assertEqual(register.value2, 50)

    def test_insert_invalid_operation(self):
        computer = Computer.create(100)
        computer.save()

        # insert invalid operation
        url = reverse('insert', kwargs={'computer_id': computer.id, 'operation': 'IVLD'})
        response = self.client.post(url, {'addr': 50})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
