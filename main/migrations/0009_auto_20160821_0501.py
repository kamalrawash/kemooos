# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160821_0500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Turor',
            new_name='Tutor',
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(blank=True, to='main.Tutor', null=True),
        ),
    ]
