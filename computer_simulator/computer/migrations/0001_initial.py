# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack_pointer', models.IntegerField(default=0)),
                ('program_counter', models.IntegerField(default=0)),
                ('computation_ended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.IntegerField()),
                ('value1', models.CharField(max_length=50)),
                ('value2', models.IntegerField()),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.Computer')),
            ],
        ),
    ]
