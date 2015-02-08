# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0005_auto_20150201_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='letterhead',
            name='logo_height',
            field=models.IntegerField(default=50, help_text='Logo height in mm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='logo_width',
            field=models.IntegerField(default=70, help_text='Logo width in mm'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='letterhead',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letterhead',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letterhead',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
