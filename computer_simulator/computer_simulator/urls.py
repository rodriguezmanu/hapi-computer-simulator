# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from computer.views import computer_create, set_pointer, insert, execute

urlpatterns = [
    url(r'^v1/computers/?$', computer_create, name='computer_create'),
    url(r'^v1/computers/(?P<computer_id>[0-9]+)/stack/pointer/?$', set_pointer, name='set_pointer'),
    url(r'^v1/computers/(?P<computer_id>[0-9]+)/insert/(?P<operation>[A-Z]+)/?$', insert, name='insert'),
    url(r'^v1/computers/(?P<computer_id>[0-9]+)/exec/?$', execute, name='execute'),
]
