# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170103_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='demo',
            field=models.BooleanField(default=False),
        ),
    ]
