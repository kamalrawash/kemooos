# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('icon', models.ImageField(default=b'/media/news_icon.jpg', null=True, upload_to=b'course_icons', blank=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='paid',
        ),
        migrations.AddField(
            model_name='registrar',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
