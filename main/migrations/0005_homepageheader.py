# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160813_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_eng', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('discription_eng', models.CharField(max_length=255)),
                ('discription_ar', models.CharField(max_length=255)),
                ('image_eng', models.ImageField(null=True, upload_to=b'header', blank=True)),
                ('image_ar', models.ImageField(null=True, upload_to=b'header', blank=True)),
            ],
        ),
    ]
