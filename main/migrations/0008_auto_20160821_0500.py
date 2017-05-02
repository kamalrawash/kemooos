# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_course_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('bio_eng', models.CharField(max_length=255)),
                ('bio_ar', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'tutor image', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='tutor_ar',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tutor_eng',
        ),
    ]
