# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_homepageheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageheader',
            name='url_ar',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepageheader',
            name='url_eng',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
