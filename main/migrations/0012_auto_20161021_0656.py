# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title_ar',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='title_eng',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrar',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
