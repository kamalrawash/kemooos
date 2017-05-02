# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('goal_eng', models.TextField()),
                ('goal_ar', models.TextField()),
                ('conditions_eng', models.TextField()),
                ('conditions_ar', models.TextField()),
                ('venue_eng', models.CharField(max_length=255)),
                ('venue_ar', models.CharField(max_length=255)),
                ('tutor_eng', models.CharField(max_length=255)),
                ('tutor_ar', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('date_of_birth', models.DateField()),
                ('degree', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mailing_list', models.BooleanField()),
                ('address', models.TextField()),
                ('course', models.ForeignKey(to='main.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Subfield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('field', models.ForeignKey(to='main.Field')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subfield',
            field=models.ForeignKey(to='main.Subfield'),
        ),
    ]
