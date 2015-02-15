# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0011_auto_20150215_1830'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LetterFile',
        ),
        migrations.AddField(
            model_name='contenttemplate',
            name='template_name',
            field=models.CharField(default='Test template', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 22, 22, 25, 364812, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 22, 22, 33, 653083, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='name',
            field=models.CharField(default='Test logo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 22, 22, 52, 14459, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='barcode',
            field=models.CharField(default='abc123', max_length=100),
            preserve_default=False,
        ),
    ]
