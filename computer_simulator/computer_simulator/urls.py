# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from computer.views import computer_create

urlpatterns = [
    url(r'^v1/computers/?$', computer_create, name='computer_create'),
]
