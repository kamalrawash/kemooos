# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160821_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tutor',
        ),
        migrations.AddField(
            model_name='tutor',
            name='course',
            field=models.ForeignKey(blank=True, to='main.Course', null=True),
        ),
    ]
