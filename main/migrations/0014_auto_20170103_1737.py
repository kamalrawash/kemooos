# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20161222_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='venue_ar',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='venue_eng',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
