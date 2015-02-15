# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0010_auto_20150215_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='lettervariable',
            name='content_template',
            field=models.ManyToManyField(to='letters.ContentTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettervariable',
            name='variable_value',
            field=models.CharField(null=True, max_length=100, default='', blank=True),
            preserve_default=True,
        ),
    ]
