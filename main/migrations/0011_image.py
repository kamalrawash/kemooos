# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160821_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_eng', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'imageGallary', blank=True)),
            ],
        ),
    ]
