# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160819_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='seats',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
