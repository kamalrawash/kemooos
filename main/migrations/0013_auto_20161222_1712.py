# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20161021_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body_ar',
            field=models.TextField(default=datetime.datetime(2016, 12, 22, 17, 12, 49, 473476, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_ar',
            field=models.CharField(default=datetime.datetime(2016, 12, 22, 17, 12, 57, 77477, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
