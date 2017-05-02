# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='big_picture',
            field=models.ImageField(default=b'/media/course_big_picture.png', null=True, upload_to=b'course_big_picture', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.ImageField(default=b'/media/course_icon.jpg', null=True, upload_to=b'course_icons', blank=True),
        ),
    ]
